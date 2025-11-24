# Spaced Repetition Plugin - OCDS Integration Guide

**Complete guide to using Spaced Repetition for OCDS flashcards**

---

## 📚 Overview

The Spaced Repetition plugin implements an SRS (Spaced Repetition System) algorithm to optimize long-term memory retention. OCDS uses it for:
- Daily flashcard review sessions
- Progress tracking (cards studied per day)
- Retention statistics
- Grading component (flashcard completion counts toward grade)

**Plugin:** https://github.com/st3v3nmw/obsidian-spaced-repetition  
**Docs:** https://www.stephenmwangi.com/obsidian-spaced-repetition/

---

## 🎴 Flashcard Formats

### Single-Line Format (Basic)

```markdown
Question text? :: Answer text
```

**Example:**
```markdown
What is the primary tongue presentation for Qi Deficiency? :: Pale, swollen with tooth marks
```

---

### Multi-Line Format (OCDS Standard)

```markdown
# Context Header
## Question
?
Answer content
<!--SR:!2025-11-10,3,250-->
```

**Example:**
```markdown
# BL-23 · SHÈNSHŪ (肾俞) · *Kidney Shu*
## What is the location and special properties?
?
**Location:** 1.5 cun lateral to the lower border of the spinous process of L2

**Special Properties:**
- Back-Shu point of the Kidney
- Tonifies Kidney Qi and Yang
- Benefits the lower back

<!--SR:!2025-11-10,3,250-->
```

---

## 🔧 OCDS Flashcard Structure

### Standard Template

All OCDS flashcards follow this structure:

```markdown
---
tags:
  - flashcards
  - {{CLASS_ID}}
  - week_{{WEEK_NUMBER}}
  - {{TOPIC}}
type: flashcard
class_id: "{{CLASS_ID}}"
topic: "{{TOPIC_NAME}}"
difficulty: "{{easy|medium|hard}}"
---

# {{CONTEXT_HEADER}}
## {{QUESTION}}
?
{{ANSWER}}
<!--SR:!{{NEXT_DATE}},{{INTERVAL}},{{EASE}}-->
```

### Frontmatter Fields

| Field | Purpose | Example |
|-------|---------|---------|
| `tags` | Categorization, filtering | `[flashcards, tcm_101, week_1, patterns]` |
| `type` | File type identifier | `flashcard` |
| `class_id` | Which class this belongs to | `TCM_101` |
| `topic` | Subject matter | `Qi Deficiency Pattern` |
| `difficulty` | Card difficulty level | `easy`, `medium`, `hard` |

### Scheduling Comment

The `<!--SR:...-->` comment stores scheduling data:

```markdown
<!--SR:!2025-11-10,3,250-->
```

- `!2025-11-10` - Next review date
- `3` - Current interval (days)
- `250` - Ease factor (percentage)

**Do not edit this manually!** The plugin updates it automatically.

---

## 📖 Review Process

### Starting a Review Session

1. **Open Command Palette** (Ctrl/Cmd + P)
2. **Type:** "Spaced Repetition: Review flashcards"
3. **Select** the command
4. **Review mode opens** with first due card

### Rating Cards

For each card, choose one of four ratings:

| Rating | Meaning | Effect |
|--------|---------|--------|
| **Again** | Didn't remember | Reset to 1 day, decrease ease |
| **Hard** | Struggled to remember | 1.2x interval, slight ease decrease |
| **Good** | Remembered correctly | 2.5x interval, maintain ease |
| **Easy** | Remembered easily | 4x interval, increase ease |

### Keyboard Shortcuts

- `1` or `Z` - Again
- `2` or `X` - Hard
- `3` or `Space` - Good
- `4` or `C` - Easy
- `S` - Show answer (if hidden)
- `Esc` - Exit review

---

## 🎯 OCDS Integration

### Daily Flashcard Tasks

OCDS generates daily tasks for flashcard review:

```markdown
---
status: pending
due: 2025-11-10
tags:
  - task
  - tcm_101
  - flashcards
estimated_minutes: 20
---

# Week 1 Day 1: Review Flashcards

## Task Details
- **Topic:** Qi Deficiency Pattern
- **Cards to review:** ~20 cards
- **Estimated time:** 20 minutes

## Instructions
1. Open Spaced Repetition review
2. Review all due cards
3. Rate each card honestly
4. Mark this task complete when done

## Materials
- [[Flashcards_Patterns_Qi.md]]
```

