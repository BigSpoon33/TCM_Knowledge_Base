#!/usr/bin/env python3
"""
Fix corrupted frontmatter from bad YAML parsing:
1. Fix ---id: → ---\nid:
2. Remove lines with just "[]" after a key
3. Remove broken [, [[, [[[, etc.
4. Ensure proper list formatting
"""

import re
from pathlib import Path


def fix_corrupted_frontmatter(content):
    """Fix corrupted YAML frontmatter"""

    # Fix missing newline after opening ---
    content = re.sub(r"^---(\w)", r"---\n\1", content, flags=re.MULTILINE)

    lines = content.split("\n")
    fixed_lines = []
    in_frontmatter = False
    frontmatter_lines = []
    body_lines = []
    found_closing = False

    for i, line in enumerate(lines):
        if line.strip() == "---":
            if not in_frontmatter:
                # Opening ---
                in_frontmatter = True
                frontmatter_lines.append(line)
            else:
                # Closing ---
                in_frontmatter = False
                found_closing = True
                # Process frontmatter before adding closing
                fixed_fm = process_frontmatter_lines(frontmatter_lines[1:])  # Skip opening ---
                fixed_lines = ["---"] + fixed_fm + ["", "---"]
                continue
        elif in_frontmatter:
            frontmatter_lines.append(line)
        else:
            body_lines.append(line)

    # Combine fixed frontmatter and body
    return "\n".join(fixed_lines) + "\n" + "\n".join(body_lines)


def process_frontmatter_lines(fm_lines):
    """Process and clean frontmatter lines"""
    cleaned = []
    i = 0

    while i < len(fm_lines):
        line = fm_lines[i]

        # Skip empty lines
        if not line.strip():
            i += 1
            continue

        # Check if it's a key: value line
        if ":" in line and not line.strip().startswith("-"):
            parts = line.split(":", 1)
            key = parts[0].strip()
            value = parts[1].strip() if len(parts) > 1 else ""
            indent = len(line) - len(line.lstrip())

            # Check if next line is just "[]" - if so, this should be key: []
            if i + 1 < len(fm_lines) and fm_lines[i + 1].strip().startswith("- ["):
                # Next line has broken array, skip it
                cleaned.append(" " * indent + f"{key}: []")
                i += 2
                continue

            # Normal key: value
            if value == "[]" or value == "":
                # Check if following lines are list items for this key
                has_list_items = False
                if i + 1 < len(fm_lines) and fm_lines[i + 1].strip().startswith("-"):
                    next_line = fm_lines[i + 1]
                    # Check if it's not a broken array marker
                    if next_line.strip() not in ["- [", "- [[", "- [[[", "- []"]:
                        has_list_items = True

                if has_list_items:
                    cleaned.append(" " * indent + f"{key}:")
                else:
                    cleaned.append(" " * indent + f"{key}: []")
            else:
                cleaned.append(" " * indent + f"{key}: {value}")
            i += 1
            continue

        # It's a list item
        if line.strip().startswith("-"):
            item = line.strip()[1:].strip()
            indent = len(line) - len(line.lstrip())

            # Skip broken array markers
            if item in ["[", "[[", "[[[", "[]", ""]:
                i += 1
                continue

            # Clean up the item
            cleaned.append(" " * indent + f"- {item}")
            i += 1
            continue

        # Unknown format, keep as is
        cleaned.append(line)
        i += 1

    return cleaned


def fix_file(filepath):
    """Fix corrupted frontmatter in a file"""
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        # Check for corruption markers
        if not any(x in content for x in ["---id:", "- [[[", "[]:", "tags: []"]):
            return False

        # Fix the content
        fixed_content = fix_corrupted_frontmatter(content)

        # Write back
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(fixed_content)

        print("  ✓ Fixed corrupted frontmatter")
        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    base_dir = Path(__file__).parent.parent / "TCM_Patterns"

    print("=" * 70)
    print("FIXING CORRUPTED FRONTMATTER")
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
