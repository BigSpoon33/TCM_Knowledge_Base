"""CapsuleCypher data model - represents the capsule manifest (cypher) file."""

import io
from dataclasses import asdict, dataclass
from typing import Any

import ruamel.yaml


@dataclass
class CapsuleCypher:
    """
    Represents a capsule cypher - the manifest defining capsule structure and content.

    The capsule cypher is stored as capsule-cypher.yaml in the root of every capsule.
    It defines metadata, file organization, schemas, and configuration.

    Attributes:
        capsule_id: Unique identifier (e.g., "TCM_Herbs_v1")
        name: Human-readable name
        version: Semantic version string (e.g., "1.0.0")
        domain_type: Content domain (e.g., "tcm", "education")
        folder_structure: Dict mapping logical names to folder paths
        contents: Dict organizing files by category with IDs
        data_schemas: Dict defining frontmatter schemas for domain sections
        sequence_mode: Learning sequence type ("freeform", "sequenced", "hybrid")
        required_plugins: List of required Obsidian plugins (optional)
        recommended_plugins: List of recommended plugins (optional)

    Example:
        >>> cypher = CapsuleCypher(
        ...     capsule_id="TCM_Test_v1",
        ...     name="TCM Test Capsule",
        ...     version="1.0.0",
        ...     domain_type="tcm",
        ...     folder_structure={"root_notes": "root_notes/"},
        ...     contents={"root_notes": []},
        ...     data_schemas={},
        ...     sequence_mode="freeform"
        ... )
        >>> cypher.capsule_id
        'TCM_Test_v1'
    """

    # Required fields
    capsule_id: str
    name: str
    version: str
    domain_type: str
    folder_structure: dict[str, str]
    contents: dict[str, Any]
    data_schemas: dict[str, Any]

    # Optional fields
    sequence_mode: str | None = None
    dashboard_metadata: dict[str, Any] | None = None
    required_plugins: list[dict[str, str]] | None = None
    recommended_plugins: list[dict[str, str]] | None = None

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize cypher to dictionary.

        Returns:
            Dictionary representation suitable for YAML export

        Example:
            >>> cypher = CapsuleCypher(
            ...     capsule_id="test-v1",
            ...     name="Test",
            ...     version="1.0.0",
            ...     domain_type="education",
            ...     folder_structure={},
            ...     contents={},
            ...     data_schemas={},
            ...     sequence_mode="freeform"
            ... )
            >>> data = cypher.to_dict()
            >>> data["capsule_id"]
            'test-v1'
        """
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "CapsuleCypher":
        """
        Create cypher from dictionary.

        Args:
            data: Dictionary with cypher fields

        Returns:
            CapsuleCypher instance

        Example:
            >>> data = {
            ...     "capsule_id": "test-v1",
            ...     "name": "Test",
            ...     "version": "1.0.0",
            ...     "domain_type": "education",
            ...     "folder_structure": {},
            ...     "contents": {},
            ...     "data_schemas": {},
            ...     "sequence_mode": "freeform"
            ... }
            >>> cypher = CapsuleCypher.from_dict(data)
            >>> cypher.name
            'Test'
        """
        return cls(**data)

    def to_yaml(self) -> str:
        """
        Serialize cypher to YAML string.

        Uses ruamel.yaml to preserve formatting and allow comments.

        Returns:
            YAML string representation

        Example:
            >>> cypher = CapsuleCypher(
            ...     capsule_id="test-v1",
            ...     name="Test",
            ...     version="1.0.0",
            ...     domain_type="education",
            ...     folder_structure={},
            ...     contents={},
            ...     data_schemas={},
            ...     sequence_mode="freeform"
            ... )
            >>> yaml_str = cypher.to_yaml()
            >>> "capsule_id: test-v1" in yaml_str
            True
        """
        yaml = ruamel.yaml.YAML()
        yaml.default_flow_style = False

        stream = io.StringIO()
        yaml.dump(self.to_dict(), stream)
        return stream.getvalue()

    @classmethod
    def from_yaml(cls, yaml_content: str) -> "CapsuleCypher":
        """
        Create cypher from YAML string.

        Args:
            yaml_content: YAML string content

        Returns:
            CapsuleCypher instance

        Example:
            >>> yaml_str = '''
            ... capsule_id: test-v1
            ... name: Test
            ... version: 1.0.0
            ... domain_type: education
            ... folder_structure: {}
            ... contents: {}
            ... data_schemas: {}
            ... sequence_mode: freeform
            ... '''
            >>> cypher = CapsuleCypher.from_yaml(yaml_str)
            >>> cypher.capsule_id
            'test-v1'
        """
        yaml = ruamel.yaml.YAML()
        data = yaml.load(yaml_content)
        return cls.from_dict(data)
