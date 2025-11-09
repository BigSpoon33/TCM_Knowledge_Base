#!/usr/bin/env python3
"""
Auto-link symptoms in TCM knowledge base files.

This script:
1. Builds a list of all standardized symptom names from TCM_Symptoms/
2. Scans herb/formula/point/pattern files for symptom mentions
3. Updates the 'symptoms' frontmatter field with wikilinks
4. Creates backups before modifying files

Usage:
    python scripts/auto_link_symptoms.py --dry-run  # Preview changes
    python scripts/auto_link_symptoms.py            # Apply changes
"""

import os
import re
import yaml
import argparse
from pathlib import Path
from typing import List, Dict, Set, Tuple
from datetime import datetime
import shutil


class SymptomLinker:
    """Automatically link symptoms in TCM knowledge base files."""

    def __init__(self, base_dir: Path, dry_run: bool = False):
        """
        Initialize the symptom linker.

        Args:
            base_dir: Root directory of the TCM knowledge base
            dry_run: If True, preview changes without modifying files
        """
        self.base_dir = base_dir
        self.dry_run = dry_run
        self.symptom_names: Set[str] = set()
        self.symptom_aliases: Dict[str, str] = {}  # alias -> canonical name
        self.changes_made = 0
        self.files_processed = 0

    def load_symptom_names(self) -> None:
        """Load all standardized symptom names from TCM_Symptoms directory."""
        symptom_dir = self.base_dir / "TCM_Symptoms"
        
        print(f"Loading symptoms from {symptom_dir}...")
        
        for file_path in symptom_dir.glob("*.md"):
            # Skip MOC and non-symptom files
            if file_path.name.startswith("00 -"):
                continue
            
            # Extract symptom name from filename (remove .md extension)
            symptom_name = file_path.stem
            self.symptom_names.add(symptom_name)
            
            # Also load aliases from frontmatter
            try:
                content = file_path.read_text(encoding='utf-8')
                frontmatter = self._extract_frontmatter(content)
                
                if frontmatter and 'aliases' in frontmatter:
                    aliases = frontmatter['aliases']
                    if isinstance(aliases, list):
                        for alias in aliases:
                            if alias:
                                self.symptom_aliases[alias.lower()] = symptom_name
            except Exception as e:
                print(f"Warning: Could not load aliases from {file_path.name}: {e}")
        
        print(f"Loaded {len(self.symptom_names)} symptoms and {len(self.symptom_aliases)} aliases")

    def _extract_frontmatter(self, content: str) -> Dict:
        """
        Extract YAML frontmatter from markdown content.

        Args:
            content: Markdown file content

        Returns:
            Dictionary of frontmatter data, or empty dict if none found
        """
        # Match frontmatter between --- delimiters
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return {}
        
        try:
            return yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError as e:
            print(f"Warning: YAML parsing error: {e}")
            return {}

    def _find_symptoms_in_text(self, text: str) -> Set[str]:
        """
        Find symptom mentions in text content.

        Args:
            text: Text to search for symptom mentions

        Returns:
            Set of standardized symptom names found in text
        """
        found_symptoms = set()
        text_lower = text.lower()
        
        # Check for each symptom name (case-insensitive)
        for symptom in self.symptom_names:
            # Create regex pattern for whole word matching
            # This prevents "pain" from matching "painful" or "Spain"
            pattern = r'\b' + re.escape(symptom.lower()) + r'\b'
            
            if re.search(pattern, text_lower):
                found_symptoms.add(symptom)
        
        # Also check aliases
        for alias, canonical_name in self.symptom_aliases.items():
            pattern = r'\b' + re.escape(alias) + r'\b'
            if re.search(pattern, text_lower):
                found_symptoms.add(canonical_name)
        
        return found_symptoms

    def _update_frontmatter_symptoms(self, content: str, symptoms: Set[str]) -> Tuple[str, bool]:
        """
        Update the symptoms field in frontmatter.

        Args:
            content: Original file content
            symptoms: Set of symptom names to add

        Returns:
            Tuple of (updated_content, was_modified)
        """
        # Extract frontmatter
        match = re.match(r'^(---\s*\n)(.*?)(\n---\s*\n)', content, re.DOTALL)
        if not match:
            print("Warning: No frontmatter found")
            return content, False
        
        prefix = match.group(1)
        frontmatter_text = match.group(2)
        suffix = match.group(3)
        body = content[match.end():]
        
        # Parse frontmatter
        try:
            frontmatter = yaml.safe_load(frontmatter_text) or {}
        except yaml.YAMLError as e:
            print(f"Warning: Could not parse frontmatter: {e}")
            return content, False
        
        # Get existing symptoms
        existing_symptoms = frontmatter.get('symptoms', [])
        if not isinstance(existing_symptoms, list):
            existing_symptoms = []
        
        # Extract symptom names from existing wikilinks
        existing_symptom_names = set()
        for item in existing_symptoms:
            # Remove wikilink brackets if present
            clean_name = re.sub(r'\[\[(.*?)\]\]', r'\1', str(item))
            existing_symptom_names.add(clean_name)
        
        # Add new symptoms (avoid duplicates)
        new_symptoms = symptoms - existing_symptom_names
        
        if not new_symptoms:
            return content, False  # No changes needed
        
        # Combine and sort symptoms
        all_symptoms = sorted(existing_symptom_names | symptoms)
        
        # Format as wikilinks
        frontmatter['symptoms'] = [f'[[{s}]]' for s in all_symptoms]
        
        # Reconstruct frontmatter
        new_frontmatter_text = yaml.dump(
            frontmatter,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False
        )
        
        new_content = prefix + new_frontmatter_text + suffix + body
        
        return new_content, True

    def process_file(self, file_path: Path) -> None:
        """
        Process a single file to add symptom wikilinks.

        Args:
            file_path: Path to the file to process
        """
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Find symptoms mentioned in the content
            symptoms_found = self._find_symptoms_in_text(content)
            
            if not symptoms_found:
                return  # No symptoms found, skip file
            
            # Update frontmatter
            new_content, was_modified = self._update_frontmatter_symptoms(content, symptoms_found)
            
            if not was_modified:
                return  # No changes needed
            
            self.files_processed += 1
            self.changes_made += len(symptoms_found)
            
            print(f"\n{'[DRY RUN] ' if self.dry_run else ''}Processing: {file_path.name}")
            print(f"  Found symptoms: {', '.join(sorted(symptoms_found))}")
            
            if not self.dry_run:
                # Create backup
                backup_path = file_path.with_suffix('.md.backup')
                shutil.copy2(file_path, backup_path)
                
                # Write updated content
                file_path.write_text(new_content, encoding='utf-8')
                print(f"  ✓ Updated (backup: {backup_path.name})")
            
        except Exception as e:
            print(f"Error processing {file_path.name}: {e}")

    def process_directory(self, directory: Path, file_pattern: str = "*.md", recursive: bool = True) -> None:
        """
        Process all files in a directory.

        Args:
            directory: Directory to process
            file_pattern: Glob pattern for files to process
            recursive: If True, process subdirectories recursively
        """
        print(f"\n{'='*60}")
        print(f"Processing directory: {directory.name}")
        print(f"{'='*60}")
        
        # Get files based on recursive flag
        if recursive:
            files = list(directory.rglob(file_pattern))
        else:
            files = list(directory.glob(file_pattern))
        
        # Filter out MOC and special files
        files = [f for f in files if not f.name.startswith("00 -")]
        
        print(f"Found {len(files)} files to process")
        
        for file_path in files:
            self.process_file(file_path)

    def run(self, directories: List[str]) -> None:
        """
        Run the symptom linking process.

        Args:
            directories: List of directory names to process (e.g., ['TCM_Herbs', 'TCM_Formulas'])
        """
        # Load symptom names first
        self.load_symptom_names()
        
        # Process each directory
        for dir_name in directories:
            dir_path = self.base_dir / dir_name
            
            if not dir_path.exists():
                print(f"Warning: Directory not found: {dir_path}")
                continue
            
            self.process_directory(dir_path)
        
        # Print summary
        print(f"\n{'='*60}")
        print(f"SUMMARY")
        print(f"{'='*60}")
        print(f"Files processed: {self.files_processed}")
        print(f"Symptom links added: {self.changes_made}")
        
        if self.dry_run:
            print("\n⚠️  DRY RUN MODE - No files were modified")
            print("Run without --dry-run to apply changes")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Auto-link symptoms in TCM knowledge base files"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without modifying files'
    )
    parser.add_argument(
        '--dirs',
        nargs='+',
        default=['TCM_Herbs', 'TCM_Formulas', 'TCM_Points', 'TCM_Patterns'],
        help='Directories to process (default: all main directories)'
    )
    parser.add_argument(
        '--base-dir',
        type=Path,
        default=Path.cwd(),
        help='Base directory of TCM knowledge base (default: current directory)'
    )
    
    args = parser.parse_args()
    
    # Initialize and run linker
    linker = SymptomLinker(args.base_dir, dry_run=args.dry_run)
    linker.run(args.dirs)


if __name__ == '__main__':
    main()
