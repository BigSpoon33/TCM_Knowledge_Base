import pytest
from unittest.mock import Mock
from capsule.core.validator import Validator
import tempfile
from pathlib import Path
import yaml


@pytest.fixture
def validator():
    with tempfile.TemporaryDirectory() as temp_dir:
        capsule_path = Path(temp_dir)
        (capsule_path / "capsule-cypher.yaml").touch()
        yield Validator(capsule_path)


def test_validate_capsule_calls_all_validation_methods(validator):
    validator.validate_capsule_structure = Mock()
    validator.validate_frontmatter_schema = Mock()
    validator.validate_file_inventory = Mock()
    validator.validate_data_types = Mock()

    validator.validate_capsule()

    validator.validate_capsule_structure.assert_called_once()
    validator.validate_frontmatter_schema.assert_called_once()
    validator.validate_file_inventory.assert_called_once()
    validator.validate_data_types.assert_called_once()


def test_validate_capsule_with_valid_capsule():
    with tempfile.TemporaryDirectory() as temp_dir:
        capsule_path = Path(temp_dir)

        # Create capsule-cypher.yaml
        cypher_data = {
            "capsule_id": "temp-capsule",
            "name": "Test Capsule",
            "version": "1.0.0",
            "domain_type": "education",
            "folder_structure": {"root_notes": "root_notes"},
            "contents": {"root_notes": [{"file": "root_notes/test.md", "id": "test-1"}]},
        }
        with open(capsule_path / "capsule-cypher.yaml", "w") as f:
            yaml.dump(cypher_data, f)

        # Create content file
        (capsule_path / "root_notes").mkdir()
        with open(capsule_path / "root_notes" / "test.md", "w") as f:
            f.write("test content")

        validator = Validator(capsule_path)
        assert validator.validate_capsule() is None


def test_validate_capsule_with_invalid_cypher():
    with tempfile.TemporaryDirectory() as temp_dir:
        capsule_path = Path(temp_dir)

        cypher_data = {
            "capsule_id": "temp-capsule",
            "name": "Test Capsule",
            "version": "1.0",
            "domain_type": "education",
            "folder_structure": {"root_notes": "root_notes"},
            "contents": {"root_notes": [{"file": "root_notes/test.md", "id": "test-1"}]},
        }
        with open(capsule_path / "capsule-cypher.yaml", "w") as f:
            yaml.dump(cypher_data, f)

        (capsule_path / "root_notes").mkdir()
        with open(capsule_path / "root_notes" / "test.md", "w") as f:
            f.write("test content")

        with pytest.raises(ValueError):
            validator = Validator(capsule_path)
            validator.validate_capsule()


def test_validate_capsule_with_extra_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        capsule_path = Path(temp_dir)

        cypher_data = {
            "capsule_id": "temp-capsule",
            "name": "Test Capsule",
            "version": "1.0.0",
            "domain_type": "education",
            "folder_structure": {"root_notes": "root_notes"},
            "contents": {"root_notes": []},
        }
        with open(capsule_path / "capsule-cypher.yaml", "w") as f:
            yaml.dump(cypher_data, f)

        (capsule_path / "root_notes").mkdir()
        with open(capsule_path / "root_notes" / "test.md", "w") as f:
            f.write("test content")

        validator = Validator(capsule_path)
        with pytest.raises(FileExistsError):
            validator.validate_capsule()


def test_validate_capsule_with_incorrect_frontmatter_type():
    with tempfile.TemporaryDirectory() as temp_dir:
        capsule_path = Path(temp_dir)

        cypher_data = {
            "capsule_id": "temp-capsule",
            "name": "Test Capsule",
            "version": "1.0.0",
            "domain_type": "education",
            "folder_structure": {"root_notes": "root_notes"},
            "contents": {"root_notes": [{"file": "root_notes/test.md", "id": "test-1"}]},
            "schema": {
                "root_notes": {"title": {"type": "str", "required": True}, "pages": {"type": "int", "required": True}}
            },
        }
        with open(capsule_path / "capsule-cypher.yaml", "w") as f:
            yaml.dump(cypher_data, f)

        (capsule_path / "root_notes").mkdir()
        with open(capsule_path / "root_notes" / "test.md", "w") as f:
            f.write('---\ntitle: Test\npages: "10"\n---')

        validator = Validator(capsule_path)
        with pytest.raises(TypeError):
            validator.validate_capsule()
