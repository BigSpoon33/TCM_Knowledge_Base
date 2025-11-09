---
count: .nan
score: 10
---
# Homework Template

**Purpose:** Define the structure and format for homework assignments in OCDS classes

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

Homework assignments in OCDS are **manually graded** tasks that require instructor review. Unlike quizzes (auto-graded), homework allows for:

- **Open-ended responses** - Essays, reflections, case studies
- **Creative work** - Projects, presentations, research
- **Practical application** - Clinical practice, real-world tasks
- **Subjective assessment** - Instructor judgment required

### Key Features

- ✅ **Flexible formats** - Text, file uploads, external links
- ✅ **Grading rubrics** - Clear assessment criteria
- ✅ **Due dates** - Integrated with timeline unlocking
- ✅ **Submission tracking** - Meta-bind forms for status
- ✅ **Feedback system** - Instructor comments and scores
>nice. this is the question I had about homework earlier that I kind of figured out bceause the documentation is good. homework is just a custom assignment.
---

## 🎯 When to Use Homework vs. Quizzes

| Use Homework When... | Use Quizzes When... |
|---------------------|---------------------|
| Subjective assessment needed | Objective right/wrong answers |
| Open-ended responses required | Multiple choice works |
| Creative work expected | Knowledge recall sufficient |
| Instructor feedback valuable | Instant feedback preferred |
| Application/synthesis needed | Recognition/comprehension tested |

**Example Homework Topics:**
- Case study analysis
- Research papers
- Reflection essays
- Clinical practice logs
- Project presentations
- Creative assignments

---

## 📝 Homework File Structure

### Frontmatter Schema

```yaml
---
# === OCDS CORE METADATA ===
ocds_type: homework
material_id: hw_week01_case_study
class_id: TCM_101
week: 1
day: 5

# === HOMEWORK DETAILS ===
title: "Week 1 Homework: Tongue Diagnosis Case Study"
description: "Analyze 3 tongue images and identify patterns"
points_possible: 20
weight: 0.20  # 20% of total grade

# === TIMELINE ===
assigned_date: 2025-01-05
due_date: 2025-01-12
unlock_requirements:
  - material_id: quiz_week01
    min_score: 70
  - material_id: study_week01_tongue
    status: completed

# === SUBMISSION ===
submission_type: text  # text, file, link, mixed
submission_format: markdown  # markdown, pdf, image, video
max_submissions: 3  # Allow resubmissions
late_penalty: 10  # 10% per day late
max_late_days: 3

# === GRADING ===
grading_rubric:
  - criterion: "Accuracy of pattern identification"
    points: 10
  - criterion: "Quality of clinical reasoning"
    points: 5
  - criterion: "Clarity of written explanation"
    points: 5

auto_grade: false
requires_instructor_review: true

# === TRACKING ===
submission_status: not_started  # not_started, in_progress, submitted, graded
submitted_date: null
graded_date: null
score: null
instructor_feedback: null

# === TAGS ===
tags:
  - homework
  - week1
  - tongue_diagnosis
  - case_study
---
```

---

## 🏗️ Homework Content Structure

### Template Layout

