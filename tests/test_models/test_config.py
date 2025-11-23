# tests/test_models/test_config.py

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from capsule.exceptions import ConfigError
from capsule.models.config import Config, yaml


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)
        self.config_data = {
            "llm_provider": "openai",
            "api_key": "test_key",
            "default_model": "gpt-4",
            "project_dir": self.temp_path,
            "user": {},
            "research": {},
            "import_settings": {},
        }
        self.config = Config(**self.config_data)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_initialization(self):
        self.assertEqual(self.config.llm_provider, "openai")
        self.assertEqual(self.config.api_key, "test_key")
        self.assertEqual(self.config.default_model, "gpt-4")
        self.assertEqual(self.config.project_dir, self.temp_path)

    def test_to_dict(self):
        expected_dict = self.config_data.copy()
        expected_dict["project_dir"] = str(self.temp_path)
        expected_dict["import"] = expected_dict.pop("import_settings")
        # Add default logging config
        expected_dict["logging"] = {
            "level": "INFO",
            "file_path": "~/.capsule/logs/capsule.log",
            "rotate_bytes": 5 * 1024 * 1024,
            "backup_count": 3,
        }
        self.assertDictEqual(self.config.to_dict(), expected_dict)

    def test_to_from_yaml_file(self):
        file_path = self.temp_path / "config.yaml"
        self.config.to_yaml_file(file_path)
        self.assertTrue(file_path.exists())

        loaded_config = Config.from_yaml_file(file_path)
        self.assertDictEqual(loaded_config.to_dict(), self.config.to_dict())

    def test_validation_success(self):
        self.config.validate()

    def test_validation_failure(self):
        config = Config(api_key=None)
        with self.assertRaisesRegex(ConfigError, "API key is not set"):
            config.validate()


class TestConfigLoading(unittest.TestCase):
    def setUp(self):
        self.original_cwd = os.getcwd()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)

        # Mock project and home directories
        self.mock_project_dir = self.temp_path / "project"
        self.mock_home_dir = self.temp_path / "home"
        self.mock_project_dir.mkdir()
        self.mock_home_dir.mkdir()

        # Patch Path.home() to return our mock home directory
        self.patcher = patch("pathlib.Path.home", return_value=self.mock_home_dir)
        self.patcher.start()

    def tearDown(self):
        os.chdir(self.original_cwd)
        self.temp_dir.cleanup()
        self.patcher.stop()

    def test_load_config_no_files(self):
        os.chdir(self.mock_project_dir)
        config = Config.load_config()
        self.assertEqual(config, Config())  # Should be default config

    def test_load_config_global_only(self):
        # Create global config
        global_config_dir = self.mock_home_dir / ".config" / "capsule"
        global_config_dir.mkdir(parents=True)
        with open(global_config_dir / "config.yaml", "w") as f:
            yaml.dump({"api_key": "global_key"}, f)

        os.chdir(self.mock_project_dir)
        config = Config.load_config()
        self.assertEqual(config.api_key, "global_key")
        self.assertEqual(config.default_model, "gpt-4-turbo")  # Default

    def test_load_config_local_only(self):
        # Create local config
        local_config_dir = self.mock_project_dir / ".capsule"
        local_config_dir.mkdir()
        with open(local_config_dir / "config.yaml", "w") as f:
            yaml.dump({"api_key": "local_key"}, f)

        os.chdir(self.mock_project_dir)
        config = Config.load_config()
        self.assertEqual(config.api_key, "local_key")

    def test_load_config_local_overrides_global(self):
        # Create global config
        global_config_dir = self.mock_home_dir / ".config" / "capsule"
        global_config_dir.mkdir(parents=True)
        with open(global_config_dir / "config.yaml", "w") as f:
            yaml.dump({"api_key": "global_key", "default_model": "gpt-3.5"}, f)

        # Create local config
        local_config_dir = self.mock_project_dir / ".capsule"
        local_config_dir.mkdir()
        with open(local_config_dir / "config.yaml", "w") as f:
            yaml.dump({"api_key": "local_key"}, f)

        os.chdir(self.mock_project_dir)
        config = Config.load_config()
        self.assertEqual(config.api_key, "local_key")  # Local overrides
        self.assertEqual(config.default_model, "gpt-3.5")  # Global is used


if __name__ == "__main__":
    unittest.main()
