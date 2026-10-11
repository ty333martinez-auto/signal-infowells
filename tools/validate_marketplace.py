#!/usr/bin/env python3
"""Dependency-free repository integrity checks for Signal InfoWells."""
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

def _json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: invalid or unreadable JSON ({exc})")
        return None

def _frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{path}: unreadable skill ({exc})")
        return {}
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\s|\Z)", text, re.DOTALL)
    if not match:
        errors.append(f"{path}: missing YAML frontmatter")
        return {}
    return {m.group(1): m.group(2).strip().strip('"').strip("'")
            for line in match.group(1).splitlines()
            if (m := re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", line))}

def validate_marketplace(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    catalog = _json(root / "marketplace.json", errors)
    if not isinstance(catalog, dict):
        return errors or ["marketplace.json must be an object"]
    if catalog.get("framework") != "signal-infowells":
        errors.append("marketplace.json: wrong framework identity")
    invariants = catalog.get("invariants")
    if not isinstance(invariants, list):
        errors.append("marketplace.json: invariants must be a list")
    elif REQUIRED_INVARIANTS - set(invariants):
        errors.append("marketplace.json: required framework invariants are missing")
    plugins = catalog.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        errors.append("marketplace.json: plugins must be a non-empty list")
        return errors
    names: set[str] = set()
    sources: set[str] = set()
    for i, plugin in enumerate(plugins):
        label = f"marketplace.json plugins[{i}]"
        if not isinstance(plugin, dict):
            errors.append(f"{label}: expected object")
            continue
        name, source = plugin.get("name"), plugin.get("source")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{label}: name must be non-empty")
            continue
        if name in names:
            errors.append(f"{label}: duplicate name {name!r}")
        names.add(name)
        if not isinstance(source, str) or not source.strip():
            errors.append(f"{label}: source must be non-empty")
            continue
        if source in sources:
            errors.append(f"{label}: duplicate source {source!r}")
        sources.add(source)
        directory = (root / source).resolve()
        if not directory.is_relative_to(root):
            errors.append(f"{label}: source escapes repository root")
            continue
        skill = directory / "SKILL.md"
        manifest_path = directory / "manifest.json"
        if not directory.is_dir() or not skill.is_file():
            errors.append(f"{label}: missing capability directory or SKILL.md ({source})")
            continue
        fields = _frontmatter(skill, errors)
        if fields.get("name") != name:
            errors.append(f"{skill}: frontmatter name does not match catalog name {name!r}")
        if fields.get("framework") != "signal-infowells":
            errors.append(f"{skill}: wrong framework identity")
        if fields.get("status") and fields["status"] not in VALID_STATUSES:
            errors.append(f"{skill}: invalid status {fields['status']!r}")
        if manifest_path.is_file():
            manifest = _json(manifest_path, errors)
            if isinstance(manifest, dict) and (manifest.get("name") != name or manifest.get("framework") != "signal-infowells"):
                errors.append(f"{manifest_path}: name/framework mismatch")
    docs_path = root / "docs" / "index.html"
    try:
        docs = docs_path.read_text(encoding="utf-8")
        for phrase in ("Perception", "Imagination", "Empathy", "Introspection", "Emotion", "Reason",
                       "Recognition", "siw-capcut-intent", ".pmcro/tasks/capcut/"):
            if phrase not in docs:
                errors.append(f"{docs_path}: public framework docs missing required concept {phrase!r}")
        if "Twelve plugins" in docs or "Twelve plugins." in docs:
            errors.append(f"{docs_path}: stale marketplace capability count")
    except OSError as exc:
        errors.append(f"{docs_path}: public framework docs missing or unreadable ({exc})")

    schema_path = root / ".infowells" / "registry" / "run_registry.schema.json"
    schema = _json(schema_path, errors)
    if isinstance(schema, dict):
        status_enum = schema.get("properties", {}).get("status", {}).get("enum")
        if set(status_enum or []) != VALID_STATUSES:
            errors.append(f"{schema_path}: status vocabulary must remain exactly {sorted(VALID_STATUSES)}")
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
    print("[PASS] Marketplace catalog, capability files, framework invariants, and status vocabulary are consistent.")
    print("Scope: repository integrity only; this does not validate reasoning quality or real-world efficacy.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
