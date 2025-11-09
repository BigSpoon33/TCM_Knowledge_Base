# Frontmatter Schema

**Complete specification for OCDS frontmatter standards**

---

## 📚 Overview

Frontmatter is YAML metadata at the top of markdown files. OCDS uses standardized frontmatter for:
- File identification
- Data queries
- Automation
- Progress tracking
- Cross-referencing

**Format:** YAML between `---` delimiters

---

## 📋 Universal Fields

All OCDS files should include these base fields:

```yaml
---
# Universal OCDS Fields
type: string                  # File type identifier
class_id: string              # Associated class
tags: array                   # Categorization
created: YYYY-MM-DD          # Creation date
updated: YYYY-MM-DD          # Last modified
---
```

---

## 📝 File Type Schemas

### 1. Study Material

```yaml
---
type: study
class_id: "TCM_101"
week: 1
day: 1
topic: "Qi Deficiency Pattern"
estimated_minutes: 60
difficulty: "beginner"
prerequisites: []
tags:
  - study
  - tcm_101
  - patterns
  - qi_deficiency
created: 2025-11-01
updated: 2025-11-05
---
```

**Fields:**
- `type`: Always "study"
- `class_id`: Which class this belongs to
- `week`: Week number
- `day`: Day number
- `topic`: Material topic
- `estimated_minutes`: Reading time
- `difficulty`: beginner | intermediate | advanced
- `prerequisites`: Required prior knowledge

---

### 2. Quiz

```yaml
---
type: quiz
class_id: "TCM_101"
week: 1
day: 5
topic: "Qi Deficiency Pattern"
total_questions: 10
passing_score: 7
time_limit_minutes: 15
allow_retake: false
show_answers_after: true

# Student data (populated on import)
student_id: ""
quiz_date: ""
start_time: ""
submit_time: ""

# Answers (populated by student)
q1_answer: ""
q2_answer: ""
# ... one per question

# Grading (populated by auto-grader)
score: 0
percentage: 0
pass_fail: ""
status: "not_started"

# Answer key (hidden from student)
answer_key:
  q1: "A"
  q2: "B"
  # ... one per question

explanations:
  q1: "Explanation text..."
  q2: "Explanation text..."
  # ... one per question

tags:
  - quiz
  - tcm_101
  - week_1
  - qi_deficiency
created: 2025-11-01
updated: 2025-11-05
---
```
>The quizes need a way to fill a note with questions from the question banks that get put into the note with checkboxes to select the answer and then somehow connect the checked answer with what gets put into the frontmatter. this way we can match the key to what checkboxes get slelected

---

### 3. Flashcards

```yaml
---
type: flashcards
class_id: "TCM_101"
topic: "Qi Deficiency Pattern"
category: "patterns"
total_cards: 20
difficulty: "mixed"
tags:
  - flashcards
  - tcm_101
  - patterns
  - qi_deficiency
created: 2025-11-01
updated: 2025-11-05
---
```

---

### 4. Task Note

```yaml
---
# TaskNotes Fields
status: pending
priority: normal
scheduled: 2025-11-10
due: 2025-11-11
dateCreated: 2025-11-05T14:30:00.000-08:00
dateModified: 2025-11-05T14:30:00.000-08:00

# Organization
tags:
  - task
  - tcm_101
  - week_1
  - day_1
contexts:
  - study
projects:
  - "[[TCM_101_Fundamentals]]"

# Dependencies
blocked_by:
  - "[[Previous_Task]]"
blocking:
  - "[[Next_Task]]"

# Time Management
estimated_minutes: 60
actual_minutes: 0
pomodoros_planned: 3
pomodoros_completed: 0

# Reminders
reminders:
  - id: rem_1730000000000
    type: relative
    relatedTo: due
    offset: -P1D
    description: "1 day before"

# OCDS Custom Fields
class_id: "TCM_101"
week: 1
day: 1
task_type: study
material_link: "[[Qi_Deficiency_Pattern]]"
points_possible: 100
points_earned: 0
---
```
>This is going to be a big part of the automation, organization, how you stay on track, sequence things, and just super important. we need to get the class system to integrate into the tasknotes app so that everything can be tracked with reminders, timers, clear way to guide student to the correct notes that are related to the topic being covered and what needs to be focused on and learned this week or interval. so basically it's like the canvas dashboard where you have your class modules that have the week's materials, homework, links, when the tests are, when projects are due, it's your one stop for homework, study, projects, class links, class time, slides, cards,etc because when we get all the class into a group of tasknotes we can look at everything in a dashboard or on a calendar. makes it easy to know what is due when, when things are happening.

