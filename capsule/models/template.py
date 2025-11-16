# capsule/models/template.py

from dataclasses import dataclass, field
from pathlib import Path
import ruamel.yaml
from typing import Any, Dict, List, Optional

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)

@dataclass
class TemplateSchema:
    """
    Represents the schema for a Capsule template, defining its structure,
    required fields, and domain-specific sections.
    """
    domain_type: str
    version: str
    required_fields: List[str] = field(default_factory=list)
    optional_fields: List[str] = field(default_factory=list)
    domain_sections: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_yaml_file(cls, path: Path) -> "TemplateSchema":
        """Loads a TemplateSchema from a YAML file."""
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.load(f)
        return cls(**data)

    def to_yaml_file(self, path: Path) -> None:
        """Saves the TemplateSchema to a YAML file."""
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(self.to_dict(), f)

    def to_dict(self) -> Dict[str, Any]:
        """Converts the TemplateSchema to a dictionary."""
        return {
            "domain_type": self.domain_type,
            "version": self.version,
            "required_fields": self.required_fields,
            "optional_fields": self.optional_fields,
            "domain_sections": self.domain_sections,
        }

    def validate_structure(self, data: Dict[str, Any]) -> bool:
        """
        Validates a given data dictionary against the schema's required fields.
        """
        for field_name in self.required_fields:
            if field_name not in data:
                return False
        return True
