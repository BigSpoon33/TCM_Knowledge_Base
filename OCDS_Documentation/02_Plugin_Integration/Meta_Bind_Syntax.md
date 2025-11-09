# Meta Bind Plugin - OCDS Integration Guide

**Complete guide to using Meta Bind for OCDS interactivity**

---

## 📚 Overview

Meta Bind creates interactive forms and buttons within markdown notes by binding input fields to frontmatter. OCDS uses it for:
- Quiz answer selection
- Student information forms
- Progress dashboards
- Interactive buttons (submit, generate, etc.)
- Grade displays
- Dynamic content

**Plugin:** https://github.com/mProjectsCode/obsidian-meta-bind-plugin  
**Docs:** https://www.moritzjung.dev/obsidian-meta-bind-plugin-docs/

---

## 🎯 Why Meta Bind for OCDS?

### Key Features
- **Bind to frontmatter** - Data persists in YAML
- **Multiple input types** - Text, select, date, editor, etc.
- **View fields** - Display frontmatter values
- **Buttons** - Trigger actions and commands
- **Inline JavaScript** - Custom logic
- **No preview mode needed** - Works in edit mode

### OCDS Use Cases
- **Quiz interfaces** - Multiple choice selection
- **Student forms** - Name, ID, date of birth
- **Progress displays** - Scores, grades, completion
- **Submit buttons** - Grade quizzes, generate IDs
- **Dashboards** - Interactive progress tracking

---

## 📝 Input Fields

### Basic Syntax

```markdown
`INPUT[type(options):field_name]`
```

### 1. Text Input

**Single-line text entry**

```markdown
`INPUT[text:field_name]`
`INPUT[text(placeholder(Enter text here)):field_name]`
`INPUT[text(class(custom-class)):field_name]`
```

**Example:**
```markdown
**Patient Name:** `INPUT[text(placeholder(Enter full name)):patient_name]`
```

**Frontmatter:**
```yaml
patient_name: "John Doe"
```

---

### 2. Text Area

**Multi-line text entry**

```markdown
`INPUT[textArea:field_name]`
`INPUT[textArea(placeholder(Enter notes)):field_name]`
`INPUT[textArea(class(meta-bind-full-width)):field_name]`
```

**Example:**
```markdown
**Chief Complaint:**
`INPUT[textArea(placeholder(Describe symptoms), class(meta-bind-full-width)):chief_complaint]`
```

---

### 3. Select Dropdown

**Single selection from options**

```markdown
`INPUT[select(option(Choice 1), option(Choice 2)):field_name]`
```

**Example:**
```markdown
**Tongue Color:**
`INPUT[select(option(Pale), option(Normal), option(Red), option(Purple)):tongue_color]`
```

**With default:**
```markdown
`INPUT[select(option(Pale), option(Normal, true), option(Red)):tongue_color]`
```

---

### 4. Multi-Select

**Multiple selections**

```markdown
`INPUT[multiSelect(option(A), option(B), option(C)):field_name]`
```

**Example:**
```markdown
**Symptoms:**
`INPUT[multiSelect(option(Fatigue), option(Headache), option(Nausea)):symptoms]`
```

**Frontmatter:**
```yaml
symptoms: [Fatigue, Headache]
```

---

### 5. Date Picker

**Date selection**

```markdown
`INPUT[datePicker:field_name]`
```

**Example:**
```markdown
**Session Date:** `INPUT[datePicker:session_date]`
**Date of Birth:** `INPUT[datePicker:date_of_birth]`
```

**Frontmatter:**
```yaml
session_date: 2025-11-10
date_of_birth: 1990-05-15
```

---

### 6. Number Input

**Numeric entry**

```markdown
`INPUT[number:field_name]`
`INPUT[number(min(0), max(100)):field_name]`
```

**Example:**
```markdown
**Age:** `INPUT[number(min(0), max(120)):age]`
**Score:** `INPUT[number(min(0), max(100)):quiz_score]`
```

---

### 7. Slider

**Visual numeric selection**

```markdown
`INPUT[slider(min(0), max(100), step(1)):field_name]`
```

**Example:**
```markdown
**Pain Level (0-10):**
`INPUT[slider(min(0), max(10), step(1)):pain_level]`
```

---

### 8. Toggle

**Boolean on/off**

```markdown
`INPUT[toggle:field_name]`
`INPUT[toggle(onValue(Yes), offValue(No)):field_name]`
```

