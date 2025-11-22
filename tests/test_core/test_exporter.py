import pytest
import zipfile
from pathlib import Path
from capsule.core.exporter import Exporter
import yaml
import json


@pytest.fixture
def sample_capsule(tmp_path):
    """Create a sample capsule for testing."""
    capsule_path = tmp_path / "test_capsule"
    capsule_path.mkdir()

    # Create capsule-cypher.yaml
    cypher_content = {
        "capsule_id": "test_capsule_v1",
        "name": "Test Capsule",
        "version": "1.0.0",
        "domain_type": "test",
        "folder_structure": {"root_notes": "root_notes/"},
        "contents": {"root_notes": [{"file": "root_notes/test_note.md", "id": "note-1"}]},
    }

    with open(capsule_path / "capsule-cypher.yaml", "w") as f:
        yaml.dump(cypher_content, f)

    # Create a root note
    root_notes_dir = capsule_path / "root_notes"
    root_notes_dir.mkdir()

    note_content = """---
id: note-1
name: Test Note
type: root_note
tags: [test]
created: 2025-11-20
updated: 2025-11-20
---

# Test Note Content
"""
    with open(root_notes_dir / "test_note.md", "w") as f:
        f.write(note_content)

    return capsule_path


def test_exporter_initialization(sample_capsule):
    """Test that the Exporter initializes correctly."""
    exporter = Exporter(sample_capsule)
    assert exporter.capsule_path == sample_capsule
    assert exporter.cypher["capsule_id"] == "test_capsule_v1"


def test_validate_capsule_success(sample_capsule):
    """Test that validation succeeds for a valid capsule."""
    exporter = Exporter(sample_capsule)
    assert exporter.validate_capsule() is True


def test_generate_manifest(sample_capsule):
    """Test that manifest generation works correctly."""
    exporter = Exporter(sample_capsule)
    manifest = exporter.generate_manifest()

    assert manifest["capsule_id"] == "test_capsule_v1"
    assert manifest["version"] == "1.0.0"
    assert "export_date" in manifest
    assert len(manifest["files"]) >= 2  # cypher + at least one note


def test_export_to_zip(sample_capsule, tmp_path):
    """Test exporting a capsule to a zip archive."""
    exporter = Exporter(sample_capsule)
    output_path = tmp_path / "test_export.capsule"

    exporter.export_to_zip(output_path)

    assert output_path.exists()
    assert output_path.is_file()

    # Verify the zip contains expected files
    with zipfile.ZipFile(output_path, "r") as zf:
        namelist = zf.namelist()
        assert "export-manifest.json" in namelist
        assert "capsule-cypher.yaml" in namelist
        assert "root_notes/test_note.md" in namelist


def test_export_to_folder(sample_capsule, tmp_path):
    """Test exporting a capsule to a folder."""
    exporter = Exporter(sample_capsule)
    output_path = tmp_path / "test_export_folder"

    exporter.export_to_folder(output_path)

    assert output_path.exists()
    assert output_path.is_dir()
    assert (output_path / "export-manifest.json").exists()
    assert (output_path / "capsule-cypher.yaml").exists()
    assert (output_path / "root_notes" / "test_note.md").exists()


def test_export_to_folder_overwrites_existing(sample_capsule, tmp_path):
    """Test that exporting to an existing folder overwrites it."""
    output_path = tmp_path / "test_export_folder"
    output_path.mkdir()
    (output_path / "old_file.txt").write_text("old content")

    exporter = Exporter(sample_capsule)
    exporter.export_to_folder(output_path)

    assert not (output_path / "old_file.txt").exists()
    assert (output_path / "capsule-cypher.yaml").exists()


def test_manifest_included_in_zip(sample_capsule, tmp_path):
    """Test that the manifest is included in the zip export."""
    exporter = Exporter(sample_capsule)
    output_path = tmp_path / "test_export.capsule"

    exporter.export_to_zip(output_path)

    with zipfile.ZipFile(output_path, "r") as zf:
        manifest_data = zf.read("export-manifest.json")
        manifest = json.loads(manifest_data)

        assert manifest["capsule_id"] == "test_capsule_v1"
        assert manifest["version"] == "1.0.0"


def test_validation_failure_prevents_export(sample_capsule, tmp_path):
    """Test that export does not proceed if validation fails."""
    # Corrupt the cypher file to cause validation failure
    cypher_path = sample_capsule / "capsule-cypher.yaml"
    with open(cypher_path, "w") as f:
        yaml.dump({"invalid": "structure"}, f)

    exporter = Exporter(sample_capsule)
    output_path = tmp_path / "should_not_exist.capsule"

    # The export should not create the file due to validation failure
    exporter.export_to_zip(output_path)
    assert not output_path.exists()
