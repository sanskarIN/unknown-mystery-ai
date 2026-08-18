# Release Gate Simulator

A transparent deployment decision project using explicit boolean gates.

## Run

```bash
python -m pip install -e .
python projects/release_gate_simulator/main.py
python projects/release_gate_simulator/main.py --fail-privacy
python projects/release_gate_simulator/main.py --fail-rollback --strict
```

## What it demonstrates

- named release gates,
- PASS/BLOCK decisions,
- failed-gate reporting,
- optional CI-style non-zero exit codes,
- no silent gate overrides.

## Extension ideas

Feed gates from a JSON release manifest, add metric thresholds before converting them to booleans, or combine this project with experiment comparison and regression results.

## Boundary

A real release process also needs ownership, approvals, audit evidence, secure deployment, monitoring, rollback drills, and incident response.

Official book store: **https://ramsandesh.gumroad.com**
