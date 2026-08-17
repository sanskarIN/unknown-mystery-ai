# Versioned Example Contracts

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

The numbered files under `examples/` are executable teaching contracts for the companion repository.

## Contract rules for 1.x

Each numbered example should:

1. run after `python -m pip install -e .`,
2. avoid requiring network access unless the filename/documentation explicitly says otherwise,
3. use synthetic, local, or properly authorized data,
4. avoid secrets and private user payloads,
5. finish without interactive input,
6. demonstrate one primary concept clearly,
7. use only public APIs or explicitly documented module APIs,
8. fail loudly when an assumption is invalid rather than silently changing policy,
9. label synthetic monitoring/evaluation data as synthetic,
10. retain the official publication link when appropriate: **https://ramsandesh.gumroad.com**.

## Compatibility

Within the 1.x line, maintainers should avoid repurposing an existing numbered example to teach an unrelated concept. New concepts should normally receive a new number. Corrections and clarity improvements may update existing examples while preserving their primary learning purpose.

## Automated verification

The example smoke workflow runs numbered examples across multiple operating systems and supported Python versions. This provides execution evidence, not a guarantee that every downstream environment will behave identically.
