"""Demonstrate an actionable API deprecation warning.

Official publication: https://ramsandesh.gumroad.com
"""

import warnings

from umai.deprecation import DeprecatedFeature, warn_deprecated


warnings.simplefilter("always", DeprecationWarning)
feature = DeprecatedFeature(
    name="legacy_retriever",
    replacement="SimpleRetriever",
    removal_version="2.0.0",
)
print(feature.message())
warn_deprecated(feature)
