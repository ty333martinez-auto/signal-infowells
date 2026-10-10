"""Bounded autonomous build-cycle decisions for Signal InfoWells."""
from __future__ import annotations
from dataclasses import dataclass
import re
from typing import Mapping

@dataclass(frozen=True)
class BuildBounds:
    max_depth: int = 4
    max_iterations: int = 8
    max_total_steps: int = 32

@dataclass(frozen=True)
class CycleAssessment:
    cycle_approved: bool
    status: str
    blockers: tuple[str, ...]
    promotion_authorized: bool = False

_REQUIRED_CHECKS = (
    "tests_passed",
    "invariants_preserved",
    "acceptance_criteria_met",
    "unresolved_questions_recorded",
)
_SHA256 = re.compile(r"^[0-9a-f]{64}$")

def assess_cycle(*, checks: Mapping[str, bool], evidence_digest: str,
                 depth: int, iterations: int, steps: int,
                 bounds: BuildBounds = BuildBounds()) -> CycleAssessment:
    """Approve a cycle to continue only when gates, evidence, and bounds pass.

    Cycle approval is not independent review, PR approval, or promotion.
    """
    blockers: list[str] = []
    for name in _REQUIRED_CHECKS:
        if checks.get(name) is not True:
            blockers.append(f"required check did not pass: {name}")
    if not _SHA256.fullmatch(evidence_digest or ""):
        blockers.append("missing or malformed sealed evidence SHA-256")
    if depth < 0 or depth > bounds.max_depth:
        blockers.append(f"depth outside allowed range 0..{bounds.max_depth}")
    if iterations < 0 or iterations > bounds.max_iterations:
        blockers.append(f"iterations outside allowed range 0..{bounds.max_iterations}")
    if steps < 0 or steps > bounds.max_total_steps:
        blockers.append(f"steps outside allowed range 0..{bounds.max_total_steps}")
    approved = not blockers
    return CycleAssessment(
        cycle_approved=approved,
        status="NOT-YET-VERIFIED" if approved else "NOT-RUN",
        blockers=tuple(blockers),
        promotion_authorized=False,
    )

def assess_promotion(cycle: CycleAssessment, *, producer_id: str,
                     validator_id: str | None, independent_validation_passed: bool,
                     evidence_sealed: bool, user_commanded_promotion: bool) -> CycleAssessment:
    """Report whether the separate promotion gate is satisfied; never auto-promote."""
    blockers = list(cycle.blockers)
    if not cycle.cycle_approved:
        blockers.append("cycle has not passed its automated gates")
    if not evidence_sealed:
        blockers.append("evidence is not sealed")
    if not validator_id or validator_id == producer_id:
        blockers.append("independent validator must be identified and differ from producer")
    if not independent_validation_passed:
        blockers.append("independent validation has not passed")
    if not user_commanded_promotion:
        blockers.append("explicit user command to promote is absent")
    return CycleAssessment(
        cycle_approved=cycle.cycle_approved,
        status="NOT-YET-VERIFIED",
        blockers=tuple(blockers),
        promotion_authorized=not blockers,
    )
