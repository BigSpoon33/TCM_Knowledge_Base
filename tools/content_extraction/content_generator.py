#!/usr/bin/env python3
"""
Content Generator - Generate content for each template heading using research context.

This module generates section content by:
- Taking heading + topic + project + research context
- Using Gemini to generate focused content for that section
- Tracking progress across all sections
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from gemini_research import GeminiDeepResearch


class ContentGenerator:
    """Generate content for template sections using AI."""

    def __init__(self, api_key: str = None):
        """
        Initialize content generator.

        Args:
            api_key: Gemini API key (uses GEMINI_API_KEY env var if None)
        """
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "Gemini API key required. Set GEMINI_API_KEY environment variable or pass api_key parameter."
            )

        self.researcher = GeminiDeepResearch(api_key=self.api_key)
        self.generated_sections = {}

    def generate_section(self, heading: dict[str, Any], topic: str, project: str, context: str) -> str:
        """
        Generate content for one section.

        Args:
            heading: {
                'level': 2,
                'text': 'Core Concepts',
                'clean_text': 'Core Concepts',
                ...
            }
            topic: "Spleen Qi Deficiency"
            project: "Traditional Chinese Medicine"
            context: "Research context from deep research..."

        Returns:
            Generated markdown content for this section
        """
        heading_text = heading.get("clean_text", heading.get("text", ""))
        level = heading.get("level", 2)

        print(f"   {'  ' * (level - 1)}✍️  Generating: {heading_text}")

        # Build section generation prompt
        prompt = self._build_section_prompt(
            heading_text=heading_text, level=level, topic=topic, project=project, context=context
        )

        # Generate content
        result = self.researcher.research(prompt, use_search=False)
        content = result["content"].strip()

        # Store generated section
        self.generated_sections[heading_text] = content

        print(f"   {'  ' * (level - 1)}✅ Generated ({len(content)} chars)")

        return content

    def generate_all_sections(self, headings: list[dict], topic: str, project: str, context: str) -> dict[str, str]:
        """
        Generate content for all sections.

        Args:
            headings: List of heading dicts from template parser
            topic: Research topic
            project: Project/domain
            context: Research context

        Returns:
            {
                'Overview': 'content...',
                'Core Concepts': 'content...',
                ...
            }
        """
        print(f"\n📝 Generating content for {len(headings)} sections...")
        print(f"   Topic: {topic}")
        print(f"   Project: {project}")
        print(f"   Context length: {len(context)} characters\n")

        sections = {}

        def process_heading(heading, indent=0):
            """Recursively process headings and children."""
            # Generate content for this heading
            content = self.generate_section(heading, topic, project, context)
            sections[heading["clean_text"]] = content

            # Process children
            if heading.get("children"):
                for child in heading["children"]:
                    process_heading(child, indent + 1)

        # Process all top-level headings
        for heading in headings:
            process_heading(heading)

        print(f"\n✅ Generated {len(sections)} sections")

        return sections

    def _build_section_prompt(self, heading_text: str, level: int, topic: str, project: str, context: str) -> str:
        """
        Build prompt for generating section content.

        This is the key prompt that generates content for each heading.
        """
        # Determine section type based on heading
        section_guidance = self._get_section_guidance(heading_text)

        prompt = f"""
Write comprehensive content for the section "{heading_text}" about "{topic}" 
as it relates to "{project}".

Use this research context:
{context[:4000]}  # Limit context to avoid token limits

SECTION REQUIREMENTS:
{section_guidance}

GENERAL REQUIREMENTS:
- Write in clear, educational language
- Be comprehensive but concise
- Use markdown formatting (lists, bold, tables where appropriate)
- Include specific examples and details
- Focus on information valuable for learning
- Do NOT include the heading itself (it will be added separately)
- Do NOT add meta-commentary or explanations about what you're doing

OUTPUT FORMAT:
Return ONLY the section content in markdown format.
Start directly with the content (no heading, no preamble).

Generate the content now:
"""

        return prompt

    def _get_section_guidance(self, heading_text: str) -> str:
        """
        Get specific guidance for different section types.

        This customizes the prompt based on what section we're generating.
        """
        heading_lower = heading_text.lower()

        # Overview sections
        if "overview" in heading_lower or "introduction" in heading_lower:
            return """
