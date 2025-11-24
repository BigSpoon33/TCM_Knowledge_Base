# How to Use TCM 101 Example Class

**Quick Start Guide for Testing the OCDS System**

---

## 📊 Start Here: The Dashboard

Open `Dashboards/Student_Dashboard.md` - this is your home base!

---

## ✅ How to Complete Each Material Type

### 1. 📝 Quizzes (Auto-Graded)

**File:** `Materials/Week_01/Quiz.md`

**Steps:**
1. Open the quiz file
2. Read each question
3. Check ONE box per question (A, B, C, or D)
4. Click the "Submit Quiz" button at the bottom
5. You'll see a notification with your score!
6. Check the dashboard - your score will appear

**Example:**
```markdown
## Question 1
Which tongue color indicates Heat?
- [ ] A) Pale
- [x] B) Red  ← Check this box
- [ ] C) Purple
- [ ] D) Blue
```

**Grading:**
- Automatic when you click Submit
- Pass = 70% (7/10 correct)
- 3 attempts allowed
- Best score counts

---

### 2. 📄 Homework (Manual Grading)

**File:** `Materials/Week_01/Homework.md`

**Steps:**
1. Open the homework file
2. Fill in your answers in the designated sections
3. Click "Submit Homework" button
4. Status changes to "Submitted"
5. Instructor grades manually (in real system)
6. For testing: manually update frontmatter with score

**To Simulate Grading (for testing):**
1. Open homework file
2. Press Ctrl/Cmd + E to edit frontmatter
3. Change:
   ```yaml
   submission_status: graded
   score: 18
   graded_date: 2025-11-07
   ```
4. Save and check dashboard

---

### 3. ✅ Tasks (Auto-Updating)

**File:** `Materials/Week_01/Tasks.md`

**Steps:**
1. Open the tasks file
2. Check off tasks as you complete them
3. Progress updates automatically!
4. Check the dashboard to see updated progress

**Example:**
```markdown
- [x] **Read Study Material** ← Check this
- [ ] **Review Flashcards**
- [ ] **Complete Quiz**
```

**How It Works:**
- DataviewJS script counts checked boxes
- Updates frontmatter automatically
- Progress bar fills in
- Points calculated based on completion

---

### 4. 🎴 Flashcards (Spaced Repetition Plugin)

**File:** `Materials/Week_01/Flashcards.md`

**Steps:**
1. Install Spaced Repetition plugin (if not installed)
2. Press Ctrl/Cmd + P
3. Type "Review flashcards"
4. Study the cards using the plugin interface
5. Mark as Hard/Good/Easy
6. **After reviewing, open Flashcards.md and refresh the page**
7. Progress updates automatically!

**How It Works:**
- Spaced Repetition plugin adds `<!--SR:!date,interval,ease-->` comments
- Our script reads these comments to count reviews
- **Dynamically tracks:** total cards, reviewed, mastered, last review date
- **Auto-adjusts:** When you add/remove cards, counts update automatically
- Dashboard reads from frontmatter (updated by script)

**Tracking Metrics:**
- `total_cards`: Auto-counted (updates when you add cards)
- `cards_reviewed`: Cards with SR comments
- `cards_mastered`: Cards with ease ≥ 250 (you know them well)
- `last_review_date`: Last study session

**To See Updated Progress:**
1. Review cards using SR plugin
2. Open `Flashcards.md`
3. **Refresh page** (Ctrl/Cmd + R) ← Important!
4. See updated stats (total, reviewed, mastered)
5. Go to dashboard and refresh
6. Progress appears!

**Dynamic Updates:**
- Add 2 cards → Total updates to 22, completion % adjusts
- Review new cards → Reviewed count increases
- Everything updates automatically on refresh!

---

### 5. 📖 Study Material

**File:** `Materials/Week_01/Study_Material.md`

**Steps:**
1. Open and read the material
2. Take notes as needed
3. No tracking required - reference material

---

## 🎯 Testing the Full Workflow

