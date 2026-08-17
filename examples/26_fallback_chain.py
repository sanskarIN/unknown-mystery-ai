"""Demonstrate an explicit primary-to-backup fallback path.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.fallback import run_fallback_chain


def primary() -> str:
    raise RuntimeError("synthetic temporary outage")


result = run_fallback_chain(
    [
        ("primary", primary),
        ("backup", lambda: "backup response"),
    ]
)
print("provider:", result.provider)
print("attempts:", result.attempts)
print("value:", result.value)
