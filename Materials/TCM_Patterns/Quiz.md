---
ocds_type: quiz
material_id: quiz_tcm_patterns
class_id: TCM_Patterns
title: "Blood Stasis Pattern Quiz"
description: Test your knowledge of Blood Stasis Pattern
questions: 6
points_possible: 6
attempts: 0
max_attempts: 3
score: 0
correct_answers: 0
graded_date: null
student_answers: []
tags:
  - quiz
  - tcm_patterns
  - tcm
  - patterns
submission_status: not_started
submitted_date: null
percentage: 0
pass_fail: null
created: 2025-11-07
updated: 2025-11-07
---

# Blood Stasis Pattern Quiz

**Questions:** 6  
**Points:** 6  
**Time Limit:** None  
**Attempts:** 3 maximum

---

## Instructions

- Answer all 6 questions
- Each question is worth 1 point
- You may retake this quiz up to 3 times
- Your best score will count
- Passing score: 70%

---

## Question 1

**Difficulty:** Easy | **Bloom Level:** Remember

Which of the following is the MOST characteristic feature of Blood Stasis?

- [x] A) Fixed, stabbing pain
- [ ] B) Moving, distending pain
- [ ] C) Dull, heavy pain
- [ ] D) Burning, intense pain

**Correct Answer:** A

**Explanation:** Fixed, stabbing pain is the hallmark of Blood Stasis. Moving pain suggests Qi Stagnation, dull pain suggests Deficiency, burning pain suggests Heat.


---

## Question 2

**Difficulty:** Medium | **Bloom Level:** Apply

A patient presents with chest pain that is stabbing and fixed in location, purple lips, and a choppy pulse. Which formula is MOST appropriate?

- [x] A) Xue Fu Zhu Yu Tang
- [ ] B) Si Jun Zi Tang
- [ ] C) Xiao Yao San
- [ ] D) Liu Wei Di Huang Wan

**Correct Answer:** A

**Explanation:** Xue Fu Zhu Yu Tang treats upper body Blood Stasis. Si Jun Zi Tang tonifies Qi, Xiao Yao San moves Liver Qi, Liu Wei Di Huang Wan nourishes Kidney Yin.


---

## Question 3

**Difficulty:** Medium | **Bloom Level:** Understand

Blood Stasis is ALWAYS an Excess pattern with no underlying Deficiency.

- [ ] True
- [x] False

**Correct Answer:** False

**Explanation:** Blood Stasis is an Excess condition in itself, but it frequently arises from underlying Deficiency (Qi Deficiency or Blood Deficiency). This is called Mixed Excess-Deficiency.


---

## Question 4

**Difficulty:** Medium | **Bloom Level:** Understand

Which pathomechanism explains how Qi Stagnation leads to Blood Stasis?

- [x] A) Qi is the commander of Blood - stagnant Qi fails to move Blood
- [ ] B) Blood generates Qi
- [ ] C) Stagnant Blood blocks Qi flow
- [ ] D) Qi and Blood are unrelated

**Correct Answer:** A

**Explanation:** Qi moves Blood. When Qi stagnates, it cannot move Blood properly, leading to Blood Stasis over time.


---

## Question 5

**Difficulty:** Hard | **Bloom Level:** Analyze

**Clinical Scenario:**

A 35-year-old woman presents with severe menstrual cramps. The pain is sharp and stabbing in the lower abdomen, worse on the first day of menses. She passes large, dark clots. Her tongue is purple with purple spots, and her pulse is choppy. She also reports fatigue and a pale complexion.

**Question:** What is the primary pattern and what formula would you use?

**Your Answer:**

_[Write your answer here]_

**Correct Answer:** Uterine Blood Stasis with underlying Blood Deficiency. Use Shao Fu Zhu Yu Tang (primary) or Tao Hong Si Wu Tang (if more deficient).

**Explanation:** Stabbing pain + dark clots + purple tongue = Blood Stasis. Fatigue + pale complexion = Blood Deficiency. Shao Fu Zhu Yu Tang treats lower body Blood Stasis. Tao Hong Si Wu Tang combines blood-moving with blood-nourishing.


---

## Question 6

**Difficulty:** Hard | **Bloom Level:** Analyze

**Clinical Scenario:**

A 50-year-old man has chronic chest pain that is stabbing and fixed in the left chest. The pain is worse at night. He has purple lips, a dark complexion, and a wiry, choppy pulse. He denies shortness of breath or sweating.

**Question:** What is the pattern and primary formula?

**Your Answer:**

_[Write your answer here]_

**Correct Answer:** Heart Blood Stasis. Use Xue Fu Zhu Yu Tang.

**Explanation:** Stabbing chest pain + fixed location + worse at night + purple lips + choppy pulse = Heart Blood Stasis. Xue Fu Zhu Yu Tang is the primary formula for upper body/chest Blood Stasis.


---

## 📊 Quiz Results

```dataviewjs
// Auto-grading logic
const file = dv.current().file;
const fm = dv.page(file.path);

// Get student answers from frontmatter
const studentAnswers = fm.student_answers || [];
const totalQuestions = fm.questions || 0;

// Define correct answers
const correctAnswers = [
  "A",  // Q1
  "A",  // Q2
  "False",  // Q3
  "A",  // Q4
  "Uterine Blood Stasis with underlying Blood Deficiency. Use Shao Fu Zhu Yu Tang (primary) or Tao Hong Si Wu Tang (if more deficient).",  // Q5
  "Heart Blood Stasis. Use Xue Fu Zhu Yu Tang."  // Q6
];

// Calculate score
let correctCount = 0;
for (let i = 0; i < Math.min(studentAnswers.length, correctAnswers.length); i++) {
  if (studentAnswers[i] === correctAnswers[i]) {
    correctCount++;
  }
}

const percentage = totalQuestions > 0 ? Math.round((correctCount / totalQuestions) * 100) : 0;
const passFail = percentage >= 70 ? 'Pass' : 'Fail';

// Update frontmatter
const currentFile = app.workspace.getActiveFile();
if (currentFile && studentAnswers.length > 0) {
  await app.fileManager.processFrontMatter(currentFile, (fm) => {
    fm.score = correctCount;
    fm.correct_answers = correctCount;
    fm.percentage = percentage;
    fm.pass_fail = passFail;
    fm.submission_status = 'graded';
    fm.graded_date = new Date().toISOString();
    if (!fm.submitted_date) {
      fm.submitted_date = new Date().toISOString();
    }
    fm.attempts = (fm.attempts || 0) + 1;
  });
}

// Display results
if (studentAnswers.length > 0) {
  dv.paragraph(`
**Score:** ${correctCount}/${totalQuestions} (${percentage}%)  
**Status:** ${passFail === 'Pass' ? '✅ Pass' : '❌ Fail'}  
**Attempts:** ${fm.attempts || 0}/${fm.max_attempts || 3}
  `);
} else {
  dv.paragraph(`
**Status:** ⏳ Not yet submitted  
**Instructions:** Answer all questions above, then click "Submit Quiz" button
  `);
}
```

---

## 🎯 Submit Quiz

**Instructions:**
1. Review your answers above
2. Click the button below to submit and grade your quiz
3. You can retake up to 3 times

`BUTTON[submit_quiz]`
Submit Quiz
`BUTTON[submit_quiz]`

---

**Note:** This is an auto-graded quiz. Your score will be calculated immediately upon submission.

