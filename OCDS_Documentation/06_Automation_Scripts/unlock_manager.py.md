# unlock_manager.py - Content Unlock Manager

**Purpose:** Manage content unlocking based on performance and timeline

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

The `unlock_manager.py` script controls **when students can access new content**. It checks unlock requirements (quiz scores, task completion, timeline dates), evaluates student performance, and unlocks content when requirements are met. It also handles early unlocking for high performers and flags struggling students for review.

---

## 🚀 Quick Start

```bash
# Check unlock status for all weeks
python unlock_manager.py --class-id TCM_101 --student-id john_doe --check-all

# Check specific week
python unlock_manager.py --class-id TCM_101 --student-id john_doe --week 5

# Force unlock (instructor override)
python unlock_manager.py --class-id TCM_101 --student-id john_doe --week 5 --force
```

---

## 📖 Command Line Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--class-id` | Class identifier (required) | `--class-id TCM_101` |
| `--student-id` | Student identifier (required) | `--student-id john_doe` |
| `--week` | Check specific week | `--week 5` |
| `--check-all` | Check all weeks | `--check-all` |
| `--force` | Force unlock (override) | `--force` |

---

## 🏗️ How It Works

### Unlock Logic

```python
def check_unlock_requirements(class_id: str, student_id: str, week: int) -> bool:
    """Check if student meets unlock requirements for a week."""
    
    timeline = load_timeline(class_id)
    progress = load_progress(class_id, student_id)
    grading_config = load_grading_config(class_id)
    
    week_data = timeline['weeks'][week - 1]
    unlock_reqs = week_data.get('unlock_requirements', {})
    
    # Check timeline date
    unlock_date = week_data.get('unlock_date')
    if unlock_date and datetime.now() < parse_date(unlock_date):
        return False  # Not yet scheduled
    
    # Check previous week completion
    if week > 1:
        prev_week = week - 1
        prev_quiz_score = progress['quizzes'].get(f'quiz_week{prev_week:02d}', {}).get('score', 0)
        prev_task_completion = progress['tasks'].get(f'task_week{prev_week:02d}', {}).get('completion', 0)
        
        min_quiz_score = unlock_reqs.get('min_quiz_score', 70)
        min_task_completion = unlock_reqs.get('min_task_completion', 80)
        
        # Performance-based unlock
        if prev_quiz_score >= min_quiz_score and prev_task_completion >= min_task_completion:
            return True
        
        # Early unlock for high performers
        if prev_quiz_score >= grading_config.get('early_unlock_threshold', 90):
            return True
        
        # Review flag for struggling students
        if prev_quiz_score < 60:
            flag_for_review(class_id, student_id, week)
            return False  # Don't block, but flag
    
    return True  # Week 1 or requirements met
```

---

## 📊 Example Output

```
🔓 OCDS Unlock Manager
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Class: TCM_101
Student: john_doe

📅 Checking Unlock Requirements...

Week 1: ✅ Unlocked (completed)
  Quiz: 90% ✅ (required: 70%)
  Tasks: 100% ✅ (required: 80%)
  Status: Complete

Week 2: ✅ Unlocked (completed)
  Quiz: 85% ✅ (required: 70%)
  Tasks: 100% ✅ (required: 80%)
  Status: Complete

Week 3: ✅ Unlocked (in progress)
  Quiz: 95% ✅ (required: 70%)
  Tasks: 80% ✅ (required: 80%)
  Status: In Progress

Week 4: 🔒 Locked
  Requirements:
    - Week 3 Quiz: ❌ Not completed
    - Week 3 Tasks: ✅ 80% complete
    - Timeline date: ✅ 2025-01-22 (passed)
  
  🎯 Early Unlock Available!
  Week 3 score: 95% (threshold: 90%)
  
  Action: Unlocking Week 4 early...
  ✅ Week 4 unlocked!

Week 5: 🔒 Locked
  Timeline date: 2025-01-29 (not yet reached)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Unlock check complete

Summary:
  Unlocked: 4 weeks
  Locked: 8 weeks
  Actions taken: 1 (Week 4 early unlock)
```

---

## 🎯 Unlock Strategies

### 1. Timeline-Based (Default)
- Week unlocks on scheduled date
- Predictable pacing
- Good for cohort-based learning

### 2. Performance-Based
- Unlock when requirements met
- Flexible pacing
- Rewards high performers

### 3. Hybrid (Recommended)
- Unlock on date OR when requirements met
- Whichever comes first
- Best of both worlds

### 4. Review Flags (Not Blocks)
- Flag struggling students
- Don't prevent progress
- Offer support, not roadblocks

---

## 📚 Related Documentation

- [[Script_Overview.md]] - All automation scripts
- [[Timeline_Schema.md]] - Timeline configuration
- [[Progress_Tracking_Schema.md]] - Progress tracking
- [[Grading_Config_Schema.md]] - Unlock thresholds

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
