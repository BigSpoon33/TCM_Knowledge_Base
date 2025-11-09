# OCDS Plugin Requirements

**Complete guide to required and optional Obsidian plugins**

---

## 📦 Required Plugins

These plugins are **essential** for OCDS to function. Install all of them.

### 1. Spaced Repetition

**Purpose:** Flashcard system with spaced repetition algorithm

**Installation:**
1. Settings → Community Plugins → Browse
2. Search "Spaced Repetition"
3. Install by **st3v3nmw**
4. Enable the plugin

**OCDS Usage:**
- Flashcard review sessions
- Progress tracking (cards studied)
- Retention statistics
- Grading component (flashcard completion)

**Documentation:** `Spaced_Repetition_Guide.md`

**Links:**
- Plugin: https://github.com/st3v3nmw/obsidian-spaced-repetition
- Docs: https://www.stephenmwangi.com/obsidian-spaced-repetition/

---

### 2. TaskNotes

**Purpose:** Advanced task management with rich metadata

**Installation:**
1. Settings → Community Plugins → Browse
2. Search "TaskNotes"
3. Install by **Carlo Zottmann**
4. Enable the plugin

**OCDS Usage:**
- Daily study tasks
- Assignment scheduling
- Quiz due dates
- Task dependencies (blocking)
- Progress tracking

**Documentation:** `TaskNotes_Integration.md`

**Links:**
- Plugin: https://github.com/czottmann/obsidian-task-notes
- Docs: https://tasknotes.dev/

---

### 3. Meta Bind

**Purpose:** Interactive forms and buttons in notes

**Installation:**
1. Settings → Community Plugins → Browse
2. Search "Meta Bind"
3. Install by **Moritz Jung**
4. Enable the plugin

**OCDS Usage:**
- Quiz answer selection
- Progress dashboards
- Student info forms
- Submit buttons
- Grade displays

**Documentation:** `Meta_Bind_Syntax.md`

**Links:**
- Plugin: https://github.com/mProjectsCode/obsidian-meta-bind-plugin
- Docs: https://www.moritzjung.dev/obsidian-meta-bind-plugin-docs/

---

### 4. Dataview

**Purpose:** Dynamic queries and data aggregation

**Installation:**
1. Settings → Community Plugins → Browse
2. Search "Dataview"
3. Install by **Michael Brenan**
4. Enable the plugin

**OCDS Usage:**
- Progress dashboards
- Grade calculations
- Material listings
- Task summaries
- Statistics displays

**Documentation:** `Dataview_Queries.md`

**Links:**
- Plugin: https://github.com/blacksmithgu/obsidian-dataview
- Docs: https://blacksmithgu.github.io/obsidian-dataview/

---

### 5. Advanced Slides

**Purpose:** Create presentations from markdown

**Installation:**
1. Settings → Community Plugins → Browse
2. Search "Advanced Slides"
3. Install by **MSzturc**
4. Enable the plugin

**OCDS Usage:**
- Lecture slide decks
- Study presentations
- Visual learning materials
- Teaching resources

**Documentation:** `Advanced_Slides_Integration.md`

**Links:**
- Plugin: https://github.com/MSzturc/obsidian-advanced-slides
- Docs: https://mszturc.github.io/obsidian-advanced-slides/

---

### 6. Templater

**Purpose:** Advanced template system with scripting

**Installation:**
1. Settings → Community Plugins → Browse
2. Search "Templater"
3. Install by **SilentVoid**
4. Enable the plugin

**OCDS Usage:**
- Material generation
- Task creation
- Quiz generation
- Dynamic content

**Documentation:** `Templater_Patterns.md`

**Links:**
- Plugin: https://github.com/SilentVoid13/Templater
- Docs: https://silentvoid13.github.io/Templater/

---

## 🔧 Optional Plugins

These plugins enhance OCDS but aren't required.

### Obsidian Pomodoro

**Purpose:** Time tracking with Pomodoro technique

**Why Use It:**
- Track study time
- Enforce break intervals
- Contribute to grading (time-based component)
- Improve focus

