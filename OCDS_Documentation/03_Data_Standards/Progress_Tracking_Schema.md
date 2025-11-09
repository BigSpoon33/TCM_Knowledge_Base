# Progress Tracking Schema

**Complete specification for student progress data**

---

## 📚 Overview

Progress tracking files store individual student performance data. They include:
- Overall grades
- Component scores
- Activity logs
- Time tracking
- Completion status

**Location:** `Student_Progress/{STUDENT_ID}/{CLASS_ID}_progress.yaml`

---

## 📋 Complete Schema

```yaml
# ===========================================
# PROGRESS TRACKING SCHEMA v1.0
# ===========================================

# ============ STUDENT INFO ============

student_id: string            # Unique student identifier
student_name: string          # Full name
class_id: string              # Class enrolled in
start_date: YYYY-MM-DD        # Class start date
status: string                # enrolled | in_progress | completed | withdrawn

# ============ PROGRESS ============

current_week: integer         # Current week number
total_weeks: integer          # Total weeks in class
current_day: integer          # Current day in week
completion_percentage: float  # Overall completion %

# ============ GRADES ============

overall_grade: float          # Overall percentage (0-100)
letter_grade: string          # A, B, C, D, F

component_scores:
  quizzes: float             # Quiz average (0-100)
  flashcards: float          # Flashcard score (0-100)
  homework: float            # Homework average (0-100)
  pomodoros: float           # Pomodoro score (0-100)

# ============ QUIZ DATA ============

quizzes:
  - quiz_id: string
    week: integer
    day: integer
    topic: string
    date_taken: YYYY-MM-DD
    score: integer           # Points earned
    total_points: integer    # Points possible
    percentage: float        # Score percentage
    pass_fail: string        # Pass | Fail
    time_taken_minutes: integer
    attempt_number: integer

# ============ FLASHCARD DATA ============

flashcard_stats:
  total_cards_studied: integer
  cards_due_today: integer
  cards_mastered: integer
  average_ease: float
  retention_rate: float      # Percentage
  study_streak_days: integer
  last_review_date: YYYY-MM-DD

weekly_flashcard_log:
  - week: integer
    cards_studied: integer
    retention_rate: float
    time_spent_minutes: integer

# ============ HOMEWORK DATA ============

homework:
  - homework_id: string
    week: integer
    title: string
    assigned_date: YYYY-MM-DD
    due_date: YYYY-MM-DD
    submitted_date: YYYY-MM-DD
    days_late: integer
    score: float             # Percentage
    status: string           # pending | submitted | graded

# ============ POMODORO DATA ============

pomodoro_stats:
  total_pomodoros: integer
  total_minutes: integer
  weekly_average: float
  daily_average: float
  longest_streak_days: integer
  current_streak_days: integer

weekly_pomodoro_log:
  - week: integer
    pomodoros_completed: integer
    total_minutes: integer
    days_active: integer

# ============ ACTIVITY LOG ============

activity_log:
  - date: YYYY-MM-DD
    activity_type: string    # study | quiz | flashcards | homework
    duration_minutes: integer
    items_completed: integer
    notes: string

# ============ UNLOCK STATUS ============

unlocked_weeks: array         # List of unlocked week numbers
  - 1
  - 2

next_unlock:
  week: integer
  condition: string          # score_threshold | date | completed
  requirement: string        # Description of what's needed
  progress: float            # Progress toward unlock (0-100)

# ============ FLAGS & ALERTS ============

flags:
  struggling: boolean        # Below warning threshold
  excelling: boolean         # Above excellence threshold
  at_risk: boolean          # Multiple failed quizzes
  inactive: boolean         # No activity in 7 days

alerts:
  - type: string            # warning | info | success
    message: string
    date: YYYY-MM-DD
    resolved: boolean

# ============ METADATA ============

last_activity_date: YYYY-MM-DD
last_updated: YYYY-MM-DDTHH:mm:ss
created: YYYY-MM-DD
```
> I want this to be super slick and functional. this is how it's going to make the user not feel like they have to manage all the backend. most people just want to look at the frontend and have a big red click here button and easy to comprehend list of things due. some basic features like day, week, month view, class list, list of assignments due and completed, links to related materials
---

