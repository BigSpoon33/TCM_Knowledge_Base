# Grading Configuration Schema

**Complete specification for `grading_config.yaml`**

---

## 📚 Overview

The grading configuration defines how student performance is calculated and evaluated. It specifies:
- Component weights
- Score calculations
- Passing thresholds
- Unlock conditions
- Grade scales

**Location:** `Classes/{CLASS_NAME}/grading_config.yaml`

---

## 📋 Complete Schema

```yaml
# ===========================================
# GRADING CONFIGURATION SCHEMA v1.0
# ===========================================

# ============ GRADING WEIGHTS ============

weights:
  quizzes: float              # 0.0-1.0 (default: 0.4)
  flashcards: float           # 0.0-1.0 (default: 0.3)
  homework: float             # 0.0-1.0 (default: 0.2)
  pomodoros: float            # 0.0-1.0 (default: 0.1)
  # Must sum to 1.0

# ============ THRESHOLDS ============

thresholds:
  passing_grade: integer      # Minimum % to pass (default: 70)
  unlock_threshold: integer   # Score to unlock early (default: 75)
  excellence_threshold: integer  # High achievement (default: 90)
  warning_threshold: integer  # Struggling student (default: 60)

# ============ QUIZ SETTINGS ============

quiz_settings:
  passing_percentage: integer # % correct to pass (default: 70)
  allow_retakes: boolean      # Allow quiz retakes (default: false)
  retake_count: integer       # Max retakes if allowed (default: 1)
  best_score_counts: boolean  # Use best score (default: true)
  show_answers: boolean       # Show correct answers (default: true)
  time_limit_enforced: boolean  # Enforce time limits (default: true)

# ============ FLASHCARD SETTINGS ============

flashcard_settings:
  daily_target: integer       # Cards per day (default: 20)
  weekly_target: integer      # Cards per week (default: 100)
  retention_weight: float     # Weight retention rate (default: 0.5)
  completion_weight: float    # Weight completion (default: 0.5)
  minimum_retention: integer  # Min retention % (default: 75)

# ============ HOMEWORK SETTINGS ============

homework_settings:
  late_penalty: float         # % penalty per day (default: 0.1)
  max_late_days: integer      # Max days late (default: 7)
  grace_period_hours: integer # Grace period (default: 24)
  completion_required: boolean  # Must complete (default: true)

# ============ POMODORO SETTINGS ============

pomodoro_settings:
  weekly_target: integer      # Pomodoros per week (default: 20)
  daily_target: integer       # Pomodoros per day (default: 3)
  bonus_threshold: integer    # Bonus points threshold (default: 30)
  bonus_points: integer       # Bonus % if exceeded (default: 5)

# ============ GRADE SCALE ============

grade_scale:
  A: 90-100
  B: 80-89
  C: 70-79
  D: 60-69
  F: 0-59

# ============ UNLOCK LOGIC ============

unlock_logic:
  type: string                # "score_based" | "time_based" | "hybrid"
  require_all_complete: boolean  # All tasks must be done (default: false)
  require_passing_quiz: boolean  # Quiz must pass (default: true)
  flexible_pacing: boolean    # Allow early unlock (default: true)
```

---

## 🔍 Field Descriptions

### Grading Weights

#### `weights` (required)

Defines how much each component contributes to overall grade.

```yaml
weights:
  quizzes: 0.4      # 40% of grade
  flashcards: 0.3   # 30% of grade
  homework: 0.2     # 20% of grade
  pomodoros: 0.1    # 10% of grade
```

**Rules:**
- All values must be between 0.0 and 1.0
- Must sum to exactly 1.0
- Can omit components (will be 0)

**Common Configurations:**

**Quiz-Heavy:**
```yaml
weights:
  quizzes: 0.6
  flashcards: 0.2
  homework: 0.2
  pomodoros: 0.0
```

**Balanced:**
```yaml
weights:
  quizzes: 0.4
  flashcards: 0.3
  homework: 0.2
  pomodoros: 0.1
```

**Practice-Heavy:**
```yaml
weights:
  quizzes: 0.3
  flashcards: 0.4
  homework: 0.2
  pomodoros: 0.1
```

---

### Thresholds

#### `passing_grade` (required)
- **Type:** integer
- **Range:** 0-100
- **Default:** 70
- **Purpose:** Minimum percentage to pass class

