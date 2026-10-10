# Autonomous Build Cycle Protocol

## Identity
Signal InfoWells is the framework and marketplace. The marketplace is part of the SIW system, not a PMCR-O product. PMCR-O-compatible files may record the trail; they do not transfer ownership of SIW.

## Default cycle
Receive → Identify → Gather → Apply → Test → Resolve → Refine → Record → Validate → Commit → Push → Promotion Gate.

## Cycle auto-approval
A cycle may be automatically approved to continue when:
- All explicit acceptance checks pass.
- Required tests pass and their scope is stated.
- Core invariants are preserved.
- Evidence has a recomputable SHA-256 digest and provenance.
- The run is within depth 4, iterations 8, steps 32, and the configured wall-time limit.
- Failures, conflicts, and unresolved questions are recorded.

A failed check blocks cycle approval. The controller may refine within remaining bounds; it must halt when bounds are exhausted.

## Promotion gate
Automatic cycle approval is not PR approval or promotion. Promotion to main requires all of:
1. An explicit user command that authorizes promotion for the current change.
2. Successful required checks on the exact head revision.
3. Sealed evidence and provenance.
4. Independent validation by a path/person distinct from the producer.
5. No unresolved blocking failures or governance conflicts.
6. Repository permissions and branch protections permit the action.

If any requirement is absent, keep the change on its branch and record NOT-YET-VERIFIED. Never fake review events, self-approve as an independent validator, disable protections, or merge around failing checks.

## Git lifecycle
- Inspect repository instructions and current status before editing.
- Use a named working branch and small commits.
- Push the branch and open/update a PR for review.
- Re-run checks after the last change; validation evidence must refer to the current head.
- Merge only after the promotion gate is satisfied and the user's command covers the merge.
- Record the merge commit and verify main after promotion.

## Registry and cognitive trail
Record task digest, run ID, parent run, branch, before/after commits, changed files, commands, actual test outputs, evidence digest, automated cycle-gate decisions, independent validator identity/result, user-command scope, promotion result, unresolved questions, and halt reason.

## Bounds
max_depth=4, max_iterations=8, max_total_steps=32, max_wall_time_sec=300. Never increase these without a separate governance change and independent review.
