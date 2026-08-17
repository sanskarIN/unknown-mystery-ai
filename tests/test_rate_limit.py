import unittest

from umai.rate_limit import FixedWindowRateLimiter


class RateLimitTests(unittest.TestCase):
    def test_limit_and_reset(self) -> None:
        limiter = FixedWindowRateLimiter(limit=2)
        self.assertTrue(limiter.allow(1))
        self.assertTrue(limiter.allow(1))
        self.assertFalse(limiter.allow(1))
        self.assertEqual(limiter.remaining, 0)
        self.assertTrue(limiter.allow(2))
        self.assertEqual(limiter.remaining, 1)

    def test_invalid_limit(self) -> None:
        with self.assertRaises(ValueError):
            FixedWindowRateLimiter(limit=0)


if __name__ == "__main__":
    unittest.main()
