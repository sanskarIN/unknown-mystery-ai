import json
import unittest

from umai.evidence import EvidenceBundle


class EvidenceTests(unittest.TestCase):
    def test_passed_when_all_checks_pass(self) -> None:
        bundle = EvidenceBundle(
            release_id="candidate-1",
            source_commit="abc123",
            checks={"tests": True, "privacy": True},
            metrics={"accuracy": 0.9},
        )
        self.assertTrue(bundle.passed)
        payload = json.loads(bundle.to_json())
        self.assertEqual(payload["source_commit"], "abc123")

    def test_empty_checks_do_not_pass(self) -> None:
        bundle = EvidenceBundle("candidate-1", "abc123", {})
        self.assertFalse(bundle.passed)

    def test_empty_identity_rejected(self) -> None:
        with self.assertRaises(ValueError):
            EvidenceBundle("", "abc", {"tests": True})


if __name__ == "__main__":
    unittest.main()
