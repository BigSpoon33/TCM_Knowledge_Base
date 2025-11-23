#!/usr/bin/env python3
"""
Fix Obsidian syntax issues in enhanced pattern files:
1. Remove ```markdown or ``` code block wrappers from first line
2. Replace heading symbols (=, <, >, etc.) with emojis
"""

import re
from pathlib import Path

# Heading symbol to emoji mapping
HEADING_MAP = {
    "## = Overview": "## 📋 Overview",
    "## < Pattern Classification": "## 🏷️ Pattern Classification",
    "## > Etiology & Pathogenesis": "## 🌱 Etiology & Pathogenesis",
    "## >z Clinical Manifestations": "## 🔍 Clinical Manifestations",
    "## = Diagnostic Criteria": "## ✅ Diagnostic Criteria",
    "## < Differential Diagnosis": "## 🔄 Differential Diagnosis",
    "## > Treatment Principles": "## 🎯 Treatment Principles",
    "## >< Herbal Formulas": "## 🌿 Herbal Formulas",
    "## >= Acupuncture Treatment": "## 📍 Acupuncture Treatment",
    "## < Lifestyle & Prevention": "## 💡 Lifestyle & Prevention",
    "## = Modern Medicine Correlation": "## 🔬 Modern Medicine Correlation",
    "## > Clinical Notes": "## 📝 Clinical Notes",
    "## =\n Diagnostic Criteria": "## ✅ Diagnostic Criteria",
}


def fix_file(filepath):
    """Fix syntax issues in a single file"""
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        original_content = content
        modified = False

        # Fix 1: Remove ```markdown or ``` from first line
        lines = content.split("\n")
        if lines and (lines[0].strip() == "```markdown" or lines[0].strip() == "```"):
            lines = lines[1:]  # Remove first line
            content = "\n".join(lines)
            modified = True
            print("  ✓ Removed code block wrapper")

        # Fix 2: Replace heading symbols with emojis
        for old_heading, new_heading in HEADING_MAP.items():
            if old_heading in content:
                content = content.replace(old_heading, new_heading)
                modified = True

        # Additional pattern-based replacements for variations
        # Handle multi-line heading issues like "## =\n Diagnostic Criteria"
        content = re.sub(r"## =\s+", "## ✅ ", content)
        content = re.sub(r"## <\s+", "## 🏷️ ", content)
        content = re.sub(r"## >\s+", "## 🌱 ", content)
        content = re.sub(r"## >z\s+", "## 🔍 ", content)
        content = re.sub(r"## ><\s+", "## 🌿 ", content)
        content = re.sub(r"## >=\s+", "## 📍 ", content)

        if content != original_content:
            modified = True

        # Write back if modified
        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return True

        return False

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    base_dir = Path(__file__).parent.parent / "TCM_Patterns"

    print("=" * 70)
    print("FIXING OBSIDIAN SYNTAX ISSUES")
    print("=" * 70)
    print()

    # Find all pattern markdown files
    pattern_files = []
    for folder in base_dir.iterdir():
        if folder.is_dir():
            for file in folder.glob("*.md"):
                # Skip index files and templates
                if not file.name.startswith("00 ") and "TEMPLATE" not in file.name:
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
