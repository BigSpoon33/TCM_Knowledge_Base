# capsule/utils/yaml_handler.py

from pathlib import Path
from typing import Any

import ruamel.yaml

from .exceptions import YAMLFileError


class YAMLHandler:
    """A utility class for handling YAML file operations with ruamel.yaml."""

    _yaml = ruamel.yaml.YAML()
    _yaml.preserve_quotes = True
    _yaml.indent(mapping=2, sequence=4, offset=2)

    @staticmethod
    def read(path: Path) -> Any:
        """
        Reads and parses a YAML file, returning its content.
        Raises YAMLFileError on failure.
        """
        try:
            with open(path, encoding="utf-8") as f:
                return YAMLHandler._yaml.load(f)
        except FileNotFoundError:
            raise YAMLFileError(f"File not found: {path}")
        except ruamel.yaml.YAMLError as e:
            raise YAMLFileError(f"Error parsing YAML file: {path}") from e

    @staticmethod
    def write(path: Path, data: Any) -> None:
        """
        Writes given data to a YAML file.
        Raises YAMLFileError on failure.
        """
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                YAMLHandler._yaml.dump(data, f)
        except OSError as e:
            raise YAMLFileError(f"Error writing to file: {path}") from e
