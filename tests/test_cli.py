import contextlib
import io
import json
import unittest

from umai.cli import main


class CliTests(unittest.TestCase):
    def capture(self, arguments: list[str]) -> tuple[int, str]:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = main(arguments)
        return code, buffer.getvalue()

    def test_version(self) -> None:
        code, output = self.capture(["version"])
        self.assertEqual(code, 0)
        self.assertRegex(output.strip(), r"^\d+\.\d+\.\d+$")

    def test_store(self) -> None:
        code, output = self.capture(["store"])
        self.assertEqual(code, 0)
        self.assertEqual(output.strip(), "https://ramsandesh.gumroad.com")

    def test_compact_info(self) -> None:
        code, output = self.capture(["info", "--compact"])
        self.assertEqual(code, 0)
        self.assertIn("github.com/sanskarIN/unknown-mystery-ai", output)
        self.assertIn("ramsandesh.gumroad.com", output)

    def test_json_info(self) -> None:
        code, output = self.capture(["info", "--json"])
        self.assertEqual(code, 0)
        payload = json.loads(output)
        self.assertEqual(payload["store"], "https://ramsandesh.gumroad.com")
        self.assertIn("unknown-mystery-ai", payload["repository"])


if __name__ == "__main__":
    unittest.main()
