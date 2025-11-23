from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from capsule.cli import app
from capsule.core.importer import CapsuleInfo, Impact, ImportPreview
from capsule.exceptions import CapsuleError

runner = CliRunner()


@pytest.fixture
def mock_importer():
    with patch("capsule.commands.import_cmd.Importer") as MockImporter:
        mock_instance = MockImporter.return_value
        yield mock_instance


@pytest.fixture
def mock_config():
    with patch("capsule.commands.import_cmd.Config") as MockConfig:
        mock_instance = MockConfig.load_config.return_value
        mock_instance.get.return_value = "/tmp/vault"
        yield mock_instance


@pytest.fixture
def mock_preview():
    return ImportPreview(
        capsule_info=CapsuleInfo(id="test", version="1.0.0", file_count=1, name="Test", domain_type="test"),
        impact=Impact(new_files=1, updated_files=0, conflicts=0),
        new_files=["test.md"],
        updates=[],
        conflicts=[],
    )


def test_import_dry_run(mock_importer, mock_config, mock_preview, tmp_path):
    mock_importer.generate_preview.return_value = mock_preview
    capsule_path = tmp_path / "test.capsule"
    capsule_path.touch()

    result = runner.invoke(app, ["import", str(capsule_path), "--dry-run"])

    if result.exit_code != 0:
        print(f"Output: {result.output}")
        print(f"Exception: {result.exception}")

    assert result.exit_code == 0
    assert "[Dry Run]" in result.stdout
    # In the new implementation, execute_import IS called (to handle dry run logic internally)
    mock_importer.execute_import.assert_called_once()


def test_import_yes(mock_importer, mock_config, mock_preview, tmp_path):
    mock_importer.generate_preview.return_value = mock_preview
    capsule_path = tmp_path / "test.capsule"
    capsule_path.touch()

    with patch("capsule.commands.import_cmd.create_backup") as mock_backup:
        result = runner.invoke(app, ["import", str(capsule_path), "--yes"])

        assert result.exit_code == 0
        mock_importer.execute_import.assert_called_once()
        mock_backup.assert_called_once()


def test_import_interactive_yes(mock_importer, mock_config, mock_preview, tmp_path):
    mock_importer.generate_preview.return_value = mock_preview
    capsule_path = tmp_path / "test.capsule"
    capsule_path.touch()

    with patch("capsule.commands.import_cmd.questionary.confirm") as mock_confirm:
        mock_confirm.return_value.ask.return_value = True
        with patch("capsule.commands.import_cmd.create_backup"):
            result = runner.invoke(app, ["import", str(capsule_path)])

            assert result.exit_code == 0
            mock_importer.execute_import.assert_called_once()


def test_import_interactive_no(mock_importer, mock_config, mock_preview, tmp_path):
    mock_importer.generate_preview.return_value = mock_preview
    capsule_path = tmp_path / "test.capsule"
    capsule_path.touch()

    with patch("capsule.commands.import_cmd.questionary.confirm") as mock_confirm:
        mock_confirm.return_value.ask.return_value = False
        result = runner.invoke(app, ["import", str(capsule_path)])

        if result.exit_code != 0:
            print(f"Output: {result.output}")
            print(f"Exception: {result.exception}")

        assert result.exit_code == 0
        assert "Import cancelled" in result.stdout
        mock_importer.execute_import.assert_not_called()


def test_import_no_backup(mock_importer, mock_config, mock_preview, tmp_path):
    mock_importer.generate_preview.return_value = mock_preview
    capsule_path = tmp_path / "test.capsule"
    capsule_path.touch()

    with patch("capsule.commands.import_cmd.create_backup") as mock_backup:
        result = runner.invoke(app, ["import", str(capsule_path), "--yes", "--no-backup"])

        assert result.exit_code == 0
        mock_importer.execute_import.assert_called_once()
        mock_backup.assert_not_called()


def test_import_error(mock_importer, mock_config, tmp_path):
    mock_importer.validate_capsule.side_effect = CapsuleError("Invalid capsule")

    capsule_path = tmp_path / "test.capsule"
    capsule_path.touch()

    result = runner.invoke(app, ["import", str(capsule_path)])

    assert result.exit_code == 1
    assert "Error: Invalid capsule" in result.stdout
