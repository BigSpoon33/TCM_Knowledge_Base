# Flexible Pacing

**Purpose:** Strategies for accommodating different learning speeds in OCDS

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

Flexible pacing allows students to progress through course materials at their own speed while maintaining structure and accountability. OCDS supports multiple pacing strategies to accommodate diverse learning needs.

---

## 🎯 Pacing Strategies

### 1. Fixed Pacing (Traditional)

**Description:** All students follow same schedule

```yaml
# timeline.yaml
pacing_strategy: fixed
weeks:
  - week: 1
    unlock_date: 2025-01-01
  - week: 2
    unlock_date: 2025-01-08
  - week: 3
    unlock_date: 2025-01-15
```

**Best for:**
- Cohort-based courses
- Live lectures/discussions
- Group projects
- Synchronous learning

---

### 2. Self-Paced (Fully Flexible)

**Description:** Students unlock content as they complete requirements

```yaml
# timeline.yaml
pacing_strategy: self_paced
weeks:
  - week: 1
    unlock_requirements: []  # Week 1 always unlocked
  - week: 2
    unlock_requirements:
      - material_id: quiz_week01
        min_score: 70
  - week: 3
    unlock_requirements:
      - material_id: quiz_week02
        min_score: 70
```

**Best for:**
- Asynchronous courses
- Individual study
- Diverse student backgrounds
- Continuing education

---

### 3. Hybrid Pacing (Recommended)

**Description:** Combines timeline with performance-based unlocking

```yaml
# timeline.yaml
pacing_strategy: hybrid
weeks:
  - week: 2
    unlock_date: 2025-01-08  # Unlocks on this date OR...
    unlock_requirements:      # ...when requirements met
      - material_id: quiz_week01
        min_score: 90  # High threshold for early unlock
```

**Best for:**
- Most OCDS courses
- Balancing flexibility and structure
- Encouraging mastery
- Supporting diverse learners

---

## 🚀 Fast Track Options

### Early Unlock for High Performers

```yaml
# grading_config.yaml
pacing:
  enable_fast_track: true
  fast_track_threshold: 90  # 90% score
  max_weeks_ahead: 2        # Can be up to 2 weeks ahead
```

**Implementation:**
```python
def check_fast_track_eligibility(student_id: str, current_week: int) -> int:
    """Determine how many weeks ahead student can unlock."""
    
    config = load_grading_config()
    
    if not config['pacing']['enable_fast_track']:
        return 0
    
    # Check recent performance
    recent_scores = get_recent_scores(student_id, weeks=3)
    avg_score = sum(recent_scores) / len(recent_scores)
    
    threshold = config['pacing']['fast_track_threshold']
    max_ahead = config['pacing']['max_weeks_ahead']
    
    if avg_score >= threshold:
        return max_ahead
    
    return 0
```

**Benefits:**
- Keeps advanced students engaged
- Rewards consistent high performance
- Prevents boredom
- Allows acceleration

---

## 🐢 Slow Track Support

### Extended Deadlines for Struggling Students

```yaml
# grading_config.yaml
pacing:
  enable_extensions: true
  auto_extend_threshold: 60  # Auto-extend if score < 60%
  extension_days: 7          # Add 7 days
  max_extensions: 2          # Per week
```

**Implementation:**
```python
def check_extension_eligibility(student_id: str, week: int) -> bool:
    """Check if student qualifies for deadline extension."""
    
    config = load_grading_config()
    
    if not config['pacing']['enable_extensions']:
        return False
    
    week_score = get_week_average(student_id, week)
    threshold = config['pacing']['auto_extend_threshold']
    
    if week_score < threshold:
        extensions_used = get_extensions_used(student_id, week)
        max_extensions = config['pacing']['max_extensions']
        
        if extensions_used < max_extensions:
            return True
    
    return False
```

**Benefits:**
- Reduces student stress
- Allows time for mastery
- Prevents falling behind
- Supports diverse needs

---

## 📊 Pacing Profiles

### Student Pacing Types

**1. Accelerated Learner**
```
Week 1: Completed in 3 days (early unlock)
Week 2: Completed in 4 days (early unlock)
Week 3: Completed in 3 days (early unlock)

Status: 2 weeks ahead of schedule
```

