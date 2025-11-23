# Epic 12: Dashboard Quality Bar Definition

**Action Item #7 from Epic 11 Retrospective**  
**Owner:** Alice (Product Owner)  
**Created:** 2025-11-22  
**Status:** Complete  
**Purpose:** Define acceptance criteria distinguishing "functional" (Epic 11) from "polished" (Epic 12) dashboards

---

## 📋 Executive Summary

This document establishes comprehensive quality standards for polished, production-ready dashboards in the Obsidian Capsule Delivery System (OCDS). Epic 11 delivered **functional** dashboards that work correctly. Epic 12 will elevate them to **polished, production-ready** dashboards that delight users.

**Key Principle:** A polished dashboard is not just functional—it's **discoverable, beautiful, performant, and teachable**.

---

## 🎯 Quality Tier System

We define **three quality tiers** to provide clear progression and allow phased delivery within Epic 12:

| Tier | Name | Description | Epic Status |
|------|------|-------------|-------------|
| **Bronze** | Functional | Works correctly, basic layout, minimal styling | ✅ Epic 11 (Achieved) |
| **Silver** | Enhanced | Improved visual hierarchy, basic theming, better UX | 🎯 Epic 12 Minimum (Required) |
| **Gold** | Polished | Professional design, interactive widgets, full theming | 🌟 Epic 12 Target (Aspirational) |

**Epic 12 Success Criteria:** All dashboards must achieve **Silver tier minimum**, with **Gold tier as stretch goal**.

---

## 🥉 Bronze Tier: Functional (Epic 11 Baseline)

### Current State Analysis

**Strengths (What Works):**
- ✅ All Dataview queries execute correctly
- ✅ Hierarchical navigation (Master → Capsule → Content) functional
- ✅ Metadata filtering works (class, topic, category, active status)
- ✅ Progress tracking calculates correctly (TaskNotes integration)
- ✅ Domain-specific sections render (TCM: formulas, herbs, patterns)
- ✅ Dashboard generation during import works
- ✅ File counts accurate (root notes, study materials)
- ✅ Recent activity tracking works

**Gaps (What Needs Improvement):**
- ❌ No visual hierarchy or theming
- ❌ Plain markdown headings (no styling, no emojis, no icons)
- ❌ No interactive elements (all read-only queries)
- ❌ No CSS customization or color coding
- ❌ Long query results lack pagination or limiting
- ❌ No helpful tooltips or user guidance
- ❌ Mobile experience not optimized
- ❌ No progressive disclosure (everything visible at once)
- ❌ No visual feedback for user actions

**Bronze Tier Example (Current Master Dashboard):**
```markdown
# Master Dashboard - My Knowledge System

> **Plugin Required**: This dashboard requires Dataview v0.5.0+.

---

## 📚 Installed Capsules

[Dataview table with no styling]
```

**Assessment:** Functional but utilitarian. Gets the job done but lacks polish and delight.

---

## 🥈 Silver Tier: Enhanced (Epic 12 Minimum)

Silver tier represents the **minimum viable polish** for production release. Dashboards must be visually organized, easy to scan, and pleasant to use.

### 1. Visual Design Standards

#### Layout & Spacing
- **Requirement:** Consistent visual rhythm using horizontal rules, section spacing
- **Standard:** 
  - Section breaks use `---` with emoji headers
  - Related content grouped with consistent spacing
  - White space used intentionally to separate concepts
  
**Example:**
```markdown
---

## 📚 Installed Capsules

[Content here]

---

## 📊 Progress Overview

[Content here]

---
```

**Acceptance Criteria:**
- [ ] All sections clearly separated with horizontal rules
- [ ] Section headers use consistent emoji system (📚 = content, 📊 = stats, 🔍 = search)
- [ ] No large walls of unbroken text

#### Visual Hierarchy
- **Requirement:** Clear information architecture using heading levels
- **Standard:**
  - H1 (`#`) = Dashboard title only
  - H2 (`##`) = Major sections
  - H3 (`###`) = Subsections within major sections
  - H4 (`####`) = Tertiary details (use sparingly)
  
**Acceptance Criteria:**
- [ ] Heading levels never skip (H2 → H4 is invalid)
- [ ] Each dashboard has exactly one H1
- [ ] Section hierarchy immediately understandable by scanning

#### Typography & Readability
- **Requirement:** Consistent text formatting for different content types
- **Standard:**
  - **Bold** for labels and emphasis
  - *Italic* for helper text, notes, metadata
  - `Code` for technical values (IDs, versions, file paths)
  - > Blockquotes for warnings, tips, important notices
  