**Example:**
```markdown
**Completed:** `INPUT[toggle:task_completed]`
**Passed:** `INPUT[toggle(onValue(Pass), offValue(Fail)):quiz_passed]`
```

---

### 9. Editor Field

**Rich text editing**

```markdown
```meta-bind
INPUT[editor:field_name]
\```

```markdown
```meta-bind
INPUT[editor(class(meta-bind-full-width)):intake_notes]
\```
```

**Example:**
```markdown
**Intake Notes:**
```meta-bind
INPUT[editor(class(meta-bind-full-width)):intake_notes]
\```
```

---

## 👁️ View Fields

### Display Frontmatter Values

```markdown
`VIEW[{field_name}][text]`
`VIEW[{field_name}][math]`
`VIEW[{field_name}][link]`
```

### Examples

**Display text:**
```markdown
**Patient ID:** `VIEW[{patient_id}][text]`
**Status:** `VIEW[{status}][text]`
```

**Display number:**
```markdown
**Score:** `VIEW[{quiz_score}][math]` / 100
**Percentage:** `VIEW[{percentage}][math]`%
```

**Display link:**
```markdown
**Class:** `VIEW[{class_link}][link]`
```

---

## 🔘 Buttons

### Basic Button Syntax

```markdown
```meta-bind-button
label: Button Text
style: default | primary | destructive | plain
action:
  type: command | inlineJS | open | input | sleep | templaterCreateNote
  [action-specific parameters]
\```
```

### Button Styles

| Style | Appearance | Use Case |
|-------|------------|----------|
| `default` | Gray | Standard actions |
| `primary` | Blue | Important actions |
| `destructive` | Red | Delete/reset actions |
| `plain` | No background | Subtle actions |

---

### 1. Command Button

**Execute Obsidian command**

```markdown
```meta-bind-button
label: Start Review
style: primary
action:
  type: command
  command: spaced-repetition:review-flashcards
\```
```

**Example - Submit Quiz:**
```markdown
```meta-bind-button
label: Submit Quiz
style: primary
action:
  type: command
  command: ocds:grade-quiz
\```
```

---

### 2. Inline JavaScript Button

**Run custom JavaScript**

```markdown
```meta-bind-button
label: Generate ID
style: default
action:
  type: inlineJS
  code: |
    // JavaScript code here
    const file = app.workspace.getActiveFile();
    // ... more code
\```
```

**Example - Generate Patient ID:**
```markdown
```meta-bind-button
label: Generate Patient ID
style: default
action:
  type: inlineJS
  code: |
    const file = app.workspace.getActiveFile();
    const cache = app.metadataCache.getFileCache(file);
    const fm = cache?.frontmatter || {};
    
    const name = fm.patient_name || '';
    const dob = fm.date_of_birth || '';
    
    if (!name || !dob) {
      new Notice('Please enter name and DOB first');
      return;
    }
    
    // Get initials
    const nameParts = name.trim().split(/\s+/);
    const initials = nameParts.length >= 2 
      ? (nameParts[0][0] + nameParts[nameParts.length - 1][0]).toUpperCase()
      : nameParts[0].substring(0, 2).toUpperCase();
    
    // Format date as MMDDYY
    const date = new Date(dob);
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const year = String(date.getFullYear()).slice(-2);
    
    const patientId = initials + month + day + year;
    
    // Update frontmatter
    await app.fileManager.processFrontMatter(file, (frontmatter) => {
      frontmatter.patient_id = patientId;
    });
    
    new Notice('Patient ID generated: ' + patientId);
\```
```

---

### 3. Open Button

**Open file or URL**

```markdown
```meta-bind-button
label: Open Material
style: default
action:
  type: open
  link: "[[Study_Material]]"
\```
```

---

### 4. Input Button

**Set frontmatter value**

```markdown
```meta-bind-button
label: Mark Complete
style: primary
action:
  type: input
  str: "completed"
  bindTarget: status
\```
```

---

## 🎓 OCDS Use Cases

### 1. Quiz Interface

**Multiple choice quiz with Meta Bind:**

