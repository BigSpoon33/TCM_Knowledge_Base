#!/usr/bin/env python3
"""
Generate Acupuncture Point Flashcards for Obsidian Spaced Repetition Plugin

This script extracts data from TCM_Points/*.md files and generates flashcards
organized by category (location, needling, indications, combinations, theory).

Each flashcard includes:
- Point code, pinyin, hanzi, and English name on the front
- Specific question/answer content
- Tags for organization
- Obsidian SR format
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


class PointFlashcardGenerator:
    def __init__(self, points_dir: str, output_dir: str):
        self.points_dir = Path(points_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Flashcard categories
        self.categories = {
            "location": [],
            "needling": [],
            "functions": [],
            "indications": [],
            "combinations": [],
            "theory": [],
        }

    def parse_point_file(self, filepath: Path) -> dict[str, Any]:
        """Extract point data from markdown file."""
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        # Extract frontmatter
        if not content.startswith("---"):
            return None

        parts = content.split("---", 2)
        if len(parts) < 3:
            return None

        try:
            frontmatter = yaml.safe_load(parts[1])
            body = parts[2]

            # Extract TCM Theory section
            theory_match = re.search(r"## 🧬 TCM Theory & Commentary\s*\n(.*?)(?=\n##|\n---|\Z)", body, re.DOTALL)
            theory_text = theory_match.group(1).strip() if theory_match else ""

            return {"frontmatter": frontmatter, "body": body, "theory": theory_text, "filepath": filepath}
        except Exception as e:
            print(f"Error parsing {filepath.name}: {e}")
            return None

    def format_point_header(self, point_data: dict) -> str:
        """Create the point header for flashcard front."""
        pd = point_data.get("point_data", {})
        code = pd.get("code", "Unknown")
        pinyin = pd.get("pinyin", "")
        hanzi = pd.get("hanzi", "")
        english = pd.get("english", "")

        return f"**{code}** · {pinyin} ({hanzi}) · *{english}*"

    def _format_flashcard(self, header: str, question: str, answer: str) -> str:
        """Formats a single flashcard string without frontmatter."""
        return f"""# {header}
