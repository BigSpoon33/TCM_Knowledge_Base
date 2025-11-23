# tests/test_commands/test_dry_run_integration.py
import shutil
from pathlib import Path

import pytest
from typer.testing import CliRunner

from capsule.cli import app
from capsule.utils.file_ops import FileOps

runner = CliRunner()


@pytest.fixture
def sample_capsule(tmp_path):
    """Create a sample capsule for testing."""
    capsule_path = tmp_path / "TestCapsule"
    capsule_path.mkdir()
    (capsule_path / "capsule-cypher.yaml").write_text(
        """
capsule_id: "TestCapsule"
name: "Test Capsule"
version: "1.0.0"
domain_type: "general"
folder_structure:
  root: "."
contents:
  root:
    - file: "note.md"
data_schemas: {}
""",
        encoding="utf-8",
    )
    (capsule_path / "note.md").write_text("# Test Note", encoding="utf-8")
    return capsule_path


def test_generate_dry_run(tmp_path):
    """Test generate command with --dry-run."""
    output_dir = tmp_path / "output"
    result = runner.invoke(
        app,
        [
            "generate",
            "Test Topic",
            "--output",
            str(output_dir),
            "--no-research",
            "--dry-run",
        ],
    )
    assert result.exit_code == 0
    assert "[DRY RUN]" in result.stdout
    assert "Would generate capsule about: Test Topic" in result.stdout
    # Verify no files were created
    assert not output_dir.exists()


def test_export_dry_run_zip(sample_capsule, tmp_path):
    """Test export command with --dry-run (zip)."""
    output_dir = tmp_path / "export_output"
    result = runner.invoke(
        app,
        [
            "export",
            str(sample_capsule),
            "--output",
            str(output_dir),
            "--zip",
            "--dry-run",
        ],
    )
    if result.exit_code != 0:
        print(result.stdout)
        print(result.exception)
    assert result.exit_code == 0
    assert "[DRY RUN]" in result.stdout
    assert "Would export capsule from" in result.stdout
    # Verify no files were created
    assert not output_dir.exists()


def test_export_dry_run_folder(sample_capsule, tmp_path):
    """Test export command with --dry-run (folder)."""
    output_dir = tmp_path / "export_output"
    result = runner.invoke(
        app,
        [
            "export",
            str(sample_capsule),
            "--output",
            str(output_dir),
            "--no-zip",
            "--dry-run",
        ],
    )
    assert result.exit_code == 0
    assert "[DRY RUN]" in result.stdout
    assert "Would export capsule from" in result.stdout
    # Verify no files were created
    assert not output_dir.exists()


def test_import_dry_run(sample_capsule, tmp_path):
    """Test import command with --dry-run."""
    # Create a dummy vault
    vault_path = tmp_path / "Vault"
    vault_path.mkdir()

    # Create a config file pointing to this vault
    config_path = tmp_path / "config.yaml"
    config_path.write_text(
        f"""
user:
  vault_path: "{vault_path}"
import:
  backup_location: "{tmp_path}/backups"
""",
        encoding="utf-8",
    )

    # We need to zip the capsule first because import expects a zip or folder
    # Let's use the folder directly

    result = runner.invoke(
        app,
        [
            "--config-path",
            str(config_path),
            "import",
            str(sample_capsule),
            "--dry-run",
        ],
    )

    if result.exit_code != 0:
        print(result.stdout)
        print(result.exception)
    assert result.exit_code == 0

    assert "[DRY RUN]" in result.stdout
    # Verify no files were imported into vault
    assert not (vault_path / "TestCapsule").exists()
    # Verify no backup was created
    assert not (tmp_path / "backups").exists()
