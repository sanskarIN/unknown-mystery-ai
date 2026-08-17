"""A small in-memory artifact registry for governance demonstrations.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ArtifactVersion:
    name: str
    version: str
    digest: str
    approved: bool = False

    @property
    def identity(self) -> str:
        return f"{self.name}:{self.version}@{self.digest}"


class ArtifactRegistry:
    """Store artifact versions by `(name, version)` with explicit approval."""

    def __init__(self) -> None:
        self._items: dict[tuple[str, str], ArtifactVersion] = {}

    def register(self, artifact: ArtifactVersion) -> None:
        key = (artifact.name, artifact.version)
        if key in self._items and self._items[key] != artifact:
            raise ValueError("artifact version already exists with different metadata")
        self._items[key] = artifact

    def get(self, name: str, version: str) -> ArtifactVersion:
        try:
            return self._items[(name, version)]
        except KeyError as exc:
            raise KeyError(f"unknown artifact: {name}:{version}") from exc

    def approve(self, name: str, version: str) -> ArtifactVersion:
        current = self.get(name, version)
        approved = ArtifactVersion(current.name, current.version, current.digest, True)
        self._items[(name, version)] = approved
        return approved

    def approved_versions(self, name: str) -> list[ArtifactVersion]:
        return [item for item in self._items.values() if item.name == name and item.approved]
