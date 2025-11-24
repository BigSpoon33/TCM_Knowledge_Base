# Student Dashboard Features

**File:** `Student_Dashboard.md`  
**Purpose:** Real-time progress tracking for TCM 101 students

---

## 🎯 What It Does

The Student Dashboard is a **live, auto-updating** progress tracker that shows:

- Overall class progress and grade
- Week-by-week completion status
- Quiz scores and averages
- Homework submissions and grades
- Task completion with visual progress bars
- Flashcard review progress
- Upcoming deadlines
- Personalized study recommendations

---

## ✨ Key Features

### 1. **Auto-Updating Progress**
- Uses DataviewJS to scan all class materials
- Calculates completion percentages in real-time
- Updates automatically when you complete materials
- No manual tracking needed!

### 2. **Visual Progress Bars**
```
████████████████████░░░░░░░░░░░░░░░░░░░░ 50%
```
- ASCII progress bars for quick visual feedback
- Color-coded status indicators (✅ 🔄 ⏸️)
- Percentage completion for each component

### 3. **Grade Calculation**
- Weighted grade breakdown:
  - Quizzes: 40%
  - Flashcards: 30%
  - Homework: 20%
  - Tasks: 10%
- Letter grade display (A, B+, C, etc.)
- Component-by-component breakdown

### 4. **Quick Actions**
- One-click navigation to materials
- "Continue Learning" button
- "Review Flashcards" button
- "View Tasks" button
- "Take Quiz" button

### 5. **Smart Recommendations**
- Identifies incomplete items
- Prioritizes by due date
- Suggests next steps
- Highlights urgent deadlines

### 6. **Upcoming Deadlines**
- Shows next 5 due items
- Color-coded urgency:
  - 🔴 Due in 1 day
  - 🟡 Due in 2-3 days
  - 🟢 Due in 4+ days
- Days remaining countdown

---

## 📊 Dashboard Sections

### Overall Progress
- Completion summary table
- Overall percentage
- Visual progress bar
- Status for each component

### Week 1 Progress
- Detailed material-by-material breakdown
- Status for each item
- Scores/progress for each
- Quick action links

### Quiz Performance
- All quiz scores in table format
- Attempts used vs. available
- Pass/fail status
- Quiz average calculation

### Homework Assignments
- Assignment status tracking
- Due dates
- Submission status
- Grades and feedback
- Homework average

### Task Completion
- Weekly task checklists
- Progress bars for each week
- Points earned
- Completion status

### Flashcard Progress
- Cards reviewed vs. total
- Mastery tracking
- Progress bars
- Overall flashcard completion

### Grade Breakdown
- Weighted grade calculation
- Component averages
- Current letter grade
- Visual grade display

### Upcoming Deadlines
- Next 5 items due
- Urgency indicators
- Days remaining
- Current status

### Study Recommendations
- Personalized next steps
- Priority suggestions
- Completion reminders

---

## 🔧 How It Works

### DataviewJS Queries
The dashboard uses DataviewJS to:

1. **Scan all materials** in the class folder
2. **Filter by type** (quiz, homework, task, flashcard)
3. **Read frontmatter** to get status, scores, dates
4. **Calculate statistics** (averages, percentages, totals)
5. **Display results** in tables and visualizations

### Example Query
```javascript
const quizzes = dv.pages('"Example_Class_TCM_101/Materials"')
  .where(p => p.ocds_type === "quiz");

const gradedQuizzes = quizzes.where(q => q.score !== null);
const avgScore = gradedQuizzes
  .map(q => q.score)
  .reduce((a, b) => a + b, 0) / gradedQuizzes.length;
```

### Auto-Update Mechanism
- Dashboard refreshes when you open it
- Dataview queries run automatically
- No manual refresh needed
- Always shows current data

---

## 🎨 Visual Elements

### Progress Bars
```
█████████████████████████░░░░░░░░░░░░░░░ 62.5%
```
- 40 characters wide
- Filled (█) vs. empty (░)
- Percentage display

### Status Indicators
- ✅ Complete
- 🔄 In Progress
- ⏸️ Not Started
- ⏳ Pending
- ⚠️ Needs Attention
- 🔴 Urgent
- 🟡 Soon
- 🟢 Plenty of Time

### Tables
- Clean, organized data display
- Sortable columns
- Clickable links to materials
- Color-coded status

---

## 📱 Meta-bind Buttons

### Quick Action Buttons
```markdown
```meta-bind-button
label: 📚 Continue Learning
style: primary
action:
  type: open
  link: "[[Week 1 Study Material]]"
\```
```

**Available Actions:**
- Continue Learning (primary button)
- Review Flashcards
- View Tasks
- Take Quiz

---

## 🔄 Real-Time Updates

### What Triggers Updates
1. **Opening the dashboard** - Queries run automatically
2. **Completing materials** - Frontmatter changes detected
3. **Submitting assignments** - Status updates reflected
4. **Checking tasks** - Progress recalculated

### What Gets Updated
- Completion percentages
- Grade calculations
- Progress bars
- Status indicators
- Recommendations
- Deadline countdowns

---

## 💡 Usage Tips

### For Students
1. **Bookmark the dashboard** - Make it your starting point
2. **Check daily** - See what's due and what to work on
3. **Use quick actions** - One-click navigation to materials
4. **Follow recommendations** - Prioritized suggestions
5. **Track your grade** - See how you're doing in real-time

### For Instructors
1. **Customize queries** - Adjust to your grading system
2. **Add sections** - Include class-specific metrics
3. **Modify weights** - Change grade component percentages
4. **Brand it** - Add your institution's style
5. **Clone for students** - Each student gets their own

---

## 🎯 Benefits

### For Students
- ✅ Always know where you stand
- ✅ Never miss a deadline
- ✅ See progress visually
- ✅ Get personalized recommendations
- ✅ One-click access to materials

### For Instructors
- ✅ Students stay organized
- ✅ Reduced "what's my grade?" emails
- ✅ Increased engagement
- ✅ Clear expectations
- ✅ Professional presentation

---

## 🔮 Future Enhancements

Potential additions:
- Study time tracking
- Pomodoro integration
- Peer comparison (anonymized)
- Achievement badges
- Study streak tracking
- Predictive grade forecasting
- Study habit analytics
- Mobile-optimized view

---

## 📝 Technical Notes

### Requirements
- Obsidian with Dataview plugin
- Meta-bind plugin (for buttons)
- Proper frontmatter in all materials
- Consistent file structure

### Performance
- Queries are fast (< 100ms typically)
- Scales well up to 100+ materials
- No external dependencies
- Works offline

### Customization
- Easy to modify queries
- Adjust weights in grade calculation
- Add/remove sections as needed
- Change visual styling

---

**The dashboard is the heart of the OCDS student experience!** 🎉

It transforms a collection of markdown files into a cohesive, trackable learning system.
