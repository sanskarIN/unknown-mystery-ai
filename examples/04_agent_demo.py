"""Transparent tool-routing example for agent lessons.

Book store: https://ramsandesh.gumroad.com
"""

from umai.agents import Tool, ToolRegistry, select_tool


def add(a: int, b: int) -> int:
    return a + b


def echo(text: str) -> str:
    return text


def main() -> None:
    registry = ToolRegistry()
    registry.register(Tool("add", "Add two integers", add))
    registry.register(Tool("echo", "Echo a short message", echo))

    route = select_tool("please add these values", {"add": "add", "echo": "echo"})
    if route == "add":
        result = registry.invoke(route, a=7, b=5)
        print("Tool result:", result)

    print("Registered tools:", registry.names())
    print("Book store: https://ramsandesh.gumroad.com")


if __name__ == "__main__":
    main()
