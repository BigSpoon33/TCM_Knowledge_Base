import re
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


class TemplateEngine:
    """
    Handles parsing of Markdown templates and filling them with content.
    Replaces the legacy TemplateParser and TemplateFiller.
    """

    def __init__(self):
        self.frontmatter = {}
        self.headings = []
        self.body_start_line = 0
        self.raw_content = ""

    def parse(self, template_path: Path) -> dict[str, Any]:
        """
        Parse template file and extract structure.
        """
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, encoding="utf-8") as f:
            self.raw_content = f.read()

        # Extract frontmatter
        self.frontmatter = self._extract_frontmatter(self.raw_content)

        # Extract headings
        self.headings = self._extract_headings(self.raw_content)

        return {
            "frontmatter": self.frontmatter,
            "headings": self.headings,
            "body_start_line": self.body_start_line,
            "raw_content": self.raw_content,
        }

    def fill(self, sections: dict[str, str], topic: str, context: dict[str, Any]) -> str:
        """
        Fill the parsed template with generated sections.
        """
        # Build frontmatter
        frontmatter_str = self._build_frontmatter(topic, context)

        # Build body content
        body_str = self._build_body(self.headings, sections)

        # Basic variable substitution
        body_str = body_str.replace("{{ topic }}", topic)
        body_str = body_str.replace("{{ Topic }}", topic)

        return f"{frontmatter_str}\n{body_str}"

    def _extract_frontmatter(self, content: str) -> dict[str, Any]:
        """Extract YAML frontmatter from markdown."""
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not match:
            return {}

        frontmatter_text = match.group(1)
        self.body_start_line = content[: match.end()].count("\n")

        try:
            # Remove comments
            frontmatter_text = re.sub(r"#[^\n]*", "", frontmatter_text)
            data = yaml.safe_load(frontmatter_text)
            return data or {}
        except yaml.YAMLError:
            return {}

    def _extract_headings(self, content: str) -> list[dict[str, Any]]:
        """Extract all headings from markdown content."""
        lines = content.split("\n")
        headings = []

        for line_num, line in enumerate(lines, 1):
            if line_num <= self.body_start_line:
                continue

            match = re.match(r"^(#{1,6})\s+(.+)$", line)
            if match:
                level = len(match.group(1))
                text = match.group(2).strip()
                clean_text = self._clean_heading_text(text)

                headings.append({"level": level, "text": text, "clean_text": clean_text, "children": []})

        return self._build_hierarchy(headings)

    def _clean_heading_text(self, text: str) -> str:
        """Remove emoji and special characters."""
        text = re.sub(r"[\U0001F300-\U0001F9FF]", "", text)
        text = re.sub(r"[\u2600-\u26FF\u2700-\u27BF]", "", text)
        return " ".join(text.split()).strip()

    def _build_hierarchy(self, headings: list[dict]) -> list[dict]:
        """Build hierarchical tree from flat heading list."""
        if not headings:
            return []

        root = []
        stack = []

        for heading in headings:
            level = heading["level"]
            while stack and stack[-1][0]["level"] >= level:
                stack.pop()

            if not stack:
                root.append(heading)
                stack.append((heading, heading["children"]))
            else:
                parent_children = stack[-1][1]
                parent_children.append(heading)
                stack.append((heading, heading["children"]))

        return root

    def _build_frontmatter(self, topic: str, context: dict[str, Any]) -> str:
        """Build YAML frontmatter."""
        fm = self.frontmatter.copy()

        # Update with dynamic values
        fm["topic"] = topic
        fm["created"] = datetime.now().strftime("%Y-%m-%d")

        # Merge with context if provided
        if context:
            fm.update({k: v for k, v in context.items() if k not in fm})

        yaml_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
        return f"---\n{yaml_str}---"

    def _build_body(self, headings: list[dict], sections: dict[str, str]) -> str:
        """Recursively build body content."""
        body = ""

        def process_heading(heading):
            nonlocal body
            level = heading["level"]
            text = heading["text"]
            clean_text = heading["clean_text"]

            body += f"{'#' * level} {text}\n\n"

            if clean_text in sections:
                body += sections[clean_text] + "\n\n"

            if level <= 2:
                body += "---\n\n"

            for child in heading["children"]:
                process_heading(child)

        for heading in headings:
            process_heading(heading)

        return body