## 📝 Complete Example

```yaml
# ===========================================
# Student Progress - John Doe
# ===========================================

# Student Info
student_id: "JD110590"
student_name: "John Doe"
class_id: "TCM_101"
start_date: 2025-11-01
status: "in_progress"

# Progress
current_week: 2
total_weeks: 12
current_day: 3
completion_percentage: 15.5

# Grades
overall_grade: 82.5
letter_grade: "B"

component_scores:
  quizzes: 85.0
  flashcards: 88.0
  homework: 80.0
  pomodoros: 75.0

# Quiz Data
quizzes:
  - quiz_id: "TCM_101_W1_Quiz"
    week: 1
    day: 5
    topic: "Qi Deficiency Pattern"
    date_taken: 2025-11-05
    score: 8
    total_points: 10
    percentage: 80.0
    pass_fail: "Pass"
    time_taken_minutes: 12
    attempt_number: 1
  
  - quiz_id: "TCM_101_W2_Quiz"
    week: 2
    day: 5
    topic: "Blood Deficiency Pattern"
    date_taken: 2025-11-12
    score: 9
    total_points: 10
    percentage: 90.0
    pass_fail: "Pass"
    time_taken_minutes: 14
    attempt_number: 1

# Flashcard Data
flashcard_stats:
  total_cards_studied: 150
  cards_due_today: 20
  cards_mastered: 45
  average_ease: 265
  retention_rate: 87.5
  study_streak_days: 12
  last_review_date: 2025-11-12

weekly_flashcard_log:
  - week: 1
    cards_studied: 75
    retention_rate: 85.0
    time_spent_minutes: 180
  
  - week: 2
    cards_studied: 75
    retention_rate: 90.0
    time_spent_minutes: 165

# Homework Data
homework:
  - homework_id: "TCM_101_W1_HW"
    week: 1
    title: "Pattern Differentiation Practice"
    assigned_date: 2025-11-01
    due_date: 2025-11-07
    submitted_date: 2025-11-06
    days_late: 0
    score: 85.0
    status: "graded"
  
  - homework_id: "TCM_101_W2_HW"
    week: 2
    title: "Case Study Analysis"
    assigned_date: 2025-11-08
    due_date: 2025-11-14
    submitted_date: 2025-11-15
    days_late: 1
    score: 75.0
    status: "graded"

# Pomodoro Data
pomodoro_stats:
  total_pomodoros: 28
  total_minutes: 700
  weekly_average: 14.0
  daily_average: 2.0
  longest_streak_days: 7
  current_streak_days: 5

weekly_pomodoro_log:
  - week: 1
    pomodoros_completed: 15
    total_minutes: 375
    days_active: 6
  
  - week: 2
    pomodoros_completed: 13
    total_minutes: 325
    days_active: 5

# Activity Log
activity_log:
  - date: 2025-11-12
    activity_type: "study"
    duration_minutes: 60
    items_completed: 1
    notes: "Completed Blood Deficiency study material"
  
  - date: 2025-11-12
    activity_type: "flashcards"
    duration_minutes: 20
    items_completed: 25
    notes: "Reviewed Week 2 flashcards"
  
  - date: 2025-11-12
    activity_type: "quiz"
    duration_minutes: 14
    items_completed: 1
    notes: "Passed Week 2 quiz with 90%"

# Unlock Status
unlocked_weeks: [1, 2]

next_unlock:
  week: 3
  condition: "score_threshold"
  requirement: "Maintain 75% average or wait until 2025-11-15"
  progress: 82.5

# Flags & Alerts
flags:
  struggling: false
  excelling: true
  at_risk: false
  inactive: false

alerts:
  - type: "success"
    message: "Excellent performance! Week 3 unlocked early."
    date: 2025-11-12
    resolved: true
  
  - type: "info"
    message: "Homework submitted 1 day late. 10% penalty applied."
    date: 2025-11-15
    resolved: true

# Metadata
last_activity_date: 2025-11-12
last_updated: 2025-11-12T18:30:00
created: 2025-11-01
```

