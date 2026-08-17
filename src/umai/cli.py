"""Command-line entry point for the UMAI companion package.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from . import __version__
from .links import GITHUB_REPOSITORY, GUMROAD_STORE
from .reporting import to_json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="umai-companion",
        description="Utilities and project information for The Unknown Mystery of the AI companion repository.",
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("version", help="print the companion package version")
    subparsers.add_parser("store", help="print the official Gumroad store")
    subparsers.add_parser("repository", help="print the GitHub repository URL")

    info = subparsers.add_parser("info", help="print version and official project links")
    output = info.add_mutually_exclusive_group()
    output.add_argument("--compact", action="store_true", help="print one-line output")
    output.add_argument("--json", action="store_true", help="print structured JSON")
    return parser


def project_info() -> dict[str, str]:
    return {
        "version": __version__,
        "repository": GITHUB_REPOSITORY,
        "store": GUMROAD_STORE,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "version":
        print(__version__)
        return 0
    if args.command == "store":
        print(GUMROAD_STORE)
        return 0
    if args.command == "repository":
        print(GITHUB_REPOSITORY)
        return 0
    if args.command == "info":
        info = project_info()
        if args.compact:
            print(f"UMAI {info['version']} | {info['repository']} | {info['store']}")
        elif args.json:
            print(to_json(info))
        else:
            print(f"version: {info['version']}")
            print(f"repository: {info['repository']}")
            print(f"store: {info['store']}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