## {question}
?
{answer}
<!--SR:!2025-11-10,3,250-->"""

    def create_location_flashcard(self, point_data: dict) -> str:
        """Generate location flashcard with image reference."""
        fm = point_data["frontmatter"]
        pd = fm.get("point_data", {})

        header = self.format_point_header(fm)
        location = pd.get("location_description", "Location not specified")
        location_notes = pd.get("location_notes", "")
        special_props = pd.get("special_properties", [])
        code = pd.get("code", "XX-XX")

        # Build answer
        answer_parts = [f"**Location:** {location}"]

        if location_notes:
            answer_parts.append(f"\n**Notes:** {location_notes}")

        if special_props:
            props_text = "\n- ".join(special_props)
            answer_parts.append(f"\n**Special Properties:**\n- {props_text}")

        # Add image reference
        answer_parts.append(f"\n![[{code}_diagram.jpg]]")

        answer = "\n".join(answer_parts)

        question = "What is the location and special properties of this point?"
        return self._format_flashcard(header, question, answer)

    def create_needling_flashcard(self, point_data: dict) -> str:
        """Generate needling technique flashcard."""
        fm = point_data["frontmatter"]
        pd = fm.get("point_data", {})

        header = self.format_point_header(fm)
        method = pd.get("needling_method", "Not specified")
        depth = pd.get("needling_depth", "Not specified")
        cautions = pd.get("needling_cautions", [])

        # Build answer
        answer_parts = [f"**Method:** {method}", f"**Depth:** {depth}"]

        if cautions:
            cautions_text = "\n- ".join(cautions)
            answer_parts.append(f"\n**⚠️ Cautions:**\n- {cautions_text}")

        answer = "\n".join(answer_parts)

        question = "What is the needling technique and cautions for this point?"
        return self._format_flashcard(header, question, answer)

    def create_functions_flashcard(self, point_data: dict) -> str:
        """Generate functions & actions flashcard."""
        fm = point_data["frontmatter"]
        pd = fm.get("point_data", {})

        header = self.format_point_header(fm)
        functions = pd.get("functions", [])

        if not functions:
            return None

        functions_text = "\n- ".join(functions)
        answer = f"- {functions_text}"

        question = "What are the functions and actions of this point?"
        return self._format_flashcard(header, question, answer)

    def create_indications_flashcard(self, point_data: dict) -> str:
        """Generate clinical indications flashcard."""
        fm = point_data["frontmatter"]
        pd = fm.get("point_data", {})

        header = self.format_point_header(fm)
        indications = pd.get("indications", {})

        # Handle different formats
        answer_parts = []

        if isinstance(indications, list):
            # List of dicts format
            for item in indications:
                if isinstance(item, dict):
                    for category, items in item.items():
                        if items:
                            cat_title = category.replace("_", " ").title()
                            if isinstance(items, list):
                                items_text = "\n  - ".join(items)
                            else:
                                items_text = str(items)
                            answer_parts.append(f"**{cat_title}:**\n  - {items_text}")
                elif isinstance(item, str):
                    answer_parts.append(f"- {item}")
        elif isinstance(indications, dict):
            # Dict format
            for category, items in indications.items():
                if items:
                    cat_title = category.replace("_", " ").title()
                    if isinstance(items, list):
                        items_text = "\n  - ".join(items)
                    else:
                        items_text = str(items)
                    answer_parts.append(f"**{cat_title}:**\n  - {items_text}")
        else:
            return None

        if not answer_parts:
            return None

        answer = "\n\n".join(answer_parts)

        question = "What are the clinical indications for this point?"
        return self._format_flashcard(header, question, answer)

    def create_combinations_flashcard(self, point_data: dict) -> str:
        """Generate point combinations flashcard."""
        fm = point_data["frontmatter"]
        pd = fm.get("point_data", {})

        header = self.format_point_header(fm)
        combinations = pd.get("combinations", [])

        if not combinations:
            return None

        # Build combinations list
        combo_parts = []
        for combo in combinations:
            condition = combo.get("condition", "Unknown condition")
            points = combo.get("points", [])
            source = combo.get("source", "Unknown source")

            points_text = ", ".join(points)
            combo_parts.append(f"**{condition}**\n  - Points: {points_text}\n  - Source: *{source}*")

        answer = "\n\n".join(combo_parts)

        if not answer.strip():
            return None

        question = "What are some classical point combinations using this point?"
        return self._format_flashcard(header, question, answer)

    def create_theory_flashcard(self, point_data: dict) -> str:
        """Generate TCM theory flashcard."""
        fm = point_data["frontmatter"]
        pd = fm.get("point_data", {})
        theory = point_data.get("theory", "")

        if not theory or not theory.strip():
            return None

        header = self.format_point_header(fm)

        answer = theory

        question = "What is the TCM theoretical understanding of this point?"
        return self._format_flashcard(header, question, answer)

    def generate_all_flashcards(self):
        """Process all point files and generate flashcards."""
        print("🔍 Scanning point files...")

        point_files = sorted(self.points_dir.glob("*.md"))
        point_files = [f for f in point_files if not f.name.startswith("TEMPLATE")]

        print(f"📚 Found {len(point_files)} point files\n")

        for filepath in point_files:
            point_data = self.parse_point_file(filepath)
            if not point_data:
                continue

            fm = point_data["frontmatter"]
            pd = fm.get("point_data", {})
            code = pd.get("code", filepath.stem)

            # Generate each type of flashcard
            cards = {
                "location": self.create_location_flashcard(point_data),
                "needling": self.create_needling_flashcard(point_data),
                "functions": self.create_functions_flashcard(point_data),
                "indications": self.create_indications_flashcard(point_data),
                "combinations": self.create_combinations_flashcard(point_data),
                "theory": self.create_theory_flashcard(point_data),
            }

            # Add to categories
            for category, card in cards.items():
                if card:
                    self.categories[category].append(
                        {
                            "code": code,
                            "content": card,
                            "channel": pd.get("channel", "unknown").lower().replace(" ", "-"),
                        }
                    )

        print("✅ Flashcard generation complete!\n")
        self.print_summary()

    def print_summary(self):
        """Print summary of generated flashcards."""
        print("=" * 60)
        print("FLASHCARD GENERATION SUMMARY")
        print("=" * 60)
        for category, cards in self.categories.items():
            print(f"{category.title():20s}: {len(cards):4d} cards")
        print("=" * 60)
        total = sum(len(cards) for cards in self.categories.values())
        print(f"{'TOTAL':20s}: {total:4d} cards")
        print("=" * 60)

    def save_flashcards(self, group_by: str = "category"):
        """
        Save flashcards to files.

        Args:
            group_by: 'category' (one file per type) or 'channel' (one file per meridian)
        """
        if group_by == "category":
            self._save_by_category()
        elif group_by == "channel":
            self._save_by_channel()
        else:
            raise ValueError(f"Unknown grouping: {group_by}")

    def _save_by_category(self):
        """Save flashcards grouped by category."""
        print("\n💾 Saving flashcards by category...")

        for category, cards in self.categories.items():
            if not cards:
                continue

            filename = f"Flashcards_Points_{category.title()}.md"
            filepath = self.output_dir / filename

            # Create file header
            header = f"""---
