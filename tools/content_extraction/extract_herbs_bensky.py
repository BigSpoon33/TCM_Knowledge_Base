#!/usr/bin/env python3
"""
Extract herbs from Bensky Materia Medica PDF
Creates properly formatted herb markdown files
"""

import re
from datetime import datetime
from pathlib import Path

import fitz


class HerbExtractor:
    """Extract herb information from Bensky Materia Medica"""

    def __init__(self, pdf_path: Path, output_dir: Path):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.herbs_dir = output_dir / "TCM_Herbs"
        self.herbs_dir.mkdir(exist_ok=True, parents=True)

        self.doc = fitz.open(self.pdf_path)
        self.toc = self.doc.get_toc()

        print(f"✅ Loaded PDF: {self.pdf_path.name}")
        print(f"   Total pages: {len(self.doc)}")

    def extract_herb(self, herb_name: str, start_page: int, end_page: int):
        """Extract a single herb"""
        print(f"\n{'=' * 60}")
        print(f"EXTRACTING: {herb_name}")
        print(f"{'=' * 60}")
        print(f"📄 Pages: {start_page}-{end_page} ({end_page - start_page + 1} pages)")

        # Extract text
        print("📝 Extracting text...")
        full_text = ""
        for page_num in range(start_page - 1, end_page):
            page = self.doc[page_num]
            text = page.get_text()
            full_text += text + "\n\n"

        print(f"  ✓ Extracted {len(full_text)} characters")

        # Parse herb data
        herb_data = self._parse_herb_info(full_text, herb_name)

        # Create markdown
        print("📝 Creating markdown file...")
        md_content = self._create_herb_markdown(herb_data, start_page, end_page)

        # Save file
        filename = f"{herb_data['pinyin'].replace(' ', '_')}.md"
        filepath = self.herbs_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"✅ Created: {filename}")
        print(f"   Size: {len(md_content)} characters")

        return filepath

    def _parse_herb_info(self, text: str, herb_name: str):
        """Parse herb information from extracted text"""

        # Extract pinyin (usually first line or near top)
        pinyin_match = re.search(r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*\n", text[:500])
        pinyin = pinyin_match.group(1).strip() if pinyin_match else herb_name

        # Extract pharmaceutical name
        pharm_match = re.search(r"\(([A-Z][a-z]+(?:ae|i|is)?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\)", text[:500])
        pharmaceutical = pharm_match.group(1).strip() if pharm_match else ""

        # Extract properties
        properties = {"taste": [], "temperature": "", "channels": [], "category": ""}

        # Taste
        taste_patterns = ["acrid", "bitter", "sweet", "sour", "salty", "bland"]
        for taste in taste_patterns:
            if taste in text.lower()[:2000]:
                properties["taste"].append(taste)

        # Temperature
        temp_match = re.search(r"\b(warm|hot|cool|cold|neutral)\b", text.lower()[:2000])
        if temp_match:
            properties["temperature"] = temp_match.group(1)

        # Channels
        channel_patterns = [
            "Lung",
            "Spleen",
            "Stomach",
            "Heart",
            "Liver",
            "Kidney",
            "Large Intestine",
            "Small Intestine",
            "Bladder",
            "Gall Bladder",
            "Pericardium",
            "Triple Burner",
        ]
        for channel in channel_patterns:
            if channel in text[:2000]:
                properties["channels"].append(channel)

        # Extract dosage
        dosage_match = re.search(r"(\d+[-–]\d+\s*g)", text[:3000])
        dosage = dosage_match.group(1) if dosage_match else ""

        # Extract functions (look for bullet points or numbered lists)
        functions = []
        function_section = re.search(
            r"(Actions?|Functions?|Indications?)[:\s]+(.*?)(?=\n\n|\nCautions?|\nContraindications?)",
            text,
            re.DOTALL | re.IGNORECASE,
        )
        if function_section:
            func_text = function_section.group(2)
            # Extract bullet points or lines starting with •, -, or numbers
            func_lines = re.findall(r"[•\-\*]\s*([^\n]+)", func_text)
            functions = [f.strip() for f in func_lines if len(f.strip()) > 10][:5]

        return {
            "name": herb_name,
            "pinyin": pinyin,
            "pharmaceutical": pharmaceutical,
            "taste": properties["taste"],
            "temperature": properties["temperature"],
            "channels": properties["channels"],
            "dosage": dosage,
            "functions": functions,
            "full_text": text,
            "category": properties["category"],
        }

    def _create_herb_markdown(self, herb_data: dict, start_page: int, end_page: int):
        """Create markdown file for herb"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        md = f"""---
id: herb-{timestamp}
name: {herb_data["name"]}
type: herb
aliases: []
tags:
- TCM
- Herb
category: []
related: []
symptoms: []
patterns: []
western_conditions: []
formulas: []
points: []
herb_data:
  hanzi: ""
  pinyin: {herb_data["pinyin"]}
  pharmaceutical: {herb_data["pharmaceutical"]}
  english: ""
  alternate_names: []
  taste:
{chr(10).join(f"  - {t}" for t in herb_data["taste"]) if herb_data["taste"] else "  []"}
  temperature: {herb_data["temperature"]}
  channels:
{chr(10).join(f"  - {c}" for c in herb_data["channels"]) if herb_data["channels"] else "  []"}
  dosage: {herb_data["dosage"]}
  toxicity: ''
  functions:
{chr(10).join(f"  - {f}" for f in herb_data["functions"]) if herb_data["functions"] else "  []"}
  dui_yao: []
  contraindications: []
  notes: ''
---

# {herb_data["name"]} ({herb_data["pinyin"]})

**Source**: Bensky *Chinese Herbal Medicine: Materia Medica* 3rd ed.
**Pages**: {start_page}-{end_page}
**Extracted**: {datetime.now().strftime("%Y-%m-%d")}

---

## Extracted Text

{herb_data["full_text"]}

---

## Notes

- This file was auto-extracted from Bensky Materia Medica
- Review and enhance with:
  - Clinical applications
  - Formula associations
  - Contraindications
  - Modern research
- Add wikilinks to related herbs, formulas, and patterns

---

*Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""
        return md


def main():
    import sys

    base_dir = Path(__file__).parent.parent
    pdf_path = base_dir / "Books" / "Bensky - Materia Medica.pdf"

    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}")
        return 1

    extractor = HerbExtractor(pdf_path, base_dir)

    # Priority 1 herbs with correct page ranges
    priority_herbs = [
        ("Ban Xia", 446, 450),  # Zhi Ban Xia (Prepared Pinellia)
        ("Ban Lan Gen", 191, 193),  # Isatis Root
        ("Bai Hua She She Cao", 216, 217),  # Oldenlandia
        ("Bai Ji", 618, 620),  # Bletilla
        ("Bai Xian Pi", 230, 232),  # Dictamnus
        ("Bi Ba", 734, 735),  # Long Pepper
        ("Cao Wu", 713, 715),  # Aconite (prepared)
        ("Chun Pi", 907, 909),  # Ailanthus
        ("Ci Ji Li", 1008, 1010),  # Tribulus
    ]

    if len(sys.argv) > 1:
        # Extract specific herb by number
        herb_num = int(sys.argv[1]) - 1
        if 0 <= herb_num < len(priority_herbs):
            name, start, end = priority_herbs[herb_num]
            extractor.extract_herb(name, start, end)
        else:
            print(f"❌ Invalid herb number. Choose 1-{len(priority_herbs)}")
            return 1
    else:
        # Extract all herbs
        for name, start, end in priority_herbs:
            extractor.extract_herb(name, start, end)

    return 0


if __name__ == "__main__":
    exit(main())
