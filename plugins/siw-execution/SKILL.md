---
name: siw-execution
description: Execute under bounded recursive limits. Halting on bounds is correct protocol.
pillar: Execution
status: NOT-RUN
framework: signal-infowells
---

# Bounded Execute

**Pillar:** Execution  
**Framework:** Signal InfoWells (independent activation marketplace)  
**Status of this skill package:** NOT-RUN until exercised in a recorded activation

## When to use
When performing action steps under Signal InfoWells bounds.

## Steps
1. Read bounds: max_depth=4, max_iterations=8, max_total_steps=32 (defaults).
2. Increment depth/iteration/step counters on entry.
3. If any bound is reached, halt and record partial results + unresolved questions.
4. Never disable counters. Halting is not failure.

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