material_type: flashcard_collection
topic: Acupuncture Points
category: {category.title()}
total_cards: {len(cards)}
created: {datetime.now().strftime("%Y-%m-%d")}
tags:
  - flashcards
  - acupoints
  - {category}
---

# Acupuncture Points Flashcards: {category.title()}

**Total Cards:** {len(cards)}
**Category:** {category.title()}
**Created:** {datetime.now().strftime("%Y-%m-%d")}

---

"""

            # Add all flashcards
            content = header + "\n\n---\n\n".join(card["content"] for card in cards)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"  ✓ {filename} ({len(cards)} cards)")

        print("\n✅ All flashcard files saved!")

    def _save_by_channel(self):
        """Save flashcards grouped by channel AND category (e.g., SI_Location, SI_Functions)."""
        print("\n💾 Saving flashcards by channel and category...")

        # Reorganize by channel and category
        by_channel_category = {}

        for category, cards in self.categories.items():
            for card in cards:
                channel_raw = card["channel"]
                # Extract channel abbreviation (e.g., "small-intestine" -> "SI")
                channel_abbrev = self._get_channel_abbreviation(channel_raw)

                key = (channel_abbrev, category)
                if key not in by_channel_category:
                    by_channel_category[key] = []
                by_channel_category[key].append(card)

        # Save each channel-category combination
        for (channel_abbrev, category), cards in sorted(by_channel_category.items()):
            filename = f"Flashcards_{channel_abbrev}_{category.title()}.md"
            filepath = self.output_dir / filename

            header = f"""---
material_type: flashcard_collection
topic: Acupuncture Points
channel: {channel_abbrev}
category: {category.title()}
total_cards: {len(cards)}
created: {datetime.now().strftime("%Y-%m-%d")}
tags:
  - flashcards
  - acupoints
  - {channel_abbrev}
  - {category}
---

# Acupuncture Points Flashcards: {channel_abbrev} - {category.title()}

**Total Cards:** {len(cards)}
**Channel:** {channel_abbrev}
**Category:** {category.title()}
**Created:** {datetime.now().strftime("%Y-%m-%d")}

---

"""

            content = header + "\n\n---\n\n".join(card["content"] for card in cards)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"  ✓ {filename} ({len(cards)} cards)")

        print("\n✅ All flashcard files saved!")

    def _get_channel_abbreviation(self, channel_raw: str) -> str:
        """Convert full channel name to standard abbreviation."""
        channel_map = {
            "lung": "L",
            "lungs": "L",
            "large-intestine": "LI",
            "stomach": "S",
            "spleen": "Sp",
            "heart": "H",
            "small-intestine": "SI",
            "bladder": "B",
            "urinary-bladder": "B",
            "kidney": "K",
            "pericardium": "P",
            "san-jiao": "SJ",
            "sanjiao": "SJ",
            "triple-burner": "SJ",
            "triple-warmer": "SJ",
            "gall-bladder": "G",
            "gallbladder": "G",
            "liver": "Liv",
            "du-mai": "Du",
            "du": "Du",
            "governing-vessel": "Du",
            "ren-mai": "Ren",
            "ren": "Ren",
            "conception-vessel": "Ren",
            "unknown": "MISC",
        }

        channel_lower = channel_raw.lower().replace(" ", "-").replace("(", "").replace(")", "")
        return channel_map.get(channel_lower, channel_raw.upper()[:3])


def main():
    """Main execution function."""
    # Paths
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    points_dir = base_dir / "TCM_Points"
    output_dir = base_dir / "Flashcards" / "Acupuncture_Points"

    print("=" * 60)
    print("ACUPUNCTURE POINT FLASHCARD GENERATOR")
    print("=" * 60)
    print(f"Points directory: {points_dir}")
    print(f"Output directory: {output_dir}")
    print("=" * 60)
    print()

    # Generate flashcards
    generator = PointFlashcardGenerator(str(points_dir), str(output_dir))
    generator.generate_all_flashcards()

    # Save by channel and category
    generator.save_flashcards(group_by="channel")

    print("\n" + "=" * 60)
    print("DONE! Flashcards ready for Obsidian Spaced Repetition")
    print("=" * 60)
    print(f"\n📂 Location: {output_dir}")
    print("\nNext steps:")
    print("1. Open the flashcard files in Obsidian")
    print("2. Install the Spaced Repetition plugin if not already installed")
    print("3. Start reviewing!")


if __name__ == "__main__":
    main()
