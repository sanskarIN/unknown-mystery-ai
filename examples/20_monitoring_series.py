"""Generate synthetic latency-like data for a dashboard exercise.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.monitoring import synthetic_metric_series


points = synthetic_metric_series(
    length=8,
    baseline=120.0,
    noise=5.0,
    trend_per_step=1.5,
    seed=42,
)

for point in points:
    print(point.step, round(point.value, 2))

print("Synthetic data only — not production telemetry.")
