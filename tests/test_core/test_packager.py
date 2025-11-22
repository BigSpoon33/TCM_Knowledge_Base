import pytest
from capsule.core.packager import CapsulePackager
import tempfile
import os
import zipfile
from pathlib import Path


from capsule.models.capsule import Capsule


@pytest.fixture
def capsule():
    return Capsule(
        capsule_id="TCM_Test_v1",
        name="Test Capsule",
        version="1.0.0",
        domain_type="tcm",
    )


@pytest.fixture
def temp_capsule():
    """Create a temporary capsule for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        capsule_path = Path(tmpdir) / "test_capsule"
        os.makedirs(capsule_path / "root_notes")
        with open(capsule_path / "root_notes" / "note1.md", "w") as f:
            f.write("---\\nid: note1\\n---\\n# Note 1")
        with open(capsule_path / "root_notes" / "note2.md", "w") as f:
            f.write("---\\nid: note2\\n---\\n# Note 2")
        with open(capsule_path / "capsule-cypher.yaml", "w") as f:
            f.write("""
capsule_id: "TCM_Test_v1"
name: "Test Capsule"
version: "1.0.0"
domain_type: "tcm"
folder_structure:
    root_notes: root_notes
contents:
    root_notes:
        - file: root_notes/note1.md
          id: note1
        - file: root_notes/note2.md
          id: note2
""")
        yield capsule_path


def test_capsule_packager_init(capsule, temp_capsule):
    """Test that the CapsulePackager can be initialized."""
    with tempfile.TemporaryDirectory() as tmpdir:
        packager = CapsulePackager(capsule, temp_capsule, tmpdir)
        assert packager.capsule.capsule_id == "TCM_Test_v1"
        assert packager.capsule_path == Path(temp_capsule)
        assert packager.output_dir == Path(tmpdir)


def test_packager_init_raises_error_if_capsule_path_not_found(capsule):
    """Test that the packager raises an error if the capsule path does not exist."""
    with pytest.raises(FileNotFoundError):
        with tempfile.TemporaryDirectory() as tmpdir:
            CapsulePackager(capsule, "non_existent_path", tmpdir)


def test_generate_cypher(capsule, temp_capsule):
    """Test that a cypher can be generated."""
    with tempfile.TemporaryDirectory() as tmpdir:
        packager = CapsulePackager(capsule, temp_capsule, tmpdir)
        cypher = packager.generate_cypher()
        assert cypher.capsule_id == "TCM_Test_v1"
        assert cypher.name == "Test Capsule"
        assert cypher.version == "1.0.0"
        assert cypher.domain_type == "tcm"
        assert len(cypher.contents["root_notes"]) == 2


def test_create_folder_bundle(capsule, temp_capsule):
    """Test that a folder bundle can be created."""
    with tempfile.TemporaryDirectory() as tmpdir:
        packager = CapsulePackager(capsule, temp_capsule, tmpdir)
        packager.package()
        bundle_path = Path(tmpdir) / "TCM_Test_v1"
        assert os.path.isdir(bundle_path)
        cypher_path = bundle_path / "capsule-cypher.yaml"
        assert os.path.isfile(cypher_path)
        with open(cypher_path, "r") as f:
            content = f.read()
            assert "capsule_id: TCM_Test_v1" in content

        # Check that the content files were copied
        assert (bundle_path / "root_notes" / "note1.md").exists()
        assert (bundle_path / "root_notes" / "note2.md").exists()


def test_create_folder_bundle_permission_error(capsule, temp_capsule):
    """Test that a permission error is raised for an unwritable output directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Make the output directory read-only
        os.chmod(tmpdir, 0o444)

        packager = CapsulePackager(capsule, temp_capsule, tmpdir)
        with pytest.raises(PermissionError):
            packager.package()


def test_generate_cypher_with_empty_root_notes(capsule, temp_capsule):
    """Test that a cypher can be generated with an empty root_notes directory."""
    # Remove the notes from the temp_capsule
    for item in (Path(temp_capsule) / "root_notes").iterdir():
        item.unlink()
    with tempfile.TemporaryDirectory() as tmpdir:
        packager = CapsulePackager(capsule, temp_capsule, tmpdir)
        cypher = packager.generate_cypher()
        assert cypher.capsule_id == "TCM_Test_v1"
        assert len(cypher.contents["root_notes"]) == 0


def test_generate_cypher_with_missing_id_in_frontmatter(capsule, temp_capsule):
    """Test that a cypher can be generated when a note is missing an id."""
    # Overwrite a note with missing id
    with open(Path(temp_capsule) / "root_notes" / "note1.md", "w") as f:
        f.write("---\\n---\\n# Note 1")
    with tempfile.TemporaryDirectory() as tmpdir:
        packager = CapsulePackager(capsule, temp_capsule, tmpdir)
        cypher = packager.generate_cypher()
        assert cypher.capsule_id == "TCM_Test_v1"
        assert len(cypher.contents["root_notes"]) == 2


def test_export_to_folder(capsule, temp_capsule):
    """Test that a capsule can be exported to a folder."""
    with tempfile.TemporaryDirectory() as tmpdir:
        destination_path = Path(tmpdir) / "destination"
        destination_path.mkdir()
        packager = CapsulePackager(capsule, temp_capsule, destination_path)
        packager.export_to_folder()
        assert (destination_path / "root_notes" / "note1.md").exists()
        assert (destination_path / "root_notes" / "note2.md").exists()
        assert (destination_path / "capsule-cypher.yaml").exists()


def test_export_to_zip(capsule, temp_capsule):
    """Test that a capsule can be exported to a zip archive."""
    with tempfile.TemporaryDirectory() as tmpdir:
        destination_path = Path(tmpdir) / "destination"
        packager = CapsulePackager(capsule, temp_capsule, destination_path)
        packager.export_to_zip()
        zip_path = Path(tmpdir) / "destination.zip"
        assert zip_path.exists()

        with zipfile.ZipFile(zip_path, "r") as zf:
            zip_contents = zf.namelist()
            assert "root_notes/note1.md" in zip_contents
            assert "root_notes/note2.md" in zip_contents
            assert "capsule-cypher.yaml" in zip_contents

        with zipfile.ZipFile(zip_path, "r") as zf:
            zip_contents = zf.namelist()
            assert "root_notes/note1.md" in zip_contents
            assert "root_notes/note2.md" in zip_contents
            assert "capsule-cypher.yaml" in zip_contents
