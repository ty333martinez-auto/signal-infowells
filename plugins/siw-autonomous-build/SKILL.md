---
name: siw-autonomous-build
description: Coordinate bounded framework and marketplace build cycles with automatic quality gates and command-gated promotion.
pillar: Execution
status: NOT-RUN
framework: signal-infowells
---

# Autonomous Build Cycle

**Framework:** Signal InfoWells  
**Capability status:** NOT-RUN until exercised in a recorded activation

## Purpose
Build and refine the framework and its marketplace through bounded, evidence-backed cycles. This capability belongs to Signal InfoWells; PMCR-O may retain the trail but does not own the framework.

## Cycle
1. Receive the user's explicit task and promotion scope.
2. Read AGENTS.md, HANDOFF.md, marketplace catalog, governance invariants, bounds, and latest run trail.
3. Identify candidate signals and affected capabilities. Preserve the separation between the reasoning core and operational skills.
4. Gather current repository evidence and establish acceptance criteria before edits.
5. Apply the smallest coherent change on a working branch.
6. Run regression tests, marketplace integrity checks, invariant checks, and applicable integration checks.
7. Automatically approve a cycle to continue only when all required gates pass, the evidence digest is sealed, and execution bounds are respected. If a gate fails, record blockers and refine within the remaining budget.
8. Record the diff, commands, actual results, digest, provenance, status, and unresolved questions.
9. Commit and push the reviewable branch when repository write access is available.
10. If the task clearly requires video creation or editing, activate `siw-capcut-intent` and emit a portable task JSON under `.pmcro/tasks/capcut/`; do not create CapCut tasks for unrelated work.
11. Promote to main only when the user's command explicitly covers that promotion and the independent-validation gate is satisfied. If either condition is missing, stop at the reviewable branch/PR.

## Automatic approval semantics
- Cycle approval means the automated quality gates permit the build loop to continue.
- It does not mean an independent reviewer approved the change, that a pull request is approved, or that a claim is CONFIRMED.
- The producing path cannot validate itself as independent.
- Never fabricate GitHub review approvals, bypass branch protection, or merge around failed checks.
- A green test is not evidence of real-world efficacy.

## Hard bounds
- max_depth = 4
- max_iterations = 8
- max_total_steps = 32
- Stop and record partial output when any bound is reached.

## Protected invariants
1. No single pillar defines reality alone.
2. Recognition remains continuous and unresolved.
3. Process success is not real-world efficacy.
4. Promotion requires independent validation.
5. Evidence must be sealed with digest and provenance.
6. CONFIRMED, NOT-YET-VERIFIED, and NOT-RUN remain distinct.

## Required output
A registry record and PMCR-O-compatible cognitive trail containing the run ID, task/evidence digests, branch and commits, commands and test results, cycle approvals, independent-validation state, promotion authorization, unresolved questions, and halt reason.

## Non-goals
- Does not automatically promote itself to CONFIRMED.
- Does not bypass repository protection or user authorization.
- Does not claim that a commit, push, or successful test proves reasoning quality or real-world efficacy.