---

### 5. Homework

```yaml
---
type: homework
class_id: "TCM_101"
week: 1
title: "Pattern Differentiation Practice"
assigned_date: 2025-11-01
due_date: 2025-11-07
estimated_minutes: 120
points_possible: 100

# Student data
student_id: ""
submitted_date: ""
days_late: 0
score: 0
status: "pending"

tags:
  - homework
  - tcm_101
  - week_1
  - patterns
created: 2025-11-01
updated: 2025-11-05
---
```
> Not sure how homework works exactly. I guess this is kind of like a group of tasks that direct you to go through the slides, do some cards, take a quiz
---

### 6. Slide Deck

```yaml
---
# Advanced Slides Configuration
theme: black
transition: slide
slideNumber: true
progress: true
controls: true
css: [css/tcm-styles.css]

# OCDS Fields
type: slides
class_id: "TCM_101"
week: 1
topic: "Qi Deficiency Pattern"
slide_count: 25
estimated_minutes: 30

tags:
  - slides
  - tcm_101
  - patterns
  - qi_deficiency
created: 2025-11-01
updated: 2025-11-05
---
```
>slides are fun, I actually really like them. need to get them more aesthetic tho
---

### 7. Progress Tracking

```yaml
---
type: progress
student_id: "JD110590"
student_name: "John Doe"
class_id: "TCM_101"
start_date: 2025-11-01
status: "in_progress"

current_week: 2
total_weeks: 12
current_day: 3
completion_percentage: 15.5

overall_grade: 82.5
letter_grade: "B"

component_scores:
  quizzes: 85.0
  flashcards: 88.0
  homework: 80.0
  pomodoros: 75.0

flags:
  struggling: false
  excelling: true
  at_risk: false
  inactive: false

last_activity_date: 2025-11-12
last_updated: 2025-11-12T18:30:00
created: 2025-11-01
---
```
> Gotta have a slick dashboard
---

### 8. Class Manifest

```yaml
---
type: class_manifest
class_id: "TCM_101"
class_name: "TCM Fundamentals: Patterns & Diagnosis"
version: "1.0.0"
author: "Dr. Jane Smith"
created_date: 2025-11-01
updated_date: 2025-11-05

duration_weeks: 12
duration_days_per_week: 7
prerequisites: []

passing_grade: 70
unlock_threshold: 75

grading_weights:
  quizzes: 0.4
  flashcards: 0.3
  homework: 0.2
  pomodoros: 0.1

description: "Introduction to TCM pattern differentiation"
tags:
  - tcm
  - patterns
  - fundamentals
difficulty: "beginner"
estimated_hours: 120
---
```
>Basically a big list of tasks that connect to material. gives you a sequenced set of material which is just a note that has a connected question bank, slides, cards, etc. so you get the notes + the study materials all in the class capsule and you can keep it forever. or if you don't care about the sequence it can just be a data dump kind of like a recipe book or a combination of 3d print files
---

## 🔍 Field Reference

### Common Fields

#### `type` (required)
- **Values:** study | quiz | flashcards | homework | slides | task | progress | class_manifest
- **Purpose:** Identify file type for queries

#### `class_id` (required for class materials)
- **Format:** Uppercase with underscores
- **Example:** "TCM_101"
- **Purpose:** Associate with class

#### `week` (required for weekly content)
- **Type:** integer
- **Range:** 1-52
- **Purpose:** Week number in class

#### `day` (optional for daily content)
- **Type:** integer
- **Range:** 1-7
- **Purpose:** Day number in week

#### `tags` (required)
- **Type:** array of strings
- **Purpose:** Categorization and filtering
- **Convention:** lowercase, underscores

#### `created` (required)
- **Format:** YYYY-MM-DD
- **Purpose:** Track creation date

#### `updated` (required)
- **Format:** YYYY-MM-DD
- **Purpose:** Track last modification

---

### Status Fields

#### `status` (for tasks, quizzes, homework)
- **Values:**
  - Tasks: pending | in_progress | completed | cancelled
  - Quizzes: not_started | in_progress | submitted | graded
  - Homework: pending | in_progress | submitted | graded
  - Progress: enrolled | in_progress | completed | withdrawn

#### `priority` (for tasks)
- **Values:** low | normal | high
- **Purpose:** Task importance

---

### Date/Time Fields

#### Date Format
```yaml
date_field: 2025-11-05
```

