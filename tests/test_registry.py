import unittest

from umai.registry import ArtifactRegistry, ArtifactVersion


class RegistryTests(unittest.TestCase):
    def test_register_and_approve(self) -> None:
        registry = ArtifactRegistry()
        artifact = ArtifactVersion("model", "1.0", "abc123")
        registry.register(artifact)
        approved = registry.approve("model", "1.0")
        self.assertTrue(approved.approved)
        self.assertEqual(registry.approved_versions("model"), [approved])

    def test_conflicting_registration_rejected(self) -> None:
        registry = ArtifactRegistry()
        registry.register(ArtifactVersion("model", "1.0", "abc"))
        with self.assertRaises(ValueError):
            registry.register(ArtifactVersion("model", "1.0", "xyz"))

    def test_unknown_artifact(self) -> None:
        registry = ArtifactRegistry()
        with self.assertRaises(KeyError):
            registry.get("missing", "1")


if __name__ == "__main__":
    unittest.main()
