"""Render experiment and artifact evidence as deterministic JSON.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.experiments import ExperimentRecord
from umai.registry import ArtifactVersion
from umai.reporting import to_json


report = {
    "experiment": ExperimentRecord("candidate", {"seed": 7}, {"accuracy": 0.87}),
    "artifact": ArtifactVersion("classifier", "1.2", "sha256-demo", approved=True),
}

print(to_json(report))
