# Signal InfoWells

**Independent Reasoning Framework + Integrated Skills Marketplace**

Signal InfoWells is the framework. Its marketplace is an integrated capability layer used to dispatch and activate skills under the framework's governance. It is independent of PMCR-O and any other marketplace.

The experimental runtime under `src/signal_infowells/` provides a read-only marketplace loader and bounded build-cycle/promotion-gate decisions. Activatable procedures remain in `plugins/*/SKILL.md`; the catalog lives in `marketplace.json`; governance lives in `.infowells/`.

> **Experimental** — Passing software checks is not proof of reasoning quality or real-world outcome improvement.

## Autonomous build lifecycle

Receive → Identify → Gather → Apply → Test → Resolve → Refine → Record → Validate → Commit → Push → Promotion Gate.

The framework can automatically approve a bounded cycle to continue when its required quality gates pass. That is not the same as independent review, GitHub PR approval, or promotion to `main`.

Promotion to `main` requires an explicit user command for the current change, passing checks on the exact revision, sealed evidence/provenance, independent validation outside the producing path, and compliance with repository permissions and branch protection. When a gate is missing, stop at the working branch/PR and record `NOT-YET-VERIFIED`.

Default execution bounds: depth ≤ 4, iterations ≤ 8, total steps ≤ 32, wall time ≤ 300 seconds. Bounds may only be raised through governance change and independent review.

## Six reasoning pillars

**No single pillar defines reality alone.**

| Pillar | Examination |
|---|---|
| Perception | What is actually here? |
| Imagination | What else could be possible? |
| Empathy | What may another person be experiencing or seeing? |
| Introspection | What is happening within me? |
| Emotion | What is moving within me, and what might that signal? |
| Reason | What follows logically, and what does not? |

Recognition remains continuous and unresolved. The operational marketplace layers (Signal, Recognition, Evidence, Execution, Validation, Provenance) support the framework; they do not replace or redefine the six reasoning pillars.

## Marketplace capabilities

The canonical catalog is `marketplace.json`. Each capability has a `plugins/<name>/SKILL.md` and a manifest. The autonomous-build capability is `siw-autonomous-build`.

## Development checks

Run the dependency-free test suite and marketplace integrity gate:

```sh
python -m unittest discover -s tests -v
python tools/validate_marketplace.py
```

These checks establish only the properties they explicitly test. They do not establish real-world efficacy.

## Status labels

`CONFIRMED` · `NOT-YET-VERIFIED` · `NOT-RUN` — never collapse.

## GitHub Pages

https://ty333martinez-auto.github.io/signal-infowells/

## License

Apache-2.0
