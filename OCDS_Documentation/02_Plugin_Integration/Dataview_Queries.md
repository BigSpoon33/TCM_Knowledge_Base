# Dataview Plugin - OCDS Integration Guide

**Complete guide to using Dataview for OCDS queries and dashboards**

---

## 📚 Overview

Dataview treats your vault as a database, allowing you to query and display data from frontmatter and file content. OCDS uses it for:
- Progress dashboards
- Grade calculations
- Task summaries
- Material listings
- Statistics displays
- Dynamic reports

**Plugin:** https://github.com/blacksmithgu/obsidian-dataview  
**Docs:** https://blacksmithgu.github.io/obsidian-dataview/

---

## 🎯 Why Dataview for OCDS?

### Key Features
- **Query frontmatter** - Access all metadata
- **Multiple formats** - LIST, TABLE, TASK, CALENDAR
- **Filtering** - WHERE clauses
- **Sorting** - ORDER BY
- **Grouping** - GROUP BY
- **Calculations** - SUM, AVG, COUNT, etc.
- **JavaScript queries** - Advanced logic

### OCDS Use Cases
- **Student dashboards** - Overall progress
- **Grade reports** - Quiz scores, averages
- **Task lists** - Pending/completed tasks
- **Material indexes** - All study materials
- **Statistics** - Flashcards studied, time spent
- **Class rosters** - Student lists

---

## 📝 Query Types

### 1. LIST Query

**Display items as a list**

```dataview
LIST
FROM "folder"
WHERE condition
SORT field
```

**Example - List all pending tasks:**
```dataview
LIST
FROM "TaskNotes"
WHERE status = "pending"
  AND contains(tags, "tcm_101")
SORT due ASC
```

**Example - List with additional info:**
```dataview
LIST due + " - " + task_type
FROM "TaskNotes"
WHERE status = "pending"
SORT due ASC
```

---

### 2. TABLE Query

**Display data in table format**

```dataview
TABLE
  field1 as "Column 1",
  field2 as "Column 2"
FROM "folder"
WHERE condition
SORT field
```

**Example - Task table:**
```dataview
TABLE
  status as "Status",
  priority as "Priority",
  due as "Due Date",
  estimated_minutes as "Time (min)"
FROM "TaskNotes"
WHERE contains(tags, "tcm_101")
SORT due ASC
```

**Example - Quiz scores:**
```dataview
TABLE
  week as "Week",
  quiz_score as "Score",
  percentage as "Percentage",
  pass_fail as "Result"
FROM "Classes/TCM_101/Quizzes"
WHERE type = "quiz"
SORT week ASC
```

---

### 3. TASK Query

**Display tasks with checkboxes**

```dataview
TASK
FROM "folder"
WHERE condition
```

**Example - Today's tasks:**
```dataview
TASK
FROM "TaskNotes"
WHERE status != "completed"
  AND scheduled <= date(today)
  AND contains(tags, "tcm_101")
SORT priority DESC, due ASC
```

---

### 4. CALENDAR Query

**Display dates in calendar view**

```dataview
CALENDAR due
FROM "TaskNotes"
WHERE contains(tags, "tcm_101")
```

---

## 🔍 Filtering with WHERE

### Basic Conditions

```dataview
WHERE field = "value"
WHERE field != "value"
WHERE field > 10
WHERE field < 100
WHERE field >= 70
WHERE field <= 100
```

### Multiple Conditions

```dataview
WHERE status = "pending" 
  AND priority = "high"
  AND due <= date(today) + dur(7 days)
```

```dataview
WHERE status = "completed" 
  OR status = "cancelled"
```

### Contains

```dataview
WHERE contains(tags, "tcm_101")
WHERE contains(file.name, "Quiz")
WHERE contains(symptoms, "Fatigue")
```

### Date Comparisons

```dataview
WHERE due = date(today)
WHERE due < date(today)
WHERE scheduled >= date(today)
WHERE created >= date(today) - dur(7 days)
```

---

## 📊 OCDS Dashboard Queries

### 1. Overall Progress Dashboard

