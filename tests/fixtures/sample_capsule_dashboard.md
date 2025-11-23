---
# Universal Dashboard Fields (Required)
type: capsule_dashboard
capsule_id: "TCM_Herbs_Test_v1"
version: "1.0.0"
created: "2025-11-22T10:00:00Z"
updated: "2025-11-22T10:00:00Z"

# Dashboard Metadata (Optional - for filtering)
dashboard_metadata:
  class: "TCM101"
  topic: "Herbal Medicine"
  category: "CALE"
  active: true

# Provenance Tracking
source_capsules: ["TCM_Herbs_Test_v1"]
---

# Capsule Dashboard: TCM Materia Medica - Herbs (Test)

## Overview

- **Capsule ID:** `TCM_Herbs_Test_v1`
- **Version:** 1.0.0
- **Domain:** Traditional Chinese Medicine
- **Sequence Mode:** freeform

**Quick Links:**
- [[Master Dashboard|← Back to All Capsules]]
- Total Root Notes: `$= dv.pages().where(p => p.source_capsules?.includes("TCM_Herbs_Test_v1") && p.type != "dashboard").length`
- Total Study Materials: `$= dv.pages('"study_material"').where(p => p.source_capsules?.includes("TCM_Herbs_Test_v1")).length`

---

## Root Notes

```dataview
TABLE type, tags, updated
FROM ""
WHERE contains(source_capsules, "TCM_Herbs_Test_v1")
  AND type != "dashboard"
  AND type != "quiz"
  AND type != "flashcard"
SORT name ASC
```

---

## Study Materials

### Flashcards
```dataview
LIST
FROM ""
WHERE contains(source_capsules, "TCM_Herbs_Test_v1")
  AND type = "flashcard"
SORT file.name ASC
```

### Quizzes
```dataview
TABLE quiz_data.difficulty, quiz_data.topic
FROM ""
WHERE contains(source_capsules, "TCM_Herbs_Test_v1")
  AND type = "quiz"
SORT file.name ASC
```

---

## Recent Activity

```dataview
TABLE type, updated
FROM ""
WHERE contains(source_capsules, "TCM_Herbs_Test_v1")
SORT updated DESC
LIMIT 10
```

---

## Test Validation Queries

### Test Query 1: Filter by Active Status
```dataview
TABLE capsule_id, dashboard_metadata.topic
FROM ""
WHERE type = "capsule_dashboard"
  AND dashboard_metadata.active = true
SORT file.name ASC
```

### Test Query 2: Filter by Class and Topic
```dataview
TABLE capsule_id, version, dashboard_metadata.category
FROM ""
WHERE type = "capsule_dashboard"
  AND dashboard_metadata.class = "TCM101"
  AND dashboard_metadata.topic = "Herbal Medicine"
```

### Test Query 3: Filter by Category
```dataview
TABLE capsule_id, dashboard_metadata.class, dashboard_metadata.topic
FROM ""
WHERE type = "capsule_dashboard"
  AND dashboard_metadata.category = "CALE"
  AND dashboard_metadata.active = true
```

### Test Query 4: Complex DataviewJS Filtering
```dataviewjs
const capsules = dv.pages()
  .where(p => p.type === "capsule_dashboard");

// Apply multiple filter criteria
const filtered = capsules
  .where(p => {
    // Must be active
    if (!p.dashboard_metadata?.active) return false;
    
    // Must match class OR category
    return (p.dashboard_metadata?.class === "TCM101" || 
            p.dashboard_metadata?.category === "CALE");
  })
  .sort(p => p.file.ctime, 'desc');

dv.table(
  ["Capsule ID", "Class", "Category", "Topic", "Active"],
  filtered.map(p => [
    p.capsule_id,
    p.dashboard_metadata?.class || "N/A",
    p.dashboard_metadata?.category || "N/A",
    p.dashboard_metadata?.topic || "N/A",
    p.dashboard_metadata?.active ? "✅" : "❌"
  ])
);
```

---

**Test Notes:**

This sample dashboard note validates the metadata schema defined in Story 11-1:
1. All required fields present (type, capsule_id, version)
2. All optional metadata fields present (class, topic, category, active)
3. Queries demonstrate filtering capabilities
4. Schema supports all query patterns from PoC (docs/sprint-artifacts/11-0-dataview-spike-poc.md)
