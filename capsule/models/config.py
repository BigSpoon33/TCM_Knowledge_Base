# capsule/models/config.py

from dataclasses import dataclass, field
from pathlib import Path
import ruamel.yaml
from typing import Any, Dict, Optional

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)

@dataclass
class Config:
    """
    Manages user-level and project-level configurations for the Capsule CLI.
    """
    llm_provider: str = "openai"
    api_key: Optional[str] = None
    default_model: str = "gpt-4-turbo"
    project_dir: Optional[Path] = None

    @classmethod
    def from_yaml_file(cls, path: Path) -> "Config":
        """Loads a Config from a YAML file."""
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.load(f)
        return cls(**data)

    def to_yaml_file(self, path: Path) -> None:
        """Saves the Config to a YAML file."""
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(self.to_dict(), f)

    def to_dict(self) -> Dict[str, Any]:
        """Converts the Config to a dictionary."""
        return {
            "llm_provider": self.llm_provider,
            "api_key": self.api_key,
            "default_model": self.default_model,
            "project_dir": str(self.project_dir) if self.project_dir else None,
        }

    def validate(self) -> None:
        """
        Validates the configuration, raising an error if required fields
        are missing or invalid.
        """
        if not self.api_key:
            raise ValueError("API key is not set in the configuration.")

    @classmethod
    def load_config(cls) -> "Config":
        """
        Handles the hierarchical loading of global and local configuration
        files and returns a merged Config instance.
        """
        global_config_path = Path.home() / ".config" / "capsule" / "config.yaml"
        # For project_dir, we'd typically search up from cwd for a .capsule dir
        # For now, we'll assume cwd is project root if .capsule exists
        local_config_path = Path.cwd() / ".capsule" / "config.yaml"

        config_data = {}
        if global_config_path.exists():
            with open(global_config_path, 'r', encoding='utf-8') as f:
                config_data.update(yaml.load(f))

        if local_config_path.exists():
            with open(local_config_path, 'r', encoding='utf-8') as f:
                config_data.update(yaml.load(f))
        
        return cls(**config_data)
