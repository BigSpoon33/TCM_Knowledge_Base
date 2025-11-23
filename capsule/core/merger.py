from dataclasses import dataclass
from typing import Any

from capsule.exceptions import MergeConflict
from capsule.models.note import Note


@dataclass
class Conflict:
    """
    Represents a merge conflict between capsule data and existing note data.

    Attributes:
        key: The frontmatter key that has a conflict
        existing_value: The current value in the existing note
        new_value: The new value from the incoming capsule
        source_capsule: The capsule ID attempting to write the conflicting value
        severity: Level of conflict severity ("WARNING" or "ERROR")

    Example:
        >>> conflict = Conflict(
        ...     key="herb_data",
        ...     existing_value={"temperature": "warm"},
        ...     new_value={"temperature": "cool"},
        ...     source_capsule="tcm-herbs-v2",
        ...     severity="ERROR"
        ... )
    """

    key: str
    existing_value: Any
    new_value: Any
    source_capsule: str
    severity: str  # "WARNING", "ERROR"


class ConflictDetector:
    """
    Detects conflicts when merging capsule frontmatter into existing notes.

    The ConflictDetector identifies three types of conflicts:
    1. CAPSULE_CONFLICT: Different capsules trying to manage the same section
    2. USER_CONFLICT: Capsule trying to overwrite user-created content
    3. No conflict: Values are identical or key is new

    The detector uses the source_capsules field to determine ownership:
    - If a key is in source_capsules, it's capsule-managed
    - If a key exists but NOT in source_capsules, it's user-created
    - If values match, no conflict regardless of ownership
    """

    @staticmethod
    def detect_conflicts(
        existing_fm: dict[str, Any], new_fm: dict[str, Any], incoming_capsule_id: str
    ) -> list[Conflict]:
        """
        Detect conflicts between existing frontmatter and new capsule frontmatter.

        Args:
            existing_fm: Current frontmatter from the existing note
            new_fm: Incoming frontmatter from the capsule being imported
            incoming_capsule_id: ID of the capsule being imported

        Returns:
            List of Conflict objects representing detected conflicts

        Algorithm:
            1. Iterate through all top-level keys in new frontmatter
            2. For each key, check provenance in source_capsules
            3. If key is managed by different capsule and values differ: CAPSULE_CONFLICT
            4. If key exists but not capsule-managed and values differ: USER_CONFLICT
            5. If values are identical: No conflict
            6. If key doesn't exist: No conflict (new addition)

        Example:
            >>> existing = {
            ...     "id": "note-1",
            ...     "source_capsules": [
            ...         {
            ...             "capsule_id": "tcm-v1",
            ...             "version": "1.0.0",
            ...             "sections_managed": ["herb_data"]
            ...         }
            ...     ],
            ...     "herb_data": {"temperature": "warm"}
            ... }
            >>> new = {
            ...     "herb_data": {"temperature": "cool"}
            ... }
            >>> conflicts = ConflictDetector.detect_conflicts(existing, new, "tcm-v2")
            >>> len(conflicts)
            1
            >>> conflicts[0].severity
            'ERROR'
        """
        conflicts: list[Conflict] = []

        # Get source_capsules list from existing frontmatter
        source_capsules = existing_fm.get("source_capsules", [])

        # Build a map of which sections are managed by which capsules
        # Support both simple string format and detailed dict format
        managed_sections: dict[str, str] = {}
        if source_capsules:
            for source in source_capsules:
                if isinstance(source, dict):
                    # Detailed format with sections_managed
                    capsule_id = source.get("capsule_id", "")
                    sections = source.get("sections_managed", [])
                    for section in sections:
                        managed_sections[section] = capsule_id
                elif isinstance(source, str):
                    # Simple string format - assume it manages all _data sections
                    # This is a fallback for simpler implementations
                    pass

        # Check each key in incoming frontmatter
        for key, new_value in new_fm.items():
            # Skip metadata fields that aren't domain data
            if key in ["id", "name", "type", "tags", "created", "updated", "source_capsules"]:
                continue

            # Check if key exists in existing frontmatter
            if key not in existing_fm:
                # New key, no conflict
                continue

            existing_value = existing_fm[key]

            # If values are identical, no conflict
            if existing_value == new_value:
                continue

            # Values differ - check ownership
            if key in managed_sections:
                # This section is managed by a capsule
                managing_capsule = managed_sections[key]

                if managing_capsule != incoming_capsule_id:
                    # Different capsule trying to manage this section
                    conflicts.append(
                        Conflict(
                            key=key,
                            existing_value=existing_value,
                            new_value=new_value,
                            source_capsule=incoming_capsule_id,
                            severity="ERROR",
                        )
                    )
                # else: Same capsule updating its own section - this is allowed
            else:
                # Section exists but is NOT capsule-managed (user-created)
                conflicts.append(
                    Conflict(
                        key=key,
                        existing_value=existing_value,
                        new_value=new_value,
                        source_capsule=incoming_capsule_id,
                        severity="WARNING",  # User conflict is a warning
                    )
                )

        return conflicts


