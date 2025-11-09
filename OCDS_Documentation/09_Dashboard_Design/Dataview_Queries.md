# Dataview Queries

**Purpose:** Collection of useful Dataview queries for OCDS dashboards

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

This document provides ready-to-use Dataview queries for building OCDS dashboards.

---

## 🎯 Student Queries

### Show All Quizzes with Scores

\`\`\`dataview
TABLE
  title as "Quiz",
  score as "Score",
  attempts as "Attempts",
  graded_date as "Date"
FROM "Classes/TCM_101/Materials"
WHERE ocds_type = "quiz"
SORT week ASC
\`\`\`
```dataview
TABLE
  title as "Quiz",
  score as "Score",
  attempts as "Attempts",
  graded_date as "Date"
FROM "Classes/TCM_101/Materials"
WHERE ocds_type = "quiz"
SORT week ASC
```


---

### Show Incomplete Tasks

\`\`\`dataview
TASK
FROM "Classes/TCM_101/Materials"
WHERE !completed AND week = 5
\`\`\`

---

### Calculate Overall Grade

\`\`\`dataviewjs
const progress = dv.current();

const quizAvg = progress.quiz_average;
const flashcardScore = progress.flashcard_score;
const homeworkAvg = progress.homework_average;
const taskCompletion = progress.task_completion;

const weights = {
  quizzes: 0.40,
  flashcards: 0.30,
  homework: 0.20,
  tasks: 0.10
};

const finalGrade = (
  quizAvg * weights.quizzes +
  flashcardScore * weights.flashcards +
  homeworkAvg * weights.homework +
  taskCompletion * weights.tasks
);

dv.paragraph(\`**Final Grade:** \${finalGrade.toFixed(1)}%\`);
\`\`\`

---

## 👨‍🏫 Instructor Queries

### Class Grade Distribution

\`\`\`dataview
TABLE
  grade_range as "Grade",
  length(rows) as "Count"
FROM "Classes/TCM_101/Progress"
GROUP BY grade_range
SORT grade_range DESC
\`\`\`

---

### Students Below 70%

\`\`\`dataview
TABLE
  student_id as "Student",
  overall_grade as "Grade",
  current_week as "Week"
FROM "Classes/TCM_101/Progress"
WHERE overall_grade < 70
SORT overall_grade ASC
\`\`\`

---

### Pending Homework Grading

\`\`\`dataview
TABLE
  student_id as "Student",
  title as "Assignment",
  submitted_date as "Submitted"
FROM "Classes/TCM_101/Materials"
WHERE ocds_type = "homework" AND submission_status = "submitted" AND score = null
SORT submitted_date ASC
\`\`\`

---

## 📚 Related Documentation

- [[Progress_Dashboard.md]] - Student dashboard
- [[Instructor_Dashboard.md]] - Instructor dashboard
- [[Meta_Bind_Components.md]] - Interactive elements

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
