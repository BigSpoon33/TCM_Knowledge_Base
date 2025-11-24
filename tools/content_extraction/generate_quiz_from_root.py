#!/usr/bin/env python3
"""
Generate OCDS-compatible auto-grading quizzes from root note files.

This script:
1. Reads a root note file with frontmatter
2. Extracts quiz_seeds from assessment_data
3. Generates auto-grading logic using MetaBind + DataviewJS
4. Creates a properly formatted quiz file for OCDS system
5. Outputs to Materials/{class_id}/ directory

Usage:
    python generate_quiz_from_root.py "Root Note Name"
    python generate_quiz_from_root.py "Blood Stasis Pattern" --output-dir "Materials/TCM_101"
"""

import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from generate_flashcards_from_root import MATERIALS_DIR, RootNoteParser, find_root_note


class QuizGenerator:
    """Generate auto-grading quizzes from root note data."""

    def __init__(self, root_note: RootNoteParser, class_id: str = None):
        self.root_note = root_note
        self.metadata = root_note.get_metadata()
        self.class_id = class_id or self._generate_class_id()
        self.questions = []

    def _generate_class_id(self) -> str:
        """Generate class ID from domain and subject."""
        domain = self.metadata["domain"].replace(" ", "_")
        subject = self.metadata["subject"].replace(" ", "_")
        return f"{domain}_{subject}"

    def generate_all_questions(self):
        """Generate all quiz questions from root note."""
        print(f"📝 Generating quiz for: {self.metadata['name']}")

        # Extract quiz seeds from assessment_data
        assessment_data = self.root_note.frontmatter.get("assessment_data", {})
        quiz_seeds = assessment_data.get("quiz_seeds", [])
        scenarios = assessment_data.get("scenarios", [])

        print(f"   📌 Processing {len(quiz_seeds)} quiz seeds...")
        for seed in quiz_seeds:
            question = self._create_question_from_seed(seed)
            if question:
                self.questions.append(question)

        print(f"   🎯 Processing {len(scenarios)} clinical scenarios...")
        for scenario in scenarios:
            question = self._create_question_from_scenario(scenario)
            if question:
                self.questions.append(question)

        print(f"✅ Generated {len(self.questions)} quiz questions")

    def _create_question_from_seed(self, seed: dict[str, Any]) -> dict[str, Any] | None:
        """Create a quiz question from a quiz seed."""
        question_type = seed.get("question_type", "multiple_choice")

        if question_type == "multiple_choice":
            return self._create_multiple_choice(seed)
        elif question_type == "true_false":
            return self._create_true_false(seed)
        elif question_type == "short_answer":
            return self._create_short_answer(seed)
        else:
            print(f"   ⚠️  Unsupported question type: {question_type}")
            return None

    def _create_multiple_choice(self, seed: dict[str, Any]) -> dict[str, Any]:
        """Create a multiple choice question."""
        question_text = seed.get("question", "")
        correct_answer = seed.get("correct_answer", "")
        distractors = seed.get("distractors", [])
        explanation = seed.get("explanation", "")
        difficulty = seed.get("difficulty", "medium")
        bloom_level = seed.get("bloom_level", "Remember")

        # Combine correct answer with distractors
        all_options = [correct_answer] + distractors

        # Assign letters (A, B, C, D)
        options = []
        correct_letter = "A"  # Default to A for correct answer
        for i, option in enumerate(all_options):
            letter = chr(65 + i)  # A=65, B=66, etc.
            options.append({"letter": letter, "text": option})
            if option == correct_answer:
                correct_letter = letter

        return {
            "type": "multiple_choice",
            "question": question_text,
            "options": options,
            "correct_answer": correct_letter,
            "explanation": explanation,
            "difficulty": difficulty,
            "bloom_level": bloom_level,
        }

    def _create_true_false(self, seed: dict[str, Any]) -> dict[str, Any]:
        """Create a true/false question."""
        question_text = seed.get("question", "")
        correct_answer = seed.get("correct_answer", "True")
        explanation = seed.get("explanation", "")
        difficulty = seed.get("difficulty", "easy")
        bloom_level = seed.get("bloom_level", "Remember")

        return {
            "type": "true_false",
            "question": question_text,
            "correct_answer": correct_answer,
            "explanation": explanation,
            "difficulty": difficulty,
            "bloom_level": bloom_level,
        }

    def _create_short_answer(self, seed: dict[str, Any]) -> dict[str, Any]:
        """Create a short answer question."""
        question_text = seed.get("question", "")
        correct_answer = seed.get("correct_answer", "")
        explanation = seed.get("explanation", "")
        difficulty = seed.get("difficulty", "hard")
        bloom_level = seed.get("bloom_level", "Apply")

        return {
            "type": "short_answer",
            "question": question_text,
            "correct_answer": correct_answer,
            "explanation": explanation,
            "difficulty": difficulty,
            "bloom_level": bloom_level,
        }

    def _create_question_from_scenario(self, scenario: dict[str, Any]) -> dict[str, Any] | None:
        """Create a clinical scenario question."""
        scenario_text = scenario.get("scenario", "")
        question_text = scenario.get("question", "")
        correct_response = scenario.get("correct_response", "")
        reasoning = scenario.get("reasoning", "")

        if not scenario_text or not question_text:
            return None

        # Treat as short answer question
        full_question = f"**Clinical Scenario:**\n\n{scenario_text}\n\n**Question:** {question_text}"

        return {
            "type": "short_answer",
            "question": full_question,
            "correct_answer": correct_response,
            "explanation": reasoning,
            "difficulty": "hard",
            "bloom_level": "Analyze",
        }

    def generate_quiz_file(self, output_path: Path):
        """Generate complete quiz markdown file with auto-grading."""
        if not self.questions:
            print("⚠️  No questions to generate!")
            return

        today = datetime.now().strftime("%Y-%m-%d")
        topic_name = self.metadata["name"]
        total_questions = len(self.questions)

        # Build frontmatter (OCDS-compatible)
        frontmatter = f"""---
ocds_type: quiz
material_id: quiz_{self.class_id.lower()}
class_id: {self.class_id}
title: "{topic_name} Quiz"
description: Test your knowledge of {topic_name}
questions: {total_questions}
points_possible: {total_questions}
attempts: 0
max_attempts: 3
score: 0
correct_answers: 0
graded_date: null
student_answers: []
tags:
  - quiz
  - {self.class_id.lower()}
  - {self.metadata["domain"].lower()}
  - {self.metadata["subject"].lower().replace(" ", "-")}
submission_status: not_started
submitted_date: null
percentage: 0
pass_fail: null
created: {today}
updated: {today}
---
"""

        # Build quiz content
        content = f"\n# {topic_name} Quiz\n\n"
        content += f"**Questions:** {total_questions}  \n"
        content += f"**Points:** {total_questions}  \n"
        content += "**Time Limit:** None  \n"
        content += "**Attempts:** 3 maximum\n\n"
        content += "---\n\n"
        content += "## Instructions\n\n"
        content += f"- Answer all {total_questions} questions\n"
        content += "- Each question is worth 1 point\n"
        content += "- You may retake this quiz up to 3 times\n"
        content += "- Your best score will count\n"
        content += "- Passing score: 70%\n\n"
        content += "---\n\n"

        # Generate questions
        for i, q in enumerate(self.questions, 1):
            content += self._generate_question_markdown(i, q)
            content += "\n---\n\n"

        # Add grading section
        content += self._generate_grading_section()

        # Write file
        full_content = frontmatter + content

        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(full_content)
            print(f"✅ Quiz file created: {output_path}")
        except Exception as e:
            print(f"❌ Error writing quiz file: {e}")

    def _generate_question_markdown(self, num: int, question: dict[str, Any]) -> str:
        """Generate markdown for a single question."""
        q_type = question["type"]
        difficulty = question.get("difficulty", "medium")
        bloom = question.get("bloom_level", "Remember")

        markdown = f"## Question {num}\n\n"
        markdown += f"**Difficulty:** {difficulty.capitalize()} | **Bloom Level:** {bloom}\n\n"
        markdown += f"{question['question']}\n\n"

        if q_type == "multiple_choice":
            markdown += self._generate_multiple_choice_markdown(num, question)
        elif q_type == "true_false":
            markdown += self._generate_true_false_markdown(num, question)
        elif q_type == "short_answer":
            markdown += self._generate_short_answer_markdown(num, question)

        return markdown

    def _generate_multiple_choice_markdown(self, num: int, question: dict[str, Any]) -> str:
        """Generate markdown for multiple choice question."""
        markdown = ""
        correct_letter = question["correct_answer"]

        for option in question["options"]:
            letter = option["letter"]
            text = option["text"]
            is_correct = letter == correct_letter
            checkbox = "[x]" if is_correct else "[ ]"
            markdown += f"- {checkbox} {letter}) {text}\n"

        markdown += f"\n**Correct Answer:** {correct_letter}\n\n"

        if question.get("explanation"):
            markdown += f"**Explanation:** {question['explanation']}\n\n"

        return markdown

    def _generate_true_false_markdown(self, num: int, question: dict[str, Any]) -> str:
        """Generate markdown for true/false question."""
        correct = question["correct_answer"]

        markdown = f"- [{'x' if correct == 'True' else ' '}] True\n"
        markdown += f"- [{'x' if correct == 'False' else ' '}] False\n\n"
        markdown += f"**Correct Answer:** {correct}\n\n"

        if question.get("explanation"):
            markdown += f"**Explanation:** {question['explanation']}\n\n"

        return markdown

    def _generate_short_answer_markdown(self, num: int, question: dict[str, Any]) -> str:
        """Generate markdown for short answer question."""
        markdown = "**Your Answer:**\n\n"
        markdown += "_[Write your answer here]_\n\n"
        markdown += f"**Correct Answer:** {question['correct_answer']}\n\n"

        if question.get("explanation"):
            markdown += f"**Explanation:** {question['explanation']}\n\n"

        return markdown

    def _generate_grading_section(self) -> str:
        """Generate auto-grading DataviewJS section."""
        total_questions = len(self.questions)

        grading = """## 📊 Quiz Results

```dataviewjs
// Auto-grading logic
const file = dv.current().file;
const fm = dv.page(file.path);

// Get student answers from frontmatter
const studentAnswers = fm.student_answers || [];
const totalQuestions = fm.questions || 0;

// Define correct answers
const correctAnswers = [
"""

        # Add correct answers array
        for i, q in enumerate(self.questions):
            if q["type"] == "multiple_choice":
                answer = f'"{q["correct_answer"]}"'
            elif q["type"] == "true_false":
                answer = f'"{q["correct_answer"]}"'
            else:
                answer = f'"{q["correct_answer"]}"'

            grading += f"  {answer}"
            if i < len(self.questions) - 1:
                grading += ","
            grading += f"  // Q{i + 1}\n"

        grading += """];

// Calculate score
let correctCount = 0;
for (let i = 0; i < Math.min(studentAnswers.length, correctAnswers.length); i++) {
  if (studentAnswers[i] === correctAnswers[i]) {
    correctCount++;
  }
}

const percentage = totalQuestions > 0 ? Math.round((correctCount / totalQuestions) * 100) : 0;
const passFail = percentage >= 70 ? 'Pass' : 'Fail';

// Update frontmatter
const currentFile = app.workspace.getActiveFile();
if (currentFile && studentAnswers.length > 0) {
  await app.fileManager.processFrontMatter(currentFile, (fm) => {
    fm.score = correctCount;
    fm.correct_answers = correctCount;
    fm.percentage = percentage;
    fm.pass_fail = passFail;
    fm.submission_status = 'graded';
    fm.graded_date = new Date().toISOString();
    if (!fm.submitted_date) {
      fm.submitted_date = new Date().toISOString();
    }
    fm.attempts = (fm.attempts || 0) + 1;
  });
}

// Display results
if (studentAnswers.length > 0) {
  dv.paragraph(`
**Score:** ${correctCount}/${totalQuestions} (${percentage}%)  
**Status:** ${passFail === 'Pass' ? '✅ Pass' : '❌ Fail'}  
**Attempts:** ${fm.attempts || 0}/${fm.max_attempts || 3}
  `);
} else {
  dv.paragraph(`
**Status:** ⏳ Not yet submitted  
**Instructions:** Answer all questions above, then click "Submit Quiz" button
  `);
}
```

---

## 🎯 Submit Quiz

**Instructions:**
1. Review your answers above
2. Click the button below to submit and grade your quiz
3. You can retake up to 3 times

`BUTTON[submit_quiz]`
Submit Quiz
`BUTTON[submit_quiz]`

---

**Note:** This is an auto-graded quiz. Your score will be calculated immediately upon submission.

"""

        return grading


