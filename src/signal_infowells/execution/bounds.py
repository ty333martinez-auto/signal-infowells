"""Bounded recursive execution limits."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionBounds:
    max_depth: int = 4
    max_iterations: int = 8
    max_total_steps: int = 32
    max_wall_time_sec: int = 300

    def tightened(
        self,
        max_depth: int | None = None,
        max_iterations: int | None = None,
        max_total_steps: int | None = None,
        max_wall_time_sec: int | None = None,
    ) -> "ExecutionBounds":
        return ExecutionBounds(
            max_depth=max_depth if max_depth is not None else self.max_depth,
            max_iterations=max_iterations if max_iterations is not None else self.max_iterations,
            max_total_steps=max_total_steps if max_total_steps is not None else self.max_total_steps,
            max_wall_time_sec=max_wall_time_sec if max_wall_time_sec is not None else self.max_wall_time_sec,
        )


class BoundExceeded(Exception):
    """Raised when a protocol bound is reached. This is correct behavior, not a crash."""

    def __init__(self, limit_name: str) -> None:
        super().__init__(f"BoundExceeded:{limit_name}")
        self.limit_name = limit_name
