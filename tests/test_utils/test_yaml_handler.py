# tests/test_utils/test_yaml_handler.py

import unittest
from pathlib import Path
import tempfile
from capsule.utils.yaml_handler import YAMLHandler
from capsule.utils.exceptions import YAMLFileError

class TestYAMLHandler(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_write_and_read_success(self):
        file_path = self.temp_path / "test.yaml"
        data = {"key": "value", "items": [1, 2]}
        YAMLHandler.write(file_path, data)
        
        read_data = YAMLHandler.read(file_path)
        self.assertEqual(data, read_data)

    def test_read_file_not_found(self):
        file_path = self.temp_path / "non_existent.yaml"
        with self.assertRaises(YAMLFileError):
            YAMLHandler.read(file_path)

    def test_read_malformed_yaml(self):
        file_path = self.temp_path / "malformed.yaml"
        with open(file_path, "w") as f:
            f.write("key: value:\n  - item1")
        
        with self.assertRaises(YAMLFileError):
            YAMLHandler.read(file_path)

    def test_comment_preservation(self):
        file_path = self.temp_path / "comments.yaml"
        content = """
# This is a main comment
key: value  # This is an inline comment
items:
  - item1
  - item2
"""
        with open(file_path, "w") as f:
            f.write(content)

        data = YAMLHandler.read(file_path)
        
        new_file_path = self.temp_path / "comments_new.yaml"
        YAMLHandler.write(new_file_path, data)

        with open(new_file_path, "r") as f:
            new_content = f.read()
        
        # Note: ruamel.yaml might reformat slightly, but comments should be there.
        self.assertIn("# This is a main comment", new_content)
        self.assertIn("# This is an inline comment", new_content)

if __name__ == "__main__":
    unittest.main()
