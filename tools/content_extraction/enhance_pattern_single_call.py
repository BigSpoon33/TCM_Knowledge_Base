#!/usr/bin/env python3
"""
Enhance Pattern (Single API Call) - Fast pattern enhancement using ONE API call.

This script:
1. Reads an existing pattern file (the stub)
2. Reads the template structure
3. Uses ONE Gemini API call to generate ALL sections at once
4. Preserves original content at the bottom

Usage:
    python enhance_pattern_single_call.py "Spleen Qi Deficiency"
    python enhance_pattern_single_call.py "Liver Qi Stagnation" --output-dir "Enhanced"
"""

import argparse
import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from gemini_research import GeminiDeepResearch


class SingleCallPatternEnhancer:
    """Enhance patterns with a single comprehensive API call."""

    def __init__(self, api_key: str = None):
        """Initialize enhancer."""
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError("Gemini API key required. Set GEMINI_API_KEY environment variable.")

        self.researcher = GeminiDeepResearch(api_key=self.api_key)

    def enhance(self, pattern_name: str, pattern_dir: Path, template_path: Path, output_dir: Path = None) -> Path:
        """
        Enhance a pattern file using ONE API call.

        Args:
            pattern_name: "Spleen Qi Deficiency"
            pattern_dir: Path to TCM_Patterns/Zang Fu Patterns
            template_path: Path to TEMPLATE_Pattern.md
            output_dir: Where to save (defaults to same as pattern_dir)

        Returns:
            Path to enhanced file
        """
        print("\n" + "=" * 70)
        print(f"🚀 FAST PATTERN ENHANCEMENT: {pattern_name}")
        print("=" * 70 + "\n")

        # Find pattern file
        pattern_file = pattern_dir / f"{pattern_name}.md"
        if not pattern_file.exists():
            raise FileNotFoundError(f"Pattern file not found: {pattern_file}")

        # Read original content
        with open(pattern_file, encoding="utf-8") as f:
            original_content = f.read()

        print(f"✅ Loaded original pattern: {pattern_file.name}")
        print(f"   Original size: {len(original_content)} characters\n")

        # Read template
        with open(template_path, encoding="utf-8") as f:
            template_content = f.read()

        print(f"✅ Loaded template: {template_path.name}\n")

        # Build comprehensive prompt
        prompt = self._build_comprehensive_prompt(pattern_name, original_content, template_content)

        print("🤖 Generating comprehensive pattern content...")
        print("   Method: Single API call")
        print("   This should take ~30-60 seconds\n")

        # Make single API call
        result = self.researcher.research(prompt, use_search=False)
        enhanced_content = result["content"].strip()

        print(f"\n✅ Content generated ({len(enhanced_content)} characters)")

        # Add original content section at the bottom
        final_content = (
            enhanced_content
            + f"""

---

## 📦 Original Note Content (For Reference)

> **Note:** The content below is the original note preserved for reference. Please review the enhanced sections above and manually integrate any missing information.

```markdown
{original_content}
```
"""
        )

        # Save enhanced file
        if not output_dir:
            output_dir = pattern_dir

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / f"{pattern_name}.md"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(final_content)

        print(f"\n✅ Enhanced pattern saved: {output_file}")
        print(f"   Final size: {len(final_content)} characters")
        print(f"   Growth: {len(final_content) - len(original_content):,} characters\n")

        print("=" * 70)
        print("✅ ENHANCEMENT COMPLETE (in 1 API call!)")
        print("=" * 70)

        return output_file

    def _build_comprehensive_prompt(self, pattern_name: str, original_content: str, template_content: str) -> str:
        """Build single comprehensive prompt for all sections."""

        prompt = f"""You are a Traditional Chinese Medicine (TCM) expert. I need you to create a comprehensive, detailed pattern note for "{pattern_name}" by filling in the template below.

# ORIGINAL PATTERN NOTE (Your Source Material):

{original_content}

# TEMPLATE TO FILL:

{template_content}

# YOUR TASK:

1. Use the original pattern note above as your BASE information
2. PRESERVE ALL formulas, acupuncture points, symptoms, and specific details from the original note
3. Fill in the template with comprehensive TCM knowledge for each section
4. Expand each section with detailed, scholarly content appropriate for TCM students and practitioners
5. Use proper markdown formatting
6. Include proper wikilinks [[like this]] for related patterns, formulas, herbs, and points
7. Make the content comprehensive but clinically relevant

# SPECIFIC SECTION GUIDELINES:

**Overview**: 2-3 paragraphs explaining the pattern's nature, significance, and general presentation

**Pattern Classification**: Fill in the eight principles clearly (Excess/Deficiency, Hot/Cold, etc.)

**Etiology & Pathogenesis**: 
- Primary Causes: List 4-6 main causes
- Pathomechanisms: Explain HOW the pattern develops (2-3 detailed paragraphs)
- Include development, progression, and common transformations

**Clinical Manifestations**:
- Cardinal symptoms: List the MUST-HAVE diagnostic features
- Complete symptom picture with chief and accompanying symptoms
- Detailed tongue and pulse descriptions

**Diagnostic Criteria**: Organize symptoms into Must Have, Usually Has, May Have

**Differential Diagnosis**: 
- Create a comparison table with 2-3 similar patterns
- Write detailed comparisons explaining key differences

**Treatment Approach**:
- Treatment principles (4-6 principles)
- Representative formulas with explanations (use formulas from original note!)
- Key herbs with dosage/role notes (use herbs/points from original note!)
- Acupuncture points with functions and combinations

**Contraindications & Cautions**: List important safety considerations

**Pattern Variations & Combinations**: Common variations and how this combines with other patterns

**Western Medical Correlates**: List Western diagnoses and explain biomedical perspective

**Classical Sources & Commentary**: Include historical references and traditional understanding

**Clinical Pearls**: Practical tips, common mistakes, treatment modifications, success indicators

**Study Notes & Memory Aids**: Key points, mnemonics, exam questions, clinical decision flowchart

# OUTPUT FORMAT:

Return ONLY the filled template in markdown format, starting with the frontmatter (---). 
Do NOT include any explanations or meta-commentary.
Just return the complete, filled template ready to save as a .md file.

Make this a comprehensive, professional TCM pattern note worthy of a clinical reference text.
"""

        return prompt


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Fast pattern enhancement using single API call",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Enhance a pattern (overwrites original)
  python enhance_pattern_single_call.py "Spleen Qi Deficiency"
  
  # Save to different directory
  python enhance_pattern_single_call.py "Liver Qi Stagnation" --output-dir "Enhanced"
        """,
    )

    parser.add_argument("pattern_name", help='Name of the pattern (e.g., "Spleen Qi Deficiency")')
    parser.add_argument(
        "--pattern-dir", default="TCM_Patterns/Zang Fu Patterns", help="Directory containing pattern files"
    )
    parser.add_argument("--template", default="TCM_Patterns/TEMPLATE_Pattern.md", help="Template file to use")
    parser.add_argument("--output-dir", help="Output directory (defaults to same as pattern-dir)")

    args = parser.parse_args()

    # Check API key
    if not os.environ.get("GEMINI_API_KEY"):
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
        enhancer = SingleCallPatternEnhancer()
        output_file = enhancer.enhance(
            pattern_name=args.pattern_name, pattern_dir=pattern_dir, template_path=template_path, output_dir=output_dir
        )

        print("\n💡 Next steps:")
        print(f"   1. Review enhanced file: {output_file}")
        print("   2. Check that original formulas/points are preserved")
        print("   3. Edit any sections that need refinement\n")

        sys.exit(0)

    except Exception as e:
        print(f"\n❌ Enhancement error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
