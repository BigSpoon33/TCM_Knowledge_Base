import pytest

from capsule.core.merger import ConflictDetector, additive_merge, merge_notes, section_level_merge
from capsule.exceptions import MergeConflict
from capsule.models.note import Note


class TestSectionLevelMerge:
    """Test same-capsule update scenarios"""

    def test_updates_domain_section(self):
        """Test that a domain section is completely replaced by the incoming version."""
        existing = {
            "id": "note-1",
            "source_capsules": ["TCM_v1"],
            "herb_data": {"temperature": "warm", "taste": "sweet"},
        }
        incoming = {"herb_data": {"temperature": "warm", "dosage": "3-9g"}}

        result = section_level_merge(existing, incoming)

        # Should replace the entire dictionary
        assert result["herb_data"]["dosage"] == "3-9g"
        assert result["herb_data"]["temperature"] == "warm"
        assert "taste" not in result["herb_data"]  # Replaced, so 'taste' is gone if not in incoming

    def test_preserves_other_sections(self):
        """Test that sections not present in incoming are preserved."""
        existing = {"herb_data": {"temperature": "warm"}, "recipe_data": {"cuisine": "asian"}}
        incoming = {"herb_data": {"temperature": "cool"}}

        result = section_level_merge(existing, incoming)

        assert result["recipe_data"] == {"cuisine": "asian"}
        assert result["herb_data"]["temperature"] == "cool"

    def test_updates_universal_fields(self):
        """Test that universal fields are updated."""
        existing = {"id": "note-1", "name": "Old Name", "tags": ["old"]}
        incoming = {"name": "New Name", "tags": ["new", "updated"]}

        result = section_level_merge(existing, incoming)

        assert result["name"] == "New Name"
        assert result["tags"] == ["new", "updated"]
        assert result["id"] == "note-1"

    def test_incoming_empty(self):
        """Test that empty incoming dict changes nothing."""
        existing = {"id": "1", "data": "value"}
        incoming = {}

        result = section_level_merge(existing, incoming)

        assert result == existing

    def test_existing_empty(self):
        """Test that empty existing dict gets populated."""
        existing = {}
        incoming = {"id": "1", "herb_data": {"val": 1}}

        result = section_level_merge(existing, incoming)

        assert result == incoming

    def test_ignores_non_managed_fields(self):
        """Test that fields not in universal list and not ending in _data are ignored if in incoming."""
        existing = {"id": "1"}
        incoming = {"random_field": "should_be_ignored"}

        result = section_level_merge(existing, incoming)

        assert "random_field" not in result


class TestAdditiveMerge:
    """Test cross-capsule enhancement scenarios"""

    def test_adds_new_section_from_different_capsule(self):
        """Test that a new domain section is added."""
        existing = {"source_capsules": ["TCM_v1"], "herb_data": {"temperature": "warm"}}
        incoming = {"recipe_data": {"cuisine": "asian"}}

        result = additive_merge(existing, incoming, "Culinary_v1")

        assert "recipe_data" in result
        assert result["recipe_data"]["cuisine"] == "asian"
        assert result["herb_data"] == {"temperature": "warm"}

    def test_detects_conflict_when_same_section_exists(self):
        """Test that MergeConflict is raised when domain section already exists."""
        existing = {"source_capsules": ["TCM_v1"], "herb_data": {"temperature": "warm"}}
        incoming = {"herb_data": {"temperature": "cool"}}

        with pytest.raises(MergeConflict) as exc:
            additive_merge(existing, incoming, "Culinary_v1", file_path="test.md")

        assert "herb_data" in str(exc.value)
        assert "test.md" in str(exc.value)

    def test_preserves_existing_sections(self):
        """Test that all existing sections are preserved."""
        existing = {"id": "note-1", "herb_data": {"temperature": "warm"}, "other_field": "value"}
        incoming = {"recipe_data": {"cuisine": "asian"}}

        result = additive_merge(existing, incoming, "Culinary_v1")

        assert result["id"] == "note-1"
        assert result["herb_data"] == {"temperature": "warm"}
        assert result["other_field"] == "value"
        assert result["recipe_data"] == {"cuisine": "asian"}

    def test_ignores_non_domain_sections(self):
        """Test that non-domain sections in incoming are ignored."""
        existing = {"id": "note-1"}
        incoming = {"recipe_data": {"cuisine": "asian"}, "random_field": "ignore_me", "id": "note-2"}

        result = additive_merge(existing, incoming, "Culinary_v1")

        assert result["id"] == "note-1"
        assert "recipe_data" in result
        assert "random_field" not in result


