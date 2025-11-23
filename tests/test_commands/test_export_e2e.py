import zipfile

import pytest
import yaml
from typer.testing import CliRunner

from capsule.cli import app

runner = CliRunner()


@pytest.fixture
def valid_capsule(tmp_path):
    capsule_path = tmp_path / "valid_capsule"
    capsule_path.mkdir()

    # Create capsule-cypher.yaml
    cypher = {
        "capsule_id": "test_capsule",
        "name": "Test Capsule",
        "version": "1.0.0",
        "domain_type": "test",
        "folder_structure": {"root": ".", "subdir": "subdir"},
        "contents": {
            "root_notes": [{"file": "note.md", "id": "note-1"}],
            "subdir_files": [{"file": "subdir/file2.txt", "id": "file-2"}],
        },
    }
    with open(capsule_path / "capsule-cypher.yaml", "w") as f:
        yaml.dump(cypher, f)

    # Create a note
    with open(capsule_path / "note.md", "w") as f:
        f.write("---\nid: note-1\n---\n# Test Note")

    # Create a subdirectory and another file
    (capsule_path / "subdir").mkdir()
    (capsule_path / "subdir" / "file2.txt").write_text("world")

    return capsule_path


def test_e2e_export_zip(valid_capsule, tmp_path):
    output_dir = tmp_path / "output"
    result = runner.invoke(app, ["export", str(valid_capsule), "--output", str(output_dir)])

    assert result.exit_code == 0
    assert "Successfully exported" in result.stdout

    zip_path = output_dir / "test_capsule_v1.0.0.zip"
    assert zip_path.exists()

    with zipfile.ZipFile(zip_path, "r") as zf:
        names = zf.namelist()
        assert "capsule-cypher.yaml" in names
        assert "note.md" in names
        assert "subdir/file2.txt" in names
        assert "export-manifest.json" in names


def test_e2e_export_folder(valid_capsule, tmp_path):
    output_dir = tmp_path / "output"
    result = runner.invoke(app, ["export", str(valid_capsule), "--output", str(output_dir), "--no-zip"])

    assert result.exit_code == 0
    assert "Successfully exported" in result.stdout

    folder_path = output_dir / "test_capsule_v1.0.0"
    assert folder_path.exists()
    assert folder_path.is_dir()

    assert (folder_path / "capsule-cypher.yaml").exists()
    assert (folder_path / "note.md").exists()
    assert (folder_path / "subdir/file2.txt").exists()
    assert (folder_path / "export-manifest.json").exists()


def test_e2e_export_invalid_path(tmp_path):
    invalid_path = tmp_path / "non_existent"
    result = runner.invoke(app, ["export", str(invalid_path)])

    assert result.exit_code != 0
    assert "Error" in result.stdout
    assert "Capsule path does not exist" in result.stdout
