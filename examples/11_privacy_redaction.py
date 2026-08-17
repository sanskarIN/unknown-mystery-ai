"""Demonstrate basic privacy-aware log preparation.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.privacy import pseudonymous_id, redact_common_identifiers


raw = "request from learner@example.com, phone +91 98765 43210"
print("before:", raw)
print("after: ", redact_common_identifiers(raw))
print("pseudonymous session:", pseudonymous_id("session-001"))
print("These helpers are teaching baselines and do not replace a complete privacy review.")