---

## 🔄 Update Patterns

### After Quiz Completion

```python
def update_after_quiz(progress_file, quiz_data):
    """Update progress after quiz completion."""
    
    # Add quiz to list
    progress_file['quizzes'].append({
        'quiz_id': quiz_data['quiz_id'],
        'week': quiz_data['week'],
        'day': quiz_data['day'],
        'topic': quiz_data['topic'],
        'date_taken': datetime.now().date(),
        'score': quiz_data['score'],
        'total_points': quiz_data['total_points'],
        'percentage': (quiz_data['score'] / quiz_data['total_points']) * 100,
        'pass_fail': 'Pass' if quiz_data['percentage'] >= 70 else 'Fail',
        'time_taken_minutes': quiz_data['time_taken'],
        'attempt_number': 1
    })
    
    # Recalculate quiz average
    quiz_avg = sum(q['percentage'] for q in progress_file['quizzes']) / len(progress_file['quizzes'])
    progress_file['component_scores']['quizzes'] = quiz_avg
    
    # Recalculate overall grade
    progress_file['overall_grade'] = calculate_overall_grade(progress_file)
    
    # Update metadata
    progress_file['last_activity_date'] = datetime.now().date()
    progress_file['last_updated'] = datetime.now()
    
    # Check unlock conditions
    check_unlock(progress_file)
    
    # Check flags
    update_flags(progress_file)
```

---

### After Flashcard Session

```python
def update_after_flashcards(progress_file, session_data):
    """Update progress after flashcard session."""
    
    # Update stats
    stats = progress_file['flashcard_stats']
    stats['total_cards_studied'] += session_data['cards_studied']
    stats['retention_rate'] = session_data['retention_rate']
    stats['last_review_date'] = datetime.now().date()
    
    # Update streak
    if session_data['date'] == datetime.now().date():
        stats['study_streak_days'] += 1
    else:
        stats['study_streak_days'] = 1
    
    # Update weekly log
    current_week = progress_file['current_week']
    week_log = next((w for w in progress_file['weekly_flashcard_log'] if w['week'] == current_week), None)
    
    if week_log:
        week_log['cards_studied'] += session_data['cards_studied']
        week_log['time_spent_minutes'] += session_data['duration']
    else:
        progress_file['weekly_flashcard_log'].append({
            'week': current_week,
            'cards_studied': session_data['cards_studied'],
            'retention_rate': session_data['retention_rate'],
            'time_spent_minutes': session_data['duration']
        })
    
    # Recalculate flashcard score
    progress_file['component_scores']['flashcards'] = calculate_flashcard_score(progress_file)
    
    # Recalculate overall grade
    progress_file['overall_grade'] = calculate_overall_grade(progress_file)
```

---

### After Pomodoro Session

```python
def update_after_pomodoro(progress_file, pomodoro_count):
    """Update progress after Pomodoro session."""
    
    # Update stats
    stats = progress_file['pomodoro_stats']
    stats['total_pomodoros'] += pomodoro_count
    stats['total_minutes'] += pomodoro_count * 25
    
    # Update weekly log
    current_week = progress_file['current_week']
    week_log = next((w for w in progress_file['weekly_pomodoro_log'] if w['week'] == current_week), None)
    
    if week_log:
        week_log['pomodoros_completed'] += pomodoro_count
        week_log['total_minutes'] += pomodoro_count * 25
    else:
        progress_file['weekly_pomodoro_log'].append({
            'week': current_week,
            'pomodoros_completed': pomodoro_count,
            'total_minutes': pomodoro_count * 25,
            'days_active': 1
        })
    
    # Recalculate averages
    total_days = (datetime.now().date() - progress_file['start_date']).days + 1
    stats['daily_average'] = stats['total_pomodoros'] / total_days
    stats['weekly_average'] = stats['total_pomodoros'] / progress_file['current_week']
    
    # Recalculate pomodoro score
    progress_file['component_scores']['pomodoros'] = calculate_pomodoro_score(progress_file)
    
    # Recalculate overall grade
    progress_file['overall_grade'] = calculate_overall_grade(progress_file)
```

