# Prompt Regression Lab

This project demonstrates deterministic output regression checks with explicit required and forbidden substrings.

## Run

```bash
python -m pip install -e .
python projects/prompt_regression_lab/main.py
```

## What it demonstrates

- transparent regression cases,
- required-output expectations,
- forbidden-output checks,
- JSON-friendly evidence,
- repeatable local validation without an external model provider.

## Extension ideas

Load cases from an authorized JSON file, add domain-specific expectations, compare two candidate outputs, or connect the results to release gates.

## Boundary

Substring checks are intentionally simple. Real AI evaluation may require semantic review, datasets, human evaluation, adversarial testing, safety testing, and calibrated thresholds.

Official book store: **https://ramsandesh.gumroad.com**
