# Cost Budget Planner

A local budgeting exercise that estimates request costs using prices supplied explicitly by the caller.

## Run

```bash
python -m pip install -e .
python projects/cost_budget_planner/main.py
python projects/cost_budget_planner/main.py --input-price 120 --output-price 360 --budget 2500 --currency INR
```

## What it demonstrates

- explicit input/output token counts,
- caller-supplied per-million-token pricing,
- estimated per-request cost,
- whole-request capacity under a fixed budget,
- clear labeling that the values are not live vendor pricing.

## Extension ideas

Compare multiple caller-supplied pricing scenarios, add cache-hit assumptions, include non-token infrastructure costs, or export a capacity-planning table.

## Boundary

Provider prices, billing units, discounts, caching rules, taxes, and infrastructure costs can change. Always verify real procurement/billing data before financial decisions.

Official book store: **https://ramsandesh.gumroad.com**
