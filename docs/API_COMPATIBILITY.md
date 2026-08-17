# Public API Compatibility Policy

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

This policy applies to the open-source `umai` companion package, not to the commercial book manuscript.

## Public API

A symbol is considered public when it is exported through `umai.__all__` and documented in `docs/API_REFERENCE.md`.

Internal implementation details, underscored names, examples, test fixtures, and undocumented module internals are not guaranteed stable.

## Versioning

The package follows semantic versioning:

- **PATCH** — compatible bug fixes and documentation corrections.
- **MINOR** — new backward-compatible public functionality.
- **MAJOR** — intentional incompatible public API changes.

## Deprecation process

Before removing or incompatibly changing a public symbol in a stable major version:

1. Mark the symbol deprecated in documentation.
2. Provide a clear replacement when one exists.
3. Emit a `DeprecationWarning` from the deprecated path when practical.
4. Record the deprecation in `CHANGELOG.md`.
5. Keep the deprecated path through at least one minor release unless a security or correctness issue requires faster removal.

## Compatibility promises

For the 1.x line, maintainers should preserve:

- documented function names and import paths,
- required positional argument meaning,
- documented return-shape contracts,
- explicit exception behavior where documented,
- package metadata and license boundaries.

New optional parameters may be added when they preserve existing behavior.

## Non-guarantees

Teaching examples may evolve to improve clarity. Numerical demonstration values, documentation wording, and internal implementation details may change without being treated as public API breaks.

## Commercial publication boundary

The eBook, chapter text, cover artwork, certificates, and commercial assets remain separately copyrighted. Official editions are distributed through **https://ramsandesh.gumroad.com**.