```markdown
# [Homework Title]

**Due:** [Date]  
**Points:** [X points]  
**Estimated Time:** [X hours]

---

## 📚 Learning Objectives

By completing this homework, you will:

- [Objective 1]
- [Objective 2]
- [Objective 3]

---

## 📋 Assignment Instructions

### Part 1: [Section Name]

[Clear instructions for this section]

**Requirements:**
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

**Example:**
[Show an example if helpful]

---

### Part 2: [Section Name]

[Instructions for next section]

---

## ✅ Submission Guidelines

### What to Submit

- [Item 1 to submit]
- [Item 2 to submit]

### How to Submit

1. Complete your work in this file (below the submission section)
2. Update `submission_status: submitted` in frontmatter
3. Update `submitted_date` to today's date
4. Save the file
5. Notify instructor (optional)

### Format Requirements

- **Length:** [X words/pages]
- **Format:** [Markdown/PDF/etc.]
- **Citations:** [Required/optional, style]
- **File naming:** [If external files required]

---

## 📊 Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| [Criterion 1] | X | [What earns full points] |
| [Criterion 2] | X | [What earns full points] |
| [Criterion 3] | X | [What earns full points] |
| **TOTAL** | **X** | |

### Grading Scale

- **90-100%** - Excellent work, exceeds expectations
- **80-89%** - Good work, meets all requirements
- **70-79%** - Satisfactory, meets most requirements
- **60-69%** - Needs improvement, missing key elements
- **Below 60%** - Incomplete or significantly below expectations

---

## 💡 Tips for Success

- ✅ [Tip 1]
- ✅ [Tip 2]
- ✅ [Tip 3]

---

## 📚 Resources

### Required Reading
- [[Study Material 1]]
- [[Study Material 2]]

### Optional Resources
- [External link 1]
- [External link 2]

---

## ❓ FAQ

**Q: Can I submit late?**  
A: Yes, with a [X]% penalty per day, up to [X] days late.

**Q: Can I resubmit?**  
A: Yes, up to [X] times before the due date.

**Q: How long should my response be?**  
A: [Guidance on length]

---

## 📝 YOUR SUBMISSION

### Submission Metadata

```meta-bind
submission_status: [not_started/in_progress/submitted/graded]
submitted_date: YYYY-MM-DD
```

---

### Your Work Goes Here

[Student completes assignment below this line]

---

## 👨‍🏫 INSTRUCTOR SECTION

### Grading

```meta-bind
score: [0-100]
graded_date: YYYY-MM-DD
```

### Rubric Scores

| Criterion | Points Earned | Points Possible |
|-----------|---------------|-----------------|
| [Criterion 1] | | X |
| [Criterion 2] | | X |
| [Criterion 3] | | X |
| **TOTAL** | | **X** |

### Feedback

[Instructor comments here]

**Strengths:**
- 

**Areas for Improvement:**
- 

**Next Steps:**
- 

---

**Graded by:** [Instructor name]  
**Date:** [Date]
```

---

## 📖 Complete Example: Case Study Homework

### Example File: `HW_Week01_Tongue_Case_Study.md`

