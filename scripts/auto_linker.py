#!/usr/bin/env python3
"""
Automated Cross-Linker for TCM Knowledge Base
Scans all files and creates bidirectional wikilinks based on content analysis.
"""

import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import yaml


class TCMAutoLinker:
    """Automatically create cross-links between TCM knowledge base files"""

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.concepts_dir = self.base_dir / "TCM_Concepts"
        self.diseases_dir = self.base_dir / "TCM_Diseases"
        self.techniques_dir = self.base_dir / "TCM_Techniques"
        self.points_dir = self.base_dir / "Acupuncture Points"
        self.herbs_dir = self.base_dir / "TCM_Herbs"

        # Knowledge maps
        self.concept_map = {}  # concept_name -> file_path
        self.disease_map = {}  # disease_name -> file_path
        self.technique_map = {}  # technique_name -> file_path

        # Relationship tracking
        self.relationships = defaultdict(lambda: defaultdict(set))

    def load_knowledge_base(self):
        """Load all entity names and file paths"""
        print("\n📚 Loading knowledge base...")
        print("=" * 60)

        # Load concepts
        if self.concepts_dir.exists():
            for file in self.concepts_dir.glob("*.md"):
                if file.stem != "TEMPLATE_Concept":
                    name = self._extract_name_from_file(file)
                    if name:
                        self.concept_map[name] = file
        print(f"✓ Loaded {len(self.concept_map)} concepts")

        # Load diseases
        if self.diseases_dir.exists():
            for file in self.diseases_dir.glob("*.md"):
                if file.stem != "TEMPLATE_Disease":
                    name = self._extract_name_from_file(file)
                    if name:
                        self.disease_map[name] = file
        print(f"✓ Loaded {len(self.disease_map)} diseases")

        # Load techniques
        if self.techniques_dir.exists():
            for file in self.techniques_dir.glob("*.md"):
                if file.stem != "TEMPLATE_Technique":
                    name = self._extract_name_from_file(file)
                    if name:
                        self.technique_map[name] = file
        print(f"✓ Loaded {len(self.technique_map)} techniques")

    def _extract_name_from_file(self, file_path: Path) -> str:
        """Extract the name field from YAML frontmatter"""
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Extract YAML frontmatter
            match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if match:
                frontmatter = yaml.safe_load(match.group(1))
                return frontmatter.get("name", "")
        except Exception as e:
            print(f"  ⚠️  Error reading {file_path.name}: {e}")
        return ""

    def scan_for_concept_mentions(self):
        """Scan disease files for mentions of concepts"""
        print("\n🔍 Scanning for concept mentions in diseases...")
        print("=" * 60)

        for disease_name, disease_file in self.disease_map.items():
            with open(disease_file, encoding="utf-8") as f:
                content = f.read()

            # Search for concept mentions in content
            for concept_name in self.concept_map.keys():
                # Create regex patterns for detection
                patterns = [
                    rf"\b{re.escape(concept_name)}\b",  # Exact match
                    rf"pathogenic {re.escape(concept_name.lower())}",  # "pathogenic wind"
                    rf"{re.escape(concept_name.lower())} invasion",  # "wind invasion"
                ]

                for pattern in patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        # Found a relationship!
                        self.relationships["disease_to_concept"][disease_name].add(concept_name)
                        self.relationships["concept_to_disease"][concept_name].add(disease_name)
                        break

        total_links = sum(len(v) for v in self.relationships["disease_to_concept"].values())
        print(f"✓ Found {total_links} disease → concept relationships")

    def add_wikilinks_to_content(self, content: str, entity_map: dict[str, Path]) -> str:
        """Add [[wikilinks]] to content for mentioned entities"""
        modified_content = content

        # Sort by length (longest first) to avoid partial matches
        sorted_entities = sorted(entity_map.keys(), key=len, reverse=True)

        for entity_name in sorted_entities:
            # Skip if already has wikilink
            if f"[[{entity_name}]]" in modified_content:
                continue

            # Create pattern that doesn't match if already in wikilinks or frontmatter
            pattern = rf'(?<!\[\[)(?<!name: ")\b({re.escape(entity_name)})\b(?!\]\])'

            # Replace with wikilink, but limit to body content (after frontmatter)
            parts = modified_content.split("---", 2)
            if len(parts) == 3:
                frontmatter, _, body = parts

                # Only link in body, not in frontmatter
                body_modified = re.sub(
                    pattern,
                    r"[[\1]]",
                    body,
                    count=3,  # Limit to first 3 occurrences per file
                    flags=re.IGNORECASE,
                )

                modified_content = f"---{frontmatter}---{body_modified}"

        return modified_content

    def update_disease_files_with_concept_links(self):
        """Add wikilinks to concepts in disease files"""
        print("\n🔗 Adding concept wikilinks to disease files...")
        print("=" * 60)

        updated_count = 0

        for disease_name, disease_file in self.disease_map.items():
            with open(disease_file, encoding="utf-8") as f:
                original_content = f.read()

            # Add wikilinks for concepts
            modified_content = self.add_wikilinks_to_content(original_content, self.concept_map)

            # Only write if changes were made
            if modified_content != original_content:
                with open(disease_file, "w", encoding="utf-8") as f:
                    f.write(modified_content)
                updated_count += 1
                print(f"  ✓ Updated: {disease_name}")

        print(f"\n✓ Updated {updated_count} disease files with concept links")

    def update_frontmatter_relationships(self):
        """Update YAML frontmatter with discovered relationships"""
        print("\n📝 Updating frontmatter relationships...")
        print("=" * 60)

        # Update concept files with related diseases
        for concept_name, related_diseases in self.relationships["concept_to_disease"].items():
            concept_file = self.concept_map.get(concept_name)
            if concept_file:
                self._update_file_frontmatter(concept_file, "related", sorted(list(related_diseases)))
                print(f"  ✓ {concept_name}: Added {len(related_diseases)} disease links")

        # Update disease files with related concepts
        for disease_name, related_concepts in self.relationships["disease_to_concept"].items():
            disease_file = self.disease_map.get(disease_name)
            if disease_file:
                self._update_file_frontmatter(disease_file, "related", sorted(list(related_concepts)))
                print(f"  ✓ {disease_name}: Added {len(related_concepts)} concept links")

    def _update_file_frontmatter(self, file_path: Path, field: str, values: list[str]):
        """Update a specific field in YAML frontmatter"""
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        # Extract frontmatter and body
        match = re.match(r"^(---\s*\n)(.*?)(\n---\s*\n)(.*)", content, re.DOTALL)
        if not match:
            return

        yaml_start, yaml_content, yaml_end, body = match.groups()

        # Parse YAML
        frontmatter = yaml.safe_load(yaml_content)

        # Update field (merge with existing values)
        existing = frontmatter.get(field, [])
        if isinstance(existing, list):
            combined = sorted(list(set(existing + values)))
            frontmatter[field] = combined
        else:
            frontmatter[field] = values

        # Add updated timestamp
        frontmatter["updated"] = datetime.now().strftime("%Y-%m-%d")

        # Write back
        new_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
        new_content = f"{yaml_start}{new_yaml}{yaml_end}{body}"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    def generate_statistics(self):
        """Generate relationship statistics"""
        print("\n📊 Relationship Statistics")
        print("=" * 60)

        # Top concepts by disease usage
        concept_usage = [(k, len(v)) for k, v in self.relationships["concept_to_disease"].items()]
        concept_usage.sort(key=lambda x: x[1], reverse=True)

        print("\n🔝 Most Referenced Concepts:")
        for concept, count in concept_usage[:10]:
            print(f"  {concept}: {count} diseases")

        # Diseases with most concept relationships
        disease_complexity = [(k, len(v)) for k, v in self.relationships["disease_to_concept"].items()]
        disease_complexity.sort(key=lambda x: x[1], reverse=True)

        print("\n🏥 Most Complex Diseases (by concept relationships):")
        for disease, count in disease_complexity[:10]:
            print(f"  {disease}: {count} concepts")

        return {
            "concept_usage": concept_usage,
            "disease_complexity": disease_complexity,
            "total_relationships": sum(len(v) for v in self.relationships["disease_to_concept"].values()),
        }

    def run(self):
        """Execute the complete auto-linking process"""
        print("\n" + "=" * 60)
        print("🚀 TCM KNOWLEDGE BASE AUTO-LINKER")
        print("=" * 60)

        # Step 1: Load all files
        self.load_knowledge_base()

        # Step 2: Scan for relationships
        self.scan_for_concept_mentions()

        # Step 3: Add wikilinks
        self.update_disease_files_with_concept_links()

        # Step 4: Update frontmatter
        self.update_frontmatter_relationships()

        # Step 5: Statistics
        stats = self.generate_statistics()

        print("\n" + "=" * 60)
        print("✅ AUTO-LINKING COMPLETE")
        print("=" * 60)
        print(f"Total relationships created: {stats['total_relationships']}")
        print(f"Concepts linked: {len(self.relationships['concept_to_disease'])}")
        print(f"Diseases updated: {len(self.relationships['disease_to_concept'])}")
        print("=" * 60)


def main():
    base_dir = Path(__file__).parent.parent
    linker = TCMAutoLinker(base_dir)
    linker.run()


if __name__ == "__main__":
    main()
