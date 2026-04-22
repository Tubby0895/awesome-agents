import json
import pathlib
import subprocess
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_catalog.py"


class GenerateCatalogTest(unittest.TestCase):
    def test_generator_exists(self) -> None:
        self.assertTrue(SCRIPT.exists(), "scripts/generate_catalog.py must exist")

    def test_generated_root_readme_contains_required_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = pathlib.Path(tmp)
            subprocess.run(
                ["python3", str(SCRIPT), "--output-dir", str(output_dir)],
                check=True,
                cwd=ROOT,
            )

            readme = (output_dir / "README.md").read_text()

            self.assertIn("## Quick Start", readme)
            self.assertIn("## Beginner Picks", readme)
            self.assertIn("## Submit an Agent", readme)
            self.assertIn("## Browse By Category", readme)

    def test_catalog_metadata_has_required_fields(self) -> None:
        catalog = json.loads((ROOT / "agents.json").read_text())

        self.assertIn("beginnerPicks", catalog)
        self.assertIn("featuredStacks", catalog)

        for category in catalog["categories"]:
            self.assertIn("description", category)
            for agent in category["agents"]:
                self.assertIn("name", agent)
                self.assertIn("tags", agent)
                self.assertIn("bestFor", agent)
                self.assertIn("maturity", agent)
                self.assertIn("requires", agent)


if __name__ == "__main__":
    unittest.main()
