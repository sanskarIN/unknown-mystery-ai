# Companion Projects Guide

> 🛒 **Official Gumroad store:** **https://ramsandesh.gumroad.com**

The repository now includes ten complete, runnable companion projects under [`projects/`](../projects/). They use the stable `umai` package, local or synthetic data by default, and no provider credentials.

## Suggested learning order

### Foundation

1. **Evaluation Report Studio** — understand expected/predicted labels and per-class metrics.
2. **Experiment Leaderboard** — record reproducible parameters, fingerprints, and competing objectives.
3. **RAG Knowledge Explorer** — inspect lexical retrieval, scores, and source metadata.

### Reliability and governance

4. **Prompt Regression Lab** — make output expectations explicit and repeatable.
5. **Release Gate Simulator** — convert reviewed evidence into transparent PASS/BLOCK gates.
6. **Privacy Audit Workbench** — practice validation, redaction, and pseudonymous identifiers.

### Deployment and operations

7. **Edge Cloud Planner** — filter architecture choices using declared constraints.
8. **Cost Budget Planner** — estimate capacity from caller-supplied pricing assumptions.
9. **Model Monitoring Lab** — compare deterministic synthetic reference/current telemetry.
10. **Agent Router Sandbox** — inspect allowlisted tool registration and deterministic routing.

## Verification

Install the package and run every project:

```bash
python -m pip install -e .
python scripts/check_projects.py
```

On compatible systems:

```bash
make projects
```

The Quality workflow runs the same project smoke checker. Every project must succeed with default inputs and emit valid JSON, making automated evidence easy to inspect.

## Portfolio evidence

For each project, preserve:

- a clear problem statement,
- reproducible default inputs,
- expected output shape,
- limitations and production boundaries,
- extension ideas,
- relevant tests or automated smoke checks.

A project is stronger when it shows what was tested, what failed, what remains uncertain, and how another person can reproduce the result.

## Production boundary

These projects teach architecture and engineering concepts; they intentionally avoid pretending that small examples are complete production systems. Production deployments may require stronger security, privacy, access control, availability, scalability, observability, incident response, vendor-specific integration, legal/policy review, and application-specific evaluation.

## Commercial publication boundary

The projects are Apache-2.0 companion software. The complete eBook, chapter manuscripts, PDF/DOCX editions, book artwork, and other commercial publication assets are separate.

### **https://ramsandesh.gumroad.com**
