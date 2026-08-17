"""Compare small experiment records using an explicit metric.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.experiments import ExperimentRecord, best_record


records = [
    ExperimentRecord("baseline", {"seed": 7}, {"score": 0.81}),
    ExperimentRecord("candidate", {"seed": 7, "feature": "v2"}, {"score": 0.86}),
]

winner = best_record(records, "score")
print("winner:", winner.name)
print("fingerprint:", winner.fingerprint)