### Progress Tracking

OCDS tracks your flashcard activity:

```yaml
# student_progress.yaml
flashcard_stats:
  total_cards_studied: 150
  cards_due_today: 20
  cards_mastered: 45
  average_ease: 265
  retention_rate: 87.5
  study_streak_days: 12
```

### Grading Component

Flashcards contribute to your overall grade:

```python
# Default grading weights
grading_weights:
  quizzes: 0.4          # 40%
  flashcards: 0.3       # 30%
  homework: 0.2         # 20%
  pomodoros: 0.1        # 10%

# Flashcard score calculation
flashcard_score = (cards_studied / cards_assigned) * 100
```

---

## 📊 Statistics & Analytics

### View Your Stats

1. **Open Command Palette** (Ctrl/Cmd + P)
2. **Type:** "Spaced Repetition: View statistics"
3. **See:**
   - Cards due today
   - Cards studied
   - Retention rate
   - Forecast (upcoming reviews)

### OCDS Dashboard Integration

Your progress dashboard shows flashcard stats:

```dataview
TABLE
  flashcard_stats.cards_due_today as "Due Today",
  flashcard_stats.cards_mastered as "Mastered",
  flashcard_stats.retention_rate as "Retention %",
  flashcard_stats.study_streak_days as "Streak"
FROM "Student_Progress"
WHERE type = "progress"
```

---

## 🔍 Filtering & Organization

### Study by Tag

Review specific topics:

```markdown
#flashcards/patterns
#flashcards/herbs
#flashcards/formulas
#flashcards/points
```

### Study by Class

Review only current class:

```markdown
#tcm_101
#tcm_201
```

### Study by Week

Review specific week's material:

```markdown
#week_1
#week_2
```

### Study by Difficulty

Focus on challenging cards:

```markdown
#difficulty/hard
#difficulty/medium
#difficulty/easy
```

---

## 🎨 Customization

### Plugin Settings

Recommended OCDS settings:

```
Settings → Spaced Repetition
├── Flashcard separator: "?"
├── Multiline card separator: "?"
├── Multiline card reverse separator: "??"
├── Show context in cards: ON
├── Bury sibling cards: ON
├── Show card's note: ON
├── Randomize card order: ON
├── Convert folders to decks: OFF
└── Tags to review: "#flashcards"
```

### Algorithm Settings

```
Algorithm Settings
├── Base ease: 250
├── Lapse multiplier: 0.5
├── Easy bonus: 1.3
├── Maximum interval: 36500 days
└── Maximum link contribution: 100
```

---

## 📝 Creating OCDS Flashcards

### From Question Banks

OCDS generates flashcards from question banks:

```python
# generate_flashcards.py
def create_flashcard(question_data):
    """Generate flashcard from question bank entry."""
    return f"""# {question_data['topic']}
## {question_data['question']}
?
{question_data['answer']}

**Explanation:** {question_data['explanation']}
<!--SR:!2025-11-10,3,250-->
"""
```

### Manual Creation

Create flashcards manually:

1. **Create new note** in flashcard folder
2. **Add frontmatter** with tags
3. **Write question** after `##`
4. **Add separator** `?`
5. **Write answer** below separator
6. **Save** - plugin will add scheduling comment

---

## 🚀 Best Practices

### Daily Review

- **Review every day** for best retention
- **Morning is best** - fresh mind
- **20-30 minutes** per session
- **Don't skip days** - breaks the algorithm

### Rating Honestly

- **Be honest** with ratings
- **Again** if you didn't know it
- **Hard** if you struggled
- **Good** if you remembered
- **Easy** if it was trivial

### Card Quality

- **One concept** per card
- **Clear questions** - no ambiguity
- **Concise answers** - key points only
- **Add context** in header
- **Include explanations** when helpful

### Organization

- **Use tags** consistently
- **Group by topic** in folders
- **Link related cards** with wikilinks
- **Review stats** weekly

---

## 🐛 Troubleshooting

### Cards Not Appearing in Review

**Problem:** No cards show up when starting review

**Solutions:**
1. Check cards have `#flashcards` tag
2. Verify cards are due (check scheduling comment)
3. Ensure plugin is enabled
4. Refresh vault (Ctrl/Cmd + R)

