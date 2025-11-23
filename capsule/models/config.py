# capsule/models/config.py

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)


@dataclass
class Config:
    """
    Manages user-level and project-level configurations for the Capsule CLI.
    """

    llm_provider: str = "openai"
    api_key: str | None = None
    default_model: str = "gpt-4-turbo"
    project_dir: Path | None = None
    user: dict[str, str] = field(default_factory=dict)
    research: dict[str, str] = field(default_factory=dict)
    import_settings: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_yaml_file(cls, path: Path) -> "Config":
        """Loads a Config from a YAML file."""
        with open(path, encoding="utf-8") as f:
            data = yaml.load(f) or {}

        if "import" in data:
            data["import_settings"] = data.pop("import")

        return cls(**data)

    def to_yaml_file(self, path: Path) -> None:
        """Saves the Config to a YAML file."""
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(self.to_dict(), f)

    def to_dict(self) -> dict[str, Any]:
        """Converts the Config to a dictionary."""
        return {
            "llm_provider": self.llm_provider,
            "api_key": self.api_key,
            "default_model": self.default_model,
            "project_dir": str(self.project_dir) if self.project_dir else None,
            "user": self.user,
            "research": self.research,
            "import": self.import_settings,
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
        # Check standard XDG config path
        xdg_config_path = Path.home() / ".config" / "capsule" / "config.yaml"
        # Check legacy/alternative home config path
        legacy_config_path = Path.home() / ".capsule" / "config.yaml"

        # For project_dir, we'd typically search up from cwd for a .capsule dir
        # For now, we'll assume cwd is project root if .capsule exists
        local_config_path = Path.cwd() / ".capsule" / "config.yaml"

        config_data = {}

        # Load from legacy path first (lowest priority of globals)
        if legacy_config_path.exists():
            with open(legacy_config_path, encoding="utf-8") as f:
                config_data.update(yaml.load(f) or {})

        # Load from XDG path (overrides legacy)
        if xdg_config_path.exists():
            with open(xdg_config_path, encoding="utf-8") as f:
                config_data.update(yaml.load(f) or {})

        # Load from local path (highest priority)
        if local_config_path.exists():
            with open(local_config_path, encoding="utf-8") as f:
                config_data.update(yaml.load(f) or {})

        if "import" in config_data:
            config_data["import_settings"] = config_data.pop("import")

        return cls(**config_data)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Gets a value from the config using dot notation.
        """
        keys = key.split(".")
        value = self.to_dict()
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
