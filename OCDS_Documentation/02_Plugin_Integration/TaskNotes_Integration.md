# TaskNotes Plugin - OCDS Integration Guide

**Complete guide to using TaskNotes for OCDS task management**

---

## 📚 Overview

TaskNotes is an advanced task management plugin that stores tasks as individual markdown files with rich frontmatter metadata. OCDS uses it for:
- Daily study task scheduling
- Assignment due dates
- Quiz scheduling
- Task dependencies (blocking relationships)
- Progress tracking
- Time estimation

**Plugin:** https://github.com/czottmann/obsidian-task-notes  
**Docs:** https://tasknotes.dev/

---

## 🎯 Why TaskNotes for OCDS?

### Advantages Over Basic Tasks
- **Rich metadata** - Store detailed task information
- **Individual files** - Each task is a separate note
- **Frontmatter-based** - Easy to query and manipulate
- **Blocking relationships** - Task dependencies
- **Contexts and projects** - Organize by class/week
- **Reminders** - Built-in notification system

### OCDS Use Cases
- **Study sessions** - Daily reading and review
- **Flashcard reviews** - Scheduled SR sessions
- **Quizzes** - Timed assessments
- **Homework** - Assignments with due dates
- **Projects** - Long-form work
- **Review sessions** - Revisit previous material

---

## 📋 TaskNotes Frontmatter Structure

### OCDS Standard Template

```yaml
---
# Core TaskNotes Fields
status: pending | in_progress | completed | cancelled
priority: low | normal | high
scheduled: YYYY-MM-DD
due: YYYY-MM-DD
dateCreated: YYYY-MM-DDTHH:MM:SS.sss-TZ
dateModified: YYYY-MM-DDTHH:MM:SS.sss-TZ

# Organization
tags:
  - task
  - {{CLASS_ID}}
  - week_{{WEEK_NUMBER}}
  - day_{{DAY_NUMBER}}
contexts:
  - study | homework | quiz | project | review
projects:
  - "[[{{CLASS_NAME}}]]"

# Dependencies
blocked_by:
  - "[[Previous_Task]]"
blocking:
  - "[[Next_Task]]"

# Time Management
estimated_minutes: 60
actual_minutes: 0

# Reminders
reminders:
  - id: rem_{{TIMESTAMP}}
    type: relative
    relatedTo: due
    offset: -P1D
    description: "1 day before due"

# OCDS Custom Fields
class_id: "{{CLASS_ID}}"
week: {{WEEK_NUMBER}}
day: {{DAY_NUMBER}}
task_type: study | flashcards | quiz | homework | project
material_link: "[[Material_File]]"
points_possible: 100
points_earned: 0
---
```

### Field Descriptions

| Field | Type | Purpose | Example |
|-------|------|---------|---------|
| `status` | enum | Task state | `pending`, `in_progress`, `completed` |
| `priority` | enum | Importance | `low`, `normal`, `high` |
| `scheduled` | date | When to start | `2025-11-10` |
| `due` | date | When to finish | `2025-11-11` |
| `tags` | array | Categorization | `[task, tcm_101, week_1]` |
| `contexts` | array | Task context | `[study, homework]` |
| `projects` | array | Parent project | `[[TCM_101_Fundamentals]]` |
| `blocked_by` | array | Dependencies | `[[Week_1_Quiz]]` |
| `blocking` | array | Blocks these | `[[Week_2_Day_1]]` |
| `estimated_minutes` | number | Time estimate | `60` |
| `reminders` | array | Notifications | See reminder structure |

---

## 📝 Task Types in OCDS

### 1. Study Task