---

## 🚦 Flag Management

### Update Flags

```python
def update_flags(progress_file, config):
    """Update student flags based on performance."""
    
    grade = progress_file['overall_grade']
    thresholds = config['thresholds']
    
    # Struggling flag
    progress_file['flags']['struggling'] = grade < thresholds['warning_threshold']
    
    # Excelling flag
    progress_file['flags']['excelling'] = grade >= thresholds['excellence_threshold']
    
    # At-risk flag (multiple failed quizzes)
    recent_quizzes = progress_file['quizzes'][-3:]  # Last 3 quizzes
    failed_count = sum(1 for q in recent_quizzes if q['pass_fail'] == 'Fail')
    progress_file['flags']['at_risk'] = failed_count >= 2
    
    # Inactive flag (no activity in 7 days)
    last_activity = progress_file['last_activity_date']
    days_since = (datetime.now().date() - last_activity).days
    progress_file['flags']['inactive'] = days_since >= 7
```

---

### Generate Alerts

```python
def generate_alerts(progress_file, config):
    """Generate alerts based on flags."""
    
    alerts = []
    flags = progress_file['flags']
    
    if flags['struggling']:
        alerts.append({
            'type': 'warning',
            'message': f"Grade below {config['thresholds']['warning_threshold']}%. Consider reviewing material.",
            'date': datetime.now().date(),
            'resolved': False
        })
    
    if flags['excelling']:
        alerts.append({
            'type': 'success',
            'message': f"Excellent work! Grade above {config['thresholds']['excellence_threshold']}%.",
            'date': datetime.now().date(),
            'resolved': False
        })
    
    if flags['at_risk']:
        alerts.append({
            'type': 'warning',
            'message': "Multiple quiz failures. Please review study materials.",
            'date': datetime.now().date(),
            'resolved': False
        })
    
    if flags['inactive']:
        alerts.append({
            'type': 'info',
            'message': "No activity in 7 days. Don't fall behind!",
            'date': datetime.now().date(),
            'resolved': False
        })
    
    # Add new alerts
    progress_file['alerts'].extend(alerts)
```

---

## 📊 Dashboard Integration

### Dataview Queries

**Overall progress:**
```dataview
TABLE WITHOUT ID
  "Current Week" as "Metric",
  current_week + " / " + total_weeks as "Value",
  round((current_week / total_weeks) * 100) + "%" as "Progress"
FROM "Student_Progress"
WHERE student_id = "JD110590" AND class_id = "TCM_101"
```

**Component scores:**
```dataview
TABLE WITHOUT ID
  "Component" as "Category",
  "Score" as "Value"
FROM "Student_Progress"
WHERE student_id = "JD110590"
FLATTEN [
  ["Quizzes", component_scores.quizzes],
  ["Flashcards", component_scores.flashcards],
  ["Homework", component_scores.homework],
  ["Pomodoros", component_scores.pomodoros]
] AS pair
```

**Recent activity:**
```dataview
TABLE
  date as "Date",
  activity_type as "Activity",
  duration_minutes as "Duration",
  notes as "Notes"
FROM "Student_Progress"
WHERE student_id = "JD110590"
FLATTEN activity_log AS activity
SORT activity.date DESC
LIMIT 10
```

---

## 💡 Best Practices

### Update Frequency
- **After each activity** - Real-time tracking
- **Daily rollup** - End-of-day summary
- **Weekly summary** - Calculate trends
- **On-demand** - When viewing dashboard

### Data Retention
- **Keep all data** - Complete history
- **Archive old classes** - After completion
- **Backup regularly** - Prevent data loss

### Privacy
- **Student ID only** - No sensitive info
- **Local storage** - In vault
- **Access control** - Instructor only
> Would be good to have these as part of a dashboard to see recent activity, summary, review schedule
---

## 📚 Related Documentation

- **Grading Config:** `Grading_Config_Schema.md`
- **Class Manifest:** `Class_Manifest_Schema.md`
- **Dashboard Design:** `../09_Dashboard_Design/Progress_Dashboard.md`

---

**Track student progress effectively! 📈**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
