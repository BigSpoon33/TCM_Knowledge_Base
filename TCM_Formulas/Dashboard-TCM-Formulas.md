---
type: capsule_dashboard
capsule_id: "tcm-formulas-v1"
version: "1.0.0"
created: "2025-11-22T19:40:33-08:00"
updated: "2025-11-22T19:40:33-08:00"

# Dashboard Metadata (optional - for filtering in master dashboard)
dashboard_metadata:
  class: "TCM101"
  topic: "Formulas"
  category: "CALE"
  active: true

# Provenance Tracking
source_capsules: ["tcm-formulas-v1"]
---

# Capsule Dashboard: TCM Formulas

> **Plugin Required**: This dashboard requires [Dataview](https://github.com/blacksmithgu/obsidian-dataview) v0.5.0+.
> Queries below will appear as code blocks until the plugin is installed.

## Overview

- **Capsule ID:** `tcm-formulas-v1`
- **Version:** 1.0.0
- **Domain:** tcm
- **Sequence Mode:** independent

**Quick Links:**
- [[Master-Dashboard|← Back to All Capsules]]
- **Total Root Notes:** `$= dv.pages().where(p => p.source_capsules && p.source_capsules.includes("tcm-formulas-v1") && p.type != "dashboard" && p.type != "capsule_dashboard").length`
- **Total Study Materials:** `$= dv.pages().where(p => p.source_capsules && p.source_capsules.includes("tcm-formulas-v1") && ["flashcard", "quiz", "slide", "conversation"].includes(p.type)).length`

---

## Root Notes

```dataview
TABLE type, tags, updated
FROM "TCM_Formulas"
WHERE contains(source_capsules, "tcm-formulas-v1")
  AND type != "dashboard"
  AND type != "capsule_dashboard"
  AND type != "quiz"
  AND type != "flashcard"
  AND type != "slide"
  AND type != "conversation"
SORT name ASC
```

---

## Study Materials

### Flashcards
```dataview
LIST
FROM "TCM_Formulas"
WHERE contains(source_capsules, "tcm-formulas-v1")
  AND type = "flashcard"
SORT file.name ASC
```

### Quizzes
```dataview
TABLE quiz_data.difficulty as "Difficulty", quiz_data.topic as "Topic"
FROM "TCM_Formulas"
WHERE contains(source_capsules, "tcm-formulas-v1")
  AND type = "quiz"
SORT file.name ASC
```

---

## Recent Activity

```dataview
TABLE type, updated
FROM "TCM_Formulas"
WHERE contains(source_capsules, "tcm-formulas-v1")
SORT updated DESC
LIMIT 10
```

---

## Domain-Specific Sections

### TCM Domain: Formulas

#### All Formulas
```dataview
TABLE 
  source as "Source",
  created as "Added",
  status as "Status"
FROM "TCM_Formulas"
WHERE contains(source_capsules, "tcm-formulas-v1")
SORT file.name ASC
```

#### Formulas by Source
```dataview
TABLE rows.file.link as "Formula"
FROM "TCM_Formulas"
WHERE contains(source_capsules, "tcm-formulas-v1")
  AND source
GROUP BY source
SORT key ASC
```

#### Recently Added Formulas
```dataview
TABLE 
  created as "Date Added",
  source as "Source"
FROM "TCM_Formulas"
WHERE contains(source_capsules, "tcm-formulas-v1")
SORT created DESC
LIMIT 20
```

#### Formulas Needing Review
```dataview
LIST
FROM "TCM_Formulas"
WHERE contains(source_capsules, "tcm-formulas-v1")
  AND status = "needs_review"
SORT file.name ASC
```
