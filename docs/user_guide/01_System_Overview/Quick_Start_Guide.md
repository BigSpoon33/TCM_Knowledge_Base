# OCDS Quick Start Guide

**Get up and running with OCDS in 15 minutes**

---

## 🎯 Goal

By the end of this guide, you'll have:
- ✅ Installed all required plugins
- ✅ Imported your first class
- ✅ Completed your first study session
- ✅ Understood the basic workflow

---

## 📋 Prerequisites

- Obsidian installed (v1.4.0+)
- Python 3.8+ installed (for automation scripts)
- Basic familiarity with Obsidian

---

## Step 1: Install Required Plugins (5 minutes)

### Open Obsidian Settings
1. Click the gear icon (⚙️) in the bottom left
2. Navigate to **Community Plugins**
3. Click **Browse** to open the plugin marketplace

### Install These Plugins

| Plugin                    | Purpose             | Required?  |
| ------------------------- | ------------------- | ---------- |
| **Spaced Repetition**     | Flashcard system    | ✅ Yes      |
| **TaskNotes**             | Task management     | ✅ Yes      |
| **Meta Bind**             | Interactive forms   | ✅ Yes      |
| **Dataview**              | Dynamic queries     | ✅ Yes      |
| **Advanced Slides**       | Presentations       | ✅ Yes      |
| **Templater**             | Template automation | ✅ Yes      |
| **~~Obsidian Pomodoro~~** | Time tracking       | ⭕ Optional |
>pomodoro is built into TaskNotes and comes with a tracking board
### Enable Each Plugin
1. After installing, toggle each plugin **ON**
2. Click **Enable** if prompted about community plugins
3. Restart Obsidian if needed

---

## Step 2: Set Up Your Vault Structure (2 minutes)

### Create Base Folders

Open a terminal in your vault directory and run:

```bash
# Create OCDS folder structure
mkdir -p Materials
mkdir -p Classes
mkdir -p Student_Progress
mkdir -p OCDS_Templates
mkdir -p scripts
```

Or create manually in Obsidian:
- Right-click in file explorer → New Folder
- Create: `Materials`, `Classes`, `Student_Progress`, `OCDS_Templates`, `scripts`
> folder structure can be automatically built through the plugin or a script. Should go into the root folder. maybe have an option to specify root folder but probably not important
---

## Step 3: Install OCDS Scripts (3 minutes)

### Download Scripts

Copy the OCDS scripts to your vault's `scripts/` folder:

```bash
# Navigate to your vault
cd /path/to/your/vault

# Copy OCDS scripts (adjust path as needed)
cp /path/to/OCDS/scripts/*.py scripts/
```

### Verify Installation

```bash
# Check scripts are present
ls scripts/

# Should see:
# import_class.py
# generate_materials.py
# generate_tasks.py
# auto_grader.py
# unlock_manager.py
```

### Install Python Dependencies

```bash
# Install required packages
pip install pyyaml python-frontmatter
```
>This could all be put into the plugin's functionality. Each script would be like a feature or module.
---

## Step 4: Import Example Class (2 minutes)

### Get the Example Class

The example class is located in `OCDS_Documentation/13_Examples/TCM_101_Example/`

### Run Import Script

```bash
# From your vault directory
python scripts/import_class.py \
  --class-path "OCDS_Documentation/13_Examples/TCM_101_Example" \
  --start-date "2025-11-10"
```

### What Happens
- ✅ Class copied to `Classes/TCM_101_Fundamentals/`
- ✅ Week 1 tasks created in `TaskNotes/TCM_101/`
- ✅ Week 1 materials copied with your start date
- ✅ Progress dashboard created in `Student_Progress/`

### Verify Import

Check these folders in Obsidian:
- `Classes/TCM_101_Fundamentals/` - should have Week_01 folder
- `TaskNotes/TCM_101/` - should have task notes
- `Student_Progress/` - should have your student folder

>get the full example class built completely with an example of each feature. able to be imported and exported as the base example.
---

## Step 5: Start Your First Study Session (3 minutes)

### Open TaskNotes

1. Navigate to `TaskNotes/TCM_101/`
2. Open `Week_1_Day_1_Study.md`
3. Read the task details

### Complete the Study Material

1. Click the link to the study material
2. Read through the content
3. Take notes if desired

### Review Flashcards

1. Open `Week_1_Day_1_Flashcards.md`
2. Use Spaced Repetition plugin to review
3. Rate each card (Again, Hard, Good, Easy)

### Take the Quiz

1. Open `Week_1_Day_1_Quiz.md`
2. Answer each question using the dropdown menus
3. Click "Submit Quiz" button
4. View your score

### Mark Tasks Complete

1. Return to the task note
2. Check off completed items
3. Update task status to "completed"
>ok this is starting to connect with what I understand about how tasknotes works and what this system is doing. the tasks are like assignments that tell you what to do and link you to the obsidian note in the materials folder. the materials are basically all of the notes I was just making and in their frontmatter they either have flashcard or review or note, slideshow, etc. so once you complete the task for the class. the material goes into the spaced repetition queue and you always review it eventually and the class completes and can stay complete. once you complete the class it's like endgame. it goes from progression through class to accumulating review points. class completes think max level. review points is like getting level 61+ in BDO and gear.
---

## Step 6: View Your Progress (2 minutes)

### Open Progress Dashboard

Navigate to `Student_Progress/[your_id]/TCM_101_Dashboard.md`

### What You'll See