#### DateTime Format (ISO 8601)
```yaml
datetime_field: 2025-11-05T14:30:00.000-08:00
```

#### Duration Format (ISO 8601)
```yaml
duration: P1D      # 1 day
duration: PT2H     # 2 hours
duration: PT30M    # 30 minutes
```

---

### Score Fields

#### `score` (for graded items)
- **Type:** integer or float
- **Range:** 0-100 (percentage) or 0-points_possible

#### `percentage` (for quizzes)
- **Type:** float
- **Range:** 0-100
- **Calculation:** (score / total_points) × 100

#### `pass_fail` (for quizzes)
- **Values:** Pass | Fail
- **Determination:** Based on passing_score threshold

---

## 📊 Dataview Integration

### Query by Type

```dataview
LIST
FROM ""
WHERE type = "quiz"
  AND class_id = "TCM_101"
SORT week, day
```

### Query by Week

```dataview
TABLE
  type as "Type",
  topic as "Topic",
  estimated_minutes as "Time"
FROM ""
WHERE class_id = "TCM_101"
  AND week = 1
SORT day, type
```

### Query by Status

```dataview
TASK
FROM ""
WHERE type = "task"
  AND status = "pending"
  AND class_id = "TCM_101"
SORT due ASC
```

### Aggregate Scores

```dataview
TABLE
  week as "Week",
  avg(rows.percentage) as "Avg Score"
FROM ""
WHERE type = "quiz"
  AND class_id = "TCM_101"
GROUP BY week
SORT week ASC
```

---

## ✅ Validation

### Required Fields Check

```python
def validate_frontmatter(file_type, frontmatter):
    """Validate frontmatter has required fields."""
    
    # Universal required fields
    universal = ['type', 'tags', 'created', 'updated']
    
    # Type-specific required fields
    type_required = {
        'study': ['class_id', 'week', 'topic'],
        'quiz': ['class_id', 'week', 'topic', 'total_questions', 'passing_score'],
        'task': ['status', 'priority', 'scheduled', 'due'],
        'homework': ['class_id', 'week', 'title', 'due_date'],
        'progress': ['student_id', 'class_id', 'start_date']
    }
    
    # Check universal fields
    for field in universal:
        if field not in frontmatter:
            raise ValueError(f"Missing required field: {field}")
    
    # Check type-specific fields
    if file_type in type_required:
        for field in type_required[file_type]:
            if field not in frontmatter:
                raise ValueError(f"Missing required field for {file_type}: {field}")
    
    return True
```

---

### Format Validation

```python
def validate_formats(frontmatter):
    """Validate field formats."""
    
    # Check date format
    if 'created' in frontmatter:
        try:
            datetime.strptime(frontmatter['created'], '%Y-%m-%d')
        except ValueError:
            raise ValueError("created must be YYYY-MM-DD format")
    
    # Check class_id format
    if 'class_id' in frontmatter:
        if not re.match(r'^[A-Z0-9_]+$', frontmatter['class_id']):
            raise ValueError("class_id must be uppercase alphanumeric with underscores")
    
    # Check status values
    if 'status' in frontmatter:
        valid_status = ['pending', 'in_progress', 'completed', 'cancelled', 
                       'not_started', 'submitted', 'graded', 'enrolled', 'withdrawn']
        if frontmatter['status'] not in valid_status:
            raise ValueError(f"Invalid status: {frontmatter['status']}")
    
    return True
```

---

## 💡 Best Practices

### Naming Conventions
- **Fields:** snake_case (e.g., `class_id`, `total_questions`)
- **Values:** lowercase for enums (e.g., `pending`, `beginner`)
- **Tags:** lowercase with underscores (e.g., `tcm_101`, `qi_deficiency`)

### Required vs Optional
- **Always include:** type, tags, created, updated
- **Include if applicable:** class_id, week, day
- **Optional:** difficulty, prerequisites, notes

### Consistency
- **Same fields across files** - Use standard names
- **Same formats** - Dates, IDs, statuses
- **Same structure** - Order fields consistently

### Documentation
- **Comment complex fields** - Explain purpose
- **Link to schemas** - Reference documentation
- **Version control** - Track changes

---

## 📚 Related Documentation

- **Class Manifest:** `Class_Manifest_Schema.md`
- **Timeline:** `Timeline_Schema.md`
- **Progress Tracking:** `Progress_Tracking_Schema.md`
- **Question Bank:** `Question_Bank_Schema.md`

---

**Standardize your frontmatter! 📋**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