```markdown
---
q1_answer: ""
q2_answer: ""
q3_answer: ""
score: 0
status: "not_started"
---

# Quiz: Qi Deficiency Pattern

## Question 1
What is the primary tongue presentation for Qi Deficiency?

```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q1_answer]
\```

**A)** Pale, swollen with tooth marks  
**B)** Red with yellow coating  
**C)** Purple with dark spots  
**D)** Normal pink

---

## Question 2
Which formula is the primary treatment?

```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q2_answer]
\```

**A)** Liu Jun Zi Tang  
**B)** Si Jun Zi Tang  
**C)** Bu Zhong Yi Qi Tang  
**D)** Gui Pi Tang

---

## Submit Quiz

```meta-bind-button
label: Submit Quiz
style: primary
action:
  type: command
  command: ocds:grade-quiz
\```

---

## Results

**Score:** `VIEW[{score}][text]` / 10  
**Percentage:** `VIEW[{percentage}][text]`%  
**Status:** `VIEW[{pass_fail}][text]`
```

---

### 2. Student Information Form

```markdown
---
student_name: ""
student_id: ""
date_of_birth: ""
email: ""
---

# Student Registration

## Personal Information

**Full Name:**  
`INPUT[text(placeholder(Enter full name)):student_name]`

**Date of Birth:**  
`INPUT[datePicker:date_of_birth]`

**Email:**  
`INPUT[text(placeholder(email@example.com)):email]`

**Student ID (auto-generated):**  
`VIEW[{student_id}][text]`

```meta-bind-button
label: Generate Student ID
style: default
action:
  type: inlineJS
  code: |
    const file = app.workspace.getActiveFile();
    const cache = app.metadataCache.getFileCache(file);
    const fm = cache?.frontmatter || {};
    
    const name = fm.student_name || '';
    const dob = fm.date_of_birth || '';
    
    if (!name || !dob) {
      new Notice('Please enter name and DOB first');
      return;
    }
    
    const initials = name.split(' ').map(n => n[0]).join('').toUpperCase();
    const date = new Date(dob);
    const dateStr = date.toISOString().slice(2,10).replace(/-/g,'');
    const studentId = initials + dateStr;
    
    await app.fileManager.processFrontMatter(file, (fm) => {
      fm.student_id = studentId;
    });
    
    new Notice('Student ID: ' + studentId);
\```

## Enrollment

**Class to Enroll:**  
```meta-bind
INPUT[select(option(TCM_101), option(TCM_201), option(TCM_301)):enrolled_class]
\```

```meta-bind-button
label: Complete Registration
style: primary
action:
  type: command
  command: ocds:register-student
\```
```

---

### 3. Progress Dashboard

```markdown
---
overall_grade: 85
quizzes_completed: 8
quizzes_total: 10
flashcards_studied: 450
flashcards_total: 500
current_week: 3
total_weeks: 12
---

# Student Progress Dashboard

## Overall Performance

**Current Grade:** `VIEW[{overall_grade}][math]`%

**Progress Bar:**
```meta-bind
INPUT[progressBar(min(0), max(100)):overall_grade]
\```

## Quiz Progress

**Completed:** `VIEW[{quizzes_completed}][math]` / `VIEW[{quizzes_total}][math]`

**Completion:** `VIEW[{quiz_percentage}][math]`%

## Flashcard Progress

**Studied:** `VIEW[{flashcards_studied}][math]` / `VIEW[{flashcards_total}][math]`

**Retention Rate:** `VIEW[{retention_rate}][math]`%

## Course Progress

**Current Week:** `VIEW[{current_week}][math]` of `VIEW[{total_weeks}][math]`

```meta-bind
INPUT[progressBar(min(0), max(12)):current_week]
\```

## Actions

```meta-bind-button
label: Refresh Stats
style: default
action:
  type: command
  command: ocds:refresh-progress
\```

```meta-bind-button
label: View Detailed Report
style: primary
action:
  type: open
  link: "[[Detailed_Progress_Report]]"
\```
```

---

### 4. Task Completion Interface

```markdown
---
status: "pending"
subtask_1: false
subtask_2: false
subtask_3: false
subtask_4: false
---

# Week 1 Day 1: Study Task

## Completion Checklist

**Read study material:**  
`INPUT[toggle(onValue(true), offValue(false)):subtask_1]` `VIEW[{subtask_1}][text]`

**Take notes:**  
`INPUT[toggle(onValue(true), offValue(false)):subtask_2]` `VIEW[{subtask_2}][text]`

**Review flashcards:**  
`INPUT[toggle(onValue(true), offValue(false)):subtask_3]` `VIEW[{subtask_3}][text]`

**Complete quiz:**  
`INPUT[toggle(onValue(true), offValue(false)):subtask_4]` `VIEW[{subtask_4}][text]`

---

## Mark Complete

```meta-bind-button
label: Mark Task Complete
style: primary
action:
  type: input
  str: "completed"
  bindTarget: status
