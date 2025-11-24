#!/usr/bin/env python3
"""
Conversation State Manager - Tracks progress through guided learning conversation.
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


class ConversationState:
    """Manages conversation progress and state for guided learning."""

    def __init__(self, root_note_path: Path):
        """
        Initialize conversation state.

        Args:
            root_note_path (Path): Path to the root note file.
        """
        self.root_note_path = root_note_path
        self.topic_name = self._extract_topic_name()
        self.headings = self._extract_headings()
        self.current_heading_index = 0
        self.attempts_per_heading = {i: 0 for i in range(len(self.headings))}
        self.understanding_scores = {i: [] for i in range(len(self.headings))}
        self.conversation_history = []
        self.start_time = datetime.now()
        self.heading_start_times = {}
        self.completed_headings = set()

    def _extract_topic_name(self) -> str:
        """Extract topic name from file path or content."""
        with open(self.root_note_path, encoding="utf-8") as f:
            content = f.read()
            # Try to extract from frontmatter
            match = re.search(r"name:\s*(.+)", content)
            if match:
                return match.group(1).strip()
            # Fallback to filename
            return self.root_note_path.stem.replace("Root_Note_", "").replace("_", " ")

    def _extract_headings(self) -> list[dict[str, Any]]:
        """
        Extract all H2 headings and their content from root note.

        Returns:
            List of dicts with heading info: {title, content, level}
        """
        with open(self.root_note_path, encoding="utf-8") as f:
            content = f.read()

        # Remove frontmatter
        content = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)

        headings = []
        # Match H2 headings (## Heading)
        sections = re.split(r"\n## ", content)

        for i, section in enumerate(sections):
            if i == 0:  # Skip content before first heading
                continue

            lines = section.split("\n", 1)
            title = lines[0].strip()
            section_content = lines[1].strip() if len(lines) > 1 else ""

            # Extract content until next heading or end
            # Remove any H3+ headings for simplicity (keep only main content)
            main_content = re.split(r"\n###", section_content)[0].strip()

            headings.append({"title": title, "content": main_content, "level": 2, "index": len(headings)})

        return headings

    def get_current_heading(self) -> dict[str, Any] | None:
        """
        Get current heading information.

        Returns:
            Dict with heading info or None if complete.
        """
        if self.is_complete():
            return None
        return self.headings[self.current_heading_index]

    def advance_heading(self):
        """Move to next heading."""
        if not self.is_complete():
            self.completed_headings.add(self.current_heading_index)
            self.current_heading_index += 1

    def record_response(self, question: str, response: str, assessment: dict[str, Any]):
        """
        Record student response and assessment.

        Args:
            question (str): The question asked.
            response (str): Student's response.
            assessment (Dict): Assessment results from UnderstandingAssessor.
        """
        heading_idx = self.current_heading_index
        self.attempts_per_heading[heading_idx] += 1
        self.understanding_scores[heading_idx].append(assessment["score"])

        self.conversation_history.append(
            {
                "timestamp": datetime.now().isoformat(),
                "heading_index": heading_idx,
                "heading_title": self.headings[heading_idx]["title"],
                "attempt": self.attempts_per_heading[heading_idx],
                "question": question,
                "response": response,
                "assessment": assessment,
            }
        )

    def get_missing_concepts(self) -> list[str]:
        """Get missing concepts from last assessment."""
        if not self.conversation_history:
            return []
        last_entry = self.conversation_history[-1]
        return last_entry["assessment"].get("missing_concepts", [])

    def get_heading_attempts(self) -> int:
        """Get number of attempts for current heading."""
        return self.attempts_per_heading[self.current_heading_index]

    def get_heading_best_score(self) -> float:
        """Get best score for current heading."""
        scores = self.understanding_scores[self.current_heading_index]
        return max(scores) if scores else 0.0

    def is_complete(self) -> bool:
        """Check if all headings have been covered."""
        return self.current_heading_index >= len(self.headings)

    def get_progress_percentage(self) -> float:
        """Get overall progress percentage."""
        if not self.headings:
            return 100.0
        return (len(self.completed_headings) / len(self.headings)) * 100

    def get_summary(self) -> dict[str, Any]:
        """
        Generate conversation summary.

        Returns:
            Dict with summary statistics.
        """
        total_time = (datetime.now() - self.start_time).total_seconds() / 60  # minutes

        heading_summaries = []
        for i, heading in enumerate(self.headings):
            scores = self.understanding_scores[i]
            heading_summaries.append(
                {
                    "title": heading["title"],
                    "attempts": self.attempts_per_heading[i],
                    "scores": scores,
                    "best_score": max(scores) if scores else 0,
                    "average_score": sum(scores) / len(scores) if scores else 0,
                    "completed": i in self.completed_headings,
                }
            )

        all_scores = [score for scores in self.understanding_scores.values() for score in scores]
        overall_average = sum(all_scores) / len(all_scores) if all_scores else 0

        return {
            "topic": self.topic_name,
            "total_headings": len(self.headings),
            "completed_headings": len(self.completed_headings),
            "progress_percentage": self.get_progress_percentage(),
            "total_time_minutes": round(total_time, 1),
            "total_attempts": sum(self.attempts_per_heading.values()),
            "overall_average_score": round(overall_average, 1),
            "heading_summaries": heading_summaries,
            "weak_areas": self._identify_weak_areas(heading_summaries),
            "strong_areas": self._identify_strong_areas(heading_summaries),
        }

    def _identify_weak_areas(self, heading_summaries: list[dict]) -> list[str]:
        """Identify headings with low scores."""
        weak = []
        for summary in heading_summaries:
            if summary["best_score"] < 70 and summary["attempts"] > 0:
                weak.append(summary["title"])
        return weak

    def _identify_strong_areas(self, heading_summaries: list[dict]) -> list[str]:
        """Identify headings with high scores."""
        strong = []
        for summary in heading_summaries:
            if summary["best_score"] >= 85 and summary["attempts"] > 0:
                strong.append(summary["title"])
        return strong

    def save_state(self, output_path: Path):
        """
        Save conversation state to JSON file.

        Args:
            output_path (Path): Path to save state file.
        """
        state_data = {
            "topic": self.topic_name,
            "root_note_path": str(self.root_note_path),
            "current_heading_index": self.current_heading_index,
            "completed_headings": list(self.completed_headings),
            "attempts_per_heading": self.attempts_per_heading,
            "understanding_scores": self.understanding_scores,
            "conversation_history": self.conversation_history,
            "start_time": self.start_time.isoformat(),
            "summary": self.get_summary(),
        }

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(state_data, f, indent=2, ensure_ascii=False)

    @classmethod
    def load_state(cls, state_path: Path) -> "ConversationState":
        """
        Load conversation state from JSON file.

        Args:
            state_path (Path): Path to state file.

        Returns:
            ConversationState instance.
        """
        with open(state_path, encoding="utf-8") as f:
            state_data = json.load(f)

        root_note_path = Path(state_data["root_note_path"])
        instance = cls(root_note_path)

        instance.current_heading_index = state_data["current_heading_index"]
        instance.completed_headings = set(state_data["completed_headings"])
        instance.attempts_per_heading = {int(k): v for k, v in state_data["attempts_per_heading"].items()}
        instance.understanding_scores = {int(k): v for k, v in state_data["understanding_scores"].items()}
        instance.conversation_history = state_data["conversation_history"]
        instance.start_time = datetime.fromisoformat(state_data["start_time"])

        return instance


if __name__ == "__main__":
    # Test with Lung Yin Deficiency
    root_note = Path(
        "/home/shuma/Documents/AI_Suite/TCM_Knowledge_Base/Materials/TCM_101/Root_Note_Lung_Yin_Deficiency.md"
    )

    state = ConversationState(root_note)

    print(f"Topic: {state.topic_name}")
    print(f"Total headings: {len(state.headings)}\n")

    for i, heading in enumerate(state.headings):
        print(f"{i + 1}. {heading['title']}")
        print(f"   Content preview: {heading['content'][:100]}...")
        print()