### Scheduling Comment Missing

**Problem:** Cards don't have `<!--SR:...-->` comment

**Solutions:**
1. Review the card once - plugin adds comment
2. Manually add: `<!--SR:!2025-11-10,3,250-->`
3. Check plugin settings are correct

### Cards Reviewing Too Often/Rarely

**Problem:** Interval seems wrong

**Solutions:**
1. Check algorithm settings (base ease, multipliers)
2. Rate cards honestly (affects future intervals)
3. Reset card if needed (delete scheduling comment)

### Stats Not Updating

**Problem:** Statistics don't reflect recent reviews

**Solutions:**
1. Close and reopen stats view
2. Restart Obsidian
3. Check for plugin updates

---

## 📈 Advanced Features

### Cloze Deletions

Hide specific words in flashcards:

```markdown
The primary formula for Qi Deficiency is ==Si Jun Zi Tang==.
```

### Image Occlusion

Hide parts of images:

```markdown
![[tongue_diagram.png]]
<!-- Use image occlusion plugin for this -->
```

### Audio Cards

Include pronunciation:

```markdown
## How do you pronounce this point?
?
Shènshū (肾俞)
![[shen_shu_pronunciation.mp3]]
```

---

## 🔗 Integration with Other OCDS Components

### With TaskNotes

```markdown
---
status: pending
due: 2025-11-10
---

# Daily Flashcard Review

Complete today's flashcard review session.

**Cards due:** `VIEW[{flashcard_stats.cards_due_today}][text]`

```meta-bind-button
label: Start Review
action:
  type: command
  command: spaced-repetition:review-flashcards
```
```

### With Grading System

```python
# auto_grader.py
def calculate_flashcard_score(student_id, week):
    """Calculate flashcard component of grade."""
    assigned = get_assigned_cards(student_id, week)
    studied = get_studied_cards(student_id, week)
    return (studied / assigned) * 100
```

### With Progress Dashboard

```dataview
TABLE
  date as "Date",
  cards_studied as "Cards",
  retention as "Retention %"
FROM "Student_Progress/Flashcard_Log"
WHERE student_id = "{{STUDENT_ID}}"
SORT date DESC
LIMIT 7
```

---

## 📚 Example Flashcard Sets

### Pattern Flashcards

```markdown
---
tags: [flashcards, tcm_101, patterns, qi_deficiency]
type: flashcard
class_id: "TCM_101"
topic: "Qi Deficiency"
---

# Qi Deficiency Pattern
## What are the cardinal symptoms?
?
- Fatigue and weakness
- Shortness of breath
- Spontaneous sweating
- Pale complexion
- Weak voice

**Tongue:** Pale, swollen with tooth marks
**Pulse:** Weak, especially in Guan position
<!--SR:!2025-11-10,3,250-->
```

### Formula Flashcards

```markdown
---
tags: [flashcards, tcm_101, formulas, qi_tonics]
type: flashcard
class_id: "TCM_101"
topic: "Si Jun Zi Tang"
---

# Si Jun Zi Tang (Four Gentlemen Decoction)
## What is the composition and dosage?
?
**Chief:**
- Ren Shen (9g) - Tonify Qi

**Deputy:**
- Bai Zhu (9g) - Strengthen Spleen

**Assistant:**
- Fu Ling (9g) - Drain Dampness

**Envoy:**
- Zhi Gan Cao (6g) - Harmonize
<!--SR:!2025-11-10,3,250-->
```

---

## ✅ Quick Reference

### Flashcard Syntax
```markdown
# Context
## Question
?
Answer
<!--SR:!DATE,INTERVAL,EASE-->
```

### Ratings
- `1` / `Z` - Again (forgot)
- `2` / `X` - Hard (struggled)
- `3` / `Space` - Good (remembered)
- `4` / `C` - Easy (trivial)

### Commands
- Review flashcards: `Ctrl/Cmd + P` → "Spaced Repetition: Review"
- View stats: `Ctrl/Cmd + P` → "Spaced Repetition: Statistics"

### Tags
- `#flashcards` - Required for all cards
- `#{{class_id}}` - Filter by class
- `#week_{{n}}` - Filter by week
- `#{{topic}}` - Filter by topic

---

**Master your material with spaced repetition! 🧠**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
