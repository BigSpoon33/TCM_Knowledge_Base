#!/usr/bin/env python3
"""
Enhance Pattern - Take existing pattern stub and enhance it with comprehensive content.

This script:
1. Reads an existing pattern file (the stub)
2. Parses the template structure
3. Uses Gemini to generate content for each heading
4. Combines into comprehensive pattern file
5. Preserves original content at the bottom

Usage:
    python enhance_pattern.py "Spleen Qi Deficiency"
    python enhance_pattern.py "Liver Qi Stagnation" --output-dir "TCM_Patterns/Enhanced"
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from template_parser import TemplateParser
from content_generator import ContentGenerator
from template_filler import TemplateFiller


class PatternEnhancer:
    """Enhance existing pattern files with comprehensive content."""
    
    def __init__(self, api_key: str = None):
        """Initialize enhancer."""
        self.api_key = api_key or os.environ.get('GEMINI_API_KEY')
        
        if not self.api_key:
            raise ValueError(
                "Gemini API key required. Set GEMINI_API_KEY environment variable."
            )
        
        self.parser = TemplateParser()
        self.generator = ContentGenerator(api_key=self.api_key)
        self.filler = TemplateFiller()
    
    def enhance(self, pattern_name: str, pattern_dir: Path, 
                template_path: Path, output_dir: Path = None) -> Path:
        """
        Enhance a pattern file.
        
        Args:
            pattern_name: "Spleen Qi Deficiency"
            pattern_dir: Path to TCM_Patterns/Zang Fu Patterns
            template_path: Path to TEMPLATE_Pattern.md
            output_dir: Where to save (defaults to same as pattern_dir)
        
        Returns:
            Path to enhanced file
        """
        print("\n" + "="*70)
        print(f"🔧 ENHANCING PATTERN: {pattern_name}")
        print("="*70 + "\n")
        
        # Find pattern file
        pattern_file = pattern_dir / f"{pattern_name}.md"
        if not pattern_file.exists():
            raise FileNotFoundError(f"Pattern file not found: {pattern_file}")
        
        # Read original content
        with open(pattern_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        print(f"✅ Loaded original pattern: {pattern_file.name}")
        print(f"   Original size: {len(original_content)} characters\n")
        
        # Parse template
        print("📋 Parsing template...")
        template_data = self.parser.parse(template_path)
        headings = self.parser._flatten_headings(template_data['headings'])
        print(f"✅ Template parsed: {len(headings)} headings\n")
        
        # Use original content as "research context"
        context = f"""
# Original Pattern Note: {pattern_name}

{original_content}

Use the above original note as the base information. Expand and enhance each section 
with comprehensive TCM knowledge while preserving all the original formulas, 
acupuncture points, and symptoms mentioned.
"""
        
        # Generate content for each heading
        print(f"✍️  Generating content for {len(headings)} sections...")
        print("-" * 70)
        
        sections = self.generator.generate_all_sections(
            headings=template_data['headings'],
            topic=pattern_name,
            project="Traditional Chinese Medicine",
            context=context
        )
        
        print(f"\n✅ All sections generated\n")
        
        # Fill template
        print("🔧 Filling template...")
        enhanced_content = self.filler.fill(
            template_path=template_path,
            sections=sections,
            topic=pattern_name,
            project="Traditional Chinese Medicine"
        )
        
        # Add original content section at the bottom
        enhanced_content += f"""

---

## 📦 Original Note Content (For Reference)

> **Note:** The content below is the original note preserved for reference. Please review the enhanced sections above and manually integrate any missing information.

```markdown
{original_content}
```
"""
        
        # Save enhanced file
        if not output_dir:
            output_dir = pattern_dir
        
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / f"{pattern_name}.md"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(enhanced_content)
        
        print(f"✅ Enhanced pattern saved: {output_file}")
        print(f"   Enhanced size: {len(enhanced_content)} characters")
        print(f"   Growth: {len(enhanced_content) - len(original_content):,} characters\n")
        
        print("="*70)
        print("✅ ENHANCEMENT COMPLETE")
        print("="*70)
        
        return output_file


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Enhance existing pattern files with comprehensive content',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Enhance a pattern (overwrites original)
  python enhance_pattern.py "Spleen Qi Deficiency"
  
  # Save to different directory
  python enhance_pattern.py "Liver Qi Stagnation" --output-dir "Enhanced"
  
  # Use custom template
  python enhance_pattern.py "Heart Qi Deficiency" --template "Custom_Template.md"
        """
    )
    
    parser.add_argument(
        'pattern_name',
        help='Name of the pattern (e.g., "Spleen Qi Deficiency")'
    )
    parser.add_argument(
        '--pattern-dir',
        default='TCM_Patterns/Zang Fu Patterns',
        help='Directory containing pattern files'
    )
    parser.add_argument(
        '--template',
        default='TCM_Patterns/TEMPLATE_Pattern.md',
        help='Template file to use'
    )
    parser.add_argument(
        '--output-dir',
        help='Output directory (defaults to same as pattern-dir)'
    )
    
    args = parser.parse_args()
    
    # Check API key
    if not os.environ.get('GEMINI_API_KEY'):
        print("❌ Error: GEMINI_API_KEY environment variable not set")
        print("\nSet it with:")
        print("  export GEMINI_API_KEY='your-api-key-here'")
        sys.exit(1)
    
    # Get base directory
    base_dir = Path(__file__).parent.parent
    pattern_dir = base_dir / args.pattern_dir
    template_path = base_dir / args.template
    output_dir = base_dir / args.output_dir if args.output_dir else None
    
    # Validate inputs
    if not pattern_dir.exists():
        print(f"❌ Error: Pattern directory not found: {pattern_dir}")
        sys.exit(1)
    
    if not template_path.exists():
        print(f"❌ Error: Template file not found: {template_path}")
        sys.exit(1)
    
    # Run enhancer
    try:
        enhancer = PatternEnhancer()
        output_file = enhancer.enhance(
            pattern_name=args.pattern_name,
            pattern_dir=pattern_dir,
            template_path=template_path,
            output_dir=output_dir
        )
        
        print(f"\n💡 Next steps:")
        print(f"   1. Review enhanced file: {output_file}")
        print(f"   2. Check that original formulas/points are preserved")
        print(f"   3. Integrate any manual edits from original\n")
        
        sys.exit(0)
        
    except Exception as e:
        print(f"\n❌ Enhancement error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
