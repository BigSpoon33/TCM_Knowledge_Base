# Obsidian Pomodoro - OCDS Integration Guide

**Complete guide to using Pomodoro timer for OCDS time tracking**

---

## 📚 Overview

The Obsidian Pomodoro plugin implements the Pomodoro Technique for focused study sessions. OCDS uses it for:
- Time tracking
- Study session management
- Break enforcement
- Progress metrics
- Grading component (optional)

**Plugin:** Search "Obsidian Pomodoro" in Community Plugins  
**Technique:** https://en.wikipedia.org/wiki/Pomodoro_Technique

---

## 🎯 Why Pomodoro for OCDS?

### The Pomodoro Technique

1. **Work for 25 minutes** (1 Pomodoro)
2. **Take 5-minute break**
3. **Repeat 4 times**
4. **Take longer break** (15-30 minutes)

### Benefits for Students

- **Focused study** - Eliminates distractions
- **Regular breaks** - Prevents burnout
- **Time awareness** - Understand study habits
- **Measurable progress** - Track sessions completed
- **Improved retention** - Spaced practice

### OCDS Integration

- **Track study time** - Log actual minutes
- **Grading component** - Pomodoros count toward grade
- **Progress metrics** - Sessions per week/day
- **Motivation** - Gamification element

---

## ⚙️ Plugin Setup

### Installation

1. Settings → Community Plugins
2. Browse → Search "Obsidian Pomodoro"
3. Install and Enable

### Recommended Configuration

```
Settings → Obsidian Pomodoro
├── Pomodoro duration: 25 minutes
├── Short break: 5 minutes
├── Long break: 15 minutes
├── Long break interval: 4 pomodoros
├── Auto-start breaks: OFF (manual control)
├── Auto-start pomodoros: OFF
├── Show notifications: ON
├── Play sound: ON (optional)
└── Log completed pomodoros: ON
```

---

## 🍅 Using the Timer

### Starting a Session

1. **Open Pomodoro panel** (ribbon icon or command)
2. **Click "Start"**
3. **Focus on task** for 25 minutes
4. **Take break** when timer ends
5. **Repeat**

### Keyboard Shortcuts

Set custom hotkeys in Settings → Hotkeys:
- Start/Pause timer
- Skip break
- Reset timer

### Status Bar

Timer shows in status bar:
- `🍅 24:35` - Time remaining
- `☕ 4:12` - Break time remaining

---

## 📊 OCDS Time Tracking

### Logging Pomodoros

When a Pomodoro completes, log it:

```yaml
# In task note frontmatter
pomodoros_completed: 3
actual_minutes: 75  # 3 × 25 minutes
```

### Manual Logging

```markdown
## Time Log

**Session 1:** 2 Pomodoros (50 min)
**Session 2:** 3 Pomodoros (75 min)
**Total:** 5 Pomodoros (125 min)
```

---

## 🎓 OCDS Integration Patterns

### 1. Task Note with Pomodoro Tracking

```markdown
---
status: in_progress
estimated_minutes: 60
actual_minutes: 0
pomodoros_planned: 3
pomodoros_completed: 0
---

# Week 1 Day 1: Study Task

## Time Tracking

**Estimated:** 60 minutes (3 Pomodoros)
**Actual:** `VIEW[{actual_minutes}][text]` minutes
**Pomodoros:** `VIEW[{pomodoros_completed}][text]` / `VIEW[{pomodoros_planned}][text]`

## Pomodoro Log

### Session 1
- Start: 14:00
- End: 14:25
- Status: ✅ Completed

### Session 2
- Start: 14:30
- End: 14:55
- Status: ✅ Completed

### Session 3
- Start: 15:00
- End: 15:25
- Status: ✅ Completed

**Total:** 3 Pomodoros (75 minutes)
```

---

### 2. Daily Study Log

```markdown
---
date: 2025-11-05
total_pomodoros: 0
total_minutes: 0
---

# Daily Study Log - <%= tp.date.now("YYYY-MM-DD") %>

## Pomodoro Sessions

| Time | Task | Pomodoros | Status |
|------|------|-----------|--------|
| 09:00 | Study Qi Deficiency | 2 | ✅ |
| 10:00 | Review Flashcards | 1 | ✅ |
| 14:00 | Complete Quiz | 1 | ✅ |
| 15:00 | Homework | 3 | ✅ |

**Total:** 7 Pomodoros (175 minutes)

## Notes

- Morning sessions most productive
- Needed extra break after 4th Pomodoro
- Quiz took less time than estimated
```

---

### 3. Weekly Time Summary