**Example:**
```markdown
**Capsule ID:** `tcm-formulas-v1.2.0`  
**Last Updated:** 2025-11-22  
*Status:* Active

> **Tip:** Click any formula name to view full details.
```

**Acceptance Criteria:**
- [ ] Labels consistently bold across all sections
- [ ] Technical values in code formatting
- [ ] Helper text differentiated from primary content

#### Color Coding System
- **Requirement:** Semantic use of emojis for visual scanning
- **Standard:**
  - 📚 Libraries/Collections (capsules, notes, materials)
  - 📊 Statistics/Analytics (progress, counts, percentages)
  - 🔍 Search/Filter (queries, interactive filters)
  - ✅ Success/Complete (100% progress, active status)
  - ⚠️ Warning/Attention (incomplete, requires action)
  - 🎯 Goals/Targets (milestones, objectives)
  - 🔗 Navigation/Links (related content, cross-refs)
  - 📅 Time/Schedule (dates, timelines, recent activity)
  - 🎓 Study/Learning (flashcards, quizzes, materials)
  
**Acceptance Criteria:**
- [ ] Emoji usage consistent across all dashboards
- [ ] Color coding aids visual scanning (can find sections by emoji)
- [ ] Emojis not overused (no emoji spam)

### 2. Functional Requirements

#### Query Performance
- **Requirement:** All queries execute in <2 seconds on typical vaults
- **Standard:**
  - Queries limited to reasonable result sets (LIMIT clause)
  - DataviewJS optimized for performance
  - Loading states or warnings for slow queries
  
**Example:**
```markdown
## 📅 Recent Activity

> 📊 Showing last 20 updates. [View All →](link)

[Dataview query with LIMIT 20]
```

**Acceptance Criteria:**
- [ ] All queries include LIMIT clause (except when <50 results expected)
- [ ] Slow queries (>50 items) have warnings or progressive loading
- [ ] Performance tested with 100+ capsules, 1000+ notes

#### Error Handling
- **Requirement:** Graceful degradation when data missing
- **Standard:**
  - Empty states explain why (no data vs. wrong folder)
  - Helpful next actions suggested
  - No broken queries or undefined values
  
**Example:**
```markdown
## 📚 Installed Capsules

> ℹ️ No capsules found. [Import your first capsule →](link)
```

**Acceptance Criteria:**
- [ ] Empty states for all sections with zero results
- [ ] Error messages actionable (tell user what to do)
- [ ] No JavaScript errors in console

#### Navigation Clarity
- **Requirement:** Users always know where they are and how to get elsewhere
- **Standard:**
  - Breadcrumb navigation at top
  - "Back to X" links clearly marked
  - Related dashboards linked in footer
  
**Example:**
```markdown
# Capsule Dashboard: TCM Formulas v1.2.0

[[Master-Dashboard|← Back to All Capsules]]

---

[Dashboard content]

---

## 🔗 Related

- [[Master-Dashboard|All Capsules]]
- [[TCM_Herbs/Dashboard|TCM Herbs Capsule]]
- [[Help|User Guide]]
```

**Acceptance Criteria:**
- [ ] Every capsule dashboard links back to master
- [ ] Master dashboard links to all capsules
- [ ] Related dashboards suggested in footer

### 3. Content Standards

#### Information Completeness
- **Requirement:** All dashboard sections provide expected information
- **Standard (Master Dashboard):**
  - List of all installed capsules with metadata
  - Aggregate progress overview
  - Interactive filtering by class, topic, category
  - Recent activity (last 7 days)
  - Cross-capsule connections
  - Quick links to all capsule dashboards
  
- **Standard (Capsule Dashboard):**
  - Capsule metadata (ID, version, domain, mode)
  - Navigation back to master
  - Total counts (root notes, study materials)
  - List of all root notes with types/tags
  - List of all study materials by type
  - Progress tracking (if sequenced mode)
  - Domain-specific sections (formulas, herbs, etc.)
  - Recent activity within capsule
  
**Acceptance Criteria:**
- [ ] All standard sections present in master dashboard
- [ ] All standard sections present in capsule dashboards
- [ ] Domain sections appear for domain-specific capsules

#### Metadata Visibility
- **Requirement:** Important metadata surfaced prominently
- **Standard:**
  - Capsule version, ID visible
  - Last updated timestamp
  - Plugin requirements noted
  - Domain type and sequence mode displayed
  
**Acceptance Criteria:**
- [ ] Capsule ID and version in overview section
- [ ] Last updated timestamp auto-refreshes
- [ ] Plugin dependencies documented

