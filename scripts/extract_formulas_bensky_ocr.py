#!/usr/bin/env python3
"""
Extract missing formulas from Bensky Formulas & Strategies (scanned PDF)
Uses OCR to extract text from images
"""

import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import re
from pathlib import Path
from datetime import datetime


def clean_pinyin_tone_marks(text):
    """Remove or convert tone mark characters that cause encoding issues"""
    replacements = {
        'ā': 'a', 'á': 'a', 'ǎ': 'a', 'à': 'a',
        'ē': 'e', 'é': 'e', 'ě': 'e', 'è': 'e',
        'ī': 'i', 'í': 'i', 'ǐ': 'i', 'ì': 'i',
        'ō': 'o', 'ó': 'o', 'ǒ': 'o', 'ò': 'o',
        'ū': 'u', 'ú': 'u', 'ǔ': 'u', 'ù': 'u',
        'ǖ': 'u', 'ǘ': 'u', 'ǚ': 'u', 'ǜ': 'u', 'ü': 'u',
        'ń': 'n', 'ň': 'n', 'ǹ': 'n',
    }
    
    result = text
    for old, new in replacements.items():
        result = result.replace(old, new)
    
    return result


def ocr_page(pdf_page, dpi=300):
    """
    OCR a single PDF page
    
    Args:
        pdf_page: PyMuPDF page object
        dpi: Resolution for rendering (higher = better quality but slower)
    
    Returns:
        str: Extracted text
    """
    # Render page to image
    mat = fitz.Matrix(dpi/72, dpi/72)  # 72 is default DPI
    pix = pdf_page.get_pixmap(matrix=mat)
    
    # Convert to PIL Image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # OCR the image
    text = pytesseract.image_to_string(img, lang='eng')
    
    return text


def extract_formula_pages(pdf, start_page, end_page, formula_name):
    """
    Extract text from a range of pages using OCR
    
    Args:
        pdf: PyMuPDF document
        start_page: Starting page number (1-indexed)
        end_page: Ending page number (1-indexed)
        formula_name: Name of formula for progress tracking
    
    Returns:
        str: Combined text from all pages
    """
    print(f"  Extracting {formula_name} (pages {start_page}-{end_page})...")
    
    full_text = ""
    for page_num in range(start_page - 1, end_page):
        if page_num < len(pdf):
            print(f"    OCR page {page_num + 1}...", end=" ", flush=True)
            page = pdf[page_num]
            text = ocr_page(page, dpi=300)
            full_text += text + "\n\n"
            print("✓")
    
    return clean_pinyin_tone_marks(full_text)