def main():
    """Main execution function."""
    print("=" * 60)
    print("OCDS Quiz Generator from Root Notes")
    print("=" * 60)

    # Parse arguments
    if len(sys.argv) < 2:
        print('Usage: python generate_quiz_from_root.py "Root Note Name" [--output-dir DIR]')
        print("\nExample:")
        print('  python generate_quiz_from_root.py "Blood Stasis Pattern"')
        print('  python generate_quiz_from_root.py "Blood Stasis Pattern" --output-dir "Materials/TCM_101"')
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
        sys.exit(1)

    print(f"✅ Found root note: {root_note_path}")

    # Parse root note
    try:
        parser = RootNoteParser(root_note_path)
    except Exception as e:
        print(f"❌ Error parsing root note: {e}")
        sys.exit(1)

    # Generate quiz
    generator = QuizGenerator(parser)
    generator.generate_all_questions()

    # Determine output path
    if output_dir:
        output_path = output_dir / "Quiz.md"
    else:
        # Default: Materials/{class_id}/Quiz.md
        output_path = MATERIALS_DIR / generator.class_id / "Quiz.md"

    # Generate quiz file
    generator.generate_quiz_file(output_path)

    print("\n" + "=" * 60)
    print("✅ Quiz generation complete!")
    print("=" * 60)
    print(f"\n📁 Output: {output_path}")
    print(f"❓ Total questions: {len(generator.questions)}")


if __name__ == "__main__":
    main()
