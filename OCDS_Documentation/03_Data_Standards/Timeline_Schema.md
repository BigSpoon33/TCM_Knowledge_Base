# Timeline Schema

**Complete specification for `timeline.yaml`**

---

## 📚 Overview

The timeline defines the week-by-week, day-by-day structure of a class. It specifies:
- Weekly organization
- Daily materials
- Task scheduling
- Unlock conditions
- Content progression

**Location:** `Classes/{CLASS_NAME}/timeline.yaml`

---

## 📋 Complete Schema

```yaml
# ===========================================
# TIMELINE SCHEMA v1.0
# ===========================================

weeks:
  - week_number: integer          # Week number (1-52)
    title: string                 # Week title/theme
    unlock_condition: string      # How this week unlocks
    unlock_score_required: integer  # Score needed (if applicable)
    description: string           # Week overview
    
    days:
      - day_number: integer       # Day number (1-7)
        title: string             # Day title/theme
        description: string       # Day overview
        
        materials:
          - type: string          # Material type
            source: string        # Path to material
            title: string         # Display name
            count: integer        # For flashcards
            questions: integer    # For quizzes
            passing_score: integer  # For quizzes
            estimated_minutes: integer
        
        tasks:
          - type: string          # Task type
            estimated_minutes: integer
            due_offset: string    # ISO 8601 duration
            priority: string      # low | normal | high
```

---

## 🔍 Field Descriptions

### Week Object

#### `week_number` (required)
- **Type:** integer
- **Range:** 1-52
- **Example:** `1`
- **Purpose:** Sequential week identifier

#### `title` (optional)
- **Type:** string
- **Example:** `"Introduction to Qi Patterns"`
- **Purpose:** Week theme/name

#### `unlock_condition` (required)
- **Type:** string
- **Values:**
  - `"class_start"` - Available immediately
  - `"week_X_complete"` - After week X complete
  - `"score_threshold"` - After reaching score
  - `"date_YYYY-MM-DD"` - On specific date
- **Example:** `"week_1_complete"`

#### `unlock_score_required` (conditional)
- **Type:** integer
- **Range:** 0-100
- **Required if:** `unlock_condition = "score_threshold"`
- **Example:** `75`

#### `description` (optional)
- **Type:** string
- **Example:** `"This week covers the fundamentals of Qi Deficiency pattern"`

---

### Day Object

#### `day_number` (required)
- **Type:** integer
- **Range:** 1-7
- **Example:** `1`

#### `title` (optional)
- **Type:** string
- **Example:** `"Qi Deficiency: Etiology & Pathogenesis"`

#### `description` (optional)
- **Type:** string
- **Example:** `"Learn the causes and development of Qi Deficiency"`

---

### Material Object

#### `type` (required)
- **Type:** string
- **Values:**
  - `"study"` - Reading material
  - `"flashcards"` - SR flashcards
  - `"quiz"` - Assessment
  - `"homework"` - Assignment
  - `"slides"` - Presentation
  - `"video"` - Video content
  - `"discussion"` - Guided conversation
- **Example:** `"study"`

#### `source` (required for study/flashcards/slides)
- **Type:** string
- **Format:** Path relative to Materials folder
- **Example:** `"TCM_Patterns/Qi_Deficiency.md"`

#### `title` (required)
- **Type:** string
- **Example:** `"Introduction to Qi Deficiency"`

#### `count` (required for flashcards)
- **Type:** integer
- **Example:** `20`
- **Purpose:** Number of flashcards to review

#### `questions` (required for quizzes)
- **Type:** integer
- **Example:** `10`
- **Purpose:** Number of quiz questions

#### `passing_score` (required for quizzes)
- **Type:** integer
- **Range:** 0-questions
- **Example:** `7` (70% of 10)

