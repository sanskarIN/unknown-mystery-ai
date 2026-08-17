import unittest

import umai


class PublicApiTests(unittest.TestCase):
    def test_all_exports_exist(self) -> None:
        missing = [name for name in umai.__all__ if not hasattr(umai, name)]
        self.assertEqual(missing, [])

    def test_exports_are_unique(self) -> None:
        self.assertEqual(len(umai.__all__), len(set(umai.__all__)))

    def test_version_is_semver_like(self) -> None:
        parts = umai.__version__.split(".")
        self.assertEqual(len(parts), 3)
        self.assertTrue(all(part.isdigit() for part in parts))


if __name__ == "__main__":
    unittest.main()
