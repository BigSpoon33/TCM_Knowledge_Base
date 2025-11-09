#!/usr/bin/env python3
"""
Master script to generate ALL OCDS materials from a root note using AI.
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from generate_flashcards_ai import FlashcardGeneratorAI
from generate_quiz_ai import QuizGeneratorAI
from generate_slides_ai import SlidesGeneratorAI
from conversation_engine import GuidedConversationEngine
from generate_flashcards_from_root import (
    RootNoteParser, 
    find_root_note,
    BASE_DIR,
    MATERIALS_DIR
)

class MaterialsPackageGenerator:
    """Generate complete OCDS materials package from root note."""

    def __init__(self, root_note_path: Path, class_id: str = None, week: int = None, output_dir: Path = None, api_key: str = None):
        self.root_note_path = root_note_path
        self.parser = RootNoteParser(root_note_path)
        self.metadata = self.parser.get_metadata()
        self.class_id = class_id or self._generate_class_id()
        self.week = week
        self.output_dir = output_dir or (MATERIALS_DIR / self.class_id)
        self.api_key = api_key
        
        self.results = {
            'flashcards': None, 'quiz': None, 'slides': None,
            'study_material': None, 'tasks': None
        }

    def _generate_class_id(self) -> str:
        domain = self.metadata.get('domain', 'TCM').replace(' ', '_')
        subject = self.metadata.get('subject', 'General').replace(' ', '_')
        return f"{domain}_{subject}"

    def generate_all(self, **skips):
        """Generate all materials."""
        print("\n" + "=" * 70)
        print("🎓 OCDS Complete Materials Generator (AI-Powered)")
        print("=" * 70)
        print(f"\n📘 Root Note: {self.metadata['name']}")
        print(f"🏫 Class ID: {self.class_id}")
        print(f"📁 Output Directory: {self.output_dir}")
        print("\n" + "-" * 70)

        self.output_dir.mkdir(parents=True, exist_ok=True)

        if not skips.get('skip_flashcards'): self._generate_flashcards()
        if not skips.get('skip_quiz'): self._generate_quiz()
        if not skips.get('skip_slides'): self._generate_slides()
        if not skips.get('skip_conversation'): self._generate_guided_conversation()
        if not skips.get('skip_study'): self._generate_study_material()
        if not skips.get('skip_tasks'): self._generate_tasks()

        self._print_summary()

    def _generate_flashcards(self):
        print("\n🎴 Generating Flashcards (AI)...")
        print("-" * 70)
        try:
            ai_gen = FlashcardGeneratorAI(api_key=self.api_key)
            flashcards = ai_gen.generate_from_content(
                content=self.parser.body, topic=self.metadata['name']
            )
            topic_slug = self.metadata['name'].replace(' ', '_')
            output_path = self.output_dir / f"{topic_slug}_Flashcards.md"
            self._write_flashcards_file(flashcards, output_path)
            self.results['flashcards'] = {'status': 'success', 'path': output_path, 'count': len(flashcards)}
        except Exception as e:
            print(f"❌ Error generating flashcards: {e}")
            self.results['flashcards'] = {'status': 'error', 'error': str(e)}

    def _generate_quiz(self):
        print("\n📝 Generating Quiz (AI)...")
        print("-" * 70)
        try:
            ai_gen = QuizGeneratorAI(api_key=self.api_key)
            questions = ai_gen.generate_from_content(
                content=self.parser.body, topic=self.metadata['name']
            )
            topic_slug = self.metadata['name'].replace(' ', '_')
            output_path = self.output_dir / f"{topic_slug}_Bank.md"
            self._write_quiz_file(questions, output_path)
            self.results['quiz'] = {'status': 'success', 'path': output_path, 'count': len(questions)}
        except Exception as e:
            print(f"❌ Error generating quiz: {e}")
            self.results['quiz'] = {'status': 'error', 'error': str(e)}

    def _write_flashcards_file(self, flashcards: list, output_path: Path):
        """Generate flashcards file from a list of cards."""
        topic_name = self.metadata['name']
        today = datetime.now().strftime("%Y-%m-%d")
        
        content = f"""---
ocds_type: flashcard
material_id: flashcards_{self.class_id.lower()}_{topic_name.replace(' ', '_').lower()}
class_id: {self.class_id}
title: "{topic_name} Flashcards"
description: Spaced repetition flashcards for {topic_name}
topic: {topic_name}
total_cards: {len(flashcards)}
---

# {topic_name} Flashcards
"""
        for card in flashcards:
            content += f"\n## {topic_name}\n{card['question']}\n?\n{card['answer']}\n\n---"
            
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Flashcards file created: {output_path}")

    def _write_quiz_file(self, questions: list, output_path: Path):
        """Generate quiz bank file from a list of questions."""
        topic_name = self.metadata['name']
        today = datetime.now().strftime("%Y-%m-%d")

        content = f"""---
