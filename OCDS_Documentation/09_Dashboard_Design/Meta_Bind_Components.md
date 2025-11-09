# Meta-Bind Components

**Purpose:** Interactive dashboard elements using Meta-bind plugin

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

Meta-bind adds interactive elements to OCDS dashboards - buttons, progress bars, forms, and dynamic displays.

---

## 🎯 Common Components

### Progress Bars

\`\`\`meta-bind
INPUT[progressBar(
  minValue(0),
  maxValue(100),
  value(overall_grade),
  label("Overall Progress")
)]
\`\`\`

---

### Buttons

\`\`\`meta-bind-button
label: Start Quiz
style: primary
action:
  type: open
  link: "[[Classes/TCM_101/Materials/Week_05/Quiz]]"
\`\`\`

---

### Dynamic Values

\`\`\`meta-bind
VIEW{overall_grade}%
\`\`\`

---

### Input Fields

\`\`\`meta-bind
INPUT[number(
  class(mb-input),
  placeholder(Enter score)
)]
\`\`\`

---

## 📊 Dashboard Examples

### Grade Summary with Progress Bar

\`\`\`markdown
## Grade Summary

**Overall:** \`VIEW{overall_grade}\`% (\`VIEW{letter_grade}\`)

\`\`\`meta-bind
INPUT[progressBar(
  minValue(0),
  maxValue(100),
  value(overall_grade)
)]
\`\`\`
\`\`\`

---

### Quick Action Buttons

\`\`\`markdown
## Quick Actions

\`\`\`meta-bind-button
label: Continue Learning
style: primary
action:
  type: open
  link: "[[Classes/TCM_101/Materials/Week_05/Study_Material]]"
\`\`\`

\`\`\`meta-bind-button
label: Review Flashcards
style: default
action:
  type: open
  link: "[[Classes/TCM_101/Materials/Week_05/Flashcards]]"
\`\`\`
\`\`\`
>Metabind has a lot of potential but I haven't really tapped into it yet. the syntax seems to have a decent amount of depth and I haven't gotten AI to make it stick yet. would be good to build out an example note of what metabind can do.
---

## 📚 Related Documentation

- [[Progress_Dashboard.md]] - Student dashboard
- [[Instructor_Dashboard.md]] - Instructor dashboard
- [[Meta_Bind_Syntax.md]] - Complete syntax guide

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
