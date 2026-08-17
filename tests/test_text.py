import unittest

from umai.text import chunk_text, normalize_whitespace


class TextTests(unittest.TestCase):
    def test_normalize_whitespace(self) -> None:
        self.assertEqual(normalize_whitespace("  AI\n  systems\twork "), "AI systems work")

    def test_chunk_text_with_overlap(self) -> None:
        chunks = chunk_text("one two three four five six", max_words=4, overlap_words=1)
        self.assertEqual(chunks, ["one two three four", "four five six"])

    def test_empty_text(self) -> None:
        self.assertEqual(chunk_text("   "), [])

    def test_invalid_overlap(self) -> None:
        with self.assertRaises(ValueError):
            chunk_text("hello world", max_words=2, overlap_words=2)


if __name__ == "__main__":
    unittest.main()