### 4. User Experience Criteria

#### Ease of Use
- **Requirement:** Non-technical users can navigate without training
- **Standard:**
  - Clear section labels (avoid jargon)
  - Helpful tooltips/notes where needed
  - Obvious interactive elements
  - Self-explanatory queries
  
**Example:**
```markdown
## 🔍 Find Capsules

> Type in the fields below to filter your capsules. Leave blank to show all.

**Class:** <input type="text" id="classFilter" placeholder="e.g., TCM101">
```

**Acceptance Criteria:**
- [ ] All interactive elements have instructions
- [ ] Technical terms explained or avoided
- [ ] Users can accomplish tasks without documentation

#### Discoverability
- **Requirement:** Features are obvious, not hidden
- **Standard:**
  - Interactive filters labeled clearly
  - Buttons/links stand out from text
  - Progressive disclosure used (summaries → details)
  - "What you can do here" sections
  
**Acceptance Criteria:**
- [ ] All filters/buttons discoverable without scrolling
- [ ] Feature availability obvious (not buried in text)
- [ ] Users don't miss key functionality

#### Consistency
- **Requirement:** Same patterns across all dashboards
- **Standard:**
  - Same emoji system everywhere
  - Same section ordering (Overview → Navigation → Content → Activity)
  - Same query table format
  - Same typography conventions
  
**Acceptance Criteria:**
- [ ] Master dashboard and all capsule dashboards use same design language
- [ ] Section order logical and consistent
- [ ] No surprises or unexpected patterns

### 5. Technical Standards

#### Performance Benchmarks
- **Requirement:** Dashboard loads and updates quickly
- **Metrics:**
  - Initial render: <3 seconds
  - Filter interaction: <1 second response
  - Query refresh: <2 seconds
  
**Acceptance Criteria:**
- [ ] Tested with vault containing 100 capsules, 1000 notes
- [ ] No blocking operations during render
- [ ] Smooth scrolling and interaction

#### Maintainability
- **Requirement:** Templates are easy to understand and modify
- **Standard:**
  - Jinja2 templates well-commented
  - Query helpers documented
  - Template variables clearly named
  - Domain templates follow standard pattern
  
**Acceptance Criteria:**
- [ ] Template variables use descriptive names
- [ ] Complex queries have explanatory comments
- [ ] Domain template creation guide exists

#### Mobile Compatibility
- **Requirement:** Dashboards readable on mobile Obsidian
- **Standard:**
  - Tables not excessively wide
  - Interactive filters work on touch
  - Text readable without zooming
  - No horizontal scrolling
  
**Acceptance Criteria:**
- [ ] Tested on Obsidian mobile (iOS/Android)
- [ ] Tables use responsive design
- [ ] Touch targets appropriately sized

### 6. Obsidian-Specific Best Practices

#### Plugin Usage Standards
- **Requirement:** Proper use of Dataview, Meta-Bind (Silver tier focuses on Dataview)
- **Standard:**
  - Dataview queries use DQL for simple cases
  - DataviewJS for complex aggregation/filtering
  - Inline queries (`=`) for single values
  - Table queries for lists
  - Task queries for TaskNotes
  
**Acceptance Criteria:**
- [ ] Right query type for each use case
- [ ] No overuse of DataviewJS where DQL suffices
- [ ] Queries follow dataview_queries.py patterns

#### Link Strategy
- **Requirement:** Wikilinks used correctly
- **Standard:**
  - Internal navigation uses [[wikilinks]]
  - External docs use markdown links
  - Link text descriptive (not "click here")
  
**Acceptance Criteria:**
- [ ] All internal links use wikilink format
- [ ] Link text makes sense out of context
- [ ] Broken links caught in validation

#### Mobile Optimization
- **Requirement:** Works well on Obsidian Mobile
- **Standard:**
  - Avoid overly wide tables
  - Use collapsible sections where appropriate
  - Test on actual mobile devices
  
**Acceptance Criteria:**
- [ ] Tables fit mobile screen width
- [ ] No tiny fonts or touch targets
- [ ] Core functionality accessible on mobile

---

## 🌟 Gold Tier: Polished (Epic 12 Target)

Gold tier represents the **aspirational target** for Epic 12. If time permits, elevate dashboards to this level. If not, these become enhancement opportunities post-Epic 12.

### 1. Advanced Visual Design

