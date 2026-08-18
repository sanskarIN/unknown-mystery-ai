# Portfolio Evidence Guide

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

The companion projects are most useful in a portfolio when they demonstrate reproducible engineering decisions rather than screenshots alone.

## A strong project record

For each project you want to present, record:

- **Problem** - what question or engineering need the project addresses.
- **Scope** - what is included and intentionally excluded.
- **Inputs** - synthetic/local data, configuration, assumptions, and constraints.
- **Baseline** - a simple reference approach when applicable.
- **Method** - the architecture or algorithm used.
- **Evidence** - metrics, checks, snapshots, release decisions, or other outputs.
- **Reproduction command** - the exact command another person can run.
- **Limitations** - what the evidence does not prove.
- **Safety/privacy boundary** - any important data, access, or operational constraint.
- **Next improvement** - the most valuable next iteration.

## Prefer reproducible evidence over claims

Instead of saying:

> This project is production ready.

Prefer evidence such as:

- all default project runs produce valid JSON,
- a stable subset snapshot passes,
- unit tests cover important branches,
- the project runs across supported platforms,
- release gates make assumptions explicit,
- privacy-sensitive values are not logged in fixtures.

Production readiness is context-specific and should not be claimed solely from the companion's educational checks.

## Recommended capstone evidence bundle

For one of the integrated capstones, preserve:

```text
project-name/
├── problem.md
├── architecture.md
├── assumptions.md
├── run-command.txt
├── result.json
├── expected.json
├── test-evidence.md
├── limitations.md
└── next-steps.md
```

These portfolio files are suggestions for your own portfolio; do not duplicate them into every repository project unless they add real value.

## Show tradeoffs

A good portfolio explanation should include at least one tradeoff. Examples:

- accuracy versus latency,
- recall versus precision,
- cloud flexibility versus edge privacy/offline requirements,
- stricter release gates versus delivery speed,
- observability detail versus privacy/data minimization,
- caching performance versus staleness risk.

## Show failure handling

Reviewers learn more from a clear failure path than from a perfect screenshot. Explain:

- what can fail,
- how the failure is detected,
- whether the system blocks, falls back, or degrades,
- what evidence is preserved,
- how recovery would be verified.

## Keep data safe

Portfolio demonstrations should use synthetic, public, or explicitly authorized data. Do not publish:

- private customer/user records,
- access tokens,
- passwords,
- proprietary datasets,
- confidential model outputs,
- private conversations.

## Cite the exact source version

When presenting a result based on this repository, record a release tag or commit SHA. A moving `main` branch is less reproducible than an immutable version.

## Suggested portfolio sequence

A balanced sequence using the included projects is:

1. Evaluation Report Studio
2. RAG Knowledge Explorer
3. Prompt Regression Lab
4. Artifact Registry Workflow
5. Model Monitoring Lab
6. Privacy Audit Workbench
7. AI Release Readiness Console
8. RAG Evaluation Capstone
9. MLOps Release Pipeline
10. Production Resilience Lab

The full 25-project catalog is in [`../projects/catalog.json`](../projects/catalog.json).

## Interview defense

Be prepared to answer:

- Why did you choose this baseline?
- Which output fields are evidence versus assumptions?
- What would change with real production traffic?
- Which failure is most important?
- What does the current test suite not prove?
- How would you protect real user data?
- What would make you block a release?
- How would you reproduce this result six months later?

## Licensing boundary

You may use and extend the Apache-2.0 companion source according to its license. The separately copyrighted commercial book/manuscript/artwork is not automatically part of that software license.

## Official publication

### 🛒 **https://ramsandesh.gumroad.com**
