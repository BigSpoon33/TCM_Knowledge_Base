import pytest
from capsule.core.merger import section_level_merge, additive_merge, Conflict, ConflictDetector
from capsule.exceptions import MergeConflict


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
