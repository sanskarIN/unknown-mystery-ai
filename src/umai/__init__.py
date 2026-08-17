"""Companion utilities for *The Unknown Mystery of the AI*.

Official book store: https://ramsandesh.gumroad.com
"""

from .evaluation import accuracy_score, classification_report
from .links import GITHUB_REPOSITORY, GUMROAD_STORE
from .release import ReleaseManifest
from .reproducibility import fingerprint_json, seed_everything
from .retrieval import Document, SimpleRetriever

__all__ = [
    "accuracy_score",
    "classification_report",
    "Document",
    "fingerprint_json",
    "GITHUB_REPOSITORY",
    "GUMROAD_STORE",
    "ReleaseManifest",
    "seed_everything",
    "SimpleRetriever",
]

__version__ = "0.1.0"
