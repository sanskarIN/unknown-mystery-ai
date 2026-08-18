import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "projects" / "rag_evaluation_capstone" / "main.py"


class RAGEvaluationCapstoneTests(unittest.TestCase):
    def test_default_run_reports_retrieval_quality(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True, check=False
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["project"], "RAG Evaluation Capstone")
        self.assertAlmostEqual(payload["metrics"]["precision_at_3"], 2 / 3)
        self.assertEqual(payload["metrics"]["recall_at_3"], 1.0)
        self.assertEqual(payload["metrics"]["reciprocal_rank"], 1.0)
        self.assertTrue(payload["regression"]["passed"])


if __name__ == "__main__":
    unittest.main()