```dataview
TABLE WITHOUT ID
  "📚 " + class_name as "Class",
  current_week + " / " + total_weeks as "Week",
  round((current_week / total_weeks) * 100) + "%" as "Progress",
  overall_grade + "%" as "Grade"
FROM "Student_Progress"
WHERE type = "progress"
SORT class_name
```

---

### 2. Quiz Performance Summary

```dataview
TABLE
  week as "Week",
  quiz_score as "Score",
  points_possible as "Total",
  round((quiz_score / points_possible) * 100) + "%" as "Percentage",
  choice(quiz_score >= passing_score, "✅ Pass", "❌ Fail") as "Result"
FROM "Classes/TCM_101"
WHERE type = "quiz" AND status = "graded"
SORT week ASC
```

---

### 3. Weekly Task Summary

```dataview
TABLE WITHOUT ID
  week as "Week",
  length(rows) as "Total Tasks",
  length(filter(rows, (r) => r.status = "completed")) as "Completed",
  length(filter(rows, (r) => r.status = "pending")) as "Pending",
  round((length(filter(rows, (r) => r.status = "completed")) / length(rows)) * 100) + "%" as "Progress"
FROM "TaskNotes"
WHERE contains(tags, "tcm_101")
GROUP BY week
SORT week ASC
```

---

### 4. Flashcard Statistics

```dataview
TABLE
  topic as "Topic",
  cards_studied as "Studied",
  cards_total as "Total",
  round((cards_studied / cards_total) * 100) + "%" as "Progress",
  retention_rate + "%" as "Retention"
FROM "Student_Progress/Flashcard_Stats"
WHERE class_id = "TCM_101"
SORT topic
```

---

### 5. Time Tracking Summary

```dataview
TABLE
  week as "Week",
  sum(rows.actual_minutes) as "Total Minutes",
  round(sum(rows.actual_minutes) / 60, 1) + " hrs" as "Total Hours",
  length(rows) as "Sessions"
FROM "TaskNotes"
WHERE contains(tags, "tcm_101") 
  AND status = "completed"
  AND actual_minutes > 0
GROUP BY week
SORT week ASC
```

---

### 6. Upcoming Deadlines

```dataview
TABLE
  file.link as "Task",
  task_type as "Type",
  due as "Due Date",
  priority as "Priority",
  estimated_minutes + " min" as "Est. Time"
FROM "TaskNotes"
WHERE status = "pending"
  AND due >= date(today)
  AND due <= date(today) + dur(7 days)
  AND contains(tags, "tcm_101")
SORT due ASC, priority DESC
```

---

### 7. Grade Breakdown

```dataview
TABLE WITHOUT ID
  component as "Component",
  weight + "%" as "Weight",
  score + "%" as "Score",
  round(score * weight / 100, 1) + "%" as "Weighted"
FROM "Student_Progress/TCM_101_Grades"
WHERE type = "grade_component"
```

---

### 8. Material Completion Tracker

```dataview
TABLE
  material_type as "Type",
  length(rows) as "Total",
  length(filter(rows, (r) => r.completed = true)) as "Done",
  round((length(filter(rows, (r) => r.completed = true)) / length(rows)) * 100) + "%" as "Progress"
FROM "Classes/TCM_101"
WHERE type = "material"
GROUP BY material_type
```

---

## 🧮 Calculations and Functions

### Aggregation Functions

```dataview
TABLE
  sum(rows.quiz_score) as "Total Points",
  avg(rows.quiz_score) as "Average Score",
  min(rows.quiz_score) as "Lowest",
  max(rows.quiz_score) as "Highest",
  count(rows) as "Quiz Count"
FROM "Classes/TCM_101/Quizzes"
WHERE type = "quiz"
```

### Math Functions

```dataview
TABLE
  round(percentage, 1) as "Rounded %",
  floor(percentage) as "Floor",
  ceil(percentage) as "Ceiling"
FROM "Classes/TCM_101/Quizzes"
```

### String Functions

