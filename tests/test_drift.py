import math
import unittest

from umai.drift import mean_shift, pooled_standard_deviation, standardized_mean_shift


class DriftTests(unittest.TestCase):
    def test_mean_shift(self) -> None:
        self.assertEqual(mean_shift([1.0, 2.0], [2.0, 3.0]), 1.0)

    def test_standardized_shift_equal_constant_samples(self) -> None:
        self.assertEqual(standardized_mean_shift([1.0, 1.0], [1.0, 1.0]), 0.0)

    def test_standardized_shift_different_constant_samples(self) -> None:
        value = standardized_mean_shift([1.0, 1.0], [2.0, 2.0])
        self.assertGreater(value, 0.0)
        self.assertFalse(math.isnan(value))

    def test_empty_sample_rejected(self) -> None:
        with self.assertRaises(ValueError):
            pooled_standard_deviation([], [])


if __name__ == "__main__":
    unittest.main()