class TestConflictDetector:
    """Test conflict detection logic for merge operations"""

    def test_no_conflict_with_identical_values(self):
        """Test that no conflict is raised when values are identical."""
        existing = {
            "id": "note-1",
            "source_capsules": [{"capsule_id": "tcm-v1", "version": "1.0.0", "sections_managed": ["herb_data"]}],
            "herb_data": {"temperature": "warm"},
        }
        new = {"herb_data": {"temperature": "warm"}}

        conflicts = ConflictDetector.detect_conflicts(existing, new, "tcm-v1")

        assert len(conflicts) == 0

    def test_capsule_conflict_different_values_different_owner(self):
        """Test that CAPSULE_CONFLICT (ERROR) is raised when different capsule owns the section."""
        existing = {
            "id": "note-1",
            "source_capsules": [{"capsule_id": "tcm-v1", "version": "1.0.0", "sections_managed": ["herb_data"]}],
            "herb_data": {"temperature": "warm"},
        }
        new = {"herb_data": {"temperature": "cool"}}

        conflicts = ConflictDetector.detect_conflicts(existing, new, "tcm-v2")

        assert len(conflicts) == 1
        assert conflicts[0].key == "herb_data"
        assert conflicts[0].existing_value == {"temperature": "warm"}
        assert conflicts[0].new_value == {"temperature": "cool"}
        assert conflicts[0].source_capsule == "tcm-v2"
        assert conflicts[0].severity == "ERROR"

    def test_user_conflict_existing_unmanaged_key(self):
        """Test that USER_CONFLICT (WARNING) is raised for user-created sections."""
        existing = {"id": "note-1", "source_capsules": [], "custom_notes": {"author_notes": "My personal notes"}}
        new = {"custom_notes": {"author_notes": "Capsule trying to overwrite"}}

        conflicts = ConflictDetector.detect_conflicts(existing, new, "tcm-v1")

        assert len(conflicts) == 1
        assert conflicts[0].key == "custom_notes"
        assert conflicts[0].severity == "WARNING"
        assert conflicts[0].source_capsule == "tcm-v1"

    def test_no_conflict_new_key(self):
        """Test that no conflict is raised for new keys not in existing."""
        existing = {"id": "note-1", "source_capsules": [], "herb_data": {"temperature": "warm"}}
        new = {"recipe_data": {"cuisine": "asian"}}

        conflicts = ConflictDetector.detect_conflicts(existing, new, "culinary-v1")

        assert len(conflicts) == 0

    def test_no_conflict_same_capsule_updates_own_section(self):
        """Test that same capsule can update its own managed sections without conflict."""
        existing = {
            "id": "note-1",
            "source_capsules": [{"capsule_id": "tcm-v1", "version": "1.0.0", "sections_managed": ["herb_data"]}],
            "herb_data": {"temperature": "warm"},
        }
        new = {"herb_data": {"temperature": "cool", "dosage": "3-9g"}}

        conflicts = ConflictDetector.detect_conflicts(existing, new, "tcm-v1")

        assert len(conflicts) == 0  # Same capsule can update its own sections

    def test_multiple_conflicts_detected(self):
        """Test that multiple conflicts are detected in a single pass."""
        existing = {
            "id": "note-1",
            "source_capsules": [{"capsule_id": "tcm-v1", "version": "1.0.0", "sections_managed": ["herb_data"]}],
            "herb_data": {"temperature": "warm"},
            "custom_field": {"user_notes": "my notes"},
        }
        new = {"herb_data": {"temperature": "cool"}, "custom_field": {"user_notes": "overwrite attempt"}}

        conflicts = ConflictDetector.detect_conflicts(existing, new, "tcm-v2")

        assert len(conflicts) == 2

        # Find each conflict by key
        herb_conflict = next(c for c in conflicts if c.key == "herb_data")
        custom_conflict = next(c for c in conflicts if c.key == "custom_field")

        assert herb_conflict.severity == "ERROR"
        assert custom_conflict.severity == "WARNING"

    def test_ignores_universal_fields(self):
        """Test that universal metadata fields are ignored by conflict detection."""
        existing = {
            "id": "note-1",
            "name": "Old Name",
            "type": "herb",
            "tags": ["old"],
            "created": "2025-01-01",
            "updated": "2025-01-01",
            "source_capsules": [],
        }
        new = {"id": "note-1", "name": "New Name", "type": "herb", "tags": ["new"], "updated": "2025-11-21"}

        conflicts = ConflictDetector.detect_conflicts(existing, new, "tcm-v1")

        # Universal fields should not trigger conflicts
        assert len(conflicts) == 0

    def test_empty_source_capsules(self):
        """Test behavior when source_capsules is empty list."""
        existing = {"id": "note-1", "source_capsules": [], "herb_data": {"temperature": "warm"}}
        new = {"herb_data": {"temperature": "cool"}}

        conflicts = ConflictDetector.detect_conflicts(existing, new, "tcm-v1")

        # Should detect user conflict since section not capsule-managed
        assert len(conflicts) == 1
        assert conflicts[0].severity == "WARNING"

    def test_missing_source_capsules_field(self):
        """Test behavior when source_capsules field doesn't exist."""
        existing = {"id": "note-1", "custom_data": {"value": "existing"}}
        new = {"custom_data": {"value": "new"}}

        conflicts = ConflictDetector.detect_conflicts(existing, new, "tcm-v1")

        # Should treat as user content (warning)
        assert len(conflicts) == 1
        assert conflicts[0].severity == "WARNING"

    def test_complex_nested_value_equality(self):
        """Test that complex nested structures are compared correctly."""
        existing = {
            "id": "note-1",
            "source_capsules": [],
            "herb_data": {
                "temperature": "warm",
                "channels": ["Lung", "Spleen", "Stomach"],
                "functions": {"primary": "warm", "secondary": "disperse"},
            },
        }
        new = {
            "herb_data": {
                "temperature": "warm",
                "channels": ["Lung", "Spleen", "Stomach"],
                "functions": {"primary": "warm", "secondary": "disperse"},
            }
        }

        conflicts = ConflictDetector.detect_conflicts(existing, new, "tcm-v1")

        # Deep equality should work - no conflict
        assert len(conflicts) == 0

    def test_multiple_source_capsules_complex_scenario(self):
        """Test scenario with multiple capsules managing different sections."""
        existing = {
            "id": "note-1",
            "source_capsules": [
                {"capsule_id": "tcm-v1", "version": "1.0.0", "sections_managed": ["herb_data"]},
                {"capsule_id": "culinary-v1", "version": "1.0.0", "sections_managed": ["recipe_data"]},
            ],
            "herb_data": {"temperature": "warm"},
            "recipe_data": {"cuisine": "asian"},
        }
        new = {
            "herb_data": {"temperature": "cool"},  # Different capsule trying to modify
            "recipe_data": {"cuisine": "italian"},  # Different capsule trying to modify
        }

        conflicts = ConflictDetector.detect_conflicts(existing, new, "tcm-v2")

        # Both sections should conflict (ERROR) since managed by different capsules
        assert len(conflicts) == 2
        assert all(c.severity == "ERROR" for c in conflicts)


