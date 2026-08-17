import subprocess
import sys
import unittest


class ModuleEntrypointTests(unittest.TestCase):
    def test_python_m_umai_version(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-m", "umai", "version"],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertRegex(completed.stdout.strip(), r"^\d+\.\d+\.\d+$")


if __name__ == "__main__":
    unittest.main()
