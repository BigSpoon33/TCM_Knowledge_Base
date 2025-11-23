"""
Unit tests for Note data model.

Tests cover creation, file I/O, frontmatter parsing, provenance tracking,
and UTF-8 encoding support.
"""

import shutil
import tempfile
from pathlib import Path

import pytest

from capsule.models.note import Note


@pytest.fixture
def temp_dir():
    """Create temporary directory for test files."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)


def test_note_creation():
    """Test creating Note with all fields."""
    note = Note(
        file_path="root_notes/Ginger.md",
        frontmatter={"id": "note-ginger-001", "name": "Ginger", "type": "herb"},
        body="# Ginger\n\nGinger is a medicinal herb.",
        source_capsules=["TCM_v1"],
    )

    assert note.file_path == "root_notes/Ginger.md"
    assert note.frontmatter["id"] == "note-ginger-001"
    assert note.frontmatter["name"] == "Ginger"
    assert note.body.startswith("# Ginger")
    assert note.source_capsules == ["TCM_v1"]


def test_note_minimal():
    """Test creating Note with minimal fields (no source_capsules)."""
    note = Note(file_path="test.md", frontmatter={"id": "note-001"}, body="Content")

    assert note.file_path == "test.md"
    assert note.frontmatter["id"] == "note-001"
    assert note.body == "Content"
    assert note.source_capsules is None


def test_from_file_with_frontmatter(temp_dir):
    """Test parsing Note from file with YAML frontmatter."""
    # Create test file with frontmatter
    test_file = temp_dir / "test_note.md"
    content = """---
id: note-test-001
name: Test Note
type: example
---
# Content here

