#!/usr/bin/env python3
"""Create a PMCR-O CapCut intent task from a JSON task description."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from src.signal_infowells.capcut_intent import requires_capcut_intent, write_pmcr_task

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task_json", help="Path to JSON containing task_text/objective and optional intent fields")
    parser.add_argument("--root", default=".", help="Repository/workspace root for PMCR-O task output")
    args = parser.parse_args()
    task_path = Path(args.task_json)
    try:
        task = json.loads(task_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        parser.error(f"cannot read task JSON: {exc}")
    task_text = str(task.get("task_text") or task.get("objective") or "")
    signal = task.get("source_signal")
    if not requires_capcut_intent(task_text, signal):
        print("No CapCut intent created: task has no explicit video-production signal.")
        return 2
    output = write_pmcr_task(task, args.root)
    print(f"Created PMCR-O CapCut intent: {output}")
    print("The artifact is a portable handoff, not a completed video export.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
