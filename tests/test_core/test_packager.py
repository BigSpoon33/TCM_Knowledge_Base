from capsule.models.capsule import Capsule
import pytest
from capsule.core.packager import CapsulePackager
import tempfile
import os
from pathlib import Path


@pytest.fixture
def temp_capsule():
    """Create a temporary capsule for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        capsule_path = Path(tmpdir) / "test_capsule"
        os.makedirs(capsule_path / "root_notes")
        with open(capsule_path / "root_notes" / "note1.md", "w") as f:
            f.write("---\nid: note1\n---\n# Note 1")
        with open(capsule_path / "root_notes" / "note2.md", "w") as f:
            f.write("---\nid: note2\n---\n# Note 2")
        yield capsule_path


def test_capsule_packager_init(temp_capsule):
    """Test that the CapsulePackager can be initialized."""
    capsule = Capsule(
        capsule_id="test-v1",
        name="Test Capsule",
        version="1.0.0",
        domain_type="education",
    )
    with tempfile.TemporaryDirectory() as tmpdir:
        packager = CapsulePackager(capsule, temp_capsule, tmpdir)
        assert packager.capsule.capsule_id == "test-v1"
        assert packager.capsule_path == Path(temp_capsule)
        assert packager.output_dir == Path(tmpdir)


def test_packager_init_raises_error_if_capsule_path_not_found():
    """Test that the packager raises an error if the capsule path does not exist."""
    capsule = Capsule(
        capsule_id="test-v1",
        name="Test Capsule",
        version="1.0.0",
        domain_type="education",
    )
    with pytest.raises(FileNotFoundError):
        with tempfile.TemporaryDirectory() as tmpdir:
            CapsulePackager(capsule, "non_existent_path", tmpdir)


def test_packager_init_raises_error_if_output_dir_not_writable():
    """Test that the packager raises an error if the output dir is not writable."""
    capsule = Capsule(
        capsule_id="test-v1",
        name="Test Capsule",
        version="1.0.0",
        domain_type="education",
    )
    with pytest.raises(IOError):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a non-writable directory
            non_writable_dir = Path(tmpdir) / "non_writable"
            os.makedirs(non_writable_dir, mode=0o444)
            CapsulePackager(capsule, tmpdir, non_writable_dir)


def test_generate_cypher(temp_capsule):
    """Test that a cypher can be generated."""
    capsule = Capsule(
        capsule_id="TCM_Test_v1",
        name="Test Capsule",
        version="1.0.0",
        domain_type="tcm",
    )
    with tempfile.TemporaryDirectory() as tmpdir:
        packager = CapsulePackager(capsule, temp_capsule, tmpdir)
        cypher = packager.generate_cypher()
        assert cypher.capsule_id == "TCM_Test_v1"
        assert len(cypher.contents["root_notes"]) == 2
        assert cypher.contents["root_notes"][0]["id"] == "note1"
        assert cypher.contents["root_notes"][1]["id"] == "note2"


def test_create_folder_bundle(temp_capsule):
    """Test that a folder bundle can be created."""
    with tempfile.TemporaryDirectory() as tmpdir:
        capsule = Capsule(
            capsule_id="TCM_Test_v1",
            name="Test Capsule",
            version="1.0.0",
            domain_type="tcm",
        )
        packager = CapsulePackager(capsule, temp_capsule, tmpdir)
        packager.package()
        bundle_path = Path(tmpdir) / "TCM_Test_v1"
        assert os.path.isdir(bundle_path)
        cypher_path = bundle_path / "capsule-cypher.yaml"
        assert os.path.isfile(cypher_path)
        with open(cypher_path, "r") as f:
            content = f.read()
            assert "capsule_id: TCM_Test_v1" in content
            assert "id: note1" in content


def test_generate_cypher_with_empty_root_notes(temp_capsule):
    """Test that a cypher can be generated with an empty root_notes directory."""
    capsule = Capsule(
        capsule_id="TCM_Test_v1",
        name="Test Capsule",
        version="1.0.0",
        domain_type="tcm",
    )
    # Remove the notes from the temp_capsule
    for item in (Path(temp_capsule) / "root_notes").iterdir():
        item.unlink()
    with tempfile.TemporaryDirectory() as tmpdir:
        packager = CapsulePackager(capsule, temp_capsule, tmpdir)
        cypher = packager.generate_cypher()
        assert cypher.capsule_id == "TCM_Test_v1"
        assert len(cypher.contents["root_notes"]) == 0


def test_generate_cypher_with_missing_id_in_frontmatter(temp_capsule):
    """Test that a cypher can be generated when a note is missing an id."""
    capsule = Capsule(
        capsule_id="TCM_Test_v1",
        name="Test Capsule",
        version="1.0.0",
        domain_type="tcm",
    )
    # Overwrite a note with missing id
    with open(Path(temp_capsule) / "root_notes" / "note1.md", "w") as f:
        f.write("---\n---\n# Note 1")
    with tempfile.TemporaryDirectory() as tmpdir:
        packager = CapsulePackager(capsule, temp_capsule, tmpdir)
        cypher = packager.generate_cypher()
        assert cypher.capsule_id == "TCM_Test_v1"
        assert len(cypher.contents["root_notes"]) == 2
        assert cypher.contents["root_notes"][0]["id"] == ""
        assert cypher.contents["root_notes"][1]["id"] == "note2"