def parse_formula_text(text, formula_name):
    """
    Parse OCR'd formula text and extract key information
    
    Returns:
        dict: Parsed formula data
    """
    data = {
        'name': formula_name,
        'pinyin': '',
        'translation': '',
        'category': '',
        'actions': [],
        'indications': [],
        'ingredients': [],
        'contraindications': '',
        'modifications': '',
        'cautions': '',
    }
    
    # Try to extract pinyin (usually at top)
    pinyin_match = re.search(r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*(?:Decoction|Powder|Pill|Tang|San|Wan)', text, re.MULTILINE)
    if pinyin_match:
        data['pinyin'] = pinyin_match.group(1).strip()
    
    # Extract translation (usually in parentheses or after formula name)
    trans_match = re.search(r'\(([^)]+(?:Decoction|Powder|Pill|Formula))\)', text)
    if trans_match:
        data['translation'] = trans_match.group(1).strip()
    
    # Extract actions
    actions_match = re.search(r'(?:ACTIONS?|THERAPEUTIC EFFECTS?)[:\s]+([^\n]+(?:\n(?![A-Z]{2,})[^\n]+)*)', text, re.IGNORECASE)
    if actions_match:
        actions_text = actions_match.group(1).strip()
        data['actions'] = [a.strip() for a in re.split(r'[;,]|\d+\.', actions_text) if a.strip()]
    
    # Extract indications
    indications_match = re.search(r'(?:INDICATIONS?|CLINICAL MANIFESTATIONS?)[:\s]+([^\n]+(?:\n(?![A-Z]{2,})[^\n]+)*)', text, re.IGNORECASE)
    if indications_match:
        indications_text = indications_match.group(1).strip()
        data['indications'] = [i.strip() for i in re.split(r'[;,]|\d+\.', indications_text) if i.strip()]
    
    # Extract contraindications
    contra_match = re.search(r'(?:CONTRAINDICATIONS?|CAUTIONS?)[:\s]+([^\n]+(?:\n(?![A-Z]{2,})[^\n]+)*)', text, re.IGNORECASE)
    if contra_match:
        data['contraindications'] = contra_match.group(1).strip()
    
    return data


def create_formula_markdown(data, raw_text):
    """
    Create markdown file content for a formula
    
    Args:
        data: Parsed formula data dict
        raw_text: Raw OCR'd text for reference
    
    Returns:
        str: Markdown content
    """
    md = f"""---
name: "{data['name']}"
pinyin: "{data['pinyin']}"
translation: "{data['translation']}"
category: "{data['category']}"
source: "Bensky - Formulas and Strategies, 2nd Edition"
created: "{datetime.now().strftime('%Y-%m-%d')}"
---

# {data['name']}

**Pinyin**: {data['pinyin']}  
**Translation**: {data['translation']}  
**Category**: {data['category']}

## Actions

"""
    
    if data['actions']:
        for action in data['actions']:
            if action:
                md += f"- {action}\n"
    else:
        md += "*(See raw text below)*\n"
    
    md += "\n## Indications\n\n"
    
    if data['indications']:
        for indication in data['indications']:
            if indication:
                md += f"- {indication}\n"
    else:
        md += "*(See raw text below)*\n"
    
    md += "\n## Ingredients\n\n"
    md += "*(See raw text below)*\n"
    
    if data['contraindications']:
        md += f"\n## Contraindications\n\n{data['contraindications']}\n"
    
    md += f"""
## Notes

This formula was extracted via OCR from a scanned PDF. Please review and edit as needed.

---

## Raw Extracted Text

```
{raw_text[:3000]}
```

*(Text truncated at 3000 characters for readability)*

"""
    
    return md


def main():
    """Main extraction function"""
    
    # Paths
    pdf_path = Path("Books/Bensky - Formulas and Strategies, 2nd Edition-1.pdf")
    formulas_dir = Path("TCM_Formulas")
    
    if not pdf_path.exists():
        print(f"ERROR: PDF not found at {pdf_path}")
        return
    
    formulas_dir.mkdir(exist_ok=True)
    
    # Open PDF
    print(f"Opening {pdf_path.name}...")
    pdf = fitz.open(pdf_path)
    print(f"Total pages: {len(pdf)}")
    
    # Get TOC
    toc = pdf.get_toc()
    print(f"TOC entries: {len(toc)}")
    
    # Priority formulas to extract (from Gap_Filling_Checklist.md)
    # Format: (formula_name, approximate_start_page, approximate_end_page)
    priority_formulas = [
        # Release Exterior
        ("Ma Xing Shi Gan Tang", 58, 61),
        ("Xiao Qing Long Tang", 44, 48),
        ("Sang Xing Tang", 142, 144),
        ("Xin Yi San", 48, 50),
        ("Chai Ge Jie Ji Tang", 54, 56),
        ("Ge Gen Tang", 29, 31),
        ("Ge Gen Huang Lian Huang Qin Tang", 56, 58),
        ("Gui Zhi Jia Ge Gen Tang", 31, 32),
        ("Bai Hu Jia Gui Zhi Tang", 168, 169),
        ("Bai Hu Jia Ren Shen Tang", 167, 168),
        
        # Clear Heat
        ("Qing Hao Bie Jia Tang", 186, 189),
        ("Huang Qin Tang", 100, 102),
        ("Huang Lian E Jiao Tang", 189, 191),
        ("Pu Ji Xiao Du Yin", 80, 82),
        ("Qing Wei San", 102, 104),
        ("Qing Ying Tang", 176, 178),
        ("Xi Jiao Di Huang Tang", 178, 181),
        ("Yu Nu Jian", 104, 106),
    ]
    
    print(f"\nExtracting {len(priority_formulas)} priority formulas...\n")
    
    extracted_count = 0
    skipped_count = 0
    
    for formula_name, start_page, end_page in priority_formulas:
        # Check if already exists
        file_path = formulas_dir / f"{formula_name}.md"
        if file_path.exists():
            print(f"⊘ Skipping {formula_name} (already exists)")
            skipped_count += 1
            continue
        
        try:
            # Extract text via OCR
            raw_text = extract_formula_pages(pdf, start_page, end_page, formula_name)
            
            # Parse the text
            data = parse_formula_text(raw_text, formula_name)
            
            # Create markdown
            markdown = create_formula_markdown(data, raw_text)
            
            # Write file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            print(f"  ✓ Created {file_path.name}\n")
            extracted_count += 1
            
        except Exception as e:
            print(f"  ✗ ERROR extracting {formula_name}: {e}\n")
    
    pdf.close()
    
    print(f"\n{'='*60}")
    print(f"Extraction complete!")
    print(f"  Extracted: {extracted_count}")
    print(f"  Skipped (already exist): {skipped_count}")
    print(f"  Total: {len(priority_formulas)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
