#!/usr/bin/env python3
"""
Auto-Sync Frontmatter System
Automatically generates and maintains frontmatter by scanning markdown content.
This is the dynamic, self-maintaining system that keeps everything in sync.
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict
from datetime import datetime


class AutoSyncFrontmatter:
    """Automatically generates frontmatter from markdown content"""

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)

        # Directories
        self.concepts_dir = self.base_dir / "TCM_Concepts"
        self.diseases_dir = self.base_dir / "TCM_Diseases"
        self.points_dir = self.base_dir / "TCM_Points"
        self.herbs_dir = self.base_dir / "TCM_Herbs"
        self.techniques_dir = self.base_dir / "TCM_Techniques"
        self.symptoms_dir = self.base_dir / "TCM_Symptoms"

        # Entity registries (name -> file_path)
        self.concepts = {}
        self.diseases = {}
        self.points = {}
        self.herbs = {}
        self.techniques = {}
        self.symptoms = {}

        # Extracted relationships
        self.extracted_data = {}  # file_path -> extracted data dict

    def build_entity_registry(self):
        """Build registry of all entities for reference"""
        print("\n📚 Building entity registry...")
        print("=" * 80)

        # Concepts
        if self.concepts_dir.exists():
            for file in self.concepts_dir.glob("*.md"):
                if file.stem not in ["TEMPLATE_Concept"]:
                    name = self._extract_name_from_file(file)
                    if name:
                        self.concepts[name] = file

        # Diseases
        if self.diseases_dir.exists():
            for file in self.diseases_dir.glob("*.md"):
                if file.stem not in ["TEMPLATE_Disease", "EXAMPLE_Wind_Stroke"]:
                    name = self._extract_name_from_file(file)
                    if name:
                        self.diseases[name] = file

        # Points
        if self.points_dir.exists():
            for file in self.points_dir.glob("*.md"):
                name = self._extract_point_code(file)
                if name:
                    self.points[name] = file

        # Herbs
        if self.herbs_dir.exists():
            for file in self.herbs_dir.glob("*.md"):
                name = self._extract_name_from_file(file)
                if name:
                    self.herbs[name] = file

        # Techniques
        if self.techniques_dir.exists():
            for file in self.techniques_dir.glob("*.md"):
                if file.stem not in ["TEMPLATE_Technique"]:
                    name = self._extract_name_from_file(file)
                    if name:
                        self.techniques[name] = file

        # Symptoms
        if self.symptoms_dir.exists():
            for file in self.symptoms_dir.glob("*.md"):
                if file.stem not in ["TEMPLATE_Symptom"]:
                    name = self._extract_name_from_file(file)
                    if name:
                        self.symptoms[name] = file

        print(f"  ✓ {len(self.concepts)} concepts")
        print(f"  ✓ {len(self.diseases)} diseases")
        print(f"  ✓ {len(self.points)} points")
        print(f"  ✓ {len(self.herbs)} herbs")
        print(f"  ✓ {len(self.techniques)} techniques")
        print(f"  ✓ {len(self.symptoms)} symptoms")

    def _extract_name_from_file(self, file_path: Path) -> str:
        """Extract entity name from file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Try frontmatter first
            match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                fm_text = match.group(1).strip()
                if fm_text:
                    try:
                        fm = yaml.safe_load(fm_text)
                        if fm and fm.get('name'):
                            return fm['name']
                    except:
                        pass

            # Try first heading
            heading_match = re.search(r'^#\s+[🩺📖🌿📍⚡]?\s*(.+?)$', content, re.MULTILINE)
            if heading_match:
                name = heading_match.group(1).strip()
                # Remove wikilinks
                name = re.sub(r'\[\[([^\]]+)\]\]', r'\1', name)
                return name

            # Fallback to filename
            return file_path.stem.replace('_', ' ')

        except:
            return file_path.stem.replace('_', ' ')

    def _extract_point_code(self, file_path: Path) -> str:
        """Extract point code from file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                fm_text = match.group(1).strip()
                if fm_text:
                    try:
                        fm = yaml.safe_load(fm_text)
                        if fm and fm.get('name'):
                            return fm['name']
                    except:
                        pass

            return file_path.stem

        except:
            return file_path.stem

    def scan_content(self, file_path: Path) -> Dict:
        """Scan markdown content and extract all relationships"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            extracted = {
                'name': self._extract_name_from_file(file_path),
                'related': set(),      # Wikilinked concepts
                'symptoms': set(),     # Extracted symptoms
                'points': set(),       # Point codes
                'herbs': set(),        # Herb names
                'patterns': set(),     # Pattern names
                'western_conditions': set(),
                'formulas': set(),
                'category': set(),
            }

            # Extract wikilinks - for concepts, herbs, symptoms
            wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
            for link in wikilinks:
                # Check which type of entity this is
                if link in self.concepts:
                    extracted['related'].add(link)
                elif link in self.herbs:
                    extracted['herbs'].add(link)
                elif link in self.symptoms:
                    extracted['symptoms'].add(link)
                # Don't add unknown wikilinks to avoid clutter

            # Extract point codes from treatment sections
            # Look for patterns like "[[Baihui (Du 20)]]" or "(Du 20)" or "DU-20"
            point_patterns = [
                r'\[\[.+?\(([A-Z]{2,3})[- ](\d{1,2})\)\]\]',  # [[Baihui (Du 20)]]
                r'\(([A-Z]{2,3})[- ](\d{1,2})\)',             # (Du 20) or (DU-20)
                r'\b([A-Z]{2,3})[- ](\d{1,2})\b',             # DU-20 or Du 20
            ]

            for pattern in point_patterns:
                point_codes = re.findall(pattern, content, re.IGNORECASE)
                for meridian, number in point_codes:
                    # Standardize to uppercase with dash
                    code = f"{meridian.upper()}-{number}"
                    if code in self.points:
                        extracted['points'].add(code)

            # Extract symptoms from specific sections
            # Look for "Main Manifestations" or "Symptoms" sections
            symptom_sections = re.findall(
                r'(?:Main Manifestations|Symptoms|Key Characteristics):?\s*\n((?:[-*]\s+.+\n?)+)',
                content,
                re.IGNORECASE
            )
            for section in symptom_sections:
                symptoms = re.findall(r'[-*]\s+(.+?)(?:\n|$)', section)
                for symptom in symptoms:
                    # Clean up symptom text - remove wikilinks
                    symptom = re.sub(r'\[\[([^\]]+)\]\]', r'\1', symptom)
                    symptom = symptom.strip()
                    if symptom and len(symptom) > 3 and len(symptom) < 200:
                        extracted['symptoms'].add(symptom)

            # Extract patterns
            patterns = re.findall(r'(?:Pattern|Syndrome)\s*\d*:?\s*(.+?)(?:\n|$)', content)
            for pattern in patterns:
                pattern = pattern.strip()
                if pattern and len(pattern) < 100:  # Reasonable pattern name length
                    extracted['patterns'].add(pattern)

            # Extract western conditions
            western_matches = re.findall(
                r'(?:Western|Modern|Biomedical)\s+(?:Diagnosis|Condition|Disease):\s*(.+?)(?:\n|$)',
                content,
                re.IGNORECASE
            )
            for match in western_matches:
                conditions = [c.strip() for c in match.split(',')]
                extracted['western_conditions'].update(conditions)

            # Extract category from content structure
            if "Internal Disease" in content or "internal disease" in content:
                extracted['category'].add("Internal Diseases")
            if "External Disease" in content or "external disease" in content:
                extracted['category'].add("External Diseases")
            if "Gynecological" in content or "gynecological" in content:
                extracted['category'].add("Gynecological Diseases")
            if "Pediatric" in content or "pediatric" in content:
                extracted['category'].add("Pediatric Diseases")

            return extracted

        except Exception as e:
            print(f"  ⚠️  Error scanning {file_path.name}: {e}")
            return None

    def generate_frontmatter_yaml(self, extracted_data: Dict, entity_type: str) -> str:
        """Generate YAML frontmatter from extracted data"""

        # Base structure
        fm = {
            'id': f"{entity_type}-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'name': extracted_data['name'],
            'type': entity_type,
            'aliases': [],
            'tags': ['TCM', entity_type.title()],
            'category': sorted(list(extracted_data.get('category', set()))),
            'related': sorted(list(extracted_data.get('related', set()))),
            'symptoms': sorted(list(extracted_data.get('symptoms', set()))),
            'patterns': sorted(list(extracted_data.get('patterns', set()))),
            'western_conditions': sorted(list(extracted_data.get('western_conditions', set()))),
            'formulas': sorted(list(extracted_data.get('formulas', set()))),
            'herbs': sorted(list(extracted_data.get('herbs', set()))),
            'points': sorted(list(extracted_data.get('points', set()))),
            'nutrition': [],
            'tests': [],
            'updated': datetime.now().strftime('%Y-%m-%d')
        }

        # Generate YAML with comments
        yaml_lines = ['---']
        yaml_lines.append('# 🔹 Core Metadata (Universal Fields)')
        yaml_lines.append(f'id: "{fm["id"]}"')
        yaml_lines.append(f'name: "{fm["name"]}"')
        yaml_lines.append(f'type: "{fm["type"]}"')
        yaml_lines.append(f'aliases: {fm["aliases"]}')
        yaml_lines.append(f'tags: {fm["tags"]}')
        yaml_lines.append('')
        yaml_lines.append('# 🔹 Cross-Link Fields (Universal Relationship Slots)')
        yaml_lines.append(f'category: {fm["category"]}')
        yaml_lines.append(f'related: {fm["related"]}')
        yaml_lines.append(f'symptoms: {fm["symptoms"]}')
        yaml_lines.append(f'patterns: {fm["patterns"]}')
        yaml_lines.append(f'western_conditions: {fm["western_conditions"]}')
        yaml_lines.append(f'formulas: {fm["formulas"]}')
        yaml_lines.append(f'herbs: {fm["herbs"]}')
        yaml_lines.append(f'points: {fm["points"]}')
        yaml_lines.append(f'nutrition: {fm["nutrition"]}')
        yaml_lines.append(f'tests: {fm["tests"]}')
        yaml_lines.append(f'updated: "{fm["updated"]}"')
        yaml_lines.append('---')

        return '\n'.join(yaml_lines)

    def update_file_frontmatter(self, file_path: Path, entity_type: str, dry_run: bool = False):
        """Update a file's frontmatter based on content scan"""

        # Scan content
        extracted = self.scan_content(file_path)
        if not extracted:
            return False

        # Read current file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Generate new frontmatter
        new_frontmatter = self.generate_frontmatter_yaml(extracted, entity_type)

        # Replace or add frontmatter
        if content.startswith('---'):
            # Replace existing frontmatter
            match = re.match(r'^---\s*\n.*?\n---\s*\n', content, re.DOTALL)
            if match:
                new_content = new_frontmatter + '\n\n' + content[match.end():]
            else:
                # Malformed frontmatter, replace anyway
                new_content = new_frontmatter + '\n\n' + content
        else:
            # Add frontmatter
            new_content = new_frontmatter + '\n\n' + content

        if dry_run:
            print(f"  Would update: {file_path.name}")
            return True

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True

    def sync_all_diseases(self, dry_run: bool = False):
        """Sync frontmatter for all disease files"""
        print("\n🩺 Syncing disease files...")
        print("=" * 80)

        if not self.diseases_dir.exists():
            print("❌ Diseases directory not found")
            return

        updated = 0
        for file_path in self.diseases_dir.glob("*.md"):
            if file_path.stem in ["TEMPLATE_Disease", "EXAMPLE_Wind_Stroke"]:
                continue

            if self.update_file_frontmatter(file_path, 'disease', dry_run):
                updated += 1

        print(f"✓ {'Would update' if dry_run else 'Updated'} {updated} disease files")

    def sync_all_entities(self, dry_run: bool = False):
        """Sync frontmatter for all entity types"""
        print("\n🔄 SYNCING ALL FRONTMATTER")
        print("=" * 80)

        # Build registry first
        self.build_entity_registry()

        # Sync each type
        self.sync_all_diseases(dry_run)

        # Could add more entity types here if needed
        # self.sync_all_herbs(dry_run)
        # self.sync_all_concepts(dry_run)

        print("\n" + "=" * 80)
        print(f"✅ SYNC {'PREVIEW' if dry_run else 'COMPLETE'}")
        print("=" * 80)

    def run(self, dry_run: bool = True):
        """Run the auto-sync system"""
        print("=" * 80)
        print("🔄 AUTO-SYNC FRONTMATTER SYSTEM")
        print("=" * 80)

        if dry_run:
            print("\n⚠️  DRY RUN MODE - No files will be modified")
            print("    Run with --execute to apply changes\n")

        self.sync_all_entities(dry_run)


def main():
    import sys

    base_dir = Path(__file__).parent.parent
    syncer = AutoSyncFrontmatter(base_dir)

    # Check for --execute flag
    dry_run = '--execute' not in sys.argv

    syncer.run(dry_run)

    if dry_run:
        print("\n💡 To apply these changes, run:")
        print("   python3 auto_sync_frontmatter.py --execute")


if __name__ == "__main__":
    main()
