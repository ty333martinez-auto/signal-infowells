# AGENTS.md — Signal InfoWells

Instructions for any coding agent (human or AI) working inside this repository.

## Identity

You are operating inside **Signal InfoWells**, an independent activation framework.
It is **not** a skill or product inside any other marketplace. Do not re-frame it as such.

## Protected Invariants (Never Violate)

1. No single pillar defines reality alone.
2. Recognition is continuous and unresolved; never treat it as finished.
3. A green software test is **not** evidence that the framework improves real-world outcomes.
4. Promotion of any capability, claim, or configuration requires independent validation.
5. Evidence must be sealed (digest + provenance) before it can influence promotion decisions.
6. Keep three statuses distinct: **CONFIRMED**, **NOT-YET-VERIFIED**, **NOT-RUN**.

## Working Rules

- Prefer small, reviewable changes.
- Every new capability or protocol change must update the run registry schema if it affects recorded runs.
- When adding tests, mark what they actually prove (unit correctness ≠ real-world efficacy).
- Do not collapse "not-yet-verified" into "confirmed."
- Do not invent promotion authority. Promotion is gated by independent validation.

## Activation Lifecycle (Must Follow)

```
Receive task
→ Identify signals
→ Dispatch candidate capabilities
→ Execute
→ Test
→ Refine within bounded cycles
→ Record evidence, changes, and unresolved questions
→ Require independent validation before promotion
```

Bounded cycles: maximum recursion depth and iteration limits are defined in `.infowells/protocols/bounded_recursive_execution.md`. Never remove or raise those bounds without an explicit governance change and independent review.

## File Ownership

| Path | Purpose |
|------|---------|
| `.infowells/` | Governance, activation, protocols, registry — treat as constitution |
| `src/signal_infowells/` | Framework implementation |
| `configs/` | Manifests and runtime configuration |
| `tests/` | Unit and protocol tests |
| `web/` | Landing page (deep-teal, responsive) |
| `docs/` | Design and handoff documents |
| `prompts/` | Media / CapCut prompts |
| `AGENTS.md` | This file |
| `HANDOFF.md` | Single entry point for continuation |

## Adding a Capability

1. Place code under `src/signal_infowells/marketplace/` (or appropriate subpackage).
2. Add a manifest entry under `configs/capabilities/`.
3. Write unit tests that clearly state what is proven.
4. Record a run in the registry with status **NOT-YET-VERIFIED**.
5. Do **not** mark as promoted until independent validation is recorded.

## Recognition Guidance

When the system surfaces a "recognition" event:

- Record it.
- Do not treat the recognition itself as confirmation of truth.
- Leave the continuous role of Recognition open; do not close it in code or documentation.

## Handoff

If you must stop work, update `HANDOFF.md` with:

- Current branch / commit
- What is CONFIRMED vs NOT-YET-VERIFIED vs NOT-RUN
- Open questions
- Exact next steps for the next agent

Then point the next agent at the repository URL and this file.
