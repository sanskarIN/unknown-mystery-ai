# Feature Flag Rollout Lab

A local configuration exercise showing explicit boolean feature flags for staged AI releases.

## Run

```bash
python -m pip install -e .
python projects/feature_flag_rollout_lab/main.py
python projects/feature_flag_rollout_lab/main.py --new-retriever off --shadow-mode yes
```

## What it demonstrates

- accepted boolean configuration spellings,
- explicit defaults for missing flags,
- independent rollout switches,
- JSON-friendly configuration evidence.

## Extension ideas

Add release cohorts, hardware segments, canary percentages, config provenance, or validation that incompatible flag combinations are blocked before deployment.

## Boundary

Feature flags are not authorization. Production rollout systems need authenticated configuration changes, audit history, safe defaults, rollback, and monitoring.

Official book store: **https://ramsandesh.gumroad.com**
