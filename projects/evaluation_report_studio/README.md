# Evaluation Report Studio

A compact synthetic classification-evaluation project built with the companion metrics helpers.

## Run

```bash
python -m pip install -e .
python projects/evaluation_report_studio/main.py
```

## What it demonstrates

- exact-label accuracy,
- per-class precision, recall, F1, and support,
- JSON-friendly evaluation evidence,
- explicit expected vs. predicted labels,
- fully synthetic demonstration data.

## Extension ideas

Load authorized evaluation fixtures from JSON, add slice-level reports, compare candidate releases, or convert acceptance criteria into release gates.

## Boundary

Classification metrics do not capture every AI-system property. Production evaluation may also require calibration, ranking metrics, robustness, safety, human review, subgroup analysis, latency, cost, and task-specific acceptance criteria.

Official book store: **https://ramsandesh.gumroad.com**