#### `estimated_minutes` (optional)
- **Type:** integer
- **Example:** `60`
- **Purpose:** Time estimate for planning
>This makes me wonder about how to link and tag material. for example there is almost like a root material of the note and then the bank, cards, slides, etc are all linked to the root. this way you can just have the root be like the comprehensive note I made for all the herbs, formulas, patterns, points, etc. and then the linked material is used for study,homework, class stuff. but you keep the comprehensive note forever and can always check it out again or reference it. 
---

### Task Object

#### `type` (required)
- **Type:** string
- **Values:** Same as material types
- **Example:** `"study"`

#### `estimated_minutes` (required)
- **Type:** integer
- **Example:** `60`

#### `due_offset` (required)
- **Type:** string
- **Format:** ISO 8601 duration
- **Examples:**
  - `"+0d"` - Due same day
  - `"+1d"` - Due next day
  - `"+3h"` - Due in 3 hours
  - `"+1w"` - Due in 1 week
- **Purpose:** When task is due relative to day start

#### `priority` (optional)
- **Type:** string
- **Values:** `low`, `normal`, `high`
- **Default:** `normal`

---

## 📝 Complete Example

```yaml
# ===========================================
# TCM 101 Timeline
# ===========================================

weeks:
  # ============ WEEK 1 ============
  - week_number: 1
    title: "Introduction to Qi Patterns"
    unlock_condition: "class_start"
    description: "Foundation week covering Qi Deficiency and related patterns"
    
    days:
      # Day 1
      - day_number: 1
        title: "Qi Deficiency: Overview"
        description: "Introduction to Qi Deficiency pattern"
        
        materials:
          - type: "study"
            source: "TCM_Patterns/Qi_Deficiency.md"
            title: "Qi Deficiency Pattern"
            estimated_minutes: 60
          
          - type: "flashcards"
            source: "Flashcards/Patterns_Qi.md"
            title: "Qi Patterns Flashcards"
            count: 20
            estimated_minutes: 20
          
          - type: "quiz"
            title: "Qi Deficiency Quiz"
            questions: 10
            passing_score: 7
            estimated_minutes: 15
        
        tasks:
          - type: "study"
            estimated_minutes: 60
            due_offset: "+0d"
            priority: "high"
          
          - type: "flashcards"
            estimated_minutes: 20
            due_offset: "+0d"
            priority: "normal"
          
          - type: "quiz"
            estimated_minutes: 15
            due_offset: "+1d"
            priority: "high"
      
      # Day 2
      - day_number: 2
        title: "Spleen Qi Deficiency"
        description: "Deep dive into Spleen Qi Deficiency"
        
        materials:
          - type: "study"
            source: "TCM_Patterns/Spleen_Qi_Deficiency.md"
            title: "Spleen Qi Deficiency"
            estimated_minutes: 60
          
          - type: "slides"
            source: "Slides/Spleen_Qi_Deficiency_Slides.md"
            title: "Spleen Qi Deficiency Presentation"
            estimated_minutes: 30
          
          - type: "flashcards"
            source: "Flashcards/Patterns_Qi.md"
            title: "Qi Patterns Review"
            count: 15
            estimated_minutes: 15
        
        tasks:
          - type: "study"
            estimated_minutes: 60
            due_offset: "+0d"
            priority: "high"
          
          - type: "flashcards"
            estimated_minutes: 15
            due_offset: "+0d"
            priority: "normal"
      
      # Day 3
      - day_number: 3
        title: "Lung Qi Deficiency"
        description: "Understanding Lung Qi Deficiency"
        
        materials:
          - type: "study"
            source: "TCM_Patterns/Lung_Qi_Deficiency.md"
            title: "Lung Qi Deficiency"
            estimated_minutes: 60
          
          - type: "homework"
            title: "Pattern Comparison Assignment"
            estimated_minutes: 90
        
        tasks:
          - type: "study"
            estimated_minutes: 60
            due_offset: "+0d"
            priority: "high"
          
          - type: "homework"
            estimated_minutes: 90
            due_offset: "+3d"
            priority: "normal"
      
      # Days 4-7 (similar structure)
      - day_number: 4
        title: "Review Day"
        materials:
          - type: "flashcards"
            source: "Flashcards/Patterns_Qi.md"
            title: "Week 1 Review"
            count: 30
            estimated_minutes: 30
        tasks:
          - type: "flashcards"
            estimated_minutes: 30
            due_offset: "+0d"
            priority: "normal"
  
  # ============ WEEK 2 ============
  - week_number: 2
    title: "Blood Patterns"
    unlock_condition: "week_1_complete"
    unlock_score_required: 75
    description: "Exploring Blood Deficiency and Blood Stasis patterns"
    
    days:
      - day_number: 1
        title: "Blood Deficiency: Overview"
        materials:
          - type: "study"
            source: "TCM_Patterns/Blood_Deficiency.md"
            title: "Blood Deficiency Pattern"
            estimated_minutes: 60
        tasks:
          - type: "study"
            estimated_minutes: 60
            due_offset: "+0d"
            priority: "high"
      
      # More days...
  
  # ============ WEEK 3-12 ============
  # Similar structure for remaining weeks...
```