```markdown
---
ocds_type: homework
material_id: hw_week01_tongue_case_study
class_id: TCM_101
week: 1
day: 5

title: "Week 1 Homework: Tongue Diagnosis Case Study"
description: "Analyze 3 tongue images and identify TCM patterns"
points_possible: 20
weight: 0.20

assigned_date: 2025-01-05
due_date: 2025-01-12

submission_type: text
submission_format: markdown
max_submissions: 2
late_penalty: 10
max_late_days: 3

grading_rubric:
  - criterion: "Accuracy of pattern identification"
    points: 10
  - criterion: "Quality of clinical reasoning"
    points: 5
  - criterion: "Clarity of written explanation"
    points: 5

submission_status: not_started
submitted_date: null
score: null

tags:
  - homework
  - week1
  - tongue_diagnosis
---

# Week 1 Homework: Tongue Diagnosis Case Study

**Due:** January 12, 2025  
**Points:** 20 points  
**Estimated Time:** 2-3 hours

---

## 📚 Learning Objectives

By completing this homework, you will:

- Apply tongue diagnosis principles to real cases
- Identify TCM patterns from tongue presentation
- Develop clinical reasoning skills
- Practice writing clear diagnostic assessments

---

## 📋 Assignment Instructions

### Part 1: Tongue Analysis (15 points)

Analyze each of the three tongue images below. For each tongue:

1. **Describe the tongue body** (color, shape, size, cracks, etc.)
2. **Describe the tongue coating** (color, thickness, distribution)
3. **Identify the primary TCM pattern(s)**
4. **Explain your reasoning** (why this pattern?)

**Requirements:**
- Use proper TCM terminology
- Cite specific tongue features that support your diagnosis
- Consider differential diagnosis (what else could it be?)
- Reference course materials

---

#### Case 1: 45-year-old Female

![Tongue Image 1](images/tongue_case_1.jpg)

**Patient complaints:** Fatigue, poor appetite, loose stools

**Your Analysis:**

[Student writes analysis here]

---

#### Case 2: 32-year-old Male

![Tongue Image 2](images/tongue_case_2.jpg)

**Patient complaints:** Insomnia, anxiety, palpitations

**Your Analysis:**

[Student writes analysis here]

---

#### Case 3: 58-year-old Female

![Tongue Image 3](images/tongue_case_3.jpg)

**Patient complaints:** Hot flashes, night sweats, dry mouth

**Your Analysis:**

[Student writes analysis here]

---

### Part 2: Reflection (5 points)

Write a brief reflection (200-300 words) on:

- What was most challenging about this assignment?
- What did you learn about tongue diagnosis?
- How will you apply this in clinical practice?

**Your Reflection:**

[Student writes reflection here]

---

## ✅ Submission Guidelines

### What to Submit

- Completed analysis for all 3 cases
- Reflection paragraph
- All work in this file (below)

### How to Submit

1. Complete your analysis in the sections above
2. Update frontmatter: `submission_status: submitted`
3. Update frontmatter: `submitted_date: 2025-01-10` (today's date)
4. Save the file
5. Your instructor will be notified automatically

### Format Requirements

- **Length:** 500-800 words total (all 3 cases + reflection)
- **Format:** Markdown (this file)
- **Citations:** Reference course materials when applicable
- **Images:** Do not modify the embedded images

---

## 📊 Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Pattern Identification Accuracy** | 10 | Correctly identifies primary patterns for all 3 cases |
| **Clinical Reasoning Quality** | 5 | Provides clear, logical explanations with supporting evidence |
| **Written Communication** | 5 | Clear, organized, uses proper TCM terminology |
| **TOTAL** | **20** | |

### Detailed Rubric

**Pattern Identification (10 points)**
- 9-10: All patterns correct with nuanced understanding
- 7-8: Most patterns correct, minor errors
- 5-6: Some patterns correct, significant gaps
- 3-4: Few patterns correct, major misunderstandings
- 0-2: Incorrect or missing

**Clinical Reasoning (5 points)**
- 5: Excellent reasoning, cites specific features, considers differentials
- 4: Good reasoning, mostly complete explanations
- 3: Adequate reasoning, some gaps in logic
- 2: Weak reasoning, minimal explanation
- 0-1: Poor or no reasoning provided

**Written Communication (5 points)**
- 5: Clear, well-organized, proper terminology, no errors
- 4: Mostly clear, minor organizational or terminology issues
- 3: Adequate clarity, some confusion or errors
- 2: Unclear writing, frequent errors
- 0-1: Very poor communication

---

## 💡 Tips for Success

- ✅ Review [[Week 1 Study Material - Tongue Diagnosis]] before starting
- ✅ Use the tongue diagnosis charts in your textbook
- ✅ Look at ALL features (body + coating) before deciding on pattern
- ✅ Explain WHY you chose each pattern (don't just name it)
- ✅ Consider what patterns you ruled out and why
- ✅ Proofread your work before submitting

---

## 📚 Resources

### Required Reading
- [[Week 1 Study Material - Tongue Diagnosis]]
- [[TCM Concepts - Tongue Body Characteristics]]
- [[TCM Concepts - Tongue Coating Analysis]]

### Optional Resources
- Maciocia, G. (2004). *Tongue Diagnosis in Chinese Medicine*
- [Tongue Diagnosis Photo Atlas](https://example.com/tongue-atlas)
- [[Flashcards - Tongue Diagnosis]]

---

## ❓ FAQ

**Q: Can I submit late?**  
A: Yes, with a 10% penalty per day, up to 3 days late. After 3 days, no credit.

**Q: Can I resubmit?**  
A: Yes, up to 2 times before the due date. Only the latest submission will be graded.

**Q: How long should my response be?**  
A: Aim for 150-200 words per case (total 450-600 words) + 200-300 word reflection.

**Q: Do I need to cite sources?**  
A: Yes, reference course materials when you use specific information (e.g., "According to Week 1 Study Material...").

**Q: What if I'm not sure about a pattern?**  
A: That's okay! Explain your reasoning and mention what you're uncertain about. Partial credit given for good reasoning even if pattern is incorrect.

---

## 📝 YOUR SUBMISSION

### Submission Metadata

```meta-bind-button
label: Mark as In Progress
style: default
action:
  type: inlineJS
  code: |
    const file = app.workspace.getActiveFile();
    await app.fileManager.processFrontMatter(file, (fm) => {
      fm.submission_status = 'in_progress';
    });
    new Notice('Assignment marked as in progress');
