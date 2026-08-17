import unittest

from umai.retry import retry_call


class RetryTests(unittest.TestCase):
    def test_eventual_success(self) -> None:
        state = {"calls": 0}

        def operation() -> str:
            state["calls"] += 1
            if state["calls"] < 3:
                raise RuntimeError("temporary")
            return "ok"

        self.assertEqual(retry_call(operation, attempts=3, retry_on=(RuntimeError,)), "ok")
        self.assertEqual(state["calls"], 3)

    def test_error_after_limit(self) -> None:
        def operation() -> None:
            raise ValueError("still failing")

        with self.assertRaises(ValueError):
            retry_call(operation, attempts=2, retry_on=(ValueError,))

    def test_invalid_attempt_count(self) -> None:
        with self.assertRaises(ValueError):
            retry_call(lambda: None, attempts=0)


if __name__ == "__main__":
    unittest.main()
