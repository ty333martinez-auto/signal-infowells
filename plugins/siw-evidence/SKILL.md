---
name: siw-evidence
description: Seal observations into digests with provenance. Sealing is not promotion.
pillar: Evidence
status: NOT-RUN
framework: signal-infowells
---

# Evidence Seal

**Pillar:** Evidence  
**Framework:** Signal InfoWells (independent activation marketplace)  
**Status of this skill package:** NOT-RUN until exercised in a recorded activation

## When to use
When recording observations or results that must be sealed before promotion influence.

## Steps
1. Collect the payload to seal (task, result, or observation).
2. Produce a deterministic content digest (e.g. SHA-256 of canonical form).
3. Attach provenance (agent, capability, parent run if any).
4. Label status NOT-YET-VERIFIED until independent validation.

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