```

```meta-bind-button
label: Submit Assignment
style: default
actions: 
  - type: updateMetadata
    bindTarget: count
    evaluate: true
    value: "x + 1"
args:
  submission_status: submitted
  submitted_date: {{date:YYYY-MM-DD}}
```

**Current Status:** `VIEW{submission_status}`  
**Submitted:** `VIEW{submitted_date}`

---

### Case 1 Analysis

**Tongue Body:**

[Your description here]

**Tongue Coating:**

[Your description here]

**Primary Pattern(s):**

[Your pattern identification here]

**Clinical Reasoning:**

[Your explanation here - why this pattern? What features support it? What did you rule out?]

---

### Case 2 Analysis

**Tongue Body:**

[Your description here]

**Tongue Coating:**

[Your description here]

**Primary Pattern(s):**

[Your pattern identification here]

**Clinical Reasoning:**

[Your explanation here]

---

### Case 3 Analysis

**Tongue Body:**

[Your description here]

**Tongue Coating:**

[Your description here]

**Primary Pattern(s):**

[Your pattern identification here]

**Clinical Reasoning:**

[Your explanation here]

---

### Reflection

[Your 200-300 word reflection here]

---

## 👨‍🏫 INSTRUCTOR SECTION

*(Students: Do not edit below this line)*

---

### Grading

```meta-bind
score: [0-20]
graded_date: YYYY-MM-DD
```

**Score:** `VIEW{score}` / 20  
**Percentage:** `VIEW{score / 20 * 100}`%  
**Graded:** `VIEW{graded_date}`

---

### Rubric Scores

| Criterion | Points Earned | Points Possible | Notes |
|-----------|---------------|-----------------|-------|
| Pattern Identification | | 10 | |
| Clinical Reasoning | | 5 | |
| Written Communication | | 5 | |
| **TOTAL** | | **20** | |

---

### Detailed Feedback

**Case 1:**
- 

**Case 2:**
- 

**Case 3:**
- 

**Reflection:**
- 

---

### Overall Comments

**Strengths:**
- 

**Areas for Improvement:**
- 

**Next Steps:**
- 

---

**Graded by:** [Instructor name]  
**Date:** [Date]  
**Time spent grading:** [X minutes]
```

---

## 🔧 Meta-Bind Integration

### Submission Status Buttons

```meta-bind-button
label: Start Assignment
style: primary
action:
  type: inlineJS
  code: |
    const file = app.workspace.getActiveFile();
    await app.fileManager.processFrontMatter(file, (fm) => {
      fm.submission_status = 'in_progress';
    });
    new Notice('Assignment started!');
```

```meta-bind-button
label: Submit for Grading
style: primary
action:
  type: inlineJS
  code: |
    const file = app.workspace.getActiveFile();
    const cache = app.metadataCache.getFileCache(file);
    const fm = cache?.frontmatter || {};
    
    if (fm.submission_status === 'in_progress') {
      await app.fileManager.processFrontMatter(file, (frontmatter) => {
        frontmatter.submission_status = 'submitted';
        frontmatter.submitted_date = new Date().toISOString().split('T')[0];
      });
      new Notice('Assignment submitted for grading!');
    } else {
      new Notice('Start the assignment first!');
    }
```