ocds_type: question_bank
material_id: bank_{self.class_id.lower()}_{topic_name.replace(' ', '_').lower()}
class_id: {self.class_id}
title: "{topic_name} Question Bank"
description: Question bank for {topic_name}
topic: {topic_name}
total_questions: {len(questions)}
---

# {topic_name} Question Bank
"""
        for i, q in enumerate(questions):
            content += f"\n### Question {i+1}\n\n**{q['question']}**\n\n"
            content += f"**Correct Answer:** {q['correct_answer']}\n\n"
            content += f"**Explanation:** {q['explanation']}\n\n"
            content += f"**Options:**\n"
            for opt in q['options']:
                content += f"- {opt}\n"
            content += "\n---"

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Question Bank file created: {output_path}")

    def _generate_slides(self):
        print("\n🎬 Generating Slides (AI)...")
        print("-" * 70)
        try:
            ai_gen = SlidesGeneratorAI(api_key=self.api_key)
            
            # Determine if this is a pattern or general topic
            category = self.metadata.get('category', '')
            if isinstance(category, list):
                category = ' '.join(category)
            category = str(category).lower()
            is_pattern = 'pattern' in category or 'deficiency' in self.metadata['name'].lower()
            
            if is_pattern:
                slides_content = ai_gen.generate_pattern_slides(
                    content=self.parser.body,
                    pattern_name=self.metadata['name']
                )
            else:
                slides_content = ai_gen.generate_from_content(
                    content=self.parser.body,
                    topic=self.metadata['name']
                )
            
            topic_slug = self.metadata['name'].replace(' ', '_')
            output_path = self.output_dir / f"{topic_slug}_Slides.md"
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(slides_content)
            
            # Count slides (approximate by counting slide separators)
            slide_count = slides_content.count('\n---\n') + slides_content.count('\n----\n')
            
            print(f"✅ Slides created: {output_path}")
            self.results['slides'] = {'status': 'success', 'path': output_path, 'count': slide_count}
        except Exception as e:
            print(f"❌ Error generating slides: {e}")
            self.results['slides'] = {'status': 'error', 'error': str(e)}

    def _generate_guided_conversation(self):
        print("\n💬 Generating Guided Conversation...")
        print("-" * 70)
        try:
            engine = GuidedConversationEngine(self.root_note_path, api_key=self.api_key)
            script = engine._generate_conversation_script()
            
            topic_slug = self.metadata['name'].replace(' ', '_')
            output_path = self.output_dir / f"{topic_slug}_Guided_Conversation.md"
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(script)
            
            heading_count = len(engine.state.headings)
            print(f"✅ Guided conversation created: {output_path}")
            self.results['guided_conversation'] = {'status': 'success', 'path': output_path, 'count': heading_count}
        except Exception as e:
            print(f"❌ Error generating guided conversation: {e}")
            self.results['guided_conversation'] = {'status': 'error', 'error': str(e)}

    def _generate_study_material(self):
        print("\n📚 Generating Study Material...")
        print("-" * 70)
        topic_slug = self.metadata['name'].replace(' ', '_')
        output_path = self.output_dir / f"{topic_slug}_Study_Material.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# Study Guide for {self.metadata['name']}\n\n*This is an auto-generated study guide.*")
        print(f"✅ Study material created: {output_path}")
        self.results['study_material'] = {'status': 'success', 'path': output_path}

    def _generate_tasks(self):
        print("\n✅ Generating Tasks...")
        print("-" * 70)
        topic_slug = self.metadata['name'].replace(' ', '_')
        output_path = self.output_dir / f"{topic_slug}_Tasks.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# Tasks for {self.metadata['name']}\n\n- [ ] Review the generated flashcards.\n- [ ] Take the generated quiz.")
        print(f"✅ Tasks file created: {output_path}")
        self.results['tasks'] = {'status': 'success', 'path': output_path}

    def _print_summary(self):
        print("\n" + "=" * 70)
        print("📊 Generation Summary")
        print("=" * 70)
        for material_type, result in self.results.items():
            if not result: continue
            status = result.get('status', 'unknown')
            if status == 'success':
                print(f"✅ {material_type.title()}: {result.get('path')} ({result.get('count', 0)} items)")
            else:
                print(f"❌ {material_type.title()}: {status} - {result.get('reason') or result.get('error')}")
        print("\n" + "=" * 70)

def main():
    parser = argparse.ArgumentParser(description='Generate OCDS materials from a root note using AI.')
    parser.add_argument('root_note', help='Name of the root note file')
    parser.add_argument('--class-id', help='Class ID (e.g., TCM_101)')
    args = parser.parse_args()
    
    print(f"🔍 Searching for root note: {args.root_note}")
    root_note_path = find_root_note(args.root_note)
    
    if not root_note_path:
        print(f"❌ Root note not found: {args.root_note}")
        sys.exit(1)
    
    print(f"✅ Found root note: {root_note_path}")
    
    generator = MaterialsPackageGenerator(root_note_path=root_note_path, class_id=args.class_id)
    generator.generate_all()

if __name__ == "__main__":
    main()
