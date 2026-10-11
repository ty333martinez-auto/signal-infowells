"""Generate portable CapCut intent task records for external media execution."""
from __future__ import annotations
from datetime import datetime, timezone
import json
import re
from pathlib import Path
from typing import Any, Mapping

VIDEO_TERMS = {
    "capcut", "video", "reel", "reels", "shorts", "short video", "edit this video",
    "video edit", "video editing", "make a video", "create a video", "timeline",
    "transitions", "video captions", "video prompt", "youtube short", "tiktok video",
}

def requires_capcut_intent(task_text: str, explicit_signal: str | None = None) -> bool:
    """Return true only for an explicit video-production/editing signal."""
    if explicit_signal in {"video_creation", "video_editing", "reel_or_short",
                           "capcut_prompt", "timeline_editing",
                           "captions_or_transitions_for_video"}:
        return True
    text = (task_text or "").casefold()
    return any(term in text for term in VIDEO_TERMS)

def _nullable(value: Any) -> Any:
    if value is None or value == "":
        return None
    return value

def build_capcut_intent(task: Mapping[str, Any], *, producer: str = "signal-infowells") -> dict[str, Any]:
    """Build a portable task artifact without inventing missing user details."""
    objective = str(task.get("objective") or task.get("task_text") or "").strip()
    if not objective:
        raise ValueError("task must include a non-empty objective or task_text")
    task_id = str(task.get("task_id") or "capcut-task").strip().lower()
    task_id = re.sub(r"[^a-z0-9-]+", "-", task_id).strip("-")
    if len(task_id) < 3:
        task_id = f"capcut-{task_id or 'task'}"
    task_id = task_id[:80].rstrip("-")
    signal = task.get("source_signal") or "video_creation"
    intent = {
        "platform": _nullable(task.get("platform")),
        "audience": _nullable(task.get("audience")),
        "source_assets": list(task.get("source_assets") or []),
        "narrative_script": _nullable(task.get("narrative_script")),
        "visual_style": _nullable(task.get("visual_style")),
        "editing_instructions": list(task.get("editing_instructions") or []),
        "aspect_ratio": _nullable(task.get("aspect_ratio")),
        "target_duration_seconds": task.get("target_duration_seconds"),
        "audio": task.get("audio"),
        "captions": task.get("captions"),
        "deliverable": _nullable(task.get("deliverable")),
        "constraints": list(task.get("constraints") or []),
    }
    questions = list(task.get("unresolved_questions") or [])
    for key, question in (
        ("platform", "Which platform or placement is this video for?"),
        ("audience", "Who is the intended audience?"),
        ("source_assets", "Which footage, images, logos, or other source assets should be used?"),
        ("narrative_script", "Is there an approved script or should the executing AI draft one?"),
        ("aspect_ratio", "What aspect ratio is required?"),
        ("target_duration_seconds", "What target duration should the export meet?"),
        ("deliverable", "What exact export format and deliverable are required?"),
    ):
        if intent[key] is None or intent[key] == []:
            if question not in questions:
                questions.append(question)
    portable_prompt = _portable_prompt(objective, intent, questions)
    return {
        "task_id": task_id,
        "task_type": "capcut_intent",
        "framework": "signal-infowells",
        "status": "NOT-YET-VERIFIED",
        "created_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "objective": objective,
        "activation": {
            "capability": "siw-capcut-intent",
            "external_execution": "handoff_only",
            "source_signal": str(signal),
        },
        "intent": intent,
        "portable_prompt": portable_prompt,
        "acceptance_checks": list(task.get("acceptance_checks") or [
            "Output is created/exported; intent generation alone does not satisfy this check.",
            "Export aspect ratio and duration match the specified requirements.",
            "Audio and captions match the specified intent when requested.",
            "No unsupported claims or invented source assets were added.",
            "Executor reports blockers and observable output evidence.",
        ]),
        "unresolved_questions": questions,
        "provenance": {
            "source_task": _nullable(task.get("source_task")),
            "producer": producer,
            "evidence_note": "Intent artifact generated from supplied task fields; no CapCut execution or export is implied.",
        },
    }

def _portable_prompt(objective: str, intent: Mapping[str, Any], questions: list[str]) -> str:
    def show(value: Any) -> str:
        return "UNKNOWN — ask before assuming" if value is None or value == [] else json.dumps(value, ensure_ascii=False)
    fields = [
        ("Objective", objective),
        ("Platform", intent["platform"]),
        ("Audience", intent["audience"]),
        ("Source assets", intent["source_assets"]),
        ("Narrative/script", intent["narrative_script"]),
        ("Visual style", intent["visual_style"]),
        ("Editing instructions", intent["editing_instructions"]),
        ("Aspect ratio", intent["aspect_ratio"]),
        ("Target duration (seconds)", intent["target_duration_seconds"]),
        ("Audio", intent["audio"]),
        ("Captions", intent["captions"]),
        ("Deliverable", intent["deliverable"]),
        ("Constraints", intent["constraints"]),
    ]
    brief = "\n".join(f"- **{name}:** {show(value)}" for name, value in fields)
    questions_text = "\n".join(f"- {question}" for question in questions) or "- None recorded"
    return (
        "You are executing a portable Signal InfoWells CapCut intent. Create/edit the video; "
        "do not claim to have edited or exported anything until you have observable evidence. "
        "Use only supplied assets and grounded claims. Ask about blockers instead of inventing details.\n\n"
        f"## Mission\n{brief}\n\n## Unresolved questions\n{questions_text}\n\n"
        "## Execution and return requirements\n"
        "Inspect assets available to you, implement the requested timeline/edit, check aspect ratio, duration, "
        "audio and captions against the brief, export the deliverable if your tools allow it, and return the actual "
        "output location, settings, passed/failed acceptance checks, blockers, and observable evidence. "
        "If you cannot operate CapCut or access the assets, say so and provide the next actionable step."
    )

def write_pmcr_task(task: Mapping[str, Any], root: str | Path = ".") -> Path:
    """Write the intent artifact to the PMCR-O task handoff directory."""
    record = build_capcut_intent(task)
    output_dir = Path(root) / ".pmcro" / "tasks" / "capcut"
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{record['task_id']}.json"
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing intent task: {output}")
    output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return output
