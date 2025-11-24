# Progress Dashboard

**Purpose:** Student-facing dashboard design and implementation

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

The Progress Dashboard is the **student's command center** for tracking their learning journey. It displays grades, progress, upcoming tasks, and provides quick access to materials.

---

## 🎯 Dashboard Components

### 1. Header Section

```markdown
# TCM 101 - Progress Dashboard

**Student:** John Doe  
**Enrolled:** January 1, 2025  
**Current Week:** 5 of 12  
**Overall Grade:** 88.7% (B+)  
**Last Updated:** `VIEW{date:YYYY-MM-DD HH:mm}`
```

---

### 2. Grade Summary

```markdown
## 📊 Grade Summary

| Component | Weight | Score | Weighted | Status |
|-----------|--------|-------|----------|--------|
| Quizzes | 40% | 85% | 34.0% | ✅ On Track |
| Flashcards | 30% | 92% | 27.6% | ✅ Excellent |
| Homework | 20% | 88% | 17.6% | ✅ Good |
| Tasks | 10% | 95% | 9.5% | ✅ Excellent |
| **TOTAL** | **100%** | | **88.7%** | **B+** |

```meta-bind
INPUT[progressBar(
  minValue(0),
  maxValue(100),
  value(overall_grade)
)]
```
```

---

### 3. Weekly Progress

```markdown
## 📅 Weekly Progress

```dataview
TABLE
  week as "Week",
  title as "Topic",
  quiz_score as "Quiz",
  homework_score as "HW",
  completion as "Complete",
  status as "Status"
FROM "Classes/TCM_101/Materials"
WHERE ocds_type = "week"
SORT week ASC
```
```

---

### 4. Current Week Tasks

```markdown
## ✅ Week 5 Tasks

**Due:** January 29, 2025

```dataview
TASK
FROM "Classes/TCM_101/Materials/Week_05"
WHERE !completed
```

**Progress:** `VIEW{completed_tasks}` / `VIEW{total_tasks}` (`VIEW{task_completion}`%)
```

---

### 5. Upcoming Deadlines

```markdown
## 📆 Upcoming Deadlines

```dataview
TABLE
  title as "Assignment",
  due_date as "Due",
  days_until_due as "Days Left",
  status as "Status"
FROM "Classes/TCM_101/Materials"
WHERE due_date >= date(today) AND status != "completed"
SORT due_date ASC
LIMIT 5
```
```

---

### 6. Recent Activity

```markdown
## 📈 Recent Activity

```dataview
TABLE
  material_title as "Activity",
  score as "Score",
  completed_date as "Date"
FROM "Classes/TCM_101/Materials"
WHERE completed_date != null
SORT completed_date DESC
LIMIT 10
```
```

---

### 7. Quick Actions

```markdown
## 🚀 Quick Actions

```meta-bind-button
label: Start Week 5 Materials
style: primary
action:
  type: open
  link: "[[Classes/TCM_101/Materials/Week_05/Study_Material]]"
```

```meta-bind-button
label: Review Flashcards
style: default
action:
  type: open
  link: "[[Classes/TCM_101/Materials/Week_05/Flashcards]]"
```

```meta-bind-button
label: View Full Class Calendar
style: default
action:
  type: open
  link: "[[Classes/TCM_101/Class_Calendar]]"
```
```

---

## 📊 Complete Dashboard Example

