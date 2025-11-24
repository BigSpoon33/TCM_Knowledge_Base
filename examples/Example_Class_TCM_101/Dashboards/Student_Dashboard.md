---
ocds_type: dashboard
class_id: TCM_101
dashboard_type: student
student_id: example_student
last_updated: 2025-11-06
student_name: Example Student
enrollment_date: 2025-01-01
current_week: 1
target_completion: 2025-03-25
overall_grade: 0
quiz_average: 0
homework_average: 0
flashcard_completion: 0
task_completion: 0
tags:
  - dashboard
  - student
  - progress
total_cards: 22
card_count: 22
cards_reviewed: 21
cards_mastered: 21
last_review_date: 2025-11-07
completed_tasks: 8
total_tasks: 8
completion_percentage: 100
status: completed
points_earned: 10
---

# TCM 101 - Student Dashboard

```dataviewjs
const fm = dv.current();
dv.paragraph(`**Student:** ${fm.student_name}`);
dv.paragraph(`**Enrolled:** ${fm.enrollment_date}`);
dv.paragraph(`**Current Week:** Week ${fm.current_week} of 12`);
dv.paragraph(`**Overall Grade:** ${fm.overall_grade}%`);
```

> [!info] How to Use This Dashboard
> - **Quizzes:** Check answer boxes, click "Submit Quiz" to auto-grade
> - **Homework:** Click "Submit Homework" button to mark as submitted (instructor grades manually)
> - **Tasks:** Check off tasks in the Tasks file - progress updates automatically
> - **Flashcards:** Use Spaced Repetition plugin (Ctrl/Cmd+P → "Review flashcards")
> - **Dashboard Updates:** Refresh this page to see latest progress

---

## 🎯 Quick Actions

```meta-bind-button
label: 📚 Continue Learning
style: primary
action:
  type: open
  link: "[[Materials/Week_01/Study_Material]]"
```

```meta-bind-button
label: 🎴 Review Flashcards
style: default
action:
  type: open
  link: "[[Materials/Week_01/Flashcards]]"
```

```meta-bind-button
label: ✅ View Tasks
style: default
action:
  type: open
  link: "[[Materials/Week_01/Tasks]]"
```

```meta-bind-button
label: 📝 Take Quiz
style: default
action:
  type: open
  link: "[[Materials/Week_01/Quiz]]"
```

---

## 📊 Overall Progress

