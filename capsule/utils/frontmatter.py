import re
from io import StringIO
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML
from ruamel.yaml.error import YAMLError

from capsule.exceptions import FileError, ValidationError


class FrontmatterHandler:
    """
    Handles reading and writing of markdown files with YAML frontmatter,
    preserving comments and ordering using ruamel.yaml.
    """

    def __init__(self, content: str = ""):
        self.yaml = YAML()
        self.yaml.preserve_quotes = True
        self.yaml.indent(mapping=2, sequence=4, offset=2)
        self.yaml.width = 4096  # Prevent line wrapping for long strings

        self._frontmatter_data: Any = None
        self._body: str = ""
        self._has_frontmatter: bool = False

        if content:
            self._parse(content)
        else:
            # Initialize empty
            self._frontmatter_data = self.yaml.load("{}")
            self._body = ""

    def _parse(self, content: str):
        """Parse content into frontmatter and body."""
        # Regex to find frontmatter: starts with ---, ends with ---
        # We use a non-greedy match for the content inside
        # Handle potential Windows line endings by normalizing or using \r?
        # But usually python reads as \n.

        # Pattern: Start of string, ---, newline, content, newline, ---, newline or end of string
        pattern = r"^---\s*\n(.*?)\n---\s*(?:\n|$)(.*)$"
        match = re.match(pattern, content, re.DOTALL)

        if match:
            self._has_frontmatter = True
            raw_frontmatter = match.group(1)
            self._body = match.group(2)
            try:
                self._frontmatter_data = self.yaml.load(raw_frontmatter)
                if self._frontmatter_data is None:
                    self._frontmatter_data = self.yaml.load("{}")
            except YAMLError as e:
                raise ValidationError(f"Invalid YAML frontmatter: {e}")
        else:
            self._has_frontmatter = False
            self._frontmatter_data = self.yaml.load("{}")
            self._body = content

    def load(self, file_path: Path) -> "FrontmatterHandler":
        """Load content from a file."""
        if not file_path.exists():
            raise FileError(f"File not found: {file_path}")

        content = file_path.read_text(encoding="utf-8")
        self._parse(content)
        return self

    def save(self, file_path: Path):
        """Save content to a file."""
        content = self.to_string()
        file_path.write_text(content, encoding="utf-8")

    def to_string(self) -> str:
        """Convert back to string."""
        # If we have data or had frontmatter, we should write it.
        # Check if data is empty
        is_empty = not self._frontmatter_data

        if not self._has_frontmatter and is_empty:
            return self._body

        stream = StringIO()
        self.yaml.dump(self._frontmatter_data, stream)
        yaml_str = stream.getvalue()

        # ruamel.yaml dump usually ends with a newline if there is content
        # If yaml_str is empty (e.g. {}), it might be "{}\n" or similar depending on flow style
        # But we initialized with load("{}") which is empty dict.

        # If it's just empty dict, dump might produce "{}\n".
        # We want to avoid "{}" in frontmatter if possible, usually we want empty or just keys.

        if yaml_str.strip() == "{}":
            yaml_str = ""

        return f"---\n{yaml_str}---\n{self._body}"

    def get_frontmatter(self) -> Any:
        """Get the frontmatter data object (ruamel CommentedMap)."""
        return self._frontmatter_data

    def get_body(self) -> str:
        """Get the body content."""
        return self._body

    def set_frontmatter(self, data: dict | Any):
        """Set the frontmatter data."""
        self._frontmatter_data = data
        self._has_frontmatter = True

    def set_body(self, content: str):
        """Set the body content."""
        self._body = content
