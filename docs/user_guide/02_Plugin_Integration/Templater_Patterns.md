# Templater Plugin - OCDS Integration Guide

**Complete guide to using Templater for OCDS automation**

---

## 📚 Overview

Templater is a powerful template engine that allows dynamic content generation using JavaScript. OCDS uses it for:
- Material generation from templates
- Task creation automation
- Dynamic date calculations
- Content customization
- Batch operations

**Plugin:** https://github.com/SilentVoid13/Templater  
**Docs:** https://silentvoid13.github.io/Templater/

---

## 🎯 Why Templater for OCDS?

### Key Features
- **JavaScript execution** - Full programming power
- **Template variables** - Dynamic content
- **Date manipulation** - Relative dates
- **File operations** - Create, move, rename
- **User input** - Prompts and selections
- **System commands** - Execute scripts

### OCDS Use Cases
- **Task generation** - Create daily/weekly tasks
- **Material customization** - Student-specific content
- **Date calculations** - Due dates, schedules
- **Batch creation** - Generate multiple files
- **Content templating** - Reusable structures

---

## 📝 Basic Syntax

### Template Variables

```markdown
<% tp.file.title %>
<% tp.date.now("YYYY-MM-DD") %>
<% tp.file.folder() %>
```

### Execution Tags

- `<% %>` - Execute code (no output)
- `<%= %>` - Execute and output result
- `<%* %>` - Execute JavaScript block

---

## 📅 Date Functions

### Current Date/Time

```markdown
Today: <% tp.date.now("YYYY-MM-DD") %>
Now: <% tp.date.now("YYYY-MM-DD HH:mm:ss") %>
Tomorrow: <% tp.date.tomorrow("YYYY-MM-DD") %>
Yesterday: <% tp.date.yesterday("YYYY-MM-DD") %>
```

### Relative Dates

```markdown
# 7 days from now
<% tp.date.now("YYYY-MM-DD", 7) %>

# 3 days ago
<% tp.date.now("YYYY-MM-DD", -3) %>

# 2 weeks from now
<% tp.date.now("YYYY-MM-DD", 14) %>
```

### Custom Date Formats

```markdown
<% tp.date.now("MMM DD, YYYY") %>  # Nov 05, 2025
<% tp.date.now("dddd, MMMM D") %>  # Tuesday, November 5
<% tp.date.now("YYYY-MM-DD HH:mm") %>  # 2025-11-05 14:30
```

---

## 📂 File Functions

### File Information

```markdown
Title: <% tp.file.title %>
Path: <% tp.file.path() %>
Folder: <% tp.file.folder() %>
Created: <% tp.file.creation_date("YYYY-MM-DD") %>
```

### File Operations

```markdown
<%* 
// Create new file
await tp.file.create_new("New Note", "Folder/Path")

// Move file
await tp.file.move("/New/Path/Note")

// Rename file
await tp.file.rename("New Name")
%>
```

---

## 💬 User Input

### Prompt for Input

```markdown
<%* 
const studentName = await tp.system.prompt("Enter student name");
const classId = await tp.system.prompt("Enter class ID");
%>

Student: <%= studentName %>
Class: <%= classId %>
```

### Suggester (Dropdown)

```markdown
<%*
const classes = ["TCM_101", "TCM_201", "TCM_301"];
const selectedClass = await tp.system.suggester(classes, classes);
%>

Selected: <%= selectedClass %>
```

---

## 🎓 OCDS Templates

### 1. Task Note Template

