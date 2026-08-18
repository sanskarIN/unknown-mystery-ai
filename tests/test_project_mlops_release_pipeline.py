import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "projects" / "mlops_release_pipeline" / "main.py"


class MLOpsReleasePipelineTests(unittest.TestCase):
    def test_default_run_approves_candidate(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True, check=False
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["project"], "MLOps Release Pipeline")
        self.assertTrue(payload["artifact"]["approved"])
        self.assertTrue(payload["release"]["passed"])
        self.assertTrue(payload["release"]["evidence_passed"])
        self.assertEqual(payload["release"]["failed_gates"], [])


if __name__ == "__main__":
    unittest.main()
