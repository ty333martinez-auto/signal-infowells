# HANDOFF — Signal InfoWells

**Repository:** https://github.com/ty333martinez-auto/signal-infowells

## Identity
Signal InfoWells is the reasoning/activation framework and integrated skills marketplace. It is independent of PMCR-O; PMCR-O-compatible trails record work but do not own SIW.

## Current architecture
- Reasoning core: Perception, Imagination, Empathy, Introspection, Emotion, Reason.
- Recognition: continuous integration/cross-checking; its distinctness and role remain unresolved.
- Operational marketplace: capability skills catalogued in marketplace.json and implemented as plugins/*/SKILL.md.
- Runtime: src/signal_infowells/ loads the marketplace and evaluates bounded build-cycle and promotion gates.
- Governance and bounds: .infowells/.
- PMCR-O-compatible evidence trails: .pmcro/trails/signal-infowells/.

## Autonomous build lifecycle
Receive → Identify → Gather → Apply → Test → Resolve → Refine → Record → Validate → Commit → Push → Promotion Gate.

Automated cycle approval permits continuation when required gates pass. It is not independent validation or PR approval. Promotion to main requires an explicit user command for the current change, successful checks on the exact revision, sealed evidence/provenance, independent validation, and repository permission/branch-protection compliance.

## Protected invariants
1. No single pillar defines reality alone.
2. Recognition remains continuous and unresolved.
3. Process success is not real-world efficacy.
4. Promotion requires independent validation outside the producing path.
5. Evidence must be sealed with digest and provenance.
6. CONFIRMED, NOT-YET-VERIFIED, and NOT-RUN remain distinct.

## Bounds
Depth <= 4; iterations <= 8; total steps <= 32; wall time <= 300 seconds. Do not increase without governance change and independent review.

## Current work
- Working branch: feature/autonomous-build-cycle-001
- Added bounded cycle gate, marketplace loader, autonomous-build skill/manifest, protocol, catalog registration, tests, and CI workflow.
- Run tests: python -m unittest discover -s tests -v
- Run repository integrity: python tools/validate_marketplace.py
- Changes are NOT-YET-VERIFIED until independently reviewed.
- Do not self-approve or merge without the promotion gate and the user's explicit command.

## Next steps
1. Inspect CI results on the final PR head.
2. Review the runtime, catalog, and promotion gate independently.
3. Resolve any CI or review findings with bounded cycles.
4. Only promote after explicit user command and all promotion requirements are satisfied.