```markdown
---
status: pending
priority: normal
scheduled: <% tp.date.now("YYYY-MM-DD") %>
due: <% tp.date.now("YYYY-MM-DD", 1) %>
dateCreated: <% tp.date.now("YYYY-MM-DDTHH:mm:ss.SSSZ") %>
dateModified: <% tp.date.now("YYYY-MM-DDTHH:mm:ss.SSSZ") %>
tags:
  - task
  - <% tp.file.folder(true).split("/").pop() %>
contexts:
  - study
projects:
  - "[[<% tp.file.folder(true).split("/").pop() %>]]"
estimated_minutes: 60
---

# <% tp.file.title %>

## Task Details

**Scheduled:** <% tp.date.now("YYYY-MM-DD") %>
**Due:** <% tp.date.now("YYYY-MM-DD", 1) %>

## Objectives

- [ ] Objective 1
- [ ] Objective 2
- [ ] Objective 3

## Materials

- [[Material 1]]
- [[Material 2]]

## Instructions

1. Step 1
2. Step 2
3. Step 3

## Completion Criteria

- [ ] All objectives met
- [ ] Materials reviewed
- [ ] Task marked complete
```

---

### 2. Quiz Generation Template

```markdown
<%*
const topic = await tp.system.prompt("Enter quiz topic");
const week = await tp.system.prompt("Enter week number");
const day = await tp.system.prompt("Enter day number");
const questions = await tp.system.prompt("Number of questions", "10");
%>
---
type: quiz
class_id: "<% tp.file.folder(true).split("/")[0] %>"
week: <%= week %>
day: <%= day %>
topic: "<%= topic %>"
total_questions: <%= questions %>
passing_score: <%= Math.ceil(questions * 0.7) %>
time_limit_minutes: <%= questions * 1.5 %>
status: "not_started"
quiz_date: ""
score: 0
percentage: 0
tags:
  - quiz
  - <% tp.file.folder(true).split("/")[0] %>
  - week_<%= week %>
---

# Quiz: <%= topic %>

**Week <%= week %>, Day <%= day %>**

> [!info] Quiz Information
> - **Questions:** <%= questions %>
> - **Passing Score:** <%= Math.ceil(questions * 0.7) %>/<%= questions %> (70%)
> - **Time Limit:** <%= questions * 1.5 %> minutes

---

## Instructions

1. Read each question carefully
2. Select ONE answer per question
3. Click "Submit Quiz" when complete

---

<%* for (let i = 1; i <= questions; i++) { %>
### Question <%= i %>

[Question text here]

\```meta-bind
INPUT[select(option(A), option(B), option(C), option(D)):q<%= i %>_answer]
\```

**A)** Option A
**B)** Option B
**C)** Option C
**D)** Option D

---

<%* } %>

## Submit Quiz

\```meta-bind-button
label: Submit Quiz
style: primary
action:
  type: command
  command: ocds:grade-quiz
\```
```

---

### 3. Weekly Task Batch Generator

```markdown
<%*
const classId = await tp.system.prompt("Enter class ID");
const week = await tp.system.prompt("Enter week number");
const startDate = await tp.system.prompt("Enter start date (YYYY-MM-DD)");

const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

for (let day = 1; day <= 7; day++) {
    const taskDate = tp.date.now("YYYY-MM-DD", day - 1, startDate);
    const dayName = days[day - 1];
    
    const taskContent = `---
status: pending
priority: normal
scheduled: ${taskDate}
due: ${taskDate}
tags:
  - task
  - ${classId}
  - week_${week}
  - day_${day}
---

# Week ${week} Day ${day}: ${dayName}

## Task Details

**Date:** ${taskDate}

## Materials

- Study material
- Flashcards
- Quiz (if applicable)

## Instructions

1. Complete study material
2. Review flashcards
3. Take quiz if scheduled
`;

    await tp.file.create_new(
        taskContent,
        `Week_${week}_Day_${day}_${dayName}`,
        false,
        `TaskNotes/${classId}/Week_${week}`
    );
}
%>

✅ Generated 7 tasks for Week <%= week %>
```

---

### 4. Student Progress Template

