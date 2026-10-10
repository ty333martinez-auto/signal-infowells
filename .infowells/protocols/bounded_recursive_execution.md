# Bounded Recursive Execution Protocol

## Purpose

Permit iterative refinement while preventing unbounded or runaway recursion.

## Hard Limits (Default)

| Parameter              | Default Value | Notes                                      |
|------------------------|---------------|--------------------------------------------|
| `max_depth`            | 4             | Maximum nesting of recursive calls         |
| `max_iterations`       | 8             | Maximum loops inside a single depth level  |
| `max_total_steps`      | 32            | Global step budget for one activation run  |
| `max_wall_time_sec`    | 300           | Soft wall-clock limit (implementation may enforce harder) |

These values may be tightened per capability or per run. They may be raised **only** through a governance change that itself undergoes independent validation.

## Execution Rules

1. Every recursive entry must increment a depth counter.
2. Every iteration inside a level must increment an iteration counter.
3. When any limit is reached, execution **halts** and records:
   - Partial results (if any)
   - Unresolved questions
   - Explicit status `NOT-YET-VERIFIED` or `NOT-RUN` for incomplete branches
4. Halting is not failure; it is correct protocol behavior.
5. Refinement may only occur inside the remaining budget.

## Recording

Every run must emit a registry entry containing:

- `run_id`
- `task_digest`
- `depth_reached`
- `iterations_used`
- `steps_used`
- `halt_reason` (if any)
- `evidence_digests[]`
- `status` (CONFIRMED / NOT-YET-VERIFIED / NOT-RUN)
- `unresolved_questions[]`
- `provenance`

## Prohibited

- Disabling the depth or iteration counters
- Treating a halted run as successful promotion
- Collapsing unresolved questions into resolved claims
