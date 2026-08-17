import unittest

from umai.prompts import PromptTemplate


class PromptTemplateTests(unittest.TestCase):
    def test_variables_and_identity(self) -> None:
        prompt = PromptTemplate("summary", "1.0", "Summarize {topic} for {audience}.")
        self.assertEqual(prompt.variables(), ("topic", "audience"))
        self.assertEqual(prompt.identity, "summary@1.0")

    def test_render(self) -> None:
        prompt = PromptTemplate("greeting", "2", "Hello {name}")
        self.assertEqual(prompt.render(name="Reader"), "Hello Reader")

    def test_missing_variable(self) -> None:
        prompt = PromptTemplate("x", "1", "Use {value}")
        with self.assertRaises(KeyError):
            prompt.render()


if __name__ == "__main__":
    unittest.main()
