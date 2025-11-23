#!/usr/bin/env python3
"""
Fix malformed YAML frontmatter issues:
- Remove extra brackets like ["item"] → item
- Remove comments like # e.g.
- Clean up broken array syntax
- Fix items that have [[] or "]
"""

import re
from pathlib import Path


def clean_yaml_line(line):
    """Clean a single YAML line of malformed syntax"""
    original = line

    # If it's a list item line
    if line.strip().startswith("-"):
        # Extract the item content
        indent = len(line) - len(line.lstrip())
        item = line.strip()[1:].strip()

        # Remove comments (everything after #)
        if "#" in item:
            item = item.split("#")[0].strip()

        # Fix malformed array syntax like ["item1", "item2"]
        if item.startswith('["') and item.endswith('"]'):
            # Extract items from array
            item = item[2:-2]  # Remove [" and "]
            # Split by ", " to get individual items
            items = [i.strip().strip("\"'") for i in item.split('", "')]
            # Return first item only (we'll handle multiple items separately)
            if items and items[0]:
                return " " * indent + f"- {items[0]}\n", items[1:] if len(items) > 1 else []
            else:
                return None, []

        # Fix items with weird brackets like 'Zang Fu Treatment Pattern"]
        item = item.rstrip('"]').rstrip('"').rstrip("']").rstrip("'")

        # Fix items that start with ["
        if item.startswith('["'):
            item = item[2:].rstrip('"')

        # Fix items like [[[]
        item = re.sub(r"\[\[\[.*?\]\]", "", item)
        item = re.sub(r"\[\[\]", "", item)

        # Clean up any remaining quotes at start/end
        item = item.strip("\"'")

        # If item is now empty or just [], skip it
        if not item or item == "[]" or item == "":
            return None, []

        return " " * indent + f"- {item}\n", []

    # Not a list item, return as is
    return line if line.endswith("\n") else line + "\n", []


def fix_frontmatter(frontmatter_text):
    """Fix all malformed YAML in frontmatter"""
    lines = frontmatter_text.split("\n")
    fixed_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip empty lines and ---
        if not line.strip() or line.strip() == "---":
            fixed_lines.append(line)
            i += 1
            continue

        # Check if it's a key: value line
        if ":" in line and not line.strip().startswith("-"):
            key = line.split(":")[0].strip()
            value = line.split(":", 1)[1].strip() if ":" in line else ""
            indent = len(line) - len(line.lstrip())

            # Remove comments from value
            if "#" in value:
                value = value.split("#")[0].strip()

            # Fix empty arrays
            if value == "" or value == "[]":
                fixed_lines.append(" " * indent + f"{key}: []\n")
            else:
                fixed_lines.append(" " * indent + f"{key}: {value}\n")
            i += 1
            continue

        # It's a list item
        if line.strip().startswith("-"):
            cleaned, extra_items = clean_yaml_line(line)
            if cleaned:
                fixed_lines.append(cleaned)
                # Add extra items that were split from array syntax
                indent = len(line) - len(line.lstrip())
                for extra in extra_items:
                    if extra:
                        fixed_lines.append(" " * indent + f"- {extra}\n")
            i += 1
            continue

        # Default: keep line as is
        fixed_lines.append(line if line.endswith("\n") else line + "\n")
        i += 1

    return "".join(fixed_lines)


def fix_file(filepath):
    """Fix malformed YAML in a file"""
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        if "---" not in content:
            return False

        # Split frontmatter and body
        parts = content.split("---", 2)
        if len(parts) < 3:
            return False

        old_frontmatter = parts[1]
        body = parts[2]

        # Check for malformed syntax indicators
        if not any(x in old_frontmatter for x in ['["', '"]', "# e.g.", "[[]", "[[]]"]):
            return False

        # Fix frontmatter
        new_frontmatter = fix_frontmatter(old_frontmatter)

        # Write back
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"---{new_frontmatter}---{body}")

        print("  ✓ Fixed malformed YAML")
        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    base_dir = Path(__file__).parent.parent / "TCM_Patterns"

    print("=" * 70)
    print("FIXING MALFORMED YAML FRONTMATTER")
    print("=" * 70)
    print()

    # Find all pattern markdown files
    pattern_files = []
    for folder in base_dir.iterdir():
        if folder.is_dir():
            for file in folder.glob("*.md"):
                if (
                    not file.name.startswith("00 ")
                    and "TEMPLATE" not in file.name
                    and "MERGE" not in file.name
                    and "PHASE" not in file.name
                    and "STANDARDIZATION" not in file.name
                    and "QUICK_REFERENCE" not in file.name
                    and "Table" not in file.name
                    and "NEXT_STEPS" not in file.name
                ):
                    pattern_files.append(file)

    print(f"Found {len(pattern_files)} pattern files to check\n")

    fixed_count = 0
    for i, filepath in enumerate(sorted(pattern_files), 1):
        rel_path = filepath.relative_to(base_dir)
        print(f"[{i}/{len(pattern_files)}] {rel_path}")

        if fix_file(filepath):
            fixed_count += 1

    print()
    print("=" * 70)
    print(f"✅ COMPLETE: Fixed {fixed_count} files")
    print("=" * 70)


if __name__ == "__main__":
    main()
