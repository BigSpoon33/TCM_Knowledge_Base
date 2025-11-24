# OCDS Folder Structure - Visual Diagrams

**Version:** 1.0.0  
**Last Updated:** 2025-11-10  
**Purpose:** Visual reference for OCDS folder organization

---

## Content Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           OCDS CONTENT FLOW                                 │
└─────────────────────────────────────────────────────────────────────────────┘

    RESEARCH & GENERATION                 CURATION & VALIDATION
    ─────────────────────                 ─────────────────────

┌──────────────────┐                    ┌──────────────────┐
│                  │                    │                  │
│   AI Research    │                    │  Expert Review   │
│   Pipeline       │                    │  & Validation    │
│                  │                    │                  │
└────────┬─────────┘                    └────────▲─────────┘
         │                                       │
         │ generates                             │ validates
         ▼                                       │
┌──────────────────┐     needs review   ┌───────┴──────────┐
│                  │────────────────────▶│                  │
│   Materials/     │                    │  Validation      │
│   Project_X/     │                    │  Queue/          │
│                  │                    │                  │
└────────┬─────────┘                    └──────────────────┘
         │                                       │
         │ approved                              │ approved
         │                                       │
         └───────────────────┬───────────────────┘
                             ▼
                    ┌──────────────────┐
                    │                  │
                    │  TCM_Patterns/   │  ← SOURCE OF TRUTH
                    │  (Curated)       │
                    │                  │
                    └────────┬─────────┘
                             │
                             │ generates materials
                             ▼
                    ┌──────────────────┐
                    │                  │
                    │  Materials/      │
                    │  {class_id}/     │
                    │                  │
                    └────────┬─────────┘
                             │
                             │ packages
                             ▼
                    ┌──────────────────┐
                    │                  │
                    │  OCDS_Classes/   │
                    │  TCM_101.zip     │
                    │                  │
                    └────────┬─────────┘
                             │
                             │ distributes
                             ▼
                    ┌──────────────────┐
                    │                  │
                    │  Student Vault   │
                    │  (Imported)      │
                    │                  │
                    └──────────────────┘
```

---

## Discovery System Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      ROOT NOTE DISCOVERY SYSTEM                             │
└─────────────────────────────────────────────────────────────────────────────┘

User runs: cap list "Heart Blood Deficiency"
                    │
                    ▼
         ┌──────────────────────┐
         │  Discovery Engine    │
         │  (Method: Hybrid)    │
         └──────────┬───────────┘
                    │
         ┌──────────┴──────────┐
         │                     │
         ▼                     ▼
┌────────────────┐    ┌────────────────┐
│ FAST PATH      │    │ SLOW PATH      │
│ Directory Scan │    │ Metadata Scan  │
└────────┬───────┘    └────────┬───────┘
         │                     │
         │ Check cache         │ Full vault scan
         │ Scan TCM_Patterns/  │ Parse YAML frontmatter
         │ Match filename      │ Filter by ocds_type
         │                     │
         ▼                     ▼
┌────────────────┐    ┌────────────────┐
│ Found in       │    │ Found by       │
│ TCM_Patterns/  │    │ metadata tag   │
│ Zang Fu/       │    │ in Materials/  │
└────────┬───────┘    └────────┬───────┘
         │                     │
         └──────────┬──────────┘
                    ▼
         ┌──────────────────────┐
         │ Return root note(s)  │
         │ + metadata           │
         │ + file path          │
         └──────────┬───────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │ Find associated      │
         │ materials:           │
         │ - Flashcards         │
         │ - Quiz               │
         │ - Slides             │
         └──────────────────────┘
```

---

## Folder Structure by Use Case

### Course Creator Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         COURSE CREATOR WORKFLOW                             │
└─────────────────────────────────────────────────────────────────────────────┘

Step 1: ORGANIZE SOURCE LIBRARY
────────────────────────────────────────────────────────────────────────────────
TCM_Patterns/
├── 01_Foundations/
│   ├── Yin_Yang_Theory.md              ← Create/curate root notes
│   └── Five_Elements.md
├── 02_Zang_Fu_Patterns/
│   ├── Heart_Patterns/
│   │   ├── Heart_Blood_Deficiency.md   ← Add metadata
│   │   └── Heart_Qi_Deficiency.md
│   └── Lung_Patterns/
└── 03_Channel_Patterns/


Step 2: GENERATE MATERIALS
────────────────────────────────────────────────────────────────────────────────
$ cap generate "Heart Blood Deficiency" --class-id TCM_101

Materials/TCM_101/
├── Heart_Blood_Deficiency_Flashcards.md  ← Auto-generated
├── Heart_Blood_Deficiency_Quiz.md        ← Auto-generated
├── Heart_Blood_Deficiency_Slides.md      ← Auto-generated
└── Heart_Blood_Deficiency_Study.md       ← Auto-generated


