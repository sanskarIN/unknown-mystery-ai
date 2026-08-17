# Companion CLI

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

After installing the repository, the `umai-companion` command provides a dependency-free interface for project metadata. The same CLI is available through `python -m umai`.

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

Equivalent module execution:

```bash
python -m umai version
python -m umai info
python -m umai info --json
```

The CLI deliberately avoids network requests and provider credentials. It is part of the documented 1.x companion interface.

## Stable 1.0.1 example

```text
version: 1.0.1
repository: https://github.com/sanskarIN/unknown-mystery-ai
store: https://ramsandesh.gumroad.com
```

For machine-readable project metadata:

```bash
umai-companion info --json
```

The official commercial publication remains available at **https://ramsandesh.gumroad.com**.
