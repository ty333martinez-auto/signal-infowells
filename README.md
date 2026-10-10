# Signal InfoWells

**Independent Activation Framework & Marketplace**

Signal InfoWells is a **standalone** activation framework with a **skills/plugins marketplace**.
You build by activating marketplace skills — not by running a framework Python package.

It is **not** subordinated to PMCR-O or any other system. The same generic pattern (skills + plugins + manifests + catalog) is used so agents can activate capabilities; governance and identity are Signal InfoWells.

> **Experimental** — Process success is **not** proof of real-world outcome improvement.

## How you build with it

1. Open this repo (or point an agent at it).
2. Read **ACTIVATION.md** and paste the activation prompt into your agent.
3. Dispatch skills from **plugins/** listed in **marketplace.json**.
4. Follow the activation lifecycle; keep status labels distinct.
5. Never auto-promote — independent validation required.

## Six Pillars

**No single pillar defines reality alone.**

| Pillar | Marketplace plugins |
|--------|---------------------|
| **Signal** | `siw-signal` |
| **Recognition** | `siw-recognition` |
| **Evidence** | `siw-evidence`, `siw-baseline`, `siw-task-digest` |
| **Execution** | `siw-execution`, `siw-refine`, `siw-echo` |
| **Validation** | `siw-validation`, `siw-status` |
| **Provenance** | `siw-provenance`, `siw-run-record` |

## Marketplace layout

```
marketplace.json           # Catalog of all plugins
plugins/*/SKILL.md         # Activatable skills
plugins/*/manifest.json    # Skill metadata
configs/capabilities/      # YAML pointers
.infowells/                # Governance
ACTIVATION.md              # Copy-paste activation prompt
```

## Status labels

CONFIRMED | NOT-YET-VERIFIED | NOT-RUN — never collapsed.

## GitHub Pages

Settings → Pages → branch `main` → folder `/docs`

https://ty333martinez-auto.github.io/signal-infowells/

## License

Apache-2.0