#### `unlock_threshold` (required)
- **Type:** integer
- **Range:** 0-100
- **Default:** 75
- **Purpose:** Score needed to unlock next week early
- **Rule:** Should be >= passing_grade

#### `excellence_threshold` (optional)
- **Type:** integer
- **Range:** 0-100
- **Default:** 90
- **Purpose:** High achievement recognition

#### `warning_threshold` (optional)
- **Type:** integer
- **Range:** 0-100
- **Default:** 60
- **Purpose:** Flag struggling students

---

### Quiz Settings

#### `passing_percentage` (required)
- **Type:** integer
- **Range:** 0-100
- **Default:** 70
- **Purpose:** % of questions correct to pass quiz

#### `allow_retakes` (optional)
- **Type:** boolean
- **Default:** false
- **Purpose:** Allow students to retake quizzes

#### `retake_count` (conditional)
- **Type:** integer
- **Default:** 1
- **Required if:** allow_retakes = true
- **Purpose:** Maximum number of retakes

#### `best_score_counts` (conditional)
- **Type:** boolean
- **Default:** true
- **Required if:** allow_retakes = true
- **Purpose:** Use best score or average

#### `show_answers` (optional)
- **Type:** boolean
- **Default:** true
- **Purpose:** Show correct answers after submission

#### `time_limit_enforced` (optional)
- **Type:** boolean
- **Default:** true
- **Purpose:** Enforce quiz time limits

---

### Flashcard Settings

#### `daily_target` (optional)
- **Type:** integer
- **Default:** 20
- **Purpose:** Cards to review per day

#### `weekly_target` (optional)
- **Type:** integer
- **Default:** 100
- **Purpose:** Cards to review per week

#### `retention_weight` (optional)
- **Type:** float
- **Range:** 0.0-1.0
- **Default:** 0.5
- **Purpose:** How much retention rate affects score

#### `completion_weight` (optional)
- **Type:** float
- **Range:** 0.0-1.0
- **Default:** 0.5
- **Purpose:** How much completion affects score
- **Rule:** retention_weight + completion_weight = 1.0

#### `minimum_retention` (optional)
- **Type:** integer
- **Range:** 0-100
- **Default:** 75
- **Purpose:** Minimum acceptable retention rate
> actually tho how can we keep track of flashcards viewed? is that  a thing?
---

### Homework Settings

#### `late_penalty` (optional)
- **Type:** float
- **Range:** 0.0-1.0
- **Default:** 0.1 (10% per day)
- **Purpose:** Penalty for late submission

#### `max_late_days` (optional)
- **Type:** integer
- **Default:** 7
- **Purpose:** Maximum days late accepted

#### `grace_period_hours` (optional)
- **Type:** integer
- **Default:** 24
- **Purpose:** Grace period before penalty applies

#### `completion_required` (optional)
- **Type:** boolean
- **Default:** true
- **Purpose:** Must complete to pass week
>I'm getting the homework a little more now. It's basically a custom assignment, can be a combo of quetions, case study, some info, could be a list of links to videos or websites to sign up with.
---

### Pomodoro Settings

#### `weekly_target` (optional)
- **Type:** integer
- **Default:** 20
- **Purpose:** Target Pomodoros per week

#### `daily_target` (optional)
- **Type:** integer
- **Default:** 3
- **Purpose:** Target Pomodoros per day

#### `bonus_threshold` (optional)
- **Type:** integer
- **Default:** 30
- **Purpose:** Pomodoros for bonus points

#### `bonus_points` (optional)
- **Type:** integer
- **Default:** 5
- **Purpose:** Bonus % if threshold exceeded
> pomodoro is build into tasknotes. Can we tap into the pomodoro dashboard 
---

### Grade Scale

#### `grade_scale` (optional)

Letter grade ranges:

```yaml
grade_scale:
  A_plus: 97-100
  A: 93-96
  A_minus: 90-92
  B_plus: 87-89
  B: 83-86
  B_minus: 80-82
  C_plus: 77-79
  C: 73-76
  C_minus: 70-72
  D: 60-69
  F: 0-59
```

**Simple scale:**
```yaml
grade_scale:
  A: 90-100
  B: 80-89
  C: 70-79
  D: 60-69
  F: 0-59
```

---

### Unlock Logic

