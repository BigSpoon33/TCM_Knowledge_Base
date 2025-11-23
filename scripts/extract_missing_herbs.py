#!/usr/bin/env python3
"""
Extract all missing NCCAOM herbs from Bensky Materia Medica
Handles pinyin tone marks properly
"""

import json
import re
from datetime import datetime
from pathlib import Path

import fitz


def clean_pinyin_tone_marks(text):
    """Remove or convert tone mark characters that cause encoding issues"""
    # Common tone mark replacements
    replacements = {
        "ā": "a",
        "á": "a",
        "ǎ": "a",
        "à": "a",
        "ē": "e",
        "é": "e",
        "ě": "e",
        "è": "e",
        "ī": "i",
        "í": "i",
        "ǐ": "i",
        "ì": "i",
        "ō": "o",
        "ó": "o",
        "ǒ": "o",
        "ò": "o",
        "ū": "u",
        "ú": "u",
        "ǔ": "u",
        "ù": "u",
        "ǖ": "u",
        "ǘ": "u",
        "ǚ": "u",
        "ǜ": "u",
        "ü": "u",
        "ń": "n",
        "ň": "n",
        "ǹ": "n",
        "ḿ": "m",
        # Additional problematic characters
        "yiw": "yao",
        "mfng": "ming",
        "zl": "zi",
    }

    result = text
    for old, new in replacements.items():
        result = result.replace(old, new)

    return result


def find_herb_in_toc(herb_name, all_herbs_data):
    """Find herb in the extracted TOC data"""
    # Try exact match first
    for herb in all_herbs_data:
        if herb["name"] == herb_name:
            return herb

    # Try partial match
    for herb in all_herbs_data:
        if herb_name in herb["name"] or herb["name"] in herb_name:
            return herb

    return None


