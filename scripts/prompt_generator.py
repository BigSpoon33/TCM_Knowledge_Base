#!/usr/bin/env python3
"""
Prompt Generator - Generates dynamic prompts for guided conversation.
"""

import os
from typing import List, Dict, Any
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from gemini_research import GeminiDeepResearch


class PromptGenerator:
    """Generates conversation prompts based on heading and context."""

    def __init__(self, api_key: str = None):
        """
        Initialize prompt generator.

        Args:
            api_key (str): Gemini API key. If None, uses GEMINI_API_KEY env var.
        """
        self.api_key = api_key or os.environ.get('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set.")
        self.researcher = GeminiDeepResearch(api_key=self.api_key)

    def generate_initial_prompt(
        self,
        heading_title: str,
        content: str,
        is_first_heading: bool = False
    ) -> str:
        """
        Generate opening question for a heading.

        Args:
            heading_title (str): Title of the heading.
            content (str): Content of the heading.
            is_first_heading (bool): Whether this is the first heading.

        Returns:
            str: Opening question.
        """
        # Use predefined templates for common headings
        templates = {
            'Overview': "What do you know about {topic}?",
            'Clinical Manifestations': "What are the cardinal symptoms and diagnostic features of {topic}?",
            'Etiology & Pathomechanisms': "What causes {topic} and how does it develop?",
            'Differential Diagnosis': "How would you distinguish {topic} from similar patterns?",
            'Treatment Principles': "What are the main treatment principles for {topic}?",
            'Herbal Formulas': "What are the key herbal formulas used for {topic}?",
            'Acupuncture Points': "Which acupuncture points would you use for {topic}?",
            'Clinical Applications': "How would you apply your knowledge of {topic} in clinical practice?",
            'Study Tips': "What strategies would help you remember the key concepts of {topic}?"
        }

        # Check if we have a template for this heading
        for template_key, template in templates.items():
            if template_key.lower() in heading_title.lower():
                # Extract topic from content or use generic
                return template.format(topic=heading_title)

        # Generate custom prompt using AI
        prompt = f"""
Generate a clear, open-ended question to test a TCM student's understanding of this topic.

HEADING: {heading_title}

CONTENT PREVIEW:
{content[:500]}

The question should:
1. Be open-ended (not yes/no)
2. Encourage the student to explain in their own words
3. Cover the main concepts in this section
4. Be appropriate for a TCM student
5. Be concise (one sentence)

Return ONLY the question, no other text.
"""

        result = self.researcher.research(prompt, use_search=False)
        return result['content'].strip()

    def generate_reinforcement_prompt(
        self,
        heading_title: str,
        missing_concepts: List[str],
        attempt_number: int
    ) -> str:
        """
        Generate follow-up prompt to reinforce learning.

        Args:
            heading_title (str): Title of the heading.
            missing_concepts (List[str]): Concepts student is missing.
            attempt_number (int): Which attempt this is.

        Returns:
            str: Follow-up question.
        """
        if not missing_concepts:
            return f"Can you explain {heading_title} in more detail?"

        # Focus on 1-2 missing concepts
        focus_concepts = missing_concepts[:2]
        concepts_str = " and ".join(focus_concepts)

        if attempt_number == 1:
            return f"Let's focus on {concepts_str}. Can you explain this concept?"
        elif attempt_number == 2:
            return f"Can you describe {concepts_str} in your own words?"
        else:
            return f"What do you remember about {concepts_str}?"

    def generate_explanation(
        self,
        heading_title: str,
        content: str,
        missing_concepts: List[str]
    ) -> str:
        """
        Generate AI explanation of missing concepts.

        Args:
            heading_title (str): Title of the heading.
            content (str): Reference content.
            missing_concepts (List[str]): Concepts to explain.

        Returns:
            str: Explanation text.
        """
        if not missing_concepts:
            return "Let me provide some additional context to help solidify your understanding."

        concepts_list = "\n".join([f"- {concept}" for concept in missing_concepts])

        prompt = f"""
You are a TCM educator providing a clear, concise explanation.

TOPIC: {heading_title}

The student needs help understanding:
{concepts_list}

REFERENCE CONTENT:
{content[:2000]}

Provide a brief explanation (2-3 paragraphs) that:
1. Explains the missing concepts clearly
2. Uses clinical examples or analogies
3. Connects to practical application
4. Is encouraging and supportive

Keep it concise and focused.
"""

        result = self.researcher.research(prompt, use_search=False)
        return result['content'].strip()

    def generate_encouragement(self, score: float, level: str) -> str:
        """
        Generate encouraging message based on performance.

        Args:
            score (float): Assessment score.
            level (str): Assessment level (poor/fair/good).

        Returns:
            str: Encouraging message.
        """
        if level == 'good':
            messages = [
                "Excellent work! You've demonstrated a solid understanding.",
                "Great job! You clearly grasp the key concepts.",
                "Well done! Your explanation shows good comprehension.",
                "Outstanding! You've mastered this section."
            ]
        elif level == 'fair':
            messages = [
                "You're on the right track! Let's refine your understanding.",
                "Good start! Let's fill in a few gaps.",
                "You've got some key points. Let's build on that.",
                "Nice effort! Let's clarify a few concepts."
            ]
        else:  # poor
            messages = [
                "No worries! Let's work through this together.",
                "This is challenging material. Let's break it down.",
                "Let's take another approach to this concept.",
                "Don't be discouraged! We'll get there step by step."
            ]

        import random
        return random.choice(messages)

    def generate_summary_prompt(self, heading_title: str) -> str:
        """
        Generate prompt asking student to summarize what they learned.

        Args:
            heading_title (str): Title of the heading.

        Returns:
            str: Summary prompt.
        """
        return f"Before we move on, can you briefly summarize the key points about {heading_title}?"


if __name__ == '__main__':
    # Test the prompt generator
    generator = PromptGenerator()

    print("Testing Prompt Generator...\n")

    # Test initial prompt
    heading = "Clinical Manifestations"
    content = """
    Cardinal Symptoms:
    - Dry Cough
    - Dryness
    - Deficiency Heat
    """

    print("1. Initial Prompt:")
    prompt = generator.generate_initial_prompt(heading, content)
    print(f"   {prompt}\n")

    # Test reinforcement prompt
    print("2. Reinforcement Prompt:")
    missing = ["deficiency heat", "tongue presentation"]
    prompt = generator.generate_reinforcement_prompt(heading, missing, 1)
    print(f"   {prompt}\n")

    # Test encouragement
    print("3. Encouragement Messages:")
    for level in ['good', 'fair', 'poor']:
        msg = generator.generate_encouragement(70, level)
        print(f"   {level.upper()}: {msg}")
