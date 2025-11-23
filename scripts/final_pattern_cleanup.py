#!/usr/bin/env python3
"""
Final cleanup: Remove all duplicate/old content sections
This script ensures each file has:
1. Frontmatter
2. Single # `=this.name` heading
3. Clean enhanced content
4. No duplicate sections
"""

import re
from pathlib import Path


def clean_file_final(filepath):
    """Remove all duplicate sections and keep only clean enhanced content"""
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Find the frontmatter
        frontmatter_match = re.match(r"(---\n.*?\n---\n)", content, re.DOTALL)
        if not frontmatter_match:
            return False

        frontmatter = frontmatter_match.group(1)
        rest = content[len(frontmatter) :]

        # Find the first # `=this.name` heading
        lines = rest.split("\n")

        # Build clean content
        clean_sections = []
        found_main_heading = False
        in_old_section = False

        for i, line in enumerate(lines):
            # Skip empty lines at start
            if not found_main_heading and line.strip() == "":
                continue

            # Found the main heading
            if "`=this.name`" in line and line.startswith("# "):
                found_main_heading = True
                clean_sections.append(line)
                continue

            # After main heading, check for old format markers
            if found_main_heading:
                # Stop if we hit old section markers
                if any(
                    marker in line
                    for marker in [
                        "# =9 Core Metadata",
                        "# =9 Cross-Link",
                        "# =9 Pattern-Specific",
                        "## YANG DEFICIENCY",
                        "## YANG COLLAPSE",
                        "# CAM",
                        "## 📦 Original Note Content",
                    ]
                ):
                    in_old_section = True
                    break

                # Keep good content
                if not in_old_section:
                    clean_sections.append(line)

        # Rebuild file
        if found_main_heading:
            new_content = frontmatter + "\n".join(clean_sections)

            # Clean up excessive newlines
            new_content = re.sub(r"\n{4,}", "\n\n\n", new_content)
            new_content = new_content.rstrip() + "\n"

            if new_content != original_content:
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
    print("FINAL PATTERN CLEANUP - REMOVING ALL DUPLICATES")
    print("=" * 70)
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
                ):  # Skip index files
                    pattern_files.append(file)

    print(f"Found {len(pattern_files)} pattern files to clean\n")

    cleaned_count = 0
    for i, filepath in enumerate(sorted(pattern_files), 1):
        rel_path = filepath.relative_to(base_dir)

        if clean_file_final(filepath):
            print(f"[{i}/{len(pattern_files)}] {rel_path} - ✓ Cleaned")
            cleaned_count += 1

    print()
    print("=" * 70)
    print(f"✅ COMPLETE: Cleaned {cleaned_count} files")
    print("=" * 70)


if __name__ == "__main__":
    main()
