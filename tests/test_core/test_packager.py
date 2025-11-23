import pytest
from pathlib import Path
from capsule.core.packager import Packager
from capsule.models.cypher import CapsuleCypher


def test_generate_cypher(tmp_path):
    # Setup dummy capsule structure
    capsule_dir = tmp_path / "test_capsule"
    capsule_dir.mkdir()

    # Create directories
    (capsule_dir / "root_notes").mkdir()
    (capsule_dir / "images").mkdir()
    (capsule_dir / "nested").mkdir()
    (capsule_dir / "nested" / "deep").mkdir()

    # Create files
    (capsule_dir / "root_notes" / "note1.md").touch()
    (capsule_dir / "images" / "img1.png").touch()
    (capsule_dir / "nested" / "deep" / "deep_note.md").touch()
    (capsule_dir / "root_file.txt").touch()

    # Initialize Packager
    # We pass an empty dict for cypher as we are testing generation
    packager = Packager(capsule_path=capsule_dir, cypher={})

    # Generate cypher
    cypher = packager.generate_cypher(capsule_id="test-id", name="Test Capsule", version="0.0.1", domain_type="test")

    # Verify basic metadata
    assert isinstance(cypher, CapsuleCypher)
    assert cypher.capsule_id == "test-id"
    assert cypher.name == "Test Capsule"
    assert cypher.version == "0.0.1"
    assert cypher.domain_type == "test"

    # Verify folder structure
    # Should contain top-level folders
    assert "root_notes" in cypher.folder_structure
    assert cypher.folder_structure["root_notes"] == "root_notes/"
    assert "images" in cypher.folder_structure
    assert cypher.folder_structure["images"] == "images/"
    assert "nested" in cypher.folder_structure

    # Verify contents
    # Should contain files organized by folder
    assert "root_notes" in cypher.contents

    root_notes_files = cypher.contents["root_notes"]
    assert any("note1.md" in str(f) for f in root_notes_files)

    images_files = cypher.contents["images"]
    assert any("img1.png" in str(f) for f in images_files)

    # Check nested files
    assert "nested" in cypher.contents
    nested_files = cypher.contents["nested"]
    assert any("deep_note.md" in str(f) for f in nested_files)

    # Check root files
    assert "root" in cypher.contents
    root_files = cypher.contents["root"]
    assert any("root_file.txt" in str(f) for f in root_files)


def test_generate_cypher_defaults(tmp_path):
    capsule_dir = tmp_path / "test_capsule_defaults"
    capsule_dir.mkdir()

    packager = Packager(capsule_path=capsule_dir, cypher={})

    cypher = packager.generate_cypher(
        capsule_id="default-id", name="Default Name", version="1.0.0", domain_type="generic"
    )

    assert cypher.capsule_id == "default-id"
    assert cypher.data_schemas == {}
    assert cypher.sequence_mode == "freeform"  # Default


def test_generate_manifest(tmp_path):
    capsule_dir = tmp_path / "test_capsule_manifest"
    capsule_dir.mkdir()
    (capsule_dir / "file.md").touch()

    packager = Packager(capsule_path=capsule_dir, cypher={"capsule_id": "test-id", "version": "1.0.0"})
    manifest = packager.generate_manifest()

    assert manifest["capsule_id"] == "test-id"
    assert manifest["version"] == "1.0.0"
    assert "export_date" in manifest
    assert "file.md" in manifest["files"]


def test_package_to_zip(tmp_path):
    capsule_dir = tmp_path / "test_capsule_zip"
    capsule_dir.mkdir()
    output_zip = tmp_path / "output.zip"

    packager = Packager(capsule_path=capsule_dir, cypher={})

    # Mock FileOps to avoid actual zip creation if desired, but tmp_path allows real testing
    # However, Packager uses FileOps internally. Let's mock FileOps to verify calls.
    from unittest.mock import MagicMock, patch

    with patch("capsule.core.packager.FileOps") as MockFileOps:
        mock_file_ops = MockFileOps.return_value
        packager.file_ops = mock_file_ops

        packager.package_to_zip(output_zip)

        mock_file_ops.create_zip.assert_called_once()
        args, _ = mock_file_ops.create_zip.call_args
        assert args[0] == output_zip
        assert args[1] == capsule_dir


def test_package_to_folder(tmp_path):
    capsule_dir = tmp_path / "test_capsule_folder"
    capsule_dir.mkdir()
    output_folder = tmp_path / "output_folder"

    packager = Packager(capsule_path=capsule_dir, cypher={})

    from unittest.mock import MagicMock, patch

    with patch("capsule.core.packager.FileOps") as MockFileOps:
        mock_file_ops = MockFileOps.return_value
        packager.file_ops = mock_file_ops

        packager.package_to_folder(output_folder)

        mock_file_ops.copytree.assert_called_once_with(capsule_dir, output_folder)
        mock_file_ops.write_text.assert_called_once()
