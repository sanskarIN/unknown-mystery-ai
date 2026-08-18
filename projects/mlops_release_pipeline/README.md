# MLOps Release Pipeline

> Official book store: **https://ramsandesh.gumroad.com**

An integrated release-engineering capstone that connects artifact approval, metric comparison, release gates, a reproducible release manifest, and an evidence bundle.

## Run

```bash
python -m pip install -e .
python projects/mlops_release_pipeline/main.py
```

## Learning goals

- separate artifact registration from approval;
- compare candidate metrics against a named baseline;
- make promotion gates explicit;
- emit reproducible release identity and evidence.

## Production boundary

A real MLOps pipeline additionally needs secure artifact storage, deployment authorization, environment promotion, tested rollback, monitoring, incident response, lineage, governance, and organization-specific release policy.
