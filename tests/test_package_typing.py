import importlib.resources
import unittest


class PackageTypingTests(unittest.TestCase):
    def test_py_typed_marker_is_packaged(self) -> None:
        marker = importlib.resources.files("umai").joinpath("py.typed")
        self.assertTrue(marker.is_file())


if __name__ == "__main__":
    unittest.main()