```dataviewjs
// Calculate overall progress across all materials
const classFolder = "OCDS_Documentation/Example_Class_TCM_101/Materials";

// Get all materials
const quizzes = dv.pages(`"${classFolder}"`)
  .where(p => p.ocds_type === "quiz");
const homework = dv.pages(`"${classFolder}"`)
  .where(p => p.ocds_type === "homework");
const tasks = dv.pages(`"${classFolder}"`)
  .where(p => p.ocds_type === "task");
const flashcards = dv.pages(`"${classFolder}"`)
  .where(p => p.ocds_type === "flashcard");

// Calculate completion
const quizCount = quizzes.length;
const quizCompleted = quizzes.where(q => q.score !== null && q.score !== undefined).length;
const quizPercent = quizCount > 0 ? Math.round((quizCompleted / quizCount) * 100) : 0;

const hwCount = homework.length;
const hwCompleted = homework.where(h => h.submission_status === "graded").length;
const hwPercent = hwCount > 0 ? Math.round((hwCompleted / hwCount) * 100) : 0;

const taskCount = tasks.length;
const taskCompleted = tasks.where(t => t.status === "completed").length;
const taskPercent = taskCount > 0 ? Math.round((taskCompleted / taskCount) * 100) : 0;

const flashcardCount = flashcards.length;
// Calculate flashcard completion based on percentage reviewed (>= 80% = complete)
const flashcardCompleted = flashcards.where(f => {
  const total = f.total_cards || f.card_count || 0;
  const reviewed = f.cards_reviewed || 0;
  return total > 0 && (reviewed / total) >= 0.8;
}).length;
const flashcardPercent = flashcardCount > 0 ? Math.round((flashcardCompleted / flashcardCount) * 100) : 0;

// Display summary
dv.header(3, "📈 Completion Summary");

dv.table(
  ["Component", "Completed", "Total", "Progress", "Status"],
  [
    ["📝 Quizzes", quizCompleted, quizCount, `${quizPercent}%`, quizPercent >= 70 ? "✅" : "🔄"],
    ["📄 Homework", hwCompleted, hwCount, `${hwPercent}%`, hwPercent >= 70 ? "✅" : "🔄"],
    ["✅ Tasks", taskCompleted, taskCount, `${taskPercent}%`, taskPercent >= 70 ? "✅" : "🔄"],
    ["🎴 Flashcards", flashcardCompleted, flashcardCount, `${flashcardPercent}%`, flashcardPercent >= 70 ? "✅" : "🔄"]
  ]
);

// Overall completion
const overallPercent = Math.round((quizPercent * 0.4) + (hwPercent * 0.2) + (taskPercent * 0.1) + (flashcardPercent * 0.3));

dv.paragraph(`**Overall Progress:** ${overallPercent}%`);

// Progress bar
const barWidth = 40;
const filledBars = Math.round((overallPercent / 100) * barWidth);
const emptyBars = barWidth - filledBars;
const progressBar = '█'.repeat(filledBars) + '░'.repeat(emptyBars);
dv.paragraph(`\`${progressBar}\` ${overallPercent}%`);
```

---

## 📅 Week 1 Progress

```dataviewjs
// Week 1 specific progress
const week1Folder = "OCDS_Documentation/Example_Class_TCM_101/Materials/Week_01";

const week1Materials = dv.pages(`"${week1Folder}"`);

dv.header(3, "Week 1: Tongue Diagnosis");

dv.table(
  ["Material", "Type", "Status", "Score/Progress", "Action"],
  week1Materials.map(m => {
    let status = "Not Started";
    let progress = "-";
    let action = "Start";
    
    if (m.ocds_type === "quiz") {
      if (m.score !== null && m.score !== undefined) {
        status = m.score >= 7 ? "✅ Passed" : "⚠️ Needs Retake";
        progress = `${m.score}/10 (${Math.round(m.score/10*100)}%)`;
        action = m.score >= 7 ? "Review" : "Retake";
      } else if (m.attempts > 0) {
        status = "🔄 In Progress";
        progress = `Attempt ${m.attempts}/3`;
        action = "Continue";
      }
    } else if (m.ocds_type === "homework") {
      if (m.submission_status === "graded") {
        status = "✅ Graded";
        progress = m.score ? `${m.score}/${m.points_possible}` : "-";
        action = "View Feedback";
      } else if (m.submission_status === "submitted") {
        status = "⏳ Pending";
        progress = "Awaiting grade";
        action = "Wait";
      } else if (m.submission_status === "in_progress") {
        status = "🔄 In Progress";
        progress = "-";
        action = "Continue";
      }
    } else if (m.ocds_type === "task") {
      status = m.status === "completed" ? "✅ Complete" : 
               m.status === "in_progress" ? "🔄 In Progress" : "Not Started";
      progress = `${m.completed_tasks || 0}/${m.total_tasks || 0}`;
      action = m.status === "completed" ? "Review" : "Continue";
    } else if (m.ocds_type === "flashcard") {
      const reviewed = m.cards_reviewed || 0;
      const total = m.total_cards || m.card_count || 0;
      const percent = total > 0 ? (reviewed / total) * 100 : 0;
      status = percent >= 80 ? "✅ Complete" : reviewed > 0 ? "🔄 In Progress" : "Not Started";
      progress = `${reviewed}/${total} cards (${Math.round(percent)}%)`;
      action = percent >= 80 ? "Review" : "Study";
    } else if (m.ocds_type === "study_material") {
      status = "📖 Available";
      progress = "-";
      action = "Read";
    }
    
    return [
      `[[${m.file.name}|${m.title || m.file.name}]]`,
      m.ocds_type || "material",
      status,
      progress,
      action
    ];
  })
);
```

---

## 📝 Quiz Performance

```dataviewjs
const quizzes = dv.pages('"OCDS_Documentation/Example_Class_TCM_101/Materials"')
  .where(p => p.ocds_type === "quiz");

