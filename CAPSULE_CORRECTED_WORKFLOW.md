# Capsule Research - Corrected Workflow

## 🎯 The Two Research Modes (Corrected!)

### Mode 1: Standard Research
**Command:** `capsule research "topic"`  
**Creates:** Single research file  
**Location:** `Materials/TCM_101/Research_topic.md`

```bash
cap study "needle technique"
```

**Output:**
```
Materials/TCM_101/
└── Research_needle_technique.md  ← Simple research notes
```

---

### Mode 2: Deep Research Pipeline ⭐
**Command:** `capsule research "topic" --deep`  
**Creates:** Complete folder with root note + all materials  
**Location:** `Materials/Traditional_Chinese_Medicine_topic/` (auto-created folder)

```bash
cap study "Edema" --deep
```

**Output:**
```
Materials/Traditional_Chinese_Medicine_Edema/  ← New folder created!
├── Root_Note_Edema.md                 ✅ Full root note with frontmatter
├── Edema_Bank.md                      ✅ Quiz questions
├── Edema_Flashcards.md                ✅ Spaced repetition cards
├── Edema_Slides.md                    ✅ Presentation slides
├── Edema_Guided_Conversation.md       ✅ Learning conversation
├── Edema_Study_Material.md            ✅ Study guide
└── Edema_Tasks.md                     ✅ Task checklist
```

**Note the naming:**
- Folder: `<Project>_<Topic>` (e.g., `Traditional_Chinese_Medicine_Edema`)
- Files inside: `<Topic>_<Type>.md` (e.g., `Edema_Bank.md`)
- Root note: `Root_Note_<Topic>.md`

---

### Mode 2b: Deep Research with Class ID
**Command:** `capsule research "topic" --deep --class-id TCM_101`  
**Creates:** Materials in existing class folder  
**Location:** `Materials/TCM_101/`

```bash
cap study "Edema" --deep --class-id TCM_101
```

**Output:**
```
Materials/TCM_101/  ← Uses existing class folder
├── Root_Note_Edema.md
├── Edema_Bank.md
├── Edema_Flashcards.md
├── Edema_Slides.md
├── Edema_Guided_Conversation.md
├── Edema_Study_Material.md
└── Edema_Tasks.md
```

---

## 📋 Complete Examples

### Example 1: Research a New Topic (Creates Everything)

```bash
# Research "Five Element Theory" and create complete materials
cap study "Five Element Theory" --deep --depth exhaustive

# This creates:
# Materials/Traditional_Chinese_Medicine_Five_Element_Theory/
#   ├── Root_Note_Five_Element_Theory.md
#   ├── Five_Element_Theory_Bank.md
#   ├── Five_Element_Theory_Flashcards.md
#   ├── Five_Element_Theory_Slides.md
#   ├── Five_Element_Theory_Guided_Conversation.md
#   ├── Five_Element_Theory_Study_Material.md
#   └── Five_Element_Theory_Tasks.md
```

### Example 2: Quick Research Notes

```bash
# Just want quick notes, not full materials
cap study "pulse diagnosis" --depth quick

# This creates:
# Materials/TCM_101/Research_pulse_diagnosis.md
```

### Example 3: Research for Specific Class

```bash
# Create materials for TCM_201 class
cap study "Advanced Needling" --deep --class-id TCM_201

# This creates materials in:
# Materials/TCM_201/
#   ├── Root_Note_Advanced_Needling.md
#   ├── Advanced_Needling_Bank.md
#   └── ... (all other materials)
```

---

## 🔄 When to Use Each Mode

| Scenario | Command | What You Get |
|----------|---------|--------------|
| Quick reference on any topic | `cap study "topic"` | Research_topic.md |
| New topic, full package | `cap study "topic" --deep` | Folder with 7 files |
| New topic, specific class | `cap study "topic" --deep --class-id CLASS` | Files in CLASS folder |
| Existing pattern needs materials | `cap gen "pattern"` | Materials from existing root note |

---

## 📁 Folder Structure Comparison

### Without --class-id (Default for --deep):
```
Materials/
└── Traditional_Chinese_Medicine_Edema/  ← Auto-created folder
    ├── Root_Note_Edema.md
    ├── Edema_Bank.md
    ├── Edema_Flashcards.md
    └── ... (all materials)
```

### With --class-id:
```
Materials/
└── TCM_101/  ← Existing folder
    ├── Root_Note_Edema.md
    ├── Edema_Bank.md
    ├── Edema_Flashcards.md
    └── ... (all materials)
```

---

## ⚡ Quick Reference

```bash
# Quick notes
cap study "topic"

# Full package (creates <Project>_<Topic> folder)
cap study "topic" --deep

# Full package in specific class
cap study "topic" --deep --class-id TCM_101

# Control depth
cap study "topic" --deep --depth exhaustive

# Custom project
cap study "topic" --deep --project "Herbology"
# Creates: Materials/Herbology_topic/
```

---

## 🎓 Deep Research Pipeline Steps

When you run `cap study "topic" --deep`:

1. 🤖 **Generate Research Prompt** - AI creates optimal research prompt
2. 🔬 **Deep Research** - Gemini conducts research with search grounding
3. 📋 **Parse Template** - Analyzes Root_Note_Template.md structure
4. ✍️  **Generate Content** - AI fills each template section
5. 📄 **Create Root Note** - Saves complete root note with frontmatter
6. 📚 **Generate Materials** - Creates all 6 material types:
   - Bank (quiz questions)
   - Flashcards (spaced repetition)
   - Slides (presentation)
   - Guided Conversation (interactive learning)
   - Study Material (study guide)
   - Tasks (checklist)
7. ✅ **Complete!** - Full package ready in Obsidian

**Time:** ~30 minutes (AI processing)

---

## ✅ What You Should See in Obsidian

After running:
```bash
cap study "Edema" --deep
```

You should see a NEW FOLDER in your file explorer:
- `Traditional_Chinese_Medicine_Edema/`

Inside that folder, you should see 7 markdown files:
- Root_Note_Edema.md
- Edema_Bank.md
- Edema_Flashcards.md
- Edema_Guided_Conversation.md
- Edema_Slides.md
- Edema_Study_Material.md
- Edema_Tasks.md

All files should be immediately visible in Obsidian!

---

**Last Updated:** 2025-11-08  
**Status:** Corrected workflow documentation
