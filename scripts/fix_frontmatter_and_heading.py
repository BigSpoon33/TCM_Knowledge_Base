#!/usr/bin/env python3
"""
Fix frontmatter and heading issues in enhanced pattern files:
1. Convert old frontmatter format to new clean format
2. Fix first heading to use `=this.name` syntax
"""

import os
from datetime import datetime
from pathlib import Path


def clean_frontmatter_value(value):
    """Clean up frontmatter values - remove extra quotes, brackets, etc."""
    if isinstance(value, str):
        # Remove quotes from simple strings
        value = value.strip("\"'")
        # Clean up list-like strings
        if value.startswith("[") and value.endswith("]"):
            # Parse as list
            items = [item.strip().strip("\"'") for item in value[1:-1].split(",")]
            return items
    return value


def convert_frontmatter(old_frontmatter, filename):
    """Convert old frontmatter format to new clean format"""

    # Parse old frontmatter
    lines = old_frontmatter.strip().split("\n")
    data = {}
    current_key = None
    current_indent = 0

    for line in lines:
        if line.strip() == "---" or line.strip().startswith("#"):
            continue

        # Count indentation
        indent = len(line) - len(line.lstrip())

        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if indent == 0:
                # Top level key
                current_key = key
                if value:
                    data[key] = clean_frontmatter_value(value)
                else:
                    data[key] = []
                current_indent = indent
            else:
                # Nested key (like pattern_data fields)
                if current_key not in data:
                    data[current_key] = {}
                if isinstance(data[current_key], dict):
                    data[current_key][key] = clean_frontmatter_value(value)
        elif line.strip().startswith("-"):
            # List item
            item = line.strip()[1:].strip()
            item = clean_frontmatter_value(item)
            if current_key:
                if not isinstance(data[current_key], list):
                    data[current_key] = []
                data[current_key].append(item)

    # Extract pattern name from filename
    pattern_name = filename.replace(".md", "").replace("_", " ")

    # Generate new ID
    date_str = datetime.now().strftime("%Y%m%d")
    id_slug = pattern_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
    new_id = f"pattern-{date_str}-{id_slug}"

    # Build new frontmatter
    new_fm = []
    new_fm.append("---")
    new_fm.append(f"id: {new_id}")
    new_fm.append(f"name: {pattern_name}")
    new_fm.append("type: pattern")

    # Aliases
    if "aliases" in data and data["aliases"]:
        new_fm.append("aliases:")
        for alias in data["aliases"] if isinstance(data["aliases"], list) else [data["aliases"]]:
            if alias and alias != "[]":
                new_fm.append(f"- {alias}")
    else:
        new_fm.append("aliases: []")

    # Tags
    if "tags" in data and data["tags"]:
        new_fm.append("tags:")
        tags = data["tags"] if isinstance(data["tags"], list) else [data["tags"]]
        for tag in tags:
            if tag and tag != "[TCM, Pattern]":
                new_fm.append(f"- {tag}")
    else:
        new_fm.append("tags:")
        new_fm.append("- TCM")
        new_fm.append("- Pattern")

    # Category
    if "category" in data and data["category"]:
        new_fm.append("category:")
        cats = data["category"] if isinstance(data["category"], list) else [data["category"]]
        for cat in cats:
            if cat:
                new_fm.append(f"- {cat}")
    else:
        new_fm.append("category: []")

    # Related
    if "related" in data and data["related"]:
        new_fm.append("related:")
        rels = data["related"] if isinstance(data["related"], list) else [data["related"]]
        for rel in rels:
            if rel:
                new_fm.append(f"- {rel}")
    else:
        new_fm.append("related: []")

    # Symptoms
    if "symptoms" in data and data["symptoms"]:
        new_fm.append("symptoms:")
        syms = data["symptoms"] if isinstance(data["symptoms"], list) else [data["symptoms"]]
        for sym in syms:
            if sym:
                # Add [[ ]] if not already present
                if not sym.startswith("[["):
                    sym = f"[[{sym}]]"
                new_fm.append(f"- '{sym}'")
    else:
        new_fm.append("symptoms: []")

    # Patterns
    new_fm.append("patterns: []")

    # Western conditions
    if "western_conditions" in data and data["western_conditions"]:
        new_fm.append("western_conditions:")
        wcs = (
            data["western_conditions"] if isinstance(data["western_conditions"], list) else [data["western_conditions"]]
        )
        for wc in wcs:
            if wc:
                new_fm.append(f"- {wc}")
    else:
        new_fm.append("western_conditions: []")

    # Formulas
    if "formulas" in data and data["formulas"]:
        new_fm.append("formulas:")
        forms = data["formulas"] if isinstance(data["formulas"], list) else [data["formulas"]]
        for form in forms:
            if form:
                new_fm.append(f"- {form}")
    else:
        new_fm.append("formulas: []")

    # Herbs
    if "herbs" in data and data["herbs"]:
        new_fm.append("herbs:")
        herbs = data["herbs"] if isinstance(data["herbs"], list) else [data["herbs"]]
        for herb in herbs:
            if herb:
                new_fm.append(f"- {herb}")
    else:
        new_fm.append("herbs: []")

    # Points
    if "points" in data and data["points"]:
        new_fm.append("points:")
        pts = data["points"] if isinstance(data["points"], list) else [data["points"]]
        for pt in pts:
            if pt:
                new_fm.append(f"- {pt}")
    else:
        new_fm.append("points: []")

    # Nutrition
    if "nutrition" in data and data["nutrition"]:
        new_fm.append("nutrition:")
        nuts = data["nutrition"] if isinstance(data["nutrition"], list) else [data["nutrition"]]
        for nut in nuts:
            if nut:
                new_fm.append(f"- {nut}")
    else:
        new_fm.append("nutrition: []")

    # Tests
    if "tests" in data and data["tests"]:
        new_fm.append("tests:")
        tests = data["tests"] if isinstance(data["tests"], list) else [data["tests"]]
        for test in tests:
            if test:
                new_fm.append(f"- {test}")
    else:
        new_fm.append("tests: []")

    # Pattern data
    if "pattern_data" in data and isinstance(data["pattern_data"], dict):
        new_fm.append("pattern_data:")
        pd = data["pattern_data"]

        for key in [
            "pattern_type",
            "pattern_subtype",
            "excess_deficiency",
            "hot_cold",
            "interior_exterior",
            "yin_yang",
        ]:
            if key in pd:
                new_fm.append(f"  {key}: {pd[key]}")

        # Lists in pattern_data
        for key in ["etiology", "pathomechanisms", "cardinal_symptoms", "treatment_principle", "contraindications"]:
            if key in pd:
                new_fm.append(f"  {key}:")
                items = pd[key] if isinstance(pd[key], list) else [pd[key]]
                for item in items:
                    if item:
                        new_fm.append(f"  - {item}")

        # String fields
        for key in ["disease_progression", "tongue", "pulse"]:
            if key in pd and pd[key]:
                new_fm.append(f"  {key}: {pd[key]}")

    # Dates
    today = datetime.now().strftime("%Y-%m-%d")
    if "created" in data:
        new_fm.append(f"created: {data['created']}")
    else:
        new_fm.append(f"created: {today}")

    if "updated" in data:
        new_fm.append(f"updated: {data['updated']}")
    else:
        new_fm.append(f"updated: {today}")

    new_fm.append("")
    new_fm.append("---")

    return "\n".join(new_fm)


