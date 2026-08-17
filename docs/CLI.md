# Companion CLI

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

After installing the repository in editable mode, the `umai-companion` command provides a small dependency-free interface for project metadata.

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
```

The CLI deliberately avoids network requests and provider credentials. It is a stable place for lightweight companion reporting and project navigation.

## Example

```text
version: 0.6.0
repository: https://github.com/sanskarIN/unknown-mystery-ai
store: https://ramsandesh.gumroad.com
```

The exact version changes over time. The official commercial publication remains available at **https://ramsandesh.gumroad.com**.