```yaml
---
status: pending
priority: high
scheduled: 2025-11-10
due: 2025-11-10
tags: [task, tcm_101, week_1, day_1]
contexts: [study]
projects: ["[[TCM_101_Fundamentals]]"]
estimated_minutes: 60
class_id: "TCM_101"
week: 1
day: 1
task_type: study
material_link: "[[Qi_Deficiency_Pattern]]"
---

# Week 1 Day 1: Study Qi Deficiency Pattern

## Objectives
- Understand the etiology of Qi Deficiency
- Learn cardinal symptoms
- Identify tongue and pulse presentations
- Review treatment principles

## Materials
- [[Qi_Deficiency_Pattern]]
- [[Spleen_Qi_Deficiency]]

## Instructions
1. Read the study material (30 min)
2. Take notes on key concepts (15 min)
3. Review related patterns (15 min)

## Completion Criteria
- [ ] Read all material
- [ ] Notes taken
- [ ] Related patterns reviewed
- [ ] Ready for flashcards

## Next Steps
After completing, proceed to: [[Week_1_Day_1_Flashcards]]
```

---

### 2. Flashcard Review Task

```yaml
---
status: pending
priority: normal
scheduled: 2025-11-10
due: 2025-11-10
tags: [task, tcm_101, week_1, day_1, flashcards]
contexts: [study]
projects: ["[[TCM_101_Fundamentals]]"]
blocked_by: ["[[Week_1_Day_1_Study]]"]
estimated_minutes: 20
class_id: "TCM_101"
week: 1
day: 1
task_type: flashcards
material_link: "[[Flashcards_Patterns_Qi]]"
points_possible: 20
---

# Week 1 Day 1: Review Flashcards

## Task Details
- **Topic:** Qi Deficiency Pattern
- **Cards to review:** ~20 cards
- **Estimated time:** 20 minutes

## Instructions
1. Open Spaced Repetition review (Ctrl/Cmd + P → "Review flashcards")
2. Review all due cards for this topic
3. Rate each card honestly (Again, Hard, Good, Easy)
4. Complete all cards before marking task done

## Materials
- [[Flashcards_Patterns_Qi]]

## Completion Criteria
- [ ] All due cards reviewed
- [ ] Cards rated appropriately
- [ ] Progress logged

## Stats Tracking
Cards studied: `VIEW[{points_earned}][text]` / `VIEW[{points_possible}][text]`

## Next Steps
After completing, proceed to: [[Week_1_Day_1_Quiz]]
```

---

### 3. Quiz Task

```yaml
---
status: pending
priority: high
scheduled: 2025-11-11
due: 2025-11-11
tags: [task, tcm_101, week_1, day_1, quiz]
contexts: [quiz]
projects: ["[[TCM_101_Fundamentals]]"]
blocked_by: 
  - "[[Week_1_Day_1_Study]]"
  - "[[Week_1_Day_1_Flashcards]]"
blocking: ["[[Week_1_Day_2_Study]]"]
estimated_minutes: 15
reminders:
  - id: rem_1730000000000
    type: relative
    relatedTo: due
    offset: -PT2H
    description: "2 hours before quiz due"
class_id: "TCM_101"
week: 1
day: 1
task_type: quiz
material_link: "[[Quiz_Qi_Deficiency]]"
points_possible: 100
points_earned: 0
---

# Week 1 Day 1: Quiz - Qi Deficiency

## Quiz Information
- **Questions:** 10
- **Passing Score:** 70%
- **Time Limit:** 15 minutes
- **Attempts:** 1

## Prerequisites
Before taking this quiz, ensure you have:
- [x] Completed study material
- [x] Reviewed flashcards
- [ ] Feel ready to be assessed

## Instructions
1. Open the quiz: [[Quiz_Qi_Deficiency]]
2. Read each question carefully
3. Select your answers
4. Click "Submit Quiz" when complete
5. Review your results
6. Mark this task complete

## Grading
- Score: `VIEW[{points_earned}][text]` / `VIEW[{points_possible}][text]`
- Percentage: `VIEW[{percentage}][text]`%
- Status: `VIEW[{pass_fail}][text]`

## Next Steps
- **If passed (≥70%):** Proceed to [[Week_1_Day_2_Study]]
- **If failed (<70%):** Review material and retake
```

