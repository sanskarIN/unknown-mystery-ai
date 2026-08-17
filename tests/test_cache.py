import unittest

from umai.cache import BoundedCache


class CacheTests(unittest.TestCase):
    def test_eviction_is_lru(self) -> None:
        cache: BoundedCache[str, int] = BoundedCache(max_items=2)
        cache.set("a", 1)
        cache.set("b", 2)
        self.assertEqual(cache.get("a"), 1)
        cache.set("c", 3)
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("c"), 3)

    def test_clear(self) -> None:
        cache: BoundedCache[str, int] = BoundedCache(max_items=1)
        cache.set("x", 1)
        cache.clear()
        self.assertEqual(len(cache), 0)

    def test_invalid_size(self) -> None:
        with self.assertRaises(ValueError):
            BoundedCache(max_items=0)


if __name__ == "__main__":
    unittest.main()
