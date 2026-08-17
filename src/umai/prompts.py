"""Versioned prompt templates with explicit variables.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass
import string


@dataclass(frozen=True)
class PromptTemplate:
    """A small immutable prompt template with a declared version."""

    name: str
    version: str
    template: str

    def variables(self) -> tuple[str, ...]:
        fields: list[str] = []
        for _, field_name, _, _ in string.Formatter().parse(self.template):
            if field_name and field_name not in fields:
                fields.append(field_name)
        return tuple(fields)

    def render(self, **values: object) -> str:
        missing = [name for name in self.variables() if name not in values]
        if missing:
            raise KeyError(f"missing prompt variables: {', '.join(missing)}")
        return self.template.format(**values)

    @property
    def identity(self) -> str:
        return f"{self.name}@{self.version}"
