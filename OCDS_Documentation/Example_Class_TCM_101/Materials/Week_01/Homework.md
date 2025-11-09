---
ocds_type: homework
material_id: hw_week01_tongue_cases
class_id: TCM_101
week: 1
title: "Week 1 Homework: Tongue Case Study Analysis"
description: Analyze tongue images and identify TCM patterns
points_possible: 20
weight: 0.2
assigned_date: 2025-01-01
due_date: 2025-01-12
submission_type: text
submission_format: markdown
max_submissions: 2
late_penalty: 10
max_late_days: 3
grading_rubric:
  - criterion: Accuracy of pattern identification
    points: 10
  - criterion: Quality of clinical reasoning
    points: 5
  - criterion: Clarity of written explanation
    points: 5
submission_status: submitted
submitted_date: 2025-11-07
score:
tags:
  - homework
  - week1
  - tongue-diagnosis
  - case-study
---

# Week 1 Homework: Tongue Case Study Analysis

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

Analyze each of the three tongue cases below. For each tongue:

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

**Patient complaints:** Fatigue, poor appetite, loose stools, cold limbs

**Tongue Description:**
[Imagine: Pale, swollen tongue with tooth marks on sides, thin white coating]

**Your Analysis:**

**Tongue Body:**

[Your description here]

**Tongue Coating:**

[Your description here]

**Primary Pattern(s):**

[Your pattern identification here]

**Clinical Reasoning:**

[Your explanation here - why this pattern? What features support it? What did you rule out?]

---

#### Case 2: 32-year-old Male

**Patient complaints:** Insomnia, anxiety, palpitations, restlessness, dry mouth

**Tongue Description:**
[Imagine: Red tongue with redder tip, thin coating or no coating in center]

**Your Analysis:**

**Tongue Body:**

[Your description here]

**Tongue Coating:**

[Your description here]

**Primary Pattern(s):**

[Your pattern identification here]

**Clinical Reasoning:**

[Your explanation here]

---

#### Case 3: 58-year-old Female

**Patient complaints:** Hot flashes, night sweats, dry mouth, insomnia, lower back pain

**Tongue Description:**
[Imagine: Red tongue with cracks, peeled coating in center, dry]

**Your Analysis:**

**Tongue Body:**

[Your description here]

**Tongue Coating:**

[Your description here]

**Primary Pattern(s):**

[Your pattern identification here]

**Clinical Reasoning:**

[Your explanation here]

---

### Part 2: Reflection (5 points)

Write a brief reflection (200-300 words) on:
- What was most challenging about this assignment?
- What did you learn about tongue diagnosis?
- How will you apply this in clinical practice?

**Your Reflection:**

[Your 200-300 word reflection here]

---

## ✅ Submission Guidelines

### What to Submit

- Completed analysis for all 3 cases
- Reflection paragraph
- All work in this file (above)

### How to Submit

1. Complete your analysis in the sections above
2. Update frontmatter: `submission_status: submitted`
3. Update frontmatter: `submitted_date: YYYY-MM-DD`
4. Save the file

### Format Requirements

- **Length:** 500-800 words total (all 3 cases + reflection)
- **Format:** Markdown (this file)
- **Citations:** Reference course materials when applicable

---

## 📊 Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Pattern Identification** | 10 | Correctly identifies primary patterns for all 3 cases |
| **Clinical Reasoning** | 5 | Clear, logical explanations with supporting evidence |
| **Written Communication** | 5 | Clear, organized, uses proper TCM terminology |
| **TOTAL** | **20** | |

---

## 💡 Tips for Success

- ✅ Review [[Week 1 Study Material]] before starting
- ✅ Use tongue diagnosis charts in your textbook
- ✅ Look at ALL features (body + coating)
- ✅ Explain WHY you chose each pattern
- ✅ Proofread before submitting

---

```meta-bind-button
label: Submit Homework
style: primary
action:
  type: inlineJS
  code: |
    const file = app.workspace.getActiveFile();
    await app.fileManager.processFrontMatter(file, (fm) => {
      fm.submission_status = 'submitted';
      fm.submitted_date = new Date().toISOString().split('T')[0];
    });
    new Notice('Homework submitted successfully!');
```
