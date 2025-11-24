#!/usr/bin/env python3
"""
Comprehensive frontmatter wikilink fix:
1. Remove single quotes from all wikilinks (including inline arrays)
2. Add wikilinks to western_conditions, formulas, herbs, and points
3. Handle both multi-line and single-line array formats
"""

import re
from pathlib import Path


def fix_frontmatter_comprehensive(content):
    """Fix all wikilink issues in frontmatter"""
    # Split frontmatter and body
    if not content.startswith("---"):
        return content, False

    parts = content.split("\n---\n", 1)
    if len(parts) < 2:
        # Try alternative split
        parts = content.split("---\n", 2)
        if len(parts) < 3:
            return content, False
        frontmatter_text = parts[1]
        body = "---\n" + parts[2]
    else:
        frontmatter_text = parts[0].replace("---\n", "", 1)
        body = "---\n" + parts[1]

    original_frontmatter = frontmatter_text
    changed = False

    # Fix 1: Remove single quotes around wikilinks in inline arrays
    # Pattern: symptoms: ['[[Something]]', '[[Other]]']
    # Also handles: symptoms: ['[[Something]]']
    new_text = re.sub(r"(\w+:\s*\[)'(\[\[[^\]]+\]\])'", r"\1\2", frontmatter_text)
    # Remove single quotes from subsequent items
    new_text = re.sub(r",\s*'(\[\[[^\]]+\]\])'", r", \1", new_text)

    if new_text != frontmatter_text:
        frontmatter_text = new_text
        changed = True

    # Fix 2: Add wikilinks to inline arrays for specific fields
    lines = frontmatter_text.split("\n")
    fixed_lines = []

    for line in lines:
        # Match fields with inline arrays
        match = re.match(r"^(western_conditions|formulas|herbs|points):\s*\[(.*)\]$", line)
        if match:
            field = match.group(1)
            array_content = match.group(2).strip()

            if array_content and array_content != "":
                # Split by comma, handling quoted strings
                items = re.findall(r'"([^"]+)"|([^,]+)', array_content)
                new_items = []

                for quoted, unquoted in items:
                    item = (quoted or unquoted).strip()
                    if not item:
                        continue

                    # Skip if already a wikilink
                    if item.startswith("[[") and item.endswith("]]"):
                        new_items.append(item)
                    else:
                        # Add wikilinks
                        new_items.append(f"[[{item}]]")
                        changed = True

                # Reconstruct line
                if new_items:
                    fixed_lines.append(f"{field}: [{', '.join(new_items)}]")
                else:
                    fixed_lines.append(f"{field}: []")
            else:
                fixed_lines.append(line)
            continue

        # Handle multi-line arrays
        match = re.match(r"^(\s*-\s+)(.+)$", line)
        if match:
            prefix = match.group(1)
            value = match.group(2).strip()

            # Remove quotes if present
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
                changed = True

            fixed_lines.append(f"{prefix}{value}")
            continue

        fixed_lines.append(line)

    frontmatter_text = "\n".join(fixed_lines)

    # Apply single quote removal one more time
    frontmatter_text = re.sub(r"'(\[\[[^\]]+\]\])'", r"\1", frontmatter_text)

    if frontmatter_text != original_frontmatter:
        changed = True

    # Reconstruct content
    new_content = "---\n" + frontmatter_text + "\n" + body

    return new_content, changed


def fix_file(filepath):
    """Fix wikilinks in a file"""
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        new_content, changed = fix_frontmatter_comprehensive(content)

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
    print("COMPREHENSIVE FRONTMATTER WIKILINK FIX")
    print("=" * 70)
    print("1. Removing single quotes from ALL [[wikilinks]]")
    print("2. Adding wikilinks to western_conditions, formulas, herbs, points")
    print("3. Handling inline arrays: ['[[Item]]'] -> [[[Item]]]")
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
