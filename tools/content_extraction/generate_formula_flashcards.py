#!/usr/bin/env python3
"""
Generate TCM Formula Flashcards for Obsidian Spaced Repetition Plugin
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


class FormulaFlashcardGenerator:
    def __init__(self, formulas_dir: str, output_dir: str):
        self.formulas_dir = Path(formulas_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Store by formula category
        # Structure: {formula_category: {card_type: [cards]}}
        self.formula_categories = {}

    def parse_formula_file(self, filepath: Path) -> dict[str, Any]:
        """Extract formula data from markdown file."""
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        if not content.startswith("---"):
            return None

        parts = content.split("---", 2)
        if len(parts) < 3:
            return None

        try:
            frontmatter = yaml.safe_load(parts[1])
            body = parts[2]

            # Extract all major sections from the body
            sections = re.findall(r"##\s+(.+?)\n(.+?)(?=\n##|\n---)", body, re.DOTALL)

            body_sections = {title.strip(): content.strip() for title, content in sections}

            return {"frontmatter": frontmatter, "body_sections": body_sections, "filepath": filepath}
        except Exception as e:
            print(f"Error parsing {filepath.name}: {e}")
            return None

    def format_formula_header(self, fm: dict) -> str:
        """Create the formula header for flashcard front."""
        name = fm.get("name", "Unnamed Formula")
        aliases = fm.get("aliases", [])

        header_parts = [f"**{name}**"]
        if aliases:
            header_parts.append(f"({', '.join(aliases)})")

        return " ".join(header_parts)

    def _format_flashcard(self, header: str, question: str, answer: str) -> str:
        """Formats a single flashcard string."""
        if not answer or not answer.strip():
            return None
        return f"""# {header}
