#!/usr/bin/env python3
"""Dependency-free integrity checks for the Signal InfoWells skill marketplace."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED_INVARIANTS = {
    "no_single_pillar_defines_reality",
    "recognition_continuous_unresolved",
    "software_test_neq_real_world_efficacy",
    "promotion_requires_independent_validation",
    "evidence_must_be_sealed",
    "status_labels_remain_distinct",
}
VALID_STATUSES = {"CONFIRMED", "NOT-YET-VERIFIED", "NOT-RUN"}


def _read_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: cannot read valid JSON ({exc})")
        return None


def _frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{path}: cannot read skill ({exc})")
        return {}
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\s|\Z)", content, re.DOTALL)
    if not match:
        errors.append(f"{path}: missing YAML frontmatter delimiters")
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        item = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if item:
            fields[item.group(1)] = item.group(2).strip().strip('"').strip("'")
    return fields


def validate_marketplace(root: Path) -> list[str]:
    """Return all detectable marketplace/catalog consistency errors."""
    root = root.resolve()
    errors: list[str] = []
    catalog = _read_json(root / "marketplace.json", errors)
    if not isinstance(catalog, dict):
        return errors or ["marketplace.json: expected a JSON object"]

    if catalog.get("framework") != "signal-infowells":
        errors.append("marketplace.json: framework must be 'signal-infowells'")

    invariants = catalog.get("invariants")
    if not isinstance(invariants, list):
        errors.append("marketplace.json: invariants must be a list")
    else:
        missing = sorted(REQUIRED_INVARIANTS - set(invariants))
        if missing:
            errors.append("marketplace.json: missing required invariants: " + ", ".join(missing))

    plugins = catalog.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        errors.append("marketplace.json: plugins must be a non-empty list")
        return errors

    seen_names: set[str] = set()
    seen_sources: set[str] = set()
    for index, plugin in enumerate(plugins):
        label = f"marketplace.json: plugins[{index}]"
        if not isinstance(plugin, dict):
            errors.append(f"{label} must be an object")
            continue
        name, source = plugin.get("name"), plugin.get("source")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{label}.name must be a non-empty string")
            continue
        if name in seen_names:
            errors.append(f"{label}.name duplicates '{name}'")
        seen_names.add(name)

        if not isinstance(source, str) or not source.strip():
            errors.append(f"{label}.source must be a non-empty string")
            continue
        if source in seen_sources:
            errors.append(f"{label}.source duplicates '{source}'")
        seen_sources.add(source)

        source_path = (root / source).resolve()
        if not source_path.is_relative_to(root):
            errors.append(f"{label}.source escapes repository root: {source}")
            continue
        skill_path = source_path / "SKILL.md"
        if not source_path.is_dir():
            errors.append(f"{label}.source directory is missing: {source}")
            continue
        if not skill_path.is_file():
            errors.append(f"{label} has no SKILL.md at {source}/SKILL.md")
            continue

        fields = _frontmatter(skill_path, errors)
        if fields.get("name") != name:
            errors.append(f"{skill_path}: frontmatter name {fields.get('name')!r} does not match catalog name {name!r}")
        if fields.get("framework") != "signal-infowells":
            errors.append(f"{skill_path}: framework must be 'signal-infowells'")
        if fields.get("status") and fields["status"] not in VALID_STATUSES:
            errors.append(f"{skill_path}: unsupported status {fields['status']!r}")

    schema_path = root / ".infowells" / "registry" / "run_registry.schema.json"
    schema = _read_json(schema_path, errors)
    if isinstance(schema, dict):
        status_enum = schema.get("properties", {}).get("status", {}).get("enum")
        if set(status_enum or []) != VALID_STATUSES:
            errors.append(f"{schema_path}: status enum must preserve exactly {sorted(VALID_STATUSES)}")
    return errors


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    root = Path(args[0]) if args else Path(__file__).resolve().parents[1]
    errors = validate_marketplace(root)
    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        print(f"Marketplace validation failed: {len(errors)} issue(s).")
        return 1
    print("[PASS] Catalog, skill references/frontmatter, invariants, and registry statuses are consistent.")
    print("Scope: repository integrity only; this does not validate reasoning quality or real-world efficacy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
