---
ocds_type: task
material_id: task_week01_checklist
class_id: TCM_101
week: 1
title: Week 1 Task Checklist
description: Complete all Week 1 learning activities
task_type: checklist
unlock_date: 2025-01-01
due_date: 2025-01-07
total_tasks: 8
completed_tasks: 8
completion_percentage: 100
status: completed
counts_toward_grade: true
weight: 0.1
points_possible: 10
points_earned: 10
tags:
  - tasks
  - week1
  - checklist
---

# `=this.title`

**`=this.status`**
**Due:** `=this.due_date`
**Progress:** `=this.completed_tasks`/`=this.total_tasks` `=this.completion_percentage`%
 
---

## 📋 Your Tasks for This Week

### 📚 Study & Review (Required)

- [x] **Read Study Material:** Complete [[Week 1 Study Material]] - Tongue Diagnosis 📅 2025-01-07 #study #required
  - Estimated time: 60 minutes
  - Focus on tongue body and coating characteristics
  
- [x] **Review Flashcards:** Study [[Week 1 Flashcards]] (20 cards minimum) 📅 2025-01-07 #flashcards #required
  - Use spaced repetition
  - Aim for 80%+ accuracy
  
- [x] **Watch Lecture:** View [[Week 1 Lecture Slides]] 📅 2025-01-07 #lecture

---

### ✍️ Assessments (Required)

- [x] **Complete Quiz:** Take [[Week 1 Quiz]] - Tongue Diagnosis 📅 2025-01-07 ⏫ #quiz #required
  - Minimum score: 70%
  - 10 questions, multiple choice
  - 3 attempts allowed
  
- [x] **Submit Homework:** Complete [[Week 1 Homework]] - Tongue Case Studies 📅 2025-01-12 ⏫ #homework #required
  - Analyze 3 tongue images
  - Due: January 12, 2025
  - Worth 20 points

---

### 🎯 Practice & Engagement (Optional - Bonus Points)

- [x] **Practice Session:** Spend 30 minutes identifying tongue patterns 📅 2025-01-07 #practice #bonus
  - Use practice images in study materials
  - Bonus: +1 point
  
- [x] **Discussion Forum:** Post in Week 1 Discussion 📅 2025-01-07 #discussion #bonus
  - Share insights or questions
  - Respond to one classmate
  - Bonus: +1 point
  
- [x] **Pomodoro Sessions:** Complete 2 focused study sessions 📅 2025-01-07 #pomodoro #bonus
  - Use 25-minute Pomodoro technique
  - Track in study log
  - Bonus: +1 point

---

## 📊 Progress Tracking

```dataviewjs
// Count completed tasks dynamically
const file = dv.current().file;
const content = await dv.io.load(file.path);
const lines = content.split('\n');

let totalTasks = 0;
let completedTasks = 0;

// Count checkboxes in the task sections
for (const line of lines) {
  if (line.match(/^- \[[ x]\]/)) {
    totalTasks++;
    if (line.match(/^- \[x\]/)) {
      completedTasks++;
    }
  }
}

const percentage = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;

// Update frontmatter
const currentFile = app.workspace.getActiveFile();
if (currentFile) {
  await app.fileManager.processFrontMatter(currentFile, (fm) => {
    fm.completed_tasks = completedTasks;
    fm.total_tasks = totalTasks;
    fm.completion_percentage = percentage;
    fm.status = completedTasks === 0 ? 'not_started' : 
                completedTasks === totalTasks ? 'completed' : 'in_progress';
    fm.points_earned = completedTasks === totalTasks ? 10 : Math.floor((completedTasks / totalTasks) * 10);
  });
}

// Display progress
dv.header(3, "Progress");
dv.paragraph(`**Completed:** ${completedTasks} / ${totalTasks} tasks (${percentage}%)`);
dv.paragraph(`**Status:** ${completedTasks === 0 ? 'Not Started' : completedTasks === totalTasks ? 'Completed ✅' : 'In Progress 🔄'}`);
dv.paragraph(`**Points Earned:** ${completedTasks === totalTasks ? 10 : Math.floor((completedTasks / totalTasks) * 10)} / 10`);

// Progress bar visualization
const barWidth = 30;
const filledBars = Math.round((completedTasks / totalTasks) * barWidth);
const emptyBars = barWidth - filledBars;
const progressBar = '█'.repeat(filledBars) + '░'.repeat(emptyBars);
dv.paragraph(`\`${progressBar}\` ${percentage}%`);
```

---

## ✅ How to Complete Tasks

1. Click the checkbox next to each task as you complete it
2. Progress updates automatically
3. Complete all required tasks (5 tasks) = 7 points
4. Complete optional tasks = +1 point each (up to 3 bonus points)
5. Maximum possible: 10 points

---

## 💡 Tips for Success

- ✅ Start early - don't wait until the last day
- ✅ Follow the order: Study → Flashcards → Quiz → Homework
- ✅ Use active learning - don't just read passively
- ✅ Practice regularly - short daily sessions > cramming
- ✅ Ask questions if stuck

---

```meta-bind-button
label: Refresh Progress
style: default
action:
  type: command
  command: dataview:dataview-force-refresh-views
```

```meta-bind-button
label: View Dashboard
style: primary
action:
  type: open
  link: "[[Student Dashboard]]"
```
