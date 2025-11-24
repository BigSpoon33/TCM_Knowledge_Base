#!/usr/bin/env python3
"""
Conversation Engine - Main orchestrator for guided learning conversations.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from conversation_state import ConversationState
from prompt_generator import PromptGenerator
from understanding_assessor import UnderstandingAssessor


class GuidedConversationEngine:
    """Main conversation orchestrator for guided learning."""

    def __init__(self, root_note_path: Path, api_key: str = None, max_attempts: int = 3):
        """
        Initialize conversation engine.

        Args:
            root_note_path (Path): Path to root note file.
            api_key (str): Gemini API key.
            max_attempts (int): Maximum attempts per heading before moving on.
        """
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set.")

        self.state = ConversationState(root_note_path)
        self.assessor = UnderstandingAssessor(api_key=self.api_key)
        self.prompt_gen = PromptGenerator(api_key=self.api_key)
        self.max_attempts = max_attempts

    def start_conversation(self, interactive: bool = True):
        """
        Begin guided conversation.

        Args:
            interactive (bool): If True, runs interactive CLI. If False, returns conversation flow.
        """
        if interactive:
            self._run_interactive()
        else:
            return self._generate_conversation_script()

    def _run_interactive(self):
        """Run interactive CLI conversation."""
        self._print_welcome()

        while not self.state.is_complete():
            self._process_heading_interactive()

        self._print_summary()

    def _print_welcome(self):
        """Print welcome message."""
        print("\n" + "=" * 70)
        print("🎓 TCM GUIDED LEARNING CONVERSATION")
        print("=" * 70)
        print(f"\n📘 Topic: {self.state.topic_name}")
        print(f"📊 Total Sections: {len(self.state.headings)}")
        print("\nThis conversation will guide you through each section of the topic.")
        print("Answer each question to the best of your ability.")
        print("The AI will assess your understanding and provide feedback.\n")
        print("Type 'skip' to skip a section, 'quit' to exit.\n")
        print("=" * 70 + "\n")

    def _process_heading_interactive(self):
        """Process current heading in interactive mode."""
        heading = self.state.get_current_heading()
        if not heading:
            return

        attempts = 0
        is_first_attempt = True

        while attempts < self.max_attempts:
            # Generate prompt
            if is_first_attempt:
                question = self.prompt_gen.generate_initial_prompt(
                    heading["title"], heading["content"], is_first_heading=(self.state.current_heading_index == 0)
                )
                is_first_attempt = False
            else:
                missing = self.state.get_missing_concepts()
                question = self.prompt_gen.generate_reinforcement_prompt(heading["title"], missing, attempts)

            # Display progress and question
            self._print_progress()
            print(f"\n📌 {heading['title']}")
            print(f"\n❓ {question}\n")

            # Get student response
            response = input("Your answer (or 'skip'/'quit'): ").strip()

            # Handle special commands
            if response.lower() == "quit":
                print("\n👋 Exiting conversation. Progress saved.")
                self._save_progress()
                return
            elif response.lower() == "skip":
                print("\n⏭️  Skipping this section.\n")
                self.state.advance_heading()
                return
            elif not response:
                print("⚠️  Please provide an answer.\n")
                continue

            # Assess response
            print("\n🤔 Assessing your response...\n")
            assessment = self.assessor.assess_response(question, response, heading["content"], heading["title"])

            # Record response
            self.state.record_response(question, response, assessment)

            # Display assessment
            self._print_assessment(assessment)

            # Check if ready to advance
            if assessment["next_action"] == "advance":
                encouragement = self.prompt_gen.generate_encouragement(assessment["score"], assessment["level"])
                print(f"\n✅ {encouragement}")
                print("Moving to next section...\n")
                self.state.advance_heading()
                return
            else:
                # Provide reinforcement
                attempts += 1
                if attempts < self.max_attempts:
                    print("\n💡 Let me help clarify...\n")
                    explanation = self.assessor.generate_reinforcement_explanation(
                        heading["title"], heading["content"], assessment["missing_concepts"]
                    )
                    print(f"{explanation}\n")
                    print("Let's try again with a focused question.\n")

        # Max attempts reached
        print(f"\n⏭️  You've made {self.max_attempts} attempts. Let's move on for now.")
        print("You can review this section later.\n")
        self.state.advance_heading()

    def _print_progress(self):
        """Print progress bar."""
        total = len(self.state.headings)
        completed = len(self.state.completed_headings)
        percentage = self.state.get_progress_percentage()

        # Progress bar
        bar_length = 30
        filled = int(bar_length * completed / total)
        bar = "█" * filled + "░" * (bar_length - filled)

        print(f"\nProgress: [{bar}] {completed}/{total} sections ({percentage:.0f}%)")

    def _print_assessment(self, assessment: dict):
        """Print assessment results."""
        score = assessment["score"]
        level = assessment["level"]

        # Color-coded score display (using emojis since we can't use ANSI colors easily)
        if level == "good":
            emoji = "🟢"
        elif level == "fair":
            emoji = "🟡"
        else:
            emoji = "🔴"

        print(f"{emoji} Score: {score}/100 ({level.upper()})")

        if assessment["strengths"]:
            print("\n✅ What you got right:")
            for strength in assessment["strengths"]:
                print(f"   • {strength}")

        if assessment["missing_concepts"]:
            print("\n⚠️  Areas to review:")
            for concept in assessment["missing_concepts"]:
                print(f"   • {concept}")

        if assessment["misconceptions"]:
            print("\n❌ Misconceptions to correct:")
            for misconception in assessment["misconceptions"]:
                print(f"   • {misconception}")

        print(f"\n📝 Feedback: {assessment['feedback']}")

    def _print_summary(self):
        """Print final summary."""
        summary = self.state.get_summary()

        print("\n" + "=" * 70)
        print("🎉 CONVERSATION COMPLETE!")
        print("=" * 70)
        print(f"\n📘 Topic: {summary['topic']}")
        print(f"⏱️  Total Time: {summary['total_time_minutes']} minutes")
        print(f"📊 Sections Completed: {summary['completed_headings']}/{summary['total_headings']}")
        print(f"🎯 Overall Average Score: {summary['overall_average_score']}/100")

        if summary["strong_areas"]:
            print("\n💪 Strong Areas:")
            for area in summary["strong_areas"]:
                print(f"   ✅ {area}")

        if summary["weak_areas"]:
            print("\n📚 Areas for Review:")
            for area in summary["weak_areas"]:
                print(f"   📖 {area}")

        print("\n" + "=" * 70)

        # Save final state
        self._save_progress()

    def _save_progress(self):
        """Save conversation progress."""
        output_dir = Path("Materials/TCM_101/conversation_logs")
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = self.state.start_time.strftime("%Y%m%d_%H%M%S")
        topic_slug = self.state.topic_name.replace(" ", "_")
        output_file = output_dir / f"{topic_slug}_conversation_{timestamp}.json"

        self.state.save_state(output_file)
        print(f"\n💾 Progress saved to: {output_file}")

    def _generate_conversation_script(self) -> str:
        """
        Generate a markdown conversation script (non-interactive).

        Returns:
            str: Markdown content for conversation guide.
        """
        content = f"""---
