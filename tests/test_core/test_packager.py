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


def test_capsule_packager_init():
    """Test that the CapsulePackager can be initialized."""
    packager = CapsulePackager("path/to/capsule", "output")
    assert packager.capsule_path == Path("path/to/capsule")
    assert packager.output_dir == Path("output")


def test_generate_cypher(temp_capsule):
    """Test that a cypher can be generated."""
    packager = CapsulePackager(temp_capsule, "output")
    cypher = packager.generate_cypher()
    assert cypher.capsule_id == "TCM_Test_v1"
    assert len(cypher.contents["root_notes"]) == 2
    assert cypher.contents["root_notes"][0]["id"] == "note1"
    assert cypher.contents["root_notes"][1]["id"] == "note2"


def test_create_folder_bundle(temp_capsule):
    """Test that a folder bundle can be created."""
    with tempfile.TemporaryDirectory() as tmpdir:
        packager = CapsulePackager(temp_capsule, tmpdir)
        packager.create_folder_bundle()
        bundle_path = Path(tmpdir) / "TCM_Test_v1"
        assert os.path.isdir(bundle_path)
        cypher_path = bundle_path / "capsule-cypher.yaml"
        assert os.path.isfile(cypher_path)
        with open(cypher_path, "r") as f:
            content = f.read()
            assert "capsule_id: TCM_Test_v1" in content
            assert "id: note1" in content
