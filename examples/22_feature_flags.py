"""Demonstrate explicit feature flags from a supplied mapping.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.config import FeatureFlags


flags = FeatureFlags(
    {
        "candidate_retriever": "enabled",
        "experimental_router": "false",
    }
)

print("candidate_retriever:", flags.enabled("candidate_retriever"))
print("experimental_router:", flags.enabled("experimental_router"))
print("missing flag default:", flags.enabled("missing"))