Step 3: PACKAGE FOR DISTRIBUTION
────────────────────────────────────────────────────────────────────────────────
$ python scripts/build_class.py --class-id TCM_101

OCDS_Classes/
└── TCM_101.zip                           ← Ready for students!
    ├── Materials/
    ├── class_manifest.yaml
    ├── timeline.yaml
    └── grading_config.yaml
```

---

### Student Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           STUDENT WORKFLOW                                  │
└─────────────────────────────────────────────────────────────────────────────┘

Step 1: IMPORT CLASS
────────────────────────────────────────────────────────────────────────────────
$ cap import TCM_101.zip --start-date 2025-11-10

My_Vault/
└── Classes/
    └── TCM_101_Fall_2025/
        ├── Week_01/
        │   ├── Study_Material.md         ← Read & study
        │   ├── Flashcards.md             ← Practice
        │   ├── Quiz.md                   ← Test knowledge
        │   └── Tasks.md                  ← Track progress
        └── Dashboard.md                  ← Monitor grades


Step 2: MAKE PERSONAL NOTES (separate from class materials!)
────────────────────────────────────────────────────────────────────────────────
My_Vault/
└── My_Notes/
    ├── Heart_Blood_Deficiency_Notes.md   ← Personal insights
    ├── Study_Journal.md                  ← Reflection
    └── Clinical_Cases.md                 ← Real-world examples


Step 3: REFERENCE MATERIALS (read-only)
────────────────────────────────────────────────────────────────────────────────
My_Vault/
└── Reference/
    └── TCM_Patterns/                     ← Linked from class
        └── Zang Fu Patterns/
            └── Heart_Blood_Deficiency.md ← DON'T EDIT!


Step 4: ARCHIVE AFTER COMPLETION
────────────────────────────────────────────────────────────────────────────────
$ mv Classes/TCM_101_Fall_2025 Archive/

My_Vault/
└── Archive/
    └── TCM_101_Fall_2025/                ← Completed work
```

---

### Research/AI Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        RESEARCH & AI WORKFLOW                               │
└─────────────────────────────────────────────────────────────────────────────┘

Step 1: GENERATE CONTENT
────────────────────────────────────────────────────────────────────────────────
$ cap research "Impotence" --deep --depth comprehensive

Materials/Traditional_Chinese_Medicine_Impotence/
├── Root_Note.md                          ← AI-generated (comprehensive)
├── Study_Material.md                     ← Auto-generated
├── Flashcards.md                         ← Auto-generated
├── Quiz.md                               ← Auto-generated
└── Slides.md                             ← Auto-generated


Step 2: VALIDATION WORKFLOW
────────────────────────────────────────────────────────────────────────────────
$ mv Materials/Traditional_Chinese_Medicine_Impotence \
     Research_Vault/Validation_Queue/Needs_Review/Impotence

Research_Vault/
└── Validation_Queue/
    ├── Needs_Review/
    │   └── Impotence/
    │       └── Root_Note.md              ← Expert reviews
    ├── In_Review/
    └── Approved/


Step 3: PROMOTE TO CURATED LIBRARY
────────────────────────────────────────────────────────────────────────────────
$ mv Research_Vault/Validation_Queue/Approved/Impotence/Root_Note.md \
     TCM_Knowledge_Base/TCM_Patterns/Clinical_Conditions/Impotence.md

TCM_Patterns/
└── Clinical_Conditions/
    └── Impotence.md                      ← Now curated & discoverable!


Step 4: DISCOVERABLE BY CAPSULE
────────────────────────────────────────────────────────────────────────────────
$ cap list
Available patterns:
  • Impotence [Clinical Conditions]      ← Shows up!
  • Heart Blood Deficiency [Zang Fu Patterns]
  • ...
```

---

## Material Linking Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MATERIAL LINKING SYSTEM                             │
└─────────────────────────────────────────────────────────────────────────────┘

                    ┌────────────────────────┐
                    │                        │
                    │  ROOT NOTE             │
                    │  Heart Blood           │
                    │  Deficiency.md         │
                    │                        │
                    │  material_id:          │
                    │  "pattern-xyz"         │
                    │                        │
                    └───────────┬────────────┘
                                │
                                │ links to
                                │
         ┌──────────────────────┼──────────────────────┐
         │                      │                      │
         ▼                      ▼                      ▼
┌────────────────┐    ┌────────────────┐    ┌────────────────┐
│ FLASHCARDS     │    │ QUIZ           │    │ SLIDES         │
│                │    │                │    │                │
│ ocds_type:     │    │ ocds_type:     │    │ ocds_type:     │
│ "flashcards"   │    │ "quiz"         │    │ "slides"       │
│                │    │                │    │                │
│ material_id:   │    │ material_id:   │    │ material_id:   │
│ "pattern-xyz"  │    │ "pattern-xyz"  │    │ "pattern-xyz"  │
│                │    │                │    │                │
└────────────────┘    └────────────────┘    └────────────────┘


DISCOVERY LOGIC:
────────────────────────────────────────────────────────────────────────────────
1. User runs: cap chat "Heart Blood Deficiency"
2. Find root note with name = "Heart Blood Deficiency"
3. Extract material_id from root note frontmatter
4. Search for materials with matching material_id:
   - Check same directory first (fast)
   - Search Materials/ directory (thorough)
5. Load all linked materials for conversation
```

