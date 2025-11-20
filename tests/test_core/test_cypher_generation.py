import os
import unittest
from pathlib import Path
from capsule.models.capsule import Capsule
from capsule.core.packager import CapsulePackager
from capsule.models.cypher import CapsuleCypher
import frontmatter
import yaml


class TestCypherGeneration(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path("test_capsule")
        self.output_dir = Path("test_output")
        self.test_dir.mkdir(exist_ok=True)
        self.output_dir.mkdir(exist_ok=True)

        # Create dummy capsule structure
        (self.test_dir / "root_notes").mkdir(exist_ok=True)
        (self.test_dir / "media").mkdir(exist_ok=True)

        self.domain_template_dir = Path("capsule/templates/domains")
        self.domain_template_dir.mkdir(exist_ok=True)
        with open(self.domain_template_dir / "test.yaml", "w") as f:
            yaml.dump(
                {"data_schemas": {"note_schema": {"type": "object", "properties": {"title": {"type": "string"}}}}}, f
            )

        # Create dummy files
        with open(self.test_dir / "root_notes" / "note1.md", "w") as f:
            f.write("---\nid: note1\n---\n# Note 1")
        with open(self.test_dir / "root_notes" / "note2.md", "w") as f:
            f.write("---\nid: note2\n---\n# Note 2")
        with open(self.test_dir / "media" / "image.png", "w") as f:
            f.write("dummy image data")

        self.capsule = Capsule(
            capsule_id="test_capsule_v1",
            name="Test Capsule",
            version="1.0.0",
            domain_type="test",
        )
        self.packager = CapsulePackager(self.capsule, str(self.test_dir), str(self.output_dir))

    def tearDown(self):
        import shutil

        shutil.rmtree(self.test_dir)
        shutil.rmtree(self.output_dir)
        os.remove(self.domain_template_dir / "test.yaml")

    def test_data_schemas(self):
        cypher = self.packager.generate_cypher()
        self.assertIn("note_schema", cypher.data_schemas)
        self.assertEqual(cypher.data_schemas["note_schema"]["properties"]["title"]["type"], "string")

    def test_file_inventory(self):
        cypher = self.packager.generate_cypher()
        self.assertIn("root_notes", cypher.contents)
        self.assertEqual(len(cypher.contents["root_notes"]), 2)
        self.assertEqual(cypher.contents["root_notes"][0]["id"], "note1")
        self.assertEqual(cypher.contents["root_notes"][0]["file"], "root_notes/note1.md")
        self.assertEqual(cypher.contents["root_notes"][1]["id"], "note2")
        self.assertEqual(cypher.contents["root_notes"][1]["file"], "root_notes/note2.md")

    def test_folder_structure(self):
        cypher = self.packager.generate_cypher()
        self.assertIn("root", cypher.folder_structure)
        self.assertIn("root_notes", cypher.folder_structure["root"])
        self.assertIn("media", cypher.folder_structure["root"])

    def test_cypher_metadata(self):
        cypher = self.packager.generate_cypher()
        self.assertEqual(cypher.capsule_id, "test_capsule_v1")
        self.assertEqual(cypher.name, "Test Capsule")
        self.assertEqual(cypher.version, "1.0.0")
        self.assertEqual(cypher.domain_type, "test")

    def test_generate_cypher(self):
        cypher = self.packager.generate_cypher()

        # Test metadata
        self.assertEqual(cypher.capsule_id, "test_capsule_v1")
        self.assertEqual(cypher.name, "Test Capsule")
        self.assertEqual(cypher.version, "1.0.0")
        self.assertEqual(cypher.domain_type, "test")

        # Test folder structure
        self.assertIn("root", cypher.folder_structure)
        self.assertIn("root_notes", cypher.folder_structure["root"])
        self.assertIn("media", cypher.folder_structure["root"])

        # Test contents
        self.assertIn("root_notes", cypher.contents)
        self.assertEqual(len(cypher.contents["root_notes"]), 2)
        self.assertEqual(cypher.contents["root_notes"][0]["id"], "note1")
        self.assertEqual(cypher.contents["root_notes"][0]["file"], "root_notes/note1.md")
        self.assertEqual(cypher.contents["root_notes"][1]["id"], "note2")
        self.assertEqual(cypher.contents["root_notes"][1]["file"], "root_notes/note2.md")


if __name__ == "__main__":
    unittest.main()
