import unittest

from umai.compare import compare_metrics


class CompareTests(unittest.TestCase):
    def test_metric_deltas(self) -> None:
        comparison = compare_metrics(
            "v1",
            "v2",
            {"accuracy": 0.8, "latency": 100.0},
            {"accuracy": 0.85, "latency": 90.0},
        )
        values = {delta.name: delta.absolute for delta in comparison.deltas}
        self.assertAlmostEqual(values["accuracy"], 0.05)
        self.assertEqual(values["latency"], -10.0)

    def test_no_shared_metrics(self) -> None:
        with self.assertRaises(ValueError):
            compare_metrics("a", "b", {"x": 1.0}, {"y": 2.0})


if __name__ == "__main__":
    unittest.main()
