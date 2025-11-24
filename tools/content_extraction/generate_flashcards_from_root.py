#!/usr/bin/env python3
"""
Generate OCDS-compatible flashcards from root note files.

This script:
1. Reads a root note file with frontmatter
2. Extracts flashcard_seeds from assessment_data
3. Generates additional flashcards from content structure
4. Creates a properly formatted flashcard file for Obsidian Spaced Repetition plugin
5. Outputs to Materials/{class_id}/ directory

Usage:
    python generate_flashcards_from_root.py "Root Note Name"
    python generate_flashcards_from_root.py "Blood Stasis Pattern" --output-dir "Materials/TCM_101"
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

# Base paths
BASE_DIR = Path(__file__).parent.parent
ROOT_NOTES_DIR = BASE_DIR / "OCDS_Documentation" / "05_Material_Templates"
MATERIALS_DIR = BASE_DIR / "Materials"


class RootNoteParser:
    """Parse root note files and extract content."""

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.frontmatter = {}
        self.body = ""
        self._parse_file()

    def _parse_file(self):
        """Parse markdown file into frontmatter and body."""
        try:
            with open(self.file_path, encoding="utf-8") as f:
                content = f.read()

            # Match frontmatter between --- markers
            match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", content, re.DOTALL)
            if not match:
                raise ValueError(f"No frontmatter found in {self.file_path.name}")

            frontmatter_text = match.group(1)
            self.body = match.group(2)

            # Parse YAML frontmatter
            try:
                self.frontmatter = yaml.safe_load(frontmatter_text) or {}
            except yaml.YAMLError as e:
                raise ValueError(f"Invalid YAML in {self.file_path.name}: {e}")

        except Exception as e:
            raise RuntimeError(f"Error reading {self.file_path}: {e}")

    def get_flashcard_seeds(self) -> list[dict[str, Any]]:
        """Extract flashcard seeds from assessment_data."""
        assessment_data = self.frontmatter.get("assessment_data", {})
        return assessment_data.get("flashcard_seeds", [])

    def get_metadata(self) -> dict[str, Any]:
        """Extract relevant metadata for flashcard generation."""
        return {
            "name": self.frontmatter.get("name", "Unknown Topic"),
            "domain": self.frontmatter.get("domain", "General"),
            "subject": self.frontmatter.get("subject", "General"),
            "difficulty": self.frontmatter.get("learning_data", {}).get("difficulty", "medium"),
            "tags": self.frontmatter.get("tags", []),
            "category": self.frontmatter.get("category", []),
        }

    def get_core_concepts(self) -> list[dict[str, Any]]:
        """Extract core concepts for additional flashcard generation."""
        content_data = self.frontmatter.get("content_data", {})
        return content_data.get("core_concepts", [])

    def get_key_facts(self) -> list[dict[str, Any]]:
        """Extract key facts for flashcard generation."""
        content_data = self.frontmatter.get("content_data", {})
        return content_data.get("key_facts", [])

    def get_comparisons(self) -> list[dict[str, Any]]:
        """Extract comparisons for flashcard generation."""
        content_data = self.frontmatter.get("content_data", {})
        return content_data.get("comparisons", [])

    def get_memory_aids(self) -> list[dict[str, Any]]:
        """Extract memory aids from presentation_data."""
        presentation_data = self.frontmatter.get("presentation_data", {})
        return presentation_data.get("memory_aids", [])


class FlashcardGenerator:
    """Generate flashcards from root note data."""

    def __init__(self, root_note: RootNoteParser, class_id: str = None):
        self.root_note = root_note
        self.metadata = root_note.get_metadata()
        self.class_id = class_id or self._generate_class_id()
        self.flashcards = []

    def _generate_class_id(self) -> str:
        """Generate class ID from domain and subject."""
        domain = self.metadata["domain"].replace(" ", "_")
        subject = self.metadata["subject"].replace(" ", "_")
        return f"{domain}_{subject}"

    def generate_all_flashcards(self):
        """Generate all flashcards from root note."""
        print(f"🎴 Generating flashcards for: {self.metadata['name']}")

        # 1. Generate from explicit flashcard seeds
        self._generate_from_seeds()

        # 2. Generate from core concepts
        self._generate_from_concepts()

        # 3. Generate from key facts
        self._generate_from_facts()

        # 4. Generate from comparisons
        self._generate_from_comparisons()

        # 5. Generate from memory aids
        self._generate_from_memory_aids()

        print(f"✅ Generated {len(self.flashcards)} flashcards")

    def _generate_from_seeds(self):
        """Generate flashcards from explicit flashcard_seeds."""
        seeds = self.root_note.get_flashcard_seeds()
        print(f"   📌 Processing {len(seeds)} flashcard seeds...")

        for seed in seeds:
            card = self._create_flashcard(
                question=seed.get("question", ""),
                answer=seed.get("answer", ""),
                context=seed.get("context", self.metadata["name"]),
                difficulty=seed.get("difficulty", "medium"),
                card_type=seed.get("card_type", "basic"),
            )
            self.flashcards.append(card)

    def _generate_from_concepts(self):
        """Generate flashcards from core concepts."""
        concepts = self.root_note.get_core_concepts()
        print(f"   🧠 Processing {len(concepts)} core concepts...")

        for concept in concepts:
            name = concept.get("name", "")
            definition = concept.get("definition", "")
            importance = concept.get("importance", "")

            if name and definition:
                # Definition flashcard
                card = self._create_flashcard(
                    question=f"What is {name}?",
                    answer=f"**Definition:** {definition}\n\n**Importance:** {importance}",
                    context=self.metadata["name"],
                    difficulty="easy",
                    card_type="basic",
                )
                self.flashcards.append(card)

    def _generate_from_facts(self):
        """Generate flashcards from key facts."""
        facts = self.root_note.get_key_facts()
        testable_facts = [f for f in facts if f.get("testable", True)]
        print(f"   📊 Processing {len(testable_facts)} testable facts...")

        for fact in testable_facts:
            fact_text = fact.get("fact", "")
            category = fact.get("category", "")

            if fact_text:
                # Convert fact into Q&A format
                question, answer = self._fact_to_qa(fact_text, category)
                if question and answer:
                    card = self._create_flashcard(
                        question=question,
                        answer=answer,
                        context=f"{self.metadata['name']} - {category}",
                        difficulty="medium",
                        card_type="basic",
                    )
                    self.flashcards.append(card)

    def _generate_from_comparisons(self):
        """Generate flashcards from comparisons."""
        comparisons = self.root_note.get_comparisons()
        print(f"   🔄 Processing {len(comparisons)} comparisons...")

        for comparison in comparisons:
            entities = comparison.get("entities", [])
            key_distinction = comparison.get("key_distinction", "")
            dimensions = comparison.get("dimensions", [])

            if len(entities) >= 2 and key_distinction:
                # Key distinction flashcard
                card = self._create_flashcard(
                    question=f"What is the key difference between {entities[0]} and {entities[1]}?",
                    answer=f"**Key Distinction:** {key_distinction}",
                    context=f"{self.metadata['name']} - Comparison",
                    difficulty="medium",
                    card_type="comparison",
                )
                self.flashcards.append(card)

                # Dimension-specific flashcards
                for dim in dimensions[:3]:  # Limit to top 3 dimensions
                    dimension = dim.get("dimension", "")
                    entity_1_value = dim.get("entity_1_value", "")
                    entity_2_value = dim.get("entity_2_value", "")

                    if dimension and entity_1_value and entity_2_value:
                        card = self._create_flashcard(
                            question=f"Compare {entities[0]} and {entities[1]} in terms of {dimension}",
                            answer=f"**{entities[0]}:** {entity_1_value}\n\n**{entities[1]}:** {entity_2_value}",
                            context=f"{self.metadata['name']} - Comparison",
                            difficulty="hard",
                            card_type="comparison",
                        )
                        self.flashcards.append(card)

    def _generate_from_memory_aids(self):
        """Generate flashcards from memory aids."""
        memory_aids = self.root_note.get_memory_aids()
        print(f"   💡 Processing {len(memory_aids)} memory aids...")

        for aid in memory_aids:
            aid_type = aid.get("type", "")
            content = aid.get("content", "")
            applies_to = aid.get("applies_to", "")

            if content and applies_to:
                if aid_type == "mnemonic" or aid_type == "acronym":
                    card = self._create_flashcard(
                        question=f"What does the {aid_type.upper()} help you remember?",
                        answer=f"**{aid_type.capitalize()}:** {content}\n\n**Applies to:** {applies_to}",
                        context=f"{self.metadata['name']} - Memory Aid",
                        difficulty="easy",
                        card_type="basic",
                    )
                    self.flashcards.append(card)

    def _fact_to_qa(self, fact: str, category: str) -> tuple:
        """Convert a fact statement into question-answer format."""
        # Simple heuristic: if fact contains "is", split on it
        if " is " in fact.lower():
            parts = fact.split(" is ", 1)
            question = f"What is {parts[0].strip()}?"
            answer = parts[1].strip()
            return question, answer

        # If fact contains specific patterns, extract them
        if "contraindicated" in fact.lower():
            question = "When is this contraindicated?"
            answer = fact
            return question, answer

        # Default: use fact as answer, generate generic question
        question = f"What is an important fact about {category}?"
        answer = fact
        return question, answer

    def _create_flashcard(
        self, question: str, answer: str, context: str, difficulty: str, card_type: str
    ) -> dict[str, Any]:
        """Create a flashcard dictionary."""
        return {
            "question": question,
            "answer": answer,
            "context": context,
            "difficulty": difficulty,
            "card_type": card_type,
        }

    def generate_flashcard_file(self, output_path: Path):
        """Generate complete flashcard markdown file."""
        if not self.flashcards:
            print("⚠️  No flashcards to generate!")
            return

        today = datetime.now().strftime("%Y-%m-%d")
        topic_name = self.metadata["name"]
        total_cards = len(self.flashcards)

        # Build frontmatter (OCDS-compatible)
        frontmatter = f"""---
