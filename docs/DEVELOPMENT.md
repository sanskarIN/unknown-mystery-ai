# Development Guide

> 🛒 **Official Gumroad store:** https://ramsandesh.gumroad.com

## Requirements

- Python 3.10+
- Git

## Setup

```bash
git clone https://github.com/sanskarIN/unknown-mystery-ai.git
cd unknown-mystery-ai
python -m venv .venv
```

Activate the environment and install editable:

```bash
python -m pip install -e .
```

## Maintainer Git identity

```bash
git config user.name "Sanskar"
git config user.email "sanskarin@outlook.in"
```

## Test

```bash
python -m unittest discover -s tests -v
```

## Build

```bash
python -m pip install build
python -m build
```

## Contribution rules

Keep new utilities dependency-light, deterministic where practical, documented, tested, and safe for learners. Do not commit API keys, private datasets, commercial manuscript files, or copyrighted assets that are not licensed for repository distribution.