### Complete Test Run (15 minutes)

1. **Open Dashboard**
   - `Dashboards/Student_Dashboard.md`
   - Note: Overall grade is 0%

2. **Complete Tasks** (2 min)
   - Open `Materials/Week_01/Tasks.md`
   - Check 3-4 boxes
   - Return to dashboard
   - See progress update!

3. **Take Quiz** (5 min)
   - Open `Materials/Week_01/Quiz.md`
   - Check answer boxes (try to get 7+ correct)
   - Click "Submit Quiz"
   - See notification with score
   - Return to dashboard
   - See quiz score appear!

4. **Submit Homework** (2 min)
   - Open `Materials/Week_01/Homework.md`
   - Click "Submit Homework"
   - Return to dashboard
   - See status change to "Submitted"

5. **Check Final Grade** (1 min)
   - Scroll to "Grade Breakdown" on dashboard
   - See weighted grade calculation
   - Note letter grade

---

## 🐛 Troubleshooting

### Dashboard Shows Errors
- **Solution:** Refresh the page (Ctrl/Cmd + R)
- DataviewJS queries run on page load

### Quiz Doesn't Grade
- **Check:** Did you check answer boxes?
- **Check:** Did you click "Submit Quiz" button?
- **Check:** Look for notification message

### Tasks Don't Update
- **Solution:** Return to dashboard and refresh
- Progress updates when dashboard loads

### Buttons Don't Work
- **Check:** Meta-bind plugin installed?
- **Check:** Click directly on button text

### Flashcards Don't Track
- **Solution:** Use Spaced Repetition plugin interface
- Dashboard shows estimated progress only

---

## 📁 File Structure

```
TCM_101/
├── Dashboards/
│   └── Student_Dashboard.md  ← START HERE
├── Materials/
│   └── Week_01/
│       ├── Study_Material.md
│       ├── Quiz.md           ← Auto-grades
│       ├── Homework.md       ← Manual grade
│       ├── Tasks.md          ← Auto-updates
│       └── Flashcards.md     ← Use SR plugin
├── README.md
└── HOW_TO_USE.md            ← This file
```

---

## 🎓 Understanding the Grading System

### Grade Components

| Component | Weight | How It's Tracked |
|-----------|--------|------------------|
| Quizzes | 40% | Auto-graded on submit |
| Flashcards | 30% | Spaced Repetition plugin |
| Homework | 20% | Manual grading |
| Tasks | 10% | Auto-tracked via checkboxes |

### Grade Calculation

```
Overall Grade = (Quiz Avg × 0.40) + 
                (Flashcard % × 0.30) + 
                (Homework Avg × 0.20) + 
                (Task % × 0.10)
```

### Letter Grades

- A: 93-100%
- A-: 90-92%
- B+: 87-89%
- B: 83-86%
- B-: 80-82%
- C+: 77-79%
- C: 73-76%
- C-: 70-72%
- D: 60-69%
- F: 0-59%

---

## 💡 Tips for Testing

1. **Start with Tasks** - Easiest to see immediate results
2. **Take the Quiz** - Most impressive feature (auto-grading!)
3. **Check Dashboard Often** - See progress update in real-time
4. **Try Multiple Attempts** - Quiz allows 3 attempts
5. **Simulate Full Class** - Complete all materials to see 100%

---

## 🚀 What's Working

- ✅ Auto-grading quizzes
- ✅ Auto-updating task progress
- ✅ Real-time dashboard updates
- ✅ Grade calculation
- ✅ Progress visualization
- ✅ One-click navigation
- ✅ Meta-bind buttons
- ✅ DataviewJS queries

---

## 📝 What's Manual (For Now)

- ⏳ Homework grading (instructor does this)
- ⏳ Flashcard tracking (Spaced Repetition plugin handles this)
- ⏳ Study material completion (no tracking needed)

---

## 🎉 You're Ready!

Open the dashboard and start testing. Everything should work smoothly now!

**Questions?** Check the main README or documentation files.
