#!/usr/bin/env python3
"""
Fix frontmatter wikilinks:
1. Remove single quotes around [[wikilinks]]
2. Add wikilinks to western_conditions, formulas, herbs, and points
"""

import re
from pathlib import Path


def fix_frontmatter_wikilinks(content):
    """Fix wikilinks in frontmatter"""
    # Split frontmatter and body
    parts = content.split("---\n", 2)
    if len(parts) < 3:
        return content, False

    frontmatter_text = parts[1]
    body = parts[2]

    original_frontmatter = frontmatter_text
    changed = False

    # Fix 1: Remove single quotes around [[wikilinks]]
    # Pattern: '[[Something]]' -> [[Something]]
    frontmatter_text = re.sub(r"'(\[\[[^\]]+\]\])'", r"\1", frontmatter_text)

    # Fix 2: Add wikilinks to list items that don't have them
    lines = frontmatter_text.split("\n")
    fixed_lines = []
    current_field = None
    in_array = False

    for line in lines:
        # Detect which field we're in
        if re.match(r"^(western_conditions|formulas|herbs|points):", line):
            field_match = re.match(r"^(western_conditions|formulas|herbs|points):", line)
            current_field = field_match.group(1)
            in_array = True
            fixed_lines.append(line)
            continue

        # Check if we've left the array (new field or dedented line)
        if in_array and line and not line.startswith("-") and not line.startswith(" "):
            in_array = False
            current_field = None

        # Process array items in relevant fields
        if in_array and current_field in ["western_conditions", "formulas", "herbs", "points"]:
            # Match list items: - Something or - [[Something]]
            item_match = re.match(r"^(\s*-\s+)(.+)$", line)
            if item_match:
                prefix = item_match.group(1)
                value = item_match.group(2).strip()

                # Skip if already a wikilink
                if value.startswith("[[") and value.endswith("]]"):
                    fixed_lines.append(line)
                    continue

                # Skip if it's a single quote wikilink (will be fixed by pattern above)
                if value.startswith("'[[") and value.endswith("]]'"):
                    fixed_lines.append(line)
                    continue

                # Skip empty values or special markers
                if not value or value == "[]":
                    fixed_lines.append(line)
                    continue

                # Add wikilinks
                new_line = f"{prefix}[[{value}]]"
                if new_line != line:
                    changed = True
                fixed_lines.append(new_line)
                continue

        fixed_lines.append(line)

    frontmatter_text = "\n".join(fixed_lines)

    # Check if anything changed
    if frontmatter_text != original_frontmatter:
        changed = True
        # Apply the single quote removal again after reconstruction
        frontmatter_text = re.sub(r"'(\[\[[^\]]+\]\])'", r"\1", frontmatter_text)

    # Reconstruct content
    new_content = "---\n" + frontmatter_text + "---\n" + body

    return new_content, changed


def fix_file(filepath):
    """Fix wikilinks in a file"""
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        new_content, changed = fix_frontmatter_wikilinks(content)

        if changed:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True

        return False

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    base_dir = Path(__file__).parent.parent / "TCM_Patterns"

    print("=" * 70)
    print("FIXING FRONTMATTER WIKILINKS")
    print("=" * 70)
    print("1. Removing single quotes from [[wikilinks]]")
    print("2. Adding wikilinks to western_conditions, formulas, herbs, points")
    print()

    # Find all pattern files
    pattern_files = []
    for folder in base_dir.iterdir():
        if folder.is_dir():
            for file in folder.glob("*.md"):
                if (
                    not file.name.startswith("00 ")
                    and "TEMPLATE" not in file.name
                    and "EXAMPLE" not in file.name
                    and "MERGE" not in file.name
                    and "PHASE" not in file.name
                    and "STANDARDIZATION" not in file.name
                    and "QUICK_REFERENCE" not in file.name
                    and "Table" not in file.name
                    and "NEXT_STEPS" not in file.name
                    and "Comparison" not in file.name
                    and "Treatment" not in file.name
                    and "COMPLETE" not in file.name
                    and "SUMMARY" not in file.name
                    and "PROGRESS" not in file.name
                    and "Patterns.md" not in file.name
                ):
                    pattern_files.append(file)

    print(f"Found {len(pattern_files)} pattern files to process\n")

    fixed_count = 0
    for i, filepath in enumerate(sorted(pattern_files), 1):
        rel_path = filepath.relative_to(base_dir)

        if fix_file(filepath):
            print(f"[{i}/{len(pattern_files)}] {rel_path} - ✓ Fixed")
            fixed_count += 1

    print()
    print("=" * 70)
    print(f"✅ COMPLETE: Fixed {fixed_count}/{len(pattern_files)} files")
    print("=" * 70)


if __name__ == "__main__":
    main()
