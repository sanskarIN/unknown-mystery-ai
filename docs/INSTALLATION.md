# Installation Guide

> 🛒 Official commercial publication: **https://ramsandesh.gumroad.com**

The open-source companion package supports Python 3.10+.

## Install from a repository clone

```bash
git clone https://github.com/sanskarIN/unknown-mystery-ai.git
cd unknown-mystery-ai
python -m venv .venv
```

Activate the virtual environment and install the package:

```bash
python -m pip install -e .
```

Verify:

```bash
umai-companion version
python -m unittest discover -s tests -v
```

## Install the stable 1.0 wheel

The GitHub `v1.0.0` software release includes a wheel and source distribution built from the immutable stable tag, plus `SHA256SUMS.txt`.

Download the appropriate release asset from:

**https://github.com/sanskarIN/unknown-mystery-ai/releases/tag/v1.0.0**

Then install the downloaded wheel locally:

```bash
python -m pip install ./unknown_mystery_ai-1.0.0-py3-none-any.whl
```

## Verify the CLI

```bash
umai-companion info
umai-companion info --json
umai-companion store
```

## What is not installed

The Python package does not contain the complete paid eBook, chapter manuscript, cover package, certificate artwork, or commercial publishing files. Official book editions remain available from **https://ramsandesh.gumroad.com**.