**Installation:**
1. Settings → Community Plugins → Browse
2. Search "Obsidian Pomodoro"
3. Install and enable

**OCDS Integration:**
- Pomodoro count tracked in progress
- Optional grading component
- Study session logging

**Documentation:** `Pomodoro_Tracking.md`

---

### Charts

**Purpose:** Visualize data with charts and graphs

**Why Use It:**
- Grade trend visualization
- Progress over time
- Quiz score charts
- Flashcard retention graphs

**Installation:**
1. Settings → Community Plugins → Browse
2. Search "Charts"
3. Install and enable

**OCDS Integration:**
- Enhanced dashboards
- Visual progress tracking
- Performance analytics

---

### Kanban

**Purpose:** Kanban board task management

**Why Use It:**
- Visual task organization
- Drag-and-drop workflow
- Alternative to TaskNotes view

**Installation:**
1. Settings → Community Plugins → Browse
2. Search "Kanban"
3. Install and enable

**OCDS Integration:**
- Alternative task view
- Visual progress tracking
- Weekly planning boards

---

### Calendar

**Purpose:** Calendar view of notes and tasks

**Why Use It:**
- See study schedule visually
- Track quiz dates
- Plan study sessions

**Installation:**
1. Settings → Community Plugins → Browse
2. Search "Calendar"
3. Install and enable

**OCDS Integration:**
- Visual timeline
- Due date tracking
- Session planning

---

## ⚙️ Plugin Configuration

### Recommended Settings

#### Spaced Repetition
```
Settings → Spaced Repetition
├── Flashcard separator: "?"
├── Multiline card separator: "?"
├── Show context in cards: ON
├── Bury sibling cards: ON
└── Show card's note: ON
```

#### TaskNotes
```
Settings → TaskNotes
├── Task folder: "TaskNotes"
├── Template folder: "OCDS_Templates"
├── Date format: "YYYY-MM-DD"
└── Auto-create task notes: ON
```

#### Meta Bind
```
Settings → Meta Bind
├── Enable inline fields: ON
├── Enable buttons: ON
├── Enable view fields: ON
└── Sync frontmatter: ON
```

#### Dataview
```
Settings → Dataview
├── Enable JavaScript queries: ON
├── Enable inline queries: ON
└── Refresh interval: 2000ms
```

#### Advanced Slides
```
Settings → Advanced Slides
├── Theme: "black" (or your preference)
├── Slide number: ON
├── Progress bar: ON
└── Controls: ON
```

#### Templater
```
Settings → Templater
├── Template folder: "OCDS_Templates"
├── Enable system commands: ON
├── Trigger on file creation: ON
└── Enable folder templates: ON
```

---

## 🔍 Verification Checklist

After installing all plugins, verify they're working:

### Test Spaced Repetition
- [ ] Create a simple flashcard
- [ ] Review it in SR mode
- [ ] Verify scheduling works

### Test TaskNotes
- [ ] Create a task note with frontmatter
- [ ] Set status, due date, priority
- [ ] Verify it appears in task queries

### Test Meta Bind
- [ ] Create an input field
- [ ] Enter data
- [ ] Verify it saves to frontmatter

### Test Dataview
- [ ] Create a simple LIST query
- [ ] Verify results appear
- [ ] Test filtering

### Test Advanced Slides
- [ ] Create a simple slide deck
- [ ] Start presentation mode
- [ ] Navigate slides

### Test Templater
- [ ] Create a template with variables
- [ ] Insert template
- [ ] Verify variables populate

---

## 🐛 Troubleshooting

### Plugin Won't Install
**Problem:** "Failed to load plugin"
**Solution:**
1. Check Obsidian version (must be 1.4.0+)
2. Restart Obsidian
3. Try manual installation from GitHub

### Plugin Installed But Not Working
**Problem:** Features don't appear
**Solution:**
1. Verify plugin is **enabled** (toggle should be ON)
2. Check for plugin conflicts
3. Restart Obsidian
4. Check console for errors (Ctrl/Cmd + Shift + I)

