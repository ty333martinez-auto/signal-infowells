# Signal InfoWells — Core Invariants

These invariants are protected. They may only be changed by explicit governance process with independent validation.

## 1. No Single Pillar Defines Reality Alone

Every claim, promotion decision, or model of the world must be examined through multiple pillars.
A signal alone, recognition alone, evidence alone, execution alone, validation alone, or provenance alone is insufficient.

## 2. Recognition Is Continuous and Unresolved

Recognition is not a terminal state.
The system must never treat a recognition event as the final determination of significance or truth.
Documentation and code must leave the continuous role of Recognition open.

## 3. Software Success ≠ Real-World Efficacy

A passing unit test, integration test, or internal consistency check is **not** proof that the reasoning framework improves real-world outcomes.
This distinction must be preserved in all status reporting and promotion gates.

## 4. Promotion Requires Independent Validation

No capability, claim, configuration, or sealed evidence may be promoted to CONFIRMED status by the same execution path that produced it.
Independent validation is mandatory.

## 5. Evidence Must Be Sealed

Before any evidence can influence a promotion decision it must carry:

- Content digest (cryptographic hash)
- Provenance chain
- Explicit status label (CONFIRMED / NOT-YET-VERIFIED / NOT-RUN)

## 6. Status Labels Remain Distinct

| Label              | Meaning                                      |
|--------------------|----------------------------------------------|
| CONFIRMED          | Independently validated and sealed           |
| NOT-YET-VERIFIED   | Produced, recorded, awaiting independent check |
| NOT-RUN            | Defined but never executed in a recorded run |

These labels must never be collapsed or silently upgraded.
