# Model Monitoring Lab

A deterministic synthetic-telemetry project for learning lightweight drift indicators.

## Run

```bash
python -m pip install -e .
python projects/model_monitoring_lab/main.py
```

## What it demonstrates

- deterministic synthetic metric generation,
- reference vs. current windows,
- absolute mean shift,
- standardized mean shift,
- explicit warning against universal drift thresholds.

## Extension ideas

Add multiple metrics, release identifiers, hardware classes, latency percentiles, fallback counts, or application-calibrated alert thresholds. Keep synthetic telemetry clearly labeled as synthetic.

## Boundary

Real monitoring needs production telemetry design, privacy review, alert ownership, SLOs, incident response, data-quality checks, and application-specific calibration.

Official book store: **https://ramsandesh.gumroad.com**