if (quizzes.length > 0) {
  dv.header(3, "Quiz Scores");
  
  dv.table(
    ["Quiz", "Week", "Score", "Percentage", "Attempts", "Status"],
    quizzes.map(q => [
      `[[${q.file.name}|${q.title}]]`,
      q.week || "-",
      q.score !== null && q.score !== undefined ? `${q.score}/${q.points_possible || 10}` : "-",
      q.score !== null && q.score !== undefined ? `${Math.round((q.score / (q.points_possible || 10)) * 100)}%` : "-",
      `${q.attempts || 0}/${q.max_attempts || 3}`,
      q.score >= 7 ? "✅ Pass" : q.attempts > 0 ? "⚠️ Retry" : "Not Started"
    ])
  );
  
  // Calculate average
  const gradedQuizzes = quizzes.where(q => q.score !== null && q.score !== undefined);
  if (gradedQuizzes.length > 0) {
    const quizArray = Array.from(gradedQuizzes);
    const avgScore = quizArray.map(q => q.score).reduce((a, b) => a + b, 0) / quizArray.length;
    const avgPercent = Math.round((avgScore / 10) * 100);
    dv.paragraph(`**Quiz Average:** ${avgScore.toFixed(1)}/10 (${avgPercent}%)`);
  }
} else {
  dv.paragraph("No quizzes available yet.");
}
```

---

## 📄 Homework Assignments

```dataviewjs
const homework = dv.pages('"OCDS_Documentation/Example_Class_TCM_101/Materials"')
  .where(p => p.ocds_type === "homework");

if (homework.length > 0) {
  dv.header(3, "Assignments");
  
  dv.table(
    ["Assignment", "Week", "Due Date", "Status", "Score", "Submitted"],
    homework.map(h => [
      `[[${h.file.name}|${h.title}]]`,
      h.week || "-",
      h.due_date || "-",
      h.submission_status === "graded" ? "✅ Graded" :
      h.submission_status === "submitted" ? "⏳ Pending" :
      h.submission_status === "in_progress" ? "🔄 In Progress" : "Not Started",
      h.score !== null && h.score !== undefined ? `${h.score}/${h.points_possible}` : "-",
      h.submitted_date || "-"
    ])
  );
  
  // Calculate average
  const gradedHW = homework.where(h => h.score !== null && h.score !== undefined);
  if (gradedHW.length > 0) {
    const hwArray = Array.from(gradedHW);
    const totalScore = hwArray.map(h => h.score).reduce((a, b) => a + b, 0);
    const totalPossible = hwArray.map(h => h.points_possible || 20).reduce((a, b) => a + b, 0);
    const avgPercent = Math.round((totalScore / totalPossible) * 100);
    dv.paragraph(`**Homework Average:** ${totalScore}/${totalPossible} (${avgPercent}%)`);
  }
} else {
  dv.paragraph("No homework assignments available yet.");
}
```

---

## ✅ Task Completion

```dataviewjs
const tasks = dv.pages('"OCDS_Documentation/Example_Class_TCM_101/Materials"')
  .where(p => p.ocds_type === "task");

