import unittest

from umai.monitoring import synthetic_metric_series


class MonitoringTests(unittest.TestCase):
    def test_deterministic_series(self) -> None:
        a = synthetic_metric_series(length=3, baseline=10.0, noise=1.0, seed=7)
        b = synthetic_metric_series(length=3, baseline=10.0, noise=1.0, seed=7)
        self.assertEqual(a, b)

    def test_trend_without_noise(self) -> None:
        points = synthetic_metric_series(length=3, baseline=1.0, trend_per_step=0.5)
        self.assertEqual([point.value for point in points], [1.0, 1.5, 2.0])

    def test_negative_length_rejected(self) -> None:
        with self.assertRaises(ValueError):
            synthetic_metric_series(length=-1, baseline=0.0)


if __name__ == "__main__":
    unittest.main()
