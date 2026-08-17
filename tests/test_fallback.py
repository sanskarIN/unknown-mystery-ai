import unittest

from umai.fallback import run_fallback_chain


class FallbackTests(unittest.TestCase):
    def test_fallback_to_second_provider(self) -> None:
        def first() -> str:
            raise RuntimeError("temporary")

        result = run_fallback_chain([("primary", first), ("backup", lambda: "ok")])
        self.assertEqual(result.provider, "backup")
        self.assertEqual(result.value, "ok")
        self.assertEqual(result.attempts, ("primary", "backup"))

    def test_non_recoverable_error_is_not_hidden(self) -> None:
        def invalid() -> str:
            raise ValueError("invalid")

        with self.assertRaises(ValueError):
            run_fallback_chain([("primary", invalid)], recoverable=(RuntimeError,))

    def test_empty_chain_rejected(self) -> None:
        with self.assertRaises(ValueError):
            run_fallback_chain([])


if __name__ == "__main__":
    unittest.main()