ocds_type: flashcard
material_id: flashcards_{self.class_id.lower()}
class_id: {self.class_id}
title: "{topic_name} Flashcards"
description: Spaced repetition flashcards for {topic_name}
topic: {topic_name}
total_cards: {total_cards}
cards_reviewed: 0
cards_mastered: 0
last_review_date: null
tags:
  - flashcards
  - {self.class_id.lower()}
  - {self.metadata["domain"].lower()}
  - {self.metadata["subject"].lower().replace(" ", "-")}
  - spaced-repetition
card_count: {total_cards}
difficulty: {self.metadata["difficulty"]}
created: {today}
updated: {today}
---
"""

        # Build flashcard content with tracking
        content = f"\n# {topic_name} Flashcards\n\n"
        content += f"**Total Cards:** {total_cards}  \n"
        content += f"**Topic:** {topic_name}\n\n"

        # Add DataviewJS tracking (OCDS-compatible)
        content += """```dataviewjs
// Track flashcard reviews using Spaced Repetition plugin data
const file = dv.current().file;
const content = await dv.io.load(file.path);
const lines = content.split('\\n');

let totalCards = 0;
let reviewedCards = 0;
let masteredCards = 0;

// Count flashcards and check review status
for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  
  // Count cards (lines with "?" separator)
  if (line.trim() === '?') {
    totalCards++;
    
    // Check next few lines for SR comment (indicates reviewed)
    for (let j = i + 1; j < Math.min(i + 5, lines.length); j++) {
      const nextLine = lines[j];
      
      // Look for SR comment: <!--SR:!2025-11-10,3,250-->
      if (nextLine.includes('<!--SR:')) {
        reviewedCards++;
        
        // Extract ease factor (last number)
        const match = nextLine.match(/,(\\d+)-->/);
        if (match) {
          const ease = parseInt(match[1]);
          // Consider mastered if ease >= 250 (default is 250)
          if (ease >= 250) {
            masteredCards++;
          }
        }
        break;
      }
    }
  }
}

// Calculate percentage
const reviewPercent = totalCards > 0 ? Math.round((reviewedCards / totalCards) * 100) : 0;

// Update frontmatter
const currentFile = app.workspace.getActiveFile();
if (currentFile) {
  await app.fileManager.processFrontMatter(currentFile, (fm) => {
    fm.total_cards = totalCards;
    fm.card_count = totalCards;
    fm.cards_reviewed = reviewedCards;
    fm.cards_mastered = masteredCards;
    if (reviewedCards > 0) {
      fm.last_review_date = new Date().toISOString().split('T')[0];
    }
  });
}

// Display stats
dv.paragraph(`
**📊 Review Progress**

