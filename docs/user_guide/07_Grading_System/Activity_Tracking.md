# Activity Tracking

**Purpose:** Documentation for tracking flashcards, tasks, and pomodoro sessions

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

Activity tracking in OCDS monitors student engagement through flashcard reviews, task completion, and study time (pomodoros). These activities contribute to the final grade and provide insights into student effort and consistency.

---

## 🎴 Flashcard Tracking

### What's Tracked

- **Completion percentage** - % of cards reviewed
- **Accuracy rate** - % of cards answered correctly
- **Review frequency** - How often cards are reviewed
- **Retention rate** - Long-term memory retention

### Grading Formula

```python
def calculate_flashcard_score(student_id: str, week: int) -> float:
    """Calculate flashcard score for a week."""
    
    flashcard_data = get_flashcard_data(student_id, week)
    
    total_cards = flashcard_data['total_cards']
    reviewed_cards = flashcard_data['reviewed_cards']
    correct_reviews = flashcard_data['correct_reviews']
    total_reviews = flashcard_data['total_reviews']
    
    # Completion: % of cards reviewed at least once
    completion = (reviewed_cards / total_cards) * 100
    
    # Accuracy: % of reviews answered correctly
    accuracy = (correct_reviews / total_reviews) * 100 if total_reviews > 0 else 0
    
    # Weighted score (50% completion, 50% accuracy)
    score = (completion * 0.5) + (accuracy * 0.5)
    
    return score
```

### Example

```
Total cards: 20
Reviewed cards: 18 (90% completion)
Correct reviews: 45 out of 54 (83% accuracy)

Score = (90 × 0.5) + (83 × 0.5) = 45 + 41.5 = 86.5%
```

---

## ✅ Task Tracking

### What's Tracked

- **Required tasks completed** - Must-do items
- **Optional tasks completed** - Bonus items
- **Completion percentage** - Overall progress
- **On-time completion** - Tasks done before due date

### Grading Formula

```python
def calculate_task_score(student_id: str, week: int) -> float:
    """Calculate task completion score."""
    
    task_data = get_task_data(student_id, week)
    
    required_tasks = task_data['required_tasks']
    required_completed = task_data['required_completed']
    
    optional_tasks = task_data['optional_tasks']
    optional_completed = task_data['optional_completed']
    
    # Base score from required tasks
    base_score = (required_completed / required_tasks) * 100
    
    # Bonus from optional tasks (up to 10% extra)
    bonus = (optional_completed / optional_tasks) * 10 if optional_tasks > 0 else 0
    
    # Total (capped at 100%)
    total_score = min(base_score + bonus, 100)
    
    return total_score
```

### Example

```
Required tasks: 5
Required completed: 5 (100%)

Optional tasks: 3
Optional completed: 2 (67%)

Base score = 100%
Bonus = 67% × 10% = 6.7%
Total = min(100 + 6.7, 100) = 100%
```

---

## ⏱️ Pomodoro Tracking

### What's Tracked

- **Total sessions** - Number of pomodoros completed
- **Total time** - Minutes of focused study
- **Consistency** - Study sessions per week
- **Time distribution** - When students study

### Grading (Optional)

```python
def calculate_pomodoro_score(student_id: str, week: int) -> float:
    """Calculate pomodoro engagement score."""
    
    pomodoro_data = get_pomodoro_data(student_id, week)
    
    sessions = pomodoro_data['sessions']
    target_sessions = 10  # Recommended per week
    
    # Score based on meeting target
    score = min((sessions / target_sessions) * 100, 100)
    
    return score
```

**Note:** Pomodoros typically don't count toward grade, but can be used for engagement metrics or bonus points.

---

## 📊 Data Collection

### Flashcard Data Source

**Spaced Repetition Plugin Logs:**
```
~/.obsidian/plugins/obsidian-spaced-repetition/data.json
```

