# Artifact Registry Workflow

A small governance project that registers immutable artifact identities and makes approval explicit.

## Run

```bash
python -m pip install -e .
python projects/artifact_registry_workflow/main.py
```

## What it demonstrates

- artifact name/version/digest identity,
- duplicate identity protection,
- explicit approval transitions,
- approved-version queries,
- separation between registration and approval.

## Extension ideas

Persist approved manifests, attach evaluation evidence, require reviewer identities, or connect approved artifacts to a release manifest and deployment gate.

## Boundary

The in-memory registry is a teaching model, not a production artifact store or authorization system.

Official book store: **https://ramsandesh.gumroad.com**