```dataview
TABLE
  upper(status) as "STATUS",
  lower(task_type) as "type",
  replace(file.name, "_", " ") as "Name"
FROM "TaskNotes"
```

### Date Functions

```dataview
TABLE
  date(today) as "Today",
  due - date(today) as "Days Until Due",
  dateformat(due, "MMM dd, yyyy") as "Formatted Date"
FROM "TaskNotes"
WHERE status = "pending"
```

---

## 📈 Advanced Queries

### 1. Grade Calculation with Weights

```dataview
TABLE WITHOUT ID
  "Overall Grade" as "Metric",
  round(
    (quiz_avg * 0.4) + 
    (flashcard_score * 0.3) + 
    (homework_avg * 0.2) + 
    (pomodoro_score * 0.1)
  ) + "%" as "Grade"
FROM "Student_Progress"
WHERE class_id = "TCM_101" AND type = "progress"
LIMIT 1
```

---

### 2. Conditional Formatting

```dataview
TABLE
  week as "Week",
  quiz_score as "Score",
  choice(
    quiz_score >= 90, "🌟 Excellent",
    quiz_score >= 80, "✅ Good",
    quiz_score >= 70, "👍 Pass",
    "❌ Review Needed"
  ) as "Performance"
FROM "Classes/TCM_101/Quizzes"
SORT week ASC
```

---

### 3. Progress Trend Analysis

```dataview
TABLE
  week as "Week",
  quiz_score as "Score",
  quiz_score - prev_score as "Change",
  choice(
    quiz_score > prev_score, "📈 Improving",
    quiz_score < prev_score, "📉 Declining",
    "➡️ Stable"
  ) as "Trend"
FROM "Classes/TCM_101/Quizzes"
SORT week ASC
```

---

### 4. Study Time vs Performance

```dataview
TABLE
  week as "Week",
  study_minutes as "Study Time (min)",
  quiz_score as "Quiz Score",
  round(quiz_score / (study_minutes / 60), 1) as "Points per Hour"
FROM "Student_Progress/Weekly_Stats"
WHERE class_id = "TCM_101"
SORT week ASC
```

---

## 🎨 Formatting Output

### Custom Column Names

```dataview
TABLE
  status as "📊 Status",
  priority as "⚡ Priority",
  due as "📅 Due Date"
FROM "TaskNotes"
```

### Concatenation

```dataview
TABLE
  "Week " + week + ", Day " + day as "Session",
  task_type + " (" + estimated_minutes + " min)" as "Task"
FROM "TaskNotes"
```

### Conditional Display

```dataview
TABLE
  choice(status = "completed", "✅", "⏳") + " " + file.link as "Task",
  choice(priority = "high", "🔴", choice(priority = "normal", "🟡", "🟢")) as "Priority"
FROM "TaskNotes"
```

---

## 🔗 OCDS Integration Patterns

### 1. Student Dashboard Template

```markdown
# Student Progress Dashboard

## Current Status

```dataview
TABLE WITHOUT ID
  "Current Week" as "Metric",
  current_week + " / " + total_weeks as "Value"
FROM "Student_Progress"
WHERE student_id = "{{STUDENT_ID}}" AND class_id = "{{CLASS_ID}}"
LIMIT 1
\```

## Overall Grade

```dataview
TABLE WITHOUT ID
  overall_grade + "%" as "Grade",
  choice(overall_grade >= 90, "A", 
         overall_grade >= 80, "B",
         overall_grade >= 70, "C",
         overall_grade >= 60, "D", "F") as "Letter"
FROM "Student_Progress"
WHERE student_id = "{{STUDENT_ID}}" AND class_id = "{{CLASS_ID}}"
\```

## Pending Tasks

```dataview
TASK
FROM "TaskNotes"
WHERE status = "pending"
  AND contains(tags, "{{CLASS_ID}}")
SORT due ASC
\```

## Recent Quiz Scores

```dataview
TABLE
  week as "Week",
  quiz_score + " / " + points_possible as "Score",
  percentage + "%" as "%"
FROM "Classes/{{CLASS_ID}}/Quizzes"
WHERE type = "quiz"
SORT week DESC
LIMIT 5
\```
```

