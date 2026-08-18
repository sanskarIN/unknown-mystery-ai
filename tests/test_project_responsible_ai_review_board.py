import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "projects" / "responsible_ai_review_board" / "main.py"


class ResponsibleAIReviewBoardTests(unittest.TestCase):
    def test_default_run_passes_documented_review(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True, check=False
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["project"], "Responsible AI Review Board")
        self.assertEqual(payload["validation_issues"], [])
        self.assertTrue(payload["review"]["passed"])
        self.assertTrue(payload["review"]["evidence_passed"])
        self.assertEqual(payload["review"]["failed_gates"], [])


if __name__ == "__main__":
    unittest.main()