---

### 4. Homework Task

```yaml
---
status: pending
priority: normal
scheduled: 2025-11-10
due: 2025-11-13
tags: [task, tcm_101, week_1, homework]
contexts: [homework]
projects: ["[[TCM_101_Fundamentals]]"]
estimated_minutes: 120
reminders:
  - id: rem_1730000000001
    type: relative
    relatedTo: due
    offset: -P1D
    description: "1 day before due"
class_id: "TCM_101"
week: 1
task_type: homework
material_link: "[[Homework_Week_1]]"
points_possible: 100
points_earned: 0
---

# Week 1 Homework: Pattern Differentiation Practice

## Assignment Overview
Practice differentiating between similar patterns using case studies.

## Objectives
- Apply pattern differentiation skills
- Analyze tongue and pulse presentations
- Select appropriate treatment principles
- Justify your diagnostic reasoning

## Instructions
1. Open homework assignment: [[Homework_Week_1]]
2. Read each case study
3. Answer all questions
4. Provide justifications
5. Submit by due date

## Deliverables
- [ ] Case 1 analysis complete
- [ ] Case 2 analysis complete
- [ ] Case 3 analysis complete
- [ ] Justifications provided
- [ ] Submitted on time

## Grading Rubric
- Correct diagnosis: 40%
- Reasoning quality: 30%
- Treatment plan: 20%
- Presentation: 10%

## Resources
- [[Qi_Deficiency_Pattern]]
- [[Blood_Deficiency_Pattern]]
- [[Differential_Diagnosis_Guide]]

## Submission
Submit via: [Submission method]
```

---

## 🔗 Task Dependencies (Blocking)

### How Blocking Works

Tasks can depend on other tasks:

```yaml
# Week 1 Day 1 Study
blocked_by: []  # No dependencies, can start immediately
blocking: ["[[Week_1_Day_1_Flashcards]]"]  # Blocks flashcards

# Week 1 Day 1 Flashcards
blocked_by: ["[[Week_1_Day_1_Study]]"]  # Must complete study first
blocking: ["[[Week_1_Day_1_Quiz]]"]  # Blocks quiz

# Week 1 Day 1 Quiz
blocked_by: 
  - "[[Week_1_Day_1_Study]]"
  - "[[Week_1_Day_1_Flashcards]]"
blocking: ["[[Week_1_Day_2_Study]]"]  # Blocks next day
```

### OCDS Blocking Patterns

**Daily Sequence:**
```
Study → Flashcards → Quiz → Next Day
```

**Weekly Sequence:**
```
Week 1 Quiz → Week 2 Day 1
```

**Prerequisite Classes:**
```
TCM_100_Complete → TCM_101_Start
```

---

## ⏰ Reminders

### Reminder Structure

```yaml
reminders:
  - id: rem_1730000000000        # Unique ID (timestamp)
    type: relative                # relative | absolute
    relatedTo: due                # scheduled | due
    offset: -P1D                  # ISO 8601 duration
    description: "1 day before"   # Human-readable
```

### Common Reminder Offsets

| Offset | Meaning |
|--------|---------|
| `-P1D` | 1 day before |
| `-PT2H` | 2 hours before |
| `-PT15M` | 15 minutes before |
| `-P1W` | 1 week before |
| `P0D` | On the day |

### OCDS Reminder Patterns

**Study Tasks:**
```yaml
reminders:
  - id: rem_study_morning
    type: relative
    relatedTo: scheduled
    offset: P0D
    description: "Study session today"
```

**Quiz Tasks:**
```yaml
reminders:
  - id: rem_quiz_day_before
    type: relative
    relatedTo: due
    offset: -P1D
    description: "Quiz tomorrow - review material"
  - id: rem_quiz_2h_before
    type: relative
    relatedTo: due
    offset: -PT2H
    description: "Quiz in 2 hours"
```