---

## Directory vs Tag Comparison

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   DIRECTORY vs TAG ORGANIZATION                             │
└─────────────────────────────────────────────────────────────────────────────┘

DIRECTORY-BASED                          TAG-BASED
───────────────                          ─────────

TCM_Patterns/                            TCM_Patterns/
├── Zang_Fu/                             ├── Heart_Blood_Deficiency.md
│   ├── Heart/                           ├── Insomnia_Pattern.md
│   │   └── Heart_Blood_Deficiency.md    └── Chronic_Fatigue.md
│   └── Spleen/                                      │
├── Symptoms/                                        │ metadata
│   └── Insomnia/                                    ▼
│       └── Insomnia_Pattern.md          ---
└── Modern_Conditions/                   tags: ['heart', 'blood', 
    └── Chronic_Fatigue.md                     'deficiency', 'insomnia']
                                         category: ['Zang Fu', 'Heart']
                                         western: ['Insomnia', 'Anxiety']
                                         ---

PROS:                                    PROS:
✓ Visual hierarchy                      ✓ Multi-dimensional categories
✓ Easy to browse                        ✓ Flexible organization
✓ Fast scanning                         ✓ Cross-referencing
✓ Intuitive for beginners               ✓ Query/filter by any dimension

CONS:                                    CONS:
✗ Single hierarchy                      ✗ Requires metadata discipline
✗ Hard to cross-categorize              ✗ Harder to browse visually
✗ Deep nesting confusing                ✗ Needs good search tools
✗ Rigid structure                       ✗ Not intuitive for beginners


HYBRID APPROACH (RECOMMENDED):
──────────────────────────────────────────────────────────────────────────────

Use BOTH:
  • Directories for primary organization (visual browsing)
  • Tags for flexible categorization (powerful filtering)
  • Discovery works across both methods

Example:
TCM_Patterns/Zang_Fu/Heart_Blood_Deficiency.md
  ↓
  Has frontmatter with rich tags
  ↓
  Discoverable by:
    - Directory: cap list --dir "Zang_Fu"
    - Tag: cap list --tag "insomnia"
    - Category: cap list --category "Heart"
    - Western: cap list --western "Anxiety"
```

---

## Scale Comparison

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ORGANIZATION AT DIFFERENT SCALES                         │
└─────────────────────────────────────────────────────────────────────────────┘

SMALL SCALE (10-50 patterns)
────────────────────────────────────────────────────────────────────────────────
Structure:    Flat or 1-level deep
Discovery:    Directory scan (fast enough)
Organization: Simple folders
Metadata:     Optional

TCM_Patterns/
├── Heart_Blood_Deficiency.md
├── Spleen_Qi_Deficiency.md
└── ...

Performance:  Instant (<10ms)
Maintenance:  Low


MEDIUM SCALE (50-500 patterns)
────────────────────────────────────────────────────────────────────────────────
Structure:    Hierarchical (2-3 levels)
Discovery:    Hybrid (directory + metadata)
Organization: Category folders
Metadata:     Recommended

TCM_Patterns/
├── Zang_Fu/
│   ├── Heart_Patterns/
│   └── Lung_Patterns/
├── Channels/
└── Six_Stages/

Performance:  Fast (<50ms)
Maintenance:  Medium


LARGE SCALE (500-5000+ patterns)
────────────────────────────────────────────────────────────────────────────────
Structure:    Flexible (directories OR flat with tags)
Discovery:    Metadata with caching
Organization: Tag-based preferred
Metadata:     Essential

Research_Vault/
├── Pattern_0001.md
├── Pattern_0002.md
└── ...
    (All patterns have rich metadata)

Performance:  Cached (~2s initial, <10ms cached)
Maintenance:  High (requires metadata discipline)
Optimization: SQLite index, background scanning
```

---

## Configuration Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      CONFIGURATION & DISCOVERY FLOW                         │
└─────────────────────────────────────────────────────────────────────────────┘

User runs: cap list
     │
     ▼