```markdown
<%*
const studentName = await tp.system.prompt("Enter student name");
const studentId = await tp.system.prompt("Enter student ID");
const classId = await tp.system.prompt("Enter class ID");
const startDate = await tp.system.prompt("Enter class start date (YYYY-MM-DD)");
%>
---
type: progress
student_name: "<%= studentName %>"
student_id: "<%= studentId %>"
class_id: "<%= classId %>"
start_date: "<%= startDate %>"
current_week: 1
total_weeks: 12
overall_grade: 0
status: "in_progress"
---

# <%= studentName %> - <%= classId %> Progress

**Student ID:** <%= studentId %>
**Start Date:** <%= startDate %>

---

## Overall Performance

**Current Week:** `VIEW[{current_week}][text]` / `VIEW[{total_weeks}][text]`

**Overall Grade:** `VIEW[{overall_grade}][text]`%

---

## Quiz Scores

\```dataview
TABLE
  week as "Week",
  quiz_score as "Score",
  percentage as "%"
FROM "Classes/<%= classId %>/Quizzes"
WHERE student_id = "<%= studentId %>"
SORT week ASC
\```

---

## Flashcard Progress

**Cards Studied:** `VIEW[{flashcards_studied}][text]`
**Retention Rate:** `VIEW[{retention_rate}][text]`%

---

## Time Tracking

**Total Study Time:** `VIEW[{total_study_minutes}][text]` minutes

---

*Progress tracking started: <% tp.date.now("YYYY-MM-DD") %>*
```

---

### 5. Material Import Template

```markdown
<%*
const materialType = await tp.system.suggester(
    ["Study Material", "Flashcards", "Quiz", "Homework", "Slides"],
    ["study", "flashcards", "quiz", "homework", "slides"]
);

const sourcePath = await tp.system.prompt("Enter source material path");
const week = await tp.system.prompt("Enter week number");
const day = await tp.system.prompt("Enter day number");

// Read source material
const sourceFile = app.vault.getAbstractFileByPath(sourcePath);
const sourceContent = await app.vault.read(sourceFile);

// Add OCDS frontmatter
const newContent = `---
type: ${materialType}
class_id: "<% tp.file.folder(true).split("/")[0] %>"
week: ${week}
day: ${day}
imported_from: "${sourcePath}"
imported_date: "<% tp.date.now("YYYY-MM-DD") %>"
---

${sourceContent}
`;

// Output new content
%>
<%= newContent %>
```

---

## 🔄 Advanced Patterns

### 1. Conditional Content

```markdown
<%*
const difficulty = await tp.system.suggester(
    ["Beginner", "Intermediate", "Advanced"],
    ["beginner", "intermediate", "advanced"]
);
%>

# Study Material

<% if (difficulty === "beginner") { %>
## Beginner Content
Basic introduction and fundamentals
<% } else if (difficulty === "intermediate") { %>
## Intermediate Content
More detailed analysis and application
<% } else { %>
## Advanced Content
Complex concepts and clinical integration
<% } %>
```

---

### 2. Loop Through Data

```markdown
<%*
const topics = ["Qi Deficiency", "Blood Deficiency", "Yin Deficiency", "Yang Deficiency"];

for (const topic of topics) {
%>
## <%= topic %>

Brief description of <%= topic %>

[[<%= topic.replace(" ", "_") %>]]

---

<%* } %>
```

---

### 3. Calculate Dates

```markdown
<%*
const startDate = "2025-11-10";
const weeks = 12;

for (let week = 1; week <= weeks; week++) {
    const weekStart = tp.date.now("YYYY-MM-DD", (week - 1) * 7, startDate);
    const weekEnd = tp.date.now("YYYY-MM-DD", week * 7 - 1, startDate);
%>
**Week <%= week %>:** <%= weekStart %> to <%= weekEnd %>
<%* } %>
```

---

### 4. Dynamic File Creation

```markdown
<%*
const classId = "TCM_101";
const materials = [
    { name: "Qi Deficiency", week: 1, day: 1 },
    { name: "Blood Deficiency", week: 1, day: 2 },
    { name: "Yin Deficiency", week: 1, day: 3 }
];

for (const material of materials) {
    const content = `---