- **Current Week/Day** - Where you are in the course
- **Overall Grade** - Your current percentage
- **Quiz Scores** - Results from assessments
- **Flashcard Stats** - Cards studied, retention rate
- **Time Spent** - Pomodoro sessions (if using timer)
- **Next Unlock** - What's coming next

### Check Unlock Status

If you scored well on the quiz (75%+), Week 2 might already be unlocked!

Check `TaskNotes/TCM_101/` for new Week 2 tasks.
>This is going to need to look and function like a modern good looking frontend have a good example from chatgpt
---

## 🎉 Congratulations!

You've successfully:
- ✅ Set up OCDS in your vault
- ✅ Imported a class
- ✅ Completed study activities
- ✅ Viewed your progress

---

## 🔄 Daily Workflow

Now that you're set up, here's your daily routine:

### Morning (5 minutes)
1. Open TaskNotes
2. Review today's tasks
3. Check progress dashboard

### Study Session (30-60 minutes)
1. Complete study material
2. Review flashcards (20 cards/day)
3. Take quiz when ready

### Evening (5 minutes)
1. Mark completed tasks
2. Review progress dashboard
3. Preview tomorrow's tasks

### Weekly (10 minutes)
1. Review week's performance
2. Identify areas needing review
3. Adjust study schedule if needed
>Part of a dashboard for trackign and focus.
---

## 🚀 Next Steps

### Learn More
- 📖 Read `System_Architecture.md` to understand how it works
- 🔌 Review `02_Plugin_Integration/` for plugin details
- 📝 Study `05_Material_Templates/` to create content

### Customize
- ⚙️ Adjust grading weights in `grading_config.yaml`
- 📅 Modify timeline in `timeline.yaml`
- 🎨 Customize dashboard appearance

### Create Your Own Class
- 📚 Organize materials in `Materials/` folder
- ✍️ Write quiz questions
- 🏗️ Build class with `build_class.py`
- 📦 Share with others!

---

## 🆘 Troubleshooting

### Plugins Not Working
- **Solution:** Restart Obsidian after installing plugins
- **Check:** Settings → Community Plugins → Ensure all are enabled

### Import Script Fails
- **Solution:** Check Python version (`python --version`)
- **Check:** Install dependencies (`pip install pyyaml python-frontmatter`)
- **Check:** Verify class path is correct

### Tasks Not Appearing
- **Solution:** Refresh file explorer (Ctrl/Cmd + R)
- **Check:** Look in `TaskNotes/[class_id]/` folder
- **Check:** Verify import completed successfully

### Quiz Not Grading
- **Solution:** Ensure Meta-bind plugin is enabled
- **Check:** Answer all questions before submitting
- **Check:** Look for error messages in console (Ctrl/Cmd + Shift + I)

### Progress Not Updating
- **Solution:** Mark tasks as "completed" in frontmatter
- **Check:** Refresh dashboard (close and reopen)
- **Check:** Verify `student_progress.yaml` exists
>Would be good to have the most common troubleshooting and faq 
---

## 💡 Pro Tips

### Keyboard Shortcuts
- `Ctrl/Cmd + P` - Command palette (quick access to everything)
- `Ctrl/Cmd + O` - Quick switcher (jump to any file)
- `Ctrl/Cmd + E` - Toggle edit/preview mode
- `Ctrl/Cmd + ,` - Open settings

### Efficient Studying
- Use **Pomodoro technique** (25 min study, 5 min break)
- Review **flashcards daily** for best retention
- Take **quizzes when ready**, not rushed
- **Flag difficult topics** for extra review

### Customization
- Change **theme** in Settings → Appearance
- Adjust **font size** for readability
- Create **custom CSS** for personal style
- Use **hotkeys** for frequent actions
>How to use tutorial is important. Needs to be reproducable and distributable. but also understandable
---

## 📚 Additional Resources

### Documentation
- Full docs in `OCDS_Documentation/`
- Plugin guides in `02_Plugin_Integration/`
- Examples in `13_Examples/`

### Community
- GitHub repository (coming soon)
- Discord server (coming soon)
- Video tutorials (coming soon)

### Support
- Check documentation first
- Search existing issues
- Ask in community forums
- File bug reports
>all really good things here. setting up a community would be dope. it could be a way to connect all kinds of things. could be a discord for the plugin ocds but could also be a discord for communities or schools even where people can exchange ocds files as long as they're verified.
---

## ✅ Quick Reference

### File Locations
```
Your_Vault/
├── Materials/              # Source content library
├── Classes/                # Imported classes
├── Student_Progress/       # Your progress data
├── TaskNotes/              # Daily tasks
├── OCDS_Templates/         # Templates
└── scripts/                # Automation scripts
```

### Common Commands
```bash
# Import a class
python scripts/import_class.py --class-path "path/to/class" --start-date "YYYY-MM-DD"

# Build a class
python scripts/build_class.py --class-id "CLASS_ID"

# Grade a quiz manually
python scripts/auto_grader.py --quiz-file "path/to/quiz.md"
```

### Plugin Syntax Quick Reference

**Spaced Repetition:**
```markdown
Question?
?
Answer
```

**TaskNotes:**
```yaml
status: pending | in_progress | completed
due: YYYY-MM-DD
```

**Meta-bind:**
```markdown
`INPUT[text:field_name]`
`VIEW[{field_name}][text]`
```

**Dataview:**
```dataview
LIST FROM "folder" WHERE condition
```

---

**You're all set! Happy learning! 🎓**

---

*Questions? Check the full documentation or ask in the community.*

*Last updated: 2025-11-05*
