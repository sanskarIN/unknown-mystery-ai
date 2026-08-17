"""Demonstrate explicit prompt identity and rendering.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.prompts import PromptTemplate


prompt = PromptTemplate(
    name="evidence-summary",
    version="1.0",
    template="Summarize {evidence} for a {audience} audience without inventing facts.",
)

print("prompt identity:", prompt.identity)
print("variables:", prompt.variables())
print(prompt.render(evidence="three synthetic validation results", audience="technical"))