#### Custom CSS Theming
- **Enhancement:** Custom CSS snippets for OCDS dashboards
- **Features:**
  - Neon/gradient theme option (inspired by HOCA-1/neon-homepage-vault)
  - Dark/light mode variants
  - Color-coded progress bars
  - Custom card layouts for capsules
  - Animated transitions
  
**Example Visual:**
```css
/* Custom OCDS Dashboard Theme */
.dashboard-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  padding: 20px;
  margin: 10px 0;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.capsule-card {
  border-left: 4px solid #667eea;
  padding-left: 15px;
}

.progress-complete {
  color: #10b981;
  font-weight: bold;
}
```

**Gold Standard:**
- [ ] Three theme options: Default, Neon, Academic
- [ ] CSS snippets bundled with system
- [ ] Theme switcher in master dashboard

#### Advanced Typography
- **Enhancement:** Custom fonts, advanced formatting
- **Features:**
  - Heading fonts optimized for readability
  - Monospace for technical content
  - Line height and spacing optimized
  - Visual dividers beyond horizontal rules
  
**Gold Standard:**
- [ ] Custom font stack defined
- [ ] Typography CSS snippet available
- [ ] Visual rhythm feels professional

#### Data Visualization
- **Enhancement:** Visual charts and graphs (beyond text)
- **Features:**
  - Progress bars (visual, not just percentages)
  - Sparklines for trends
  - Pie charts for distributions
  - Timeline visualizations
  
**Example (using DataviewJS + Unicode):**
```markdown
## 📊 Progress Breakdown

**Formulas:** ████████████░░░░░░░░ 60% (30/50)
**Herbs:** ██████████████████░░ 90% (45/50)
**Patterns:** ██████░░░░░░░░░░░░░░ 30% (15/50)
```

**Gold Standard:**
- [ ] Progress bars for all completion metrics
- [ ] Visual trend indicators (↗️ improving, ↘️ declining)
- [ ] Data visualization guide for developers

### 2. Interactive Widgets (Meta-Bind Integration)

#### Interactive Filters
- **Enhancement:** Meta-Bind form controls for filtering
- **Features:**
  - Dropdown selects (not just text inputs)
  - Multi-select checkboxes
  - Radio buttons for exclusive choices
  - Date pickers for timeline filtering
  
**Example:**
```markdown
## 🔍 Filter Capsules

```meta-bind
INPUT[select(option(All), option(TCM), option(Coding), option(Cooking)):domain]
INPUT[toggle:activeOnly]
```

**Gold Standard:**
- [ ] All major filters use Meta-Bind controls
- [ ] Form state persists across sessions
- [ ] Visual feedback on filter changes

#### Action Buttons
- **Enhancement:** Clickable buttons for common actions
- **Features:**
  - "Import New Capsule" button
  - "Generate Study Materials" button
  - "Refresh Dashboard" button
  - "View All" expansion buttons
  
**Example:**
```markdown
```meta-bind-button
label: 📥 Import New Capsule
style: primary
action:
  type: command
  command: capsule:import
```

**Gold Standard:**
- [ ] All common actions have button shortcuts
- [ ] Button styling consistent with theme
- [ ] Buttons provide visual feedback on click

#### Dynamic Content
- **Enhancement:** Content updates based on user input
- **Features:**
  - Filter results update in real-time
  - Conditional sections (show/hide based on state)
  - Drill-down details (click to expand)
  
**Gold Standard:**
- [ ] Real-time filter updates (no refresh needed)
- [ ] Smooth transitions on content changes
- [ ] Progressive disclosure implemented

### 3. Advanced Plugin Integration

#### Templater Integration
- **Enhancement:** Dynamic content generation via Templater
- **Features:**
  - "Create New Capsule" wizard
  - Study material quick-add buttons
  - Dynamic date/time insertions
  - Custom scripts for common tasks
  
**Gold Standard:**
- [ ] One-click study material creation
- [ ] Wizard for capsule metadata entry
- [ ] Templater patterns documented

#### Spaced Repetition Integration
- **Enhancement:** Flashcard stats in dashboards
- **Features:**
  - Cards due today/this week
  - Retention percentages
  - Study streak tracking
  - Quick links to review sessions
  
**Gold Standard:**
- [ ] SR stats visible in capsule dashboards
- [ ] "Start Review" buttons for capsules with flashcards
- [ ] Study progress tracked over time

#### TaskNotes Advanced Features
- **Enhancement:** Rich task management displays
- **Features:**
  - Kanban-style task boards
  - Task dependency visualization
  - Time tracking integration
  - Burndown charts
  
**Gold Standard:**
- [ ] Visual task boards in dashboards
- [ ] Task trends and analytics
- [ ] Time-to-completion estimates

