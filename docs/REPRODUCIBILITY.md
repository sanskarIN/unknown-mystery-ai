# Reproducibility Checklist

> 🛒 **Official Gumroad store:** **https://ramsandesh.gumroad.com**

Use this checklist when turning an AI experiment into something another person can inspect and reproduce.

## Record before running

- problem statement and success criteria,
- code revision,
- environment/runtime version,
- dataset identity and allowed usage,
- preprocessing version,
- model/configuration identity,
- random seed where applicable,
- hardware/runtime notes,
- evaluation protocol.

## Record after running

- metrics and uncertainty where relevant,
- failed cases and known limitations,
- generated artifact identifiers,
- release manifest fingerprint,
- runtime and resource observations,
- any deviations from the planned protocol.

## Important limit

A seed alone does not guarantee identical results across every operating system, framework, accelerator, compiler, or parallel execution path. Reproducibility is a system property involving code, data, dependencies, configuration, runtime, hardware, and evaluation evidence.

## Practice with the companion utilities

Start with `src/umai/reproducibility.py` and `src/umai/release.py`, then adapt the pattern to your own framework.

## Continue learning

Full MLOps, lineage, deployment, monitoring, and governance coverage is part of the complete book:

### https://ramsandesh.gumroad.com