ocds_type: guided_conversation
material_id: conversation_{self.state.topic_name.lower().replace(" ", "_")}
class_id: TCM_101
title: "{self.state.topic_name} - Guided Learning Conversation"
topic: {self.state.topic_name}
total_headings: {len(self.state.headings)}
estimated_time: {len(self.state.headings) * 5}-{len(self.state.headings) * 8} minutes
---

# {self.state.topic_name} - Guided Learning Conversation

## How to Use This Guide

This guided conversation will help you master {self.state.topic_name} through active recall and discussion. Work through each section, testing your knowledge before reviewing the content.

**Instructions:**
1. Read each question carefully
2. Answer in your own words before looking at the reference content
3. Compare your answer to the key concepts
4. If you're missing concepts, review the explanation and try again

---

"""

        for i, heading in enumerate(self.state.headings):
            content += f"""
## {i + 1}. {heading["title"]}

**Question:**
{self.prompt_gen.generate_initial_prompt(heading["title"], heading["content"])}

**Key Concepts to Cover:**
{self._extract_key_concepts(heading["content"])}

**Assessment Criteria:**
- Can you explain the main concepts clearly?
- Can you provide clinical examples?
- Can you relate this to other concepts?

**Reference Content:**
{heading["content"][:500]}...

---

"""

        return content

    def _extract_key_concepts(self, content: str) -> str:
        """Extract key concepts from content."""
        # Simple extraction - look for bullet points
        lines = content.split("\n")
        concepts = []
        for line in lines[:10]:  # First 10 lines
            if line.strip().startswith("*") or line.strip().startswith("-"):
                concepts.append(line.strip())

        if concepts:
            return "\n".join(concepts[:5])  # Top 5
        else:
            return "- Review the main points in this section"


if __name__ == "__main__":
    # Test the engine
    root_note = Path(
        "/home/shuma/Documents/AI_Suite/TCM_Knowledge_Base/Materials/TCM_101/Root_Note_Lung_Yin_Deficiency.md"
    )

    print("Initializing Guided Conversation Engine...")
    engine = GuidedConversationEngine(root_note)

    print(f"\nTopic: {engine.state.topic_name}")
    print(f"Headings: {len(engine.state.headings)}")
    print("\nReady to start conversation!")