**Data Structure:**
```json
{
  "cards": {
    "card_id_1": {
      "reviews": 5,
      "correct": 4,
      "last_review": "2025-01-05",
      "next_review": "2025-01-08",
      "ease": 2.5
    }
  }
}
```

---

### Task Data Source

**Task Frontmatter:**
```yaml
tasks:
  - id: task_01
    description: "Read study material"
    completed: true
    completed_date: 2025-01-05
    required: true
    points: 1
```

---

### Pomodoro Data Source

**Pomodoro Plugin Logs:**
```
~/.obsidian/plugins/obsidian-pomodoro/logs/
```

**Log Entry:**
```json
{
  "date": "2025-01-05",
  "sessions": [
    {
      "start": "14:00",
      "end": "14:25",
      "duration": 25,
      "task": "Study Week 1 Material"
    }
  ]
}
```

---

## 🔄 Auto-Update Process

### Tracking Workflow

```python
def update_activity_tracking(class_id: str, student_id: str):
    """Update all activity tracking."""
    
    progress_file = f'Classes/{class_id}/Progress/{student_id}_progress.yaml'
    progress = load_yaml(progress_file)
    
    # Update flashcards
    for week in range(1, 13):
        flashcard_score = calculate_flashcard_score(student_id, week)
        progress['flashcards'][f'week_{week}'] = {
            'score': flashcard_score,
            'updated': datetime.now().strftime('%Y-%m-%d')
        }
    
    # Update tasks
    for week in range(1, 13):
        task_score = calculate_task_score(student_id, week)
        progress['tasks'][f'week_{week}'] = {
            'score': task_score,
            'updated': datetime.now().strftime('%Y-%m-%d')
        }
    
    # Update pomodoros
    pomodoro_data = get_all_pomodoros(student_id)
    progress['pomodoros'] = {
        'total_sessions': pomodoro_data['total_sessions'],
        'total_minutes': pomodoro_data['total_minutes'],
        'updated': datetime.now().strftime('%Y-%m-%d')
    }
    
    save_yaml(progress_file, progress)
```

---

## 📈 Activity Analytics

### Weekly Activity Dashboard

```dataview
TABLE
  flashcard_score as "Flashcards",
  task_completion as "Tasks",
  pomodoro_sessions as "Pomodoros",
  total_engagement as "Engagement"
FROM "Classes/TCM_101/Progress"
WHERE week = 1
```

### Engagement Trends

```dataviewjs
const weeks = [1, 2, 3, 4, 5];
const student = dv.current();

const flashcards = weeks.map(w => student.flashcards[`week_${w}`].score);
const tasks = weeks.map(w => student.tasks[`week_${w}`].score);

dv.paragraph(`
**5-Week Engagement Trend:**
- Flashcards: ${flashcards.join(', ')}
- Tasks: ${tasks.join(', ')}
- Average Flashcards: ${(flashcards.reduce((a,b) => a+b) / 5).toFixed(1)}%
- Average Tasks: ${(tasks.reduce((a,b) => a+b) / 5).toFixed(1)}%
`);
```

---

## 🎯 Best Practices

### For Students

**Flashcards:**
- ✅ Review daily (consistency > cramming)
- ✅ Use spaced repetition algorithm
- ✅ Don't mark cards correct if unsure
- ✅ Review difficult cards more often

**Tasks:**
- ✅ Complete required tasks first
- ✅ Attempt bonus tasks for extra credit
- ✅ Check off tasks as you complete them
- ✅ Review task list at start of week

**Pomodoros:**
- ✅ Use 25-minute focused sessions
- ✅ Take 5-minute breaks
- ✅ Track what you study
- ✅ Aim for consistency (daily sessions)

---

## 📚 Related Documentation

- [[Auto_Grading_Overview.md]] - Overall grading system
- [[Flashcard_Template.md]] - Flashcard format
- [[Task_Template.md]] - Task format
- [[Spaced_Repetition_Guide.md]] - Flashcard plugin
- [[Pomodoro_Tracking.md]] - Pomodoro plugin

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
