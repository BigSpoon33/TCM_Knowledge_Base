# Task Template

**Purpose:** Define the structure and format for tasks using TaskNotes plugin in OCDS classes

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

Tasks in OCDS use the **TaskNotes** plugin to create actionable to-do items that integrate with the class timeline and grading system. Tasks can be:

- **Study tasks** - Read materials, watch videos, review notes
- **Practice tasks** - Complete exercises, practice techniques
- **Submission tasks** - Submit homework, take quizzes
- **Administrative tasks** - Register for class, set up workspace
- **Milestone tasks** - Complete week, finish module

### Key Features

- ✅ **Checkbox tracking** - Mark tasks complete with `- [x]`
- ✅ **Due dates** - Integrated with timeline
- ✅ **Dependencies** - Tasks unlock based on completion
- ✅ **Progress tracking** - Counts toward engagement score
- ✅ **Automatic generation** - Created from timeline
- ✅ **Dashboard integration** - Visual progress bars

---

## 🎯 When to Use Tasks

| Use Tasks For... | Use Other Materials For... |
|------------------|----------------------------|
| Action items | Content delivery |
| Checklists | Knowledge assessment |
| Progress tracking | Detailed instruction |
| Workflow guidance | Reference materials |
| Engagement metrics | Graded assignments |

**Example Task Types:**
- Read Week 1 Study Material
- Complete Tongue Diagnosis Quiz
- Submit Case Study Homework
- Review flashcards (20 cards)
- Watch lecture video
- Practice pulse diagnosis (30 min)

---

## 📝 Task File Structure

### Frontmatter Schema

```yaml
---
# === OCDS CORE METADATA ===
ocds_type: task
material_id: task_week01_checklist
class_id: TCM_101
week: 1
day: 0  # 0 = week-level task

# === TASK DETAILS ===
title: "Week 1 Task Checklist"
description: "Complete all Week 1 learning activities"
task_type: checklist  # checklist, milestone, submission, practice, admin

# === TIMELINE ===
unlock_date: 2025-01-01
due_date: 2025-01-07
unlock_requirements: []  # Week 1 unlocked by default

# === TRACKING ===
total_tasks: 12
completed_tasks: 0
completion_percentage: 0
status: not_started  # not_started, in_progress, completed
first_started: null
completed_date: null

# === GRADING ===
counts_toward_grade: true
weight: 0.10  # Tasks = 10% of total grade (via engagement)
points_possible: 10  # Points for completing ALL tasks
points_earned: 0

# === TASK ITEMS ===
tasks:
  - id: task_01
    description: "Read Week 1 Study Material - Tongue Diagnosis"
    completed: false
    required: true
    points: 1
    linked_material: study_week01_tongue
  
  - id: task_02
    description: "Review Tongue Diagnosis Flashcards (20 cards)"
    completed: false
    required: true
    points: 1
    linked_material: flashcards_week01_tongue
  
  - id: task_03
    description: "Watch Lecture Slides - Introduction to Tongue Diagnosis"
    completed: false
    required: true
    points: 1
    linked_material: slides_week01_tongue_diagnosis
  
  - id: task_04
    description: "Complete Week 1 Quiz"
    completed: false
    required: true
    points: 2
    linked_material: quiz_week01
  
  - id: task_05
    description: "Submit Tongue Case Study Homework"
    completed: false
    required: true
    points: 2
    linked_material: hw_week01_case_study
  
  - id: task_06
    description: "Practice identifying tongue patterns (30 min)"
    completed: false
    required: false
    points: 1
    linked_material: null
  
  - id: task_07
    description: "Participate in Week 1 Discussion Forum"
    completed: false
    required: false
    points: 1
    linked_material: discussion_week01
  
  - id: task_08
    description: "Complete 2 Pomodoro study sessions"
    completed: false
    required: false
    points: 1
    linked_material: null

# === TAGS ===
tags:
  - tasks
  - week1
  - checklist
---
```

---

## 🏗️ Task Content Structure

### Template Layout

