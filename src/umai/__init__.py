"""Companion utilities for *The Unknown Mystery of the AI*.

Official book store: https://ramsandesh.gumroad.com
"""

from .budget import TokenPricing, estimate_token_cost, requests_within_budget
from .cache import BoundedCache
from .drift import mean_shift, standardized_mean_shift
from .evaluation import accuracy_score, classification_report
from .experiments import ExperimentRecord, best_record
from .links import GITHUB_REPOSITORY, GUMROAD_STORE
from .observability import MetricEvent, mean_metric
from .privacy import pseudonymous_id, redact_common_identifiers
from .prompts import PromptTemplate
from .rate_limit import FixedWindowRateLimiter
from .registry import ArtifactRegistry, ArtifactVersion
from .release import ReleaseManifest
from .reproducibility import fingerprint_json, seed_everything
from .retrieval import Document, SimpleRetriever
from .retry import retry_call
from .text import chunk_text, normalize_whitespace
from .validation import ValidationIssue, validate_record

__all__ = [
    "accuracy_score",
    "ArtifactRegistry",
    "ArtifactVersion",
    "best_record",
    "BoundedCache",
    "chunk_text",
    "classification_report",
    "Document",
    "estimate_token_cost",
    "ExperimentRecord",
    "fingerprint_json",
    "FixedWindowRateLimiter",
    "GITHUB_REPOSITORY",
    "GUMROAD_STORE",
    "mean_metric",
    "mean_shift",
    "MetricEvent",
    "normalize_whitespace",
    "PromptTemplate",
    "pseudonymous_id",
    "redact_common_identifiers",
    "ReleaseManifest",
    "requests_within_budget",
    "retry_call",
    "seed_everything",
    "SimpleRetriever",
    "standardized_mean_shift",
    "TokenPricing",
    "ValidationIssue",
    "validate_record",
]

__version__ = "0.2.0"