**Homework Tasks:**
```yaml
reminders:
  - id: rem_hw_1week
    type: relative
    relatedTo: due
    offset: -P1W
    description: "Homework due in 1 week"
  - id: rem_hw_1day
    type: relative
    relatedTo: due
    offset: -P1D
    description: "Homework due tomorrow"
```

---

## 📊 Task Queries with Dataview

### View All Pending Tasks

```dataview
TABLE
  status as "Status",
  priority as "Priority",
  due as "Due Date",
  estimated_minutes as "Est. Time"
FROM "TaskNotes"
WHERE status = "pending"
  AND contains(tags, "tcm_101")
SORT due ASC
```

### View Today's Tasks

```dataview
TASK
FROM "TaskNotes"
WHERE status != "completed"
  AND scheduled <= date(today)
  AND contains(tags, "tcm_101")
SORT priority DESC, due ASC
```

### View Blocked Tasks

```dataview
LIST blocked_by
FROM "TaskNotes"
WHERE status = "pending"
  AND length(blocked_by) > 0
  AND contains(tags, "tcm_101")
```

### View Completed Tasks This Week

```dataview
TABLE
  dateCompleted as "Completed",
  task_type as "Type",
  points_earned as "Score"
FROM "TaskNotes"
WHERE status = "completed"
  AND dateCompleted >= date(today) - dur(7 days)
  AND contains(tags, "tcm_101")
SORT dateCompleted DESC
```

---

## 🎨 Task Generation

### Automated Task Creation

OCDS generates tasks automatically from timeline:

```python
# generate_tasks.py
def create_study_task(class_id, week, day, material, start_date):
    """Generate a study task from timeline."""
    task_date = start_date + timedelta(weeks=week-1, days=day-1)
    
    frontmatter = {
        'status': 'pending',
        'priority': 'high',
        'scheduled': task_date.isoformat(),
        'due': task_date.isoformat(),
        'tags': ['task', class_id, f'week_{week}', f'day_{day}'],
        'contexts': ['study'],
        'projects': [f'[[{class_id}]]'],
        'estimated_minutes': material.get('estimated_minutes', 60),
        'class_id': class_id,
        'week': week,
        'day': day,
        'task_type': 'study',
        'material_link': f"[[{material['source']}]]"
    }
    
    content = generate_task_content(material)
    
    return create_task_file(frontmatter, content)
```

### Manual Task Creation

Create tasks manually using template:

1. **Create new note** in `TaskNotes/` folder
2. **Add frontmatter** with required fields
3. **Write task content** (objectives, instructions, etc.)
4. **Save** - TaskNotes plugin will index it

---

## 🔄 Task Workflow

### Student Workflow

```
1. VIEW TASKS
   ↓
2. SELECT TASK (by due date/priority)
   ↓
3. OPEN TASK NOTE
   ↓
4. REVIEW OBJECTIVES & MATERIALS
   ↓
5. COMPLETE ACTIVITIES
   ↓
6. CHECK OFF COMPLETION CRITERIA
   ↓
7. UPDATE STATUS TO "completed"
   ↓
8. AUTO-GRADER RUNS (if quiz)
   ↓
9. UNLOCK NEXT TASKS (if conditions met)
   ↓
10. REPEAT
```

### Task State Transitions

```
pending → in_progress → completed
   ↓
cancelled (if no longer needed)
```

---

## 🎯 OCDS Integration

### With Auto-Grader

When quiz task completed:

```python
# auto_grader.py
def on_task_complete(task_file):
    """Triggered when task marked complete."""
    if task_file.frontmatter['task_type'] == 'quiz':
        quiz_file = task_file.frontmatter['material_link']
        score = grade_quiz(quiz_file)
        
        # Update task with score
        update_task_frontmatter(task_file, {
            'points_earned': score,
            'percentage': (score / task_file.frontmatter['points_possible']) * 100
        })
        
        # Check unlock conditions
        check_unlock_conditions(task_file.frontmatter['class_id'])
```

