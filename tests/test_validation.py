import unittest

from umai.validation import validate_record


class ValidationTests(unittest.TestCase):
    def test_valid_record(self) -> None:
        issues = validate_record({"name": "model-a", "version": 1}, {"name": str, "version": int})
        self.assertEqual(issues, [])

    def test_missing_and_wrong_type(self) -> None:
        issues = validate_record({"version": "1"}, {"name": str, "version": int})
        self.assertEqual(len(issues), 2)

    def test_extra_field_rejected_when_requested(self) -> None:
        issues = validate_record({"name": "x", "extra": True}, {"name": str}, allow_extra=False)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].field, "extra")


if __name__ == "__main__":
    unittest.main()
