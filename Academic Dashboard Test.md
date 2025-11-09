Perfect — here’s what the **TCM101 Course Dashboard** would look like in Obsidian after importing the `.occz` file.  
This simulates the **Dataview + Tasknotes + Templater integration** and shows how your class material becomes a live, interactive workspace.

---

# 🏛️ **TCM101 — Introduction to Chinese Internal Medicine**

> _Instructor: Dr. Huabing Wen, PhD_  
> _Credits: 3 | Duration: 8 weeks | Start: Nov 5, 2025_

---

## 🧭 Course Overview

```dataview
TABLE 
    module AS "Week",
    topic AS "Topic",
    type AS "Type",
    file.link AS "Material"
FROM "Courses/TCM101/Materials"
SORT module ASC
```

|Week|Topic|Type|Material|
|---|---|---|---|
|Week 1|Tai Yin Deficiency Cold|Lecture|[[Week1 Lecture]]|
|Week 1|Spleen Yang Deficiency|Case Study|[[Week1 Case Study]]|
|Week 2|Yang Ming Heat Excess|Lecture|[[Week2 Lecture]]|
|Week 2|Qi and Blood Stagnation|Review Qs|[[Week2 Review Questions]]|

---

## 📅 **Tasknotes Dashboard**

```dataview
TASK
FROM "Courses/TCM101/Tasks"
WHERE !completed
SORT due ASC
GROUP BY project
```

🧩 **Project: Midterm Case Analysis**

-  Review Lecture: Tai Yin Deficiency Cold ✅ due:: 2025-11-06
    
-  Write analysis for assigned case ✅ due:: 2025-11-20
    
-  Submit OCCZ for grading ✅ due:: 2025-12-01
    

📖 **Weekly Study Tasks**

-  Review Lecture: Week 1 — Tai Yin Deficiency Cold
    
-  Review Case Study: Spleen Yang Deficiency
    
-  Prepare Flashcards for Herbs
    
-  Take Week 1 Self-Quiz
    

---

## 🧠 **Study Material Access**

**Flashcards**

```dataview
TABLE 
    file.link AS "Deck", 
    length(rows) AS "Cards"
FROM "Courses/TCM101/Flashcards"
GROUP BY deck_name
```

|Deck|Cards|
|---|---|
|[[herbs_deck]]|20|
|[[formulas_deck]]|15|

Use with → 🧩 _Spaced Repetition Plugin_  
→ Each flashcard auto-tags with `#tcm101/flashcard` and `#study/herbs`

---

## 📚 **Projects & Assignments**

```dataview
TABLE
    title AS "Project",
    due AS "Due Date",
    file.link AS "Details"
FROM "Courses/TCM101/Projects"
SORT due ASC
```

|Project|Due Date|Details|
|---|---|---|
|Midterm Case Analysis|Dec 1, 2025|[[Midterm Case Analysis]]|

🧩 **Submit via OCCZ Export** → Generates a zip file of your assignment and metadata for grading.

---

## 🔍 **Research Notes & Clinical Crosslinks**

```dataview
TABLE
    topic AS "Related Topic",
    link(file.link) AS "Note"
FROM "Herbs" OR "Formulas"
WHERE contains(tags, "taiyin")
SORT topic ASC
```

|Related Topic|Note|
|---|---|
|Tai Yin Deficiency|[[Ai Ye — Mugwort Leaf]]|
|Middle Burner Cold|[[Li Zhong Wan]]|
|Spleen Yang Deficiency|[[Gan Jiang — Dried Ginger]]|

---

## 📈 **Progress Tracking**

```dataviewjs
const tasks = dv.pages('"Courses/TCM101/Tasks"').file.tasks
const total = tasks.length
const completed = tasks.where(t => t.completed).length
const percent = Math.round((completed / total) * 100)
dv.paragraph(`✅ **Progress:** ${percent}% complete (${completed}/${total} tasks finished)`)
```

✅ **Progress:** 33% complete (10/30 tasks finished)

---

## 🧩 **Quick Actions**

|Action|Description|
|---|---|
|🧠 Start Study Session|Generates today’s study tasks via Templater|
|🗓️ View Weekly Schedule|Opens Tasknotes Calendar for this class|
|🧾 Export OCCZ|Packages notes + metadata for grading or sharing|
|📥 Import Updates|Syncs updated materials or grades from instructor|
|📊 Open Analytics|Shows time spent, average scores, and task stats|

---

## 🧩 Visual Flow (in Obsidian Canvas)

```text
[Course Manifest]
      ↓
[Templater Templates] → Generates → [Daily Tasks]
      ↓
[Dataview Tables] ← Tracks ← [Study Materials, Projects, Flashcards]
      ↓
[Tasknotes] → Schedules → [Calendar View]
      ↓
[Export OCCZ] → Grading/Sharing
```

---

Would you like me to **generate a visual Canvas mockup** of this dashboard (like how it would actually appear inside Obsidian with cards, links, and dynamic tables)?  
That would make it clearer how the dashboard interacts with Tasknotes, flashcards, and the OCCZ backend.