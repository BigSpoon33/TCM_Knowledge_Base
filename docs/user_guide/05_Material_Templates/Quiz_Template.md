# Quiz Template

**Complete template for creating auto-gradable quizzes**

---

## 📚 Overview

OCDS quizzes are multiple-choice assessments that can be automatically graded. This template provides the standard format for creating quizzes that integrate with:
- Meta-bind for answer selection
- Auto-grader for scoring
- Progress tracking for grades
- Unlock system for progression

---

## 📋 Complete Template

```markdown
---
# Quiz Metadata
type: quiz
class_id: "{{CLASS_ID}}"
week: {{WEEK_NUMBER}}
day: {{DAY_NUMBER}}
topic: "{{TOPIC_NAME}}"

# Quiz Configuration
total_questions: {{QUESTION_COUNT}}
passing_score: {{PASSING_SCORE}}
time_limit_minutes: {{TIME_LIMIT}}
allow_retake: false
show_answers_after: true

# Student Data (populated on import)
student_id: ""
quiz_date: ""
start_time: ""
submit_time: ""

# Answers (populated by student)
q1_answer: ""
q2_answer: ""
q3_answer: ""
# ... one per question

# Grading (populated by auto-grader)
score: 0
percentage: 0
pass_fail: ""
status: "not_started"

# Tags
tags:
  - quiz
  - {{CLASS_ID}}
  - week_{{WEEK_NUMBER}}
  - {{TOPIC_TAG}}
---

# Quiz: {{TOPIC_NAME}}

**Class:** {{CLASS_NAME}}  
**Week {{WEEK_NUMBER}}, Day {{DAY_NUMBER}}**

> [!info] Quiz Information
> - **Questions:** {{QUESTION_COUNT}}
> - **Passing Score:** {{PASSING_SCORE}}/{{QUESTION_COUNT}} ({{PASSING_PERCENTAGE}}%)
> - **Time Limit:** {{TIME_LIMIT}} minutes
> - **Retakes Allowed:** {{ALLOW_RETAKE}}
> - **Status:** `VIEW[{status}][text]`

---

## Instructions

1. **Read each question carefully**
2. **Select ONE answer per question** using the dropdown
3. **Review your answers** before submitting
4. **Click "Submit Quiz"** when complete
5. **View your results** below

> [!warning] Important
> - You have {{TIME_LIMIT}} minutes to complete this quiz
> - Once submitted, answers cannot be changed
> - Make sure all questions are answered before submitting

---

## Questions

### Question 1

{{QUESTION_1_TEXT}}

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q1_answer]
\```

**A)** {{OPTION_1A}}  
**B)** {{OPTION_1B}}  
**C)** {{OPTION_1C}}  
**D)** {{OPTION_1D}}

---

### Question 2

{{QUESTION_2_TEXT}}

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q2_answer]
\```

**A)** {{OPTION_2A}}  
**B)** {{OPTION_2B}}  
**C)** {{OPTION_2C}}  
**D)** {{OPTION_2D}}

---

### Question 3

{{QUESTION_3_TEXT}}

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q3_answer]
\```

**A)** {{OPTION_3A}}  
**B)** {{OPTION_3B}}  
**C)** {{OPTION_3C}}  
**D)** {{OPTION_3D}}

---

<!-- Repeat for all questions -->

---

## Submit Quiz

\```meta-bind-button
label: Submit Quiz
style: primary
action:
  type: command
  command: ocds:grade-quiz
\```

> [!tip] Before Submitting
> - Review all your answers
> - Ensure no questions are blank
> - Check your time remaining

---

## Results

**Score:** `VIEW[{score}][text]` / {{QUESTION_COUNT}}  
**Percentage:** `VIEW[{percentage}][text]`%  
**Result:** `VIEW[{pass_fail}][text]`

**Time Taken:** `VIEW[{time_taken}][text]` minutes

---

## Answer Key

<!-- Hidden until quiz is graded -->

\```dataview
TABLE WITHOUT ID
  question as "Question",
  your_answer as "Your Answer",
  correct_answer as "Correct Answer",
  choice(correct, "✅", "❌") as "Result",
  explanation as "Explanation"
FROM "this.file"
WHERE status = "graded"
\```

---

## Next Steps

\```dataview
LIST
FROM "TaskNotes"
WHERE contains(blocking, this.file.link)
  AND status = "pending"
LIMIT 1
\```

---

*Quiz generated from question bank: {{QUESTION_BANK_SOURCE}}*
```

