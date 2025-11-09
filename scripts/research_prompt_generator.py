#!/usr/bin/env python3
"""
Research Prompt Generator - AI-powered generation of optimal deep research prompts.

This module uses AI to craft targeted research prompts based on:
- Topic and project context
- Template structure (headings to fill)
- Educational requirements
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from template_parser import TemplateParser
from gemini_research import GeminiDeepResearch


class ResearchPromptGenerator:
    """AI-powered generator for optimal deep research prompts."""
    
    def __init__(self, api_key: str = None):
        """
        Initialize prompt generator.
        
        Args:
            api_key: Gemini API key (uses GEMINI_API_KEY env var if None)
        """
        self.api_key = api_key or os.environ.get('GEMINI_API_KEY')
        
        if not self.api_key:
            raise ValueError(
                "Gemini API key required. Set GEMINI_API_KEY environment variable "
                "or pass api_key parameter."
            )
        
        self.researcher = GeminiDeepResearch(api_key=self.api_key)
    
    def generate_prompt(self, topic: str, project: str, 
                       template_path: Path) -> str:
        """
        Generate optimal research prompt using AI.
        
        Args:
            topic: "Spleen Qi Deficiency"
            project: "Traditional Chinese Medicine"
            template_path: Path to template file
        
        Returns:
            Optimized research prompt string
        """
        print(f"🎯 Generating research prompt...")
        print(f"   Topic: {topic}")
        print(f"   Project: {project}")
        print(f"   Template: {template_path.name}")
        
        # Parse template to extract headings
        parser = TemplateParser()
        template_data = parser.parse(template_path)
        
        # Get heading list
        headings = parser.get_heading_list(include_level=True)
        
        print(f"   Headings extracted: {len(headings)}")
        
        # Build meta-prompt
        meta_prompt = self._build_meta_prompt(topic, project, headings)
        
        # Generate research prompt using AI
        print(f"   🤖 Calling Gemini to generate prompt...")
        result = self.researcher.research(meta_prompt, use_search=False)
        
        research_prompt = result['content'].strip()
        
        print(f"✅ Research prompt generated ({len(research_prompt)} characters)")
        
        return research_prompt
    
    def _build_meta_prompt(self, topic: str, project: str, 
                          headings: List[str]) -> str:
        """
        Build meta-prompt for prompt generation.
        
        This is the "prompt to generate the research prompt".
        """
        headings_formatted = "\n".join(headings)
        
        return f"""
You are an expert research prompt engineer specializing in educational content creation.

CONTEXT:
- Topic: {topic}
- Domain/Project: {project}
- Template Sections to Fill:
{headings_formatted}

TASK:
Create an optimal deep research prompt that will gather comprehensive information 
to fill ALL the template sections listed above.

The research prompt you create should:
1. Clearly state the topic and domain
2. Request information organized by the template sections
3. Specify what details are needed for each major section
4. Ask for authoritative sources and citations
5. Request clinical examples, comparisons, and practical applications
6. Request information suitable for creating:
   - Educational flashcards (testable facts)
   - Quiz questions (with plausible distractors)
   - Study materials (comprehensive explanations)
   - Clinical scenarios (real-world applications)

REQUIREMENTS FOR THE RESEARCH PROMPT:
- Be comprehensive but focused on the template structure
- Target educational use (for students/learners)
- Request specific details relevant to the domain (e.g., for TCM: tongue, pulse, formulas, points)
- Ask for differential diagnosis information
- Request common misconceptions and corrections
- Ask for memory aids and mnemonics
- Request comparison tables where applicable

OUTPUT FORMAT:
Return ONLY the research prompt text itself.
Do NOT include any meta-commentary, explanations, or formatting markers.
The prompt should be ready to use directly with a research API.

EXAMPLE STRUCTURE (adapt to the specific topic and template):
"Conduct comprehensive research on [topic] in the context of [domain].

Provide detailed, authoritative information organized as follows:

1. [Section 1 from template]: [specific details needed]
2. [Section 2 from template]: [specific details needed]
...

Include:
- Authoritative sources with citations
- Clinical examples and case studies
- Comparison tables with similar concepts
- Practical applications and treatment approaches
- Common misconceptions and corrections
- Memory aids, mnemonics, or analogies
- Information suitable for flashcards and quiz questions

Focus on information that would be valuable for creating comprehensive educational materials."

Now create the optimal research prompt for the given topic, domain, and template structure.
Output ONLY the research prompt text:
"""
    
    def save_prompt(self, prompt: str, output_path: Path, 
                   topic: str = None, project: str = None):
        """
        Save generated prompt to file.
        
        Args:
            prompt: Generated research prompt
            output_path: Where to save
            topic: Optional topic for metadata
            project: Optional project for metadata
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# Generated Deep Research Prompt\n\n")
            
            if topic:
                f.write(f"**Topic:** {topic}\n")
            if project:
                f.write(f"**Project:** {project}\n")
            
            f.write(f"**Generated:** {datetime.now().isoformat()}\n\n")
            f.write(f"---\n\n")
            f.write(prompt)
            f.write(f"\n\n---\n\n")
            f.write(f"*Generated by ResearchPromptGenerator*\n")
        
        print(f"💾 Prompt saved: {output_path}")
    
    def load_prompt(self, input_path: Path) -> str:
        """
        Load previously generated prompt.
        
        Args:
            input_path: Path to saved prompt file
        
        Returns:
            Prompt text
        """
        input_path = Path(input_path)
        
        if not input_path.exists():
            raise FileNotFoundError(f"Prompt file not found: {input_path}")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract prompt between --- markers
        parts = content.split('---')
        if len(parts) >= 3:
            prompt = parts[1].strip()
        else:
            # Fallback: use entire content
            prompt = content
        
        return prompt


def main():
    """Test research prompt generator."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate optimal deep research prompts using AI'
    )
    parser.add_argument('--topic', required=True, help='Research topic')
    parser.add_argument('--project', required=True, help='Project/domain context')
    parser.add_argument('--template', required=True, help='Template file path')
    parser.add_argument('--output', help='Output file path (optional)')
    
    args = parser.parse_args()
    
    # Check for API key
    if not os.environ.get('GEMINI_API_KEY'):
        print("❌ Error: GEMINI_API_KEY environment variable not set")
        print("\nSet it with:")
        print("  export GEMINI_API_KEY='your-api-key-here'")
        sys.exit(1)
    
    # Initialize generator
    generator = ResearchPromptGenerator()
    
    # Generate prompt
    print(f"\n{'='*70}")
    print(f"🎯 AI-Powered Research Prompt Generation")
    print(f"{'='*70}\n")
    
    research_prompt = generator.generate_prompt(
        topic=args.topic,
        project=args.project,
        template_path=Path(args.template)
    )
    
    # Display result
    print(f"\n{'='*70}")
    print("📝 Generated Research Prompt:")
    print(f"{'='*70}\n")
    print(research_prompt)
    print(f"\n{'='*70}")
    
    # Save if output specified
    if args.output:
        generator.save_prompt(
            prompt=research_prompt,
            output_path=Path(args.output),
            topic=args.topic,
            project=args.project
        )
        print(f"\n💡 Use this prompt with:")
        print(f"   python scripts/gemini_research.py \\")
        print(f"     --topic \"{args.topic}\" \\")
        print(f"     --project \"{args.project}\" \\")
        print(f"     --output research_results.md")


if __name__ == "__main__":
    main()