#### `type` (required)
- **Values:**
  - `"score_based"` - Unlock based on performance
  - `"time_based"` - Unlock on schedule
  - `"hybrid"` - Both (unlock early if score met, or on date)

#### `require_all_complete` (optional)
- **Type:** boolean
- **Default:** false
- **Purpose:** All tasks must be completed to unlock

#### `require_passing_quiz` (optional)
- **Type:** boolean
- **Default:** true
- **Purpose:** Quiz must be passed to unlock

#### `flexible_pacing` (optional)
- **Type:** boolean
- **Default:** true
- **Purpose:** Allow students to progress at own pace

---

## 📝 Complete Example

```yaml
# ===========================================
# TCM 101 Grading Configuration
# ===========================================

# Grading Weights
weights:
  quizzes: 0.4
  flashcards: 0.3
  homework: 0.2
  pomodoros: 0.1

# Thresholds
thresholds:
  passing_grade: 70
  unlock_threshold: 75
  excellence_threshold: 90
  warning_threshold: 60

# Quiz Settings
quiz_settings:
  passing_percentage: 70
  allow_retakes: false
  retake_count: 1
  best_score_counts: true
  show_answers: true
  time_limit_enforced: true

# Flashcard Settings
flashcard_settings:
  daily_target: 20
  weekly_target: 100
  retention_weight: 0.5
  completion_weight: 0.5
  minimum_retention: 75

# Homework Settings
homework_settings:
  late_penalty: 0.1  # 10% per day
  max_late_days: 7
  grace_period_hours: 24
  completion_required: true

# Pomodoro Settings
pomodoro_settings:
  weekly_target: 20
  daily_target: 3
  bonus_threshold: 30
  bonus_points: 5

# Grade Scale
grade_scale:
  A: 90-100
  B: 80-89
  C: 70-79
  D: 60-69
  F: 0-59

# Unlock Logic
unlock_logic:
  type: "hybrid"
  require_all_complete: false
  require_passing_quiz: true
  flexible_pacing: true
```

---

## 🧮 Score Calculations

### Overall Grade Calculation

```python
def calculate_overall_grade(student_data, config):
    """Calculate overall grade from components."""
    
    # Get component scores
    quiz_score = calculate_quiz_score(student_data)
    flashcard_score = calculate_flashcard_score(student_data, config)
    homework_score = calculate_homework_score(student_data, config)
    pomodoro_score = calculate_pomodoro_score(student_data, config)
    
    # Apply weights
    weights = config['weights']
    overall = (
        quiz_score * weights['quizzes'] +
        flashcard_score * weights['flashcards'] +
        homework_score * weights['homework'] +
        pomodoro_score * weights['pomodoros']
    )
    
    return round(overall, 2)
```

---

### Quiz Score

```python
def calculate_quiz_score(student_data):
    """Calculate average quiz score."""
    quizzes = student_data['quizzes']
    
    if not quizzes:
        return 0
    
    total = sum(q['percentage'] for q in quizzes)
    return total / len(quizzes)
```

---

### Flashcard Score

```python
def calculate_flashcard_score(student_data, config):
    """Calculate flashcard score."""
    settings = config['flashcard_settings']
    
    # Completion score
    completed = student_data['flashcards_studied']
    target = settings['weekly_target']
    completion = min((completed / target) * 100, 100)
    
    # Retention score
    retention = student_data['retention_rate']
    
    # Weighted average
    score = (
        completion * settings['completion_weight'] +
        retention * settings['retention_weight']
    )
    
    return score
```

---

### Homework Score

```python
def calculate_homework_score(student_data, config):
    """Calculate homework score with late penalties."""
    settings = config['homework_settings']
    homework = student_data['homework']
    
    if not homework:
        return 0
    
    total_score = 0
    for hw in homework:
        score = hw['score']
        
        # Apply late penalty
        if hw['days_late'] > 0:
            penalty = min(
                hw['days_late'] * settings['late_penalty'],
                1.0  # Max 100% penalty
            )
            score = score * (1 - penalty)
        
        total_score += score
    
    return total_score / len(homework)
```

---

### Pomodoro Score

```python
def calculate_pomodoro_score(student_data, config):
    """Calculate Pomodoro score with bonus."""
    settings = config['pomodoro_settings']
    
    completed = student_data['pomodoros_completed']
    target = settings['weekly_target']
    
    # Base score
    score = min((completed / target) * 100, 100)
    
    # Bonus for exceeding threshold
    if completed >= settings['bonus_threshold']:
        score = min(score + settings['bonus_points'], 100)
    
    return score
```

