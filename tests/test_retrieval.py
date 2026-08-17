import unittest

from umai.retrieval import Document, SimpleRetriever, tokenize


class RetrievalTests(unittest.TestCase):
    def test_tokenize(self) -> None:
        self.assertEqual(tokenize("RAG + MLOps!"), ["rag", "mlops"])

    def test_relevant_document_ranks_first(self) -> None:
        retriever = SimpleRetriever(
            [
                Document("rag", "retrieval augmented generation uses retrieved evidence"),
                Document("cv", "computer vision processes images"),
            ]
        )
        results = retriever.search("retrieval evidence", top_k=1)
        self.assertEqual(results[0][0].doc_id, "rag")
        self.assertGreater(results[0][1], 0.0)

    def test_empty_documents_rejected(self) -> None:
        with self.assertRaises(ValueError):
            SimpleRetriever([])


if __name__ == "__main__":
    unittest.main()
