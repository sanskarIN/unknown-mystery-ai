# AI Release Readiness Console

> Official book store: **https://ramsandesh.gumroad.com**

An integrated capstone that combines structured validation, privacy-aware identifiers, classification evaluation, explicit release gates, and an evidence bundle.

## Run

```bash
python -m pip install -e .
python projects/ai_release_readiness_console/main.py
```

The default run uses synthetic data and prints deterministic JSON evidence.

## Learning goals

- connect model metrics to release decisions;
- keep validation and privacy checks visible;
- separate PASS/BLOCK evidence from narrative confidence;
- retain a machine-readable evidence summary.

## Production boundary

Real release qualification needs application-specific requirements, representative evaluation, security/privacy review, operational SLOs, rollback testing, governance approvals, and accountable human ownership.