---

## 📝 Filled Example

```markdown
---
# Quiz Metadata
type: quiz
class_id: "TCM_101"
week: 1
day: 1
topic: "Qi Deficiency Pattern"

# Quiz Configuration
total_questions: 10
passing_score: 7
time_limit_minutes: 15
allow_retake: false
show_answers_after: true

# Student Data
student_id: "JD110590"
quiz_date: ""
start_time: ""
submit_time: ""

# Answers
q1_answer: ""
q2_answer: ""
q3_answer: ""
q4_answer: ""
q5_answer: ""
q6_answer: ""
q7_answer: ""
q8_answer: ""
q9_answer: ""
q10_answer: ""

# Grading
score: 0
percentage: 0
pass_fail: ""
status: "not_started"

# Tags
tags:
  - quiz
  - tcm_101
  - week_1
  - qi_deficiency
---

# Quiz: Qi Deficiency Pattern

**Class:** TCM 101 - Fundamentals  
**Week 1, Day 1**

> [!info] Quiz Information
> - **Questions:** 10
> - **Passing Score:** 7/10 (70%)
> - **Time Limit:** 15 minutes
> - **Retakes Allowed:** No
> - **Status:** `VIEW[{status}][text]`

---

## Instructions

1. **Read each question carefully**
2. **Select ONE answer per question** using the dropdown
3. **Review your answers** before submitting
4. **Click "Submit Quiz"** when complete
5. **View your results** below

> [!warning] Important
> - You have 15 minutes to complete this quiz
> - Once submitted, answers cannot be changed
> - Make sure all questions are answered before submitting

---

## Questions

### Question 1

What is the primary tongue presentation for Qi Deficiency?

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q1_answer]
\```

**A)** Pale, swollen with tooth marks  
**B)** Red with yellow coating  
**C)** Purple with dark spots  
**D)** Normal pink

---

### Question 2

Which of the following is a cardinal symptom of Qi Deficiency?

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q2_answer]
\```

**A)** Thirst with desire for cold drinks  
**B)** Fatigue and weakness  
**C)** Night sweats  
**D)** Dry stools

---

### Question 3

What is the pulse presentation typically seen in Qi Deficiency?

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q3_answer]
\```

**A)** Wiry and rapid  
**B)** Slippery and full  
**C)** Weak and empty  
**D)** Choppy and irregular

---

### Question 4

Which formula is the foundational treatment for Spleen Qi Deficiency?

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q4_answer]
\```

**A)** Liu Jun Zi Tang  
**B)** Si Jun Zi Tang  
**C)** Bu Zhong Yi Qi Tang  
**D)** Gui Pi Tang

---

### Question 5

What is the primary etiology of Qi Deficiency?

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q5_answer]
\```

**A)** External pathogenic factors  
**B)** Emotional stress and overwork  
**C)** Dietary irregularities and constitutional weakness  
**D)** Trauma and injury

---

### Question 6

Which organ is most commonly affected in Qi Deficiency patterns?

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q6_answer]
\```

**A)** Liver  
**B)** Heart  
**C)** Spleen  
**D)** Kidney

---

### Question 7

What type of sweating is characteristic of Qi Deficiency?

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q7_answer]
\```

**A)** Night sweats  
**B)** Spontaneous sweating during the day  
**C)** Sweating only with exertion  
**D)** No sweating

---

### Question 8

Which treatment principle is appropriate for Qi Deficiency?

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q8_answer]
\```

**A)** Clear Heat and Drain Fire  
**B)** Tonify Qi and Strengthen the Spleen  
**C)** Nourish Yin and Clear Deficiency Heat  
**D)** Invigorate Blood and Remove Stasis

---

### Question 9

What is the voice quality typically associated with Qi Deficiency?

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q9_answer]
\```

**A)** Loud and strong  
**B)** Weak and low  
**C)** Hoarse and rough  
**D)** High-pitched and rapid

---

### Question 10

Which symptom differentiates Spleen Qi Deficiency from Lung Qi Deficiency?

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q10_answer]
\```

**A)** Fatigue  
**B)** Poor appetite and loose stools  
**C)** Spontaneous sweating  
**D)** Pale complexion

---

## Submit Quiz

\```meta-bind-button
label: Submit Quiz
style: primary
action:
  type: command
  command: ocds:grade-quiz
\```

> [!tip] Before Submitting
> - Review all your answers
> - Ensure no questions are blank
> - Check your time remaining

---

## Results

**Score:** `VIEW[{score}][text]` / 10  
**Percentage:** `VIEW[{percentage}][text]`%  
**Result:** `VIEW[{pass_fail}][text]`

**Time Taken:** `VIEW[{time_taken}][text]` minutes

---

## Answer Key

<!-- This section appears after grading -->

| Question | Your Answer | Correct | Result | Explanation |
|----------|-------------|---------|--------|-------------|
| 1 | `VIEW[{q1_answer}][text]` | A | `VIEW[{q1_result}][text]` | Qi Deficiency typically shows pale, swollen tongue with tooth marks due to Spleen Qi Deficiency affecting fluid metabolism. |
| 2 | `VIEW[{q2_answer}][text]` | B | `VIEW[{q2_result}][text]` | Fatigue and weakness are cardinal symptoms of Qi Deficiency, reflecting insufficient Qi to support normal activities. |
| 3 | `VIEW[{q3_answer}][text]` | C | `VIEW[{q3_result}][text]` | Weak and empty pulse indicates Qi Deficiency, showing insufficient Qi to fill the vessels. |
| 4 | `VIEW[{q4_answer}][text]` | B | `VIEW[{q4_result}][text]` | Si Jun Zi Tang (Four Gentlemen Decoction) is the foundational formula for Spleen Qi Deficiency. |
| 5 | `VIEW[{q5_answer}][text]` | C | `VIEW[{q5_result}][text]` | Dietary irregularities and constitutional weakness are primary causes of Qi Deficiency. |
| 6 | `VIEW[{q6_answer}][text]` | C | `VIEW[{q6_result}][text]` | The Spleen is the primary organ affected in Qi Deficiency patterns, as it governs transformation and transportation. |
| 7 | `VIEW[{q7_answer}][text]` | B | `VIEW[{q7_result}][text]` | Spontaneous sweating during the day indicates Qi Deficiency, as Qi fails to secure the exterior. |
| 8 | `VIEW[{q8_answer}][text]` | B | `VIEW[{q8_result}][text]` | Tonifying Qi and strengthening the Spleen is the appropriate treatment principle for Qi Deficiency. |
| 9 | `VIEW[{q9_answer}][text]` | B | `VIEW[{q9_result}][text]` | Weak and low voice indicates Qi Deficiency, as insufficient Qi cannot support strong vocalization. |
| 10 | `VIEW[{q10_answer}][text]` | B | `VIEW[{q10_result}][text]` | Poor appetite and loose stools are specific to Spleen Qi Deficiency, while shortness of breath is more characteristic of Lung Qi Deficiency. |

---

## Next Steps

**Proceed to:** [[Week_1_Day_2_Study]]

> [!success] Congratulations!
> You've completed the Qi Deficiency quiz. Review any incorrect answers and proceed to the next lesson.

---

*Quiz generated from question bank: Materials/Question_Banks/Patterns/qi_patterns.yaml*
```

