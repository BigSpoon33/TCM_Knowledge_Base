#!/usr/bin/env python3
"""
Generate Guided Conversation - CLI tool for guided learning conversations.
"""

import sys
import argparse
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from conversation_engine import GuidedConversationEngine
from generate_flashcards_from_root import find_root_note, BASE_DIR, MATERIALS_DIR


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Start a guided learning conversation for a TCM pattern.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Start interactive conversation
  python generate_guided_conversation.py "Lung Yin Deficiency"
  
  # Generate conversation script (markdown)
  python generate_guided_conversation.py "Lung Yin Deficiency" --script-only
  
  # Specify custom max attempts
  python generate_guided_conversation.py "Lung Yin Deficiency" --max-attempts 5
        """
    )

    parser.add_argument(
        'pattern',
        help='Name of the TCM pattern (e.g., "Lung Yin Deficiency")'
    )
    parser.add_argument(
        '--script-only',
        action='store_true',
        help='Generate conversation script markdown instead of interactive mode'
    )
    parser.add_argument(
        '--max-attempts',
        type=int,
        default=3,
        help='Maximum attempts per heading before moving on (default: 3)'
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=None,
        help='Output directory for conversation script (default: Materials/TCM_101/)'
    )

    args = parser.parse_args()

    # Find root note
    print(f"🔍 Searching for root note: {args.pattern}")
    root_note_path = find_root_note(args.pattern)

    if not root_note_path:
        # Try searching in Materials directory
        materials_dir = MATERIALS_DIR / "TCM_101"
        pattern_slug = args.pattern.replace(' ', '_')
        possible_paths = [
            materials_dir / f"Root_Note_{pattern_slug}.md",
            materials_dir / f"{pattern_slug}.md",
        ]

        for path in possible_paths:
            if path.exists():
                root_note_path = path
                break

    if not root_note_path:
        print(f"❌ Root note not found for: {args.pattern}")
        print(f"\nSearched in:")
        print(f"  - {BASE_DIR}")
        print(f"  - {materials_dir}")
        print(f"\nMake sure the root note exists and has 'type: root_note' in frontmatter.")
        sys.exit(1)

    print(f"✅ Found root note: {root_note_path}\n")

    # Initialize engine
    try:
        engine = GuidedConversationEngine(
            root_note_path,
            max_attempts=args.max_attempts
        )
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("\nMake sure GEMINI_API_KEY environment variable is set.")
        sys.exit(1)

    # Run conversation
    if args.script_only:
        # Generate markdown script
        print("📝 Generating conversation script...\n")
        script = engine._generate_conversation_script()

        # Save to file
        output_dir = args.output_dir or (MATERIALS_DIR / "TCM_101")
        output_dir.mkdir(parents=True, exist_ok=True)

        topic_slug = engine.state.topic_name.replace(' ', '_')
        output_file = output_dir / f"{topic_slug}_Guided_Conversation.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(script)

        print(f"✅ Conversation script saved to: {output_file}")
    else:
        # Run interactive conversation
        engine.start_conversation(interactive=True)


if __name__ == '__main__':
    main()
