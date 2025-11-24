#!/usr/bin/env python3
"""
Generate Quiz with AI - Uses Gemini to create a quiz from a root note.
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Any

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from gemini_research import GeminiDeepResearch


class QuizGeneratorAI:
    """Generates a quiz from root note content using AI."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set.")
        self.researcher = GeminiDeepResearch(api_key=self.api_key)

    def generate_from_content(self, content: str, topic: str, num_questions: int = 5) -> list[dict[str, Any]]:
        """Generates a quiz from the body of a root note."""
        print(f"🧠 Generating {num_questions} quiz questions for '{topic}' using AI...")

        prompt = f"""
        Based on the following content about "{topic}", generate a {num_questions}-question multiple-choice quiz.
        Format the output as a JSON array, where each object has "question", "options" (an array of 4 strings), "correct_answer" (the full text of the correct option), and "explanation".

        ---
        CONTENT:
        {content[:8000]}
        ---

        Generate the JSON quiz now.
        """

        result = self.researcher.research(prompt, use_search=False)
        ai_content = result["content"]

        # Clean and parse the JSON
        try:
            # Remove markdown and backticks
            cleaned_json = re.sub(r"```json\n|\n```", "", ai_content).strip()
            quiz_data = json.loads(cleaned_json)
            print(f"✅ Generated {len(quiz_data)} quiz questions.")
            return quiz_data
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing JSON from AI response: {e}")
            print(f"Raw response:\n{ai_content}")
            return []


if __name__ == "__main__":
    test_content = """
    ## Clinical Manifestations
    - **Cardinal Symptoms:** Fatigue, poor appetite, loose stools, abdominal distention.
    - **Tongue:** Pale, swollen, with teeth marks.
    - **Pulse:** Weak (ruo) or empty (xu).
    
    ## Treatment Principles
    - **Primary Principle:** Tonify Spleen Qi.
    - **Key Formula:** Si Jun Zi Tang (Four Gentlemen Decoction).
    - **Differentiation:** Must be differentiated from Spleen Yang Deficiency, which has more cold signs.
    """
    generator = QuizGeneratorAI()
    questions = generator.generate_from_content(test_content, "Spleen Qi Deficiency")

    for q in questions:
        print(json.dumps(q, indent=2))