```meta-bind-button
label: Resubmit
style: default
action:
  type: inlineJS
  code: |
    const file = app.workspace.getActiveFile();
    const cache = app.metadataCache.getFileCache(file);
    const fm = cache?.frontmatter || {};
    
    if (fm.submission_status === 'graded' && fm.score < 80) {
      await app.fileManager.processFrontMatter(file, (frontmatter) => {
        frontmatter.submission_status = 'submitted';
        frontmatter.submitted_date = new Date().toISOString().split('T')[0];
      });
      new Notice('Assignment resubmitted!');
    } else {
      new Notice('Resubmission not available');
    }
```
>The metabind syntax is not right. There are a couple errors in this document. I fixed one. The documentation for buttons is here:
>https://www.moritzjung.dev/obsidian-meta-bind-plugin-docs/reference/buttonactions/updatemetadata/
---

### Status Display

```meta-bind
INPUT[progressBar(
  minValue(0),
  maxValue(20),
  value(score)
)]
```

**Status:** `VIEW{submission_status}`  
**Score:** `VIEW{score}` / `VIEW{points_possible}` (`VIEW{score / points_possible * 100}`%)  
**Submitted:** `VIEW{submitted_date}`  
**Graded:** `VIEW{graded_date}`
>Gotta get these things working. will look really cool and increase functionality, quick readability of dashboards. 
---

## 📊 Dataview Integration

### Show All Homework for This Week

```dataview
TABLE
  title as "Assignment",
  points_possible as "Points",
  due_date as "Due",
  submission_status as "Status",
  score as "Score"
FROM "Classes/TCM_101"
WHERE ocds_type = "homework" AND week = 1
SORT due_date ASC
```

---

### Show Graded Homework

```dataview
TABLE
  title as "Assignment",
  score as "Score",
  points_possible as "Possible",
  round(score / points_possible * 100, 1) + "%" as "Percentage",
  graded_date as "Graded"
FROM "Classes/TCM_101"
WHERE ocds_type = "homework" AND submission_status = "graded"
SORT graded_date DESC
```

---

### Calculate Homework Average

```dataviewjs
const homework = dv.pages('"Classes/TCM_101"')
  .where(p => p.ocds_type === "homework" && p.score != null);

const totalPoints = homework.map(h => h.score).reduce((a, b) => a + b, 0);
const totalPossible = homework.map(h => h.points_possible).reduce((a, b) => a + b, 0);
const average = (totalPoints / totalPossible * 100).toFixed(1);

dv.paragraph(`**Homework Average:** ${average}% (${totalPoints}/${totalPossible} points)`);
```
>Gotta have some slick dataviews, baseviews, and js
---

## 🔄 Automation Scripts

### Auto-Update Submission Status

```python
# scripts/update_homework_status.py

def check_homework_submissions(class_id: str):
    """Check all homework files and update submission status."""
    
    homework_files = get_files_by_type(class_id, "homework")
    
    for hw_file in homework_files:
        frontmatter = parse_frontmatter(hw_file)
        
        # Check if past due date
        if is_past_due(frontmatter['due_date']):
            if frontmatter['submission_status'] == 'not_started':
                update_frontmatter(hw_file, 'submission_status', 'missing')
        
        # Check if submitted but not graded
        if frontmatter['submission_status'] == 'submitted':
            days_waiting = days_since(frontmatter['submitted_date'])
            if days_waiting > 7:
                notify_instructor(hw_file, "Grading overdue")
```

---

### Calculate Late Penalty

```python
def calculate_late_penalty(submitted_date: str, due_date: str, 
                          late_penalty: int, max_late_days: int) -> float:
    """Calculate late penalty percentage."""
    
    days_late = (submitted_date - due_date).days
    
    if days_late <= 0:
        return 0.0  # On time
    
    if days_late > max_late_days:
        return 1.0  # 100% penalty (no credit)
    
    penalty = (late_penalty / 100) * days_late
    return min(penalty, 1.0)  # Cap at 100%

# Example usage
penalty = calculate_late_penalty("2025-01-15", "2025-01-12", 10, 3)
# 3 days late, 10% per day = 30% penalty
final_score = raw_score * (1 - penalty)
```

