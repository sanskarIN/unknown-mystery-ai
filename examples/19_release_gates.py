"""Demonstrate a transparent PASS/BLOCK release decision.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.gates import evaluate_release_gates


decision = evaluate_release_gates(
    {
        "unit-tests": True,
        "evaluation-threshold": True,
        "privacy-review": True,
        "rollback-ready": False,
    }
)

print("release passed:", decision.passed)
for result in decision.results:
    print(result.name, result.detail)