```markdown
# Week 1 Time Summary

\```dataview
TABLE
  date as "Date",
  pomodoros_completed as "Pomodoros",
  actual_minutes as "Minutes"
FROM "TaskNotes/TCM_101"
WHERE week = 1
  AND pomodoros_completed > 0
SORT date ASC
\```

**Total Pomodoros:** `= sum(this.pomodoros_completed)`
**Total Minutes:** `= sum(this.actual_minutes)`
**Average per Day:** `= round(sum(this.actual_minutes) / 7, 1)` minutes
```

---

### 4. Progress Dashboard Integration

```markdown
## Time Tracking

**This Week:**
- Pomodoros: `VIEW[{week_pomodoros}][text]`
- Study Time: `VIEW[{week_minutes}][text]` minutes
- Average/Day: `VIEW[{avg_daily_minutes}][text]` minutes

**This Month:**
- Total Pomodoros: `VIEW[{month_pomodoros}][text]`
- Total Time: `VIEW[{month_hours}][text]` hours

\```dataview
TABLE
  week as "Week",
  sum(rows.pomodoros_completed) as "Pomodoros",
  sum(rows.actual_minutes) as "Minutes"
FROM "TaskNotes/TCM_101"
WHERE pomodoros_completed > 0
GROUP BY week
SORT week ASC
\```
```

---

## 📈 Grading Integration

### Pomodoro Score Calculation

```python
def calculate_pomodoro_score(student_id, week):
    """Calculate Pomodoro component of grade."""
    
    # Get completed pomodoros
    completed = get_pomodoros_completed(student_id, week)
    
    # Get target (from timeline)
    target = get_target_pomodoros(week)
    
    # Calculate score (capped at 100%)
    score = min((completed / target) * 100, 100)
    
    return score

# Example:
# Target: 20 Pomodoros per week
# Completed: 18 Pomodoros
# Score: (18 / 20) * 100 = 90%
```

### Grading Weight

```yaml
# grading_config.yaml
grading_weights:
  quizzes: 0.4      # 40%
  flashcards: 0.3   # 30%
  homework: 0.2     # 20%
  pomodoros: 0.1    # 10%
```

### Weekly Targets

```yaml
# timeline.yaml
weeks:
  - week_number: 1
    pomodoro_target: 20  # 20 Pomodoros (500 min)
    days:
      - day_number: 1
        pomodoro_target: 3  # 3 Pomodoros (75 min)
```

---

## 💡 Study Strategies

### Effective Pomodoro Use

**Do:**
- ✅ Eliminate distractions before starting
- ✅ Have materials ready
- ✅ Take breaks seriously
- ✅ Track what you accomplish
- ✅ Adjust length if needed

**Don't:**
- ❌ Skip breaks
- ❌ Check phone during session
- ❌ Start without clear goal
- ❌ Work through fatigue
- ❌ Multitask

### Task Breakdown

**Large task (3+ hours):**
```
Study Chapter → 6 Pomodoros
├── Read (3 Pomodoros)
├── Notes (2 Pomodoros)
└── Review (1 Pomodoro)
```

**Medium task (1-2 hours):**
```
Complete Quiz → 2-3 Pomodoros
├── Review material (1 Pomodoro)
├── Take quiz (1 Pomodoro)
└── Review answers (1 Pomodoro)
```

**Small task (<1 hour):**
```
Flashcard Review → 1-2 Pomodoros
```

---

## 📊 Analytics & Insights

### Personal Metrics

Track these over time:
- **Pomodoros per day** - Consistency
- **Best time of day** - Peak productivity
- **Task completion rate** - Estimation accuracy
- **Break adherence** - Self-care
- **Weekly trends** - Progress over time

### Dataview Queries

**Daily average:**
```dataview
TABLE WITHOUT ID
  "Average Pomodoros/Day" as "Metric",
  round(sum(rows.pomodoros_completed) / count(rows), 1) as "Value"
FROM "TaskNotes"
WHERE pomodoros_completed > 0
  AND contains(tags, "tcm_101")
```

**Most productive day:**
```dataview
TABLE
  date as "Date",
  pomodoros_completed as "Pomodoros"
FROM "TaskNotes"
WHERE pomodoros_completed > 0
SORT pomodoros_completed DESC
LIMIT 1
```

**Weekly trend:**
```dataview
TABLE
  week as "Week",
  sum(rows.pomodoros_completed) as "Total Pomodoros",
  round(avg(rows.pomodoros_completed), 1) as "Avg/Day"
FROM "TaskNotes"
WHERE contains(tags, "tcm_101")
GROUP BY week
SORT week ASC
```

---

## 🎯 OCDS Workflow

