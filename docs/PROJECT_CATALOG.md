# Project Catalog Contract

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

[`projects/catalog.json`](../projects/catalog.json) is the machine-readable inventory for the repository's runnable companion projects.

## Schema

Top-level fields:

- `schema_version` — currently `1`.
- `official_store` — canonical Gumroad publication destination.
- `projects` — ordered list of project records.

Each project record contains:

- `id` — directory-safe project identifier;
- `title` — human-readable title;
- `category` — one of the documented learning groups;
- `level` — `foundation`, `intermediate`, `advanced`, or `capstone`;
- `entrypoint` — repository-relative `main.py` path;
- `snapshot` — whether the project has an `expected.json` stable-subset fixture.

## Validation contract

`scripts/check_project_catalog.py` verifies:

- schema version and canonical store link;
- exactly 25 unique project IDs for the 1.1.0 project suite;
- allowed category and level values;
- exact entrypoint naming;
- `main.py` and `README.md` existence;
- snapshot declaration/fixture consistency;
- canonical Gumroad link in every project README;
- parity between catalog IDs and discovered runnable project directories;
- exactly five snapshot-backed integrated capstones.

The unit-test suite independently checks important catalog invariants.

## Why a catalog?

A machine-readable catalog lets documentation, future static sites, portfolio indexes, release checks, and maintenance scripts discover projects without scraping prose. It also makes accidental project omissions visible in CI.

The catalog describes public companion software only; it does not list paid manuscript or commercial publishing files.
