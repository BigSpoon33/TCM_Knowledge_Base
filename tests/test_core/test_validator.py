import pytest
from pathlib import Path
import yaml
import frontmatter
from capsule.core.validator import Validator


@pytest.fixture
def sample_capsule(tmp_path):
    capsule_dir = tmp_path / "sample_capsule"
    capsule_dir.mkdir()

    # Create capsule-cypher.yaml
    cypher_data = {
        "capsule_id": "test-capsule",
        "name": "Test Capsule",
        "version": "1.0.0",
        "domain_type": "test",
        "folder_structure": {"notes": "notes"},
        "contents": {"notes": [{"file": "notes/note1.md", "id": "note1"}]},
        "schema": {"notes": {"title": {"required": True, "type": "str"}, "tags": {"required": False, "type": "list"}}},
    }
    with open(capsule_dir / "capsule-cypher.yaml", "w") as f:
        yaml.dump(cypher_data, f)

    # Create note1.md
    notes_dir = capsule_dir / "notes"
    notes_dir.mkdir()
    note1_content = """---
title: "Note 1"
tags: ["a", "b"]
---
This is note 1.
"""
    with open(notes_dir / "note1.md", "w") as f:
        f.write(note1_content)

    return capsule_dir


def test_validator_success(sample_capsule):
    """
    Tests that a valid capsule passes validation.
    The test passes if no exception is raised.
    """
    validator = Validator(sample_capsule)
    validator.validate_capsule()


def test_validator_missing_field(sample_capsule):
    # Remove title from note1.md
    note1_path = sample_capsule / "notes" / "note1.md"
    post = frontmatter.load(note1_path)
    del post.metadata["title"]
    with open(note1_path, "w") as f:
        f.write(frontmatter.dumps(post))

    validator = Validator(sample_capsule)
    with pytest.raises(ValueError, match="Missing required field 'title'"):
        validator.validate_capsule()


def test_validator_invalid_data_type(sample_capsule):
    # Change title to an int in note1.md
    note1_path = sample_capsule / "notes" / "note1.md"
    post = frontmatter.load(note1_path)
    post.metadata["title"] = 123
    with open(note1_path, "w") as f:
        f.write(frontmatter.dumps(post))

    validator = Validator(sample_capsule)
    with pytest.raises(TypeError, match="Invalid data type for field 'title'"):
        validator.validate_capsule()


def test_validator_invalid_cypher_file(sample_capsule):
    # Corrupt the capsule-cypher.yaml file
    cypher_path = sample_capsule / "capsule-cypher.yaml"
    with open(cypher_path, "r") as f:
        cypher_data = yaml.safe_load(f)

    del cypher_data["capsule_id"]

    with open(cypher_path, "w") as f:
        yaml.dump(cypher_data, f)

    validator = Validator(sample_capsule)
    with pytest.raises(ValueError, match="Missing required fields in capsule-cypher.yaml: capsule_id"):
        validator.validate_capsule_structure()


def test_validator_missing_file_in_cypher(sample_capsule):
    # Remove a file that is listed in the cypher
    (sample_capsule / "notes" / "note1.md").unlink()

    validator = Validator(sample_capsule)
    with pytest.raises(FileNotFoundError, match="File from cypher not found in capsule"):
        validator.validate_file_inventory()


def test_validator_extra_file_in_directory(sample_capsule):
    # Add an extra file to the capsule directory
    with open(sample_capsule / "notes" / "extra_note.md", "w") as f:
        f.write("This is an extra note.")

    validator = Validator(sample_capsule)
    with pytest.raises(FileExistsError, match="Extra files found in capsule"):
        validator.validate_file_inventory()
