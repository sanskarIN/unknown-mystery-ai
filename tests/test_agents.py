import unittest

from umai.agents import Tool, ToolRegistry, select_tool


class AgentTests(unittest.TestCase):
    def test_register_and_invoke(self) -> None:
        registry = ToolRegistry()
        registry.register(Tool("double", "Double a value", lambda value: value * 2))
        self.assertEqual(registry.invoke("double", value=6), 12)

    def test_unknown_tool_raises(self) -> None:
        registry = ToolRegistry()
        with self.assertRaises(KeyError):
            registry.invoke("missing")

    def test_rule_router(self) -> None:
        self.assertEqual(select_tool("please ADD 2 and 3", {"add": "calculator"}), "calculator")


if __name__ == "__main__":
    unittest.main()
