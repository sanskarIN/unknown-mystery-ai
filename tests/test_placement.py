import unittest

from umai.placement import PlacementOption, eligible_placements


class PlacementTests(unittest.TestCase):
    def test_filter_for_offline_and_privacy(self) -> None:
        options = [
            PlacementOption("edge", 15.0, 2.0, 0.9, True),
            PlacementOption("cloud", 80.0, 1.0, 0.6, False),
        ]
        selected = eligible_placements(options, min_privacy_score=0.8, require_offline=True)
        self.assertEqual([item.name for item in selected], ["edge"])

    def test_latency_filter(self) -> None:
        options = [PlacementOption("cloud", 80.0, 1.0, 0.8, False)]
        self.assertEqual(eligible_placements(options, max_latency_ms=50.0), [])

    def test_invalid_privacy_score(self) -> None:
        with self.assertRaises(ValueError):
            PlacementOption("x", 1.0, 1.0, 1.5, False)


if __name__ == "__main__":
    unittest.main()
