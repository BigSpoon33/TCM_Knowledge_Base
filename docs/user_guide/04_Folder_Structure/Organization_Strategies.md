# Organization Strategies for OCDS

**Version:** 1.0.0  
**Last Updated:** 2025-11-10  
**Purpose:** Practical guide to organizing educational content

---

## Overview

This document provides concrete organizational strategies for different use cases in the OCDS ecosystem. Whether you're a course creator, student, or institution, you'll find a recommended structure that fits your needs.

---

## Table of Contents

1. [For Course Creators](#for-course-creators)
2. [For Students](#for-students)
3. [For Institutions](#for-institutions)
4. [For Research & AI Generation](#for-research--ai-generation)
5. [Migration Strategies](#migration-strategies)
6. [Real-World Examples](#real-world-examples)

---

## For Course Creators

### Strategy: Hierarchical Source Library

**Use case:** Building structured curriculum with clear progression

```
TCM_Knowledge_Base/
│
├── TCM_Patterns/                      # 📚 SOURCE LIBRARY (curated)
│   ├── 01_Foundations/
│   │   ├── Yin_Yang_Theory.md
│   │   ├── Five_Elements.md
│   │   └── Qi_Blood_Fluids.md
│   │
│   ├── 02_Zang_Fu_Patterns/
│   │   ├── Heart_Patterns/
│   │   │   ├── Heart_Qi_Deficiency.md
│   │   │   ├── Heart_Blood_Deficiency.md
│   │   │   ├── Heart_Yin_Deficiency.md
│   │   │   └── Heart_Fire_Blazing.md
│   │   ├── Lung_Patterns/
│   │   ├── Spleen_Patterns/
│   │   ├── Liver_Patterns/
│   │   └── Kidney_Patterns/
│   │
│   ├── 03_Channel_Patterns/
│   │   ├── Tai_Yang_Patterns/
│   │   ├── Shao_Yang_Patterns/
│   │   └── Yang_Ming_Patterns/
│   │
│   └── 04_Advanced_Patterns/
│       ├── Six_Stages_Theory/
│       ├── Four_Levels_Theory/
│       └── San_Jiao_Patterns/
│
├── Materials/                         # 🎓 GENERATED MATERIALS (per class)
│   ├── TCM_101_Foundations/
│   │   ├── Week_01/
│   │   ├── Week_02/
│   │   └── ...
│   │
│   ├── TCM_201_Diagnosis/
│   │   ├── Week_01/
│   │   └── ...
│   │
│   └── TCM_301_Treatment/
│       └── ...
│
└── OCDS_Classes/                      # 📦 PACKAGED CLASSES (for distribution)
    ├── TCM_101.zip
    ├── TCM_201.zip
    └── TCM_301.zip
```

### Metadata Strategy

**Root notes in source library:**
```yaml
---
# Core identification
ocds_type: "root_note"
material_id: "pattern-heart-blood-def-001"
name: "Heart Blood Deficiency"
type: "pattern"

# Organization
category: ["Zang Fu", "Heart", "Blood Deficiency"]
tags: ['tcm', 'pattern', 'deficiency', 'heart', 'blood']
difficulty_level: "beginner"              # beginner | intermediate | advanced
curriculum_order: 15                      # Order in curriculum

# Status tracking
status: "published"                       # draft | review | published | archived
source: "curated"                         # curated | generated | imported
version: "1.2.0"
last_reviewed: 2025-11-01

# Cross-references
related: 
  - "Spleen Qi Deficiency"
  - "Liver Blood Deficiency"
western_conditions: 
  - "Insomnia"
  - "Anxiety"
  - "Anemia"
formulas: 
  - "Gui Pi Tang"
  - "Suan Zao Ren Tang"

# Usage tracking
used_in_classes: ["TCM_101", "TCM_201"]
---
```

### Workflow

```bash
# 1. Create/curate root note in source library
vim TCM_Patterns/02_Zang_Fu_Patterns/Heart_Patterns/Heart_Blood_Deficiency.md

# 2. Generate materials for specific class
cap generate "Heart Blood Deficiency" --class-id TCM_101

# 3. Materials appear in Materials/TCM_101/
ls Materials/TCM_101/
# → Heart_Blood_Deficiency_Flashcards.md
# → Heart_Blood_Deficiency_Quiz.md
# → Heart_Blood_Deficiency_Slides.md

# 4. Package class for distribution
python scripts/build_class.py --class-id TCM_101

# 5. Distribute OCDS_Classes/TCM_101.zip
```

### Benefits

- ✅ Clear curriculum progression (numbered folders)
- ✅ Easy to find and edit source material
- ✅ Separate source from generated content
- ✅ Reuse same root note across multiple classes
- ✅ Version control on source library

---

## For Students

### Strategy: Class-Centric Organization

**Use case:** Taking multiple classes, want isolated workspaces

```
My_Obsidian_Vault/
│
├── Classes/                           # 🎓 ACTIVE CLASSES
│   ├── TCM_101_Fall_2025/
│   │   ├── Week_01/
│   │   │   ├── Study_Material.md
│   │   │   ├── Flashcards.md
│   │   │   ├── Quiz.md
│   │   │   └── Tasks.md
│   │   ├── Week_02/
│   │   ├── Dashboard.md
│   │   └── class_manifest.yaml
│   │
│   ├── TCM_201_Spring_2026/
│   │   └── ...
│   │
│   └── Acupuncture_301/
│       └── ...
│
├── My_Notes/                          # ✍️ PERSONAL NOTES
│   ├── Heart_Blood_Deficiency_Notes.md
│   ├── Study_Journal.md
│   └── Clinical_Cases.md
│
├── Reference/                         # 📚 READ-ONLY REFERENCE
│   ├── TCM_Patterns/                 # Linked from class materials
│   ├── TCM_Formulas/
│   └── TCM_Herbs/
│
└── Archive/                           # 📦 COMPLETED CLASSES
    ├── TCM_101_Fall_2025/            # Moved after completion
    └── TCM_201_Spring_2026/
```

### Metadata Strategy

**Personal annotations:**
```yaml
---
# Student metadata (added to class materials)
my_understanding: 4                    # 1-5 scale
review_priority: "high"                # high | medium | low
last_reviewed: 2025-11-10
next_review: 2025-11-17                # Spaced repetition
confidence_level: "comfortable"        # struggling | learning | comfortable | mastered

# Personal tags
my_tags: ['review', 'exam-prep', 'clinical-relevant']
notes_location: "My_Notes/Heart_Blood_Deficiency_Notes.md"
---
```

### Workflow

```bash
# 1. Import new class
cap import TCM_101.zip --start-date 2025-11-10

# 2. Class appears in Classes/TCM_101_Fall_2025/
cd Classes/TCM_101_Fall_2025

# 3. Study materials appear week-by-week
# Week 1 unlocks immediately
# Week 2 unlocks after completing Week 1 quiz with 80%+

# 4. Make personal notes (separate from class materials)
vim My_Notes/Heart_Blood_Deficiency_Notes.md

# 5. Link to class material (don't duplicate)
[[Classes/TCM_101_Fall_2025/Week_03/Study_Material#Heart Blood Deficiency]]

# 6. After class completion, archive
mv Classes/TCM_101_Fall_2025 Archive/
```

### Benefits

- ✅ Clean separation: class materials vs personal notes
- ✅ Easy to archive completed classes
- ✅ No confusion about what to modify
- ✅ Personal annotations don't interfere with updates
- ✅ Can take multiple classes simultaneously

---

## For Institutions

### Strategy: Multi-Instructor Repository

**Use case:** Multiple instructors sharing content library

```
Institution_Vault/
│
├── Content_Library/                   # 📚 SHARED REPOSITORY
│   ├── TCM/
│   │   ├── Patterns/
│   │   ├── Formulas/
│   │   └── Points/
│   │
│   ├── Herbalism/
│   │   ├── Western_Herbs/
│   │   └── Chinese_Herbs/
│   │
│   └── Acupuncture/
│       ├── Classical_Points/
│       └── Modern_Techniques/
│
├── Courses/                           # 🎓 COURSE TEMPLATES
│   ├── TCM_Foundations/
│   │   ├── v1.0.0/                   # Versioned courses
│   │   ├── v1.1.0/
│   │   └── timeline.yaml
│   │
│   ├── Advanced_Diagnosis/
│   └── Clinical_Practice/
│
├── Instructors/                       # 👨‍🏫 INSTRUCTOR WORKSPACES
│   ├── Dr_Smith/
│   │   ├── Fall_2025_TCM_101/        # Per-semester customizations
│   │   └── Spring_2026_TCM_201/
│   │
│   └── Dr_Jones/
│       └── Fall_2025_TCM_101/        # Same course, different instructor
│
├── Student_Deployments/               # 🎓 PACKAGED FOR STUDENTS
│   ├── Fall_2025/
│   │   ├── TCM_101_Smith.zip
│   │   ├── TCM_101_Jones.zip
│   │   └── TCM_201_Smith.zip
│   │
│   └── Spring_2026/
│       └── ...
│
└── Analytics/                         # 📊 AGGREGATE DATA
    ├── Course_Performance.md
    └── Content_Usage_Stats.md
```

### Metadata Strategy

**Institutional tracking:**
```yaml
---
# Ownership
author: "Dr. Smith"
contributors: ["Dr. Jones", "Dr. Chen"]
institution: "East West College"
department: "Traditional Chinese Medicine"

# Versioning
version: "1.2.0"
created: 2024-01-15
last_updated: 2025-11-10
review_cycle: "annual"                # annual | semester | quarterly
next_review: 2026-11-10

# Accreditation
accredited_by: ["ACAOM", "NCCAOM"]
learning_outcomes: 
  - "LO-001: Identify Zang Fu patterns"
  - "LO-002: Differentiate excess/deficiency"
competencies: ["diagnosis", "pattern-recognition"]

# Usage tracking
times_taught: 15
student_success_rate: 0.87            # 87% pass rate
average_time_to_complete: "45 minutes"

# Rights
license: "CC-BY-NC-SA-4.0"
internal_use_only: false
---
```

### Workflow

```bash
# 1. Content team curates library
cd Content_Library/TCM/Patterns
git pull origin main

# 2. Instructor creates course from library
cap build-course \
  --template "TCM_Foundations" \
  --instructor "Dr_Smith" \
  --semester "Fall_2025" \
  --content-source "Content_Library/TCM"

# 3. Instructor customizes
cd Instructors/Dr_Smith/Fall_2025_TCM_101
# Edit timeline, add custom quizzes, etc.

# 4. Package for students
cap package-course \
  --course "Instructors/Dr_Smith/Fall_2025_TCM_101" \
  --output "Student_Deployments/Fall_2025/TCM_101_Smith.zip"

# 5. Students download and import
# Student downloads TCM_101_Smith.zip
# Student runs: cap import TCM_101_Smith.zip

# 6. Aggregate analytics
python scripts/analyze_course_performance.py \
  --course "TCM_101" \
  --semester "Fall_2025"
```

### Benefits

- ✅ Shared content library reduces duplication
- ✅ Version control prevents conflicts
- ✅ Instructor autonomy (customize per semester)
- ✅ Analytics across instructors
- ✅ Consistent quality standards

---

## For Research & AI Generation

### Strategy: Flat with Rich Metadata

**Use case:** AI-generated content, exploratory research, cross-cutting topics

```
Research_Vault/
│
├── Generated_Content/                 # 🤖 AI-GENERATED ROOT NOTES
│   ├── Impotence_TCM.md
│   ├── Chronic_Fatigue_Syndrome.md
│   ├── Long_COVID_Treatment.md
│   ├── Migraine_Patterns.md
│   └── PTSD_TCM_Approach.md
│
├── Research_Projects/                 # 🔬 RESEARCH OUTPUTS
│   ├── Project_Autoimmune_2025/
│   │   ├── Root_Note_Autoimmunity.md
│   │   ├── Literature_Review.md
│   │   ├── Case_Studies/
│   │   └── Analysis.md
│   │
│   └── Project_Pain_Management_2025/
│       └── ...
│
├── Cross_References/                  # 🔗 LINKING NOTES
│   ├── Western_TCM_Correlations.md
│   ├── Symptom_Pattern_Map.md
│   └── Research_Gaps.md
│
└── Validation_Queue/                  # ✅ CONTENT REVIEW
    ├── Needs_Review/
    ├── In_Review/
    └── Approved/
```

### Metadata Strategy

**Research-focused metadata:**
```yaml
---
# Identification
ocds_type: "root_note"
material_id: "research-impotence-001"
name: "Impotence - TCM Pattern Analysis"
type: "pattern"

# Multi-dimensional categorization (no hierarchy needed!)
tags: 
  - 'tcm'
  - 'pattern'
  - 'mens-health'
  - 'kidney-deficiency'
  - 'qi-stagnation'
  - 'blood-stasis'
  - 'research'

# Western medicine correlation
western_conditions: 
  - "Erectile Dysfunction"
  - "Male Sexual Dysfunction"
icd10_codes: ["N52.9", "F52.21"]

# TCM categorization
tcm_patterns:
  - "Kidney Yang Deficiency"
  - "Kidney Yin Deficiency"
  - "Liver Qi Stagnation"
  - "Blood Stasis in Lower Jiao"

# Generation metadata
source: "research"                     # AI-generated from research
generated_by: "deep_research_pipeline"
generation_date: 2025-11-10
model: "gemini-1.5-pro"
prompt_version: "2.1.0"

# Quality status
validation_status: "pending"           # pending | in_review | validated | rejected
reviewed_by: null
review_date: null
confidence_score: 0.85                 # AI confidence in content

# Research provenance
research_depth: "comprehensive"        # quick | comprehensive | exhaustive
sources_consulted: 15
references: 
  - "Maciocia, G. (2015). Foundations of Chinese Medicine"
  - "Bensky, D. (2004). Chinese Herbal Medicine: Materia Medica"
pubmed_articles: ["PMID:12345678", "PMID:87654321"]

# Content characteristics
word_count: 4500
estimated_reading_time: "20 minutes"
complexity_level: "intermediate"

# Usage potential
suitable_for_classes: ["TCM_301", "Clinical_Practice"]
needs_validation: true
clinical_relevance: "high"
---
```

### Workflow

```bash
# 1. Run deep research on new topic
cap research "Impotence" --deep --depth comprehensive

# Output:
# → Materials/Traditional_Chinese_Medicine_Impotence/
#   ├── Root_Note.md
#   ├── Study_Material.md
#   ├── Flashcards.md
#   └── Slides.md

# 2. Move to validation queue
mv Materials/Traditional_Chinese_Medicine_Impotence \
   Research_Vault/Validation_Queue/Needs_Review/Impotence

# 3. Expert review
cap review "Impotence" --reviewer "Dr_Smith"
# → Updates validation_status to "in_review"

# 4. After validation, promote to content library
mv Research_Vault/Validation_Queue/Approved/Impotence \
   TCM_Knowledge_Base/TCM_Patterns/Clinical_Conditions/Impotence.md

# 5. Now discoverable by Capsule
cap list
# → Shows "Impotence" pattern

# 6. Can generate materials for classes
cap generate "Impotence" --class-id TCM_301
```

### Discovery Queries

With rich metadata, you can query flexibly:

```bash
# Find all kidney-related patterns
cap list --tag kidney

# Find patterns needing review
cap list --status pending --validation-status "needs_validation"

# Find research-generated content
cap list --source research

# Find content by Western condition
cap list --western "Erectile Dysfunction"

# Find high-confidence AI generations
cap list --confidence-min 0.8
```

### Benefits

- ✅ No rigid folder structure needed
- ✅ Multi-dimensional categorization
- ✅ AI-friendly (can generate anywhere)
- ✅ Rich filtering and querying
- ✅ Validation workflow built in
- ✅ Provenance tracking

---

## Migration Strategies

### From Flat to Hierarchical

**Before:**
```
TCM_Patterns/
├── Heart_Qi_Deficiency.md
├── Heart_Blood_Deficiency.md
├── Lung_Qi_Deficiency.md
├── Spleen_Qi_Deficiency.md
└── [100+ more files]
```

**After:**
```
TCM_Patterns/
├── Heart_Patterns/
│   ├── Heart_Qi_Deficiency.md
│   └── Heart_Blood_Deficiency.md
├── Lung_Patterns/
│   └── Lung_Qi_Deficiency.md
└── Spleen_Patterns/
    └── Spleen_Qi_Deficiency.md
```

**Migration script:**
```bash
# Group by organ system
for file in TCM_Patterns/*.md; do
  organ=$(echo $file | grep -oE "(Heart|Lung|Spleen|Liver|Kidney)")
  mkdir -p "TCM_Patterns/${organ}_Patterns"
  mv "$file" "TCM_Patterns/${organ}_Patterns/"
done

# Capsule still finds them (recursive search)
cap list  # Works!
```

---

### From Hierarchical to Tagged

**Keep folder structure for browsing:**
```
TCM_Patterns/
└── Zang_Fu_Patterns/
    └── Heart_Blood_Deficiency.md
```

**Add metadata for flexible discovery:**
```yaml
---
ocds_type: "root_note"
tags: ['heart', 'blood', 'deficiency', 'zang-fu', 'insomnia']
category: ["Zang Fu", "Heart Patterns", "Blood Deficiency"]
---
```

**Now discoverable both ways:**
```bash
# By directory
cap list --directory "TCM_Patterns/Zang_Fu_Patterns"

# By tag
cap list --tag "insomnia"

# By category
cap list --category "Blood Deficiency"
```

---

## Real-World Examples

### Example 1: Small Private Practice

**Scenario:** Solo practitioner creating study materials for students

```
My_TCM_Vault/
├── Clinical_Notes/                    # Personal clinical cases
├── Patient_Resources/                 # Handouts for patients
├── Student_Materials/                 # For interns/apprentices
│   ├── Foundations/
│   ├── Diagnosis/
│   └── Treatment/
└── Reference_Library/                 # Source patterns
```

**Organization:** Flat with tags (small scale, flexible)

---

### Example 2: Large TCM University

**Scenario:** 20 instructors, 500 students, 50 courses

```
University_Vault/
├── Content_Repository/                # 5000+ curated patterns
│   └── [Highly structured hierarchy]
├── Instructor_Workspaces/            # Per-instructor customization
├── Course_Catalog/                    # All course templates
└── Student_Packages/                  # Per-semester distributions
```

**Organization:** Hierarchical with versioning (scale demands structure)

---

### Example 3: AI Research Lab

**Scenario:** Generating 100s of patterns, validating, publishing

```
Research_Vault/
├── Generated/                         # AI outputs (flat)
├── Validation/                        # Review workflow
├── Published/                         # Validated content
└── Experiments/                       # Prompt testing
```

**Organization:** Flat with rich metadata (AI-friendly, flexible validation)

---

## Summary

### Choosing Your Strategy

| Use Case | Organization | Discovery | Key Benefit |
|----------|-------------|-----------|-------------|
| **Course Creator** | Hierarchical | Directory | Clear curriculum structure |
| **Student** | Class-centric | Directory | Clean separation of concerns |
| **Institution** | Multi-layer | Hybrid | Shared library + customization |
| **Research/AI** | Flat + Tags | Metadata | Maximum flexibility |

### Universal Best Practices

1. **Use metadata consistently** - Enables future flexibility
2. **Separate source from generated** - `TCM_Patterns/` vs `Materials/`
3. **Version your content** - Track changes over time
4. **Link, don't duplicate** - Use `[[wikilinks]]` for references
5. **Plan for scale** - Structure that works with 10 patterns AND 10,000

---

## Next Steps

1. **Identify your use case** from examples above
2. **Choose organization strategy** that fits
3. **Migrate existing content** using provided scripts
4. **Add metadata** to enable discovery
5. **Test workflow** with `cap` commands

---

**Related Documentation:**
- `README.md` - Folder structure overview
- `Root_Note_Discovery.md` - Discovery system technical details
- `03_Data_Standards/Frontmatter_Schema.md` - Metadata specification
- `12_Best_Practices/Content_Organization.md` - Additional best practices

---

*Last updated: 2025-11-10*  
*Version: 1.0.0*
