import unittest

from src.signal_infowells.cycle import BuildBounds, assess_cycle, assess_promotion

GOOD_CHECKS = {
    "tests_passed": True,
    "invariants_preserved": True,
    "acceptance_criteria_met": True,
    "unresolved_questions_recorded": True,
}
DIGEST = "a" * 64


class AutonomousBuildCycleTests(unittest.TestCase):
    def test_cycle_auto_approves_only_when_all_gates_pass(self):
        result = assess_cycle(checks=GOOD_CHECKS, evidence_digest=DIGEST,
                              depth=1, iterations=1, steps=8)
        self.assertTrue(result.cycle_approved)
        self.assertEqual(result.status, "NOT-YET-VERIFIED")
        self.assertFalse(result.promotion_authorized)

    def test_failed_check_blocks_cycle_approval(self):
        checks = dict(GOOD_CHECKS, tests_passed=False)
        result = assess_cycle(checks=checks, evidence_digest=DIGEST,
                              depth=1, iterations=1, steps=1)
        self.assertFalse(result.cycle_approved)
        self.assertTrue(any("tests_passed" in item for item in result.blockers))

    def test_bad_digest_blocks_cycle_approval(self):
        result = assess_cycle(checks=GOOD_CHECKS, evidence_digest="not-a-digest",
                              depth=1, iterations=1, steps=1)
        self.assertFalse(result.cycle_approved)

    def test_bounds_are_enforced(self):
        result = assess_cycle(checks=GOOD_CHECKS, evidence_digest=DIGEST,
                              depth=5, iterations=1, steps=1, bounds=BuildBounds())
        self.assertFalse(result.cycle_approved)

    def test_promotion_requires_independent_validation_and_user_command(self):
        cycle = assess_cycle(checks=GOOD_CHECKS, evidence_digest=DIGEST,
                             depth=1, iterations=1, steps=1)
        missing_command = assess_promotion(
            cycle, producer_id="maker", validator_id="checker",
            independent_validation_passed=True, evidence_sealed=True,
            user_commanded_promotion=False,
        )
        self.assertFalse(missing_command.promotion_authorized)
        commanded = assess_promotion(
            cycle, producer_id="maker", validator_id="checker",
            independent_validation_passed=True, evidence_sealed=True,
            user_commanded_promotion=True,
        )
        self.assertTrue(commanded.promotion_authorized)

    def test_producer_cannot_claim_independent_validation(self):
        cycle = assess_cycle(checks=GOOD_CHECKS, evidence_digest=DIGEST,
                             depth=1, iterations=1, steps=1)
        result = assess_promotion(
            cycle, producer_id="maker", validator_id="maker",
            independent_validation_passed=True, evidence_sealed=True,
            user_commanded_promotion=True,
        )
        self.assertFalse(result.promotion_authorized)


if __name__ == "__main__":
    unittest.main()
