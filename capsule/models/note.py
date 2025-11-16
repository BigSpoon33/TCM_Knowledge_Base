"""
Note data model for Obsidian markdown files with YAML frontmatter.

This module provides the Note class for parsing, manipulating, and writing
markdown files with YAML frontmatter using the python-frontmatter library.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional
import frontmatter  # type: ignore[import-untyped]


@dataclass
class Note:
    """
    Represents an Obsidian markdown note with YAML frontmatter.

    The Note model uses python-frontmatter library for safe parsing and writing
    of markdown files with YAML frontmatter. It supports provenance tracking
    to enable cross-domain composability (multiple capsules contributing to
    the same note).

    Attributes:
        file_path: Relative or absolute path to the .md file
        frontmatter: YAML frontmatter as dictionary (flexible schema)
        body: Markdown content after frontmatter
        source_capsules: Optional list of capsule IDs that contributed to this note

    Example:
        >>> note = Note(
        ...     file_path="root_notes/Ginger.md",
        ...     frontmatter={
        ...         "id": "note-ginger-001",
        ...         "name": "Ginger",
        ...         "type": "herb"
        ...     },
        ...     body="# Ginger\\n\\nGinger is a medicinal herb."
        ... )
        >>> note.file_path
        'root_notes/Ginger.md'
        >>> note.frontmatter["name"]
        'Ginger'
    """

    file_path: str
    frontmatter: dict[str, Any]
    body: str
    source_capsules: Optional[list[str]] = None

    @classmethod
    def from_file(cls, filepath: str) -> "Note":
        """
        Parse markdown file with frontmatter and create Note instance.

        Uses python-frontmatter library to safely parse YAML frontmatter
        and markdown body content. Handles files with or without frontmatter.

        Args:
            filepath: Path to markdown file (relative or absolute)

        Returns:
            Note instance with parsed frontmatter and body

        Raises:
            FileNotFoundError: If the file does not exist

        Example:
            >>> # Given a file test.md with:
            >>> # ---
            >>> # id: note-001
            >>> # name: Test
            >>> # ---
            >>> # # Content here
            >>> note = Note.from_file("test.md")
            >>> note.frontmatter["id"]
            'note-001'
            >>> "# Content" in note.body
            True
        """
        path = Path(filepath)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")

        # Parse frontmatter using python-frontmatter library
        with open(path, "r", encoding="utf-8") as f:
            post = frontmatter.load(f)

        # Extract frontmatter dict and body content
        fm_dict = dict(post.metadata) if post.metadata else {}
        body_content = post.content

        # Extract source_capsules from frontmatter if present
        source_capsules = fm_dict.get("source_capsules", None)

        return cls(
            file_path=str(filepath),
            frontmatter=fm_dict,
            body=body_content,
            source_capsules=source_capsules,
        )

    def to_file(self, filepath: str) -> None:
        """
        Write Note to markdown file with frontmatter.

        Uses python-frontmatter library to serialize frontmatter and body
        content. Creates parent directories if needed. Always uses UTF-8 encoding.

        Args:
            filepath: Path to write the file (relative or absolute)

        Example:
            >>> note = Note(
            ...     file_path="output.md",
            ...     frontmatter={"id": "note-001", "name": "Test"},
            ...     body="# Test Content"
            ... )
            >>> note.to_file("output.md")
            >>> # File created with frontmatter and body
        """
        path = Path(filepath)

        # Create parent directories if they don't exist
        path.parent.mkdir(parents=True, exist_ok=True)

        # Update frontmatter with source_capsules if present
        fm_dict = self.frontmatter.copy()
        if self.source_capsules is not None:
            fm_dict["source_capsules"] = self.source_capsules

        # Create frontmatter Post object
        post = frontmatter.Post(self.body, **fm_dict)

        # Write to file with UTF-8 encoding
        with open(path, "w", encoding="utf-8") as f:
            f.write(frontmatter.dumps(post))

    def add_source_capsule(self, capsule_id: str) -> None:
        """
        Add capsule ID to source_capsules list for provenance tracking.

        Initializes source_capsules list if None. Prevents duplicate entries.
        Updates both the instance field and frontmatter dict.

        Args:
            capsule_id: Capsule ID to add (e.g., "TCM_Materia_Medica_v1")

        Example:
            >>> note = Note(
            ...     file_path="test.md",
            ...     frontmatter={"id": "note-001"},
            ...     body="Content"
            ... )
            >>> note.add_source_capsule("TCM_v1")
            >>> note.source_capsules
            ['TCM_v1']
            >>> note.add_source_capsule("TCM_v1")  # Duplicate ignored
            >>> note.source_capsules
            ['TCM_v1']
        """
        # Initialize list if None
        if self.source_capsules is None:
            self.source_capsules = []

        # Add capsule ID if not already present (prevent duplicates)
        if capsule_id not in self.source_capsules:
            self.source_capsules.append(capsule_id)

        # Update frontmatter dict as well
        self.frontmatter["source_capsules"] = self.source_capsules

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize Note to dictionary.

        Returns:
            Dictionary representation suitable for JSON/YAML export

        Example:
            >>> note = Note(
            ...     file_path="test.md",
            ...     frontmatter={"id": "note-001"},
            ...     body="Content"
            ... )
            >>> data = note.to_dict()
            >>> data["file_path"]
            'test.md'
        """
        return {
            "file_path": self.file_path,
            "frontmatter": self.frontmatter,
            "body": self.body,
            "source_capsules": self.source_capsules,
        }

    def __repr__(self) -> str:
        """
        Return string representation for debugging.

        Returns:
            String showing file path and frontmatter keys
        """
        fm_keys = list(self.frontmatter.keys()) if self.frontmatter else []
        return f"Note(file_path='{self.file_path}', frontmatter_keys={fm_keys})"