### Daily Routine

**Morning (9:00 AM):**
1. Review today's tasks
2. Estimate Pomodoros needed
3. Plan study sessions

**Study Session:**
1. Choose task
2. Start Pomodoro timer
3. Focus for 25 minutes
4. Take 5-minute break
5. Log completed Pomodoro
6. Repeat

**Evening (6:00 PM):**
1. Review completed Pomodoros
2. Update task frontmatter
3. Plan tomorrow

---

### Weekly Review

**Sunday evening:**
1. Count total Pomodoros
2. Calculate study time
3. Compare to target
4. Identify patterns
5. Adjust next week

---

## 🔧 Customization

### Adjust Duration

Some students prefer:
- **Shorter:** 15-20 minutes (for difficult material)
- **Longer:** 30-45 minutes (for flow state)
- **Variable:** Adjust by task type

### Break Variations

- **Active breaks:** Stretch, walk
- **Passive breaks:** Rest, breathe
- **Social breaks:** Chat with classmate
- **Reward breaks:** Snack, music

---

## 📱 Mobile Integration

### Obsidian Mobile

Pomodoro plugin works on mobile:
- Start timer on phone
- Study anywhere
- Sync logs to vault

### External Apps

Can use external Pomodoro apps:
- Log sessions manually
- Update task notes
- Maintain consistency

---

## 🎮 Gamification

### Achievements

Create personal milestones:
- 🥉 **Bronze:** 50 Pomodoros
- 🥈 **Silver:** 100 Pomodoros
- 🥇 **Gold:** 250 Pomodoros
- 💎 **Diamond:** 500 Pomodoros

### Streaks

Track consecutive days:
- 7-day streak: 🔥
- 14-day streak: 🔥🔥
- 30-day streak: 🔥🔥🔥

### Leaderboards

Compare with classmates (optional):
```dataview
TABLE
  student_name as "Student",
  sum(rows.pomodoros_completed) as "Total Pomodoros"
FROM "Student_Progress"
WHERE class_id = "TCM_101"
GROUP BY student_name
SORT sum(rows.pomodoros_completed) DESC
```

---

## 💡 Best Practices

### Time Management
- **Morning sessions** - Most productive
- **Consistent schedule** - Same time daily
- **Realistic goals** - Don't overcommit
- **Buffer time** - Account for interruptions

### Focus Techniques
- **Single-tasking** - One thing at a time
- **Environment** - Quiet, organized space
- **Tools ready** - Materials prepared
- **Phone away** - Eliminate temptation

### Break Optimization
- **Move around** - Don't stay seated
- **Hydrate** - Drink water
- **Rest eyes** - Look away from screen
- **Mental reset** - Clear your mind

---

## 🐛 Troubleshooting

### Timer Not Starting

**Problem:** Can't start Pomodoro

**Solutions:**
1. Check plugin is enabled
2. Restart Obsidian
3. Check for conflicts with other plugins
4. Verify settings are correct

### Notifications Not Working

**Problem:** No alerts when timer ends

**Solutions:**
1. Enable notifications in plugin settings
2. Check OS notification permissions
3. Test with sound enabled
4. Verify Obsidian is in focus

### Time Not Logging

**Problem:** Completed Pomodoros not tracked

**Solutions:**
1. Manually log in task note
2. Use daily log template
3. Set up automatic logging
4. Create tracking system

---

## ✅ Quick Reference

### Timer Controls
- **Start:** Click start button or hotkey
- **Pause:** Click pause button
- **Skip:** Skip current session
- **Reset:** Reset timer to 25:00

### Logging Format
```yaml
pomodoros_completed: 3
actual_minutes: 75
```

### Target Setting
```yaml
pomodoro_target: 20  # per week
```

### Score Calculation
```
score = (completed / target) × 100
```

---

## 📚 Related Documentation

- **Grading System:** `../07_Grading_System/Activity_Tracking.md`
- **Task Template:** `../05_Material_Templates/Task_Template.md`
- **Progress Dashboard:** `../09_Dashboard_Design/Progress_Dashboard.md`

---

## 🎓 Study Tips

### For Different Material Types

**Reading (Study Material):**
- 2-3 Pomodoros per chapter
- Take notes during session
- Review notes during break

**Flashcards:**
- 1 Pomodoro = ~50 cards
- Focus on difficult cards
- Use breaks to rest eyes

**Quizzes:**
- 1 Pomodoro per 10 questions
- Review material first
- Check answers after

**Homework:**
- 3-6 Pomodoros for assignments
- Break into smaller tasks
- Take longer breaks

---

**Master your time with Pomodoro! 🍅**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