def section_level_merge(existing: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    """
    Update matching sections in existing frontmatter with values from incoming frontmatter,
    while preserving other sections.

    Args:
        existing: The existing frontmatter dictionary.
        incoming: The incoming frontmatter dictionary from the capsule.

    Returns:
        The merged frontmatter dictionary.
    """
    merged = existing.copy()

    # Universal fields that should be updated
    universal_fields = [
        "id",
        "name",
        "type",
        "tags",
        "created",
        "updated",
        "capsule_id",
        "version",
        "dashboard_metadata",
    ]

    for section_key, section_value in incoming.items():
        # Update domain sections (ending with _data)
        if section_key.endswith("_data"):
            merged[section_key] = section_value
        # Update universal fields
        elif section_key in universal_fields:
            merged[section_key] = section_value

    return merged

    return merged


def additive_merge(
    existing: dict[str, Any], incoming: dict[str, Any], capsule_id: str, file_path: str = "unknown"
) -> dict[str, Any]:
    """
    Add new sections from incoming frontmatter to existing frontmatter,
    raising MergeConflict if sections overlap.

    Args:
        existing: The existing frontmatter dictionary.
        incoming: The incoming frontmatter dictionary.
        capsule_id: The ID of the capsule being imported.
        file_path: Path to the file being merged (for error reporting).

    Returns:
        The merged frontmatter dictionary.

    Raises:
        MergeConflict: If a domain section in incoming already exists in existing.
    """
    merged = existing.copy()

    for section_key, section_value in incoming.items():
        # Check for domain sections (ending with _data)
        if section_key.endswith("_data"):
            if section_key in existing:
                raise MergeConflict(
                    file=file_path,
                    section=section_key,
                    existing_source=existing.get("source_capsules", []),
                    incoming_source=capsule_id,
                )
            merged[section_key] = section_value

    return merged


def merge_notes(existing_note: Note, incoming_note: Note, capsule_id: str) -> Note:
    """
    Merge frontmatter from incoming note into existing note while ALWAYS preserving
    the existing note's body content.

    This is the core merge function that implements the Capsule merge algorithm:
    1. Same capsule ID + newer version → UPDATE sections (section-level merge)
    2. Different capsule ID → ADD sections (additive merge)
    3. User content (body) → ALWAYS PRESERVE
    4. Conflicts → Raise MergeConflict exception

    Args:
        existing_note: The current note in the vault
        incoming_note: The new note from the capsule import
        capsule_id: The ID of the capsule being imported

    Returns:
        Merged Note with combined frontmatter and the existing note's body

    Raises:
        MergeConflict: If domain sections conflict during additive merge

    Example:
        >>> existing = Note(
        ...     file_path="test.md",
        ...     frontmatter={
        ...         "id": "note-1",
        ...         "source_capsules": ["TCM_v1"],
        ...         "herb_data": {"temperature": "warm"}
        ...     },
        ...     body="My personal notes about this herb."
        ... )
        >>> incoming = Note(
        ...     file_path="test.md",
        ...     frontmatter={
        ...         "herb_data": {"temperature": "warm", "dosage": "3-9g"}
        ...     },
        ...     body="This body will be DISCARDED."
        ... )
        >>> merged = merge_notes(existing, incoming, "TCM_v1")
        >>> merged.frontmatter["herb_data"]["dosage"]
        '3-9g'
        >>> merged.body
        'My personal notes about this herb.'
    """
    # Extract frontmatter
    existing_fm = existing_note.frontmatter
    existing_body = existing_note.body

    # Check capsule provenance to determine merge strategy
    existing_sources = existing_fm.get("source_capsules", [])

    # Handle both simple string format and detailed dict format for source_capsules
    existing_capsule_ids = []
    if existing_sources:
        for source in existing_sources:
            if isinstance(source, dict):
                # Detailed format with capsule_id, version, sections_managed
                existing_capsule_ids.append(source.get("capsule_id", ""))
            elif isinstance(source, str):
                # Simple string format (just capsule ID)
                existing_capsule_ids.append(source)

    # Determine merge strategy based on capsule provenance
    if capsule_id in existing_capsule_ids:
        # Same capsule update - section-level merge
        merged_fm = section_level_merge(existing_fm, incoming_note.frontmatter)
    else:
        # Different capsule - additive merge
        merged_fm = additive_merge(
            existing_fm, incoming_note.frontmatter, capsule_id, file_path=existing_note.file_path
        )
        # Add capsule to source list if not already present
        if capsule_id not in existing_capsule_ids:
            if "source_capsules" not in merged_fm:
                merged_fm["source_capsules"] = []
            merged_fm["source_capsules"].append(capsule_id)

    # CRITICAL: Always preserve user content (body)
    return Note(file_path=existing_note.file_path, frontmatter=merged_fm, body=existing_body, source_capsules=None)