```markdown
---
ocds_type: dashboard
class_id: TCM_101
student_id: john_doe
last_updated: 2025-01-25 14:30:00
---

# TCM 101 - Progress Dashboard

**Student:** John Doe  
**Enrolled:** January 1, 2025  
**Current Week:** 5 of 12  
**Overall Grade:** 88.7% (B+)

---

## 📊 Grade Summary

| Component | Weight | Score | Weighted | Trend |
|-----------|--------|-------|----------|-------|
| Quizzes | 40% | 85% | 34.0% | ↗️ +3% |
| Flashcards | 30% | 92% | 27.6% | ➡️ Stable |
| Homework | 20% | 88% | 17.6% | ↗️ +5% |
| Tasks | 10% | 95% | 9.5% | ➡️ Stable |
| **TOTAL** | **100%** | | **88.7%** | **↗️ +2%** |

**Letter Grade:** B+

```meta-bind
INPUT[progressBar(
  minValue(0),
  maxValue(100),
  value(88.7),
  label("Overall Progress")
)]
```

---

## 📅 Weekly Progress

| Week | Topic | Quiz | HW | Tasks | Status |
|------|-------|------|----|----|--------|
| 1 | Tongue Diagnosis | 90% | 90% | 100% | ✅ Complete |
| 2 | Pulse Diagnosis | 85% | 85% | 100% | ✅ Complete |
| 3 | Pattern Differentiation | 80% | 90% | 100% | ✅ Complete |
| 4 | Treatment Principles | 85% | 88% | 95% | ✅ Complete |
| 5 | Point Selection | 85% | - | 60% | 🔄 In Progress |
| 6 | Formula Selection | - | - | - | 🔒 Locked |

---

## ✅ Week 5 Tasks

**Due:** January 29, 2025 (4 days)

- [x] Read Week 5 Study Material
- [x] Review Week 5 Flashcards (20 cards)
- [x] Watch Week 5 Lecture Slides
- [ ] Complete Week 5 Quiz
- [ ] Submit Week 5 Homework

**Progress:** 3 / 5 tasks (60%)

---

## 📆 Upcoming Deadlines

| Assignment | Due | Days Left | Status |
|------------|-----|-----------|--------|
| Week 5 Quiz | Jan 27 | 2 | Not Started |
| Week 5 Homework | Jan 29 | 4 | Not Started |
| Week 6 Quiz | Feb 3 | 9 | Locked |

---

## 📈 Grade Trend

```dataviewjs
const weeks = [1, 2, 3, 4, 5];
const scores = [90, 87, 85, 87, 88];

dv.paragraph("**5-Week Grade Trend:**");
for (let i = 0; i < weeks.length; i++) {
  const bar = '█'.repeat(scores[i] / 2);
  dv.paragraph(`Week ${weeks[i]}: ${bar} ${scores[i]}%`);
}
```
> I like bars and graphs and stuff. want to have more radial or star graphs too. those are dope. like the pokemon stat star
---

## 🎯 Performance Insights

**Strengths:**
- ✅ Excellent task completion (95% average)
- ✅ Strong flashcard engagement (92%)
- ✅ Consistent improvement trend

**Areas for Growth:**
- ⚠️ Quiz scores slightly below target (85% vs 90% goal)
- 💡 Tip: Review flashcards before quizzes

**Recommendations:**
- Continue current study habits
- Spend 10 more minutes on quiz review
- Aim for 90%+ on Week 5 quiz

---

## 🚀 Quick Actions

```meta-bind-button
label: Start Week 5 Quiz
style: primary
action:
  type: open
  link: "[[Classes/TCM_101/Materials/Week_05/Quiz]]"
```

```meta-bind-button
label: Review Flashcards
style: default
action:
  type: open
  link: "[[Classes/TCM_101/Materials/Week_05/Flashcards]]"
```

```meta-bind-button
label: View Class Calendar
style: default
action:
  type: open
  link: "[[Classes/TCM_101/Class_Calendar]]"
```
---

## 📚 Resources

- [[Class Syllabus]]
- [[Office Hours Schedule]]
- [[Discussion Forum]]
- [[Study Group Info]]

---

*Dashboard auto-updates as you complete materials*
```

---

## 🎨 Dashboard Customization

### Theme Options

```yaml
# dashboard_config.yaml
theme:
  primary_color: "#4CAF50"
  accent_color: "#2196F3"
  warning_color: "#FF9800"
  danger_color: "#F44336"
  
layout:
  show_grade_summary: true
  show_weekly_progress: true
  show_tasks: true
  show_deadlines: true
  show_recent_activity: true
  show_insights: true
  
widgets:
  - type: grade_summary
    position: top
  - type: weekly_progress
    position: middle
  - type: current_tasks
    position: sidebar
```
>So how can we make the dashboards universal? should there be a dashboard for each class and a universal dashboard? that would be easy to do.
---

## 📚 Related Documentation

- [[Instructor_Dashboard.md]] - Instructor view
- [[Dataview_Queries.md]] - Query examples
- [[Meta_Bind_Components.md]] - Interactive elements
- [[Grade_Reports.md]] - Grade reporting

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
