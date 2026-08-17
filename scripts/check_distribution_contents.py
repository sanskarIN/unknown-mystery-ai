"""Verify required public files are present in built wheel and source archives.

Official publication: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from pathlib import Path
import sys
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

WHEEL_REQUIRED_SUFFIXES = (
    "umai/__init__.py",
    "umai/py.typed",
    ".dist-info/METADATA",
)

SDIST_REQUIRED_SUFFIXES = (
    "/README.md",
    "/LICENSE",
    "/NOTICE",
    "/CITATION.cff",
    "/pyproject.toml",
    "/src/umai/py.typed",
)


def has_suffix(names: list[str], suffix: str) -> bool:
    return any(name.endswith(suffix) for name in names)


def main() -> int:
    wheels = sorted(DIST.glob("*.whl"))
    sdists = sorted(DIST.glob("*.tar.gz"))
    failures: list[str] = []

    if len(wheels) != 1:
        failures.append(f"expected exactly one wheel, found {len(wheels)}")
    if len(sdists) != 1:
        failures.append(f"expected exactly one source distribution, found {len(sdists)}")

    if len(wheels) == 1:
        with zipfile.ZipFile(wheels[0]) as archive:
            names = archive.namelist()
        for suffix in WHEEL_REQUIRED_SUFFIXES:
            if not has_suffix(names, suffix):
                failures.append(f"wheel missing required path suffix: {suffix}")

    if len(sdists) == 1:
        with tarfile.open(sdists[0], mode="r:gz") as archive:
            names = archive.getnames()
        for suffix in SDIST_REQUIRED_SUFFIXES:
            if not has_suffix(names, suffix):
                failures.append(f"sdist missing required path suffix: {suffix}")

    if failures:
        print("Distribution contents: FAIL")
        for failure in failures:
            print("-", failure)
        return 1

    print("Distribution contents: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