### 4. UX Excellence

#### Onboarding Experience
- **Enhancement:** Help new users get started
- **Features:**
  - "First time here?" welcome section
  - Interactive tour/walkthrough
  - Quick start checklist
  - Video tutorials embedded
  
**Gold Standard:**
- [ ] New user welcome on first load
- [ ] Contextual help tooltips
- [ ] "Getting Started" checklist

#### Search & Discovery
- **Enhancement:** Better content discovery
- **Features:**
  - Global search across all capsules
  - Tag cloud visualization
  - "Related content" suggestions
  - Recent/popular content surfacing
  
**Gold Standard:**
- [ ] Unified search across dashboards
- [ ] Smart recommendations based on activity
- [ ] Content discovery features

#### Accessibility
- **Enhancement:** WCAG compliance
- **Features:**
  - Screen reader friendly
  - Keyboard navigation
  - High contrast mode
  - Text size flexibility
  
**Gold Standard:**
- [ ] WCAG 2.1 AA compliance
- [ ] All features keyboard-accessible
- [ ] Accessibility testing completed

### 5. Polish & Delight

#### Micro-interactions
- **Enhancement:** Small delightful touches
- **Features:**
  - Hover effects on interactive elements
  - Smooth transitions and animations
  - Loading spinners for async operations
  - Celebration animations on milestones
  
**Gold Standard:**
- [ ] Hover states on all clickable elements
- [ ] Smooth fade-ins for content
- [ ] Confetti on 100% completion 🎉

#### Easter Eggs & Personality
- **Enhancement:** Character and charm
- **Features:**
  - Encouraging messages on progress milestones
  - Fun fact tooltips
  - Themed seasonal variations
  - Customizable mascot/avatar
  
**Gold Standard:**
- [ ] Personality consistent with OCDS brand
- [ ] Easter eggs discoverable but not intrusive
- [ ] User can customize personality level

#### Performance Optimization
- **Enhancement:** Lightning-fast dashboards
- **Features:**
  - Query result caching
  - Lazy loading for large datasets
  - Optimized DataviewJS
  - Preloading common views
  
**Gold Standard:**
- [ ] Dashboard loads in <1 second
- [ ] Queries cached intelligently
- [ ] No jank or lag on interaction

---

## 📏 Measurable Standards & Acceptance Criteria

### Quantitative Metrics

#### Performance Metrics
| Metric | Bronze (Baseline) | Silver (Minimum) | Gold (Target) |
|--------|-------------------|------------------|---------------|
| Initial Load Time | <5 sec | <3 sec | <1 sec |
| Query Response Time | <5 sec | <2 sec | <500ms |
| Filter Interaction | N/A | <1 sec | <300ms |
| Mobile Load Time | Untested | <5 sec | <2 sec |
| Scroll Performance | Acceptable | Smooth 60fps | Buttery 60fps |

#### Content Metrics
| Metric | Bronze (Baseline) | Silver (Minimum) | Gold (Target) |
|--------|-------------------|------------------|---------------|
| Section Count (Master) | 8 | 8-10 | 10-12 |
| Section Count (Capsule) | 6-8 | 8-10 | 10-15 |
| Emoji Usage | Inconsistent | Standardized | Themed |
| Interactive Elements | 1 (filter) | 3-5 | 8-10 |
| Documentation Links | 1-2 | 5+ | 10+ |

#### User Experience Metrics
| Metric | Bronze (Baseline) | Silver (Minimum) | Gold (Target) |
|--------|-------------------|------------------|---------------|
| Click Depth to Content | 3-4 | 2-3 | 1-2 |
| Empty States Handled | 50% | 100% | 100% + suggestions |
| Mobile Usability | Not tested | Functional | Optimized |
| Discoverability Score | Low | Medium | High |
| New User Onboarding | None | Basic | Guided |

### Qualitative Standards

#### Visual Quality Checklist
- [ ] **Information Hierarchy:** Can identify most important info at a glance
- [ ] **Scannability:** Section headers stand out; easy to find specific section
- [ ] **Visual Balance:** No cramped or sparse sections; even spacing
- [ ] **Color Psychology:** Emojis/colors reinforce meaning (green=good, red=warning)
- [ ] **Professional Appearance:** Looks intentionally designed, not default Markdown

#### Functional Quality Checklist
- [ ] **Zero Errors:** No broken queries, no console errors
- [ ] **Complete Information:** All expected data present
- [ ] **Accurate Counts:** File counts, percentages match reality
- [ ] **Working Links:** All wikilinks resolve correctly
- [ ] **Graceful Degradation:** Works even with missing plugins (degrades to static)

