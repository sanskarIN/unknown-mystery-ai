import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "projects" / "production_resilience_lab" / "main.py"


class ProductionResilienceLabTests(unittest.TestCase):
    def test_default_run_recovers_with_fallback(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True, check=False
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["project"], "Production Resilience Lab")
        self.assertEqual(payload["fallback"]["selected_provider"], "fallback")
        self.assertEqual(payload["fallback"]["attempts"], ["primary", "fallback"])
        self.assertTrue(payload["serving"]["ok"])
        self.assertEqual(payload["eligible_placements"], ["device", "regional-cloud"])
        self.assertAlmostEqual(payload["estimated_demo_request_cost"], 0.005)


if __name__ == "__main__":
    unittest.main()
