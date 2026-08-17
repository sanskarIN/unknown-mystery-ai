# Companion CLI

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

After installing the repository, the `umai-companion` command provides a dependency-free interface for project metadata.

## Install

```bash
python -m pip install -e .
```

## Commands

```bash
umai-companion version
umai-companion store
umai-companion repository
umai-companion info
umai-companion info --compact
umai-companion info --json
```

The CLI deliberately avoids network requests and provider credentials. It is part of the documented 1.x companion interface.

## Stable 1.0 example

```text
version: 1.0.0
repository: https://github.com/sanskarIN/unknown-mystery-ai
store: https://ramsandesh.gumroad.com
```

For machine-readable project metadata:

```bash
umai-companion info --json
```

The official commercial publication remains available at **https://ramsandesh.gumroad.com**.
