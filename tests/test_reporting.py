import json
import unittest

from umai.reporting import key_value_report, to_json
from umai.registry import ArtifactVersion


class ReportingTests(unittest.TestCase):
    def test_dataclass_json(self) -> None:
        artifact = ArtifactVersion("model", "1.0", "abc", True)
        payload = json.loads(to_json(artifact))
        self.assertEqual(payload["name"], "model")
        self.assertTrue(payload["approved"])

    def test_key_value_report_is_sorted(self) -> None:
        report = key_value_report({"z": 1, "a": 2})
        self.assertEqual(report.splitlines(), ["a: 2", "z: 1"])

    def test_invalid_indent(self) -> None:
        with self.assertRaises(ValueError):
            to_json({"x": 1}, indent=-1)


if __name__ == "__main__":
    unittest.main()
