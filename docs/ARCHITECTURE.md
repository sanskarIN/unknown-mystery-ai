# Companion Architecture

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

The repository is intentionally small, dependency-light, and educational. It demonstrates production-minded AI engineering patterns without pretending that a teaching utility is a complete production platform.

## Layers

1. **Core utilities (`src/umai/`)** — deterministic, reusable Python helpers.
2. **Examples (`examples/`)** — runnable demonstrations with synthetic or local data.
3. **Tests (`tests/`)** — standard-library unit tests for expected behavior and edge cases.
4. **Documentation (`docs/`)** — implementation notes, governance checklists, and learning roadmaps.
5. **Automation (`.github/`)** — CI, release checks, contribution templates, and dependency maintenance.

## Design principles

- Prefer explicit data flow over hidden global state.
- Prefer deterministic examples when possible.
- Keep user payloads out of logs by default.
- Keep commercial book content outside the open-source repository.
- Treat model, prompt, data, and release identity as versioned evidence.
- Make failure modes visible and testable.

## Trust boundaries

The examples do not automatically call external AI providers. Any future integration should isolate credentials, validate inputs, record release identity, and document data handling before network access is enabled.

## License boundary

Source code is Apache-2.0 unless noted otherwise. The complete book, PDF/DOCX editions, chapter text, cover art, certificates, and commercial assets remain © 2026 Ram Sandesh, All Rights Reserved.