if (tasks.length > 0) {
  dv.header(3, "Weekly Tasks");
  
  dv.table(
    ["Week", "Tasks", "Completed", "Progress", "Points", "Status"],
    tasks.map(t => {
      const percent = t.completion_percentage || 0;
      const barWidth = 20;
      const filled = Math.round((percent / 100) * barWidth);
      const empty = barWidth - filled;
      const bar = '█'.repeat(filled) + '░'.repeat(empty);
      
      return [
        `[[${t.file.name}|Week ${t.week}]]`,
        t.total_tasks || 0,
        t.completed_tasks || 0,
        `\`${bar}\` ${percent}%`,
        `${t.points_earned || 0}/${t.points_possible || 10}`,
        t.status === "completed" ? "✅" : t.status === "in_progress" ? "🔄" : "⏸️"
      ];
    })
  );
  
  // Calculate total task points
  const taskArray = Array.from(tasks);
  const totalEarned = taskArray.length > 0
    ? taskArray.map(t => t.points_earned || 0).reduce((a, b) => a + b, 0)
    : 0;
  const totalPossible = taskArray.length > 0
    ? taskArray.map(t => t.points_possible || 10).reduce((a, b) => a + b, 0)
    : 0;
  const taskPercent = totalPossible > 0 ? Math.round((totalEarned / totalPossible) * 100) : 0;
  dv.paragraph(`**Task Points:** ${totalEarned}/${totalPossible} (${taskPercent}%)`);
} else {
  dv.paragraph("No tasks available yet.");
}
```

---

## 🎴 Flashcard Progress

```dataviewjs
const flashcards = dv.pages('"OCDS_Documentation/Example_Class_TCM_101/Materials"')
  .where(p => p.ocds_type === "flashcard");

if (flashcards.length > 0) {
  dv.header(3, "Spaced Repetition");
  
  dv.table(
    ["Deck", "Week", "Total Cards", "Reviewed", "Mastered", "Progress"],
    flashcards.map(f => {
      const reviewed = f.cards_reviewed || 0;
      const total = f.total_cards || 0;
      const percent = total > 0 ? Math.round((reviewed / total) * 100) : 0;
      const barWidth = 20;
      const filled = Math.round((percent / 100) * barWidth);
      const empty = barWidth - filled;
      const bar = '█'.repeat(filled) + '░'.repeat(empty);
      
      return [
        `[[${f.file.name}|${f.title}]]`,
        f.week || "-",
        total,
        reviewed,
        f.cards_mastered || 0,
        `\`${bar}\` ${percent}%`
      ];
    })
  );
  
  // Calculate total flashcard progress
  const flashcardArray = Array.from(flashcards);
  const totalCards = flashcardArray.length > 0 
    ? flashcardArray.map(f => f.total_cards || 0).reduce((a, b) => a + b, 0)
    : 0;
  const totalReviewed = flashcardArray.length > 0
    ? flashcardArray.map(f => f.cards_reviewed || 0).reduce((a, b) => a + b, 0)
    : 0;
  const flashcardPercent = totalCards > 0 ? Math.round((totalReviewed / totalCards) * 100) : 0;
  dv.paragraph(`**Overall Flashcard Progress:** ${totalReviewed}/${totalCards} cards (${flashcardPercent}%)`);
} else {
  dv.paragraph("No flashcard decks available yet.");
}
```

---

## 📈 Grade Breakdown

```dataviewjs
dv.header(3, "Current Grade Calculation");

// Get all materials
const classFolder = "OCDS_Documentation/Example_Class_TCM_101/Materials";
const quizzes = dv.pages(`"${classFolder}"`).where(p => p.ocds_type === "quiz");
const homework = dv.pages(`"${classFolder}"`).where(p => p.ocds_type === "homework");
const tasks = dv.pages(`"${classFolder}"`).where(p => p.ocds_type === "task");
const flashcards = dv.pages(`"${classFolder}"`).where(p => p.ocds_type === "flashcard");

// Calculate component averages
const gradedQuizzes = quizzes.where(q => q.score !== null && q.score !== undefined);
const quizArray = Array.from(gradedQuizzes);
const quizAvg = quizArray.length > 0 
  ? quizArray.map(q => (q.score / (q.points_possible || 10)) * 100).reduce((a, b) => a + b, 0) / quizArray.length 
  : 0;

