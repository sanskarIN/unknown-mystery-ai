import unittest

from umai.release import ReleaseManifest


class ReleaseTests(unittest.TestCase):
    def test_summary_contains_identity_fields(self) -> None:
        manifest = ReleaseManifest(
            project="demo",
            version="1.0.0",
            model_id="model-1",
            data_id="data-1",
            code_revision="abc123",
            created_at="2026-08-17T00:00:00+00:00",
        )
        summary = manifest.summary()
        self.assertIn("demo@1.0.0", summary)
        self.assertIn("model=model-1", summary)

    def test_fingerprint_is_deterministic_when_timestamp_fixed(self) -> None:
        kwargs = dict(
            project="demo",
            version="1.0.0",
            model_id="model-1",
            data_id="data-1",
            code_revision="abc123",
            created_at="2026-08-17T00:00:00+00:00",
        )
        self.assertEqual(ReleaseManifest(**kwargs).fingerprint(), ReleaseManifest(**kwargs).fingerprint())


if __name__ == "__main__":
    unittest.main()
