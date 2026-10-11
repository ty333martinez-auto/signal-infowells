# Signal InfoWells

**Independent reasoning and activation framework with an integrated skills marketplace.**

Signal InfoWells examines situations through six reasoning pillars, cross-checks their outputs, preserves uncertainty, and supports proportionate action. Marketplace capabilities are operational tools, not additional reasoning pillars.

> **Foundational principle:** No single pillar is allowed to define reality alone.  
> **Status:** Experimental. Passing software checks is not proof of real-world reasoning efficacy.

## Start here
1. Read the [complete reasoning framework and cognitive trail](docs/reasoning-framework.md).
2. Read [ACTIVATION.md](ACTIVATION.md) and [HANDOFF.md](HANDOFF.md).
3. Activate capabilities from [marketplace.json](marketplace.json) by following `plugins/*/SKILL.md`.

## The six reasoning pillars
| Pillar | Core question |
|---|---|
| **Perception** | What is actually here and observable? |
| **Imagination** | What else could be possible? |
| **Empathy** | What may another person be experiencing or seeing? |
| **Introspection** | What is happening within me? |
| **Emotion** | What is moving within me, and what might that signal? |
| **Reason** | What follows from the evidence and premises? |

**Awareness** is foundational, not a seventh pillar. **Recognition** integrates and cross-checks the examination and is explicitly stated after sufficient examination. Whether Recognition is a distinct operation remains unresolved.

## Living cycle
`Awareness → Six Pillars / Cross-Check → Recognition → Action → Experience → Reflection → Awareness`

Cross-checking does not require agreement. “Don't know yet” is a valid result.

## Marketplace is a separate operational layer
The marketplace registers capabilities across categories such as Signal, Recognition, Evidence, Execution, Validation, and Provenance. These categories do not replace or expand the six reasoning pillars.

- `marketplace.json` — catalog.
- `plugins/*/SKILL.md` and `plugins/*/manifest.json` — capability instructions and metadata.
- `src/signal_infowells/` — read-only marketplace loader and bounded cycle/promotion-gate runtime.
- `.infowells/` — governance, protocols, and run registry.
- `.pmcro/trails/signal-infowells/` — PMCR-O-compatible trail; PMCR-O does not own the framework.
- `docs/reasoning-framework.md` — canonical framework guide.
- `docs/index.html` — public GitHub Pages guide.

## Bounded autonomous build
`siw-autonomous-build` supports bounded cycles: depth ≤ 4, iterations ≤ 8, steps ≤ 32, wall time ≤ 300 seconds. Automated gates may allow a cycle to continue; they are not independent review, PR approval, or efficacy validation.

Promotion to `main` requires an explicit user command for this change, successful checks on the exact head, sealed evidence/provenance, independent validation, and repository permission/branch-protection compliance. Never auto-promote.

## Conditional CapCut intent
For tasks that clearly require video production/editing, `siw-capcut-intent` can generate a portable task artifact under `.pmcro/tasks/capcut/`, using `schemas/capcut_intent.schema.json`. Unknowns stay unresolved rather than invented. Intent generation is not a rendered video export.

## Status labels
- **CONFIRMED** — independently validated within the stated scope.
- **NOT-YET-VERIFIED** — produced or recorded, but independent validation is pending.
- **NOT-RUN** — defined but not exercised.

A passed CI run proves only the properties covered by its checks.

## GitHub Pages
https://ty333martinez-auto.github.io/signal-infowells/  
The public guide is served from `/docs` on `main`; feature-branch changes are not live until promotion.

## License
Apache-2.0
