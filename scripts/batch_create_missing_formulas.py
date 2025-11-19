#!/usr/bin/env python3
"""
Batch create missing NCCAOM formulas from Chen book
"""

import fitz
from pathlib import Path
from datetime import datetime
import re


# Map of missing formulas to search for
MISSING_FORMULAS = {
    # Release the Exterior
    "Sang Ju Yin": {"aliases": ["Mulberry Leaf and Chrysanthemum"], "category": "Release Exterior"},
    "Xiao Qing Long Tang": {"aliases": ["Minor Blue-Green Dragon"], "category": "Release Exterior"},
    "Cong Chi Tang": {"aliases": ["Scallion and Prepared Soybean"], "category": "Release Exterior"},
    "Gui Zhi Jia Hou Po Xing Zi Tang": {"aliases": ["Cinnamon Twig plus Magnolia"], "category": "Release Exterior"},
    "Gui Zhi Ma Huang Ge Ban Tang": {"aliases": ["Cinnamon Twig and Ephedra Half"], "category": "Release Exterior"},
    "Jia Jian Wei Rui Tang": {"aliases": ["Modified Polygonatum"], "category": "Release Exterior"},
    "Xin Yi San": {"aliases": ["Magnolia Flower Powder"], "category": "Release Exterior"},
    
    # Clear Heat
    "Bai Tou Weng Tang": {"aliases": ["Pulsatilla"], "category": "Clear Heat"},
    "Dao Chi San": {"aliases": ["Guide Out the Red"], "category": "Clear Heat"},
    "San Huang Xie Xin Tang": {"aliases": ["Three-Yellow Drain Epigastrium"], "category": "Clear Heat"},
    "An Gong Niu Huang Wan": {"aliases": ["Calm Palace with Cattle Gallstone"], "category": "Clear Heat"},
    "Shao Yao Tang": {"aliases": ["Peony Decoction"], "category": "Clear Heat"},
    "Xie Bai San": {"aliases": ["Drain the White"], "category": "Clear Heat"},
    "Xie Huang San": {"aliases": ["Drain the Yellow"], "category": "Clear Heat"},
    "Zhi Zi Chi Tang": {"aliases": ["Gardenia and Prepared Soybean"], "category": "Clear Heat"},
    
    # Harmonize
    "Da Chai Hu Tang": {"aliases": ["Major Bupleurum"], "category": "Harmonize"},
    "Dan Zhi Xiao Yao San": {"aliases": ["Moutan and Gardenia Rambling"], "category": "Harmonize"},
    
    # Drain Downward
    "Da Xian Xiong Tang": {"aliases": ["Major Sinking into Chest"], "category": "Drain Downward"},
    "Ji Chuan Jian": {"aliases": ["Benefit the River Flow"], "category": "Drain Downward"},
    
    # Expel Dampness
    "Er Miao San": {"aliases": ["Two-Marvel Powder"], "category": "Expel Dampness"},
    "Si Miao San": {"aliases": ["Four-Marvel Powder"], "category": "Expel Dampness"},
    "Wu Pi San": {"aliases": ["Five-Peel Powder"], "category": "Expel Dampness"},
    
    # Warm Interior
    "Fu Zi Li Zhong Wan": {"aliases": ["Aconite Regulate Middle"], "category": "Warm Interior"},
    
    # Tonify
    "Gui Zhi Jia Long Gu Mu Li Tang": {"aliases": ["Cinnamon Twig plus Dragon Bone"], "category": "Tonify"},
    "Ren Shen Ge Jie San": {"aliases": ["Ginseng and Gecko Powder"], "category": "Tonify"},
    "Ren Shen Hu Tao Tang": {"aliases": ["Ginseng and Walnut"], "category": "Tonify"},
    
    # Regulate Qi
    "Jin Ling Zi San": {"aliases": ["Melia Toosendan Powder"], "category": "Regulate Qi"},
    "Liang Fu Wan": {"aliases": ["Alpinia and Cyperus Pill"], "category": "Regulate Qi"},
    "Mu Xiang Bing Lang Wan": {"aliases": ["Aucklandia and Areca"], "category": "Regulate Qi"},
    
    # Invigorate Blood
    "Die Da Wan": {"aliases": ["Trauma Pill"], "category": "Invigorate Blood"},
    "Sheng Hua Tang": {"aliases": ["Generating and Transforming"], "category": "Invigorate Blood"},
    "Shi Xiao San": {"aliases": ["Sudden Smile Powder"], "category": "Invigorate Blood"},
    
    # Stop Bleeding
    "Huai Hua San": {"aliases": ["Sophora Flower"], "category": "Stop Bleeding"},
    "Shi Hui San": {"aliases": ["Ten Partially-Charred"], "category": "Stop Bleeding"},
    "Xiao Ji Yin Zi": {"aliases": ["Small Thistle"], "category": "Stop Bleeding"},
    "Yun Nan Bai Yao": {"aliases": ["Yunnan White Medicine"], "category": "Stop Bleeding"},
    
    # Expel Wind
    "Da Qin Jiao Tang": {"aliases": ["Major Gentiana Macrophylla"], "category": "Expel Wind"},
    "Ding Xian Wan": {"aliases": ["Arrest Seizures"], "category": "Expel Wind"},
    "Qian Zheng San": {"aliases": ["Lead to Symmetry"], "category": "Expel Wind"},
    "Xiao Huo Luo Dan": {"aliases": ["Minor Invigorate Collaterals"], "category": "Expel Wind"},
    "Yu Zhen San": {"aliases": ["True Jade"], "category": "Expel Wind"},
    "Zhen Gan Xi Feng Tang": {"aliases": ["Sedate Liver Extinguish Wind"], "category": "Expel Wind"},
    
    # Food Stagnation
    "Jian Pi Wan": {"aliases": ["Strengthen Spleen"], "category": "Food Stagnation"},
    "Zhi Shi Dao Zhi Wan": {"aliases": ["Immature Bitter Orange"], "category": "Food Stagnation"},
    
    # Stabilize and Bind
    "Gu Chong Tang": {"aliases": ["Stabilize Gushing"], "category": "Stabilize"},
    "Gu Jing Wan": {"aliases": ["Stabilize Menses"], "category": "Stabilize"},
    "Mu Li San": {"aliases": ["Oyster Shell Powder"], "category": "Stabilize"},
    "Sang Piao Xiao San": {"aliases": ["Mantis Egg-Case"], "category": "Stabilize"},
    "Shui Lu Er Xian Dan": {"aliases": ["Water and Land Two-Immortal"], "category": "Stabilize"},
    "Si Shen Wan": {"aliases": ["Four-Miracle Pill"], "category": "Stabilize"},
    "Suo Quan Wan": {"aliases": ["Shut the Sluice"], "category": "Stabilize"},
    "Wan Dai Tang": {"aliases": ["End Discharge"], "category": "Stabilize"},
}


