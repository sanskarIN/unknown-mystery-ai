import unittest
import warnings

from umai.deprecation import DeprecatedFeature, warn_deprecated


class DeprecationTests(unittest.TestCase):
    def test_message_contains_replacement_and_removal(self) -> None:
        feature = DeprecatedFeature("old_api", "new_api", "2.0.0")
        message = feature.message()
        self.assertIn("old_api is deprecated", message)
        self.assertIn("use new_api instead", message)
        self.assertIn("planned removal: 2.0.0", message)

    def test_warning_category(self) -> None:
        feature = DeprecatedFeature("old_api")
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            warn_deprecated(feature)
        self.assertEqual(len(caught), 1)
        self.assertIs(caught[0].category, DeprecationWarning)

    def test_invalid_stacklevel(self) -> None:
        with self.assertRaises(ValueError):
            warn_deprecated(DeprecatedFeature("x"), stacklevel=0)


if __name__ == "__main__":
    unittest.main()
