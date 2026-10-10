---
name: siw-validation
description: Independent validation gate. Never auto-promotes to CONFIRMED.
pillar: Validation
status: NOT-RUN
framework: signal-infowells
---

# Validation Gate

**Pillar:** Validation  
**Framework:** Signal InfoWells (independent activation marketplace)  
**Status of this skill package:** NOT-RUN until exercised in a recorded activation

## When to use
Before any promotion decision.

## Steps
1. Check whether independent validation (outside originating path) is present.
2. Check whether evidence is sealed with digest + provenance.
3. If either is missing, keep NOT-YET-VERIFIED.
4. Never set CONFIRMED from the same path that produced the claim.

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

## Non-goals
- Does not auto-promote to CONFIRMED
- Does not claim real-world efficacy from process success alone