\```

**Status:** `VIEW[{status}][text]`
```

---

## 🎨 Styling

### CSS Classes

Add custom styling with classes:

```markdown
`INPUT[text(class(custom-input)):field_name]`
```

**Common OCDS classes:**
- `meta-bind-full-width` - Full width input
- `meta-bind-large` - Larger text
- `meta-bind-center` - Centered content
- `meta-bind-highlight` - Highlighted field

### Custom CSS

Add to vault's CSS snippets:

```css
/* OCDS Meta Bind Styles */
.meta-bind-full-width {
  width: 100%;
}

.meta-bind-large {
  font-size: 1.2em;
}

.meta-bind-highlight {
  background-color: rgba(255, 255, 0, 0.2);
  padding: 5px;
  border-radius: 3px;
}

.meta-bind-quiz-option {
  margin: 10px 0;
  padding: 10px;
  border: 1px solid var(--background-modifier-border);
  border-radius: 5px;
}
```

---

## 🔧 Plugin Configuration

### Recommended Settings

```
Settings → Meta Bind
├── Enable inline fields: ON
├── Enable buttons: ON
├── Enable view fields: ON
├── Sync frontmatter: ON
├── Enable JavaScript: ON
├── Show button icons: ON
└── Button click feedback: ON
```

---

## 🐛 Troubleshooting

### Fields Not Rendering

**Problem:** Input fields show as plain text

**Solutions:**
1. Ensure Meta Bind plugin is enabled
2. Switch to Reading mode (some fields only work there)
3. Check syntax is correct (backticks, brackets)
4. Refresh note (close and reopen)

### Values Not Saving

**Problem:** Input doesn't update frontmatter

**Solutions:**
1. Check field name matches frontmatter key
2. Ensure frontmatter exists (add empty field)
3. Verify YAML syntax is valid
4. Check for typos in field names

### Buttons Not Working

**Problem:** Button click does nothing

**Solutions:**
1. Check action type is correct
2. Verify command exists (for command buttons)
3. Check JavaScript syntax (for inlineJS buttons)
4. Look for errors in console (Ctrl/Cmd + Shift + I)

### JavaScript Errors

**Problem:** InlineJS button throws error

**Solutions:**
1. Check JavaScript syntax
2. Verify API calls are correct
3. Add error handling (try/catch)
4. Test code in console first

---

## 💡 Best Practices

### Field Naming
- **Use snake_case** - `patient_name` not `patientName`
- **Be descriptive** - `quiz_score` not `score`
- **Avoid spaces** - Use underscores
- **Consistent prefixes** - `q1_answer`, `q2_answer`

### Button Design
- **Clear labels** - "Submit Quiz" not "Submit"
- **Appropriate styles** - Primary for important actions
- **Confirmation** - Use notices for feedback
- **Error handling** - Check inputs before processing

### Form Layout
- **Logical grouping** - Related fields together
- **Clear labels** - Explain what to enter
- **Helpful placeholders** - Show format examples
- **Visual hierarchy** - Important fields first

### Performance
- **Limit buttons** - Too many slow down page
- **Simple JavaScript** - Complex code in scripts
- **Cache queries** - Don't repeat expensive operations
- **Test thoroughly** - Verify all interactions work

---

## ✅ Quick Reference

### Input Types
```markdown
`INPUT[text:field]`
`INPUT[textArea:field]`
`INPUT[select(option(A), option(B)):field]`
`INPUT[datePicker:field]`
`INPUT[number:field]`
`INPUT[toggle:field]`
```

### View Fields
```markdown
`VIEW[{field}][text]`
`VIEW[{field}][math]`
`VIEW[{field}][link]`
```

### Button Template
```markdown
```meta-bind-button
label: Button Text
style: primary
action:
  type: command
  command: command-id
\```
```

### Common Actions
- `type: command` - Run Obsidian command
- `type: inlineJS` - Execute JavaScript
- `type: open` - Open file/URL
- `type: input` - Set frontmatter value

---

**Create interactive experiences with Meta Bind! 🎨**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
