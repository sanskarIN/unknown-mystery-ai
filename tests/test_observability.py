import unittest

from umai.observability import MetricEvent, mean_metric


class ObservabilityTests(unittest.TestCase):
    def test_mean_metric(self) -> None:
        events = [
            MetricEvent("release-1", "latency_ms", 10.0),
            MetricEvent("release-1", "latency_ms", 14.0),
            MetricEvent("release-1", "memory_mb", 100.0),
        ]
        self.assertEqual(mean_metric(events, "latency_ms"), 12.0)

    def test_missing_metric_raises(self) -> None:
        with self.assertRaises(ValueError):
            mean_metric([], "latency_ms")

    def test_empty_release_id_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MetricEvent("", "latency_ms", 10.0)


if __name__ == "__main__":
    unittest.main()
