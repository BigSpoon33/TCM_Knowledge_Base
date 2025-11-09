#!/usr/bin/env python3
"""
Generate Flashcards with AI - Uses Gemini to create flashcards from a root note.
"""

import os
import re
from typing import Dict, List, Any
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from gemini_research import GeminiDeepResearch

class FlashcardGeneratorAI:
    """Generates flashcards from root note content using AI."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set.")
        self.researcher = GeminiDeepResearch(api_key=self.api_key)

    def generate_from_content(self, content: str, topic: str, num_cards: int = 10) -> List[Dict[str, str]]:
        """Generates flashcards from the body of a root note."""
        print(f"🧠 Generating {num_cards} flashcards for '{topic}' using AI...")

        prompt = f"""
        Based on the following content about "{topic}", generate {num_cards} high-quality flashcards.
        Each flashcard should be in the format:
        Q: [Question]
        A: [Answer]

        The questions should cover the most important concepts, definitions, and clinical details.
        Provide concise and accurate answers.

        ---
        CONTENT:
        {content[:8000]}
        ---

        Generate the flashcards now.
        """

        result = self.researcher.research(prompt, use_search=False)
        ai_content = result['content']

        # Parse the AI-generated content
        flashcards = []
        pattern = r'Q:\s*(.+?)\nA:\s*(.+?)(?=\nQ:|\Z)'
        matches = re.findall(pattern, ai_content, re.DOTALL)

        for q, a in matches:
            flashcards.append({'question': q.strip(), 'answer': a.strip()})
        
        print(f"✅ Generated {len(flashcards)} flashcards.")
        return flashcards

if __name__ == '__main__':
    test_content = """
    ## Clinical Manifestations
    - **Cardinal Symptoms:** Fatigue, poor appetite, loose stools, abdominal distention.
    - **Tongue:** Pale, swollen, with teeth marks.
    - **Pulse:** Weak (ruo) or empty (xu).
    
    ## Treatment Principles
    - **Primary Principle:** Tonify Spleen Qi.
    - **Key Formula:** Si Jun Zi Tang (Four Gentlemen Decoction).
    """
    generator = FlashcardGeneratorAI()
    cards = generator.generate_from_content(test_content, "Spleen Qi Deficiency")
    
    for card in cards:
        print(f"Q: {card['question']}\nA: {card['answer']}\n")