#### UX Quality Checklist
- [ ] **Intuitive Navigation:** Users find what they need without help
- [ ] **Clear Feedback:** Actions provide visible response
- [ ] **Error Recovery:** Users can fix mistakes easily
- [ ] **Helpful Guidance:** Instructions/tooltips where needed
- [ ] **Satisfying Experience:** Users feel accomplished, not frustrated

---

## 🎨 Examples & Reference Implementations

### Example 1: Silver Tier Master Dashboard (Minimum Viable Polish)

```markdown
---
type: master_dashboard
title: "OCDS Knowledge System"
created: "2025-11-22T19:40:33-08:00"
updated: "2025-11-22T19:40:33-08:00"
---

# 🎓 My Knowledge System

> **Welcome!** This is your command center for all learning capsules.  
> **New here?** Start with [[Quick-Start-Guide|Getting Started →]]

---

## 📊 Overview

**Total Capsules:** `= dv.pages().where(p => p.type === "capsule_dashboard").length`  
**Total Notes:** `= dv.pages().where(p => p.source_capsules).length`  
**Last Activity:** `= dv.pages().where(p => p.source_capsules).sort(p => p.file.mtime, 'desc').first().file.mtime`

---

## 🔍 Find Your Capsules

> Filter by class, topic, or category. Leave fields blank to show all.

**Class:** <input type="text" id="classFilter" placeholder="e.g., TCM101">  
**Topic:** <input type="text" id="topicFilter" placeholder="e.g., Herbal Medicine">  
**Category:** <input type="text" id="categoryFilter" placeholder="e.g., CALE">  
**Status:** <select id="activeFilter"><option>All</option><option>Active</option><option>Inactive</option></select>

```dataviewjs
// [Interactive filtering code - optimized for performance]
```

---

## 📚 All Capsules

```dataview
TABLE 
  capsule_id as "ID",
  version as "Version",
  dashboard_metadata.topic as "Topic",
  dashboard_metadata.category as "Category"
FROM ""
WHERE type = "capsule_dashboard"
SORT file.name ASC
```

> **Tip:** Click any capsule name to view its dashboard.

---

## 📅 Recent Activity (Last 7 Days)

```dataview
TABLE 
  type as "Type", 
  file.mtime as "Updated"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
  AND source_capsules
SORT file.mtime DESC
LIMIT 20
```

> Showing 20 most recent updates. [[All-Activity|View all →]]

---

## 🔗 Quick Links

- [[TCM_Formulas/Dashboard|TCM Formulas]]
- [[TCM_Herbs/Dashboard|TCM Herbs]]
- [[TCM_Patterns/Dashboard|TCM Patterns]]
- [[Help|User Guide]] | [[FAQ]] | [[Community]]

---

*Dashboard auto-refreshes every 2 seconds* | *Powered by Dataview v0.5.0+*
```

**Why This is Silver Tier:**
- ✅ Clear visual hierarchy (sections, spacing)
- ✅ Consistent emoji system
- ✅ Helpful instructions and tooltips
- ✅ Performance limits (LIMIT 20)
- ✅ Empty state handling (tips)
- ✅ Professional typography
- ❌ No custom CSS theming (Gold)
- ❌ No Meta-Bind widgets (Gold)
- ❌ No data visualizations (Gold)

### Example 2: Gold Tier Capsule Dashboard (Aspirational)

```markdown
---
type: capsule_dashboard
capsule_id: "tcm-formulas-v1.2.0"
version: "1.2.0"
theme: "neon"
---

# 🌿 TCM Formulas v1.2.0

<div class="dashboard-header">
  <div class="metadata">
    <span class="badge badge-primary">Active</span>
    <span class="badge badge-info">TCM Domain</span>
    <span class="badge badge-success">90% Complete</span>
  </div>
  <div class="actions">
    ```meta-bind-button
    label: 📥 Import Update
    style: primary
    ```
    ```meta-bind-button
    label: 🎓 Start Study Session
    style: default
    ```
  </div>
</div>

[[Master-Dashboard|← All Capsules]] | [[TCM_Herbs/Dashboard|TCM Herbs →]]

---

## 📊 Progress Overview

<div class="progress-section">
  <div class="progress-card">
    <h4>📝 Root Notes</h4>
    <div class="progress-bar">
      <div class="progress-fill" style="width: 90%"></div>
    </div>
    <p>45/50 Complete (90%)</p>
  </div>
  
  <div class="progress-card">
    <h4>🎴 Flashcards</h4>
    <div class="progress-bar">
      <div class="progress-fill" style="width: 75%"></div>
    </div>
    <p>150/200 Reviewed (75%)</p>
  </div>
  
  <div class="progress-card">
    <h4>✅ Quizzes</h4>
    <div class="progress-bar">
      <div class="progress-fill" style="width: 100%"></div>
    </div>
    <p>10/10 Complete (100%) 🎉</p>
  </div>
</div>

---

## 🌿 Formulas by Category

```meta-bind
INPUT[suggester(optionQuery("formulas"), useLinks(true)):selectedFormula]
```

```dataviewjs
// Dynamic formula details based on selection
```

### Top Formulas This Week

```dataview
TABLE WITHOUT ID
  file.link as "Formula",
  pattern_data.functions as "Functions",
  "⭐".repeat(popularity) as "Popular"