---

### 2. Instructor Dashboard Template

```markdown
# Instructor Dashboard - {{CLASS_NAME}}

## Class Statistics

```dataview
TABLE WITHOUT ID
  "Total Students" as "Metric",
  length(rows) as "Count"
FROM "Student_Progress"
WHERE class_id = "{{CLASS_ID}}"
\```

## Average Performance

```dataview
TABLE WITHOUT ID
  "Average Grade" as "Metric",
  round(avg(rows.overall_grade), 1) + "%" as "Value"
FROM "Student_Progress"
WHERE class_id = "{{CLASS_ID}}"
\```

## Student List

```dataview
TABLE
  student_name as "Name",
  current_week as "Week",
  overall_grade + "%" as "Grade",
  choice(overall_grade >= 70, "✅", "⚠️") as "Status"
FROM "Student_Progress"
WHERE class_id = "{{CLASS_ID}}"
SORT overall_grade DESC
\```

## Quiz Performance Distribution

```dataview
TABLE
  week as "Week",
  round(avg(rows.quiz_score), 1) as "Avg Score",
  min(rows.quiz_score) as "Min",
  max(rows.quiz_score) as "Max"
FROM "Classes/{{CLASS_ID}}/Quizzes"
WHERE type = "quiz"
GROUP BY week
SORT week ASC
\```
```

---

## 🔧 Plugin Configuration

### Recommended Settings

```
Settings → Dataview
├── Enable JavaScript queries: ON
├── Enable inline queries: ON
├── Enable inline JavaScript queries: ON
├── Refresh interval: 2000ms
└── Date format: yyyy-MM-dd
```

---

## 💡 Best Practices

### Query Performance
- **Limit results** - Use LIMIT when possible
- **Specific paths** - FROM "specific/folder" not FROM ""
- **Index efficiently** - Let Dataview cache build
- **Avoid complex calculations** - Do in JavaScript if needed

### Maintainability
- **Comment queries** - Explain complex logic
- **Consistent naming** - Use standard field names
- **Reusable patterns** - Create query templates
- **Test incrementally** - Build queries step by step

### Readability
- **Format nicely** - Indent WHERE clauses
- **Use aliases** - Rename columns clearly
- **Add context** - Explain what query shows
- **Visual indicators** - Use emojis for status

---

## 🐛 Troubleshooting

### Query Returns No Results

**Problem:** Query shows empty

**Solutions:**
1. Check folder path is correct
2. Verify frontmatter fields exist
3. Test WHERE conditions individually
4. Check for typos in field names

### Query Shows Error

**Problem:** "Evaluation Error" message

**Solutions:**
1. Check syntax (commas, quotes, parentheses)
2. Verify field names are correct
3. Test simpler version of query
4. Check console for details (Ctrl/Cmd + Shift + I)

### Query Too Slow

**Problem:** Takes long time to load

**Solutions:**
1. Add LIMIT clause
2. Narrow FROM path
3. Simplify WHERE conditions
4. Reduce calculations

### Values Not Updating

**Problem:** Old data showing

**Solutions:**
1. Wait for refresh interval (2 seconds)
2. Close and reopen note
3. Restart Obsidian
4. Check frontmatter was saved

---

## ✅ Quick Reference

### Query Structure
```dataview
LIST|TABLE|TASK|CALENDAR [fields]
FROM "folder"
WHERE condition
SORT field [ASC|DESC]
LIMIT number
```

### Common Functions
- `sum()`, `avg()`, `min()`, `max()`, `count()`
- `round()`, `floor()`, `ceil()`
- `length()`, `contains()`, `filter()`
- `date()`, `dur()`, `dateformat()`

### Date Helpers
- `date(today)` - Today's date
- `dur(7 days)` - 7 day duration
- `dur(2 weeks)` - 2 week duration
- `dateformat(date, "format")` - Format date

### Conditionals
- `choice(condition, true_value, false_value)`
- `default(field, default_value)`

---

**Query your vault like a database with Dataview! 📊**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
