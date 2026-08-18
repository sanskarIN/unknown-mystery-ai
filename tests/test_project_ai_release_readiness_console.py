import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "projects" / "ai_release_readiness_console" / "main.py"


class AIReleaseReadinessConsoleTests(unittest.TestCase):
    def test_default_run_passes_readiness_contract(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True, check=False
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["project"], "AI Release Readiness Console")
        self.assertEqual(payload["metrics"]["accuracy"], 0.75)
        self.assertTrue(payload["release"]["passed"])
        self.assertTrue(payload["release"]["evidence_passed"])
        self.assertEqual(payload["validation_issues"], [])


if __name__ == "__main__":
    unittest.main()