class TestMergeNotes:
    """Test the merge_notes function which combines Note objects while preserving body content"""

    def test_preserves_body_content_from_existing_note(self):
        """
        Test that the body content of the existing note is ALWAYS preserved,
        even when the incoming note has different body content.

        This is the core requirement from AC#1 and AC#3.
        """
        existing = Note(
            file_path="test.md",
            frontmatter={
                "id": "note-1",
                "name": "Test Herb",
                "source_capsules": ["TCM_v1"],
                "herb_data": {"temperature": "warm"},
            },
            body="My personal notes about this herb.\nI use it for colds.",
        )
        incoming = Note(
            file_path="test.md",
            frontmatter={"herb_data": {"temperature": "warm", "dosage": "3-9g"}},
            body="This is completely different body content that should be DISCARDED.",
        )

        merged = merge_notes(existing, incoming, "TCM_v1")

        # Body from existing note MUST be preserved
        assert merged.body == "My personal notes about this herb.\nI use it for colds."
        # Frontmatter should be merged
        assert merged.frontmatter["herb_data"]["dosage"] == "3-9g"
        assert merged.frontmatter["herb_data"]["temperature"] == "warm"

    def test_section_level_merge_for_same_capsule(self):
        """
        Test that section-level merge is used when the same capsule
        updates its own sections (AC#2).
        """
        existing = Note(
            file_path="test.md",
            frontmatter={
                "id": "note-1",
                "source_capsules": ["TCM_v1"],
                "herb_data": {"temperature": "warm", "taste": "bitter"},
            },
            body="Original body content.",
        )
        incoming = Note(
            file_path="test.md",
            frontmatter={"herb_data": {"temperature": "cool", "dosage": "3-9g"}},
            body="Incoming body.",
        )

        merged = merge_notes(existing, incoming, "TCM_v1")

        # Section-level merge should replace the entire herb_data section
        assert merged.frontmatter["herb_data"] == {"temperature": "cool", "dosage": "3-9g"}
        # Body preserved
        assert merged.body == "Original body content."

    def test_additive_merge_for_different_capsule(self):
        """
        Test that additive merge is used when a different capsule
        contributes new sections (AC#2).
        """
        existing = Note(
            file_path="test.md",
            frontmatter={"id": "note-1", "source_capsules": ["TCM_v1"], "herb_data": {"temperature": "warm"}},
            body="My notes.",
        )
        incoming = Note(file_path="test.md", frontmatter={"recipe_data": {"cuisine": "asian"}}, body="Different body.")

        merged = merge_notes(existing, incoming, "Culinary_v1")

        # New section should be added
        assert "recipe_data" in merged.frontmatter
        assert merged.frontmatter["recipe_data"]["cuisine"] == "asian"
        # Original section preserved
        assert merged.frontmatter["herb_data"]["temperature"] == "warm"
        # New capsule added to source list
        assert "Culinary_v1" in merged.frontmatter["source_capsules"]
        # Body preserved
        assert merged.body == "My notes."

    def test_empty_body_is_preserved(self):
        """Test that even an empty body is preserved (edge case)."""
        existing = Note(
            file_path="test.md",
            frontmatter={"id": "note-1", "source_capsules": ["TCM_v1"], "herb_data": {"temperature": "warm"}},
            body="",
        )
        incoming = Note(
            file_path="test.md",
            frontmatter={"herb_data": {"temperature": "cool"}},
            body="This incoming body should be discarded.",
        )

        merged = merge_notes(existing, incoming, "TCM_v1")

        # Empty body should be preserved
        assert merged.body == ""

    def test_whitespace_only_body_is_preserved(self):
        """Test that body with only whitespace is preserved exactly."""
        existing = Note(
            file_path="test.md",
            frontmatter={"id": "note-1", "source_capsules": ["TCM_v1"]},
            body="   \n\n\t\n  ",
        )
        incoming = Note(file_path="test.md", frontmatter={"herb_data": {"temperature": "warm"}}, body="New content.")

        merged = merge_notes(existing, incoming, "TCM_v1")

        # Whitespace-only body preserved exactly
        assert merged.body == "   \n\n\t\n  "

    def test_complex_body_with_markdown_preserved(self):
        """Test that complex markdown body content is preserved intact."""
        complex_body = """# My Notes

## Section 1

- Bullet point 1
- Bullet point 2

### Subsection

Some **bold** and *italic* text.

```python
# Code block
def example():
    return "test"
```

[Link to something](https://example.com)

![Image](image.png)
"""
        existing = Note(
            file_path="test.md",
            frontmatter={"id": "note-1", "source_capsules": ["TCM_v1"]},
            body=complex_body,
        )
        incoming = Note(
            file_path="test.md",
            frontmatter={"herb_data": {"temperature": "warm"}},
            body="Simple body that should be discarded.",
        )

        merged = merge_notes(existing, incoming, "TCM_v1")

        # Complex markdown body preserved exactly
        assert merged.body == complex_body

    def test_raises_merge_conflict_on_domain_section_overlap(self):
        """
        Test that MergeConflict is raised when a different capsule
        tries to add a domain section that already exists.
        """
        existing = Note(
            file_path="test.md",
            frontmatter={"id": "note-1", "source_capsules": ["TCM_v1"], "herb_data": {"temperature": "warm"}},
            body="My notes.",
        )
        incoming = Note(
            file_path="test.md",
            frontmatter={"herb_data": {"temperature": "cool"}},  # Conflict!
            body="Different body.",
        )

        with pytest.raises(MergeConflict) as exc:
            merge_notes(existing, incoming, "Culinary_v1")

        assert "herb_data" in str(exc.value)
        assert "test.md" in str(exc.value)

    def test_handles_source_capsules_dict_format(self):
        """Test that detailed dict format for source_capsules is handled correctly."""
        existing = Note(
            file_path="test.md",
            frontmatter={
                "id": "note-1",
                "source_capsules": [{"capsule_id": "TCM_v1", "version": "1.0.0", "sections_managed": ["herb_data"]}],
                "herb_data": {"temperature": "warm"},
            },
            body="Original body.",
        )
        incoming = Note(
            file_path="test.md", frontmatter={"herb_data": {"temperature": "cool", "dosage": "3-9g"}}, body="New body."
        )

        merged = merge_notes(existing, incoming, "TCM_v1")

        # Should recognize TCM_v1 in dict format and do section-level merge
        assert merged.frontmatter["herb_data"]["dosage"] == "3-9g"
        assert merged.body == "Original body."

    def test_no_source_capsules_field_defaults_to_additive(self):
        """Test that missing source_capsules field is handled gracefully."""
        existing = Note(
            file_path="test.md", frontmatter={"id": "note-1", "herb_data": {"temperature": "warm"}}, body="Body."
        )
        incoming = Note(file_path="test.md", frontmatter={"recipe_data": {"cuisine": "asian"}}, body="New body.")

        merged = merge_notes(existing, incoming, "Culinary_v1")

        # Should use additive merge since no source_capsules
        assert "recipe_data" in merged.frontmatter
        assert "Culinary_v1" in merged.frontmatter["source_capsules"]
        assert merged.body == "Body."