type: study
class_id: "${classId}"
week: ${material.week}
day: ${material.day}
---

# ${material.name}

Study material content here...
`;

    await tp.file.create_new(
        content,
        `${material.name.replace(" ", "_")}`,
        false,
        `Classes/${classId}/Week_${material.week}`
    );
}
%>

✅ Created <%= materials.length %> study materials
```

---

## 🔧 Plugin Configuration

### Recommended Settings

```
Settings → Templater
├── Template folder: "OCDS_Templates"
├── Trigger on file creation: ON
├── Enable system commands: ON
├── Enable folder templates: ON
├── Folder templates:
│   ├── TaskNotes/ → Task_Template.md
│   ├── Quizzes/ → Quiz_Template.md
│   └── Progress/ → Progress_Template.md
```

---

## 💡 Best Practices

### Template Organization
- **Separate folder** - Keep templates in `OCDS_Templates/`
- **Clear naming** - `Task_Template.md`, `Quiz_Template.md`
- **Documentation** - Comment complex logic
- **Reusable** - Make templates generic

### Error Handling
```markdown
<%*
try {
    const result = await someOperation();
} catch (error) {
    console.error("Error:", error);
    tR += "Error occurred. Please try again.";
}
%>
```

### User Experience
- **Clear prompts** - Explain what to enter
- **Default values** - Provide sensible defaults
- **Validation** - Check inputs before processing
- **Feedback** - Confirm actions completed

---

## 🔗 Integration with OCDS

### With Import Script

```python
# import_class.py
def generate_task_from_template(template_path, variables):
    """Generate task using Templater."""
    # Read template
    with open(template_path) as f:
        template = f.read()
    
    # Replace variables
    for key, value in variables.items():
        template = template.replace(f"<% {key} %>", str(value))
    
    return template
```

### With Auto-Grader

```markdown
<%*
// After quiz graded, generate next task
if (tp.frontmatter.pass_fail === "Pass") {
    const nextWeek = tp.frontmatter.week + 1;
    await tp.file.create_new(
        "Next week task content",
        `Week_${nextWeek}_Day_1`,
        false,
        "TaskNotes"
    );
}
%>
```

---

## 🐛 Troubleshooting

### Template Not Executing

**Problem:** Template code shows as text

**Solutions:**
1. Ensure Templater plugin is enabled
2. Check syntax: `<% %>` not `< %>`
3. Verify template folder is set
4. Restart Obsidian

### Dates Not Calculating

**Problem:** Date functions return errors

**Solutions:**
1. Check date format string
2. Verify offset is number
3. Use valid moment.js formats
4. Test with simple example first

### File Creation Fails

**Problem:** `create_new` doesn't work

**Solutions:**
1. Check folder path exists
2. Verify file name is valid
3. Ensure no duplicate names
4. Check permissions

---

## ✅ Quick Reference

### Date Functions
```markdown
<% tp.date.now("YYYY-MM-DD") %>
<% tp.date.now("YYYY-MM-DD", 7) %>  # +7 days
<% tp.date.tomorrow("YYYY-MM-DD") %>
```

### File Functions
```markdown
<% tp.file.title %>
<% tp.file.folder() %>
<% tp.file.path() %>
```

### User Input
```markdown
<%* const input = await tp.system.prompt("Question"); %>
<%* const choice = await tp.system.suggester(options, values); %>
```

### Execution
```markdown
<% %>   # Execute, no output
<%= %>  # Execute and output
<%* %>  # JavaScript block
```

---

## 📚 Related Documentation

- **Material Templates:** `../05_Material_Templates/`
- **Automation Scripts:** `../06_Automation_Scripts/`
- **Task Template:** `../05_Material_Templates/Task_Template.md`

---

**Automate content creation with Templater! ⚡**

---

*Last updated: 2025-11-05*  
*OCDS Version: 1.0.0*
