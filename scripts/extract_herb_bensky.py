#!/usr/bin/env python3
"""
Extract herb information from Bensky Materia Medica and create herb markdown files
"""

import re
from datetime import datetime
from pathlib import Path

import fitz  # PyMuPDF


class HerbExtractor:
    """Extract herb information from Bensky Materia Medica PDF"""

    def __init__(self, pdf_path: Path, output_dir: Path):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.herbs_dir = output_dir / "TCM_Herbs"
        self.herbs_dir.mkdir(exist_ok=True, parents=True)

        # Load PDF
        self.doc = fitz.open(self.pdf_path)
        print(f"✅ Loaded PDF: {self.pdf_path.name}")
        print(f"   Total pages: {len(self.doc)}")

    def extract_herb(self, start_page: int, end_page: int, herb_name: str):
        """Extract herb information from specified pages"""
        print(f"\n{'=' * 60}")
        print(f"EXTRACTING: {herb_name}")
        print(f"{'=' * 60}")
        print(f"📄 Pages: {start_page}-{end_page} ({end_page - start_page + 1} pages)")

        # Extract text
        print("📝 Extracting text...")
        full_text = ""
        for page_num in range(start_page - 1, end_page):  # PDF pages are 0-indexed
            page = self.doc[page_num]
            text = page.get_text()
            full_text += text + "\n\n"

        print(f"  ✓ Extracted {len(full_text)} characters")

        # Parse herb information
        herb_data = self._parse_herb_text(full_text, herb_name)

        # Create markdown file
        print("📝 Creating markdown file...")
        md_content = self._create_markdown(herb_data)

        # Save file
        filename = f"{herb_data['pinyin']}.md"
        filepath = self.herbs_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"✅ Created: {filename}")
        print(f"   Size: {len(md_content)} characters")
        print(f"\n{'=' * 60}")
        print("EXTRACTION COMPLETE")
        print(f"{'=' * 60}\n")

        return filepath

    def _parse_herb_text(self, text: str, herb_name: str):
        """Parse extracted text to extract herb information"""
        herb_data = {
            "name": herb_name,
            "pinyin": "",
            "hanzi": "",
            "pharmaceutical": "",
            "english": "",
            "category": "",
            "taste": [],
            "temperature": "",
            "channels": [],
            "dosage": "",
            "functions": [],
            "indications": "",
            "contraindications": "",
            "toxicity": "",
            "full_text": text,
        }

        # Extract pinyin (usually at the top)
        pinyin_match = re.search(r"([A-Z][a-z]+ [A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s*\n", text[:500])
        if pinyin_match:
            herb_data["pinyin"] = pinyin_match.group(1).strip()

        # Extract pharmaceutical name
        pharm_match = re.search(r"([A-Z][a-z]+(?:ae|i|is)?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)", text[:1000])
        if pharm_match:
            herb_data["pharmaceutical"] = pharm_match.group(1).strip()

        # Extract properties
        if "acrid" in text.lower() or "pungent" in text.lower():
            herb_data["taste"].append("acrid")
        if "bitter" in text.lower():
            herb_data["taste"].append("bitter")
        if "sweet" in text.lower():
            herb_data["taste"].append("sweet")
        if "sour" in text.lower():
            herb_data["taste"].append("sour")
        if "salty" in text.lower():
            herb_data["taste"].append("salty")

        # Extract temperature
        temp_match = re.search(r"(warm|hot|cool|cold|neutral)", text.lower())
        if temp_match:
            herb_data["temperature"] = temp_match.group(1)

        return herb_data

    def _create_markdown(self, herb_data: dict):
        """Create markdown content from herb data"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        md = f"""---
id: herb-{timestamp}
name: {herb_data["name"]}
type: herb
aliases: []
tags:
- TCM
- Herb
category:
- {herb_data["category"] if herb_data["category"] else "Transform Phlegm-Cold"}
related: []
symptoms: []
patterns: []
western_conditions: []
formulas: []
points: []
nutrition: []
tests: []
herb_data:
  hanzi: {herb_data["hanzi"]}
  pinyin: {herb_data["pinyin"]}
  pharmaceutical: {herb_data["pharmaceutical"]}
  english: {herb_data["english"]}
  alternate_names: []
  taste:
{chr(10).join(f"  - {t}" for t in herb_data["taste"]) if herb_data["taste"] else "  - []"}
  temperature: {herb_data["temperature"]}
  channels:
{chr(10).join(f"  - {c}" for c in herb_data["channels"]) if herb_data["channels"] else "  - []"}
  dosage: {herb_data["dosage"]}
  toxicity: ''
  functions:
{chr(10).join(f"  - {f}" for f in herb_data["functions"]) if herb_data["functions"] else "  - []"}
  dui_yao: []
  contraindications: []
  notes: ''
---

# {herb_data["name"]} ({herb_data["pinyin"]})

**Source**: Bensky *Chinese Herbal Medicine: Materia Medica* 3rd ed.
**Extracted**: {datetime.now().strftime("%Y-%m-%d")}

---

## Extracted Text

{herb_data["full_text"]}

---

## Clinical Applications

*To be added based on extracted text review*

## Formulas Containing This Herb

*To be linked*

## Related Herbs

*To be linked*

---

*Note: This file was auto-generated and requires manual review and enhancement*
"""
        return md


def main():
    # Setup paths
    base_dir = Path(__file__).parent.parent
    pdf_path = base_dir / "Books" / "Bensky - Materia Medica.pdf"

    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}")
        return

    extractor = HerbExtractor(pdf_path, base_dir)

    # Extract Ban Xia (pages 820-824)
    extractor.extract_herb(820, 824, "Ban Xia")


if __name__ == "__main__":
    main()
