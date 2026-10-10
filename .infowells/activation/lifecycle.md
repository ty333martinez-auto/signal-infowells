# Activation Lifecycle

Signal InfoWells autonomous agent operation follows a fixed sequence.
All steps are mandatory; none may be skipped for convenience.

```
1. Receive task
2. Identify signals
3. Dispatch candidate capabilities
4. Execute
5. Test
6. Refine within bounded cycles
7. Record evidence, changes, and unresolved questions
8. Require independent validation before promotion
```

## Bounds

- Maximum recursive depth: defined in `../protocols/bounded_recursive_execution.md`
- Maximum iterations per cycle: defined in the same protocol
- Time / resource limits: declared per run in the registry

## Promotion Gate

Promotion from NOT-YET-VERIFIED → CONFIRMED occurs **only** after:

1. Independent validation (different agent or human reviewer)
2. Evidence sealing with digest + provenance
3. Explicit record in the run registry

No automatic promotion is permitted.
