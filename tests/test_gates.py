import unittest

from umai.gates import evaluate_release_gates


class GateTests(unittest.TestCase):
    def test_all_pass(self) -> None:
        decision = evaluate_release_gates({"tests": True, "privacy": True, "rollback": True})
        self.assertTrue(decision.passed)
        self.assertEqual(decision.failed, ())

    def test_failed_gate_blocks_release(self) -> None:
        decision = evaluate_release_gates({"tests": True, "privacy": False})
        self.assertFalse(decision.passed)
        self.assertEqual([item.name for item in decision.failed], ["privacy"])

    def test_empty_gate_set_rejected(self) -> None:
        with self.assertRaises(ValueError):
            evaluate_release_gates({})


if __name__ == "__main__":
    unittest.main()