This is test content."""

    test_file.write_text(content, encoding="utf-8")

    # Parse file
    note = Note.from_file(str(test_file))

    assert note.frontmatter["id"] == "note-test-001"
    assert note.frontmatter["name"] == "Test Note"
    assert note.frontmatter["type"] == "example"
    assert "# Content here" in note.body
    assert "test content" in note.body


def test_from_file_no_frontmatter(temp_dir):
    """Test parsing Note from file without frontmatter (empty dict expected)."""
    # Create test file without frontmatter
    test_file = temp_dir / "no_fm.md"
    content = "# Just Content\n\nNo frontmatter here."
    test_file.write_text(content, encoding="utf-8")

    # Parse file
    note = Note.from_file(str(test_file))

    assert note.frontmatter == {}
    assert "# Just Content" in note.body


def test_from_file_not_found():
    """Test that from_file raises FileNotFoundError for missing files."""
    with pytest.raises(FileNotFoundError):
        Note.from_file("nonexistent_file.md")


def test_to_file(temp_dir):
    """Test writing Note to file."""
    note = Note(
        file_path="output.md",
        frontmatter={"id": "note-001", "name": "Test"},
        body="# Test Content\n\nThis is a test.",
    )

    output_file = temp_dir / "output.md"
    note.to_file(str(output_file))

    # Verify file was created
    assert output_file.exists()

    # Verify contents
    content = output_file.read_text(encoding="utf-8")
    assert "id: note-001" in content
    assert "name: Test" in content
    assert "# Test Content" in content


def test_to_file_creates_parent_dirs(temp_dir):
    """Test that to_file creates parent directories if needed."""
    note = Note(file_path="nested/path/file.md", frontmatter={"id": "note-001"}, body="Content")

    output_file = temp_dir / "nested" / "path" / "file.md"
    note.to_file(str(output_file))

    assert output_file.exists()
    assert output_file.parent.exists()


def test_roundtrip(temp_dir):
    """Test read → write → read (verify identical)."""
    # Original note
    original = Note(
        file_path="test.md",
        frontmatter={
            "id": "note-roundtrip-001",
            "name": "Roundtrip Test",
            "tags": ["test", "roundtrip"],
        },
        body="# Roundtrip Test\n\nThis tests file I/O roundtrip.",
    )

    # Write to file
    test_file = temp_dir / "roundtrip.md"
    original.to_file(str(test_file))

    # Read back
    loaded = Note.from_file(str(test_file))

    # Verify identical
    assert loaded.frontmatter["id"] == original.frontmatter["id"]
    assert loaded.frontmatter["name"] == original.frontmatter["name"]
    assert loaded.frontmatter["tags"] == original.frontmatter["tags"]
    assert loaded.body == original.body


def test_modify_frontmatter():
    """Test modifying frontmatter and verify changes."""
    note = Note(
        file_path="test.md",
        frontmatter={"id": "note-001", "name": "Original"},
        body="Content",
    )

    # Modify frontmatter
    note.frontmatter["name"] = "Modified"
    note.frontmatter["new_field"] = "added"

    # Verify changes
    assert note.frontmatter["name"] == "Modified"
    assert note.frontmatter["new_field"] == "added"


def test_modify_body():
    """Test modifying body content and verify changes."""
    note = Note(file_path="test.md", frontmatter={"id": "note-001"}, body="Original content")

    # Modify body
    note.body = "# New Content\n\nModified body."

    # Verify changes
    assert note.body == "# New Content\n\nModified body."


def test_add_source_capsule():
    """Test adding capsule ID to provenance tracking."""
    note = Note(file_path="test.md", frontmatter={"id": "note-001"}, body="Content")

    # Initially None
    assert note.source_capsules is None

    # Add first capsule
    note.add_source_capsule("TCM_v1")
    assert note.source_capsules == ["TCM_v1"]
    assert note.frontmatter["source_capsules"] == ["TCM_v1"]

    # Add second capsule
    note.add_source_capsule("Culinary_v2")
    assert note.source_capsules == ["TCM_v1", "Culinary_v2"]

    # Add duplicate (should be ignored)
    note.add_source_capsule("TCM_v1")
    assert note.source_capsules == ["TCM_v1", "Culinary_v2"]


def test_add_source_capsule_with_existing_list():
    """Test adding to existing source_capsules list."""
    note = Note(
        file_path="test.md",
        frontmatter={"id": "note-001"},
        body="Content",
        source_capsules=["Existing_v1"],
    )

    note.add_source_capsule("New_v2")
    assert note.source_capsules == ["Existing_v1", "New_v2"]


def test_utf8_content(temp_dir):
    """Test handling Chinese characters and emojis in frontmatter and body."""
    note = Note(
        file_path="chinese.md",
        frontmatter={
            "id": "note-chinese-001",
            "name": "生姜 (Shēng Jiāng)",
            "pinyin": "Shēng Jiāng",
            "emoji": "🌿",
        },
        body="# 生姜 - Ginger 🌿\n\n中医草药 Traditional Chinese Medicine herb.",
    )

    # Write to file
    test_file = temp_dir / "chinese.md"
    note.to_file(str(test_file))

    # Read back
    loaded = Note.from_file(str(test_file))

    # Verify UTF-8 content preserved
    assert loaded.frontmatter["name"] == "生姜 (Shēng Jiāng)"
    assert loaded.frontmatter["pinyin"] == "Shēng Jiāng"
    assert loaded.frontmatter["emoji"] == "🌿"
    assert "生姜" in loaded.body
    assert "🌿" in loaded.body
    assert "中医草药" in loaded.body


def test_to_dict():
    """Test serializing Note to dictionary."""
    note = Note(
        file_path="test.md",
        frontmatter={"id": "note-001", "name": "Test"},
        body="Content",
        source_capsules=["TCM_v1"],
    )

    data = note.to_dict()

    assert data["file_path"] == "test.md"
    assert data["frontmatter"]["id"] == "note-001"
    assert data["body"] == "Content"
    assert data["source_capsules"] == ["TCM_v1"]


def test_repr():
    """Test string representation for debugging."""
    note = Note(
        file_path="test.md",
        frontmatter={"id": "note-001", "name": "Test"},
        body="Content",
    )

    repr_str = repr(note)

    assert "Note(" in repr_str
    assert "test.md" in repr_str
    assert "frontmatter_keys" in repr_str
