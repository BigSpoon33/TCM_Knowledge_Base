#!/usr/bin/env python3
"""
Standardize all emoji headings to match TEMPLATE_Pattern.md
"""

import re
from pathlib import Path

# Standard emoji headings from template
HEADING_STANDARDS = {
    "Overview": "📋",
    "Pattern Classification": "🏷️",
    "Etiology & Pathogenesis": "🌱",
    "Clinical Manifestations": "🔍",
    "Diagnostic Criteria": "✅",
    "Differential Diagnosis": "🔄",
    "Treatment Principles": "🎯",
    "Herbal Formulas": "🌿",
    "Acupuncture Treatment": "📍",
    "Lifestyle & Prevention": "💡",
    "Modern Medicine Correlation": "🔬",
    "Clinical Notes": "📝",
    "References & Resources": "📚",
    "Case Studies": "📋",
}


def standardize_heading(line):
    """Standardize a heading to use correct emoji from template"""
    # Match pattern: ## [emoji] Heading Text
    match = re.match(r"^(##\s+)[^\s]+\s+(.+)$", line)
    if not match:
        return line

    prefix = match.group(1)  # "## "
    heading_text = match.group(2).strip()

    # Check if this heading matches one of our standards
    for standard_text, emoji in HEADING_STANDARDS.items():
        if standard_text.lower() in heading_text.lower() or heading_text.lower() in standard_text.lower():
            return f"{prefix}{emoji} {standard_text}\n"

    # If no match, return original
    return line


def fix_file(filepath):
    """Standardize emoji headings in a file"""
    try:
        with open(filepath, encoding="utf-8") as f:
            lines = f.readlines()

        fixed_lines = []
        changed = False

        for line in lines:
            if line.startswith("## ") and not line.startswith("### "):
                # Check if it has an emoji (non-ASCII character after ##)
                if any(ord(c) > 127 for c in line[:10]):
                    new_line = standardize_heading(line)
                    if new_line != line:
                        changed = True
                    fixed_lines.append(new_line)
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)

        if changed:
            with open(filepath, "w", encoding="utf-8") as f:
                f.writelines(fixed_lines)
            print("  ✓ Standardized emoji headings")
            return True

        return False

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    base_dir = Path(__file__).parent.parent / "TCM_Patterns"

    print("=" * 70)
    print("STANDARDIZING EMOJI HEADINGS TO MATCH TEMPLATE")
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
    print(f"✅ COMPLETE: Standardized {fixed_count} files")
    print("=" * 70)


if __name__ == "__main__":
    main()
