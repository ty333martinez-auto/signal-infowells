# .pmcro — PMCR-O loop interface for Signal InfoWells

This folder lets a **PMCR-O colony loop** observe and trail work on **Signal InfoWells** without subordinating Signal InfoWells to PMCR-O.

- **Signal InfoWells identity** remains independent (marketplace skills under `plugins/`, governance under `.infowells/`).
- **This `.pmcro/` tree** is the trail / cycle interface so your loop can Plan → Make → Check → Reflect → Seal against this repo and this session.

## Layout

| Path | Purpose |
|------|---------|
| `agents/*.md` | Phase contracts scoped to SIW |
| `trails/<subject>/<trailId>/` | Sealed phase frames |
| `CYCLE-LOG.md` | Human-readable cycle index |
| `instance.yaml` | Instance identity + trail location |
| `hil/README.md` | HIL notes |
| `handoffs/signal-infowells/` | Pointers to SIW docs |

## Domain

**Subject:** Signal InfoWells marketplace framework  
**Repo:** https://github.com/ty333martinez-auto/signal-infowells  
**Not:** a PMCR-O skill product — SIW is its own activation framework.
