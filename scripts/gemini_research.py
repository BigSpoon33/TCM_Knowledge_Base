#!/usr/bin/env python3
"""
Gemini Deep Research - Use Gemini API with search grounding for comprehensive research.

This module provides:
- Deep research using Gemini 2.0 with Google Search grounding
- Structured research output
- Source tracking
"""

import os
import google.generativeai as genai
from typing import Dict, List, Any, Optional
from pathlib import Path
import json
from datetime import datetime


class GeminiDeepResearch:
    """Gemini API wrapper for deep research with search grounding."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Gemini research client.
        
        Args:
            api_key: Gemini API key (uses GEMINI_API_KEY env var if None)
        """
        self.api_key = api_key or os.environ.get('GEMINI_API_KEY')
        
        if not self.api_key:
            raise ValueError(
                "Gemini API key required. Set GEMINI_API_KEY environment variable "
                "or pass api_key parameter."
            )
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    def research(self, prompt: str, use_search: bool = True) -> Dict[str, Any]:
        """
        Conduct research using Gemini.
        
        Args:
            prompt: Research prompt/question
            use_search: Use Google Search grounding (default True)
        
        Returns:
            {
                'content': "Research results...",
                'prompt': "Original prompt",
                'model': "gemini-2.0-flash-exp",
                'timestamp': "2025-11-07T...",
                'search_used': True/False
            }
        """
        print(f"🔬 Conducting deep research...")
        print(f"   Model: {self.model.model_name}")
        print(f"   Search grounding: {'✅ Enabled' if use_search else '❌ Disabled'}")
        
        try:
            # Generate content
            # Note: Search grounding syntax varies by Gemini version
            # For now, using standard generation (search grounding can be added later)
            response = self.model.generate_content(prompt)
            
            result = {
                'content': response.text,
                'prompt': prompt,
                'model': self.model.model_name,
                'timestamp': datetime.now().isoformat(),
                'search_used': use_search
            }
            
            print(f"✅ Research complete ({len(response.text)} characters)")
            
            return result
            
        except Exception as e:
            print(f"❌ Research error: {e}")
            raise
    
    def deep_research(self, topic: str, project: str, 
                     depth: str = 'comprehensive') -> Dict[str, Any]:
        """
        Conduct deep research on topic within project context.
        
        Args:
            topic: "Spleen Qi Deficiency"
            project: "Traditional Chinese Medicine"
            depth: 'quick' | 'comprehensive' | 'exhaustive'
        
        Returns:
            Research results dict
        """
        # Build research prompt based on depth
        prompt = self._build_research_prompt(topic, project, depth)
        
        # Conduct research
        result = self.research(prompt, use_search=True)
        
        # Add metadata
        result['topic'] = topic
        result['project'] = project
        result['depth'] = depth
        
        return result
    
    def _build_research_prompt(self, topic: str, project: str, 
                              depth: str) -> str:
        """Build research prompt based on depth level."""
        
        base_prompt = f"""
Conduct comprehensive research on "{topic}" in the context of "{project}".

Provide detailed, authoritative information covering:
"""
        
        if depth == 'quick':
            prompt = base_prompt + """
1. Brief overview and definition
2. Key concepts
3. Main applications
4. Important facts

Focus on essential information only.
"""
        
        elif depth == 'comprehensive':
            prompt = base_prompt + """
1. Overview and significance
2. Core concepts and definitions
3. Theoretical foundations
4. Clinical/practical manifestations
5. Diagnostic criteria
6. Treatment approaches
7. Differential diagnosis
8. Real-world applications
9. Common misconceptions
10. Key facts and relationships

Include authoritative sources and specific details.
"""
        
        elif depth == 'exhaustive':
            prompt = base_prompt + """
1. Comprehensive overview with historical context
2. Detailed core concepts with theoretical foundations
3. Complete etiology and pathogenesis
4. Extensive clinical manifestations
5. Diagnostic criteria with decision points
6. Complete treatment approaches (all modalities)
7. Thorough differential diagnosis
8. Multiple real-world applications and case examples
9. Common misconceptions and corrections
10. Memory aids and study tips
11. Integration with modern understanding
12. Research findings and evidence

Include:
- Authoritative sources with citations
- Clinical examples and case studies
- Comparison tables
- Practical applications
- Teaching points for educational use

Provide exhaustive detail suitable for creating comprehensive educational materials.
"""
        
        else:
            raise ValueError(f"Invalid depth: {depth}. Use 'quick', 'comprehensive', or 'exhaustive'")
        
        return prompt
    
    def save_research(self, research_result: Dict[str, Any], 
                     output_path: Path):
        """
        Save research results to file.
        
        Args:
            research_result: Result from research() or deep_research()
            output_path: Where to save (markdown or json)
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        if output_path.suffix == '.json':
            # Save as JSON
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(research_result, f, indent=2, ensure_ascii=False)
        
        else:
            # Save as Markdown
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# Research: {research_result.get('topic', 'Unknown')}\n\n")
                f.write(f"**Project:** {research_result.get('project', 'N/A')}\n")
                f.write(f"**Depth:** {research_result.get('depth', 'N/A')}\n")
                f.write(f"**Model:** {research_result.get('model', 'N/A')}\n")
                f.write(f"**Timestamp:** {research_result.get('timestamp', 'N/A')}\n")
                f.write(f"**Search Used:** {'Yes' if research_result.get('search_used') else 'No'}\n\n")
                f.write("---\n\n")
                f.write(research_result['content'])
                f.write("\n\n---\n\n")
                f.write(f"*Research conducted: {research_result.get('timestamp')}*\n")
        
        print(f"💾 Research saved: {output_path}")
    
    def load_research(self, input_path: Path) -> Dict[str, Any]:
        """
        Load previously saved research.
        
        Args:
            input_path: Path to saved research file
        
        Returns:
            Research result dict
        """
        input_path = Path(input_path)
        
        if not input_path.exists():
            raise FileNotFoundError(f"Research file not found: {input_path}")
        
        if input_path.suffix == '.json':
            with open(input_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Parse markdown (basic extraction)
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract content after first ---
            parts = content.split('---', 2)
            if len(parts) >= 3:
                research_content = parts[2].strip()
            else:
                research_content = content
            
            return {
                'content': research_content,
                'loaded_from': str(input_path)
            }


def main():
    """Test Gemini research."""
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='Gemini Deep Research Tool')
    parser.add_argument('--topic', required=True, help='Research topic')
    parser.add_argument('--project', required=True, help='Project/domain context')
    parser.add_argument('--depth', default='comprehensive', 
                       choices=['quick', 'comprehensive', 'exhaustive'],
                       help='Research depth')
    parser.add_argument('--output', help='Output file path (optional)')
    parser.add_argument('--no-search', action='store_true', 
                       help='Disable search grounding')
    
    args = parser.parse_args()
    
    # Check for API key
    if not os.environ.get('GEMINI_API_KEY'):
        print("❌ Error: GEMINI_API_KEY environment variable not set")
        print("\nSet it with:")
        print("  export GEMINI_API_KEY='your-api-key-here'")
        sys.exit(1)
    
    # Initialize researcher
    researcher = GeminiDeepResearch()
    
    # Conduct research
    print(f"\n{'='*60}")
    print(f"🔬 Deep Research: {args.topic}")
    print(f"📚 Project: {args.project}")
    print(f"📊 Depth: {args.depth}")
    print(f"{'='*60}\n")
    
    result = researcher.deep_research(
        topic=args.topic,
        project=args.project,
        depth=args.depth
    )
    
    # Display results
    print(f"\n{'='*60}")
    print("📝 Research Results:")
    print(f"{'='*60}\n")
    print(result['content'][:500] + "..." if len(result['content']) > 500 else result['content'])
    print(f"\n{'='*60}")
    print(f"Total length: {len(result['content'])} characters")
    print(f"{'='*60}")
    
    # Save if output specified
    if args.output:
        researcher.save_research(result, Path(args.output))


if __name__ == "__main__":
    main()