---

## 🎨 Customization Options

### Question Variations

**4 Options (Standard):**
```markdown
\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q1_answer]
\```
```

**5 Options (More Challenging):**
```markdown
\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D), option(E)):q1_answer]
\```
```

**3 Options (Simpler):**
```markdown
\```meta-bind
INPUT[select(option(A), option(B), option(C)):q1_answer]
\```
```

---

### Time Limits

**Short Quiz (5-10 questions):**
- Time limit: 10-15 minutes
- 1-1.5 minutes per question

**Medium Quiz (10-20 questions):**
- Time limit: 15-30 minutes
- 1.5 minutes per question

**Long Quiz (20+ questions):**
- Time limit: 30-45 minutes
- 1.5-2 minutes per question

---

### Passing Scores

**Lenient (60%):**
```yaml
passing_score: 6  # out of 10
```

**Standard (70%):**
```yaml
passing_score: 7  # out of 10
```

**Strict (80%):**
```yaml
passing_score: 8  # out of 10
```

---

## 🔧 Auto-Grader Integration

### Answer Key Format

Stored in quiz frontmatter (hidden from student):

```yaml
# Answer Key (not visible in rendered note)
answer_key:
  q1: "A"
  q2: "B"
  q3: "C"
  q4: "B"
  q5: "C"
  q6: "C"
  q7: "B"
  q8: "B"
  q9: "B"
  q10: "B"

# Explanations
explanations:
  q1: "Qi Deficiency typically shows pale, swollen tongue..."
  q2: "Fatigue and weakness are cardinal symptoms..."
  # ... etc
```

