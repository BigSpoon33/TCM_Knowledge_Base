# Capsule CLI - Complete Workflow Guide

## 🎯 Understanding the Different Research Modes

### Mode 1: Standard Research (Quick Notes)
**Command:** `capsule research <topic>`  
**What it does:** Creates a research markdown file with AI-generated content  
**Output:** Single research file in `Materials/TCM_101/Research_<topic>.md`

**Use when:** You want quick research notes on any topic

**Example:**
```bash
cap study "needle technique"
# Creates: Materials/TCM_101/Research_needle_technique.md
```

**What you get:**
- Markdown file with research
- Metadata (timestamp, model, depth)
- Well-structured content
- NOT a root note (no frontmatter)

---

### Mode 2: Deep Research Pipeline (Complete Package)
**Command:** `capsule research <topic> --deep`  
**What it does:** Creates a complete OCDS class package with root note + all materials  
**Output:** Root note + flashcards + quiz + slides + conversation + study guide + tasks

**Use when:** You want to create complete learning materials for a new topic

**Example:**
```bash
cap study "Spleen Qi Deficiency" --deep
```

**What you get:**
```
Materials/TCM_101/
├── Root_Note_Spleen_Qi_Deficiency.md  ✅ Full root note with frontmatter
├── Flashcards_Spleen_Qi_Deficiency.md ✅ ~20 spaced repetition cards
├── Quiz_Spleen_Qi_Deficiency.md       ✅ ~6 questions with answers
├── Slides_Spleen_Qi_Deficiency.md     ✅ ~10 presentation slides
├── Conversation_Spleen_Qi_Deficiency.md ✅ Guided learning script
├── Study_Material_Spleen_Qi_Deficiency.md ✅ Study guide
└── Tasks_Spleen_Qi_Deficiency.md      ✅ Task checklist
```

**Pipeline Steps:**
1. 🤖 AI generates optimal research prompt
2. 🔬 Conducts deep research (Gemini + Search)
3. 📋 Parses template structure
4. ✍️  Generates content for each section
5. 📄 Fills template → Creates root note
6. 📚 Generates all materials from root note
7. ✅ Complete package ready!

**Time:** ~30 minutes (AI processing)

---

## 🔄 Complete Workflow Options

### Option A: Topic Exists (Has Root Note)
**Scenario:** You already have a root note for "Kidney Yang Deficiency"

```bash
# Just generate materials from existing root note
cap gen "Kidney Yang Deficiency"

# ⚠️  Will ask before overwriting existing materials
# ✅ Generates: flashcards, quiz, slides, conversation, etc.
```

---

### Option B: Topic Doesn't Exist (No Root Note)
**Scenario:** You want to study "needle technique" (doesn't exist yet)

**Quick Research (No Materials):**
```bash
cap study "needle technique"
# Creates: Research_needle_technique.md
# Good for: Quick reference, notes
```

**Full Package (Root Note + Materials):**
```bash
cap study "needle technique" --deep
# Creates: Root note + all materials
# Good for: Complete learning package
```

---

### Option C: Interactive Learning
**Scenario:** You have a root note and want to study with AI guidance

```bash
# Start interactive conversation
cap chat "Kidney Yang Deficiency"

# The AI will:
# - Ask questions about each section
# - Assess your understanding
# - Provide feedback
# - Guide you through the material
```

---

## 📊 Comparison: Research vs Generate

| Feature | `research` | `research --deep` | `generate` |
|---------|-----------|------------------|------------|
| **Input** | Topic name | Topic name | Pattern name (must exist) |
| **Prerequisites** | None | None | Root note must exist |
| **Creates Root Note** | ❌ No | ✅ Yes | ❌ No (uses existing) |
| **Creates Materials** | ❌ No | ✅ Yes | ✅ Yes |
| **Output File** | Research_*.md | Root_Note_*.md + materials | Materials only |
| **Time** | ~30 seconds | ~30 minutes | ~5 minutes |
| **Use Case** | Quick notes | New complete topic | Update existing materials |

---

## 💡 Recommended Workflows

### Workflow 1: Learning Existing TCM Patterns
```bash
# 1. See what patterns exist
cap list | grep -i kidney

# 2. Generate materials if needed
cap gen "Kidney Yang Deficiency"

# 3. Start learning
cap chat "Kidney Yang Deficiency"
```

---

### Workflow 2: Creating New Topic from Scratch
```bash
# 1. Do deep research (creates everything)
cap study "Five Element Theory" --deep --depth exhaustive

# 2. Review generated materials
ls Materials/TCM_101/*Five_Element_Theory*

# 3. Start learning
cap chat "Five Element Theory"
```

---

### Workflow 3: Quick Research for Reference
```bash
# Just want quick notes on a topic
cap study "pulse diagnosis techniques" --depth comprehensive

# File created at: Materials/TCM_101/Research_pulse_diagnosis_techniques.md
# Open in Obsidian to read
```

---

## 🎓 Research Depth Options

All research commands support depth control:

| Depth | Time | Detail Level | When to Use |
|-------|------|--------------|-------------|
| `quick` | ~30s | Basic overview | Quick reference |
| `comprehensive` | ~2min | Detailed content | Default, good balance |
| `exhaustive` | ~5min | Very detailed | In-depth study |

**Examples:**
```bash
cap study "topic" --depth quick         # Fast overview
cap study "topic" --depth comprehensive # Default
cap study "topic" --depth exhaustive    # Maximum detail
```

---

## 🔧 Common Issues & Solutions

### Issue 1: "Pattern not found"
**Problem:** Pattern doesn't exist in TCM_Patterns/  
**Solution:** Use `research --deep` instead of `generate`

```bash
# ❌ Won't work (pattern doesn't exist)
cap gen "new topic"

# ✅ Works (creates from scratch)
cap study "new topic" --deep
```

---

### Issue 2: "Root note not found"
**Problem:** Trying to generate materials but no root note exists  
**Solution:** Create root note first with `--deep`

```bash
# Create root note first
cap study "topic" --deep

# Then you can use generate
cap gen "topic"
```

---

### Issue 3: Research file not appearing in Obsidian
**Check:**
1. File was created: `ls Materials/TCM_101/Research_*.md`
2. Obsidian is watching the vault
3. Try: Ctrl+P → "Reload without saving"

**Expected location:** `Materials/TCM_101/Research_<topic>.md`

---

## 📁 File Naming Conventions

| Type | Naming Pattern | Example |
|------|---------------|---------|
| Research notes | `Research_<topic>.md` | `Research_needle_technique.md` |
| Root notes | `Root_Note_<topic>.md` | `Root_Note_Spleen_Qi_Deficiency.md` |
| Flashcards | `Flashcards_<topic>.md` | `Flashcards_Kidney_Yang_Deficiency.md` |
| Quiz | `Quiz_<topic>.md` | `Quiz_Heart_Blood_Deficiency.md` |
| Slides | `Slides_<topic>.md` | `Slides_Liver_Qi_Stagnation.md` |
| Conversation | `Conversation_<topic>.md` | `Conversation_Lung_Yin_Deficiency.md` |

All files go to: `Materials/<class_id>/`

---

## 🚀 Quick Reference

```bash
# List patterns
cap list

# Quick research
cap study "topic"

# Full package
cap study "topic" --deep

# Generate materials from existing root note
cap gen "pattern"

# Interactive learning
cap chat "pattern"

# Configure
cap config set api.gemini_key "key"
```

---

**Last Updated:** 2025-11-08  
**Status:** Complete workflow documentation
