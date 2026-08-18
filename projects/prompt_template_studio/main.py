"""Versioned prompt-template rendering project."""

from __future__ import annotations

from umai import PromptTemplate, to_json


def main() -> None:
    template = PromptTemplate(
        name="evidence-answer",
        version="2.0",
        template=(
            "Question: {question}\n"
            "Evidence: {evidence}\n"
            "Instruction: Answer only from the supplied evidence and state uncertainty when needed."
        ),
    )
    rendered = template.render(
        question="What should be checked before an AI release?",
        evidence="Evaluation, privacy review, observability, and rollback readiness should be explicit.",
    )
    print(
        to_json(
            {
                "identity": template.identity,
                "variables": list(template.variables()),
                "rendered": rendered,
            }
        )
    )


if __name__ == "__main__":
    main()
