import unittest

from umai.reproducibility import canonical_json, fingerprint_json, seed_everything


class ReproducibilityTests(unittest.TestCase):
    def test_canonical_json_orders_keys(self) -> None:
        self.assertEqual(canonical_json({"b": 2, "a": 1}), '{"a":1,"b":2}')

    def test_fingerprint_is_stable_for_key_order(self) -> None:
        left = fingerprint_json({"b": 2, "a": 1})
        right = fingerprint_json({"a": 1, "b": 2})
        self.assertEqual(left, right)

    def test_seed_requires_integer(self) -> None:
        with self.assertRaises(TypeError):
            seed_everything("42")  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
