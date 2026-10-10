---
name: siw-run-record
description: Emit a run-registry-shaped record for an activation cycle.
pillar: Provenance
status: NOT-RUN
framework: signal-infowells
---

# Run Record

**Pillar:** Provenance  
**Framework:** Signal InfoWells (independent activation marketplace)  
**Status of this skill package:** NOT-RUN until exercised in a recorded activation

## When to use
At the end of an activation cycle or bounded halt.

## Steps
1. Fill run_id, timestamp, task_digest, counters, evidence_digests, provenance.
2. Set status to NOT-YET-VERIFIED by default.
3. List unresolved questions (include Recognition continuous note when relevant).
4. Do not promote.

## Protected invariants (always)
1. No single pillar defines reality alone.
2. Recognition is continuous and unresolved.
3. A successful software/process check is not proof of real-world outcome improvement.
4. Promotion requires independent validation outside the originating path.
5. Evidence must be sealed before it can influence promotion.
6. CONFIRMED / NOT-YET-VERIFIED / NOT-RUN stay distinct.
