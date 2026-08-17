"""Evaluate a synthetic retrieval result with simple ranking metrics.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.ranking import precision_at_k, recall_at_k, reciprocal_rank


retrieved = ["doc-4", "doc-2", "doc-7", "doc-1"]
relevant = {"doc-2", "doc-1"}

print("precision@3:", round(precision_at_k(retrieved, relevant, 3), 3))
print("recall@3:", round(recall_at_k(retrieved, relevant, 3), 3))
print("reciprocal rank:", round(reciprocal_rank(retrieved, relevant), 3))