const gradedHW = homework.where(h => h.score !== null && h.score !== undefined);
const hwArray = Array.from(gradedHW);
const hwAvg = hwArray.length > 0
  ? hwArray.map(h => (h.score / (h.points_possible || 20)) * 100).reduce((a, b) => a + b, 0) / hwArray.length
  : 0;

// Convert to arrays and calculate task points
const taskArray = Array.from(tasks);
const totalTaskPoints = taskArray.length > 0 
  ? taskArray.map(t => t.points_earned || 0).reduce((a, b) => a + b, 0)
  : 0;
const totalTaskPossible = taskArray.length > 0
  ? taskArray.map(t => t.points_possible || 10).reduce((a, b) => a + b, 0)
  : 0;
const taskAvg = totalTaskPossible > 0 ? (totalTaskPoints / totalTaskPossible) * 100 : 0;

// Convert to arrays and calculate flashcard progress
const flashcardArray = Array.from(flashcards);
const totalFlashcards = flashcardArray.length > 0
  ? flashcardArray.map(f => f.total_cards || 0).reduce((a, b) => a + b, 0)
  : 0;
const totalReviewed = flashcardArray.length > 0
  ? flashcardArray.map(f => f.cards_reviewed || 0).reduce((a, b) => a + b, 0)
  : 0;
const flashcardAvg = totalFlashcards > 0 ? (totalReviewed / totalFlashcards) * 100 : 0;

// Calculate weighted grade
const quizWeight = 0.40;
const hwWeight = 0.20;
const taskWeight = 0.10;
const flashcardWeight = 0.30;

const weightedQuiz = quizAvg * quizWeight;
const weightedHW = hwAvg * hwWeight;
const weightedTask = taskAvg * taskWeight;
const weightedFlashcard = flashcardAvg * flashcardWeight;

const overallGrade = weightedQuiz + weightedHW + weightedTask + weightedFlashcard;

// Determine letter grade
let letterGrade = "F";
if (overallGrade >= 93) letterGrade = "A";
else if (overallGrade >= 90) letterGrade = "A-";
else if (overallGrade >= 87) letterGrade = "B+";
else if (overallGrade >= 83) letterGrade = "B";
else if (overallGrade >= 80) letterGrade = "B-";
else if (overallGrade >= 77) letterGrade = "C+";
else if (overallGrade >= 73) letterGrade = "C";
else if (overallGrade >= 70) letterGrade = "C-";
else if (overallGrade >= 60) letterGrade = "D";

dv.table(
  ["Component", "Weight", "Average", "Weighted", "Trend"],
  [
    ["📝 Quizzes", "40%", `${quizAvg.toFixed(1)}%`, `${weightedQuiz.toFixed(1)}%`, gradedQuizzes.length > 0 ? "📊" : "-"],
    ["📄 Homework", "20%", `${hwAvg.toFixed(1)}%`, `${weightedHW.toFixed(1)}%`, gradedHW.length > 0 ? "📊" : "-"],
    ["✅ Tasks", "10%", `${taskAvg.toFixed(1)}%`, `${weightedTask.toFixed(1)}%`, tasks.length > 0 ? "📊" : "-"],
    ["🎴 Flashcards", "30%", `${flashcardAvg.toFixed(1)}%`, `${weightedFlashcard.toFixed(1)}%`, flashcards.length > 0 ? "📊" : "-"],
    ["**TOTAL**", "**100%**", "", `**${overallGrade.toFixed(1)}%**`, `**${letterGrade}**`]
  ]
);

// Visual grade display
dv.paragraph(`### Current Grade: ${overallGrade.toFixed(1)}% (${letterGrade})`);

const gradeBarWidth = 40;
const gradeFilled = Math.round((overallGrade / 100) * gradeBarWidth);
const gradeEmpty = gradeBarWidth - gradeFilled;
const gradeBar = '█'.repeat(gradeFilled) + '░'.repeat(gradeEmpty);
dv.paragraph(`\`${gradeBar}\` ${overallGrade.toFixed(1)}%`);
```

---

## 🎯 Upcoming Deadlines

```dataviewjs
dv.header(3, "Due Soon");

