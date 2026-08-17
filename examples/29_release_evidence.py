"""Render a synthetic release evidence bundle as JSON.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.evidence import EvidenceBundle


bundle = EvidenceBundle(
    release_id="companion-candidate",
    source_commit="demo-sha",
    checks={"tests": True, "evaluation": True, "privacy": True, "rollback": True},
    metrics={"accuracy": 0.88, "latency_ms": 105.0},
    notes=("Synthetic evidence for documentation only.",),
)

print("passed:", bundle.passed)
print(bundle.to_json())
