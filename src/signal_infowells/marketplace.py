"""Read-only loader for the Signal InfoWells marketplace catalog."""
from __future__ import annotations
from dataclasses import dataclass
import json
from pathlib import Path

class MarketplaceError(ValueError):
    """Raised when the marketplace catalog cannot be safely loaded."""

@dataclass(frozen=True)
class Capability:
    name: str
    source: str
    description: str
    pillar: str

@dataclass(frozen=True)
class Marketplace:
    name: str
    version: str
    framework: str
    status: str
    capabilities: tuple[Capability, ...]
    invariants: tuple[str, ...]

def load_marketplace(root: str | Path) -> Marketplace:
    """Load catalog metadata and verify every capability resolves to SKILL.md.

    Plugin content is not executed by the loader; activation remains an explicit
    orchestrator action.
    """
    base = Path(root).resolve()
    catalog_path = base / "marketplace.json"
    try:
        data = json.loads(catalog_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise MarketplaceError(f"cannot load marketplace.json: {exc}") from exc
    if not isinstance(data, dict) or data.get("framework") != "signal-infowells":
        raise MarketplaceError("catalog must identify framework 'signal-infowells'")
    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        raise MarketplaceError("catalog plugins must be a non-empty list")
    capabilities: list[Capability] = []
    seen_names: set[str] = set()
    for index, plugin in enumerate(plugins):
        if not isinstance(plugin, dict):
            raise MarketplaceError(f"plugins[{index}] must be an object")
        name, source = plugin.get("name"), plugin.get("source")
        if not isinstance(name, str) or not name.strip():
            raise MarketplaceError(f"plugins[{index}].name must be non-empty")
        if name in seen_names:
            raise MarketplaceError(f"duplicate capability name: {name}")
        seen_names.add(name)
        if not isinstance(source, str) or not source.strip():
            raise MarketplaceError(f"{name}: source must be non-empty")
        target = (base / source).resolve()
        if not target.is_relative_to(base):
            raise MarketplaceError(f"{name}: source escapes repository root")
        if not (target / "SKILL.md").is_file():
            raise MarketplaceError(f"{name}: missing SKILL.md at {source}")
        capabilities.append(Capability(
            name=name, source=source,
            description=str(plugin.get("description", "")),
            pillar=str(plugin.get("pillar", "")),
        ))
    invariants = data.get("invariants")
    if not isinstance(invariants, list) or not invariants:
        raise MarketplaceError("catalog invariants must be a non-empty list")
    return Marketplace(
        name=str(data.get("name", "")), version=str(data.get("version", "")),
        framework="signal-infowells", status=str(data.get("status", "NOT-RUN")),
        capabilities=tuple(capabilities),
        invariants=tuple(str(item) for item in invariants),
    )
