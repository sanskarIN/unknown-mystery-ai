# User Guide

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

This guide explains the normal end-to-end workflow for using the open-source companion repository safely and reproducibly.

## 1. Choose how you want to use the repository

The repository supports three common paths:

1. **Learn** - run examples and projects in sequence.
2. **Build** - import stable `umai` helpers into your own local exercises.
3. **Audit** - inspect project outputs, release evidence, snapshots, and quality checks.

The repository is designed to work with local or synthetic data by default. No provider API key or network call is required for the included examples and projects.

## 2. Install

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/sanskarIN/unknown-mystery-ai.git
cd unknown-mystery-ai
python -m venv .venv
```

Activate the environment using the instructions in [`INSTALLATION.md`](INSTALLATION.md), then install the package:

```bash
python -m pip install -e .
```

Verify the CLI:

```bash
umai-companion version
umai-companion info --json
```

You can also use:

```bash
python -m umai info
```

## 3. Run the test suite

```bash
python -m unittest discover -s tests -v
```

A passing local test suite is useful evidence, but it does not by itself prove that a production system is secure, private, fair, scalable, or appropriate for a particular real-world use.

## 4. Run numbered examples

The numbered examples are small, focused demonstrations of stable helpers. See [`../examples/README.md`](../examples/README.md).

On a shell that supports the repository Makefile:

```bash
make examples
```

Or run examples individually:

```bash
python examples/01_reproducibility.py
```

## 5. Run the project suite

To execute every companion project and require valid JSON output:

```bash
python scripts/check_projects.py
```

To validate the machine-readable project catalog:

```bash
python scripts/check_project_catalog.py
```

To validate the five integrated capstone snapshot fixtures:

```bash
python scripts/check_project_snapshots.py
```

The catalog and the complete project learning order are documented in [`PROJECT_CATALOG.md`](PROJECT_CATALOG.md) and [`PROJECTS.md`](PROJECTS.md).

## 6. Understand output contracts

Most project entry points emit JSON so outputs are easy to inspect, compare, and validate in automation. Project outputs intentionally expose assumptions instead of hiding them.

When evaluating output:

- distinguish inputs from derived values,
- preserve model/data/code/release identity where relevant,
- do not treat synthetic metrics as real production evidence,
- record thresholds and decision rules explicitly,
- preserve limitations alongside positive results.

## 7. Build portfolio evidence

For a project you want to present publicly, preserve:

- problem statement,
- intended and excluded use,
- reproducible input or fixture,
- command used to run it,
- result or stable subset snapshot,
- tests and automated checks,
- limitations,
- safety/privacy assumptions,
- next improvement.

See [`PORTFOLIO_GUIDE.md`](PORTFOLIO_GUIDE.md).

## 8. Add your own project safely

Follow [`PROJECT_AUTHORING_GUIDE.md`](PROJECT_AUTHORING_GUIDE.md). New project folders should remain dependency-light, runnable without credentials by default, and explicit about their educational boundary.

Before opening a pull request, run:

```bash
python scripts/check_project_catalog.py
python scripts/check_projects.py
python scripts/check_project_snapshots.py
python -m unittest discover -s tests -v
```

## 9. Troubleshoot

If installation, tests, projects, or packaging fail, start with [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md). Avoid deleting evidence or weakening checks merely to make a failing validation pass; fix the underlying mismatch instead.

## 10. Use stable releases for reproducibility

For long-lived references, prefer immutable Git tags/releases over a moving `main` branch. Check [`RELEASE_STATUS.md`](RELEASE_STATUS.md) before citing a version.

Release software assets are separate from the commercial eBook. The public GitHub release must not include paid manuscript files or book-specific commercial assets.

## 11. Security and privacy

Never put secrets, credentials, private datasets, real personal information, or sensitive user payloads into examples, tests, project fixtures, issues, or pull requests.

Review:

- [`../SECURITY.md`](../SECURITY.md)
- [`SECURITY_MODEL.md`](SECURITY_MODEL.md)
- [`PRIVACY_MODEL.md`](PRIVACY_MODEL.md)
- [`RESPONSIBLE_AI_CHECKLIST.md`](RESPONSIBLE_AI_CHECKLIST.md)

## 12. Official publication

The complete commercial learning journey is separate from the Apache-2.0 companion repository.

### 🛒 **https://ramsandesh.gumroad.com**