FROM "TCM_Formulas"
WHERE source_capsules = "tcm-formulas-v1.2.0"
  AND file.mtime >= date(today) - dur(7 days)
SORT popularity DESC
LIMIT 5
```

---

## 🎓 Study Materials

### 🎴 Flashcard Decks

```dataview
LIST
  "📊 " + cards_total + " cards | " + cards_studied + " studied | Next review: " + next_review
FROM ""
WHERE type = "flashcard" AND contains(source_capsules, "tcm-formulas-v1.2.0")
```

```meta-bind-button
label: 🚀 Start Review Session
style: primary
action:
  type: command
  command: spaced-repetition:review
```

### 📝 Quizzes

```dataview
TABLE
  quiz_data.difficulty as "Level",
  quiz_data.score as "Score",
  quiz_data.attempts as "Attempts"
FROM ""
WHERE type = "quiz" AND contains(source_capsules, "tcm-formulas-v1.2.0")
SORT quiz_data.score DESC
```

---

## 🔗 Related Capsules

- [[TCM_Herbs/Dashboard|🌱 TCM Herbs]] - Herb ingredients for these formulas
- [[TCM_Patterns/Dashboard|🔮 TCM Patterns]] - Conditions treated by formulas
- [[TCM_Points/Dashboard|📍 Acupuncture Points]] - Point prescriptions

---

## 📈 Your Stats

**Study Streak:** 🔥 7 days  
**Total Study Time:** ⏱️ 12h 34m  
**Cards Mastered:** ⭐ 89/200  
**Avg Quiz Score:** 📊 87%

> 💡 **Tip:** You're doing great! Keep up the daily study habit.

---

<div class="dashboard-footer">
  <p><em>Last updated: 2 minutes ago</em> | <a href="help">Help</a> | <a href="settings">Settings</a></p>
</div>
```

**Why This is Gold Tier:**
- ✅ Custom CSS theming (neon theme)
- ✅ Meta-Bind interactive widgets
- ✅ Visual progress bars
- ✅ Action buttons for common tasks
- ✅ Spaced Repetition integration
- ✅ Study stats and streaks
- ✅ Dynamic content based on user input
- ✅ Personality and encouragement
- ✅ Related content discovery
- ✅ Professional card-based layout

---

## 🎯 Acceptance Criteria by Tier

### Silver Tier (Epic 12 Minimum) - Must Have

**Visual Design:**
- [ ] All sections use consistent emoji system
- [ ] Horizontal rules separate major sections
- [ ] Heading hierarchy correct (H1 → H2 → H3)
- [ ] Labels bold, metadata italic, IDs in code blocks
- [ ] White space used intentionally

**Functionality:**
- [ ] All queries execute in <2 seconds
- [ ] All queries include LIMIT clause or warning
- [ ] Empty states for zero results
- [ ] Error messages actionable
- [ ] Navigation breadcrumbs present

**Content:**
- [ ] All standard sections present (see standards above)
- [ ] Metadata visible (ID, version, timestamp)
- [ ] Plugin requirements documented
- [ ] Domain sections for domain capsules

**UX:**
- [ ] Non-technical users can navigate
- [ ] Interactive elements have instructions
- [ ] Features discoverable without scrolling
- [ ] Consistent patterns across all dashboards

**Technical:**
- [ ] Performance tested (100 capsules, 1000 notes)
- [ ] Mobile compatible (readable, no horizontal scroll)
- [ ] Templates well-commented
- [ ] Query helpers documented

**Obsidian:**
- [ ] Right query type for each use case
- [ ] Wikilinks used correctly
- [ ] Works on Obsidian mobile

