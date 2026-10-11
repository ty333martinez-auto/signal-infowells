---
name: siw-capcut-intent
description: Detect video-creation/editing needs and produce portable CapCut intent task artifacts for PMCR-O handoff to another capable AI.
pillar: Execution
status: NOT-RUN
framework: signal-infowells
---

# CapCut Intent — External Media Handoff

## Purpose
When a task requires creating or editing video, generate a structured, tool-agnostic CapCut intent artifact. The artifact is activated through Signal InfoWells and recorded under `.pmcro/tasks/capcut/` so another AI or a human can execute it in CapCut or a compatible video tool.

## Activation signals
Activate only when the user's task requests video/reel/short creation, video editing, a CapCut prompt, captions, transitions, timeline editing, or other clearly video-production work. Do not emit a CapCut task for unrelated framework, reasoning, writing, or image-only work.

## Required lifecycle
1. Identify the requested media outcome and intended platform/audience if supplied.
2. Gather source assets and constraints explicitly available in the task or referenced artifacts.
3. Preserve unknowns as `null` or list them under `unresolved_questions`; do not invent campaign facts, footage, brand assets, claims, or user preferences.
4. Generate a canonical CapCut intent JSON conforming to `schemas/capcut_intent.schema.json`.
5. Include a portable execution prompt another AI can use without requiring Signal InfoWells runtime access.
6. Record the intent as a PMCR-O task artifact at `.pmcro/tasks/capcut/<task_id>.json` with provenance and acceptance checks.
7. Return the artifact path, summary, and activation instruction to the user.

## Portability
The task must describe the desired outcome, not assume a specific AI vendor or hidden connector. It can be handed to a capable AI, CapCut operator, or other video editor. Do not claim to operate CapCut directly unless that interaction actually occurred.

## Required intent fields
Objective; platform; audience; source assets; narrative/script; visual style; editing instructions; aspect ratio; target duration; audio; captions; deliverable; acceptance checks; constraints; unresolved questions; and a portable prompt.

## Status and limits
- Newly generated task: `NOT-YET-VERIFIED` until reviewed and executed.
- Intent generation is not video rendering and does not prove that a video exists.
- Never mark an external deliverable complete without evidence.
- Keep the six reasoning pillars and Recognition invariants intact.
