# Compatibility Matrix

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

This document summarizes the supported and continuously validated compatibility surface for the companion repository.

## Python

The package metadata declares:

```text
Python >= 3.10
```

The CI workflow validates the unit-test suite on:

- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13

The Project Matrix currently validates the complete project suite on multiple supported Python versions across Linux, Windows, and macOS.

## Operating systems

The code is intended to be operating-system independent where practical.

Automated project verification covers:

- Ubuntu / Linux
- Windows
- macOS

Python source should use `pathlib.Path` or other cross-platform standard-library APIs instead of assuming POSIX path separators.

## Runtime dependencies

The stable companion package intentionally has no mandatory third-party runtime dependencies. Examples and projects normally use:

- Python standard library
- the local `umai` package

Build tooling such as `setuptools` and `build` is used for packaging but is not a normal runtime requirement for end users.

## CLI compatibility

Supported forms:

```bash
umai-companion version
umai-companion info
umai-companion info --json
umai-companion store
python -m umai info
```

The console entry point and module entry point are both covered by tests.

## Public API compatibility

The 1.x line treats the committed `umai.__all__` symbol set as stable unless a documented compatibility exception is required for security or material correctness.

Validate with:

```bash
python scripts/check_public_api.py --require-version-match
```

See [`API_COMPATIBILITY.md`](API_COMPATIBILITY.md) and [`STABILITY.md`](STABILITY.md).

## Project output compatibility

All project default runs must:

- exit successfully,
- emit valid JSON,
- remain non-interactive,
- require no provider credential by default.

The five integrated capstones additionally validate selected stable fields against committed `expected.json` fixtures.

## Packaging compatibility

The quality workflow builds both:

- wheel distribution,
- source distribution.

Distribution-content checks verify required package content, including the PEP 561 `py.typed` marker.

## GitHub Actions compatibility

External actions are pinned to full commit SHAs. Workflow permissions should remain minimal and pull-request checks should not depend on repository secrets for the normal public validation path.

## Container example

The included Dockerfile is an educational non-root container example. Container behavior may vary by host engine and is not used to redefine the package's Python compatibility contract.

## What is not guaranteed

This repository does not guarantee compatibility with:

- end-of-life Python versions below 3.10,
- every shell implementation,
- every container runtime configuration,
- arbitrary third-party model providers,
- vendor-specific GPU/NPU runtimes,
- undocumented private APIs,
- a future major version after 1.x without migration guidance.

## Official publication

### 🛒 **https://ramsandesh.gumroad.com**
