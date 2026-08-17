import unittest

from umai.privacy import pseudonymous_id, redact_common_identifiers


class PrivacyTests(unittest.TestCase):
    def test_redact_email_and_phone(self) -> None:
        text = "Contact reader@example.com or +91 98765 43210"
        redacted = redact_common_identifiers(text)
        self.assertNotIn("reader@example.com", redacted)
        self.assertNotIn("98765", redacted)
        self.assertIn("[REDACTED_EMAIL]", redacted)
        self.assertIn("[REDACTED_PHONE]", redacted)

    def test_pseudonymous_id_is_deterministic(self) -> None:
        first = pseudonymous_id("user-123")
        second = pseudonymous_id("user-123")
        self.assertEqual(first, second)
        self.assertEqual(len(first), 16)

    def test_empty_identifier_rejected(self) -> None:
        with self.assertRaises(ValueError):
            pseudonymous_id("")


if __name__ == "__main__":
    unittest.main()
