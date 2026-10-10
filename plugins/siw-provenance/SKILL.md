---
name: siw-provenance
description: Record chain of custody for claims and changes.
pillar: Provenance
status: NOT-RUN
framework: signal-infowells
---

# Provenance Track

**Pillar:** Provenance  
**Framework:** Signal InfoWells (independent activation marketplace)  
**Status of this skill package:** NOT-RUN until exercised in a recorded activation

## When to use
On every recorded step or claim.

## Steps
1. Record agent_id, capability ids, parent_run_id, optional git_commit.
2. Attach to the evidence or run record.
3. Do not treat provenance alone as proof of truth.

## Protected invariants (always)
1. No single pillar defines reality alone.
2. Recognition is continuous and unresolved.
3. A successful software/process check is not proof of real-world outcome improvement.
4. Promotion requires independent validation outside the originating path.
5. Evidence must be sealed before it can influence promotion.
6. CONFIRMED / NOT-YET-VERIFIED / NOT-RUN stay distinct.

## Output
- Provenance chain suitable for a run record
- Status NOT-YET-VERIFIED by default
