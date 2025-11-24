#!/usr/bin/env python3
"""
Herb-to-Disease Bidirectional Linker
Links herbs to diseases they treat and vice versa.
"""

import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import yaml


class HerbDiseaseLinker:
    """Create bidirectional links between herbs and diseases"""

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.diseases_dir = self.base_dir / "TCM_Diseases"
        self.herbs_dir = self.base_dir / "TCM_Herbs"

        # Maps
        self.disease_map = {}  # disease_name -> file_path
        self.herb_map = {}  # herb_name -> file_path

        # Relationships
        self.disease_to_herbs = defaultdict(set)  # disease -> set of herb names
        self.herb_to_diseases = defaultdict(set)  # herb -> set of disease names
        self.herb_usage_count = defaultdict(int)  # herb -> usage frequency

    def load_files(self):
        """Load all disease and herb files"""
        print("\n📚 Loading files...")
        print("=" * 60)

        # Load diseases
        if self.diseases_dir.exists():
            for file in self.diseases_dir.glob("*.md"):
                if file.stem not in ["TEMPLATE_Disease", "EXAMPLE_Wind_Stroke"]:
                    name = self._extract_name_from_file(file)
                    if name:
                        self.disease_map[name] = file
        print(f"✓ Loaded {len(self.disease_map)} diseases")

        # Load herbs
        if self.herbs_dir.exists():
            for file in self.herbs_dir.glob("*.md"):
                if file.stem != "00 - Single Herb MoC":
                    herb_name = self._extract_herb_name_from_file(file)
                    if herb_name:
                        self.herb_map[herb_name] = file
        print(f"✓ Loaded {len(self.herb_map)} herbs")

    def _extract_name_from_file(self, file_path: Path) -> str:
        """Extract disease name from YAML frontmatter or first heading"""
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Try to get name from YAML frontmatter first
            match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if match:
                frontmatter_text = match.group(1).strip()
                if frontmatter_text:  # Only parse if not empty
                    try:
                        frontmatter = yaml.safe_load(frontmatter_text)
                        if frontmatter and frontmatter.get("name"):
                            return frontmatter["name"]
                    except:
                        pass

            # Fall back to first heading
            heading_match = re.search(r"^#\s+🩺?\s*(.+?)$", content, re.MULTILINE)
            if heading_match:
                return heading_match.group(1).strip()

            # Last resort: use filename
            return file_path.stem.replace("_", " ")
        except Exception:
            pass
        return ""

    def _extract_herb_name_from_file(self, file_path: Path) -> str:
        """Extract herb name from YAML frontmatter or filename"""
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()
            match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if match:
                frontmatter = yaml.safe_load(match.group(1))
                # Try 'name' field first
                name = frontmatter.get("name")
                if name:
                    return name
            # Fall back to filename
            return file_path.stem
        except Exception:
            return file_path.stem

    def extract_herbs_from_diseases(self):
        """Scan disease treatment protocols for herb usage"""
        print("\n🔍 Extracting herbs from disease treatment protocols...")
        print("=" * 60)

        total_relationships = 0

        for disease_name, disease_file in self.disease_map.items():
            with open(disease_file, encoding="utf-8") as f:
                content = f.read()

            # Extract herbs from frontmatter
            match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if match:
                try:
                    frontmatter = yaml.safe_load(match.group(1))
                    herbs = frontmatter.get("herbs", [])

                    if herbs:
                        for herb_name in herbs:
                            # Clean herb name (remove wikilinks and extra info)
                            cleaned_name = self._clean_herb_name(herb_name)

                            if cleaned_name and cleaned_name in self.herb_map:
                                self.disease_to_herbs[disease_name].add(cleaned_name)
                                self.herb_to_diseases[cleaned_name].add(disease_name)
                                self.herb_usage_count[cleaned_name] += 1
                                total_relationships += 1

                except Exception as e:
                    print(f"  ⚠️  Error parsing {disease_name}: {e}")

        print(f"✓ Found {total_relationships} herb-disease relationships")
        print(f"✓ {len(self.herb_to_diseases)} unique herbs used")

    def _clean_herb_name(self, herb_str: str) -> str:
        """Clean herb name from various formats"""
        # Remove wikilink brackets: [[Herb]] -> Herb
        herb_str = herb_str.replace("[[", "").replace("]]", "")
        herb_str = herb_str.strip()
        return herb_str

    def update_herb_files_with_diseases(self):
        """Add disease relationships to herb frontmatter"""
        print("\n📝 Updating herb files with disease relationships...")
        print("=" * 60)

        updated_count = 0

        for herb_name, diseases in self.herb_to_diseases.items():
            herb_file = self.herb_map.get(herb_name)
            if herb_file:
                self._update_file_frontmatter(herb_file, "treats_diseases", sorted(list(diseases)))
                print(f"  ✓ {herb_name}: Added {len(diseases)} disease links")
                updated_count += 1

        print(f"\n✓ Updated {updated_count} herb files")

    def _update_file_frontmatter(self, file_path: Path, field_name: str, values: list[str]):
        """Update a specific field in YAML frontmatter"""
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        # Parse frontmatter
        match = re.match(r"^(---\s*\n)(.*?)(\n---)", content, re.DOTALL)
        if match:
            pre = match.group(1)
            fm_content = match.group(2)
            post = match.group(3)
            rest = content[match.end() :]

            # Parse YAML
            frontmatter = yaml.safe_load(fm_content)

            # Update field
            frontmatter[field_name] = values
            frontmatter["updated"] = datetime.now().strftime("%Y-%m-%d")

            # Reconstruct YAML
            new_fm = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)

            # Write back
            new_content = pre + new_fm + post + rest
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)

    def add_herb_wikilinks_to_diseases(self):
        """Add wikilinks to herbs in disease files"""
        print("\n🔗 Adding herb wikilinks to disease files...")
        print("=" * 60)

        updated_count = 0

        for disease_name, herbs in self.disease_to_herbs.items():
            disease_file = self.disease_map.get(disease_name)
            if disease_file:
                with open(disease_file, encoding="utf-8") as f:
                    original_content = f.read()

                # Add wikilinks to herb names in the content
                modified_content = self.add_wikilinks_to_content(original_content, self.herb_map)

                if modified_content != original_content:
                    with open(disease_file, "w", encoding="utf-8") as f:
                        f.write(modified_content)
                    print(f"  ✓ Updated: {disease_name}")
                    updated_count += 1

        print(f"\n✓ Updated {updated_count} disease files with herb wikilinks")

    def add_wikilinks_to_content(self, content: str, entity_map: dict[str, Path]) -> str:
        """Add wikilinks to entity mentions in content"""
        for entity_name in sorted(entity_map.keys(), key=len, reverse=True):
            # Skip if already wikilinked
            if f"[[{entity_name}]]" in content:
                continue

            # Create patterns to match
            patterns = [
                rf"\b{re.escape(entity_name)}\b",
            ]

            for pattern in patterns:
                content = re.sub(pattern, f"[[{entity_name}]]", content, flags=re.IGNORECASE)

        return content

    def generate_statistics(self):
        """Generate and print usage statistics"""
        print("\n📊 Herb Usage Statistics")
        print("=" * 60)

        # Most frequently used herbs
        if self.herb_usage_count:
            sorted_herbs = sorted(self.herb_usage_count.items(), key=lambda x: x[1], reverse=True)
            print("\n🔝 Most Frequently Used Herbs:")
            for herb, count in sorted_herbs[:20]:
                diseases = self.herb_to_diseases[herb]
                print(f"  {herb}: {count} uses in {len(diseases)} diseases")

        # Total statistics
        print("\n📈 Total Statistics:")
        print(f"  Total herb-disease relationships: {sum(self.herb_usage_count.values())}")
        print(f"  Herbs used in treatments: {len(self.herb_to_diseases)}")
        print(f"  Diseases with herb protocols: {len(self.disease_to_herbs)}")
        if len(self.disease_to_herbs) > 0:
            print(
                f"  Average herbs per disease: {sum(self.herb_usage_count.values()) / len(self.disease_to_herbs):.1f}"
            )

    def run(self):
        """Run the complete linking process"""
        print("=" * 60)
        print("🔗 HERB-DISEASE BIDIRECTIONAL LINKER")
        print("=" * 60)

        self.load_files()
        self.extract_herbs_from_diseases()
        self.update_herb_files_with_diseases()
        self.add_herb_wikilinks_to_diseases()
        self.generate_statistics()

        print("\n" + "=" * 60)
        print("✅ HERB-DISEASE LINKING COMPLETE")
        print("=" * 60)


def main():
    base_dir = Path(__file__).parent.parent
    linker = HerbDiseaseLinker(base_dir)
    linker.run()


if __name__ == "__main__":
    main()
