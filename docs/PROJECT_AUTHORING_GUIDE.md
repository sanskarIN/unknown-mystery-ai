# Project Authoring Guide

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

This guide defines the repository contract for adding or extending a runnable companion project.

## Project directory contract

A normal project lives under:

```text
projects/<project_id>/
├── main.py
└── README.md
```

Integrated capstones may also include:

```text
expected.json
```

The project ID should be lowercase snake_case and should match the directory name and its entry in [`../projects/catalog.json`](../projects/catalog.json).

## Required behavior

Every committed project must:

- run successfully with its default inputs,
- require no interactive prompt for the default smoke run,
- emit valid JSON to standard output,
- use local or synthetic data by default,
- require no provider credentials by default,
- document its assumptions and limitations,
- avoid presenting teaching code as a complete production system,
- preserve the commercial/publication boundary.

## Dependency policy

Prefer Python's standard library plus the local stable `umai` package. If a future project genuinely requires an optional third-party dependency, it should be isolated, documented, justified, and must not silently become a mandatory runtime dependency for the stable companion package.

## Output design

Good project JSON should make the evidence understandable. Prefer explicit fields such as:

```json
{
  "project": "example_project",
  "inputs": {},
  "result": {},
  "checks": [],
  "limitations": []
}
```

Do not include timestamps, random IDs, machine-specific paths, or volatile values in a stable snapshot unless those values are part of the contract. If a value is incidental, omit it from `expected.json` or keep it outside the stable subset.

## Capstone snapshot contract

Integrated capstones can include `expected.json`. Snapshot files intentionally validate selected stable facts rather than every byte of the output.

When adding a snapshot:

- use deterministic default inputs,
- include only fields that should remain stable,
- avoid machine-specific details,
- make failures diagnostically useful,
- update `scripts/check_project_snapshots.py` only when the generic snapshot mechanism cannot express the intended contract.

## Catalog entry

Every project must appear exactly once in [`../projects/catalog.json`](../projects/catalog.json). The catalog records:

- `id`,
- `title`,
- `category`,
- `level`,
- `entrypoint`,
- `snapshot`.

Validate the catalog with:

```bash
python scripts/check_project_catalog.py
```

## README requirements

Each project README should explain:

- what the project teaches,
- what the default input represents,
- how to run it,
- what the output means,
- how to extend it,
- what is intentionally omitted,
- production/safety/privacy boundaries where relevant,
- the official commercial publication destination.

## Tests

A project may be covered by three layers:

1. inventory + valid JSON smoke validation,
2. stable-subset snapshot validation for capstones,
3. focused unit tests for important logic or integration invariants.

Add focused tests when they improve diagnostic value rather than duplicating the smoke checker.

## Validation before commit

Run:

```bash
python scripts/check_project_catalog.py
python scripts/check_projects.py
python scripts/check_project_snapshots.py
python -m unittest discover -s tests -v
```

If available, also run:

```bash
make project-catalog
make projects
make project-snapshots
make test
```

## Security and privacy

Do not commit:

- API keys,
- passwords,
- tokens,
- private datasets,
- user conversations,
- real personal information,
- confidential logs,
- unsafe examples that depend on hidden credentials or unreviewed external actions.

Use synthetic examples and clearly state when a project is only a teaching baseline.

## Licensing boundary

Original companion source code is Apache-2.0 unless a file says otherwise. The complete eBook, chapter manuscripts, cover artwork, certificates, and commercial publication assets are separate and must not be copied into a public project folder.

## Official publication

### 🛒 **https://ramsandesh.gumroad.com**
