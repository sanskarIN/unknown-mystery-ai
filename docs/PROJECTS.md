# Companion Projects Guide

> 🛒 **Official Gumroad store:** **https://ramsandesh.gumroad.com**

The repository now includes twenty complete, runnable companion projects under [`projects/`](../projects/). They use the stable `umai` package, local or synthetic data by default, and no provider credentials.

## Suggested learning order

### Foundation and evaluation

1. **Evaluation Report Studio** — understand expected/predicted labels and per-class metrics.
2. **Experiment Leaderboard** — record reproducible parameters, fingerprints, and competing objectives.
3. **RAG Knowledge Explorer** — inspect lexical retrieval, scores, and source metadata.
4. **Retrieval Ranking Benchmark** — measure precision@k, recall@k, and reciprocal rank.
5. **Text Chunking Lab** — inspect normalization, chunk size, overlap, and deterministic preprocessing.

### Prompting, agents, and serving

6. **Prompt Template Studio** — version prompts and expose required variables.
7. **Prompt Regression Lab** — make output expectations explicit and repeatable.
8. **Agent Router Sandbox** — inspect allowlisted tool registration and deterministic routing.
9. **Local Serving Contract** — practice request identity, model versioning, and structured invalid-request responses.
10. **Resilient Request Pipeline** — combine bounded caching with explicit fallback behavior.

### Governance and release engineering

11. **Artifact Registry Workflow** — separate artifact registration from approval.
12. **Release Manifest Builder** — bind model, data, code, metrics, metadata, and fingerprints.
13. **Evidence Bundle Builder** — collect source/check/metric evidence in a structured bundle.
14. **Release Comparison Dashboard** — compare shared baseline/candidate metrics without hiding direction semantics.
15. **Release Gate Simulator** — convert reviewed evidence into transparent PASS/BLOCK gates.

### Deployment, operations, privacy, and cost

16. **Feature Flag Rollout Lab** — use explicit rollout switches and safe defaults.
17. **Edge Cloud Planner** — filter architecture choices using declared constraints.
18. **Model Monitoring Lab** — compare deterministic synthetic reference/current telemetry.
19. **Privacy Audit Workbench** — practice validation, redaction, and pseudonymous identifiers.
20. **Cost Budget Planner** — estimate capacity from caller-supplied pricing assumptions.

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
