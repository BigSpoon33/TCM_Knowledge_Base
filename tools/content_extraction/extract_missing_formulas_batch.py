#!/usr/bin/env python3
"""
Batch extract missing NCCAOM formulas from Bensky Formulas & Strategies
Uses the existing OCR extraction script
"""

import subprocess
import sys
from pathlib import Path

# Priority formulas with page numbers from Scheid/Bensky Formulas & Strategies 2nd ed.
PRIORITY_FORMULAS = [
    # Release the Exterior
    {"name": "Ma Huang Tang", "pages": (23, 29), "priority": 1},
    {"name": "Sang Ju Yin", "pages": (135, 138), "priority": 1},
    {"name": "Xiao Qing Long Tang", "pages": (44, 48), "priority": 1},
    {"name": "Cong Chi Tang", "pages": (14, 16), "priority": 3},
    {"name": "Gui Zhi Jia Hou Po Xing Zi Tang", "pages": (36, 38), "priority": 3},
    {"name": "Gui Zhi Ma Huang Ge Ban Tang", "pages": (34, 36), "priority": 3},
    {"name": "Jia Jian Wei Rui Tang", "pages": (144, 146), "priority": 3},
    {"name": "Xin Yi San", "pages": (48, 50), "priority": 2},
    # Clear Heat
    {"name": "Bai Tou Weng Tang", "pages": (112, 115), "priority": 1},
    {"name": "Dao Chi San", "pages": (91, 93), "priority": 1},
    {"name": "San Huang Xie Xin Tang", "pages": (106, 109), "priority": 1},
    {"name": "An Gong Niu Huang Wan", "pages": (196, 199), "priority": 2},
    {"name": "Shao Yao Tang", "pages": (115, 118), "priority": 2},
    {"name": "Xie Bai San", "pages": (93, 95), "priority": 3},
    {"name": "Xie Huang San", "pages": (95, 97), "priority": 3},
    {"name": "Zhi Zi Chi Tang", "pages": (74, 77), "priority": 2},
    # Harmonize
    {"name": "Da Chai Hu Tang", "pages": (239, 241), "priority": 1},
    {"name": "Dan Zhi Xiao Yao San", "pages": (258, 259), "priority": 1},
    # Drain Downward
    {"name": "Da Xian Xiong Tang", "pages": (275, 279), "priority": 2},
    {"name": "Ji Chuan Jian", "pages": (287, 289), "priority": 3},
    # Expel Dampness
    {"name": "Er Miao San", "pages": (362, 364), "priority": 2},
    {"name": "Si Miao San", "pages": (364, 366), "priority": 2},
    {"name": "Wu Pi San", "pages": (344, 346), "priority": 3},
    # Warm Interior
    {"name": "Fu Zi Li Zhong Wan", "pages": (432, 434), "priority": 2},
    # Tonify
    {"name": "Gui Zhi Jia Long Gu Mu Li Tang", "pages": (937, 940), "priority": 2},
    {"name": "Ren Shen Ge Jie San", "pages": (688, 690), "priority": 3},
    {"name": "Ren Shen Hu Tao Tang", "pages": (691, 693), "priority": 3},
    # Regulate Qi
    {"name": "Jin Ling Zi San", "pages": (523, 525), "priority": 3},
    {"name": "Liang Fu Wan", "pages": (525, 527), "priority": 3},
    {"name": "Mu Xiang Bing Lang Wan", "pages": (504, 507), "priority": 2},
    # Invigorate Blood
    {"name": "Die Da Wan", "pages": (642, 644), "priority": 3},
    {"name": "Sheng Hua Tang", "pages": (610, 613), "priority": 1},
    {"name": "Shi Xiao San", "pages": (617, 619), "priority": 2},
    # Stop Bleeding
    {"name": "Huai Hua San", "pages": (1026, 1028), "priority": 2},
    {"name": "Shi Hui San", "pages": (1028, 1030), "priority": 2},
    {"name": "Xiao Ji Yin Zi", "pages": (1034, 1037), "priority": 2},
    {"name": "Yun Nan Bai Yao", "pages": (1030, 1032), "priority": 3},
    # Expel Wind
    {"name": "Da Qin Jiao Tang", "pages": (757, 760), "priority": 2},
    {"name": "Ding Xian Wan", "pages": (913, 916), "priority": 2},
    {"name": "Qian Zheng San", "pages": (899, 901), "priority": 2},
    {"name": "Xiao Huo Luo Dan", "pages": (751, 753), "priority": 2},
    {"name": "Yu Zhen San", "pages": (896, 898), "priority": 3},
    {"name": "Zhen Gan Xi Feng Tang", "pages": (920, 922), "priority": 1},
    # Reduce Food Stagnation
    {"name": "Jian Pi Wan", "pages": (495, 497), "priority": 2},
    {"name": "Zhi Shi Dao Zhi Wan", "pages": (497, 499), "priority": 3},
    # Stabilize and Bind
    {"name": "Gu Chong Tang", "pages": (1071, 1074), "priority": 2},
    {"name": "Gu Jing Wan", "pages": (1074, 1076), "priority": 2},
    {"name": "Mu Li San", "pages": (1064, 1066), "priority": 2},
    {"name": "Sang Piao Xiao San", "pages": (1054, 1056), "priority": 2},
    {"name": "Shui Lu Er Xian Dan", "pages": (1082, 1084), "priority": 3},
    {"name": "Si Shen Wan", "pages": (1042, 1045), "priority": 2},
    {"name": "Suo Quan Wan", "pages": (1051, 1053), "priority": 2},
    {"name": "Wan Dai Tang", "pages": (1086, 1088), "priority": 2},
]


