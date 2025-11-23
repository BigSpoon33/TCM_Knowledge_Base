from ..core.researcher import ResearchProvider


class SlidesGenerator:
    """Generates presentation slides from root note content using AI."""

    def __init__(self, researcher: ResearchProvider):
        self.researcher = researcher

    def generate_from_content(self, content: str, topic: str, theme: str = "black") -> str:
        """Generates slide deck markdown from the body of a root note."""
        print(f"🎬 Generating slide deck for '{topic}' using AI...")

        prompt = f"""
        Based on the following content about "{topic}", create a professional presentation slide deck using Advanced Slides markdown format.

        REQUIREMENTS:
        1. Use the Advanced Slides format with "---" to separate slides
        2. Create an engaging, visually-structured presentation
        3. Include the following slide types:
           - Title slide with topic name
           - Overview/Learning objectives slide
           - Content slides covering key concepts (use fragments for progressive reveal)
           - Clinical manifestations slide
           - Treatment principles slide
           - Key formulas/points slide (if applicable)
           - Clinical pearls/study tips slide
           - Summary slide with key takeaways
        4. Use markdown formatting: headers, bullet points, tables, bold/italic
        5. Add fragment animations with: <!-- .element: class="fragment" -->
        6. Include speaker notes using: Note: [your note here]
        7. Use visual organization (columns, grids, callouts)
        8. Keep text concise - slides are for showing, not telling
        9. Add clinical pearls and mnemonics where appropriate

        STYLE GUIDELINES:
        - Use emojis sparingly for visual interest (🌿 💊 🎯 ⚠️ 💡)
        - Create 10-15 slides total
        - Each slide should have ONE main idea
        - Use progressive reveal (fragments) for complex information
        - Include practical clinical applications

        ---
        CONTENT:
        {content[:10000]}
        ---

        Generate the complete slide deck now in Advanced Slides markdown format.
        Start with the frontmatter, then create all slides.
        """

        slides_content = self.researcher.generate_content(prompt)

        # Add frontmatter if not present
        if not slides_content.startswith("---"):
            frontmatter = f"""---
theme: {theme}
transition: slide
slideNumber: true
progress: true
controls: true
tags:
  - slides
  - tcm
  - {topic.lower().replace(" ", "-")}
---

"""
            slides_content = frontmatter + slides_content

        return slides_content

    def generate_pattern_slides(self, content: str, pattern_name: str) -> str:
        """Specialized slide generation for TCM patterns."""
        print(f"🎬 Generating TCM pattern slides for '{pattern_name}'...")

        prompt = f"""
        Create a professional TCM pattern presentation for "{pattern_name}" using Advanced Slides format.

        SLIDE STRUCTURE:
        1. Title Slide: Pattern name in English and Chinese (if available)
        2. Overview: Pattern category, key characteristics
        3. Etiology & Pathology: How this pattern develops
        4. Clinical Manifestations: Cardinal symptoms (use fragments)
        5. Tongue & Pulse: Diagnostic indicators with visual descriptions
        6. Differential Diagnosis: Similar patterns to distinguish from
        7. Treatment Principles: Primary and secondary principles
        8. Key Formulas: Main formulas with brief descriptions
        9. Acupuncture Points: Essential points with functions
        10. Clinical Pearls: Practical tips and mnemonics
        11. Case Example: Brief clinical scenario (if content allows)
        12. Summary: Key takeaways and study tips

        FORMATTING:
        - Use "---" to separate slides
        - Use "----" for vertical sub-slides (optional)
        - Add fragments: <!-- .element: class="fragment" -->
        - Include speaker notes: Note: [clinical insight]
        - Use tables for organized information
        - Add emojis for visual interest: 🌿 (herbs), 💊 (formulas), 📍 (points), ⚠️ (cautions)

        ---
        CONTENT:
        {content[:10000]}
        ---

        Generate the complete slide deck now.
        """

        slides_content = self.researcher.generate_content(prompt)

        # Add frontmatter
        if not slides_content.startswith("---"):
            frontmatter = f"""---
theme: sky
transition: slide
slideNumber: true
progress: true
controls: true
tags:
  - slides
  - tcm
  - patterns
  - {pattern_name.lower().replace(" ", "-")}
material_type: presentation
---

"""
            slides_content = frontmatter + slides_content

        return slides_content