**2. On-Pace Learner**
```
Week 1: Completed in 7 days (on schedule)
Week 2: Completed in 7 days (on schedule)
Week 3: Completed in 7 days (on schedule)

Status: On track
```

**3. Deliberate Learner**
```
Week 1: Completed in 10 days (extension granted)
Week 2: Completed in 9 days (extension granted)
Week 3: Completed in 8 days (improving)

Status: Slightly behind, improving
```

---

## 🔧 Configuring Pacing

### Timeline Configuration

```yaml
# timeline.yaml
class_id: TCM_101
pacing_strategy: hybrid

# Global pacing settings
pacing_settings:
  default_week_duration: 7  # days
  min_week_duration: 3      # Can't complete faster than 3 days
  max_week_duration: 14     # Must complete within 14 days
  
weeks:
  - week: 1
    title: "Introduction to Tongue Diagnosis"
    unlock_date: 2025-01-01
    due_date: 2025-01-07
    unlock_requirements: []  # Always unlocked
    
  - week: 2
    title: "Pulse Diagnosis Fundamentals"
    unlock_date: 2025-01-08
    due_date: 2025-01-14
    unlock_requirements:
      - material_id: quiz_week01
        min_score: 70
      - material_id: task_week01
        min_completion: 80
    early_unlock_threshold: 90  # Override global
```

---

## 📈 Pacing Analytics

### Student Pacing Dashboard

```dataview
TABLE
  week as "Week",
  days_to_complete as "Days",
  unlock_reason as "Unlock Type",
  pace_status as "Status"
FROM "Classes/TCM_101/Progress"
WHERE student_id = "john_doe"
```

**Pace Status:**
- 🚀 **Accelerated** - Completed early
- ✅ **On-Pace** - Completed on schedule
- ⏱️ **Extended** - Used extension
- ⚠️ **Behind** - Past due date

---

### Class Pacing Distribution

```dataviewjs
const students = dv.pages('"Classes/TCM_101/Progress"');

const accelerated = students.filter(s => s.pace_status === 'accelerated').length;
const onPace = students.filter(s => s.pace_status === 'on-pace').length;
const extended = students.filter(s => s.pace_status === 'extended').length;
const behind = students.filter(s => s.pace_status === 'behind').length;

dv.paragraph(`
**Class Pacing Distribution:**
- 🚀 Accelerated: ${accelerated} students
- ✅ On-Pace: ${onPace} students
- ⏱️ Extended: ${extended} students
- ⚠️ Behind: ${behind} students
`);
```

---

## 🎯 Best Practices

### For Instructors

**Designing Flexible Pacing:**
- ✅ **Set reasonable defaults** - 7 days per week is standard
- ✅ **Allow acceleration** - Don't hold back fast learners
- ✅ **Support extensions** - Help struggling students
- ✅ **Monitor pacing** - Track who's ahead/behind
- ✅ **Adjust as needed** - Respond to class needs

**Communicating Pacing:**
- ✅ **Explain options** - Students should understand flexibility
- ✅ **Set expectations** - Clarify deadlines vs. recommendations
- ✅ **Encourage planning** - Help students pace themselves
- ✅ **Provide feedback** - Let students know their pace status

---

### For Students

**Managing Your Pace:**
- ✅ **Know your style** - Fast, moderate, or deliberate?
- ✅ **Plan ahead** - Don't wait until deadlines
- ✅ **Use flexibility** - Take advantage of early unlock
- ✅ **Ask for extensions** - If you need more time
- ✅ **Stay consistent** - Regular progress beats cramming

**Pacing Strategies:**
```
Fast Learner:
- Complete materials as soon as unlocked
- Aim for early unlock bonuses
- Use extra time for deeper study
- Help peers in discussions

Moderate Learner:
- Follow recommended schedule
- Complete by due dates
- Balance with other commitments
- Maintain steady progress

Deliberate Learner:
- Start materials early
- Request extensions if needed
- Focus on mastery over speed
- Use all available resources
```

---

## 📚 Related Documentation

- [[Progression_Logic.md]] - Unlock logic
- [[Review_Flags.md]] - Student support
- [[Timeline_Schema.md]] - Timeline configuration
- [[unlock_manager.py.md]] - Unlock script

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