---

## 🔓 Unlock Logic

### Score-Based Unlock

```python
def check_unlock_score_based(student_data, config):
    """Check if student can unlock next week."""
    overall = calculate_overall_grade(student_data, config)
    threshold = config['thresholds']['unlock_threshold']
    
    # Check overall score
    if overall < threshold:
        return False, f"Need {threshold}%, have {overall}%"
    
    # Check quiz requirement
    if config['unlock_logic']['require_passing_quiz']:
        last_quiz = student_data['quizzes'][-1]
        if last_quiz['percentage'] < config['quiz_settings']['passing_percentage']:
            return False, "Must pass quiz"
    
    # Check completion requirement
    if config['unlock_logic']['require_all_complete']:
        if not all_tasks_complete(student_data):
            return False, "Must complete all tasks"
    
    return True, "Unlocked!"
```

---

### Hybrid Unlock

```python
def check_unlock_hybrid(student_data, config, current_date, scheduled_date):
    """Check unlock with hybrid logic."""
    
    # Try score-based unlock first
    score_unlock, msg = check_unlock_score_based(student_data, config)
    if score_unlock:
        return True, "Unlocked early (score)"
    
    # Fall back to time-based
    if current_date >= scheduled_date:
        return True, "Unlocked on schedule"
    
    # Calculate days until scheduled unlock
    days_remaining = (scheduled_date - current_date).days
    return False, f"Unlocks in {days_remaining} days or reach {config['thresholds']['unlock_threshold']}%"
```

---

## ✅ Validation Rules

```python
def validate_grading_config(config):
    """Validate grading configuration."""
    
    # Check weights sum to 1.0
    weights = config['weights']
    total = sum(weights.values())
    if abs(total - 1.0) > 0.01:
        raise ValueError(f"Weights must sum to 1.0, got {total}")
    
    # Check thresholds are valid
    thresholds = config['thresholds']
    if thresholds['unlock_threshold'] < thresholds['passing_grade']:
        raise ValueError("unlock_threshold must be >= passing_grade")
    
    # Check flashcard weights sum to 1.0
    fc_settings = config['flashcard_settings']
    fc_total = fc_settings['retention_weight'] + fc_settings['completion_weight']
    if abs(fc_total - 1.0) > 0.01:
        raise ValueError(f"Flashcard weights must sum to 1.0, got {fc_total}")
    
    # Check late penalty is reasonable
    hw_settings = config['homework_settings']
    if hw_settings['late_penalty'] > 0.5:
        raise ValueError("late_penalty should not exceed 0.5 (50%)")
    
    return True
```

---

## 💡 Best Practices

### Weight Distribution

**Assessment-Focused:**
- Quizzes: 50-60%
- Homework: 20-30%
- Flashcards: 10-20%
- Pomodoros: 5-10%

**Practice-Focused:**
- Flashcards: 40-50%
- Quizzes: 30-40%
- Homework: 10-20%
- Pomodoros: 5-10%

**Balanced:**
- Quizzes: 40%
- Flashcards: 30%
- Homework: 20%
- Pomodoros: 10%

---

### Threshold Settings

**Lenient:**
- Passing: 60%
- Unlock: 65%
- Excellence: 85%

**Standard:**
- Passing: 70%
- Unlock: 75%
- Excellence: 90%

**Strict:**
- Passing: 75%
- Unlock: 80%
- Excellence: 95%

---

### Late Policies

**Flexible:**
```yaml
late_penalty: 0.05  # 5% per day
max_late_days: 14
grace_period_hours: 48
```

**Standard:**
```yaml
late_penalty: 0.1   # 10% per day
max_late_days: 7
grace_period_hours: 24
```

**Strict:**
```yaml
late_penalty: 0.2   # 20% per day
max_late_days: 3
grace_period_hours: 0
```

---

## 📚 Related Documentation

- **Class Manifest:** `Class_Manifest_Schema.md`
- **Progress Tracking:** `Progress_Tracking_Schema.md`
- **Auto-Grader:** `../07_Grading_System/Auto_Grading_Overview.md`

---

**Configure fair and effective grading! 📊**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
