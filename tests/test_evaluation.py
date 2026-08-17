import unittest

from umai.evaluation import accuracy_score, classification_report


class EvaluationTests(unittest.TestCase):
    def test_accuracy(self) -> None:
        self.assertAlmostEqual(accuracy_score([1, 0, 1], [1, 1, 1]), 2 / 3)

    def test_report_contains_overall_accuracy(self) -> None:
        report = classification_report(["a", "a", "b"], ["a", "b", "b"])
        self.assertIn("__overall__", report)
        self.assertAlmostEqual(float(report["__overall__"]["accuracy"]), 2 / 3)

    def test_length_mismatch_raises(self) -> None:
        with self.assertRaises(ValueError):
            accuracy_score([1, 2], [1])


if __name__ == "__main__":
    unittest.main()
