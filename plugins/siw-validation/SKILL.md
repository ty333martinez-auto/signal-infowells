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
Before any promotion decision or claim of capability readiness.

## Steps
1. Identify the claim, acceptance criteria, originating run, producer, and evidence artifacts.
2. Verify validator independence: the validator and validation path must be separate from the path that produced the claim. If independence is unclear, stop and report the gap.
3. Verify each evidence artifact's digest against its canonical content and check provenance, scope, timestamp, and status. A digest string alone is not proof that the content was correctly sealed.
4. Test the claim against explicit acceptance criteria; record method, observed result, failures, and limitations. Do not substitute a green process test for real-world efficacy evidence.
5. Check whether contradictory evidence, missing evidence, or unresolved Recognition questions materially limit the claim.
6. If independence, evidence integrity, or required criteria are missing, retain NOT-YET-VERIFIED. If the capability was not executed, use NOT-RUN.
7. Set CONFIRMED only when independent validation is documented, evidence is sealed, and all required criteria are met. This skill never promotes automatically.

## Required output
- Claim and acceptance criteria
- Validator identity/path and independence rationale
- Evidence digests checked and provenance status
- Tests performed, results, failures, and limitations
- Conflicts and unresolved questions
- Exactly one status: CONFIRMED / NOT-YET-VERIFIED / NOT-RUN

## Protected invariants
1. No single pillar defines reality alone.
2. Recognition is continuous and unresolved.
3. Software/process success is not proof of real-world outcome improvement.
4. Promotion requires independent validation outside the originating path.
5. Evidence must be sealed before it influences promotion.
6. Status labels remain distinct.

## Non-goals
- Does not auto-promote to CONFIRMED.
- Does not treat a matching digest as proof of truth or efficacy.
