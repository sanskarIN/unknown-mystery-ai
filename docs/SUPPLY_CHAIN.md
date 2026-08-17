# Software Supply-Chain Guidance

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

The companion keeps its dependency surface deliberately small, but build and automation inputs still form a software supply chain.

## Controls used here

- Apache-2.0 license and explicit NOTICE boundary,
- no third-party runtime dependencies in the stable core,
- GitHub Actions dependency updates through Dependabot,
- package metadata validation,
- source/wheel build verification,
- SHA-256 release artifact manifests,
- stable public API snapshots,
- source commit identity in release evidence,
- non-root container example.

## Maintainer review

Before accepting a new dependency or Action version, review its publisher, license, update history, required permissions, network/data behavior, and whether a narrower alternative exists.

## Build provenance

Checksums detect byte differences but do not by themselves prove who created an artifact. Stronger provenance can include protected branches, signed commits/tags where available, trusted CI identities, attestations, immutable source references, and reproducible build inputs.

## Release boundary

Do not place the paid eBook manuscript or commercial assets inside public software release artifacts. Official publication materials belong at **https://ramsandesh.gumroad.com**.