┌─────────────────────┐
│ Load Configuration  │
│ ~/.config/capsule/  │
│ config.yaml         │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Get Settings:       │
│ - knowledge_base    │ → /home/user/TCM_Knowledge_Base
│ - pattern_dirs      │ → ["TCM_Patterns", "Materials"]
│ - search.method     │ → "hybrid"
│ - search.recursive  │ → true
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Build Search Paths: │
│                     │
│ /home/user/         │
│   TCM_Knowledge_Base│
│   ├─ TCM_Patterns/  │ ← Search here
│   └─ Materials/     │ ← And here
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Execute Discovery:  │
│                     │
│ if method=hybrid:   │
│   try directory     │
│   fallback metadata │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Return Results      │
│ + Apply Filters     │
│ + Sort/Format       │
│ + Cache Results     │
└─────────────────────┘
```

---

## Migration Pathways

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          MIGRATION PATHWAYS                                 │
└─────────────────────────────────────────────────────────────────────────────┘

PATH 1: Legacy Flat → OCDS Hierarchical
────────────────────────────────────────────────────────────────────────────────

BEFORE                              AFTER

Old_Vault/                          TCM_Knowledge_Base/
├── pattern1.md                     ├── TCM_Patterns/
├── pattern2.md                     │   ├── Zang_Fu/
├── pattern3.md                     │   │   └── pattern1.md
└── ...                             │   └── Channels/
                                    │       └── pattern2.md
    ↓ Migration Script              └── Materials/
    ↓ + Add Metadata                    └── TCM_101/
    ↓ + Organize by Category
                                    Discovery: Works with directories!


PATH 2: Existing Content → Add Metadata (Non-Breaking)
────────────────────────────────────────────────────────────────────────────────

BEFORE                              AFTER

TCM_Patterns/                       TCM_Patterns/
└── Heart_Blood_Deficiency.md       └── Heart_Blood_Deficiency.md
    ---                                 ---
    name: "Heart Blood Def"             ocds_type: "root_note"
    ---                                 material_id: "pattern-xyz"
                                        name: "Heart Blood Deficiency"
    ↓ Add metadata                      tags: ['heart', 'blood']
    ↓ Keep existing structure           category: ['Zang Fu']
    ↓ No files moved!                   status: "published"
                                        ---

                                    Discovery: Now works with metadata too!


PATH 3: Multiple Sources → Unified Vault
────────────────────────────────────────────────────────────────────────────────

BEFORE                              AFTER

Source_A/                           TCM_Knowledge_Base/
├── patterns/                       ├── TCM_Patterns/
└── ...                             │   └── [All curated content]
                                    ├── Materials/
Source_B/                           │   └── [Generated materials]
├── content/                        └── Research/
└── ...                                 └── [Research outputs]
    
Research_Output/                    ↓ Single vault
└── generated/                      ↓ Unified discovery
                                    ↓ Consistent structure
    ↓ Consolidate
    ↓ Standardize metadata          Discovery: Works everywhere!
```

---

## Summary Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            QUICK REFERENCE                                  │
└─────────────────────────────────────────────────────────────────────────────┘

FOLDER PURPOSES:
────────────────────────────────────────────────────────────────────────────────
TCM_Patterns/         ← Curated source of truth (version controlled)
Materials/            ← Generated materials (per-class, ephemeral)
Research/             ← Research outputs (validation queue)
OCDS_Classes/         ← Packaged distributions (.zip files)


DISCOVERY COMMANDS:
────────────────────────────────────────────────────────────────────────────────
cap list              → Show all root notes
cap list --tag X      → Filter by tag
cap list --category X → Filter by category
cap list --status X   → Filter by status


GENERATION COMMANDS:
────────────────────────────────────────────────────────────────────────────────
cap research "X" --deep              → Research → root note + materials
cap generate "X" --class-id TCM_101  → Root note → materials
cap chat "X"                         → Interactive learning


ORGANIZATION STRATEGIES:
────────────────────────────────────────────────────────────────────────────────
Course Creator   → Hierarchical in TCM_Patterns/
Student          → Class-centric in Classes/
Institution      → Multi-layer with shared library
Research/AI      → Flat with rich metadata


KEY METADATA:
────────────────────────────────────────────────────────────────────────────────
ocds_type: "root_note"    ← Enables discovery
material_id: "xyz"        ← Links materials
category: [...]           ← Hierarchical tags
tags: [...]               ← Flat tags
status: "published"       ← Lifecycle


LINKING METHODS:
────────────────────────────────────────────────────────────────────────────────
1. Naming:    Heart_Blood_Deficiency_Flashcards.md
2. Metadata:  material_id in frontmatter
3. Directory: Same folder = linked
```

---

*Last updated: 2025-11-10*  
*Version: 1.0.0*
