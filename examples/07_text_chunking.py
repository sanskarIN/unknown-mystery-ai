"""Demonstrate deterministic text chunking.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.text import chunk_text


TEXT = (
    "Reliable AI systems need clear inputs, measurable outputs, reproducible "
    "configuration, explicit release identity, privacy-aware telemetry, and "
    "tested failure handling. Chunking is one small transformation that should "
    "be evaluated rather than assumed to be universally optimal."
)

for index, chunk in enumerate(chunk_text(TEXT, max_words=12, overlap_words=3), start=1):
    print(f"chunk {index}: {chunk}")