def extract_herb(pdf, herb_name, start_page, end_page, herbs_dir):
    """Extract a single herb"""
    # Extract text
    full_text = ""
    for page_num in range(start_page - 1, end_page):
        if page_num < len(pdf):
            page = pdf[page_num]
            text = page.get_text()
            full_text += text + "\n\n"

    # Clean tone marks from full text
    full_text = clean_pinyin_tone_marks(full_text)

    # Parse pharmaceutical name
    pharm_match = re.search(r"PHARMACEUTICAL NAME\s+([^\n]+)", full_text)
    pharmaceutical = pharm_match.group(1).strip() if pharm_match else ""

    # Parse properties
    props_match = re.search(r"PROPERTIES\s+([^\n]+)", full_text)
    properties = props_match.group(1).strip() if props_match else ""

    taste = []
    temperature = ""
    if properties:
        if "acrid" in properties:
            taste.append("acrid")
        if "bitter" in properties:
            taste.append("bitter")
        if "sweet" in properties:
            taste.append("sweet")
        if "sour" in properties:
            taste.append("sour")
        if "salty" in properties:
            taste.append("salty")
        if "bland" in properties:
            taste.append("bland")

        if "warm" in properties:
            temperature = "warm"
        elif "hot" in properties:
            temperature = "hot"
        elif "cool" in properties:
            temperature = "cool"
        elif "cold" in properties:
            temperature = "cold"
        elif "neutral" in properties:
            temperature = "neutral"

    # Extract channels
    channels_match = re.search(r"CHANNELS ENTERED\s+([^\n]+)", full_text)
    channels_text = channels_match.group(1).strip() if channels_match else ""
    channels = [c.strip() for c in channels_text.split(",") if c.strip()]

    # Extract dosage
    dosage_match = re.search(r"DosAGE\s+([^\n]+)", full_text)
    dosage = dosage_match.group(1).strip() if dosage_match else ""

    # Extract category
    category_match = re.search(r"\d+\s+I\s+Herbs that ([^\n]+)", full_text)
    category = category_match.group(1).strip() if category_match else ""

    # Create markdown
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    md = f"""---
id: herb-{timestamp}
name: {herb_name}
type: herb
aliases: []
tags:
- TCM
- Herb
category:
- {category if category else "To be categorized"}
related: []
symptoms: []
patterns: []
western_conditions: []
formulas: []
points: []
herb_data:
  hanzi: ""
  pinyin: {herb_name}
  pharmaceutical: {pharmaceutical}
  english: ""
  alternate_names: []
  taste:
{chr(10).join(f"  - {t}" for t in taste) if taste else "  []"}
  temperature: {temperature}
  channels:
{chr(10).join(f"  - {c}" for c in channels) if channels else "  []"}
  dosage: {dosage}
  toxicity: ''
  functions: []
  dui_yao: []
  contraindications: []
  notes: ''
---

# {herb_name}

**Pharmaceutical**: {pharmaceutical}
**Source**: Bensky *Chinese Herbal Medicine: Materia Medica* 3rd ed.
**Pages**: {start_page}-{end_page}
**Category**: {category if category else "To be categorized"}
**Extracted**: {datetime.now().strftime("%Y-%m-%d")}

---

## Properties

- **Taste**: {", ".join(taste) if taste else "Not specified"}
- **Temperature**: {temperature if temperature else "Not specified"}
- **Channels**: {", ".join(channels) if channels else "Not specified"}
- **Dosage**: {dosage if dosage else "Not specified"}

---

## Extracted Text

{full_text}

---

## Clinical Applications

*To be added*

## Formulas Containing This Herb

*To be linked*

---

*Auto-extracted from Bensky Materia Medica*
*Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""

    # Save file
    filename = f"{herb_name.replace(' ', '_')}.md"
    filepath = herbs_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)

    return filepath


def main():

    base_dir = Path(__file__).parent.parent
    pdf_path = base_dir / "Books" / "Bensky - Materia Medica.pdf"
    herbs_dir = base_dir / "TCM_Herbs"

    # Load missing herbs list
    missing_file = base_dir / "missing_herbs_list.txt"
    if not missing_file.exists():
        print("❌ missing_herbs_list.txt not found")
        return 1

    with open(missing_file) as f:
        missing_herbs = [line.strip() for line in f if line.strip()]

    # Load all herbs TOC data
    toc_file = base_dir / "all_bensky_herbs.json"
    if not toc_file.exists():
        print("❌ all_bensky_herbs.json not found")
        return 1

    with open(toc_file, encoding="utf-8") as f:
        all_herbs_data = json.load(f)

    # Open PDF
    pdf = fitz.open(pdf_path)

    print("=" * 60)
    print(f"EXTRACTING {len(missing_herbs)} MISSING HERBS")
    print("=" * 60)

    extracted = 0
    not_found = []

    for i, herb_name in enumerate(missing_herbs, 1):
        # Find herb in TOC
        herb_data = find_herb_in_toc(herb_name, all_herbs_data)

        if herb_data:
            print(f"\n[{i}/{len(missing_herbs)}] {herb_name}...")
            try:
                filepath = extract_herb(pdf, herb_name, herb_data["start"], herb_data["end"], herbs_dir)
                print(f"  ✓ Created: {filepath.name}")
                extracted += 1
            except Exception as e:
                print(f"  ✗ Error: {e}")
                not_found.append(herb_name)
        else:
            print(f"\n[{i}/{len(missing_herbs)}] {herb_name}... ✗ Not found in TOC")
            not_found.append(herb_name)

    pdf.close()

    print(f"\n{'=' * 60}")
    print("EXTRACTION COMPLETE")
    print(f"{'=' * 60}")
    print(f"Extracted: {extracted}/{len(missing_herbs)}")
    print(f"Not found: {len(not_found)}")

    if not_found:
        print("\nHerbs not found:")
        for herb in not_found:
            print(f"  - {herb}")

    return 0


if __name__ == "__main__":
    exit(main())
