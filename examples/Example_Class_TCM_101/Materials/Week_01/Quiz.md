---
ocds_type: quiz
material_id: quiz_week01
class_id: TCM_101
week: 1
title: "Week 1 Quiz: Tongue Diagnosis"
description: Test your knowledge of tongue diagnosis fundamentals
questions: 10
points_possible: 10
attempts: 3
max_attempts: 3
score: 10
correct_answers: 10
graded_date: 2025-11-07T07:09:34.742Z
student_answers:
  - B
  - B
  - B
  - B
  - B
  - C
  - B
  - B
  - B
  - B
tags:
  - quiz
  - week1
  - tongue-diagnosis
submission_status: graded
submitted_date: 2025-11-07T07:09:34.742Z
percentage: 100
pass_fail: Pass
---

# Week 1 Quiz: Tongue Diagnosis

**Questions:** 10  
**Points:** 10  
**Time Limit:** None  
**Attempts:** 3 maximum

---

## Instructions

- Answer all 10 questions
- Each question is worth 1 point
- You may retake this quiz up to 3 times
- Your best score will count
- Passing score: 70%

---

## Question 1

Which tongue color indicates Heat in TCM diagnosis?

- [ ] A) Pale
- [x] B) Red
- [ ] C) Purple
- [ ] D) Blue

---

## Question 2

A thick tongue coating indicates:

- [ ] A) Deficiency
- [x] B) Excess pathogen
- [ ] C) Normal condition
- [ ] D) Yin deficiency

---

## Question 3

A pale, swollen tongue with tooth marks most likely indicates:

- [ ] A) Liver Fire
- [x] B) Spleen Qi Deficiency
- [ ] C) Heart Blood Stasis
- [ ] D) Kidney Yin Deficiency

---

## Question 4

Which tongue coating color indicates Cold?

- [ ] A) Yellow
- [x] B) White
- [ ] C) Gray
- [ ] D) Black

---

## Question 5

A red tongue with no coating indicates:

- [ ] A) Excess Heat
- [x] B) Yin Deficiency with Heat
- [ ] C) Damp Heat
- [ ] D) Phlegm Heat

---

## Question 6

The tip of the tongue corresponds to which organ(s)?

- [ ] A) Liver and Gallbladder
- [ ] B) Spleen and Stomach
- [x] C) Heart and Lungs
- [ ] D) Kidneys and Bladder

---

## Question 7

A normal healthy tongue should be:

- [ ] A) Bright red with thick coating
- [x] B) Pale red with thin white coating
- [ ] C) Purple with no coating
- [ ] D) Dark red with yellow coating

---

## Question 8

Cracks on the tongue generally indicate:

- [ ] A) Excess Heat
- [x] B) Yin Deficiency
- [ ] C) Blood Stasis
- [ ] D) Dampness

---

## Question 9

A purple tongue with purple spots indicates:

- [ ] A) Qi Stagnation
- [x] B) Blood Stasis
- [ ] C) Phlegm accumulation
- [ ] D) Yin Deficiency

---

## Question 10

A peeled coating (no coating in certain areas) indicates:

- [ ] A) Excess pathogen
- [x] B) Stomach/Kidney Yin Deficiency
- [ ] C) Dampness
- [ ] D) Blood Stagnation

---

## Submit Quiz

```meta-bind-button
label: Submit Quiz
style: primary
action:
  type: inlineJS
  code: |
    const file = app.workspace.getActiveFile();
    const content = await app.vault.read(file);
    const lines = content.split('\n');
    
    // Define correct answers (B, B, B, B, B, C, B, B, B, B)
    const correctAnswers = ['B', 'B', 'B', 'B', 'B', 'C', 'B', 'B', 'B', 'B'];
    let score = 0;
    let studentAnswers = [];
    
    // Parse student answers from checkboxes
    let questionNum = 0;
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      
      // Look for checked answers (- [x])
      if (line.match(/^- \[x\]/)) {
        // Extract the answer letter (A, B, C, or D)
        const match = line.match(/\[x\]\s+([A-D])\)/);
        if (match && questionNum < 10) {
          const answer = match[1];
          studentAnswers.push(answer);
          
          // Check if correct
          if (answer === correctAnswers[questionNum]) {
            score++;
          }
          questionNum++;
        }
      }
      
      // Reset for next question when we hit a separator
      if (line.trim() === '---' && questionNum > 0 && questionNum < 10) {
        // Move to next question
      }
    }
    
    // Calculate percentage
    const percentage = Math.round((score / 10) * 100);
    const passFail = score >= 7 ? 'Pass' : 'Fail';
    
    // Update frontmatter
    await app.fileManager.processFrontMatter(file, (fm) => {
      fm.submission_status = 'graded';
      fm.submitted_date = new Date().toISOString();
      fm.graded_date = new Date().toISOString();
      fm.attempts = (fm.attempts || 0) + 1;
      fm.score = score;
      fm.correct_answers = score;
      fm.percentage = percentage;
      fm.pass_fail = passFail;
      fm.student_answers = studentAnswers;
    });
    
    new Notice(`Quiz graded! Score: ${score}/10 (${percentage}%) - ${passFail}`);
```

---

**After submission, your quiz will be auto-graded and results will appear in your dashboard.**
