#!/usr/bin/env python3
"""
Understanding Assessor - AI-powered assessment of student responses.
"""

import os
import re
import json
from typing import Dict, List, Any
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from gemini_research import GeminiDeepResearch


class UnderstandingAssessor:
    """Assesses student understanding using AI."""

    def __init__(self, api_key: str = None):
        """
        Initialize assessor.

        Args:
            api_key (str): Gemini API key. If None, uses GEMINI_API_KEY env var.
        """
        self.api_key = api_key or os.environ.get('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set.")
        self.researcher = GeminiDeepResearch(api_key=self.api_key)

    def assess_response(
        self,
        question: str,
        student_response: str,
        reference_content: str,
        heading_title: str = ""
    ) -> Dict[str, Any]:
        """
        Assess student understanding based on their response.

        Args:
            question (str): The question asked.
            student_response (str): Student's response.
            reference_content (str): Reference content from root note.
            heading_title (str): Title of the heading being assessed.

        Returns:
            Dict with assessment results:
            {
                'score': 0-100,
                'level': 'poor'|'fair'|'good',
                'missing_concepts': [...],
                'misconceptions': [...],
                'strengths': [...],
                'feedback': "...",
                'next_action': 'reinforce'|'advance'
            }
        """
        prompt = f"""
You are an expert TCM educator assessing a student's understanding.

HEADING: {heading_title}

QUESTION ASKED:
{question}

STUDENT'S RESPONSE:
{student_response}

REFERENCE CONTENT (What they should know):
{reference_content[:3000]}

---

ASSESSMENT TASK:
Evaluate the student's response on a scale of 0-100:
- 0-40: POOR - Missing key concepts, major gaps in understanding, or significant misconceptions
- 41-70: FAIR - Partial understanding, some key concepts present but incomplete or imprecise
- 71-100: GOOD - Demonstrates solid understanding, can explain concepts clearly

Provide your assessment in the following JSON format:
{{
  "score": <number 0-100>,
  "level": "<poor|fair|good>",
  "missing_concepts": ["concept1", "concept2", ...],
  "misconceptions": ["misconception1", ...],
  "strengths": ["what they got right1", "what they got right2", ...],
  "feedback": "<constructive feedback for the student>",
  "next_action": "<reinforce|advance>"
}}

GUIDELINES:
1. Be encouraging but honest
2. Identify specific missing concepts (not vague statements)
3. Note any misconceptions that need correction
4. Highlight what they got right
5. Provide actionable feedback
6. If score >= 71, next_action should be "advance"
7. If score < 71, next_action should be "reinforce"

Return ONLY the JSON object, no other text.
"""

        try:
            result = self.researcher.research(prompt, use_search=False)
            assessment = self._parse_assessment(result['content'])
            return assessment
        except Exception as e:
            print(f"Error in assessment: {e}")
            # Return default assessment on error
            return {
                'score': 50,
                'level': 'fair',
                'missing_concepts': [],
                'misconceptions': [],
                'strengths': [],
                'feedback': "Unable to assess response. Please try again.",
                'next_action': 'reinforce'
            }

    def _parse_assessment(self, ai_response: str) -> Dict[str, Any]:
        """
        Parse AI response into structured assessment.

        Args:
            ai_response (str): Raw AI response.

        Returns:
            Dict with assessment data.
        """
        # Try to extract JSON from response
        # Sometimes AI wraps JSON in markdown code blocks
        json_match = re.search(r'```json\s*(\{.*?\})\s*```', ai_response, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            # Try to find JSON object directly
            json_match = re.search(r'\{.*\}', ai_response, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
            else:
                raise ValueError("No JSON found in AI response")

        try:
            assessment = json.loads(json_str)

            # Validate required fields
            required_fields = ['score', 'level', 'missing_concepts', 'misconceptions',
                             'strengths', 'feedback', 'next_action']
            for field in required_fields:
                if field not in assessment:
                    assessment[field] = [] if field in ['missing_concepts', 'misconceptions', 'strengths'] else ""

            # Ensure score is in range
            assessment['score'] = max(0, min(100, assessment['score']))

            # Ensure level matches score
            if assessment['score'] >= 71:
                assessment['level'] = 'good'
                assessment['next_action'] = 'advance'
            elif assessment['score'] >= 41:
                assessment['level'] = 'fair'
                assessment['next_action'] = 'reinforce'
            else:
                assessment['level'] = 'poor'
                assessment['next_action'] = 'reinforce'

            return assessment

        except json.JSONDecodeError as e:
            print(f"JSON parse error: {e}")
            print(f"Response was: {ai_response[:500]}")
            raise

    def generate_reinforcement_explanation(
        self,
        heading_title: str,
        reference_content: str,
        missing_concepts: List[str]
    ) -> str:
        """
        Generate explanation to reinforce missing concepts.

        Args:
            heading_title (str): Title of the heading.
            reference_content (str): Reference content.
            missing_concepts (List[str]): Concepts student is missing.

        Returns:
            str: Explanation text.
        """
        if not missing_concepts:
            return "Let me provide some additional context to help solidify your understanding."

        concepts_list = "\n".join([f"- {concept}" for concept in missing_concepts])

        prompt = f"""
You are a TCM educator providing a clear, concise explanation to help a student.

TOPIC: {heading_title}

The student is missing understanding of these concepts:
{concepts_list}

REFERENCE CONTENT:
{reference_content[:2000]}

---

Provide a brief, clear explanation (2-3 paragraphs) that:
1. Explains the missing concepts in simple terms
2. Uses clinical examples or analogies where helpful
3. Connects concepts to the bigger picture
4. Is encouraging and supportive

Keep it concise and focused on the missing concepts.
"""

        result = self.researcher.research(prompt, use_search=False)
        return result['content'].strip()

    def generate_follow_up_question(
        self,
        heading_title: str,
        missing_concepts: List[str],
        attempt_number: int
    ) -> str:
        """
        Generate a follow-up question to test understanding.

        Args:
            heading_title (str): Title of the heading.
            missing_concepts (List[str]): Concepts to focus on.
            attempt_number (int): Which attempt this is.

        Returns:
            str: Follow-up question.
        """
        concepts_focus = ", ".join(missing_concepts[:3]) if missing_concepts else "the key concepts"

        prompt = f"""
You are a TCM educator creating a follow-up question.

TOPIC: {heading_title}
FOCUS AREAS: {concepts_focus}
ATTEMPT NUMBER: {attempt_number}

Generate a clear, specific question that:
1. Tests understanding of the focus areas
2. Is appropriate for attempt #{attempt_number} (make it slightly easier if attempt > 1)
3. Encourages the student to explain in their own words
4. Can be answered in 2-3 sentences

Return ONLY the question, no other text.
"""

        result = self.researcher.research(prompt, use_search=False)
        return result['content'].strip()


if __name__ == '__main__':
    # Test the assessor
    assessor = UnderstandingAssessor()

    # Test case
    question = "What are the fundamental characteristics of Lung Yin Deficiency?"
    student_response = "It's when the lungs are dry and there's some heat."
    reference = """
    Fundamental Characteristics:
    - Dryness: A lack of fluids to moisten the Lung
    - Deficiency Heat: A "false heat" arising from relative excess of Yang
    - Impaired Lung Function: The Lung's ability to govern Qi and fluids is compromised
    """

    print("Testing Understanding Assessor...")
    print(f"\nQuestion: {question}")
    print(f"Student Response: {student_response}")
    print("\nAssessing...\n")

    assessment = assessor.assess_response(question, student_response, reference, "Fundamental Characteristics")

    print(f"Score: {assessment['score']}/100")
    print(f"Level: {assessment['level']}")
    print(f"Missing Concepts: {assessment['missing_concepts']}")
    print(f"Strengths: {assessment['strengths']}")
    print(f"Feedback: {assessment['feedback']}")
    print(f"Next Action: {assessment['next_action']}")
