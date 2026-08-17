# 1.x Stability Guarantees

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

The 1.x line of the open-source companion package treats the documented symbols exported through `umai.__all__` as the stable public API.

## What maintainers aim to preserve

- documented import paths,
- documented parameter meaning,
- documented return structures,
- documented exception behavior,
- package command names,
- license and commercial-publication boundaries.

Backward-compatible additions may be made in minor versions. Bug fixes and documentation improvements may be made in patch versions.

## Deprecations

When a public API needs replacement, maintainers should document the replacement, emit an actionable deprecation warning where practical, record the change in the changelog, and retain the old path for at least one minor release unless security or correctness requires faster action.

## Teaching examples

Numbered examples are versioned learning contracts, but their printed demonstration values may change when a correction or clarity improvement is required. Each example should remain runnable, local/synthetic by default, and aligned with the public API available in its release line.

## Security and correctness

Compatibility is not a promise to preserve insecure or materially incorrect behavior. Security fixes may require faster changes, and those changes should be clearly documented.

## Book boundary

The stability promise covers the Apache-2.0 companion software. It does not relicense the commercial eBook, chapter text, PDF/DOCX editions, covers, certificates, or publication assets.

Official book editions: **https://ramsandesh.gumroad.com**.
