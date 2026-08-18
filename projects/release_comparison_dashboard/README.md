# Release Comparison Dashboard

Compare shared metrics between a synthetic baseline and candidate release.

## Run

```bash
python -m pip install -e .
python projects/release_comparison_dashboard/main.py
```

## What it demonstrates

- named release identities,
- shared-metric comparisons,
- explicit baseline/candidate values,
- absolute metric deltas,
- warning that metric direction is application-specific.

## Extension ideas

Add acceptance bands, uncertainty intervals, release-gate conversion, slice metrics, or a Markdown report. Keep metric semantics explicit rather than assuming every increase is an improvement.

Official book store: **https://ramsandesh.gumroad.com**
