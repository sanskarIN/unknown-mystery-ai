import unittest

from umai.ranking import precision_at_k, recall_at_k, reciprocal_rank


class RankingTests(unittest.TestCase):
    def test_precision_and_recall(self) -> None:
        retrieved = ["a", "x", "b", "y"]
        relevant = {"a", "b", "c"}
        self.assertAlmostEqual(precision_at_k(retrieved, relevant, 3), 2 / 3)
        self.assertAlmostEqual(recall_at_k(retrieved, relevant, 3), 2 / 3)

    def test_reciprocal_rank(self) -> None:
        self.assertEqual(reciprocal_rank(["x", "b"], {"b"}), 0.5)
        self.assertEqual(reciprocal_rank(["x"], {"b"}), 0.0)

    def test_invalid_k(self) -> None:
        with self.assertRaises(ValueError):
            precision_at_k([], set(), 0)


if __name__ == "__main__":
    unittest.main()
