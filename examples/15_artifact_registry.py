"""Demonstrate explicit artifact registration and approval.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.registry import ArtifactRegistry, ArtifactVersion


registry = ArtifactRegistry()
registry.register(ArtifactVersion("classifier", "1.0", "sha256-demo-a"))
registry.register(ArtifactVersion("classifier", "1.1", "sha256-demo-b"))

approved = registry.approve("classifier", "1.1")
print("approved:", approved.identity)
print("approved versions:", [item.version for item in registry.approved_versions("classifier")])
