#!/usr/bin/env python3
"""
Template Parser - Extract heading structure from markdown templates.

This module parses markdown template files and extracts:
- YAML frontmatter
- Heading hierarchy (# ## ### ####)
- Template structure for content generation
"""

import re
from pathlib import Path
from typing import Any

import yaml


class TemplateParser:
    """Parse markdown templates and extract structure."""

    def __init__(self):
        self.frontmatter = {}
        self.headings = []
        self.body_start_line = 0

    def parse(self, template_path: Path) -> dict[str, Any]:
        """
        Parse template file and extract structure.

        Args:
            template_path: Path to markdown template file

        Returns:
            {
                'frontmatter': {...},  # YAML frontmatter dict
                'headings': [...],     # List of heading dicts
                'body_start_line': int,  # Line where body starts
                'raw_content': str     # Full file content
            }
        """
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, encoding="utf-8") as f:
            content = f.read()

        # Extract frontmatter
        self.frontmatter = self._extract_frontmatter(content)

        # Extract headings
        self.headings = self._extract_headings(content)

        return {
            "frontmatter": self.frontmatter,
            "headings": self.headings,
            "body_start_line": self.body_start_line,
            "raw_content": content,
            "template_path": template_path,
        }

    def _extract_frontmatter(self, content: str) -> dict[str, Any]:
        """Extract YAML frontmatter from markdown."""
        # Match frontmatter between --- markers
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)

        if not match:
            return {}

        frontmatter_text = match.group(1)

        # Find where body starts (after frontmatter)
        self.body_start_line = content[: match.end()].count("\n")

        try:
            # Parse YAML, handling comments
            frontmatter_text = re.sub(r"#[^\n]*", "", frontmatter_text)
            data = yaml.safe_load(frontmatter_text)
            return data or {}
        except yaml.YAMLError as e:
            print(f"⚠️  YAML parsing error: {e}")
            return {}

    def _extract_headings(self, content: str) -> list[dict[str, Any]]:
        """
        Extract all headings from markdown content.

        Returns list of heading dicts with hierarchy.
        """
        lines = content.split("\n")
        headings = []

        for line_num, line in enumerate(lines, 1):
            # Skip frontmatter
            if line_num <= self.body_start_line:
                continue

            # Match markdown headings (# ## ### ####)
            match = re.match(r"^(#{1,6})\s+(.+)$", line)

            if match:
                level = len(match.group(1))  # Number of # symbols
                text = match.group(2).strip()

                # Remove emoji and special characters for clean text
                clean_text = self._clean_heading_text(text)

                heading = {
                    "level": level,
                    "text": text,  # Original with emoji
                    "clean_text": clean_text,  # Without emoji
                    "line_number": line_num,
                    "full_line": line,
                }

                headings.append(heading)

        # Build hierarchy
        headings_tree = self._build_hierarchy(headings)

        return headings_tree

    def _clean_heading_text(self, text: str) -> str:
        """Remove emoji and special characters from heading text."""
        # Remove emoji (Unicode ranges)
        text = re.sub(r"[\U0001F300-\U0001F9FF]", "", text)
        # Remove other emoji ranges
        text = re.sub(r"[\u2600-\u26FF\u2700-\u27BF]", "", text)
        # Remove extra whitespace
        text = " ".join(text.split())
        return text.strip()

    def _build_hierarchy(self, headings: list[dict]) -> list[dict]:
        """
        Build hierarchical tree from flat heading list.

        Converts:
            # Overview
            ## Core Concepts
            ### Concept 1
            ## Applications

        To:
            [
                {
                    'level': 1,
                    'text': 'Overview',
                    'children': [
                        {
                            'level': 2,
                            'text': 'Core Concepts',
                            'children': [
                                {'level': 3, 'text': 'Concept 1', 'children': []}
                            ]
                        },
                        {
                            'level': 2,
                            'text': 'Applications',
                            'children': []
                        }
                    ]
                }
            ]
        """
        if not headings:
            return []

        root = []
        stack = []  # Stack of (heading, children_list)

        for heading in headings:
            heading["children"] = []
            level = heading["level"]

            # Pop stack until we find the parent level
            while stack and stack[-1][0]["level"] >= level:
                stack.pop()

            if not stack:
                # Top level heading
                root.append(heading)
                stack.append((heading, heading["children"]))
            else:
                # Add as child to current parent
                parent_heading, parent_children = stack[-1]
                parent_children.append(heading)
                stack.append((heading, heading["children"]))

        return root

    def get_heading_list(self, headings_tree: list[dict] = None, include_level: bool = False) -> list[str]:
        """
        Flatten heading tree to simple list.

        Args:
            headings_tree: Tree structure (uses self.headings if None)
            include_level: Include indentation based on level

        Returns:
            [
                "Overview",
                "  Core Concepts",
                "    Concept 1",
                "  Applications"
            ]
        """
        if headings_tree is None:
            headings_tree = self.headings

        result = []

        def traverse(nodes, indent=0):
            for node in nodes:
                if include_level:
                    prefix = "  " * indent
                    result.append(f"{prefix}{node['clean_text']}")
                else:
                    result.append(node["clean_text"])

                if node.get("children"):
                    traverse(node["children"], indent + 1)

        traverse(headings_tree)
        return result

    def get_section_headings_only(self, min_level: int = 2, max_level: int = 3) -> list[str]:
        """
        Get only section headings (filter by level).

        Args:
            min_level: Minimum heading level (default 2 = ##)
            max_level: Maximum heading level (default 3 = ###)

        Returns:
            List of heading texts within level range
        """
        result = []

        def traverse(nodes):
            for node in nodes:
                if min_level <= node["level"] <= max_level:
                    result.append(node["clean_text"])

                if node.get("children"):
                    traverse(node["children"])

        traverse(self.headings)
        return result

    def print_structure(self):
        """Print template structure (for debugging)."""
        print("\n📋 Template Structure:")
        print("=" * 60)

        if self.frontmatter:
            print("\n✅ Frontmatter Found:")
            print(f"   - Type: {self.frontmatter.get('type', 'N/A')}")
            print(f"   - Domain: {self.frontmatter.get('domain', 'N/A')}")

        print(f"\n📑 Headings ({len(self._flatten_headings(self.headings))} total):")

        def print_tree(nodes, indent=0):
            for node in nodes:
                prefix = "  " * indent
                emoji = "📘" if node["level"] == 1 else "📄" if node["level"] == 2 else "📝"
                print(f"{prefix}{emoji} {node['text']}")

                if node.get("children"):
                    print_tree(node["children"], indent + 1)

        print_tree(self.headings)
        print("=" * 60)

    def _flatten_headings(self, tree):
        """Flatten tree to count total headings."""
        result = []

        def traverse(nodes):
            for node in nodes:
                result.append(node)
                if node.get("children"):
                    traverse(node["children"])

        traverse(tree)
        return result


def main():
    """Test template parser."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python template_parser.py <template_file>")
        sys.exit(1)

    template_path = Path(sys.argv[1])

    parser = TemplateParser()
    result = parser.parse(template_path)

    # Print structure
    parser.print_structure()

    # Print heading list
    print("\n📝 Flat Heading List:")
    print("-" * 60)
    for heading in parser.get_heading_list(include_level=True):
        print(heading)

    print("\n✅ Section Headings Only (## and ###):")
    print("-" * 60)
    for heading in parser.get_section_headings_only():
        print(f"  - {heading}")


if __name__ == "__main__":
    main()
