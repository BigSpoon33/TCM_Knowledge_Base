#!/usr/bin/env python3
"""
Point Code Standardization Script
Converts L.I.-4 → LI-4, S.I.-3 → SI-3 across all files
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple


class PointCodeStandardizer:
    """Standardizes point codes across the knowledge base"""

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.points_dir = self.base_dir / "TCM_Points"
        self.images_dir = self.base_dir / "TCM_Points_Images"

        # Mapping of old → new codes
        self.rename_map = {}  # old_code → new_code

        # Track changes
        self.renamed_files = []
        self.updated_files = []

    def build_rename_map(self):
        """Build mapping of files that need renaming"""
        print("\n🔍 Scanning for files to standardize...")
        print("=" * 80)

        if not self.points_dir.exists():
            print("❌ Points directory not found")
            return

        for file in self.points_dir.glob("*.md"):
            old_name = file.stem

            # Check if it has dots in meridian code
            if re.match(r'^[A-Z]\.[A-Z]\.-\d+$', old_name):
                # L.I.-4 → LI-4
                new_name = old_name.replace('.', '')
                self.rename_map[old_name] = new_name

        print(f"✓ Found {len(self.rename_map)} files to rename")

        if self.rename_map:
            print("\nExamples:")
            for old, new in list(self.rename_map.items())[:5]:
                print(f"  {old} → {new}")

    def rename_point_files(self, dry_run: bool = True):
        """Rename point markdown files"""
        print("\n📝 Renaming point files...")
        print("=" * 80)

        for old_code, new_code in self.rename_map.items():
            old_file = self.points_dir / f"{old_code}.md"
            new_file = self.points_dir / f"{new_code}.md"

            if dry_run:
                print(f"  Would rename: {old_code}.md → {new_code}.md")
            else:
                if old_file.exists():
                    old_file.rename(new_file)
                    self.renamed_files.append((old_code, new_code))
                    print(f"  ✓ Renamed: {old_code}.md → {new_code}.md")

    def update_frontmatter_in_files(self, dry_run: bool = True):
        """Update 'name' field in frontmatter of renamed files"""
        print("\n📋 Updating frontmatter in renamed files...")
        print("=" * 80)

        for old_code, new_code in self.rename_map.items():
            file_path = self.points_dir / f"{new_code if not dry_run else old_code}.md"

            if not file_path.exists():
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Update name field in frontmatter
                match = re.match(r'^(---\s*\n)(.*?)(\n---)', content, re.DOTALL)
                if match:
                    pre = match.group(1)
                    fm_text = match.group(2)
                    post = match.group(3)
                    rest = content[match.end():]

                    # Parse and update
                    fm = yaml.safe_load(fm_text)
                    if fm and 'name' in fm and fm['name'] == old_code:
                        fm['name'] = new_code

                        # Regenerate YAML
                        new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
                        new_content = pre + new_fm + post + rest

                        if dry_run:
                            print(f"  Would update frontmatter: {old_code} → {new_code}")
                        else:
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            print(f"  ✓ Updated frontmatter: {file_path.name}")

            except Exception as e:
                print(f"  ⚠️  Error updating {file_path.name}: {e}")

    def update_wikilinks_in_all_files(self, dry_run: bool = True):
        """Update wikilinks across all markdown files"""
        print("\n🔗 Updating wikilinks in all files...")
        print("=" * 80)

        # Search in all directories
        search_dirs = [
            self.base_dir / "TCM_Diseases",
            self.base_dir / "TCM_Concepts",
            self.base_dir / "TCM_Herbs",
            self.base_dir / "TCM_Techniques",
            self.base_dir / "TCM_Points"
        ]

        updated_count = 0

        for directory in search_dirs:
            if not directory.exists():
                continue

            for file in directory.glob("*.md"):
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        content = f.read()

                    original_content = content
                    changed = False

                    # Replace wikilinks for each renamed point
                    for old_code, new_code in self.rename_map.items():
                        # Pattern: [[L.I.-4]] or [[text (L.I.-4)]]
                        patterns = [
                            (rf'\[\[{re.escape(old_code)}\]\]', f'[[{new_code}]]'),
                            (rf'\[\[([^\]]+)\({re.escape(old_code)}\)\]\]', rf'[[\1({new_code})]]'),
                        ]

                        for pattern, replacement in patterns:
                            if re.search(pattern, content):
                                content = re.sub(pattern, replacement, content)
                                changed = True

                    if changed:
                        if dry_run:
                            print(f"  Would update wikilinks: {file.name}")
                        else:
                            with open(file, 'w', encoding='utf-8') as f:
                                f.write(content)
                            print(f"  ✓ Updated: {file.name}")
                        updated_count += 1

                except Exception as e:
                    print(f"  ⚠️  Error updating {file.name}: {e}")

        print(f"\n✓ {'Would update' if dry_run else 'Updated'} wikilinks in {updated_count} files")

    def rename_image_files(self, dry_run: bool = True):
        """Rename corresponding image files"""
        print("\n🖼️  Renaming image files...")
        print("=" * 80)

        if not self.images_dir.exists():
            print("  No images directory found")
            return

        renamed_count = 0

        for old_code, new_code in self.rename_map.items():
            # Find all image files for this point
            image_patterns = [
                f"{old_code}_*.png",
                f"{old_code}_*.jpg",
                f"{old_code}_*.jpeg"
            ]

            for pattern in image_patterns:
                for image_file in self.images_dir.glob(pattern):
                    # Generate new filename
                    old_name = image_file.name
                    new_name = old_name.replace(old_code, new_code)
                    new_path = image_file.parent / new_name

                    if dry_run:
                        print(f"  Would rename: {old_name} → {new_name}")
                    else:
                        image_file.rename(new_path)
                        print(f"  ✓ Renamed: {old_name} → {new_name}")
                    renamed_count += 1

        print(f"\n✓ {'Would rename' if dry_run else 'Renamed'} {renamed_count} image files")

    def run(self, dry_run: bool = True):
        """Run complete standardization process"""
        print("=" * 80)
        print("🔧 POINT CODE STANDARDIZATION")
        print("=" * 80)

        if dry_run:
            print("\n⚠️  DRY RUN MODE - No changes will be made")
            print("    Run with --execute to apply changes\n")

        self.build_rename_map()

        if not self.rename_map:
            print("\n✅ All point codes already standardized!")
            return

        self.rename_point_files(dry_run)
        self.update_frontmatter_in_files(dry_run)
        self.update_wikilinks_in_all_files(dry_run)
        self.rename_image_files(dry_run)

        print("\n" + "=" * 80)
        print(f"✅ STANDARDIZATION {'PREVIEW' if dry_run else 'COMPLETE'}")
        print("=" * 80)

        if dry_run:
            print("\n💡 To apply these changes, run:")
            print("   python3 standardize_point_codes.py --execute")
            print("\n⚠️  After running, you should:")
            print("   1. Run: python3 auto_sync_frontmatter.py --execute")
            print("   2. Commit changes to git")


def main():
    import sys

    base_dir = Path(__file__).parent.parent
    standardizer = PointCodeStandardizer(base_dir)

    # Check for --execute flag
    dry_run = '--execute' not in sys.argv

    standardizer.run(dry_run)


if __name__ == "__main__":
    main()