- **Total Cards:** ${totalCards}
- **Reviewed:** ${reviewedCards} (${reviewPercent}%)
- **Mastered:** ${masteredCards}
- **Status:** ${reviewPercent >= 80 ? '✅ Complete' : '⏳ In Progress'}
`);
```

---

"""

        # Group flashcards by context
        flashcards_by_context = {}
        for card in self.flashcards:
            context = card["context"]
            if context not in flashcards_by_context:
                flashcards_by_context[context] = []
            flashcards_by_context[context].append(card)

        # Generate flashcard blocks
        for context, cards in flashcards_by_context.items():
            for card in cards:
                content += f"# {context}\n"
                content += f"## {card['question']}\n"
                content += "?\n"
                content += f"{card['answer']}\n"
                content += "<!--SR:!2025-11-10,3,250-->\n\n"
                content += "---\n\n"

        # Write file
        full_content = frontmatter + content

        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(full_content)
            print(f"✅ Flashcard file created: {output_path}")
        except Exception as e:
            print(f"❌ Error writing flashcard file: {e}")


def find_root_note(note_name: str) -> Path | None:
    """Find root note file by name."""
    # Search in Materials/TCM_101 first
    materials_dir = MATERIALS_DIR / "TCM_101"
    if materials_dir.exists():
        # Sanitize note_name to match file naming convention
        sanitized_name = f"Root_Note_{note_name.replace(' ', '_')}.md"

        for file_path in materials_dir.glob("*.md"):
            if file_path.name == sanitized_name:
                return file_path

    # Search in root notes directory
    for file_path in ROOT_NOTES_DIR.rglob("*.md"):
        if file_path.stem == note_name or note_name in file_path.stem:
            return file_path

    # Search in entire base directory
    for file_path in BASE_DIR.rglob("*.md"):
        if file_path.stem == note_name:
            # Check if it's a root note
            try:
                with open(file_path, encoding="utf-8") as f:
                    content = f.read()
                    if 'type: "root_note"' in content or "type: root_note" in content:
                        return file_path
            except:
                continue

    return None


def main():
    """Main execution function."""
    import sys

    print("=" * 60)
    print("OCDS Flashcard Generator from Root Notes")
    print("=" * 60)

    # Parse arguments
    if len(sys.argv) < 2:
        print('Usage: python generate_flashcards_from_root.py "Root Note Name" [--output-dir DIR]')
        print("\nExample:")
        print('  python generate_flashcards_from_root.py "Blood Stasis Pattern"')
        print('  python generate_flashcards_from_root.py "Blood Stasis Pattern" --output-dir "Materials/TCM_101"')
        sys.exit(1)

    note_name = sys.argv[1]
    output_dir = None

    # Check for output directory argument
    if "--output-dir" in sys.argv:
        idx = sys.argv.index("--output-dir")
        if idx + 1 < len(sys.argv):
            output_dir = Path(sys.argv[idx + 1])

    print(f"\n🔍 Searching for root note: {note_name}")

    # Find root note file
    root_note_path = find_root_note(note_name)
    if not root_note_path:
        print(f"❌ Root note not found: {note_name}")
        print("\nSearched in:")
        print(f"  - {ROOT_NOTES_DIR}")
        print(f"  - {BASE_DIR}")
        sys.exit(1)

    print(f"✅ Found root note: {root_note_path}")

    # Parse root note
    try:
        parser = RootNoteParser(root_note_path)
    except Exception as e:
        print(f"❌ Error parsing root note: {e}")
        sys.exit(1)

    # Generate flashcards
    generator = FlashcardGenerator(parser)
    generator.generate_all_flashcards()

    # Determine output path
    if output_dir:
        output_path = output_dir / "Flashcards.md"
    else:
        # Default: Materials/{class_id}/Flashcards.md
        output_path = MATERIALS_DIR / generator.class_id / "Flashcards.md"

    # Generate flashcard file
    generator.generate_flashcard_file(output_path)

    print("\n" + "=" * 60)
    print("✅ Flashcard generation complete!")
    print("=" * 60)
    print(f"\n📁 Output: {output_path}")
    print(f"🎴 Total cards: {len(generator.flashcards)}")


if __name__ == "__main__":
    main()