### Syntax Not Rendering
**Problem:** Meta-bind fields show as text
**Solution:**
1. Ensure Meta Bind is enabled
2. Switch to Reading mode
3. Check syntax is correct
4. Refresh note (close and reopen)

### Queries Not Working
**Problem:** Dataview queries show no results
**Solution:**
1. Verify Dataview is enabled
2. Check query syntax
3. Ensure files have required frontmatter
4. Wait for index to refresh (2-3 seconds)

---

## 📊 Plugin Comparison

| Feature | Spaced Rep | TaskNotes | Meta Bind | Dataview | Adv Slides | Templater |
|---------|-----------|-----------|-----------|----------|------------|-----------|
| **Flashcards** | ✅ Primary | ❌ | ❌ | 📊 Query | ❌ | 🔧 Generate |
| **Tasks** | ❌ | ✅ Primary | 📝 Forms | 📊 Query | ❌ | 🔧 Generate |
| **Interactivity** | ❌ | ❌ | ✅ Primary | ❌ | ❌ | ❌ |
| **Queries** | ❌ | ❌ | ❌ | ✅ Primary | ❌ | ❌ |
| **Presentations** | ❌ | ❌ | ❌ | ❌ | ✅ Primary | ❌ |
| **Automation** | ❌ | ❌ | 🔘 Buttons | ❌ | ❌ | ✅ Primary |

Legend:
- ✅ Primary purpose
- 📊 Data display
- 📝 Data input
- 🔧 Content generation
- 🔘 Action triggers
- ❌ Not applicable

---

## 🔄 Update Policy

### Checking for Updates
1. Settings → Community Plugins
2. Click "Check for updates"
3. Update plugins as needed

### OCDS Compatibility
- **Spaced Repetition:** v1.10.0+
- **TaskNotes:** v1.0.0+
- **Meta Bind:** v0.9.0+
- **Dataview:** v0.5.0+
- **Advanced Slides:** v2.0.0+
- **Templater:** v1.16.0+

### Breaking Changes
If a plugin update breaks OCDS:
1. Check OCDS documentation for updates
2. Revert plugin to previous version
3. Report issue to OCDS maintainers

---

## 📚 Additional Resources

### Plugin Documentation
- Each plugin has detailed docs (see links above)
- OCDS-specific usage in individual guides
- Examples in `13_Examples/`

### Video Tutorials
- Plugin installation walkthrough (coming soon)
- OCDS setup guide (coming soon)
- Advanced features (coming soon)

### Community Support
- Plugin-specific Discord servers
- Obsidian forum discussions
- OCDS community (coming soon)

---

## ✅ Installation Checklist

Print this or keep it open while setting up:

### Required Plugins
- [ ] Spaced Repetition installed and enabled
- [ ] TaskNotes installed and enabled
- [ ] Meta Bind installed and enabled
- [ ] Dataview installed and enabled
- [ ] Advanced Slides installed and enabled
- [ ] Templater installed and enabled

### Optional Plugins
- [ ] Obsidian Pomodoro (if using time tracking)
- [ ] Charts (if using visualizations)
- [ ] Kanban (if using board view)
- [ ] Calendar (if using calendar view)

### Configuration
- [ ] Spaced Repetition settings configured
- [ ] TaskNotes folder set to "TaskNotes"
- [ ] Meta Bind inline fields enabled
- [ ] Dataview JavaScript enabled
- [ ] Advanced Slides theme selected
- [ ] Templater template folder set

### Verification
- [ ] All plugins show as enabled
- [ ] Test flashcard works
- [ ] Test task note works
- [ ] Test meta-bind field works
- [ ] Test dataview query works
- [ ] Test slide deck works
- [ ] Test template works

---

**All plugins installed and configured? You're ready to use OCDS! 🎉**

Next: Import your first class with `Quick_Start_Guide.md`

---

*Last updated: 2025-11-05*
*OCDS Version: 1.0.0*
