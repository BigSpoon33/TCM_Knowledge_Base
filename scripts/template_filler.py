#!/usr/bin/env python3
"""
Template Filler - Assemble complete root note from template and generated sections.

This module:
- Takes template structure and generated content
- Fills template with content
- Preserves frontmatter
- Creates complete root note markdown file
"""

import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from template_parser import TemplateParser


class TemplateFiller:
    """Fill template with generated content to create complete root note."""

    def __init__(self):
        self.template_data = None
        self.sections = {}
        self.filled_content = ""

    def fill(self, template_path: Path, sections: dict[str, str], topic: str, project: str) -> str:
        """
        Fill template with generated sections.

        Args:
            template_path: Path to template file
            sections: {'Overview': 'content...', 'Core Concepts': 'content...'}
            topic: Topic name
            project: Project/domain name

        Returns:
            Complete filled markdown content
        """
        print("\n🔧 Filling template...")
        print(f"   Template: {template_path.name}")
        print(f"   Sections to fill: {len(sections)}")

        # Parse template
        parser = TemplateParser()
        self.template_data = parser.parse(template_path)
        self.sections = sections

        # Build frontmatter
        frontmatter = self._build_frontmatter(topic, project)

        # Build body content
        body = self._build_body(self.template_data["headings"])

        # Combine
        self.filled_content = frontmatter + "\n" + body

        print(f"✅ Template filled ({len(self.filled_content)} characters)")

        return self.filled_content

    def _build_frontmatter(self, topic: str, project: str) -> str:
        """
        Build YAML frontmatter for root note.

        Uses template frontmatter as base, customizes for topic.
        """
        # Start with template frontmatter
        fm = self.template_data.get("frontmatter", {}).copy()

        # Update with topic-specific values
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        today = datetime.now().strftime("%Y-%m-%d")

        fm["id"] = f"root-{timestamp}"
        fm["name"] = topic
        fm["type"] = "root_note"
        fm["domain"] = project
        fm["created"] = today
        fm["updated"] = today

        # Ensure required fields exist
        if "tags" not in fm:
            fm["tags"] = ["root_note", project.replace(" ", "_")]

        # Convert to YAML string
        yaml_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)

        # Replace placeholders in the YAML string
        material_id = f"flashcards_{project.replace(' ', '_').lower()}_{topic.replace(' ', '_').lower()}"
        class_id = project.replace(" ", "_")  # Assuming class_id is derived from project

        yaml_str = yaml_str.replace("{{MATERIAL_ID}}", material_id)
        yaml_str = yaml_str.replace("{{CLASS_ID}}", class_id)
        yaml_str = yaml_str.replace("{{TOPIC_NAME}}", topic)
        yaml_str = yaml_str.replace("{{PROJECT_NAME}}", project)

        return f"---\n{yaml_str}---"

    def _build_body(self, headings: list[dict]) -> str:
        """
        Build body content from headings and generated sections.

        Recursively processes heading tree and inserts generated content.
        """
        body = ""

        def process_heading(heading, indent=0):
            nonlocal body

            # Add heading
            level = heading["level"]
            text = heading["text"]
            clean_text = heading["clean_text"]

            body += f"{'#' * level} {text}\n\n"

            # Add generated content if available
            if clean_text in self.sections:
                content = self.sections[clean_text]
                body += content + "\n\n"
            else:
                # Placeholder if content not generated
                body += f"*[Content for {clean_text} to be added]*\n\n"

            # Add separator
            if level <= 2:
                body += "---\n\n"

            # Process children
            if heading.get("children"):
                for child in heading["children"]:
                    process_heading(child, indent + 1)

        # Process all top-level headings
        for heading in headings:
            process_heading(heading)

        return body

    def save(self, output_path: Path):
        """
        Save filled root note to file.

        Args:
            output_path: Where to save the filled root note
        """
        if not self.filled_content:
            raise ValueError("No content to save. Call fill() first.")

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(self.filled_content)

        print(f"💾 Root note saved: {output_path}")

        return output_path

    def validate(self) -> dict[str, Any]:
        """
        Validate filled root note.

        Returns:
            {
                'valid': True/False,
                'has_frontmatter': True/False,
                'sections_filled': int,
                'sections_missing': [list of missing sections],
                'warnings': [list of warnings]
            }
        """
        warnings = []
        missing_sections = []

        # Check frontmatter
        has_frontmatter = self.filled_content.startswith("---")
        if not has_frontmatter:
            warnings.append("No frontmatter found")

        # Check which sections were filled
        sections_filled = 0
        for heading_text in self.sections.keys():
            if heading_text in self.filled_content:
                sections_filled += 1
            else:
                missing_sections.append(heading_text)

        # Check for placeholders
        if "[Content for" in self.filled_content:
            placeholders = re.findall(r"\[Content for (.+?) to be added\]", self.filled_content)
            if placeholders:
                warnings.append(f"Found {len(placeholders)} placeholder sections")
                missing_sections.extend(placeholders)

        valid = has_frontmatter and len(missing_sections) == 0

        return {
            "valid": valid,
            "has_frontmatter": has_frontmatter,
            "sections_filled": sections_filled,
            "sections_missing": missing_sections,
            "warnings": warnings,
        }


def main():
    """Test template filler."""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Fill template with generated content")
    parser.add_argument("--template", required=True, help="Template file path")
    parser.add_argument("--sections", required=True, help="JSON file with sections")
    parser.add_argument("--topic", required=True, help="Topic name")
    parser.add_argument("--project", required=True, help="Project/domain")
    parser.add_argument("--output", required=True, help="Output file path")

    args = parser.parse_args()

    # Load sections
    with open(args.sections) as f:
        sections = json.load(f)

    # Fill template
    filler = TemplateFiller()

    print(f"\n{'=' * 60}")
    print("🔧 Template Filler")
    print(f"{'=' * 60}\n")

    content = filler.fill(template_path=Path(args.template), sections=sections, topic=args.topic, project=args.project)

    # Validate
    validation = filler.validate()

    print("\n📊 Validation Results:")
    print(f"   Valid: {'✅' if validation['valid'] else '❌'}")
    print(f"   Has frontmatter: {'✅' if validation['has_frontmatter'] else '❌'}")
    print(f"   Sections filled: {validation['sections_filled']}")

    if validation["sections_missing"]:
        print(f"   Missing sections: {len(validation['sections_missing'])}")
        for section in validation["sections_missing"][:5]:
            print(f"      - {section}")

    if validation["warnings"]:
        print("   Warnings:")
        for warning in validation["warnings"]:
            print(f"      ⚠️  {warning}")

    # Save
    output_path = filler.save(Path(args.output))

    print(f"\n✅ Complete root note created: {output_path}")


if __name__ == "__main__":
    main()
