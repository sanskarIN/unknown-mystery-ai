import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "projects" / "catalog.json"


class ProjectCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(CATALOG.read_text(encoding="utf-8"))
        cls.projects = cls.data["projects"]

    def test_catalog_has_25_unique_projects(self) -> None:
        ids = [item["id"] for item in self.projects]
        self.assertEqual(len(ids), 25)
        self.assertEqual(len(set(ids)), 25)

    def test_catalog_has_five_capstone_snapshots(self) -> None:
        capstones = [item for item in self.projects if item["snapshot"]]
        self.assertEqual(len(capstones), 5)
        self.assertTrue(all(item["level"] == "capstone" for item in capstones))

    def test_catalog_matches_project_entrypoints(self) -> None:
        catalog_ids = {item["id"] for item in self.projects}
        discovered = {path.parent.name for path in (ROOT / "projects").glob("*/main.py")}
        self.assertEqual(catalog_ids, discovered)

    def test_catalog_uses_canonical_store(self) -> None:
        self.assertEqual(self.data["official_store"], "https://ramsandesh.gumroad.com")


if __name__ == "__main__":
    unittest.main()