```markdown
# [Task Title]

**Week:** [X]  
**Due:** [Date]  
**Status:** `VIEW{status}`  
**Progress:** `VIEW{completed_tasks}` / `VIEW{total_tasks}` (`VIEW{completion_percentage}`%)

---

## 📋 Task Checklist

### Required Tasks

- [ ] **Task 1:** [Description] → [[Linked Material]]
- [ ] **Task 2:** [Description] → [[Linked Material]]
- [ ] **Task 3:** [Description] → [[Linked Material]]

### Optional Tasks (Bonus Points)

- [ ] **Bonus 1:** [Description]
- [ ] **Bonus 2:** [Description]

---

## 📊 Progress Tracking

```dataviewjs
// Auto-count completed tasks and update frontmatter
const file = dv.current().file;
const content = await dv.io.load(file.path);
const lines = content.split('\n');

let totalTasks = 0;
let completedTasks = 0;

// Count checkboxes
for (const line of lines) {
  if (line.match(/^- \[[ x]\]/)) {
    totalTasks++;
    if (line.match(/^- \[x\]/)) {
      completedTasks++;
    }
  }
}

const percentage = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;

// Update frontmatter automatically
const currentFile = app.workspace.getActiveFile();
if (currentFile) {
  await app.fileManager.processFrontMatter(currentFile, (fm) => {
    fm.completed_tasks = completedTasks;
    fm.total_tasks = totalTasks;
    fm.completion_percentage = percentage;
    fm.status = completedTasks === 0 ? 'not_started' : 
                completedTasks === totalTasks ? 'completed' : 'in_progress';
    fm.points_earned = completedTasks === totalTasks ? (fm.points_possible || 10) : 
                       Math.floor((completedTasks / totalTasks) * (fm.points_possible || 10));
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

> [!tip] Auto-Update Feature
> This DataviewJS script automatically counts your completed checkboxes and updates the frontmatter. Just check off tasks and the progress updates in real-time!

---

## ✅ How to Complete Tasks

1. Click the checkbox next to each task when complete
2. Progress updates automatically
3. Points awarded when ALL required tasks complete
4. Bonus tasks add extra points

---

## 🎯 Tips for Success

- ✅ [Tip 1]
- ✅ [Tip 2]
- ✅ [Tip 3]
```

---

## 📖 Complete Example: Week 1 Task Checklist

### Example File: `Task_Week01_Checklist.md`

```markdown
---
ocds_type: task
material_id: task_week01_checklist
class_id: TCM_101
week: 1
day: 0

title: "Week 1 Task Checklist"
description: "Complete all Week 1 learning activities"
task_type: checklist

unlock_date: 2025-01-01
due_date: 2025-01-07

total_tasks: 8
completed_tasks: 0
completion_percentage: 0
status: not_started

counts_toward_grade: true
weight: 0.10
points_possible: 10
points_earned: 0

tasks:
  - id: task_01
    description: "Read Week 1 Study Material - Tongue Diagnosis"
    completed: false
    required: true
    points: 1
  
  - id: task_02
    description: "Review Tongue Diagnosis Flashcards (20 cards)"
    completed: false
    required: true
    points: 1
  
  - id: task_03
    description: "Watch Lecture Slides"
    completed: false
    required: true
    points: 1
  
  - id: task_04
    description: "Complete Week 1 Quiz (70% minimum)"
    completed: false
    required: true
    points: 2
  
  - id: task_05
    description: "Submit Tongue Case Study Homework"
    completed: false
    required: true
    points: 2
  
  - id: task_06
    description: "Practice identifying tongue patterns (30 min)"
    completed: false
    required: false
    points: 1
  
  - id: task_07
    description: "Participate in Discussion Forum"
    completed: false
    required: false
    points: 1
  
  - id: task_08
    description: "Complete 2 Pomodoro study sessions"
    completed: false
    required: false
    points: 1

tags:
  - tasks
  - week1
  - checklist
---

# Week 1 Task Checklist

**Week:** 1 - Introduction to Tongue Diagnosis  
**Due:** January 7, 2025  
**Status:** `VIEW{status}`  
**Progress:** `VIEW{completed_tasks}` / `VIEW{total_tasks}` tasks (`VIEW{completion_percentage}`%)

---

## 📋 Your Tasks for This Week

### 📚 Study & Review (Required)

- [ ] **Read Study Material:** Complete [[Week 1 Study Material]] 📅 2025-01-07 #study #required
  - Estimated time: 45 minutes
  - Focus on tongue body characteristics and coating analysis
  
- [ ] **Review Flashcards:** Study [[Week 1 Flashcards]] (minimum 20 cards) 📅 2025-01-07 #flashcards #required
  - Use spaced repetition
  - Aim for 80%+ accuracy
  
- [ ] **Watch Lecture:** View [[Week 1 Lecture Slides]] 📅 2025-01-07 #lecture

---

### ✍️ Assessments (Required)

- [ ] **Complete Quiz:** Take [[Week 1 Quiz]] 📅 2025-01-07 ⏫ #quiz #required
  - Minimum score: 70%
  - Multiple choice, 10 questions
  - 3 attempts allowed
  
- [ ] **Submit Homework:** Complete [[Week 1 Homework]] 📅 2025-01-12 ⏫ #homework #required
  - Analyze 3 tongue images
  - Due: January 12, 2025
  - Worth 20 points

---

### 🎯 Practice & Engagement (Optional - Bonus Points)

- [ ] **Practice Session:** Spend 30 minutes identifying tongue patterns 📅 2025-01-07 #practice #bonus
  - Use practice images in study materials
  - Try to identify without looking at answers first
  - Bonus: +1 point
  
- [ ] **Discussion Forum:** Post in [[Week 1 Discussion Forum]] 📅 2025-01-07 #discussion #bonus
  - Share an interesting tongue diagnosis case
  - Respond to at least one classmate
  - Bonus: +1 point
  
- [ ] **Pomodoro Sessions:** Complete 2 focused study sessions
  - Use Pomodoro timer (25 min work, 5 min break)
  - Track in your study log
  - Bonus: +1 point

---

## 📊 Progress Tracking

### Visual Progress

```meta-bind
INPUT[progressBar(
  minValue(0),
  maxValue(8),
  value(completed_tasks)
)]
```

**Completion:** `VIEW{completion_percentage}`%  
**Points Earned:** `VIEW{points_earned}` / `VIEW{points_possible}`  
**Status:** `VIEW{status}`

---

### Task Breakdown

| Category | Tasks | Completed | Points |
|----------|-------|-----------|--------|
| **Study & Review** | 3 | `VIEW{tasks[0].completed + tasks[1].completed + tasks[2].completed}` | 3 |
| **Assessments** | 2 | `VIEW{tasks[3].completed + tasks[4].completed}` | 4 |
| **Practice & Engagement** | 3 | `VIEW{tasks[5].completed + tasks[6].completed + tasks[7].completed}` | 3 |
| **TOTAL** | **8** | **`VIEW{completed_tasks}`** | **10** |

---

## ✅ How to Use This Checklist

### Step 1: Start Tasks
Click the checkbox `- [ ]` next to each task as you complete it. It will change to `- [x]`.

### Step 2: Track Progress
Your progress updates automatically in the frontmatter and progress bar above.

### Step 3: Earn Points
- Complete ALL required tasks (5 tasks) = 7 points
- Complete optional tasks = +1 point each (up to 3 bonus points)
- Maximum possible: 10 points

### Step 4: Check Dashboard
View your overall progress in [[Student Dashboard]].

---

## 🎯 Tips for Success

- ✅ **Start early** - Don't wait until the last day
- ✅ **Follow the order** - Study materials → Flashcards → Quiz → Homework
- ✅ **Use active learning** - Don't just read passively
- ✅ **Practice regularly** - Short daily sessions > long cramming
- ✅ **Ask questions** - Use discussion forum if stuck
- ✅ **Track your time** - Use Pomodoro technique for focus

---

## 📅 Suggested Schedule

### Day 1-2 (Mon-Tue)
- [ ] Read study material
- [ ] Start flashcards (10 cards/day)

### Day 3-4 (Wed-Thu)
- [ ] Watch lecture slides
- [ ] Continue flashcards
- [ ] Practice identifying patterns

### Day 5 (Fri)
- [ ] Complete quiz
- [ ] Start homework

### Day 6-7 (Sat-Sun)
- [ ] Finish homework
- [ ] Review any weak areas
- [ ] Participate in discussion

---

## 🔗 Quick Links

### This Week's Materials
- [[Week 1 Study Material - Tongue Diagnosis]]
- [[Flashcards - Tongue Diagnosis]]
- [[Slides - Introduction to Tongue Diagnosis]]
- [[Quiz - Week 1 Tongue Diagnosis]]
- [[Homework - Tongue Case Study]]

### Support Resources
- [[Week 1 Discussion Forum]]
- [[Office Hours Schedule]]
- [[Student Dashboard]]
- [[Class Calendar]]

---

## ❓ FAQ

**Q: Do I have to complete tasks in order?**  
A: Required tasks should be done in the suggested order (study → practice → assess), but you can do optional tasks anytime.

**Q: What happens if I don't complete all tasks?**  
A: You'll earn partial points based on what you complete. However, some tasks may be required to unlock next week's content.

**Q: Can I complete tasks after the due date?**  
A: Yes, but you may not earn full points. Check individual task requirements.

**Q: How do bonus tasks work?**  
A: Optional tasks give you extra points beyond the base 7. Great for boosting your grade!

**Q: Do tasks count toward my final grade?**  
A: Yes! Task completion = 10% of your final grade (engagement score).

---

## 📊 Integration with Grading

### How Task Points Work

```
Task Score = (Points Earned / Points Possible) × 100
Example: (8 / 10) × 100 = 80%
```

### Grading Weight

Tasks contribute to your **Engagement Score** (10% of final grade):

```
Engagement Score = (Task Completion + Pomodoro Sessions) / 2
```

See [[Grading Config]] for complete breakdown.

---

## 🔄 Automatic Updates

### Task Status Auto-Updates

The following fields update automatically:

- `completed_tasks` - Counts checked boxes
- `completion_percentage` - Calculates % complete
- `status` - Changes based on progress:
  - `not_started` - 0% complete
  - `in_progress` - 1-99% complete
  - `completed` - 100% complete
- `points_earned` - Sums points from completed tasks

### Linked Material Tracking

When you complete linked materials (quizzes, homework), the corresponding task auto-checks:

```yaml
# When quiz_week01 score >= 70%, task_04 auto-completes
- id: task_04
  description: "Complete Week 1 Quiz (70% minimum)"
  completed: true  # Auto-updated!
  linked_material: quiz_week01
```

---

## 📱 Meta-Bind Buttons

### Quick Actions

```meta-bind-button
label: Mark All Study Tasks Complete
style: primary
action:
  type: inlineJS
  code: |
    const file = app.workspace.getActiveFile();
    await app.fileManager.processFrontMatter(file, (fm) => {
      if (fm.tasks && Array.isArray(fm.tasks)) {
        fm.tasks.forEach(task => task.completed = true);
      }
      fm.completed_tasks = fm.total_tasks || 0;
      fm.status = 'completed';
    });
    new Notice('All tasks marked complete!');
```

```meta-bind-button
label: Reset All Tasks
style: destructive
action:
  type: inlineJS
  code: |
    const file = app.workspace.getActiveFile();
    const cache = app.metadataCache.getFileCache(file);
    const fm = cache?.frontmatter || {};
    
    if (fm.status === 'completed') {
      await app.fileManager.processFrontMatter(file, (frontmatter) => {
        frontmatter.completed_tasks = 0;
        frontmatter.status = 'not_started';
        if (frontmatter.tasks && Array.isArray(frontmatter.tasks)) {
          frontmatter.tasks.forEach(task => task.completed = false);
        }
      });
      new Notice('All tasks reset!');
    } else {
      new Notice('Can only reset completed tasks');
    }
```

```meta-bind-button
label: View Progress Dashboard
style: default
action:
  type: open
  link: "[[Student Dashboard]]"
```
>still with the metabind syntax errors. need to get the buttons fine tuned and try to get the most we can out of this plugin. will be cool to have clickable elements
---

## 📊 Dataview Queries

### Show All Tasks for This Week

```dataview
TABLE
  description as "Task",
  completed as "Done",
  required as "Required",
  points as "Points"
FROM [[]]
WHERE ocds_type = "task" AND week = 1
```

---

### Show Incomplete Required Tasks

```dataview
TASK
WHERE !completed AND required = true
```

---

### Calculate Task Completion Rate

```dataviewjs
const tasks = dv.current().tasks;
const completed = tasks.filter(t => t.completed).length;
const total = tasks.length;
const percentage = (completed / total * 100).toFixed(1);

dv.paragraph(`**Task Completion:** ${completed}/${total} (${percentage}%)`);
```
> More syntax to fix
---

## 🔧 TaskNotes Plugin Integration

### Task Syntax

TaskNotes recognizes these formats:

```markdown
# Standard checkbox
- [ ] Task description

# With due date (RECOMMENDED)
- [ ] Task description 📅 2025-01-07

# With priority
- [ ] Task description ⏫  # High priority (red)
- [ ] Task description 🔼  # Medium-high priority (orange)
- [ ] Task description 🔽  # Low priority (blue)

# With tags (RECOMMENDED for filtering)
- [ ] Task description #study #week1 #required

# Complete syntax (BEST PRACTICE)
- [ ] **Task Name:** Description 📅 2025-01-07 ⏫ #category #required

# Completed (auto-adds completion date)
- [x] Task description ✅ 2025-01-05
```

**OCDS Best Practice Format:**
```markdown
- [ ] **Read Study Material:** Complete Week 1 notes 📅 2025-01-07 #study #required
- [ ] **Complete Quiz:** Tongue Diagnosis Quiz 📅 2025-01-07 ⏫ #quiz #required
- [ ] **Practice Session:** 30 min tongue identification 📅 2025-01-07 #practice #bonus
```

---

### Task Queries

```markdown
# Show all incomplete tasks
```tasks
not done
```
>going to help a lot when buliding the dashboard. good to have a quick glance format that gives you all the necessary information about due dates
# Show tasks due this week
```tasks
due this week
```

# Show high priority tasks
```tasks
priority is high
```
```

---

## 🎯 Best Practices

### For Instructors Creating Task Lists

**Design:**
- ✅ **Clear descriptions** - Students know exactly what to do
- ✅ **Reasonable scope** - Don't overwhelm with too many tasks
- ✅ **Logical order** - Sequence tasks for optimal learning
- ✅ **Mix required/optional** - Core tasks + bonus opportunities
- ✅ **Link materials** - Connect tasks to specific resources

**Tracking:**
- ✅ **Set due dates** - Align with timeline
- ✅ **Define points** - Weight tasks appropriately
- ✅ **Auto-update** - Link to material completion
- ✅ **Monitor progress** - Check dashboard regularly
- ✅ **Provide feedback** - Encourage struggling students

---

### For Students Using Task Lists

**Planning:**
- ✅ **Review weekly** - Check tasks at start of week
- ✅ **Schedule time** - Block time for each task
- ✅ **Prioritize** - Do required tasks first
- ✅ **Break down** - Split large tasks into smaller steps
- ✅ **Set reminders** - Use due dates

**Execution:**
- ✅ **Check off promptly** - Mark tasks as you complete them
- ✅ **Track time** - Note how long tasks take
- ✅ **Ask for help** - If stuck, reach out
- ✅ **Review progress** - Check dashboard daily
- ✅ **Celebrate wins** - Acknowledge completed tasks!

---

## 🔍 Troubleshooting

### Common Issues

**Issue:** "Checkboxes don't update completion percentage"  
**Solution:** Make sure frontmatter `total_tasks` matches actual number of tasks. Run update script.

**Issue:** "Linked material completion doesn't auto-check task"  
**Solution:** Verify `linked_material` ID matches exactly. Check automation script is running.

**Issue:** "Progress bar doesn't show"  
**Solution:** Meta-bind plugin must be installed. Check frontmatter syntax for `completed_tasks` field.

**Issue:** "Tasks don't show in dashboard"  
**Solution:** Verify `ocds_type: task` in frontmatter. Check dataview query path.

**Issue:** "Points not calculating correctly"  
**Solution:** Ensure `points` field is a number (not text). Check grading script logic.

---

## 🔄 Automation Scripts

### Generate Tasks from Timeline

```python
# scripts/generate_tasks.py

def generate_week_tasks(class_id: str, week: int):
    """Generate task checklist from timeline."""
    
    timeline = load_timeline(class_id)
    week_data = timeline['weeks'][week - 1]
    
    tasks = []
    task_id = 1
    
    # Study materials
    for material in week_data.get('study_materials', []):
        tasks.append({
            'id': f'task_{task_id:02d}',
            'description': f'Read {material["title"]}',
            'completed': False,
            'required': True,
            'points': 1,
            'linked_material': material['material_id']
        })
        task_id += 1
    
    # Quizzes
    for quiz in week_data.get('quizzes', []):
        tasks.append({
            'id': f'task_{task_id:02d}',
            'description': f'Complete {quiz["title"]} (70% minimum)',
            'completed': False,
            'required': True,
            'points': 2,
            'linked_material': quiz['material_id']
        })
        task_id += 1
    
    # Homework
    for hw in week_data.get('homework', []):
        tasks.append({
            'id': f'task_{task_id:02d}',
            'description': f'Submit {hw["title"]}',
            'completed': False,
            'required': True,
            'points': 2,
            'linked_material': hw['material_id']
        })
        task_id += 1
    
    # Create task file
    create_task_file(class_id, week, tasks)
```

---

### Auto-Update Task Completion

```python
# scripts/update_task_completion.py

def update_task_completion(task_file: str):
    """Update task completion based on linked materials."""
    
    frontmatter = parse_frontmatter(task_file)
    tasks = frontmatter['tasks']
    
    for task in tasks:
        if task.get('linked_material'):
            material = load_material(task['linked_material'])
            
            # Check completion criteria
            if material['ocds_type'] == 'quiz':
                if material.get('score', 0) >= 70:
                    task['completed'] = True
            
            elif material['ocds_type'] == 'homework':
                if material.get('submission_status') == 'submitted':
                    task['completed'] = True
            
            elif material['ocds_type'] in ['study', 'slides', 'flashcards']:
                if material.get('view_status') == 'completed':
                    task['completed'] = True
    
    # Update totals
    completed = sum(1 for t in tasks if t['completed'])
    total = len(tasks)
    percentage = int(completed / total * 100)
    
    # Update status
    if completed == 0:
        status = 'not_started'
    elif completed == total:
        status = 'completed'
    else:
        status = 'in_progress'
    
    # Calculate points
    points_earned = sum(t['points'] for t in tasks if t['completed'])
    
    # Update frontmatter
    update_frontmatter(task_file, {
        'tasks': tasks,
        'completed_tasks': completed,
        'completion_percentage': percentage,
        'status': status,
        'points_earned': points_earned
    })
```

---

## 📚 Related Documentation

- [[TaskNotes_Integration.md]] - Complete plugin guide
- [[Progress_Tracking_Schema.md]] - How progress is tracked
- [[Grading_Config_Schema.md]] - How task points contribute to grade
- [[Timeline_Schema.md]] - How tasks are generated from timeline
- [[Student_Dashboard]] - Viewing task progress

---

## ✅ Task Template Checklist

### For Instructors Creating Tasks

- [ ] Clear, descriptive title
- [ ] Complete frontmatter with all required fields
- [ ] Appropriate number of tasks (not too many)
- [ ] Mix of required and optional tasks
- [ ] Logical task order
- [ ] All tasks have descriptions
- [ ] Points assigned to each task
- [ ] Linked materials specified
- [ ] Due date set
- [ ] Progress tracking configured
- [ ] Meta-bind buttons added
- [ ] Dataview queries included
- [ ] Tips and FAQ provided

---

### For Students Using Tasks

- [ ] Review all tasks at start of week
- [ ] Understand required vs. optional
- [ ] Note due dates
- [ ] Plan schedule for completion
- [ ] Check off tasks as completed
- [ ] Monitor progress regularly
- [ ] Complete required tasks first
- [ ] Attempt bonus tasks if time allows
- [ ] Ask for help if stuck

---

**Tasks turn learning into action. Check them off and watch your progress grow!**

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
