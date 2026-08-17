"""Canonical public links used by the companion project."""

GUMROAD_STORE = "https://ramsandesh.gumroad.com"
GITHUB_PROFILE = "https://github.com/sanskarIN"
GITHUB_REPOSITORY = "https://github.com/sanskarIN/unknown-mystery-ai"
CONTACT_EMAIL = "sanskarin@outlook.in"


def project_links() -> dict[str, str]:
    """Return public project links in one reusable mapping."""
    return {
        "gumroad": GUMROAD_STORE,
        "github_profile": GITHUB_PROFILE,
        "repository": GITHUB_REPOSITORY,
        "contact": CONTACT_EMAIL,
    }