def formula_exists(formula_name):
    """Check if formula file already exists"""
    formula_path = Path("TCM_Formulas") / f"{formula_name}.md"
    return formula_path.exists()


def extract_formula(formula_data, pdf_path, dry_run=False, overwrite=False):
    """Extract a single formula using the OCR script"""
    name = formula_data["name"]
    start_page, end_page = formula_data["pages"]
    priority = formula_data.get("priority", 2)

    if formula_exists(name) and not overwrite:
        print(f"  ✓ {name} already exists, skipping")
        return True

    print(f"\n{'=' * 60}")
    print(f"Extracting: {name}")
    print(f"Pages: {start_page}-{end_page} | Priority: {priority}")
    print(f"{'=' * 60}")

    if dry_run:
        print("  [DRY RUN] Would extract this formula")
        return True

    cmd = [
        "python3",
        "scripts/extract_formulas_bensky_ocr.py",
        "--pdf",
        pdf_path,
        "--formula",
        name,
        "--start-page",
        str(start_page),
        "--end-page",
        str(end_page),
        "--overwrite",
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        print(f"  ✓ {name} extracted successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Error extracting {name}:")
        print(e.stderr)
        return False


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Batch extract missing NCCAOM formulas")
    parser.add_argument(
        "--pdf", default="Books/Bensky - Formulas and Strategies, 2nd Edition-1.pdf", help="Path to Bensky Formulas PDF"
    )
    parser.add_argument(
        "--priority", type=int, choices=[1, 2, 3], help="Only extract formulas of this priority (1=highest)"
    )
    parser.add_argument("--dry-run", action="store_true", help="Show what would be extracted without actually doing it")
    parser.add_argument("--limit", type=int, help="Limit number of formulas to extract")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")

    args = parser.parse_args()

    # Filter formulas by priority if specified
    formulas = PRIORITY_FORMULAS
    if args.priority:
        formulas = [f for f in formulas if f.get("priority") == args.priority]
        print(f"\nFiltering for Priority {args.priority} formulas: {len(formulas)} total")

    # Apply limit if specified
    if args.limit:
        formulas = formulas[: args.limit]
        print(f"Limiting to first {args.limit} formulas")

    print(f"\n{'=' * 60}")
    print("BATCH FORMULA EXTRACTION")
    print(f"{'=' * 60}")
    print(f"Total formulas to process: {len(formulas)}")
    print(f"PDF: {args.pdf}")
    print(f"Dry run: {args.dry_run}")
    print(f"{'=' * 60}\n")

    # Check which formulas already exist
    if args.overwrite:
        existing = []
        missing = formulas
        print("Overwrite mode: all formulas will be processed")
    else:
        existing = [f["name"] for f in formulas if formula_exists(f["name"])]
        missing = [f for f in formulas if not formula_exists(f["name"])]

    print("\nStatus check:")
    print(f"  Already exist: {len(existing)}")
    print(f"  Need to extract: {len(missing)}")

    if existing:
        print("\nExisting formulas (will skip):")
        for name in existing[:10]:  # Show first 10
            print(f"  ✓ {name}")
        if len(existing) > 10:
            print(f"  ... and {len(existing) - 10} more")

    if not missing:
        print("\n✓ All formulas already extracted!")
        return 0

    print(f"\nFormulas to extract ({len(missing)}):")
    for f in missing:
        print(f"  • {f['name']} (Priority {f.get('priority', 2)})")

    if args.dry_run:
        print("\n[DRY RUN] No formulas will be extracted")
        return 0

    # Confirm before proceeding
    if not args.dry_run:
        response = "y"  # Auto-confirm in batch mode
        if response.lower() != "y":
            print("Cancelled")
            return 0

    # Extract formulas
    success_count = 0
    fail_count = 0

    for i, formula_data in enumerate(missing, 1):
        print(f"\n[{i}/{len(missing)}]", end=" ")
        if extract_formula(formula_data, args.pdf, args.dry_run, args.overwrite):
            success_count += 1
        else:
            fail_count += 1

    # Summary
    print(f"\n{'=' * 60}")
    print("EXTRACTION COMPLETE")
    print(f"{'=' * 60}")
    print(f"Success: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Total: {len(missing)}")
    print(f"{'=' * 60}\n")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
