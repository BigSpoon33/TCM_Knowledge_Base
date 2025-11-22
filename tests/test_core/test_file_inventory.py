import unittest
from pathlib import Path
import tempfile
import shutil
from capsule.core.packager import CapsulePackager
from capsule.models.capsule import Capsule


class TestFileInventory(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.capsule_path = Path(self.test_dir) / "test_capsule"
        self.capsule_path.mkdir()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_flat_file_structure(self):
        # Create a simple capsule with a flat file structure
        (self.capsule_path / "note1.md").write_text("---\nid: note1\n---\n# Note 1")
        (self.capsule_path / "note2.md").write_text("---\nid: note2\n---\n# Note 2")

        capsule = Capsule(
            capsule_id="test_capsule",
            name="Test Capsule",
            version="1.0.0",
            domain_type="test",
        )
        packager = CapsulePackager(capsule, str(self.capsule_path), self.test_dir)

        contents, folder_structure = packager._scan_contents()

        self.assertIn("root", contents)
        self.assertEqual(len(contents["root"]), 2)
        self.assertEqual(contents["root"][0]["file"], "note1.md")
        self.assertEqual(contents["root"][1]["file"], "note2.md")
        self.assertIn("id", contents["root"][0])
        self.assertIn("id", contents["root"][1])

    def test_nested_folders(self):
        # Create a capsule with nested folders
        (self.capsule_path / "root_note.md").write_text("---\nid: root_note\n---\n# Root Note")
        (self.capsule_path / "folder1").mkdir()
        (self.capsule_path / "folder1" / "note1.md").write_text("---\nid: note1\n---\n# Note 1")
        (self.capsule_path / "folder1" / "subfolder").mkdir()
        (self.capsule_path / "folder1" / "subfolder" / "note2.md").write_text("---\nid: note2\n---\n# Note 2")

        capsule = Capsule(
            capsule_id="test_capsule",
            name="Test Capsule",
            version="1.0.0",
            domain_type="test",
        )
        packager = CapsulePackager(capsule, str(self.capsule_path), self.test_dir)

        contents, folder_structure = packager._scan_contents()

        self.assertIn("root", contents)
        self.assertEqual(len(contents["root"]), 1)
        self.assertEqual(contents["root"][0]["file"], "root_note.md")

        self.assertIn("folder1", contents)
        self.assertEqual(len(contents["folder1"]), 1)
        self.assertEqual(contents["folder1"][0]["file"], "folder1/note1.md")

        self.assertIn("folder1_subfolder", contents)
        self.assertEqual(len(contents["folder1_subfolder"]), 1)
        self.assertEqual(contents["folder1_subfolder"][0]["file"], "folder1/subfolder/note2.md")

    def test_various_file_types(self):
        # Create a capsule with various file types
        (self.capsule_path / "note.md").write_text("---\nid: note\n---\n# Note")
        (self.capsule_path / "image.jpg").touch()
        (self.capsule_path / "document.pdf").touch()

        capsule = Capsule(
            capsule_id="test_capsule",
            name="Test Capsule",
            version="1.0.0",
            domain_type="test",
        )
        packager = CapsulePackager(capsule, str(self.capsule_path), self.test_dir)

        contents, folder_structure = packager._scan_contents()

        self.assertIn("root", contents)
        self.assertEqual(len(contents["root"]), 1)
        self.assertEqual(contents["root"][0]["file"], "note.md")

    def test_empty_capsule(self):
        # Create an empty capsule
        capsule = Capsule(
            capsule_id="test_capsule",
            name="Test Capsule",
            version="1.0.0",
            domain_type="test",
        )
        packager = CapsulePackager(capsule, str(self.capsule_path), self.test_dir)

        contents, folder_structure = packager._scan_contents()

        self.assertEqual(len(contents), 0)
        self.assertEqual(len(folder_structure), 0)


if __name__ == "__main__":
    unittest.main()
