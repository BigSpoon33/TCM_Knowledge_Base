#!/usr/bin/env python3
"""
Quick extract formulas from Chen Chinese Herbal Formulas book (has extractable text)
Much faster than OCR approach
"""

import fitz
import re
from pathlib import Path
from datetime import datetime


def normalize_formula_name(name):
    """Normalize formula name for file naming"""
    return name.replace("/", "-").strip()


def extract_formula_from_chen(pdf_path, formula_name, search_pages=50):
    """
    Extract formula information from Chen book
    Searches for the formula name and extracts surrounding text
    """
    pdf = fitz.open(pdf_path)
    formula_text = ""
    found_page = None
    
    # Search for formula name in PDF
    for page_num in range(min(len(pdf), search_pages)):
        page = pdf[page_num]
        text = page.get_text()
        
        # Check if formula name appears on this page
        if formula_name.lower() in text.lower():
            found_page = page_num
            # Extract text from this page and next 2-3 pages
            for i in range(4):  # Current page + next 3
                if page_num + i < len(pdf):
                    formula_text += pdf[page_num + i].get_text() + "\n\n"
            break
    
    pdf.close()
    
    if not found_page:
        return None, None
    
    return formula_text, found_page + 1


def create_formula_markdown(formula_name, text, source_page):
    """Create a markdown file for the formula"""
    today = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Try to extract key information from text
    ingredients = []
    actions = []
    indications = []
    
    # Simple parsing - look for common patterns
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if 'ingredient' in line.lower() or 'composition' in line.lower():
            # Extract next few lines as ingredients
            for j in range(i+1, min(i+15, len(lines))):
                if lines[j].strip() and not lines[j].startswith('#'):
                    ingredients.append(lines[j].strip())
        
        if 'action' in line.lower() or 'function' in line.lower():
            for j in range(i+1, min(i+10, len(lines))):
                if lines[j].strip():
                    actions.append(lines[j].strip())
        
        if 'indication' in line.lower() or 'use' in line.lower():
            for j in range(i+1, min(i+10, len(lines))):
                if lines[j].strip():
                    indications.append(lines[j].strip())
    
    # Create markdown content
    content = f"""---
id: formula-{today}
name: "{formula_name}"
type: formula
category: []
aliases: []
tags:
  - TCM
  - Formula
  - NCCAOM
related: []
patterns: []
symptoms: []
diseases: []
western_conditions: []
herbs: []
points: []
formulas: []
chief_herbs: []
actions: []
source: Chen - Chinese Herbal Formulas and Applications
source_page: "{source_page}"
updated: {datetime.now().strftime("%Y-%m-%d")}
stock: true
---

# {formula_name}

## 📖 Source Reference
Extracted from Chen - Chinese Herbal Formulas and Applications, page {source_page}

## 🌿 Composition & Dosages

*Note: This is an auto-generated template. Please review and enhance with specific dosages and hierarchy.*

{chr(10).join(['- ' + ing for ing in ingredients[:10]]) if ingredients else '- [Ingredients to be added]'}

## 🎯 Clinical Applications

### Primary Pattern & Manifestations

**Actions:**
{chr(10).join(['- ' + act for act in actions[:5]]) if actions else '- [Actions to be added]'}

**Indications:**
{chr(10).join(['- ' + ind for ind in indications[:5]]) if indications else '- [Indications to be added]'}

## 📋 Key Diagnostic Signs

- **Tongue**: [To be added]
- **Pulse**: [To be added]

## ⚕️ Modifications

*To be added based on specific presentations*

## ⚠️ Contraindications & Cautions

- [To be added]

## 📚 Clinical Notes

*Extracted text for reference:*

{text[:2000]}

---

*Auto-generated from Chen source. Please review and enhance.*
*Last updated: {datetime.now().strftime("%Y-%m-%d")}*
"""
    
    return content


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Quick extract formulas from Chen book")
    parser.add_argument("--formula", required=True, help="Formula name to extract")
    parser.add_argument("--pdf", default="Books/Chinese Herbal Formulas and Applications Pharmacological Effects Clinical Research by John K. Chen Tina T. Chen Minh Nguyen Lily Huang Jimmy Chang Rick Friesen Chien-Hui Liao (z-lib.org).pdf")
    
    args = parser.parse_args()
    
    print(f"Searching for: {args.formula}")
    
    text, page = extract_formula_from_chen(args.pdf, args.formula, search_pages=1500)
    
    if not text:
        print(f"✗ Formula '{args.formula}' not found in PDF")
        return 1
    
    print(f"✓ Found on page {page}")
    
    # Create markdown file
    content = create_formula_markdown(args.formula, text, page)
    filename = normalize_formula_name(args.formula) + ".md"
    filepath = Path("TCM_Formulas") / filename
    
    filepath.write_text(content, encoding='utf-8')
    print(f"✓ Created: {filepath}")
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
