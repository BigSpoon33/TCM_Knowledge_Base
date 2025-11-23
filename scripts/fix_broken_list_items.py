#!/usr/bin/env python3
"""
Fix broken multi-line list items in frontmatter (especially nutrition field)
Example issue:
  nutrition:
  - Iron-rich foods (red meat
  - liver
  - spinach)

Should be:
  nutrition:
  - Iron-rich foods (red meat, liver, spinach)
"""

import re
from pathlib import Path


def fix_broken_lists(frontmatter):
    """Fix broken list items in frontmatter"""
    lines = frontmatter.split("\n")
    fixed_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is a list item that looks incomplete (ends with open paren or comma)
        if line.strip().startswith("-") and i + 1 < len(lines):
            current_item = line.strip()[1:].strip()

            # Look ahead to see if next items should be merged
            merged_items = [current_item]
            j = i + 1

            # Check if item has unmatched parenthesis or ends with comma
            has_open_paren = current_item.count("(") > current_item.count(")")

            if has_open_paren:
                # Merge continuation lines until we find the closing paren
                while j < len(lines):
                    next_line = lines[j].strip()

                    # If it's another list item starting with -, it's a continuation
                    if next_line.startswith("-"):
                        next_item = next_line[1:].strip()
                        merged_items.append(next_item)
                        j += 1

                        # Check if we found the closing paren
                        combined = ", ".join(merged_items)
                        if combined.count("(") == combined.count(")"):
                            break
                    else:
                        break

                # Create the merged line
                indent = len(line) - len(line.lstrip())
                merged = ", ".join(merged_items)
                fixed_lines.append(" " * indent + f"- {merged}")
                i = j
            else:
                fixed_lines.append(line)
                i += 1
        else:
            fixed_lines.append(line)
            i += 1

    return "\n".join(fixed_lines)


def fix_file(filepath):
    """Fix broken lists in a file"""
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

        # Check if has broken list items
        if not re.search(r"- [^\n]+\([^\)]+\n- ", old_frontmatter):
            return False

        # Fix broken lists
        new_frontmatter = fix_broken_lists(old_frontmatter)

        # Write back
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"---{new_frontmatter}---{body}")

        print("  ✓ Fixed broken list items")
        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    base_dir = Path(__file__).parent.parent / "TCM_Patterns"

    print("=" * 70)
    print("FIXING BROKEN MULTI-LINE LIST ITEMS IN FRONTMATTER")
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
