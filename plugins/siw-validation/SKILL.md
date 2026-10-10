---
name: siw-validation
description: Independent validation gate. Never auto-promotes to CONFIRMED.
pillar: Validation
status: NOT-RUN
framework: signal-infowells
---

# Validation Gate

**Pillar:** Validation  
**Status:** NOT-RUN until exercised in a recorded activation.

## Use
Before any promotion decision or readiness claim.

## Steps
1. Identify the claim, acceptance criteria, originating run, producer, and evidence.
2. Verify validator independence. The validator and path must be separate from the producing path; if unclear, stop and record the gap.
3. Recompute each evidence digest from canonical content. Check provenance, scope, timestamp, and status; a digest string alone proves neither integrity nor truth.
4. Test explicit criteria. Record method, results, failures, and limitations. A passing process test does not prove real-world efficacy.
5. Check for contradictory/missing evidence and unresolved Recognition questions.
6. If independence, evidence integrity, or required criteria are missing, retain NOT-YET-VERIFIED. If not executed, use NOT-RUN.
7. Use CONFIRMED only when independent validation is documented, evidence is sealed, and all criteria pass. Never auto-promote.

## Required output
- Claim and acceptance criteria
- Validator/path and independence rationale
- Digests and provenance checked
- Tests, results, failures, limitations
- Conflicts and unresolved questions
- One status: CONFIRMED / NOT-YET-VERIFIED / NOT-RUN

## Invariants
- No single pillar defines reality alone.
- Recognition is continuous and unresolved.
- Software success is not proof of real-world efficacy.
- Promotion requires independent validation.
- Seal evidence before it influences promotion.
- Never collapse status labels.

## Non-goals
Does not auto-promote or treat digest matches as proof of truth.