### Grading Logic

```python
def grade_quiz(quiz_file):
    """Grade a completed quiz."""
    fm = quiz_file.frontmatter
    
    # Check all questions answered
    for i in range(1, fm['total_questions'] + 1):
        if not fm.get(f'q{i}_answer'):
            return {'error': 'Not all questions answered'}
    
    # Calculate score
    correct = 0
    for i in range(1, fm['total_questions'] + 1):
        student_answer = fm[f'q{i}_answer']
        correct_answer = fm['answer_key'][f'q{i}']
        
        if student_answer == correct_answer:
            correct += 1
            fm[f'q{i}_result'] = '✅'
        else:
            fm[f'q{i}_result'] = '❌'
    
    # Update frontmatter
    fm['score'] = correct
    fm['percentage'] = round((correct / fm['total_questions']) * 100, 1)
    fm['pass_fail'] = 'Pass' if correct >= fm['passing_score'] else 'Fail'
    fm['status'] = 'graded'
    fm['submit_time'] = datetime.now().isoformat()
    
    # Calculate time taken
    if fm.get('start_time'):
        start = datetime.fromisoformat(fm['start_time'])
        end = datetime.fromisoformat(fm['submit_time'])
        fm['time_taken'] = round((end - start).seconds / 60, 1)
    
    # Save updated frontmatter
    save_frontmatter(quiz_file, fm)
    
    return {
        'score': correct,
        'total': fm['total_questions'],
        'percentage': fm['percentage'],
        'pass_fail': fm['pass_fail']
    }
```

---

## 💡 Best Practices

### Question Writing
- **Clear and concise** - No ambiguity
- **One correct answer** - Definitively right
- **Plausible distractors** - Wrong but reasonable
- **Avoid "all of the above"** - Too easy
- **Avoid "none of the above"** - Confusing

### Difficulty Balance
- **Easy (30%)** - Recall facts
- **Medium (50%)** - Apply knowledge
- **Hard (20%)** - Analyze and synthesize

### Answer Distribution
- **Randomize** - Don't make A always correct
- **Balance** - Each option used equally
- **No patterns** - Avoid ABCD, ABCD sequences

### Explanations
- **Always include** - Learning opportunity
- **Reference material** - Link to study notes
- **Explain why wrong** - Not just why right

---

## ✅ Quiz Checklist

Before publishing a quiz:

- [ ] All questions have 4 options
- [ ] One correct answer per question
- [ ] Answer key complete
- [ ] Explanations written
- [ ] Passing score set appropriately
- [ ] Time limit reasonable
- [ ] Frontmatter complete
- [ ] Meta-bind syntax correct
- [ ] Tested in preview mode
- [ ] Linked to task note

---

**Create effective assessments with quiz templates! 📝**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
