"""Release-manifest helpers for reproducible AI project examples.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

from .reproducibility import fingerprint_json


@dataclass(frozen=True)
class ReleaseManifest:
    """A compact immutable record that identifies an AI release."""

    project: str
    version: str
    model_id: str
    data_id: str
    code_revision: str
    metrics: dict[str, float] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable dictionary."""
        return asdict(self)

    def fingerprint(self) -> str:
        """Return a stable fingerprint of the manifest fields."""
        return fingerprint_json(self.to_dict())

    def summary(self) -> str:
        """Return a concise human-readable release identifier."""
        return (
            f"{self.project}@{self.version} | model={self.model_id} | "
            f"data={self.data_id} | code={self.code_revision}"
        )
