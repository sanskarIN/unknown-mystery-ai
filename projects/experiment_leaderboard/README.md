# Experiment Leaderboard

A reproducible comparison project built around compact `ExperimentRecord` evidence.

## Run

```bash
python -m pip install -e .
python projects/experiment_leaderboard/main.py
```

## What it demonstrates

- explicit hyperparameter records,
- stable experiment fingerprints,
- metric-based sorting,
- separate winners for accuracy and latency,
- deterministic JSON-friendly output.

## Extension ideas

Add validation-loss, memory, cost, fairness slices, or energy metrics. Build Pareto-style comparisons instead of collapsing every goal into a single score.

## Boundary

A leaderboard does not prove production readiness. Dataset quality, statistical uncertainty, robustness, subgroup behavior, reproducibility, deployment constraints, and governance still matter.

Official book store: **https://ramsandesh.gumroad.com**
