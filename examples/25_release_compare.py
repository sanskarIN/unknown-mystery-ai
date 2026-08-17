"""Compare synthetic release metrics without hiding tradeoffs.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.compare import compare_metrics


comparison = compare_metrics(
    "release-1",
    "release-2",
    {"accuracy": 0.84, "latency_ms": 120.0, "memory_mb": 600.0},
    {"accuracy": 0.86, "latency_ms": 105.0, "memory_mb": 640.0},
)

for delta in comparison.deltas:
    print(delta.name, "delta=", round(delta.absolute, 3))
