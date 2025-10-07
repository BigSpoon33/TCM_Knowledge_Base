#!/usr/bin/env python3
"""
Point-to-Disease Bidirectional Linker
Links acupuncture points to diseases they treat and vice versa.
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict
from datetime import datetime


class PointDiseaseLinker:
    """Create bidirectional links between points and diseases"""

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.diseases_dir = self.base_dir / "TCM_Diseases"
        self.points_dir = self.base_dir / "TCM_Points"

        # Maps
        self.disease_map = {}  # disease_name -> file_path
        self.point_map = {}    # point_code -> file_path

        # Relationships
        self.disease_to_points = defaultdict(set)  # disease -> set of point codes
        self.point_to_diseases = defaultdict(set)  # point -> set of disease names
        self.point_usage_count = defaultdict(int)  # point -> usage frequency

    def load_files(self):
        """Load all disease and point files"""
        print("\n📚 Loading files...")
        print("=" * 60)

        # Load diseases
        if self.diseases_dir.exists():
            for file in self.diseases_dir.glob("*.md"):
                if file.stem != "TEMPLATE_Disease":
                    name = self._extract_name_from_file(file)
                    if name:
                        self.disease_map[name] = file
        print(f"✓ Loaded {len(self.disease_map)} diseases")

        # Load points
        if self.points_dir.exists():
            for file in self.points_dir.glob("*.md"):
                point_code = self._extract_point_code_from_file(file)
                if point_code:
                    self.point_map[point_code] = file
        print(f"✓ Loaded {len(self.point_map)} acupuncture points")

    def _extract_name_from_file(self, file_path: Path) -> str:
        """Extract name from YAML frontmatter or first heading"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Try to get name from YAML frontmatter first
            match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                frontmatter_text = match.group(1).strip()
                if frontmatter_text:  # Only parse if not empty
                    try:
                        frontmatter = yaml.safe_load(frontmatter_text)
                        if frontmatter and frontmatter.get('name'):
                            return frontmatter['name']
                    except:
                        pass

            # Fall back to first heading
            heading_match = re.search(r'^#\s+🩺?\s*(.+?)$', content, re.MULTILINE)
            if heading_match:
                return heading_match.group(1).strip()

            # Last resort: use filename
            return file_path.stem.replace('_', ' ')
        except Exception:
            pass
        return ""

    def _extract_point_code_from_file(self, file_path: Path) -> str:
        """Extract point code from YAML frontmatter or filename"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                frontmatter = yaml.safe_load(match.group(1))
                # Try 'name' field first, then 'point_code', finally filename
                code = frontmatter.get('name') or frontmatter.get('point_code') or file_path.stem
                return code
            # Fall back to filename if no frontmatter
            return file_path.stem
        except Exception as e:
            # Silently fall back to filename
            return file_path.stem

    def extract_points_from_diseases(self):
        """Scan disease treatment protocols for point usage"""
        print("\n🔍 Extracting points from disease treatment protocols...")
        print("=" * 60)

        total_relationships = 0

        for disease_name, disease_file in self.disease_map.items():
            with open(disease_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract points from frontmatter
            match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                try:
                    frontmatter = yaml.safe_load(match.group(1))
                    points = frontmatter.get('points', [])

                    if points:
                        for point_code in points:
                            # Clean point code (remove parentheses and extra info)
                            cleaned_code = self._clean_point_code(point_code)

                            if cleaned_code and cleaned_code in self.point_map:
                                self.disease_to_points[disease_name].add(cleaned_code)
                                self.point_to_diseases[cleaned_code].add(disease_name)
                                self.point_usage_count[cleaned_code] += 1
                                total_relationships += 1

                except Exception as e:
                    print(f"  ⚠️  Error parsing {disease_name}: {e}")

        print(f"✓ Found {total_relationships} point-disease relationships")
        print(f"✓ {len(self.point_to_diseases)} unique points used")

    def _clean_point_code(self, point_str: str) -> str:
        """Clean point code from various formats"""
        # Remove parentheses and everything inside them
        # e.g., "Baihui (Du 20)" -> "Du 20" -> "DU-20"
        # e.g., "[[DU-20]]" -> "DU-20"

        # Remove wikilink brackets
        point_str = point_str.replace('[[', '').replace(']]', '')

        # Extract from parentheses if present
        paren_match = re.search(r'\((.*?)\)', point_str)
        if paren_match:
            point_str = paren_match.group(1)

        # Convert space to hyphen if needed
        # "Du 20" -> "DU-20"
        point_str = point_str.strip()

        # Standardize format
        parts = point_str.replace('-', ' ').split()
        if len(parts) == 2:
            meridian, number = parts
            # Standardize meridian code
            meridian = meridian.upper()
            return f"{meridian}-{number}"

        return point_str

    def update_point_files_with_diseases(self):
        """Add disease relationships to point frontmatter"""
        print("\n📝 Updating point files with disease relationships...")
        print("=" * 60)

        updated_count = 0

        for point_code, diseases in self.point_to_diseases.items():
            point_file = self.point_map.get(point_code)
            if point_file:
                self._update_file_frontmatter(
                    point_file,
                    'treats_diseases',
                    sorted(list(diseases))
                )
                updated_count += 1
                print(f"  ✓ {point_code}: Added {len(diseases)} disease links")

        print(f"\n✓ Updated {updated_count} point files")

    def _update_file_frontmatter(self, file_path: Path, field: str, values: List[str]):
        """Update a specific field in YAML frontmatter"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract frontmatter and body
        match = re.match(r'^(---\s*\n)(.*?)(\n---\s*\n)(.*)', content, re.DOTALL)
        if not match:
            print(f"  ⚠️  No frontmatter found in {file_path.name}")
            return

        yaml_start, yaml_content, yaml_end, body = match.groups()

        # Parse YAML
        try:
            frontmatter = yaml.safe_load(yaml_content)
        except Exception as e:
            print(f"  ⚠️  Error parsing YAML in {file_path.name}: {e}")
            return

        # Update field
        frontmatter[field] = values

        # Add updated timestamp
        frontmatter['updated'] = datetime.now().strftime("%Y-%m-%d")

        # Write back
        new_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
        new_content = f"{yaml_start}{new_yaml}{yaml_end}{body}"

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

    def generate_statistics(self):
        """Generate usage statistics"""
        print("\n📊 Point Usage Statistics")
        print("=" * 60)

        # Sort by usage frequency
        usage_sorted = sorted(
            self.point_usage_count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        print("\n🔝 Most Frequently Used Points:")
        for point_code, count in usage_sorted[:20]:
            diseases = self.point_to_diseases[point_code]
            print(f"  {point_code}: {count} uses in {len(diseases)} diseases")

        print(f"\n📈 Total Statistics:")
        print(f"  Total point-disease relationships: {sum(self.point_usage_count.values())}")
        print(f"  Points used in treatments: {len(self.point_to_diseases)}")
        print(f"  Diseases with point protocols: {len(self.disease_to_points)}")
        if len(self.disease_to_points) > 0:
            print(f"  Average points per disease: {sum(self.point_usage_count.values()) / len(self.disease_to_points):.1f}")

        return usage_sorted

    def add_point_wikilinks_to_diseases(self):
        """Add [[wikilinks]] for points in disease content"""
        print("\n🔗 Adding point wikilinks to disease files...")
        print("=" * 60)

        updated_count = 0

        for disease_name, disease_file in self.disease_map.items():
            with open(disease_file, 'r', encoding='utf-8') as f:
                original_content = f.read()

            modified_content = original_content

            # Get points used in this disease
            points = self.disease_to_points.get(disease_name, set())

            # Add wikilinks for each point
            for point_code in points:
                # Only link if not already linked
                if f"[[{point_code}]]" not in modified_content:
                    # Pattern to match point code not already in wikilinks
                    # Match things like "Du 20", "DU-20", "Du-20" but not in [[]]
                    patterns = [
                        rf'(?<!\[\[)\b{re.escape(point_code)}\b(?!\]\])',
                        rf'(?<!\[\[)\b{re.escape(point_code.replace("-", " "))}\b(?!\]\])',
                    ]

                    for pattern in patterns:
                        # Split content to avoid frontmatter
                        parts = modified_content.split('---', 2)
                        if len(parts) == 3:
                            frontmatter, _, body = parts

                            # Only modify body
                            body_modified = re.sub(
                                pattern,
                                f"[[{point_code}]]",
                                body,
                                count=5,  # Limit to first 5 occurrences
                                flags=re.IGNORECASE
                            )

                            modified_content = f"---{frontmatter}---{body_modified}"

            # Write if changed
            if modified_content != original_content:
                with open(disease_file, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                updated_count += 1
                print(f"  ✓ Updated: {disease_name}")

        print(f"\n✓ Updated {updated_count} disease files with point wikilinks")

    def run(self):
        """Execute complete point-disease linking process"""
        print("\n" + "=" * 60)
        print("🔗 POINT-DISEASE BIDIRECTIONAL LINKER")
        print("=" * 60)

        # Step 1: Load files
        self.load_files()

        # Step 2: Extract relationships
        self.extract_points_from_diseases()

        # Step 3: Update point files
        self.update_point_files_with_diseases()

        # Step 4: Add wikilinks to diseases
        self.add_point_wikilinks_to_diseases()

        # Step 5: Statistics
        self.generate_statistics()

        print("\n" + "=" * 60)
        print("✅ POINT-DISEASE LINKING COMPLETE")
        print("=" * 60)


def main():
    base_dir = Path(__file__).parent.parent
    linker = PointDiseaseLinker(base_dir)
    linker.run()


if __name__ == "__main__":
    main()
