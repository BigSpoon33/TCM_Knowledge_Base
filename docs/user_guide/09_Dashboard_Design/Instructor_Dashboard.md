# Instructor Dashboard

**Purpose:** Instructor-facing dashboard for class management and monitoring

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

The Instructor Dashboard provides a comprehensive view of class performance, student progress, and items requiring attention.

---

## 🎯 Key Components

### 1. Class Overview

```markdown
# TCM 101 - Instructor Dashboard

**Class:** Traditional Chinese Medicine Fundamentals  
**Instructor:** Dr. Jane Smith  
**Students:** 25 enrolled  
**Current Week:** 5 of 12  
**Class Average:** 84.2% (B)

---

## 📊 Class Statistics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **Class Average** | 84.2% | 80% | ✅ Above Target |
| **Completion Rate** | 92% | 90% | ✅ On Track |
| **Active Students** | 23/25 | 100% | ⚠️ 2 Inactive |
| **Avg Study Time** | 8.5 hrs/week | 8 hrs | ✅ Good |
```

---

### 2. Grade Distribution

```markdown
## 📈 Grade Distribution

```dataview
TABLE
  grade_range as "Grade",
  count(student_id) as "Students",
  round(count(student_id) / 25 * 100, 1) + "%" as "Percentage"
FROM "Classes/TCM_101/Progress"
GROUP BY grade_range
SORT grade_range DESC
```

**Distribution:**
- A (90-100%): 8 students (32%)
- B (80-89%): 12 students (48%)
- C (70-79%): 4 students (16%)
- D (60-69%): 1 student (4%)
```

---

### 3. Students Needing Attention

```markdown
## ⚠️ Review Queue

```dataview
TABLE
  student_id as "Student",
  overall_grade as "Grade",
  flag_severity as "Priority",
  issue as "Issue",
  days_flagged as "Days"
FROM "Classes/TCM_101/Flags"
WHERE status = "open"
SORT flag_severity DESC, days_flagged DESC
```
```

---

### 4. Pending Grading

```markdown
## 📝 Pending Grading

**Homework to Grade:** 12 submissions  
**Estimated Time:** 3 hours

```dataview
TABLE
  student_id as "Student",
  homework_title as "Assignment",
  submitted_date as "Submitted",
  days_waiting as "Waiting"
FROM "Classes/TCM_101/Materials"
WHERE ocds_type = "homework" AND submission_status = "submitted" AND score = null
SORT submitted_date ASC
```
```

---

### 5. Component Performance

```markdown
## 🎯 Component Averages

| Component | Class Avg | Std Dev | Min | Max |
|-----------|-----------|---------|-----|-----|
| Quizzes | 82.5% | 8.2% | 65% | 98% |
| Flashcards | 87.3% | 6.5% | 72% | 100% |
| Homework | 85.1% | 9.1% | 68% | 96% |
| Tasks | 91.2% | 5.3% | 78% | 100% |
```

---

## 📚 Related Documentation

- [[Progress_Dashboard.md]] - Student view
- [[Dataview_Queries.md]] - Query examples
- [[Grade_Reports.md]] - Reporting

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
