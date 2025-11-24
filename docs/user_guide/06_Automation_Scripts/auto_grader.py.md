# auto_grader.py - Auto-Grading Engine

**Purpose:** Automatically grade quizzes and calculate final scores

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

The `auto_grader.py` script is the **grading engine** for OCDS. It automatically grades multiple choice quizzes, tracks activity completion (flashcards, tasks, pomodoros), calculates weighted scores, and generates grade reports.

---

## 🚀 Quick Start

```bash
# Grade all materials for a student
python auto_grader.py --class-id TCM_101 --student-id john_doe

# Grade specific quiz
python auto_grader.py --class-id TCM_101 --student-id john_doe --quiz quiz_week01

# Generate grade report
python auto_grader.py --class-id TCM_101 --student-id john_doe --report
```

---

## 📖 Command Line Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--class-id` | Class identifier (required) | `--class-id TCM_101` |
| `--student-id` | Student identifier (required) | `--student-id john_doe` |
| `--quiz` | Grade specific quiz | `--quiz quiz_week01` |
| `--report` | Generate grade report | `--report` |
| `--output` | Report output file | `--output report.pdf` |

---

## 🏗️ How It Works

### Quiz Grading

```python
def grade_quiz(quiz_file: Path) -> float:
    """Grade a multiple choice quiz."""
    
    frontmatter = parse_frontmatter(quiz_file)
    questions = frontmatter['questions']
    student_answers = frontmatter['student_answers']
    
    correct = 0
    total = len(questions)
    
    for i, question in enumerate(questions):
        if student_answers[i] == question['correct_answer']:
            correct += 1
    
    score = (correct / total) * 100
    
    # Update frontmatter
    update_frontmatter(quiz_file, {
        'score': score,
        'correct_answers': correct,
        'total_questions': total,
        'graded_date': datetime.now().strftime('%Y-%m-%d')
    })
    
    return score
```

### Final Grade Calculation

```python
def calculate_final_grade(class_id: str, student_id: str) -> float:
    """Calculate weighted final grade."""
    
    grading_config = load_yaml(f'Classes/{class_id}/grading_config.yaml')
    progress = load_yaml(f'Classes/{class_id}/Progress/{student_id}_progress.yaml')
    
    # Get component scores
    quiz_avg = calculate_quiz_average(progress)
    flashcard_avg = calculate_flashcard_completion(progress)
    homework_avg = calculate_homework_average(progress)
    task_avg = calculate_task_completion(progress)
    
    # Apply weights
    weights = grading_config['weights']
    final_grade = (
        quiz_avg * weights['quizzes'] +
        flashcard_avg * weights['flashcards'] +
        homework_avg * weights['homework'] +
        task_avg * weights['tasks']
    )
    
    return final_grade
```

---

## 📊 Example Output

```
📊 OCDS Auto-Grader
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Class: TCM_101
Student: john_doe

📝 Grading Quizzes...
  Week 1 Quiz: 90% (9/10 correct)
  Week 2 Quiz: 85% (8.5/10 correct)
  Week 3 Quiz: 95% (9.5/10 correct)
  Average: 90%

🎴 Checking Flashcards...
  Week 1: 100% complete (20/20 cards, 85% accuracy)
  Week 2: 100% complete (25/25 cards, 90% accuracy)
  Week 3: 80% complete (20/25 cards, 88% accuracy)
  Average: 93%

✍️ Checking Homework...
  Week 1: 18/20 points (90%)
  Week 2: 19/20 points (95%)
  Week 3: Not yet graded
  Average: 92.5%

⏱️  Checking Pomodoros...
  Total: 24 sessions (12 hours)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Final Grade Calculation

  Quizzes (40%):     90.0% × 0.40 = 36.0%
  Flashcards (30%):  93.0% × 0.30 = 27.9%
  Homework (20%):    92.5% × 0.20 = 18.5%
  Tasks (10%):       95.0% × 0.10 = 9.5%
  
  TOTAL: 91.9% (A-)

✅ Grade updated in progress_tracking.yaml
```

---

## 🎯 Grading Components

### 1. Quizzes (40% default)
- Auto-graded multiple choice
- Instant feedback
- Unlimited attempts (best score counts)

### 2. Flashcards (30% default)
- Completion percentage
- Accuracy rate
- Spaced repetition adherence

### 3. Homework (20% default)
- Manual grading by instructor
- Rubric-based scoring
- Late penalties applied

### 4. Tasks (10% default)
- Completion percentage
- Engagement metric
- Bonus points available

---

## 📚 Related Documentation

- [[Script_Overview.md]] - All automation scripts
- [[Grading_Config_Schema.md]] - Grading configuration
- [[Quiz_Template.md]] - Quiz format
- [[Progress_Tracking_Schema.md]] - Progress tracking

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
