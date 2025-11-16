"""Tests for CapsuleCypher model."""

import pytest
from capsule.models.cypher import CapsuleCypher


def test_cypher_creation() -> None:
    """Test basic cypher instantiation."""
    cypher = CapsuleCypher(
        capsule_id="test-cypher-v1",
        name="Test Cypher",
        version="1.0.0",
        domain_type="education",
        folder_structure={
            "root_notes": "root_notes/",
            "study_material": "study_material/",
        },
        contents={
            "root_notes": [],
            "study_material": {"flashcards": [], "quizzes": []},
        },
        data_schemas={"example_data": {"field1": "string", "field2": "number"}},
        sequence_mode="freeform",
    )

    assert cypher.capsule_id == "test-cypher-v1"
    assert cypher.name == "Test Cypher"
    assert cypher.version == "1.0.0"
    assert cypher.domain_type == "education"
    assert cypher.sequence_mode == "freeform"
    assert "root_notes" in cypher.folder_structure


def test_cypher_required_fields() -> None:
    """Test that all required fields must be provided."""
    cypher = CapsuleCypher(
        capsule_id="required-test",
        name="Required Test",
        version="1.0.0",
        domain_type="test",
        folder_structure={},
        contents={},
        data_schemas={},
        sequence_mode="freeform",
    )
    assert cypher.capsule_id == "required-test"

    # Missing required field should raise TypeError
    with pytest.raises(TypeError):
        CapsuleCypher(  # type: ignore
            name="Missing ID",
            version="1.0.0",
            domain_type="test",
            folder_structure={},
            contents={},
            data_schemas={},
            sequence_mode="freeform",
        )


def test_cypher_optional_fields() -> None:
    """Test optional plugin fields."""
    cypher = CapsuleCypher(
        capsule_id="plugins-test",
        name="Plugins Test",
        version="1.0.0",
        domain_type="test",
        folder_structure={},
        contents={},
        data_schemas={},
        sequence_mode="freeform",
        required_plugins=[{"name": "dataview", "min_version": "0.5.0"}],
        recommended_plugins=[{"name": "templater", "min_version": "1.0.0"}],
    )

    assert cypher.required_plugins is not None
    assert len(cypher.required_plugins) == 1
    assert cypher.required_plugins[0]["name"] == "dataview"
    assert cypher.recommended_plugins is not None


def test_cypher_to_dict() -> None:
    """Test serialization to dictionary."""
    cypher = CapsuleCypher(
        capsule_id="dict-test",
        name="Dict Test",
        version="1.0.0",
        domain_type="test",
        folder_structure={"root": "root/"},
        contents={"root": []},
        data_schemas={},
        sequence_mode="sequenced",
    )

    cypher_dict = cypher.to_dict()

    assert isinstance(cypher_dict, dict)
    assert cypher_dict["capsule_id"] == "dict-test"
    assert cypher_dict["sequence_mode"] == "sequenced"
    assert "root" in cypher_dict["folder_structure"]


def test_cypher_from_dict() -> None:
    """Test deserialization from dictionary."""
    data = {
        "capsule_id": "from-dict-test",
        "name": "From Dict Test",
        "version": "2.0.0",
        "domain_type": "reference",
        "folder_structure": {"notes": "notes/"},
        "contents": {},
        "data_schemas": {"schema1": {"field": "string"}},
        "sequence_mode": "hybrid",
    }

    cypher = CapsuleCypher.from_dict(data)

    assert cypher.capsule_id == "from-dict-test"
    assert cypher.sequence_mode == "hybrid"
    assert "notes" in cypher.folder_structure


def test_cypher_to_yaml() -> None:
    """Test YAML serialization."""
    cypher = CapsuleCypher(
        capsule_id="yaml-test",
        name="YAML Test",
        version="1.0.0",
        domain_type="education",
        folder_structure={"root_notes": "root_notes/"},
        contents={},
        data_schemas={},
        sequence_mode="freeform",
    )

    yaml_str = cypher.to_yaml()

    assert isinstance(yaml_str, str)
    assert "capsule_id:" in yaml_str
    assert "yaml-test" in yaml_str
    assert "sequence_mode:" in yaml_str
    assert "freeform" in yaml_str


def test_cypher_from_yaml() -> None:
    """Test YAML deserialization."""
    yaml_content = """
capsule_id: from-yaml-v1
name: From YAML Test
version: 1.0.0
domain_type: reference
folder_structure:
  root_notes: root_notes/
  study_material: study_material/
contents:
  root_notes: []
data_schemas:
  test_data:
    field1: string
sequence_mode: freeform
"""

    cypher = CapsuleCypher.from_yaml(yaml_content)

    assert cypher.capsule_id == "from-yaml-v1"
    assert cypher.name == "From YAML Test"
    assert cypher.version == "1.0.0"
    assert "root_notes" in cypher.folder_structure
    assert "test_data" in cypher.data_schemas


def test_cypher_roundtrip_yaml() -> None:
    """Test that to_yaml() and from_yaml() are inverses."""
    original = CapsuleCypher(
        capsule_id="roundtrip-v1",
        name="Roundtrip Test",
        version="3.0.0",
        domain_type="tcm",
        folder_structure={"root_notes": "root_notes/"},
        contents={"root_notes": [{"file": "test.md", "id": "note-1"}]},
        data_schemas={"herb_data": {"temperature": "string"}},
        sequence_mode="sequenced",
        required_plugins=[{"name": "dataview", "min_version": "0.5.0"}],
    )

    # Serialize to YAML and back
    yaml_str = original.to_yaml()
    restored = CapsuleCypher.from_yaml(yaml_str)

    # Should be equal
    assert restored.capsule_id == original.capsule_id
    assert restored.name == original.name
    assert restored.version == original.version
    assert restored.domain_type == original.domain_type
    assert restored.sequence_mode == original.sequence_mode
    assert restored.folder_structure == original.folder_structure
    assert restored.contents == original.contents
    assert restored.data_schemas == original.data_schemas
    assert restored.required_plugins == original.required_plugins


def test_cypher_folder_structure() -> None:
    """Test folder structure dict handling."""
    cypher = CapsuleCypher(
        capsule_id="folders-test",
        name="Folders Test",
        version="1.0.0",
        domain_type="test",
        folder_structure={
            "root_notes": "root_notes/",
            "study_material": "study_material/",
            "resources": "resources/",
        },
        contents={},
        data_schemas={},
        sequence_mode="freeform",
    )

    assert len(cypher.folder_structure) == 3
    assert cypher.folder_structure["root_notes"] == "root_notes/"
    assert cypher.folder_structure["study_material"] == "study_material/"


def test_cypher_contents_inventory() -> None:
    """Test file inventory structure in contents."""
    cypher = CapsuleCypher(
        capsule_id="inventory-test",
        name="Inventory Test",
        version="1.0.0",
        domain_type="test",
        folder_structure={"root_notes": "root_notes/"},
        contents={
            "root_notes": [
                {"file": "root_notes/note1.md", "id": "note-001"},
                {"file": "root_notes/note2.md", "id": "note-002"},
            ],
            "study_material": {
                "flashcards": [
                    {"file": "study_material/flashcards/deck1.md", "id": "fc-001"}
                ]
            },
        },
        data_schemas={},
        sequence_mode="freeform",
    )

    assert "root_notes" in cypher.contents
    assert len(cypher.contents["root_notes"]) == 2
    assert cypher.contents["root_notes"][0]["id"] == "note-001"