def find_formula_in_chen(pdf, formula_name, aliases):
    """Find formula in Chen book and return page number and text"""
    search_terms = [formula_name] + aliases
    
    for page_num in range(len(pdf)):
        page = pdf[page_num]
        text = page.get_text()
        lines = text.split('\n')
        
        # Look for formula name as heading
        for i, line in enumerate(lines):
            for term in search_terms:
                if term.lower() in line.lower() and len(line) < 100:
                    # Check if it's a section heading (has content after it)
                    context_lines = lines[i:min(len(lines), i+20)]
                    if any(len(l) > 50 for l in context_lines[1:10]):  # Has substantial content
                        # Extract 3-4 pages
                        full_text = ""
                        for p in range(page_num, min(page_num + 4, len(pdf))):
                            full_text += pdf[p].get_text() + "\n\n"
                        return page_num + 1, full_text
    
    return None, None


def create_basic_formula_file(name, category, aliases, page, text):
    """Create a basic formula markdown file"""
    today = datetime.now().strftime("%Y%m%d%H%M%S")
    
    content = f"""---
id: formula-{today}
name: "{name}"
type: formula
category:
  - {category}
aliases:
{chr(10).join(['  - ' + a for a in aliases])}
tags:
  - TCM
  - Formula
  - NCCAOM
herbs: []
chief_herbs: []
actions: []
source: Chen - Chinese Herbal Formulas and Applications
source_page: "{page}"
updated: {datetime.now().strftime("%Y-%m-%d")}
stock: true
---

# {name}
## {aliases[0] if aliases else ''}

## 📖 Source Reference
Chen - Chinese Herbal Formulas and Applications, page {page}

## 🌿 Composition & Dosages

*Note: Please review Chen book pages {page}-{page+2} for complete composition and dosages*

## 🎯 Clinical Applications

### Primary Pattern & Manifestations

*Information to be added from source text*

## 📋 Key Diagnostic Signs

- **Tongue**: [Review source]
- **Pulse**: [Review source]

## ⚕️ Modifications

*Review source text for modifications*

## ⚠️ Contraindications & Cautions

*Review source text for safety information*

## 📚 Clinical Notes

**Source Text Reference:**
Page {page} in Chen - Chinese Herbal Formulas and Applications

*Note: This is a template created from automated extraction. Please review the source text to add specific details about composition, dosages, and clinical applications.*

---

*Created: {datetime.now().strftime("%Y-%m-%d")}*
*Source: Automated extraction from Chen book*
"""
    
    return content


def main():
    pdf_path = "Books/Chinese Herbal Formulas and Applications Pharmacological Effects Clinical Research by John K. Chen Tina T. Chen Minh Nguyen Lily Huang Jimmy Chang Rick Friesen Chien-Hui Liao (z-lib.org).pdf"
    
    print("Opening Chen book...")
    pdf = fitz.open(pdf_path)
    print(f"✓ Loaded PDF ({len(pdf)} pages)\n")
    
    print(f"Processing {len(MISSING_FORMULAS)} formulas...\n")
    
    created = []
    not_found = []
    already_exist = []
    
    for i, (name, info) in enumerate(MISSING_FORMULAS.items(), 1):
        # Check if already exists
        filepath = Path("TCM_Formulas") / f"{name}.md"
        if filepath.exists():
            already_exist.append(name)
            print(f"[{i}/{len(MISSING_FORMULAS)}] ✓ {name} - already exists")
            continue
        
        print(f"[{i}/{len(MISSING_FORMULAS)}] Searching for {name}...", end=" ")
        
        page, text = find_formula_in_chen(pdf, name, info.get("aliases", []))
        
        if page:
            print(f"✓ Found on page {page}")
            content = create_basic_formula_file(
                name, 
                info["category"],
                info.get("aliases", []),
                page,
                text
            )
            filepath.write_text(content, encoding='utf-8')
            created.append(name)
        else:
            print(f"✗ Not found")
            not_found.append(name)
    
    pdf.close()
    
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Created: {len(created)}")
    print(f"Already existed: {len(already_exist)}")
    print(f"Not found: {len(not_found)}")
    print(f"Total processed: {len(MISSING_FORMULAS)}")
    
    if not_found:
        print(f"\nNot found in Chen book ({len(not_found)}):")
        for name in not_found:
            print(f"  - {name}")
    
    print(f"\n✓ Batch creation complete!")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
