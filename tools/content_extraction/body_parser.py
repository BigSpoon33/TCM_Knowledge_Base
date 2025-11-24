#!/usr/bin/env python3
"""
Body Parser - Extracts structured data from root note markdown body.
"""

import re
from typing import Any


class BodyParser:
    """Parses markdown body to extract structured data for materials."""

    def __init__(self, markdown_content: str):
        self.content = markdown_content

    def extract_from_heading(self, heading: str) -> str:
        """Extract content under a specific heading."""
        pattern = rf"##\s*{re.escape(heading)}\s*\n(.*?)(?=\n##\s*|\n---|\Z)"
        match = re.search(pattern, self.content, re.DOTALL | re.IGNORECASE)
        return match.group(1).strip() if match else ""

    def extract_flashcard_seeds(self) -> list[dict[str, str]]:
        """Extract flashcard Q&A pairs from markdown."""
        seeds = []
        flashcard_section = self.extract_from_heading("Flashcard Seeds")
        if not flashcard_section:
            return []

        pattern = r"-\s*Q:\s*(.+?)\n-\s*A:\s*(.+?)(?=\n-\s*Q:|\s*\Z)"
        matches = re.findall(pattern, flashcard_section, re.DOTALL)

        for question, answer in matches:
            seeds.append({"question": question.strip(), "answer": answer.strip()})
        return seeds

    def extract_quiz_seeds(self) -> list[dict[str, Any]]:
        """Extract quiz questions from markdown."""
        seeds = []
        quiz_section = self.extract_from_heading("Quiz Seeds")
        if not quiz_section:
            return []

        # Split scenarios by '###' headings
        scenarios = re.split(r"\n###\s*", quiz_section)
        for scenario_text in scenarios:
            if not scenario_text.strip() or "**Question:**" not in scenario_text:
                continue

            q_match = re.search(r"\*\*Question:\*\*(.+?)\n", scenario_text, re.DOTALL)
            o_match = re.search(r"\*\*Options:\*\*(.+?)\n\n", scenario_text, re.DOTALL)
            ca_match = re.search(r"\*\*Correct Answer:\*\*(.+?)\n", scenario_text, re.DOTALL)
            ex_match = re.search(r"\*\*Explanation:\*\*(.+)", scenario_text, re.DOTALL)

            if q_match and o_match and ca_match and ex_match:
                question = q_match.group(1).strip()
                options_text = o_match.group(1).strip()
                correct = ca_match.group(1).strip()
                explanation = ex_match.group(1).strip()

                options = []
                option_lines = [opt.strip() for opt in options_text.split("\n-") if opt.strip()]
                for line in option_lines:
                    letter, text = line.split(")", 1)
                    options.append({"letter": letter.strip(), "text": text.strip()})

                seeds.append(
                    {
                        "question": question,
                        "options": options,
                        "correct_answer": correct,
                        "explanation": explanation,
                        "type": "multiple_choice",
                    }
                )
        return seeds

    def extract_core_concepts(self) -> list[dict[str, str]]:
        """Extract core concepts from markdown lists."""
        concepts = []
        concept_section = self.extract_from_heading("Core Concepts")
        if not concept_section:
            return []

        pattern = r"-\s*\*\*(.+?):\*\*\s*(.+?)(?=\n-\s*\*|\s*\Z)"
        matches = re.findall(pattern, concept_section, re.DOTALL)

        for name, description in matches:
            concepts.append({"name": name.strip(), "description": description.strip()})
        return concepts


if __name__ == "__main__":
    test_content = """
    # Test Note

    ## Clinical Manifestations
    - **Symptom 1:** Description 1
    - **Symptom 2:** Description 2

    ---
    # Assessment Data

    ## Flashcard Seeds
    - Q: What is a test question?
    - A: This is a test answer.
    - Q: What is another question?
    - A: Another answer.

    ## Quiz Seeds
    ### Clinical Scenario 1
    **Question:** A test patient presents with symptoms. What is the pattern?

    **Options:**
    - A) Pattern A
    - B) Pattern B

    **Correct Answer:** A

    **Explanation:** Because of reasons.
    
    ## Core Concepts
    - **Concept 1:** This is the first concept.
    - **Concept 2:** This is the second concept.
    """
    parser = BodyParser(test_content)

    print("--- Flashcard Seeds ---")
    print(parser.extract_flashcard_seeds())

    print("\n--- Quiz Seeds ---")
    print(parser.extract_quiz_seeds())

    print("\n--- Core Concepts ---")
    print(parser.extract_core_concepts())

    print("\n--- Content from Heading ---")
    print(parser.extract_from_heading("Clinical Manifestations"))

    print("\n✅ Body Parser Test Complete")