def fix_file(filepath):
    """Fix both frontmatter and first heading in a file"""
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        if "---" not in content:
            return False

        # Extract frontmatter
        parts = content.split("---", 2)
        if len(parts) < 3:
            return False

        old_frontmatter = parts[1]
        body = parts[2]

        filename = os.path.basename(filepath)

        # Check if already in new format (has symptoms with [[]])
        if "'[[" in old_frontmatter and "pattern-202" in old_frontmatter:
            print("  ✓ Already in new format, checking heading...")
            # Just fix heading
            # Find first h1 heading after frontmatter
            lines = body.split("\n")
            for i, line in enumerate(lines):
                if line.strip().startswith("# ") and not line.strip().startswith("## "):
                    # Fix heading
                    if "=." in line or "=" in line:
                        pattern_name = filename.replace(".md", "")
                        lines[i] = "# `=this.name`"
                        body = "\n".join(lines)

                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(f"---{old_frontmatter}---{body}")
                        print("  ✓ Fixed heading")
                        return True
                    elif "`=this.name`" in line:
                        print("  ✓ Heading already correct")
                        return False
                    break
            return False

        # Convert frontmatter
        print("  Converting frontmatter...")
        new_frontmatter = convert_frontmatter(old_frontmatter, filename)

        # Fix first heading
        lines = body.split("\n")
        for i, line in enumerate(lines):
            if line.strip().startswith("# ") and not line.strip().startswith("## "):
                lines[i] = "# `=this.name`"
                break

        body = "\n".join(lines)

        # Write back
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"{new_frontmatter}\n{body}")

        print("  ✓ Fixed frontmatter and heading")
        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    base_dir = Path(__file__).parent.parent / "TCM_Patterns"

    print("=" * 70)
    print("FIXING FRONTMATTER AND HEADING SYNTAX")
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
