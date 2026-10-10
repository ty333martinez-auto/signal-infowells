---
name: siw-signal
description: Detect and prioritize candidate signals from a task. Does not rank truth.
pillar: Signal
status: NOT-RUN
framework: signal-infowells
---

# Signal Detect

**Pillar:** Signal  
**Framework:** Signal InfoWells (independent activation marketplace)  
**Status of this skill package:** NOT-RUN until exercised in a recorded activation

## When to use
When receiving a new task and identifying inputs that matter.

## Steps
1. Read the task text as given.
2. Extract candidate signals (named entities, constraints, goals, risks).
3. List signals without claiming which are true or final.
4. Hand off a signal list labeled NOT-YET-VERIFIED.

## Protected invariants (always)
1. No single pillar defines reality alone.
2. Recognition is continuous and unresolved.
3. A successful software/process check is not proof of real-world outcome improvement.
4. Promotion requires independent validation outside the originating path.
5. Evidence must be sealed before it can influence promotion.
6. CONFIRMED / NOT-YET-VERIFIED / NOT-RUN stay distinct.

## Output
- Structured notes suitable for a run record
- Explicit status label (default NOT-YET-VERIFIED)
- Unresolved questions left open when Recognition is involved

## Non-goals
- Does not subordinate Signal InfoWells to any other marketplace
- Does not auto-promote to CONFIRMED
- Does not claim real-world efficacy from process success alone