### With Unlock Manager

When task completed, check if next content unlocks:

```python
# unlock_manager.py
def check_unlock_conditions(class_id, week):
    """Check if next week should unlock."""
    week_tasks = get_week_tasks(class_id, week)
    
    if all_tasks_complete(week_tasks):
        week_score = calculate_week_score(week_tasks)
        
        if week_score >= unlock_threshold:
            generate_next_week_tasks(class_id, week + 1)
            notify_student(f"Week {week + 1} unlocked!")
```

### With Progress Dashboard

Display task progress:

```dataview
TABLE
  week as "Week",
  count(rows) as "Total Tasks",
  length(filter(rows, (r) => r.status = "completed")) as "Completed",
  round((length(filter(rows, (r) => r.status = "completed")) / count(rows)) * 100) + "%" as "Progress"
FROM "TaskNotes"
WHERE contains(tags, "tcm_101")
GROUP BY week
SORT week ASC
```

---

## 🛠️ Plugin Configuration

### Recommended Settings

```
Settings → TaskNotes
├── Task folder: "TaskNotes"
├── Template folder: "OCDS_Templates"
├── Date format: "YYYY-MM-DD"
├── Time format: "HH:mm"
├── Auto-create task notes: ON
├── Show task count in sidebar: ON
└── Enable reminders: ON
```

---

## 📝 Best Practices

### Task Organization
- **One task per file** - Keep tasks focused
- **Clear titles** - Include week/day/type
- **Detailed instructions** - No ambiguity
- **Completion criteria** - Checkboxes for sub-tasks
- **Link materials** - Easy access to resources

### Scheduling
- **Realistic estimates** - Don't underestimate time
- **Buffer time** - Add 20% to estimates
- **Consistent schedule** - Same time each day
- **Respect dependencies** - Don't skip prerequisites

### Status Management
- **Update promptly** - Mark in_progress when starting
- **Complete fully** - Don't mark done until finished
- **Cancel wisely** - Only if truly not needed
- **Track time** - Log actual_minutes for future estimates

---

## 🐛 Troubleshooting

### Tasks Not Appearing

**Problem:** Created task doesn't show in queries

**Solutions:**
1. Verify frontmatter is valid YAML
2. Check file is in TaskNotes folder
3. Ensure `status` field exists
4. Refresh vault (Ctrl/Cmd + R)

### Reminders Not Working

**Problem:** No notifications for reminders

**Solutions:**
1. Enable reminders in plugin settings
2. Check reminder syntax is correct
3. Verify offset is negative (for "before")
4. Restart Obsidian

### Blocking Not Working

**Problem:** Can start blocked tasks

**Solutions:**
1. Blocking is informational, not enforced
2. Use queries to filter blocked tasks
3. Implement custom logic in scripts
4. Train students to respect dependencies

---

## ✅ Quick Reference

### Task Frontmatter Template
```yaml
status: pending
priority: normal
scheduled: YYYY-MM-DD
due: YYYY-MM-DD
tags: [task, class_id, week_X, day_Y]
contexts: [study]
projects: ["[[Class_Name]]"]
estimated_minutes: 60
class_id: "CLASS_ID"
week: X
day: Y
task_type: study
```

### Common Queries
```dataview
# Today's tasks
FROM "TaskNotes" WHERE scheduled = date(today)

# Overdue tasks
FROM "TaskNotes" WHERE due < date(today) AND status != "completed"

# This week's tasks
FROM "TaskNotes" WHERE scheduled >= date(today) - dur(7 days)
```

### Task Types
- `study` - Reading and learning
- `flashcards` - Spaced repetition review
- `quiz` - Assessment
- `homework` - Assignment
- `project` - Long-form work
- `review` - Revisit previous material

---

**Organize your learning with TaskNotes! 📋**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