## {question}
?
{answer}
<!--SR:!2025-11-10,3,250-->"""

    def generate_flashcards_for_file(self, formula_info: dict, formula_category: str):
        """Generate all flashcards for a single formula file and add to category."""
        fm = formula_info["frontmatter"]
        header = self.format_formula_header(fm)

        # Initialize card types dict for this category if needed
        if formula_category not in self.formula_categories:
            self.formula_categories[formula_category] = {
                "category": [],
                "patterns": [],
                "symptoms": [],
                "diseases_conditions": [],
                "composition": [],
                "clinical_applications": [],
                "therapeutic_actions": [],
                "modifications": [],
                "cautions": [],
                "related_formulas": [],
                "clinical_notes": [],
                "study_notes": [],
                "research": [],
            }

        # --- Frontmatter-based cards ---

        # Category
        category = ", ".join(fm.get("category", []))
        if category:
            card = self._format_flashcard(header, "What is the **Formula Category**?", category)
            if card:
                self.formula_categories[formula_category]["category"].append(card)

        # Patterns
        patterns = "\n- ".join(fm.get("patterns", []))
        if patterns:
            card = self._format_flashcard(header, "What **TCM Patterns** does this formula treat?", f"- {patterns}")
            if card:
                self.formula_categories[formula_category]["patterns"].append(card)

        # Symptoms
        symptoms = "\n- ".join([s.replace("[[", "").replace("]]", "") for s in fm.get("symptoms", [])])
        if symptoms:
            card = self._format_flashcard(header, "What are the key **Symptoms** for this formula?", f"- {symptoms}")
            if card:
                self.formula_categories[formula_category]["symptoms"].append(card)

        # Diseases and Western Conditions
        diseases = "\n- ".join(fm.get("diseases", []))
        western = "\n- ".join(fm.get("western_conditions", []))
        disease_answer = []
        if diseases:
            disease_answer.append(f"**TCM Diseases:**\n- {diseases}")
        if western:
            disease_answer.append(f"**Western Conditions:**\n- {western}")
        if disease_answer:
            card = self._format_flashcard(
                header,
                "What **Diseases and Western Conditions** is this formula used for?",
                "\n\n".join(disease_answer),
            )
            if card:
                self.formula_categories[formula_category]["diseases_conditions"].append(card)

        # --- Body-based cards ---

        body_sections = formula_info.get("body_sections", {})
        for title, content in body_sections.items():
            # Skip the source reference section
            if "Source Reference" in title:
                continue

            # Clean up title for the question
            question_title = re.sub(
                r"^\s*🌿\s*|\s*📝\s*|\s*🎯\s*|\s*🔄\s*|\s*⚠️\s*|\s*🔗\s*|\s*💡\s*|\s*📚\s*|\s*🔬\s*", "", title
            ).strip()
            question = f"What are the details for **{question_title}**?"

            card = self._format_flashcard(header, question, content)
            if not card:
                continue

            # Categorize by section type
            title_lower = title.lower()
            if "composition" in title_lower or "dosage" in title_lower:
                self.formula_categories[formula_category]["composition"].append(card)
            elif "clinical application" in title_lower:
                self.formula_categories[formula_category]["clinical_applications"].append(card)
            elif "therapeutic action" in title_lower or "action" in title_lower:
                self.formula_categories[formula_category]["therapeutic_actions"].append(card)
            elif "modification" in title_lower or "variation" in title_lower:
                self.formula_categories[formula_category]["modifications"].append(card)
            elif "caution" in title_lower or "contraindication" in title_lower:
                self.formula_categories[formula_category]["cautions"].append(card)
            elif "related formula" in title_lower:
                self.formula_categories[formula_category]["related_formulas"].append(card)
            elif "clinical note" in title_lower or "commentary" in title_lower:
                self.formula_categories[formula_category]["clinical_notes"].append(card)
            elif "study note" in title_lower or "memory" in title_lower:
                self.formula_categories[formula_category]["study_notes"].append(card)
            elif "research" in title_lower or "evidence" in title_lower:
                self.formula_categories[formula_category]["research"].append(card)

    def generate_all(self):
        print("🔍 Scanning formula files...")
        formula_files = sorted(
            [
                f
                for f in self.formulas_dir.glob("*.md")
                if not f.name.endswith(".backup.md") and not f.name.startswith("TEMPLATE")
            ]
        )
        print(f"📚 Found {len(formula_files)} formula files\n")

        for filepath in formula_files:
            formula_info = self.parse_formula_file(filepath)
            if not formula_info:
                continue

            # Set formula name from h1 if not in frontmatter
            if not formula_info["frontmatter"].get("name"):
                h1_match = re.search(r"#\s+(.+)", formula_info.get("body_sections", {}).get("", ""))
                if not h1_match:  # Check the raw body if sections parsing failed
                    raw_body = open(filepath, encoding="utf-8").read().split("---", 2)[2]
                    h1_match = re.search(r"#\s+(.+)", raw_body)
                if h1_match:
                    formula_info["frontmatter"]["name"] = h1_match.group(1).strip()

            # Get formula category from frontmatter
            fm = formula_info["frontmatter"]
            formula_category_list = fm.get("category", ["Uncategorized"])
            # Use first category if multiple exist
            formula_category = formula_category_list[0] if formula_category_list else "Uncategorized"

            self.generate_flashcards_for_file(formula_info, formula_category)

        print("✅ Flashcard generation complete!\n")
        self.print_summary()

    def print_summary(self):
        print("=" * 60)
        print("FORMULA FLASHCARD GENERATION SUMMARY")
        print("=" * 60)
        total = 0
        for formula_cat, card_types in sorted(self.formula_categories.items()):
            cat_total = sum(len(cards) for cards in card_types.values())
            total += cat_total
            print(f"{formula_cat[:40]:40s}: {cat_total:4d} cards")
        print("=" * 60)
        print(f"{'TOTAL':40s}: {total:4d} cards")
        print("=" * 60)

    def save_flashcards_to_file(self):
        print("\n💾 Saving flashcards by formula category and card type...")

        for formula_cat, card_types in sorted(self.formula_categories.items()):
            # Clean up category name for filename
            clean_cat = (
                formula_cat.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace("-", "_")
            )

            for card_type, cards in card_types.items():
                if not cards:
                    continue

                card_type_name = card_type.replace("_", " ").title()
                filename = f"Flashcards_{clean_cat}_{card_type_name.replace(' ', '_')}.md"
                filepath = self.output_dir / filename

                header = f"""---
material_type: flashcard_collection
topic: TCM Formulas
formula_category: {formula_cat}
card_type: {card_type_name}
total_cards: {len(cards)}
created: {datetime.now().strftime("%Y-%m-%d")}
tags:
  - flashcards
  - formulas
  - {clean_cat.lower()}
---

# TCM Formulas Flashcards: {formula_cat} - {card_type_name}

**Total Cards:** {len(cards)}
**Formula Category:** {formula_cat}
**Card Type:** {card_type_name}
**Created:** {datetime.now().strftime("%Y-%m-%d")}

---

"""
                content = header + "\n\n---\n\n".join(cards)

                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)

                print(f"  ✓ {filename} ({len(cards)} cards)")

        print("\n✅ All flashcard files saved!")


def main():
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    formulas_dir = base_dir / "TCM_Formulas"
    output_dir = base_dir / "Flashcards" / "Formulas"

    print("=" * 60)
    print("TCM FORMULA FLASHCARD GENERATOR")
    print("=" * 60)
    print(f"Formulas directory: {formulas_dir}")
    print(f"Output directory: {output_dir}")
    print("=" * 60)
    print()

    generator = FormulaFlashcardGenerator(str(formulas_dir), str(output_dir))
    generator.generate_all()
    generator.save_flashcards_to_file()

    print("\n" + "=" * 60)
    print("DONE! Formula flashcards are ready for Obsidian.")
    print(f"\n📂 Location: {output_dir}")


if __name__ == "__main__":
    main()