class TestProvenanceTracking:
    """Test provenance tracking via source_capsules array (Story 8-6)"""

    def test_initial_note_creation_adds_source_capsule(self):
        """
        AC#1: When a note is created from a capsule, source_capsules array
        is added to frontmatter containing the source capsule ID.
        """
        # Simulate creating a new note (no existing note)
        # In practice, this would be handled by the import logic
        # Here we test that merge_notes adds source_capsules for new capsule
        existing = Note(
            file_path="test.md",
            frontmatter={"id": "note-1", "name": "Ginger"},
            body="",
        )
        incoming = Note(
            file_path="test.md",
            frontmatter={"herb_data": {"temperature": "warm"}},
            body="Capsule-generated content",
        )

        merged = merge_notes(existing, incoming, "TCM_v1")

        # source_capsules should be initialized with the capsule ID
        assert "source_capsules" in merged.frontmatter
        assert "TCM_v1" in merged.frontmatter["source_capsules"]
        assert isinstance(merged.frontmatter["source_capsules"], list)

    def test_same_capsule_update_preserves_source_capsules(self):
        """
        AC#2: When a note is updated by the same capsule, the source_capsules
        array MUST remain unchanged.
        """
        existing = Note(
            file_path="test.md",
            frontmatter={
                "id": "note-1",
                "source_capsules": ["TCM_v1"],
                "herb_data": {"temperature": "warm"},
            },
            body="My notes.",
        )
        incoming = Note(
            file_path="test.md",
            frontmatter={"herb_data": {"temperature": "warm", "dosage": "3-9g"}},
            body="Updated content.",
        )

        merged = merge_notes(existing, incoming, "TCM_v1")

        # source_capsules should remain exactly the same
        assert merged.frontmatter["source_capsules"] == ["TCM_v1"]
        # Frontmatter should be updated
        assert merged.frontmatter["herb_data"]["dosage"] == "3-9g"

    def test_different_capsule_appends_to_source_capsules(self):
        """
        AC#3: When a note is updated by a different capsule (additive merge),
        the new capsule's ID MUST be appended to the source_capsules array.
        """
        existing = Note(
            file_path="test.md",
            frontmatter={
                "id": "note-1",
                "source_capsules": ["TCM_v1"],
                "herb_data": {"temperature": "warm"},
            },
            body="My notes.",
        )
        incoming = Note(
            file_path="test.md",
            frontmatter={"recipe_data": {"cuisine": "asian"}},
            body="Recipe content.",
        )

        merged = merge_notes(existing, incoming, "Culinary_v1")

        # New capsule ID should be appended
        assert "source_capsules" in merged.frontmatter
        assert "TCM_v1" in merged.frontmatter["source_capsules"]
        assert "Culinary_v1" in merged.frontmatter["source_capsules"]
        assert len(merged.frontmatter["source_capsules"]) == 2

    def test_no_duplicate_capsule_ids_in_source_capsules(self):
        """
        AC#4: The source_capsules array MUST NOT contain duplicate capsule IDs.
        """
        # Start with a note that already has the capsule in source_capsules
        existing = Note(
            file_path="test.md",
            frontmatter={
                "id": "note-1",
                "source_capsules": ["TCM_v1"],
                "herb_data": {"temperature": "warm"},
            },
            body="My notes.",
        )
        incoming = Note(
            file_path="test.md",
            frontmatter={"herb_data": {"temperature": "cool", "dosage": "3-9g"}},
            body="Updated content.",
        )

        # Merge with same capsule (section-level merge)
        merged = merge_notes(existing, incoming, "TCM_v1")

        # Should still have only one entry for TCM_v1
        assert merged.frontmatter["source_capsules"].count("TCM_v1") == 1

    def test_multiple_capsules_contribute_to_same_note(self):
        """
        Test that multiple different capsules can contribute to the same note
        and all are tracked in source_capsules.
        """
        # Start with note from first capsule
        existing = Note(
            file_path="test.md",
            frontmatter={
                "id": "note-1",
                "source_capsules": ["TCM_v1"],
                "herb_data": {"temperature": "warm"},
            },
            body="Original content.",
        )

        # Add content from second capsule
        incoming2 = Note(
            file_path="test.md",
            frontmatter={"recipe_data": {"cuisine": "asian"}},
            body="Recipe content.",
        )
        merged2 = merge_notes(existing, incoming2, "Culinary_v1")

        # Add content from third capsule
        incoming3 = Note(
            file_path="test.md",
            frontmatter={"remedy_data": {"condition": "nausea"}},
            body="Remedy content.",
        )
        merged3 = merge_notes(merged2, incoming3, "HomeRemedies_v1")

        # All three capsules should be tracked
        assert len(merged3.frontmatter["source_capsules"]) == 3
        assert "TCM_v1" in merged3.frontmatter["source_capsules"]
        assert "Culinary_v1" in merged3.frontmatter["source_capsules"]
        assert "HomeRemedies_v1" in merged3.frontmatter["source_capsules"]

        # All sections should be present
        assert "herb_data" in merged3.frontmatter
        assert "recipe_data" in merged3.frontmatter
        assert "remedy_data" in merged3.frontmatter

        # Body should be preserved from original
        assert merged3.body == "Original content."

    def test_empty_source_capsules_initialized_correctly(self):
        """
        Test that if source_capsules doesn't exist, it's initialized as a list.
        """
        existing = Note(
            file_path="test.md",
            frontmatter={"id": "note-1"},
            body="Content.",
        )
        incoming = Note(
            file_path="test.md",
            frontmatter={"herb_data": {"temperature": "warm"}},
            body="New content.",
        )

        merged = merge_notes(existing, incoming, "TCM_v1")

        # source_capsules should be created and populated
        assert "source_capsules" in merged.frontmatter
        assert isinstance(merged.frontmatter["source_capsules"], list)
        assert "TCM_v1" in merged.frontmatter["source_capsules"]

    def test_source_capsules_persisted_to_file(self):
        """
        Test that source_capsules array is correctly written to file
        when Note.to_file() is called.
        """
        import os
        import tempfile

        existing = Note(
            file_path="test.md",
            frontmatter={
                "id": "note-1",
                "source_capsules": ["TCM_v1"],
                "herb_data": {"temperature": "warm"},
            },
            body="My notes.",
        )
        incoming = Note(
            file_path="test.md",
            frontmatter={"recipe_data": {"cuisine": "asian"}},
            body="Recipe content.",
        )

        merged = merge_notes(existing, incoming, "Culinary_v1")

        # Write to temporary file
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = os.path.join(tmpdir, "test.md")
            merged.to_file(test_file)

            # Read back and verify source_capsules is in the file
            reloaded = Note.from_file(test_file)
            assert "source_capsules" in reloaded.frontmatter
            assert "TCM_v1" in reloaded.frontmatter["source_capsules"]
            assert "Culinary_v1" in reloaded.frontmatter["source_capsules"]
            assert reloaded.body == "My notes."
