from unittest.mock import patch

import pytest
import yaml

from capsule.core.exporter import Exporter
from capsule.exceptions import ValidationError


@pytest.fixture
def sample_capsule(tmp_path):
    """Create a sample capsule for testing."""
    capsule_path = tmp_path / "test_capsule"
    capsule_path.mkdir()

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

    root_notes_dir = capsule_path / "root_notes"
    root_notes_dir.mkdir()

    note_content = """---
id: note-1
---
# Test Note Content
"""
    (root_notes_dir / "test_note.md").write_text(note_content)

    return capsule_path


def test_exporter_initialization(sample_capsule):
    """Test that the Exporter initializes correctly."""
    exporter = Exporter(sample_capsule)
    assert exporter.capsule_path == sample_capsule
    assert exporter.cypher["capsule_id"] == "test_capsule_v1"
    assert exporter.packager is not None


def test_validate_capsule_success(sample_capsule):
    """Test that validation succeeds for a valid capsule."""
    exporter = Exporter(sample_capsule)
    # validate_capsule should not raise an exception for a valid capsule
    try:
        exporter.validate_capsule()
    except ValidationError:
        pytest.fail("validate_capsule() raised ValidationError unexpectedly!")


def test_export_to_zip_calls_packager(sample_capsule, tmp_path):
    """Test exporting a capsule to a zip archive calls the packager."""
    exporter = Exporter(sample_capsule)
    output_path = tmp_path / "test_export.zip"

    with patch.object(exporter.packager, "package_to_zip") as mock_package:
        exporter.export_to_zip(output_path)
        mock_package.assert_called_once_with(output_path)


def test_export_to_folder_calls_packager(sample_capsule, tmp_path):
    """Test exporting a capsule to a folder calls the packager."""
    exporter = Exporter(sample_capsule)
    output_path = tmp_path / "test_export_folder"

    with patch.object(exporter.packager, "package_to_folder") as mock_package:
        exporter.export_to_folder(output_path)
        mock_package.assert_called_once_with(output_path)


def test_validation_failure_prevents_export(sample_capsule, tmp_path):
    """Test that export does not proceed if validation fails."""
    cypher_path = sample_capsule / "capsule-cypher.yaml"
    with open(cypher_path, "w") as f:
        yaml.dump({"invalid": "structure"}, f)

    exporter = Exporter(sample_capsule)
    output_path = tmp_path / "should_not_exist.zip"

    with pytest.raises(ValidationError):
        exporter.export_to_zip(output_path)

    assert not output_path.exists()
