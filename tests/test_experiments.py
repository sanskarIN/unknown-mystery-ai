import unittest

from umai.experiments import ExperimentRecord, best_record


class ExperimentTests(unittest.TestCase):
    def test_fingerprint_is_stable(self) -> None:
        a = ExperimentRecord("run", {"seed": 7, "lr": 0.1})
        b = ExperimentRecord("run", {"lr": 0.1, "seed": 7})
        self.assertEqual(a.fingerprint, b.fingerprint)

    def test_best_record(self) -> None:
        records = [
            ExperimentRecord("a", {"x": 1}, {"accuracy": 0.8}),
            ExperimentRecord("b", {"x": 2}, {"accuracy": 0.9}),
        ]
        self.assertEqual(best_record(records, "accuracy").name, "b")

    def test_missing_metric(self) -> None:
        record = ExperimentRecord("a", {}, {})
        with self.assertRaises(KeyError):
            record.metric("loss")


if __name__ == "__main__":
    unittest.main()
