"""Create a SHA-256 manifest for release artifacts supplied on the command line.

Official publication: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import sys


def digest(path: Path) -> str:
    hasher = sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def main(arguments: list[str]) -> int:
    if not arguments:
        print("usage: python scripts/create_checksum_manifest.py FILE [FILE ...]")
        return 2

    missing = [value for value in arguments if not Path(value).is_file()]
    if missing:
        for value in missing:
            print("missing file:", value)
        return 1

    for value in arguments:
        path = Path(value)
        print(f"{digest(path)}  {path.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
