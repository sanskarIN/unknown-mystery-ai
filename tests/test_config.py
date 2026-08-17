import unittest

from umai.config import FeatureFlags, parse_bool


class ConfigTests(unittest.TestCase):
    def test_parse_bool(self) -> None:
        self.assertTrue(parse_bool("YES"))
        self.assertFalse(parse_bool("off"))

    def test_feature_flag_default(self) -> None:
        flags = FeatureFlags({"new_retriever": "true"})
        self.assertTrue(flags.enabled("new_retriever"))
        self.assertFalse(flags.enabled("missing"))

    def test_invalid_boolean(self) -> None:
        with self.assertRaises(ValueError):
            parse_bool("maybe")


if __name__ == "__main__":
    unittest.main()
