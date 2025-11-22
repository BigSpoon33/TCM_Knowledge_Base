from typer.testing import CliRunner
from capsule.cli import app
import pytest
from pathlib import Path
import shutil

runner = CliRunner()


@pytest.fixture
def temp_capsule(tmp_path):
    capsule_dir = tmp_path / "test_capsule"
    capsule_dir.mkdir()
    (capsule_dir / "file1.txt").write_text("hello")
    (capsule_dir / "subdir").mkdir()
    (capsule_dir / "subdir" / "file2.txt").write_text("world")
    (capsule_dir / "capsule-cypher.yaml").write_text(
        """
capsule_id: test_capsule
name: Test Capsule
version: 1.0.0
domain_type: generic
contents:
    root:
        - file: file1.txt
          id: 1
    subdir:
        - file: subdir/file2.txt
          id: 2
folder_structure:
    subdir: subdir
"""
    )
    return capsule_dir


def test_export_folder(temp_capsule, tmp_path):
    destination_dir = tmp_path / "destination"
    result = runner.invoke(app, ["export", "export", str(temp_capsule), str(destination_dir), "--format", "folder"])
    print(result.stdout)
    assert result.exit_code == 0
    assert "Successfully exported capsule to" in result.stdout
    assert (destination_dir / "file1.txt").exists()
    assert (destination_dir / "subdir" / "file2.txt").exists()
    assert (destination_dir / "export-manifest.json").exists()


def test_export_zip(temp_capsule, tmp_path):
    destination_dir = tmp_path / "destination"
    destination_dir.mkdir()
    destination_zip = destination_dir / "test_capsule"
    result = runner.invoke(app, ["export", "export", str(temp_capsule), str(destination_zip), "--format", "zip"])
    print(result.stdout)
    assert result.exit_code == 0
    assert "Successfully exported capsule to" in result.stdout
    assert (destination_dir / "test_capsule.capsule").exists()


def test_export_invalid_format(temp_capsule, tmp_path):
    """Test the export command with an invalid format."""
    output_path = tmp_path / "output"

    result = runner.invoke(app, ["export", "export", str(temp_capsule), str(output_path), "--format", "invalid"])

    assert result.exit_code == 1
    assert "Invalid format" in result.stdout


def test_export_adds_capsule_extension(temp_capsule, tmp_path):
    """Test that the export command adds .capsule extension for zip format."""
    output_path = tmp_path / "output"

    result = runner.invoke(app, ["export", "export", str(temp_capsule), str(output_path), "--format", "zip"])

    assert result.exit_code == 0
    expected_path = tmp_path / "output.capsule"
    assert expected_path.exists()


def test_export_default_format(temp_capsule, tmp_path):
    """Test that the export command defaults to zip format."""
    output_path = tmp_path / "output.capsule"

    result = runner.invoke(app, ["export", "export", str(temp_capsule), str(output_path)])

    assert result.exit_code == 0
    assert output_path.exists()

    # Verify it's a zip file
    import zipfile

    with zipfile.ZipFile(output_path, "r") as zf:
        assert "export-manifest.json" in zf.namelist()