---

## 🎯 Best Practices

### For Instructors

**Creating Homework:**
- ✅ **Clear instructions** - Students should know exactly what to do
- ✅ **Specific rubric** - Define what earns full points
- ✅ **Reasonable scope** - Don't overload students
- ✅ **Aligned objectives** - Homework should match learning goals
- ✅ **Provide examples** - Show what good work looks like

**Grading Homework:**
- ✅ **Grade promptly** - Within 1 week of submission
- ✅ **Use rubric** - Be consistent across students
- ✅ **Give feedback** - Not just a score, explain why
- ✅ **Encourage revision** - Allow resubmission if appropriate
- ✅ **Track time** - Note how long grading takes (improve efficiency)

---

### For Students

**Completing Homework:**
- ✅ **Start early** - Don't wait until the last minute
- ✅ **Read instructions** - Carefully, multiple times
- ✅ **Check rubric** - Make sure you address all criteria
- ✅ **Use resources** - Reference course materials
- ✅ **Proofread** - Check for errors before submitting

**After Submission:**
- ✅ **Review feedback** - Learn from instructor comments
- ✅ **Ask questions** - If feedback is unclear
- ✅ **Apply learning** - Use feedback on future assignments
- ✅ **Track progress** - Monitor your homework average

---

## 🔍 Troubleshooting

### Common Issues

**Issue:** "I can't find the homework file"  
**Solution:** Check `Classes/[CLASS_ID]/Homework/` folder. Make sure week is unlocked.

**Issue:** "Submit button doesn't work"  
**Solution:** Make sure Meta-bind plugin is installed and enabled. Check frontmatter syntax.

**Issue:** "I submitted but status still shows 'in_progress'"  
**Solution:** Manually update frontmatter: `submission_status: submitted` and add `submitted_date`.

**Issue:** "My score isn't showing in dashboard"  
**Solution:** Make sure `score` field in frontmatter is a number (not text). Refresh dashboard.

**Issue:** "Late penalty calculated wrong"  
**Solution:** Check `late_penalty` and `max_late_days` in frontmatter. Verify date format is YYYY-MM-DD.

---

## 📚 Related Documentation

- [[Quiz_Template.md]] - Auto-graded multiple choice quizzes
- [[Grading_Config_Schema.md]] - How grading weights work
- [[Progress_Tracking_Schema.md]] - How scores are tracked
- [[Meta_Bind_Syntax.md]] - Interactive form elements
- [[Dataview_Queries.md]] - Dashboard queries for homework

---

## 🎓 Homework vs. Other Assessment Types

| Feature | Homework | Quiz | Flashcards | Pomodoros |
|---------|----------|------|------------|-----------|
| **Grading** | Manual | Auto | Auto | Auto |
| **Format** | Open-ended | Multiple choice | Q&A pairs | Time tracking |
| **Feedback** | Detailed | Instant | Spaced repetition | Progress bars |
| **Weight** | 20% (default) | 40% | 30% | 10% |
| **Purpose** | Application | Knowledge | Retention | Engagement |

---

## ✅ Homework Checklist

### For Instructors Creating Homework

- [ ] Clear, specific title
- [ ] Complete frontmatter with all required fields
- [ ] Learning objectives stated
- [ ] Step-by-step instructions
- [ ] Detailed grading rubric
- [ ] Submission guidelines
- [ ] Due date set
- [ ] Unlock requirements defined
- [ ] Resources linked
- [ ] Example provided (if helpful)
- [ ] FAQ section included
- [ ] Meta-bind buttons configured
- [ ] Instructor grading section prepared

---

### For Students Completing Homework

- [ ] Read all instructions carefully
- [ ] Review grading rubric
- [ ] Check required resources
- [ ] Start assignment early
- [ ] Complete all required sections
- [ ] Proofread work
- [ ] Check word count / length requirements
- [ ] Update submission status
- [ ] Add submission date
- [ ] Save file
- [ ] Verify submission in dashboard

---

**Homework is where learning becomes application. Make it meaningful!**

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
