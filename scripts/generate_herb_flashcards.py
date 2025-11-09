#!/usr/bin/env python3
"""
Generate Herb Flashcards for Obsidian Spaced Repetition Plugin

This script extracts data from TCM_Herbs/*.md files and generates flashcards
organized by category.
"""

import os
import yaml
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

class HerbFlashcardGenerator:
    def __init__(self, herbs_dir: str, output_dir: str):
        self.herbs_dir = Path(herbs_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Store by herb category (e.g., "Herbs that Stop Bleeding")
        # Structure: {herb_category: {card_type: [cards]}}
        self.herb_categories = {}
    
    def parse_herb_file(self, filepath: Path) -> Dict[str, Any]:
        """Extract herb data from markdown file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return None
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None
        
        try:
            frontmatter = yaml.safe_load(parts[1])
            body = parts[2]
            
            # Extract specific sections from body for more detail
            functions_match = re.search(
                r'## ⚡ Functions & Actions\s*\n(.*?)(?=\n##|\n---|\Z)',
                body,
                re.DOTALL
            )
            functions_text = functions_match.group(1).strip() if functions_match else ""

            cautions_match = re.search(
                r'## ⚠️ Cautions & Contraindications\s*\n(.*?)(?=\n##|\n---|\Z)',
                body,
                re.DOTALL
            )
            cautions_text = cautions_match.group(1).strip() if cautions_match else ""

            return {
                'frontmatter': frontmatter,
                'functions_body': functions_text,
                'cautions_body': cautions_text,
                'filepath': filepath
            }
        except Exception as e:
            print(f"Error parsing {filepath.name}: {e}")
            return None
    
    def format_herb_header(self, herb_data: Dict) -> str:
        """Create the herb header for flashcard front."""
        hd = herb_data.get('herb_data', {})
        pinyin = hd.get('pinyin', '')
        hanzi = hd.get('hanzi', '')
        pharma = hd.get('pharmaceutical', '')
        english = hd.get('english', '')
        
        return f"**{pinyin} ({hanzi})** · *{pharma}* · {english}"

    def _format_flashcard(self, header: str, question: str, answer: str) -> str:
        """Formats a single flashcard string without frontmatter."""
        return f"""# {header}
## {question}
?
{answer}
<!--SR:!2025-11-10,3,250-->"""

    def create_category_properties_flashcard(self, herb_info: Dict) -> str:
        fm = herb_info['frontmatter']
        hd = fm.get('herb_data', {})
        header = self.format_herb_header(fm)
        
        category = ', '.join(fm.get('category', ['N/A']))
        taste = ', '.join(hd.get('taste', ['N/A']))
        temp = hd.get('temperature', 'N/A')
        channels = ', '.join(hd.get('channels', ['N/A']))

        answer = f"""**Category:** {category}
**Taste:** {taste}
**Temperature:** {temp}
**Channels:** {channels}"""
        
        question = "What are the Category and Properties of this herb?"
        return self._format_flashcard(header, question, answer)

    def create_dosage_flashcard(self, herb_info: Dict) -> str:
        fm = herb_info['frontmatter']
        hd = fm.get('herb_data', {})
        header = self.format_herb_header(fm)
        
        dosage = hd.get('dosage', 'N/A')
        answer = f"**Dosage:** {dosage}"
        
        question = "What is the standard Dosage for this herb?"
        return self._format_flashcard(header, question, answer)

    def create_symptoms_flashcard(self, herb_info: Dict) -> str:
        fm = herb_info['frontmatter']
        header = self.format_herb_header(fm)
        
        symptoms = fm.get('symptoms', [])
        if not symptoms:
            return None
            
        symptoms_text = '\n- '.join([s.replace('[[', '').replace(']]', '') for s in symptoms])
        answer = f"- {symptoms_text}"
        
        question = "What are the common Symptoms and Indications for this herb?"
        return self._format_flashcard(header, question, answer)

    def create_cautions_flashcard(self, herb_info: Dict) -> str:
        fm = herb_info['frontmatter']
        hd = fm.get('herb_data', {})
        header = self.format_herb_header(fm)
        
        cautions_body = herb_info.get('cautions_body', '')
        if cautions_body and cautions_body.strip():
            answer = cautions_body
        else:
            contra = '\n- '.join(hd.get('contraindications', []))
            cautions = '\n- '.join(hd.get('cautions', []))
            toxicity = hd.get('toxicity', '')
            
            parts = []
            if contra: parts.append(f"**Contraindications:**\n- {contra}")
            if cautions: parts.append(f"**Cautions:**\n- {cautions}")
            if toxicity: parts.append(f"**Toxicity:**\n{toxicity}")
            
            if not parts: return None
            answer = '\n\n'.join(parts)

        if not answer.strip(): return None
        question = "What are the Cautions & Contraindications for this herb?"
        return self._format_flashcard(header, question, answer)

    def create_functions_flashcard(self, herb_info: Dict) -> str:
        fm = herb_info['frontmatter']
        header = self.format_herb_header(fm)
        
        functions_body = herb_info.get('functions_body', '')
        if functions_body and functions_body.strip():
            answer = functions_body
        else:
            functions_list = fm.get('herb_data', {}).get('functions', [])
            if not functions_list: return None
            answer = "- " + '\n- '.join(functions_list)
        
        if not answer.strip(): return None
        question = "What are the Functions & Actions of this herb?"
        return self._format_flashcard(header, question, answer)

    def generate_all_flashcards(self):
        print("🔍 Scanning herb files...")
        herb_files = sorted([f for f in self.herbs_dir.glob("*.md") if not f.name.startswith('00 -')])
        print(f"📚 Found {len(herb_files)} herb files\n")
        
        for filepath in herb_files:
            herb_info = self.parse_herb_file(filepath)
            if not herb_info:
                continue
            
            # Get herb category from frontmatter
            fm = herb_info['frontmatter']
            herb_category_list = fm.get('category', ['Uncategorized'])
            # Use first category if multiple exist
            herb_category = herb_category_list[0] if herb_category_list else 'Uncategorized'
            
            # Initialize category if not exists
            if herb_category not in self.herb_categories:
                self.herb_categories[herb_category] = {
                    'category_properties': [],
                    'dosage': [],
                    'symptoms': [],
                    'cautions': [],
                    'functions': []
                }
            
            # Generate cards
            cards = {
                'category_properties': self.create_category_properties_flashcard(herb_info),
                'dosage': self.create_dosage_flashcard(herb_info),
                'symptoms': self.create_symptoms_flashcard(herb_info),
                'cautions': self.create_cautions_flashcard(herb_info),
                'functions': self.create_functions_flashcard(herb_info),
            }
            
            # Add cards to appropriate herb category
            for card_type, card in cards.items():
                if card:
                    self.herb_categories[herb_category][card_type].append(card)
        
        print("✅ Flashcard generation complete!\n")
        self.print_summary()

    def print_summary(self):
        print("=" * 60)
        print("HERB FLASHCARD GENERATION SUMMARY")
        print("=" * 60)
        total = 0
        for herb_cat, card_types in sorted(self.herb_categories.items()):
            cat_total = sum(len(cards) for cards in card_types.values())
            total += cat_total
            print(f"{herb_cat[:40]:40s}: {cat_total:4d} cards")
        print("=" * 60)
        print(f"{'TOTAL':40s}: {total:4d} cards")
        print("=" * 60)

    def save_flashcards(self):
        print("\n💾 Saving flashcards by herb category and card type...")
        
        for herb_cat, card_types in sorted(self.herb_categories.items()):
            # Clean up category name for filename
            clean_cat = herb_cat.replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '')
            
            for card_type, cards in card_types.items():
                if not cards:
                    continue
                
                card_type_name = card_type.replace('_', ' ').title()
                filename = f"Flashcards_{clean_cat}_{card_type_name.replace(' ', '_')}.md"
                filepath = self.output_dir / filename
                
                header = f"""---
material_type: flashcard_collection
topic: TCM Herbs
herb_category: {herb_cat}
card_type: {card_type_name}
total_cards: {len(cards)}
created: {datetime.now().strftime('%Y-%m-%d')}
tags:
  - flashcards
  - herbs
  - {clean_cat.lower()}
---

# TCM Herbs Flashcards: {herb_cat} - {card_type_name}

**Total Cards:** {len(cards)}
**Herb Category:** {herb_cat}
**Card Type:** {card_type_name}
**Created:** {datetime.now().strftime('%Y-%m-%d')}

---

"""
                content = header + '\n\n---\n\n'.join(cards)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"  ✓ {filename} ({len(cards)} cards)")
        
        print("\n✅ All flashcard files saved!")

def main():
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    herbs_dir = base_dir / "TCM_Herbs"
    output_dir = base_dir / "Flashcards" / "Herbs"
    
    print("=" * 60)
    print("TCM HERB FLASHCARD GENERATOR")
    print("=" * 60)
    print(f"Herbs directory: {herbs_dir}")
    print(f"Output directory: {output_dir}")
    print("=" * 60)
    print()
    
    generator = HerbFlashcardGenerator(str(herbs_dir), str(output_dir))
    generator.generate_all_flashcards()
    generator.save_flashcards()
    
    print("\n" + "=" * 60)
    print("DONE! Herb flashcards are ready for Obsidian.")
    print(f"\n📂 Location: {output_dir}")

if __name__ == "__main__":
    main()
