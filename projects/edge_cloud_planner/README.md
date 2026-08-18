# Edge Cloud Planner

This project compares synthetic edge and cloud deployment options using explicit latency, privacy, cost, and offline constraints.

## Run

```bash
python -m pip install -e .
python projects/edge_cloud_planner/main.py
python projects/edge_cloud_planner/main.py --require-offline
python projects/edge_cloud_planner/main.py --max-latency 50 --min-privacy 0.9
```

## What it demonstrates

- explicit deployment constraints,
- edge/cloud eligibility filtering,
- simple transparent ranking,
- privacy and offline tradeoffs,
- deterministic synthetic planning data.

## Extension ideas

Add device memory, battery, thermal, model-size, accelerator, availability, or regional policy constraints. Treat every score as an application-specific decision aid rather than a universal truth.

## Boundary

The synthetic costs and scores are not vendor pricing or benchmarks. Production placement requires measurements on actual hardware and infrastructure.

Official book store: **https://ramsandesh.gumroad.com**
