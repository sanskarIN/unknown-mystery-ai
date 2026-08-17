# Dependency Policy

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

The stable companion package intentionally has **no third-party runtime dependencies**. This keeps the core examples inspectable, portable, and easier to audit.

## Build tooling

`setuptools` is used as the build backend. The quality and release workflows build both source and wheel distributions so packaging failures are visible before release decisions.

## Adding a runtime dependency

A future dependency should be added only when it provides meaningful value that cannot reasonably be achieved by the standard library or an optional adapter. A proposal should document:

- why the dependency is needed,
- its license,
- supported Python/platform versions,
- security and maintenance considerations,
- data/network behavior,
- effect on installation size and reproducibility,
- whether it can remain optional.

## GitHub Actions

GitHub Actions dependencies are maintained through Dependabot and should be reviewed before merging updates.

## Commercial book boundary

The dependency policy covers the open-source companion code. Official commercial book editions remain at **https://ramsandesh.gumroad.com**.