---

## 🎯 Common Patterns

### Week 1 Pattern (Always Unlocked)
```yaml
- week_number: 1
  title: "Introduction"
  unlock_condition: "class_start"
  days:
    # ... days
```

### Sequential Week Pattern
```yaml
- week_number: 2
  title: "Week 2 Content"
  unlock_condition: "week_1_complete"
  unlock_score_required: 75
  days:
    # ... days
```

### Date-Based Unlock
```yaml
- week_number: 3
  title: "Week 3 Content"
  unlock_condition: "date_2025-12-01"
  days:
    # ... days
```

---

### Study Day Pattern
```yaml
- day_number: 1
  title: "New Topic"
  materials:
    - type: "study"
      source: "path/to/material.md"
      title: "Topic Name"
      estimated_minutes: 60
    - type: "flashcards"
      source: "path/to/flashcards.md"
      title: "Topic Flashcards"
      count: 20
      estimated_minutes: 20
  tasks:
    - type: "study"
      estimated_minutes: 60
      due_offset: "+0d"
      priority: "high"
    - type: "flashcards"
      estimated_minutes: 20
      due_offset: "+0d"
      priority: "normal"
```

### Quiz Day Pattern
```yaml
- day_number: 5
  title: "Week Assessment"
  materials:
    - type: "quiz"
      title: "Week 1 Quiz"
      questions: 15
      passing_score: 11
      estimated_minutes: 20
  tasks:
    - type: "quiz"
      estimated_minutes: 20
      due_offset: "+0d"
      priority: "high"
```

### Review Day Pattern
```yaml
- day_number: 7
  title: "Weekly Review"
  materials:
    - type: "flashcards"
      source: "path/to/flashcards.md"
      title: "Week Review"
      count: 50
      estimated_minutes: 40
  tasks:
    - type: "flashcards"
      estimated_minutes: 40
      due_offset: "+0d"
      priority: "normal"
```

---

## ✅ Validation Rules

