#!/usr/bin/env python3
"""
Generate Slides with AI - Uses Gemini to create presentation slides from a root note.
"""

import os
import re
from typing import Dict, List, Any
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from gemini_research import GeminiDeepResearch

class SlidesGeneratorAI:
    """Generates presentation slides from root note content using AI."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set.")
        self.researcher = GeminiDeepResearch(api_key=self.api_key)

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

        result = self.researcher.research(prompt, use_search=False)
        slides_content = result['content']
        
        # Add frontmatter if not present
        if not slides_content.startswith('---'):
            frontmatter = f"""---
theme: {theme}
transition: slide
slideNumber: true
progress: true
controls: true
tags:
  - slides
  - tcm
  - {topic.lower().replace(' ', '-')}
---

"""
            slides_content = frontmatter + slides_content
        
        print(f"✅ Generated slide deck with multiple slides.")
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

        result = self.researcher.research(prompt, use_search=False)
        slides_content = result['content']
        
        # Add frontmatter
        if not slides_content.startswith('---'):
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
  - {pattern_name.lower().replace(' ', '-')}
material_type: presentation
---

"""
            slides_content = frontmatter + slides_content
        
        print(f"✅ Generated TCM pattern slide deck.")
        return slides_content

if __name__ == '__main__':
    # Test with sample content
    test_content = """
    # Spleen Qi Deficiency
    
    ## Overview
    Spleen Qi Deficiency is one of the most common patterns in TCM, characterized by impaired transformation and transportation functions of the Spleen.
    
    ## Clinical Manifestations
    - **Cardinal Symptoms:** Fatigue, poor appetite, loose stools, abdominal distention
    - **Secondary Symptoms:** Pale complexion, weak limbs, tendency to bruise easily
    - **Tongue:** Pale, swollen, with teeth marks, thin white coating
    - **Pulse:** Weak (ruo) or empty (xu)
    
    ## Etiology
    - Irregular eating habits
    - Excessive mental work
    - Chronic illness
    - Constitutional weakness
    
    ## Treatment Principles
    - **Primary Principle:** Tonify Spleen Qi
    - **Secondary Principle:** Strengthen digestive function
    
    ## Key Formulas
    - **Si Jun Zi Tang (Four Gentlemen Decoction):** Primary formula for Spleen Qi Deficiency
    - **Bu Zhong Yi Qi Tang:** For Spleen Qi sinking
    
    ## Acupuncture Points
    - **ST-36 (Zu San Li):** Tonifies Spleen and Stomach Qi
    - **SP-6 (San Yin Jiao):** Strengthens Spleen
    - **CV-12 (Zhong Wan):** Front-Mu point of Stomach
    """
    
    generator = SlidesGeneratorAI()
    slides = generator.generate_pattern_slides(test_content, "Spleen Qi Deficiency")
    
    print("\n" + "="*70)
    print("GENERATED SLIDES:")
    print("="*70)
    print(slides[:1000] + "\n...\n")