### Gold Tier (Epic 12 Target) - Should Have

**Visual Design:**
- [ ] Custom CSS theme available (at least 1)
- [ ] Advanced typography (fonts, spacing)
- [ ] Visual data representations (progress bars)

**Interactivity:**
- [ ] Meta-Bind filters (dropdowns, toggles)
- [ ] Action buttons for common tasks
- [ ] Dynamic content updates

**Integration:**
- [ ] Templater quick-add features
- [ ] Spaced Repetition stats
- [ ] TaskNotes advanced features

**UX:**
- [ ] Onboarding for new users
- [ ] Search and discovery features
- [ ] Accessibility (WCAG AA)

**Polish:**
- [ ] Micro-interactions (hover, transitions)
- [ ] Personality and encouragement
- [ ] Performance optimization (<1s load)

---

## 🚀 Epic 12 Implementation Strategy

### Phase 1: Silver Tier Foundation (Week 1)
**Goal:** Achieve minimum viable polish on all dashboards

**Stories:**
1. Apply consistent emoji system and visual hierarchy
2. Implement empty states and error handling
3. Add helpful tooltips and instructions
4. Optimize query performance (LIMIT clauses)
5. Mobile compatibility testing and fixes
6. Navigation breadcrumbs and cross-links

**Deliverable:** All dashboards meet Silver tier standards

### Phase 2: Gold Tier Enhancements (Week 2)
**Goal:** Add interactive and visual enhancements (time permitting)

**Stories:**
7. CSS theming system (at least 1 theme)
8. Meta-Bind interactive filters
9. Action buttons for common tasks
10. Data visualizations (progress bars, charts)
11. Plugin integrations (Templater, SR)
12. Micro-interactions and polish

**Deliverable:** Gold tier features on priority dashboards (Master + TCM capsules)

### Phase 3: Documentation & Polish (Week 3)
**Goal:** Document and refine

**Stories:**
13. Dashboard user guide with screenshots
14. Theme customization guide
15. Developer guide for dashboard creation
16. Tutorial capsule creation (showcase all features)

**Deliverable:** Comprehensive documentation and tutorial

---

## 📚 References & Inspiration

### Existing Dashboards (Baseline)
- [Master-Dashboard.md](../../Master-Dashboard.md) - Epic 11 functional master dashboard
- [Student Dashboard.md](../../Student Dashboard.md) - Academic diagnostic dashboard
- [Academic Dashboard Test.md](../../Academic Dashboard Test.md) - TCM101 course dashboard

### External Inspiration (Gold Tier)
- [HOCA-1/neon-homepage-vault](https://github.com/HOCA-1/neon-homepage-vault) - Neon theme aesthetic
- [rafaelveiga/obsidian-widgets](https://github.com/rafaelveiga/obsidian-widgets) - Interactive widgets
- [olrenso/obsidian-home-tab](https://github.com/olrenso/obsidian-home-tab) - Home tab design
- [mirnovov/obsidian-homepage](https://github.com/mirnovov/obsidian-homepage) - Homepage plugin
- [TfTHacker/DashboardPlusPlus](https://github.com/TfTHacker/DashboardPlusPlus) - Advanced dashboards

### Documentation
- [Epic 11 Retrospective](epic-11-retro-2025-11-22.md)
- [Tech Spec Epic 11](tech-spec-epic-11.md)
- [Progress Dashboard Design](../../OCDS_Documentation/09_Dashboard_Design/Progress_Dashboard.md)
- [Plugin Requirements](../../OCDS_Documentation/02_Plugin_Integration/Plugin_Requirements.md)

---

## ✅ Sign-Off

**Document Status:** ✅ Complete  
**Action Item:** #7 from Epic 11 Retrospective  
**Owner:** Alice (Product Owner)  
**Reviewed By:** BMad (Project Lead), Charlie (Senior Dev)  
**Date:** 2025-11-22

**Approval for Epic 12 Planning:** ✅ APPROVED

This quality bar provides clear, measurable standards for Epic 12. Silver tier is achievable and represents production-ready dashboards. Gold tier is aspirational and allows for phased excellence.

**Next Steps:**
1. Charlie to complete Action Item #8 (CSS theming research)
2. Elena to complete Action Item #9 (Meta-Bind evaluation)
3. Alice to complete Action Item #10 (Epic 12 story breakdown)
4. Team to begin Epic 12 planning session with this quality bar as foundation

---

*Last updated: 2025-11-22*  
*Epic 12: Dashboard Polish & Interactivity - Prep Sprint*