```python
def validate_timeline(timeline):
    """Validate timeline structure."""
    
    # Check weeks exist
    if 'weeks' not in timeline or not timeline['weeks']:
        raise ValueError("Timeline must have at least one week")
    
    # Check week numbers are sequential
    week_numbers = [w['week_number'] for w in timeline['weeks']]
    if week_numbers != list(range(1, len(week_numbers) + 1)):
        raise ValueError("Week numbers must be sequential starting from 1")
    
    # Validate each week
    for week in timeline['weeks']:
        # Required fields
        if 'week_number' not in week:
            raise ValueError("Week missing week_number")
        if 'unlock_condition' not in week:
            raise ValueError(f"Week {week['week_number']} missing unlock_condition")
        if 'days' not in week or not week['days']:
            raise ValueError(f"Week {week['week_number']} must have at least one day")
        
        # Validate unlock condition
        valid_conditions = ['class_start', 'score_threshold']
        if not (week['unlock_condition'] in valid_conditions or 
                week['unlock_condition'].startswith('week_') or
                week['unlock_condition'].startswith('date_')):
            raise ValueError(f"Invalid unlock_condition: {week['unlock_condition']}")
        
        # If score_threshold, must have unlock_score_required
        if week['unlock_condition'] == 'score_threshold':
            if 'unlock_score_required' not in week:
                raise ValueError(f"Week {week['week_number']} needs unlock_score_required")
        
        # Validate days
        day_numbers = [d['day_number'] for d in week['days']]
        if day_numbers != list(range(1, len(day_numbers) + 1)):
            raise ValueError(f"Week {week['week_number']} day numbers must be sequential")
        
        # Validate each day
        for day in week['days']:
            if 'materials' not in day or not day['materials']:
                raise ValueError(f"Week {week['week_number']} Day {day['day_number']} needs materials")
            
            # Validate materials
            for material in day['materials']:
                if 'type' not in material:
                    raise ValueError("Material missing type")
                if 'title' not in material:
                    raise ValueError("Material missing title")
                
                # Type-specific validation
                if material['type'] in ['study', 'flashcards', 'slides']:
                    if 'source' not in material:
                        raise ValueError(f"{material['type']} material needs source")
                
                if material['type'] == 'flashcards':
                    if 'count' not in material:
                        raise ValueError("Flashcard material needs count")
                
                if material['type'] == 'quiz':
                    if 'questions' not in material:
                        raise ValueError("Quiz material needs questions")
                    if 'passing_score' not in material:
                        raise ValueError("Quiz material needs passing_score")
    
    return True
```

---

## 💡 Best Practices

### Week Organization
- **Week 1:** Always `unlock_condition: "class_start"`
- **Progressive:** Each week builds on previous
- **Review days:** Include periodic review (Day 7)
- **Assessments:** Quiz at end of week

### Day Structure
- **Consistent timing:** Similar daily workload
- **Variety:** Mix study, flashcards, quizzes
- **Reasonable:** 60-90 minutes total per day
- **Flexibility:** Some days lighter for catch-up

### Material Sequencing
- **Study first:** Reading before flashcards
- **Practice:** Flashcards after study
- **Assessment:** Quiz after practice
- **Homework:** Longer assignments span multiple days

### Task Timing
- **Study:** Due same day (`+0d`)
- **Flashcards:** Due same day (`+0d`)
- **Quizzes:** Due next day (`+1d`) - allows review time
- **Homework:** Due 3-7 days (`+3d` to `+7d`)

---

## 🔄 Timeline Generation

### From Template

```python
def generate_timeline(class_config):
    """Generate timeline from class configuration."""
    timeline = {'weeks': []}
    
    for week_num in range(1, class_config['duration_weeks'] + 1):
        week = {
            'week_number': week_num,
            'title': f"Week {week_num}",
            'unlock_condition': 'class_start' if week_num == 1 else f'week_{week_num-1}_complete',
            'days': []
        }
        
        if week_num > 1:
            week['unlock_score_required'] = class_config.get('unlock_threshold', 75)
        
        # Generate days
        for day_num in range(1, class_config.get('duration_days_per_week', 7) + 1):
            day = {
                'day_number': day_num,
                'title': f"Day {day_num}",
                'materials': [],
                'tasks': []
            }
            week['days'].append(day)
        
        timeline['weeks'].append(week)
    
    return timeline
```

---

## 📚 Related Documentation

- **Class Manifest:** `Class_Manifest_Schema.md`
- **Material Templates:** `../05_Material_Templates/`
- **Task Generation:** `../06_Automation_Scripts/generate_tasks.py.md`

---

**Structure your class timeline for optimal learning! 📅**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
