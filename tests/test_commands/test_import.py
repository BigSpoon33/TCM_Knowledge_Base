from unittest.mock import patch, MagicMock
import pytest
import yaml
from pathlib import Path
from typer.testing import CliRunner
from capsule.cli import app
from capsule.core.packager import Packager
from capsule.models.config import Config

runner = CliRunner()


@pytest.fixture
def mock_config(monkeypatch, tmp_path):
    mock_class = MagicMock()
    mock_instance = MagicMock(spec=Config)
    mock_class.load_config.return_value = mock_instance

    # Set vault path to a temp dir
    vault_path = tmp_path / "vault"
    vault_path.mkdir()
    mock_instance.get.return_value = str(vault_path)

    monkeypatch.setattr("capsule.commands.import_cmd.Config", mock_class)
    return vault_path


@pytest.fixture
def valid_capsule_zip(tmp_path):
    capsule_path = tmp_path / "source_capsule"
    capsule_path.mkdir()
    cypher_content = {
        "capsule_id": "test_capsule",
        "name": "Test Capsule",
        "version": "1.0.0",
        "domain_type": "test",
        "folder_structure": {},
        "contents": {"root": [{"file": "test.md"}]},
        "data_schemas": {},
    }
    with open(capsule_path / "capsule-cypher.yaml", "w") as f:
        yaml.dump(cypher_content, f)

    (capsule_path / "test.md").write_text("Test content")

    # Package it
    packager = Packager(capsule_path)
    zip_path = tmp_path / "test_capsule.zip"
    packager.package_to_zip(zip_path)

    return zip_path


def test_import_dry_run(mock_config, valid_capsule_zip):
    result = runner.invoke(app, ["import", str(valid_capsule_zip), "--dry-run"])

    if result.exit_code != 0:
        print(f"Output: {result.output}")
        print(f"Exception: {result.exception}")

    assert result.exit_code == 0
    assert "[Dry Run]" in result.stdout
    # assert "Preview of import" in result.stdout


def test_import_yes(mock_config, valid_capsule_zip):
    # Mock create_backup to avoid actual backup logic if it's complex,
    # but real Importer calls it. Let's mock it to keep test focused on import.
    with patch("capsule.commands.import_cmd.create_backup") as mock_backup:
        result = runner.invoke(app, ["import", str(valid_capsule_zip), "--yes"])

        assert result.exit_code == 0
        assert "Import execution completed" in result.stdout

        # Verify file exists in vault
        vault_path = mock_config
        # Importer usually creates a folder for the capsule or merges.
        # Let's check if test.md exists somewhere.
        # Based on Importer logic, it should be in vault/test_capsule/test.md (if folder structure is default)
        # or just vault/test.md if root is .
        # Let's check recursively
        assert list(vault_path.rglob("test.md"))


def test_import_interactive_yes(mock_config, valid_capsule_zip):
    with patch("capsule.commands.import_cmd.questionary.confirm") as mock_confirm:
        mock_confirm.return_value.ask.return_value = True
        with patch("capsule.commands.import_cmd.create_backup"):
            result = runner.invoke(app, ["import", str(valid_capsule_zip)])

            assert result.exit_code == 0
            assert "Import execution completed" in result.stdout


def test_import_interactive_no(mock_config, valid_capsule_zip):
    with patch("capsule.commands.import_cmd.questionary.confirm") as mock_confirm:
        mock_confirm.return_value.ask.return_value = False
        result = runner.invoke(app, ["import", str(valid_capsule_zip)])

        assert result.exit_code == 0
        assert "Import cancelled" in result.stdout

        # Verify NO file exists in vault
        vault_path = mock_config
        assert not list(vault_path.rglob("test.md"))


def test_import_error(mock_config, tmp_path):
    # Create invalid zip (not a zip file)
    invalid_zip = tmp_path / "invalid.zip"
    invalid_zip.write_text("not a zip")

    result = runner.invoke(app, ["import", str(invalid_zip)])

    assert result.exit_code == 1
    assert "Error" in result.stdout