const allMaterials = dv.pages('"OCDS_Documentation/Example_Class_TCM_101/Materials"');
const today = new Date();

// Get materials with due dates
const upcoming = allMaterials
  .where(m => m.due_date && new Date(m.due_date) >= today)
  .sort(m => m.due_date, 'asc')
  .limit(5);

if (upcoming.length > 0) {
  dv.table(
    ["Item", "Type", "Due Date", "Days Left", "Status"],
    upcoming.map(m => {
      const dueDate = new Date(m.due_date);
      const daysLeft = Math.ceil((dueDate - today) / (1000 * 60 * 60 * 24));
      const urgency = daysLeft <= 1 ? "🔴" : daysLeft <= 3 ? "🟡" : "🟢";
      
      let status = "Not Started";
      if (m.ocds_type === "quiz" && m.score !== null) status = "✅ Complete";
      else if (m.ocds_type === "homework" && m.submission_status === "submitted") status = "✅ Submitted";
      else if (m.ocds_type === "task" && m.status === "completed") status = "✅ Complete";
      else if (m.submission_status === "in_progress" || m.status === "in_progress") status = "🔄 In Progress";
      
      return [
        `[[${m.file.name}|${m.title}]]`,
        m.ocds_type,
        m.due_date,
        `${urgency} ${daysLeft} days`,
        status
      ];
    })
  );
} else {
  dv.paragraph("No upcoming deadlines. Great job staying on top of things! 🎉");
}
```

---

## 💡 Study Recommendations

```dataviewjs
dv.header(3, "Suggested Next Steps");

const classFolder = "OCDS_Documentation/Example_Class_TCM_101/Materials";
const allMaterials = dv.pages(`"${classFolder}"`);

// Find incomplete items
const incompleteQuizzes = allMaterials
  .where(m => m.ocds_type === "quiz" && (m.score === null || m.score === undefined || m.score < 7));
const incompleteHW = allMaterials
  .where(m => m.ocds_type === "homework" && m.submission_status !== "graded");
const incompleteTasks = allMaterials
  .where(m => m.ocds_type === "task" && m.status !== "completed");
const incompleteFlashcards = allMaterials
  .where(m => m.ocds_type === "flashcard" && (m.cards_reviewed || 0) < 20);

const recommendations = [];

if (incompleteQuizzes.length > 0) {
  recommendations.push(`📝 **Take ${incompleteQuizzes.length} quiz(es)** - Quizzes are 40% of your grade`);
}
if (incompleteHW.length > 0) {
  recommendations.push(`📄 **Complete ${incompleteHW.length} homework assignment(s)** - Due soon!`);
}
if (incompleteTasks.length > 0) {
  recommendations.push(`✅ **Finish ${incompleteTasks.length} task checklist(s)** - Quick points!`);
}
if (incompleteFlashcards.length > 0) {
  recommendations.push(`🎴 **Review flashcards** - Spaced repetition is 30% of your grade`);
}

if (recommendations.length > 0) {
  dv.list(recommendations);
} else {
  dv.paragraph("🎉 **You're all caught up!** Great work! Consider reviewing previous materials or getting ahead on next week's content.");
}
```

---

## 📚 Resources

- [[OCDS_Documentation/Example_Class_TCM_101/README|Class Information]]
- [[class_manifest.yaml|Class Syllabus]]
- [[timeline.yaml|Course Schedule]]
- [[grading_config.yaml|Grading Details]]

---

## 🆘 Need Help?

**Office Hours:** Tuesdays 2-4pm, Thursdays 10am-12pm  
**Email:** dr.smith@example.edu  
**Discussion Forum:** Available in class materials

---

*Dashboard auto-updates as you complete materials. Refresh the page to see latest progress.*

**Last Updated:** `VIEW{last_updated}`