- Provide a clear, concise overview (2-3 paragraphs)
- Explain what this topic is and why it matters
- Give context and significance
- Set the stage for detailed sections to follow
"""

        # Core concepts
        elif "core concept" in heading_lower or "key concept" in heading_lower:
            return """
- Define each core concept clearly
- Explain why each concept is important
- Use this format for each concept:
  ### Concept Name
  **Definition:** [clear definition]
  **Importance:** [why it matters]
  **Key Characteristics:** [bullet list]
"""

        # Clinical manifestations / symptoms
        elif "clinical" in heading_lower or "manifestation" in heading_lower or "symptom" in heading_lower:
            return """
- List cardinal/essential symptoms
- Describe tongue presentation (if applicable)
- Describe pulse presentation (if applicable)
- Include accompanying symptoms
- Use bullet lists for clarity
"""

        # Etiology / causes
        elif "etiolog" in heading_lower or "cause" in heading_lower or "pathogen" in heading_lower:
            return """
- List primary causes
- Explain pathomechanisms (how it develops)
- Describe disease progression
- Include common transformations
"""

        # Differential diagnosis
        elif "differential" in heading_lower or "vs" in heading_lower or "comparison" in heading_lower:
            return """
- Compare with similar conditions/patterns
- Use comparison tables where helpful
- Highlight key distinguishing features
- Provide decision points for diagnosis
"""

        # Treatment
        elif "treatment" in heading_lower or "therapy" in heading_lower:
            return """
- State treatment principles
- List primary formulas/interventions (with brief explanations)
- Include key herbs/medications
- Mention acupuncture points (if applicable)
- Provide practical treatment guidance
"""

        # Applications / examples
        elif "application" in heading_lower or "example" in heading_lower or "scenario" in heading_lower:
            return """
- Provide real-world examples
- Include clinical scenarios
- Show practical application
- Use concrete, specific cases
"""

        # Study aids / memory
        elif "study" in heading_lower or "memory" in heading_lower or "mnemonic" in heading_lower:
            return """
- Provide mnemonics or memory devices
- Include analogies if helpful
- Suggest study strategies
- Create memorable associations
"""

        # Summary
        elif "summary" in heading_lower or "key takeaway" in heading_lower:
            return """
- Summarize key points (bullet list)
- Highlight essential facts to remember
- Include common exam questions
- Keep concise and focused
"""

        # Default guidance
        else:
            return """
- Provide comprehensive information for this section
- Use appropriate formatting (lists, tables, etc.)
- Include specific details and examples
- Focus on educational value
"""

    def save_sections(self, output_path: Path):
        """
        Save generated sections to file (for debugging/review).

        Args:
            output_path: Where to save sections
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("# Generated Sections\n\n")
            f.write(f"**Generated:** {datetime.now().isoformat()}\n")
            f.write(f"**Total Sections:** {len(self.generated_sections)}\n\n")
            f.write("---\n\n")

            for heading, content in self.generated_sections.items():
                f.write(f"## {heading}\n\n")
                f.write(content)
                f.write("\n\n---\n\n")

        print(f"💾 Sections saved: {output_path}")


def main():
    """Test content generator."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate content for template sections")
    parser.add_argument("--topic", required=True, help="Topic")
    parser.add_argument("--project", required=True, help="Project/domain")
    parser.add_argument("--heading", required=True, help="Heading text")
    parser.add_argument("--context-file", required=True, help="File with research context")
    parser.add_argument("--output", help="Output file (optional)")

    args = parser.parse_args()

    # Check for API key
    if not os.environ.get("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY environment variable not set")
        sys.exit(1)

    # Load context
    with open(args.context_file) as f:
        context = f.read()

    # Initialize generator
    generator = ContentGenerator()

    # Generate section
    heading = {"level": 2, "text": args.heading, "clean_text": args.heading}

    print(f"\n{'=' * 60}")
    print("📝 Generating Section Content")
    print(f"{'=' * 60}\n")

    content = generator.generate_section(heading=heading, topic=args.topic, project=args.project, context=context)

    # Display result
    print(f"\n{'=' * 60}")
    print("Generated Content:")
    print(f"{'=' * 60}\n")
    print(content)

    # Save if output specified
    if args.output:
        with open(args.output, "w") as f:
            f.write(f"## {args.heading}\n\n")
            f.write(content)
        print(f"\n💾 Saved to: {args.output}")


if __name__ == "__main__":
    main()
