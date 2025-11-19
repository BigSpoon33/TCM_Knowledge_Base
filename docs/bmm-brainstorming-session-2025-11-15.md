# Brainstorming Session: Capsule Metadata Architecture

**Date:** 2025-11-15
**Project:** Obsidian_Capsule_Delivery
**Facilitator:** BMad Analyst Agent
**Participant:** User

---

## Session Plan

**Approach:** Progressive Technique Flow
**Duration:** 60-90 minutes
**Goal:** Design universal capsule metadata architecture and author template

### Techniques Selected:
1. **Metaphor Mapping** (20-25 min) - Divergent exploration through concrete mental models
2. **Morphological Analysis** (20-25 min) - Systematic parameter combination analysis
3. **First Principles Thinking** (15-20 min) - Distill to essential capsule foundation

---

## Phase 1: Metaphor Mapping

**Start Time:** Session beginning

### Metaphor Exploration


#### Core Metaphor: **"A Capsule is a Musical Score"**

**Key Insights:**
- Musical scores have **universal notation** (notes, clefs, time signatures) but express **infinite compositions**
- Can be played **solo or ensemble** (standalone capsule or integrated with others)
- Can be performed **in parts or as a whole** (modular consumption)
- Has **interchangeable elements** (sections can combine with other scores)
- Different **keys and time signatures** (domain-specific configurations)
- Universal structure enables **sight-reading by anyone** (immediate comprehension)

#### Capsule Core Components (The "Musical Notation System"):

1. **Dashboard** → The Score's Title Page/Index (shows structure, movements, instrumentation)
2. **Root Notes** → The Core Melody/Theme (fundamental knowledge, key concepts)
3. **Study Material** → The Practice Exercises/Etudes (reinforcement, skill building)
4. **Other Relevant Files** → Sheet Music Annotations/Performance Notes (context, media, references)

**Flexibility:** Can include anything - pictures, code, PDFs, media (like performance recordings, conductor notes, historical context)

**Fundamental Structure:** Dashboard + Root Notes + Study Material + Relevant Files

---

### Metaphor Extension Questions


#### Musical Metaphor Mappings:

**🎵 Key Signature = Capsule Descriptor/Cypher File**
- **Purpose:** Explains how to "read" the capsule
- **Contents:**
  - Name, topic, categories
  - Domain-specific metadata schema
  - Custom field definitions
  - "Rosetta stone" for interpreting this capsule's structure
- **Analogy:** Like the key signature tells you "all F's are sharp in this piece," the descriptor tells you "this capsule uses herb_data, pattern_data, formula_data fields"

**⏱️ Time Signature = Sequence Configuration**
- **Two Modes:**
  1. **Sequenced/Structured** → Like 4/4 time (strict rhythm)
     - 15-week course with defined schedule
     - Timeline events tied to capsule start date
     - Ordered progression (Week 1 → Week 2 → etc.)
     - Generates TaskNotes with specific due dates/scheduled times
  
  2. **Free-form/Random Access** → Like free jazz (flexible rhythm)
     - Cookbook-style: browse at will
     - No mandatory sequence
     - Random or user-chosen order
     - TaskNotes optional or self-scheduled

**Example Contrast:**
- **Baking CLASS (Sequenced):** "Week 1: Bread basics (Nov 18), Week 2: Pastries (Nov 25)" → Auto-generates tasks with dates
- **Recipe COLLECTION (Random):** "50 recipes, pick any" → No timeline, browse freely

**Key Insight:** Same content (recipes), different temporal structure. The capsule's "time signature" determines if/how it generates scheduled events.

---

### Design Implications

**1. Capsule Descriptor File ("Cypher Key")**
- Could be named: `capsule-manifest.md` or `_capsule.yaml`
- Declares:
  - Domain type (TCM, cooking, programming, etc.)
  - Custom frontmatter schema extensions
  - Valid data section types for this domain
  - Sequence mode: `sequenced` | `freeform` | `hybrid`

**2. Timeline/Sequence Configuration**
- If `sequenced`:
  - Capsule has timeline.yaml or schedule section
  - References capsule start_date variable
  - Maps content → calendar events
  - Auto-generates TaskNotes with:
    - `scheduled: start_date + offset`
    - `due: start_date + offset + duration`
    - Links to specific capsule material

- If `freeform`:
  - No timeline required
  - Content just exists as reference
  - User browses dashboard at will
  - Optional manual task creation

**3. Hybrid Example:**
- TCM 101 CLASS = sequenced 12-week course
- TCM Herb Reference = freeform encyclopedia
- Same domain (TCM), different temporal structures

---

### Emerging Questions


#### Universal "Staff Lines" - The Minimum Grid

**Proposed Universal Fields (Present in EVERY capsule note):**
```yaml
---
id: unique-identifier           # UUID or semantic ID
name: "Display Name"            # Human-readable title
type: content-type              # herb, pattern, quiz, study, etc.
tags: [array, of, tags]         # Categorization/filtering
created: YYYY-MM-DD             # Creation timestamp
updated: YYYY-MM-DD             # Last modification timestamp
---
```

**Potential Additions to Consider:**
- `capsule_id` or `source_capsules: []` - Track which capsule(s) this note belongs to
- `version: "1.0.0"` - Semantic versioning for updates/expansions
- `aliases: []` - Alternative names (already in some examples)
- `related: []` - Cross-references (already in patterns)

**Decision:** Start with the 6-field minimum, validate through usage, expand as needed.

---

#### Domain Extension Strategy: The "Cypher File"

**YES - "Cypher" is perfect!** 
- **Cypher** = key to decrypt/decode (exactly right!)
- The capsule-cypher.yaml is the **Rosetta Stone** for this capsule

**How it works:**
```yaml
# capsule-cypher.yaml (in capsule root)
capsule_id: "TCM_Fundamentals_v1"
domain_type: "traditional_chinese_medicine"
version: "1.0.0"

# Maps content types → required data sections
type_schema:
  herb:
    required_sections: [herb_data]
    optional_sections: [recipe_data, cultivation_data]
  
  pattern:
    required_sections: [pattern_data]
    optional_sections: [case_study_data]
  
  formula:
    required_sections: [formula_data]
    optional_sections: [recipe_data, preparation_data]

# Defines what fields exist in each data section
data_schemas:
  herb_data:
    hanzi: string
    pinyin: string
    pharmaceutical: string
    taste: array
    temperature: string
    channels: array
    dosage: string
    functions: array
    # ... etc
  
  recipe_data:
    cuisine: string
    prep_time: integer
    cook_time: integer
    ingredients: array
    steps: array
    # ... etc
```

**Key Insight:** The cypher file is the "type system" for this capsule's domain.

---

#### BREAKTHROUGH: Cross-Domain Notes (Capsule Composability!)

**🚀 Major Design Decision: Notes can have MULTIPLE domain data sections!**

**Example: Ginger Note**
```yaml
---
id: note-ginger-20251115
name: "Ginger / 生姜 (Shēng Jiāng)"
type: herb  # Primary type
tags: [herb, spice, tcm, culinary, medicinal]
created: 2025-11-15
updated: 2025-11-15

# BELONGS TO MULTIPLE CAPSULES
source_capsules:
  - TCM_Materia_Medica_v1
  - Culinary_Herbs_v2
  - Home_Remedies_v1

# MULTIPLE DOMAIN DATA SECTIONS
herb_data:
  hanzi: "生姜"
  pinyin: "Shēng Jiāng"
  temperature: warm
  taste: [acrid]
  channels: [Lung, Spleen, Stomach]
  functions:
    - releases the exterior
    - warms the middle jiao
    - transforms phlegm

recipe_data:
  cuisine: asian
  flavor_profile: [spicy, warming, aromatic]
  common_uses:
    - stir_fry
    - tea
    - marinades
  pairs_with: [garlic, soy_sauce, honey]

remedy_data:
  conditions: [nausea, cold, indigestion]
  preparations: [tea, compress, tincture]
  dosage_home_use: "1-2 slices fresh"
---
```

**Implications:**

1. **Capsule Updates/Expansions:**
   - TCM capsule creates herb note with `herb_data`
   - Later, Culinary capsule ADDS `recipe_data` to same note
   - Note grows richer with each capsule that touches it
   - `source_capsules` tracks provenance

2. **Cross-Domain Queries:**
   - "Show me all herbs that are also culinary ingredients"
   - "Find TCM patterns treated by ingredients in my kitchen"
   - Rich cross-pollination between knowledge domains

3. **Capsule Import/Export:**
   - When importing TCM capsule: adds/updates `herb_data` sections
   - When importing Culinary capsule: adds/updates `recipe_data` sections
   - Merge strategy: additive (new sections) + versioned updates (existing sections)

4. **Cypher File Role:**
   - Each capsule's cypher declares which data sections IT contributes
   - Multiple capsules can contribute to same note type
   - System validates: "does this note have required sections for its source capsules?"

**Architecture Principle:** 
> Notes are composable knowledge units. Capsules are lenses that add domain-specific structure to shared notes.

---

### Key Architectural Insights from Metaphor


#### Staff Lines = File Type Definition (Refined Understanding)

**CORRECTION - Staff Lines Define FILE PURPOSE within capsule:**

The "staff lines" (universal fields) tell you **what kind of file this is** in the capsule ecosystem:

```yaml
---
id: unique-identifier
name: "Display Name"
type: flashcard | quiz_bank | guided_conversation | study_material | root_note | etc.
tags: [categorization]
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_capsules: [which capsules include this file]
---
```

**File Types (The "Instruments" in the Score):**
- `root_note` → Core knowledge/reference material
- `study_material` → Learning content
- `flashcard` → Spaced repetition cards
- `quiz_bank` → Question repository
- `guided_conversation` → Interactive learning dialogue
- `slide_deck` → Presentation/lecture content
- `task_sequence` → Scheduled activities
- `dashboard` → Navigation/overview
- `cypher` → Capsule metadata/schema definition

**Each file type can ALSO have domain-specific data sections:**
```yaml
type: root_note
herb_data:
  # TCM-specific fields
recipe_data:
  # Culinary-specific fields
```

---

#### Master Dashboard: The "Conductor's Score"

**Vision: Master Dashboard as Portal to All Capsules**

**Core Functions:**

**1. Capsule Windows (Quick Links)**
```
┌─────────────────────────────────────────────┐
│  MASTER DASHBOARD - My Knowledge System     │
├─────────────────────────────────────────────┤
│                                             │
│  📚 Active Capsules                         │
│  ┌──────────────┐  ┌──────────────┐        │
│  │ TCM 101      │  │ Cooking Class│        │
│  │ Week 3/12    │  │ Week 1/8     │        │
│  │ [Open] 📊    │  │ [Open] 📊    │        │
│  └──────────────┘  └──────────────┘        │
│                                             │
│  ┌──────────────┐  ┌──────────────┐        │
│  │ Herb Ref     │  │ Recipe Book  │        │
│  │ Freeform     │  │ Freeform     │        │
│  │ [Open] 📊    │  │ [Open] 📊    │        │
│  └──────────────┘  └──────────────┘        │
└─────────────────────────────────────────────┘
```

**2. Cross-Capsule Analysis**
- **Connection Graph:** "Ginger appears in 3 capsules, 47 notes link to it"
- **Shared Notes:** "12 notes are enhanced by multiple capsules"
- **Domain Overlap:** "TCM + Culinary share 23 ingredients"

**3. Aggregate Progress**
```
Overall Progress: 45%
├─ TCM 101: 25% (Week 3/12) - Sequenced
├─ Cooking Class: 12.5% (Week 1/8) - Sequenced  
├─ Herb Reference: Browsing - Freeform
└─ Recipe Book: Browsing - Freeform
```

**4. Active Timelines (Unified Calendar View)**
```
This Week:
Mon Nov 18: TCM - Study Qi Deficiency Pattern
Tue Nov 19: Cooking - Baking Basics Lecture
Wed Nov 20: TCM - Quiz: Patterns (due)
Thu Nov 21: Cooking - Practice: Sourdough Bread
Fri Nov 22: TCM - Herb Flashcards Review
```

**5. Capsule Library (Collection Management)**
```
📦 Installed Capsules (8)
  ✓ TCM_Materia_Medica_v1 (completed)
  ▶ TCM_101_v2 (in progress - 25%)
  ▶ Culinary_Herbs_v1 (in progress - browsing)
  ○ Home_Remedies_v1 (not started)
  ...
  
📥 Available Updates (2)
  ↑ TCM_101_v2 → v2.1 (new herb data)
  ↑ Culinary_Herbs_v1 → v1.2 (5 new recipes)
```

**6. Unified Task Queue (All Capsules)**
```
Next Up (sorted by due date):
[ ] Wed: TCM Quiz - Patterns (due 11/20)
[ ] Thu: Cook Sourdough Bread (scheduled 11/21 2pm)
[ ] Fri: Review 20 Herb Flashcards (due 11/22)
[ ] Sat: Complete Guided Conversation: Diagnosis (optional)
```

**7. Quick Stats Dashboard**
```
📊 This Week's Activity
├─ Study Hours: 4.5 / 10 target
├─ Flashcards Reviewed: 87 / 100
├─ Quizzes Completed: 1 / 2
├─ Tasks Completed: 5 / 8
└─ Streak: 12 days 🔥
```

---

### Master Dashboard Architecture

**Implementation Approach:**

```yaml
# master-dashboard.md (in vault root)
---
type: master_dashboard
title: "My Knowledge System"
view_modes:
  - library      # Capsule collection browser
  - calendar     # Unified timeline
  - tasks        # Cross-capsule task list
  - progress     # Aggregate stats
  - connections  # Cross-capsule graph
default_view: library
---

# Dynamic queries pull from all capsule dashboards
```

**Data Flow:**
1. Each capsule has its own dashboard with local context
2. Master dashboard queries across all capsule dashboards
3. Dataview aggregates:
   - Active timelines from sequenced capsules
   - Task items from all capsules
   - Progress metrics from capsule manifests
   - Cross-references between notes

**Key Principle:**
> The Master Dashboard is a **view layer** over individual capsule dashboards. It doesn't duplicate data—it aggregates and presents unified cross-capsule insights.

---

### Phase 1 Summary: Metaphor Mapping Complete ✓

**Musical Score Metaphor Revealed:**

🎵 **Universal Notation (Staff Lines):**
- 6 universal frontmatter fields define file type/identity
- Works for ANY knowledge domain

🎼 **Key Signature (Cypher File):**
- Declares domain-specific data schemas
- Each capsule has cypher defining its custom fields
- Enables validation and tooling

⏱️ **Time Signature (Sequence Mode):**
- Sequenced (strict timeline) vs Freeform (browse at will)
- Determines if/how tasks are auto-generated
- Same content, different temporal structures

🎹 **Instruments (File Types):**
- root_note, study_material, flashcard, quiz_bank, guided_conversation, slides, tasks
- Each file type can have multiple domain data sections

🎻 **Ensemble (Cross-Domain Notes):**
- Notes can belong to multiple capsules
- Capsules ADD domain sections to shared notes
- Composable, expandable knowledge units

🎺 **Conductor's Score (Master Dashboard):**
- Portal to all capsule dashboards
- Unified timeline, tasks, progress
- Cross-capsule analytics and connections
- Library management and updates

**Ready to move to Phase 2: Morphological Analysis?**

This will systematically explore parameter combinations to validate the architecture.


---

## Phase 2: Morphological Analysis

**Start Time:** Phase transition
**Goal:** Systematically explore design parameter combinations to validate architecture

### Design Parameters Identified

From Phase 1, we have several independent design axes that need to work together:


#### Design Parameter Matrix

**Axis 1: Frontmatter Strategy**
- **SELECTED: A2 - Nested sections (domain fields in sub-objects)**
- **Rationale:** Domain-specific metadata lives in named sections (herb_data, pattern_data, recipe_data)
- **Benefit:** Clear separation of concerns, supports multiple domain sections per note
- **Example:** 
  ```yaml
  ---
  # Universal fields
  id: note-ginger
  name: Ginger
  type: herb
  tags: [herb, tcm, culinary]
  
  # Domain-specific sections
  herb_data:
    hanzi: "生姜"
    temperature: warm
  
  recipe_data:
    cuisine: asian
    prep_time: 10
  ---
  ```

---

**Axis 2: Capsule Packaging**
- **SELECTED: B1/B2 Hybrid - Folder bundle OR zip archive**
- **Package Contents:**
  - Root notes (core knowledge files)
  - Study material (quizzes, flashcards, guided conversations, slides)
  - Other relevant files (PDFs, images, code, etc.)
  - capsule-cypher.yaml (manifest with schema definitions)
  - capsule-dashboard.md (navigation template)
  
- **Structure:**
  ```
  /TCM_Materia_Medica_v1/
  ├── capsule-cypher.yaml       # Schema & metadata
  ├── capsule-dashboard.md       # Dashboard template
  ├── root_notes/
  │   ├── Ai_Ye.md              # Herb notes
  │   ├── Dang_Gui.md
  │   └── ...
  ├── study_material/
  │   ├── flashcards/
  │   ├── quizzes/
  │   └── slides/
  └── resources/
      ├── images/
      └── references/
  ```

- **Export Formats:**
  - **Development:** Folder (easy to edit/version control)
  - **Distribution:** `.capsule` zip file (portable, shareable)

---

**Axis 3: Dashboard Template Strategy**
- **SELECTED: C2 - Base template + domain extensions**
- **Approach:**
  - **Universal template** has generic headings/sections
  - Links to master dashboard for cross-capsule aggregation
  - **Domain sections** can be customized per capsule
  
- **Universal Dashboard Sections (every capsule has these):**
  ```markdown
  # Capsule Dashboard: {{capsule_name}}
  
  ## Overview
  - Capsule ID: {{capsule_id}}
  - Version: {{version}}
  - Progress: {{completion_percentage}}%
  
  ## Quick Links
  - [[Master Dashboard]] ← Back to all capsules
  - Root Notes: {{root_note_count}}
  - Study Material: {{study_material_count}}
  
  ## Active Timeline (if sequenced)
  [Dataview query: upcoming tasks]
  
  ## Recent Activity
  [Dataview query: recently updated notes]
  ```

- **Domain-Specific Extensions (custom per capsule):**
  ```markdown
  ## TCM Categories (custom for TCM capsule)
  - Herbs by Category
  - Patterns by Type
  - Formulas by Function
  
  ## Recipe Collections (custom for Cooking capsule)
  - By Cuisine
  - By Difficulty
  - By Prep Time
  ```

- **Master Dashboard Integration:**
  - Universal fields get relayed: progress %, task counts, recent activity
  - Master aggregates these across all capsules
  - Custom sections stay local to individual capsule dashboards

---

**Axis 4: Import/Export Merge Strategy**
- **PRIMARY: D3 - Section-level merge**
- **FALLBACK: D1 - Additive when uncertain**

**How Section-Level Merge Works:**

**Scenario A: Same note, same capsule (update)**
```yaml
# Existing note in vault
---
id: note-ginger
source_capsules: [TCM_v1]
herb_data:
  hanzi: "生姜"
  temperature: warm
---
```

**Import TCM_v1.1 (updated capsule):**
```yaml
# Updated version
herb_data:
  hanzi: "生姜"
  temperature: warm
  dosage: "3-9g"  # NEW FIELD
---
```

**Result: UPDATE (same capsule, newer version)**
```yaml
---
id: note-ginger
source_capsules: [TCM_v1.1]  # Version updated
herb_data:
  hanzi: "生姜"
  temperature: warm
  dosage: "3-9g"  # Added from update
---
```

---

**Scenario B: Same note, different capsule (additive merge)**
```yaml
# Existing note
---
id: note-ginger
source_capsules: [TCM_v1]
herb_data:
  hanzi: "生姜"
  temperature: warm
---
```

**Import Culinary_Herbs_v1 (different capsule, same ingredient):**
```yaml
# New capsule adds recipe data
source_capsules: [Culinary_Herbs_v1]
recipe_data:
  cuisine: asian
  prep_time: 10
---
```

**Result: ADDITIVE MERGE (different capsule)**
```yaml
---
id: note-ginger
source_capsules: [TCM_v1, Culinary_Herbs_v1]  # Both listed
herb_data:
  hanzi: "生姜"
  temperature: warm
recipe_data:  # NEW SECTION added
  cuisine: asian
  prep_time: 10
---
```

---

**Scenario C: Personal notes preservation**
```yaml
# User's enhanced note
---
id: note-ginger
source_capsules: [TCM_v1]
herb_data:
  hanzi: "生姜"
  temperature: warm

# User's personal section (not from capsule)
---

## My Study Notes
- Tried ginger tea for nausea - worked great!
- Remember: warming, acrid
```

**Import TCM_v1.1 (update):**

**Result: PRESERVE user content, update capsule data**
```yaml
---
id: note-ginger
source_capsules: [TCM_v1.1]
herb_data:
  hanzi: "生姜"
  temperature: warm
  dosage: "3-9g"  # Updated from capsule

# User content PRESERVED (not in frontmatter = safe)
---

## My Study Notes
- Tried ginger tea for nausea - worked great!
- Remember: warming, acrid
```

---

**Merge Rules Summary:**

1. **Same capsule ID + newer version** → UPDATE frontmatter sections
2. **Different capsule ID** → ADD new sections (never overwrite other capsule's sections)
3. **User content outside frontmatter** → ALWAYS PRESERVE (never touched by import)
4. **Conflict detection** → If same section from different capsules, prompt user:
   ```
   Conflict detected:
   - TCM_v1 defines: herb_data
   - Culinary_v1 also defines: herb_data
   
   Options:
   a) Keep both (rename one to herb_data_tcm, herb_data_culinary)
   b) Merge fields (combine into single herb_data)
   c) Skip import of conflicting section
   ```

---

### Tested Scenario: TCM Student

**Scenario Replay:**
1. Import "TCM Materia Medica" (500 herbs) → Creates 500 notes with `herb_data`
2. Add personal study notes to herb files (below frontmatter)
3. Import "TCM 101 Course" (references 50 same herbs) → Wants to add `study_material` links

**Solution with selected parameters:**

**Step 1: Initial import (TCM Materia Medica)**
- **B1:** Extracts folder → 500 herb notes created
- **A2:** Each has `herb_data` section
- **C2:** Capsule dashboard created with herb categories

**Step 2: User adds study notes**
- User edits notes, adds content BELOW frontmatter
- Personal notes are NOT in frontmatter = safe from imports

**Step 3: Import TCM 101 Course**
- **D3 Section-level merge** detects:
  - 50 herb notes already exist (same `id`)
  - TCM_101 is DIFFERENT capsule from Materia_Medica
  - TCM_101 wants to add `course_data` section with study links

**Result:**
```yaml
---
id: note-ai-ye
name: Ai Ye
type: herb
source_capsules: [TCM_Materia_Medica_v1, TCM_101_v1]  # Both!

herb_data:  # From Materia Medica
  hanzi: "艾叶"
  functions: [...]

course_data:  # ADDED by TCM 101
  week: 3
  quiz_id: quiz-herbs-week3
  flashcard_deck: week3-herbs
---

# Ai Ye (Mugwort Leaf)

[Original capsule content]

## My Study Notes
[User's preserved notes - untouched]
```

**Outcome:**
✓ No duplicate notes
✓ User study notes preserved
✓ Both capsules contribute data sections
✓ Course can link to herbs via `course_data` section

---

### Design Validation: PASSED ✓

**Selected Architecture:**
- **A2:** Nested domain sections (extensible, composable)
- **B1/B2:** Folder/zip bundle (flexible distribution)
- **C2:** Base template + domain extensions (universal + customizable)
- **D3:** Section-level merge (smart, safe, composable)

**This combination supports:**
✓ Cross-domain notes (ginger = herb + recipe)
✓ Capsule updates (version-aware)
✓ User personalization (preserved outside frontmatter)
✓ Multiple capsules enhancing same notes
✓ Universal + custom dashboard sections


---

## Phase 3: First Principles Thinking

**Start Time:** Final phase
**Goal:** Strip away assumptions and distill to essential capsule foundation

### The First Principles Questions

Rebuilding from fundamental truths about what a "universal educational content unit" truly requires.


#### Fundamental Truth #1: The Essence of a Capsule

> **"A capsule is the smallest unit of information that can be used and shared universally between users or other capsules."**

**Breaking this down:**
- **Smallest unit** → Self-contained, atomic, complete in itself
- **Information** → Knowledge, not just data; meaningful content
- **Can be used** → Functional, actionable, consumable by someone
- **Shared universally** → Platform-agnostic, format that anyone can understand
- **Between users** → Human-to-human knowledge transfer
- **Or other capsules** → Machine-readable, composable with other units

**Implications:**
1. A capsule must be **self-describing** (you can understand it without external context)
2. A capsule must be **portable** (works regardless of where it's imported)
3. A capsule must be **composable** (can combine with others without breaking)
4. A capsule must have **identity** (unique, trackable, versionable)
5. A capsule must declare **dependencies** (what it needs, what it provides)

---

#### Question 2: What Makes Information "Universal"?


#### Fundamental Truth #2: Universal = Adherence to Framework

> **"Universality comes from following a reproducible framework, not from complexity or content. A capsule can be a single concept or an entire encyclopedia—both are equally valid if they follow the capsule structure."**

**The Framework (Non-Negotiable Minimum):**

1. **Root Material** (required)
   - The core knowledge content
   - Can be 1 note or 1000 notes
   - Self-contained information units

2. **Study Material** (optional but common)
   - Flashcards, quizzes, slides, guided conversations
   - Reinforcement/practice resources
   - Interactive learning components

3. **Other Relevant Files** (optional)
   - PDFs, images, code, media
   - Supporting context and references
   - Anything that enhances understanding

4. **Capsule Cypher** (required - THE KEY)
   - Declares folder structure
   - Lists all notes/files in capsule
   - Defines sequence (if applicable)
   - Specifies domain schemas
   - **Provides capsule overview/metadata for display**

**Key Insight: The Cypher is the Contract**

The cypher file is what makes a capsule "readable" by:
- **Humans** → Overview shows what's in the capsule, how it's organized
- **Systems** → Machine-readable manifest for import/export/validation
- **Other Capsules** → Declares what data sections this capsule contributes

**Scalability:**
- **Minimal capsule:** 1 root note + cypher = valid capsule
- **Complex capsule:** 500 notes + full study materials + resources + cypher = valid capsule
- **Both work** because they both follow the framework

---

#### Question 3: The Irreducible Minimum - What Can't You Remove?


#### Fundamental Truth #3: Text Files = Universal Portability

> **"Everything is markdown text files. No proprietary formats. Pure text is universally transferable, extractable, and manipulatable. This is the foundation of true portability."**

**Why This Matters:**
- Works in ANY Obsidian vault
- Works in ANY text editor
- Can be version controlled (git)
- Can be scripted/automated
- Future-proof (text never becomes obsolete)
- Platform-independent

**Plugin Dependencies:**
- Base plugins like Dataview, TaskNotes, etc. are OPTIONAL
- Cypher declares which plugins are needed/recommended
- Capsule degrades gracefully without plugins (still readable, just less functional)

---

#### The Irreducible Minimum: Capsule Cypher Template

**Testing the absolute bare minimum for `capsule-cypher.yaml`:**

```yaml
# ============================================
# CAPSULE CYPHER - Minimum Required Fields
# ============================================

# === IDENTITY ===
capsule_id: "unique_capsule_identifier_v1"
  # Purpose: Unique identifier (prevents collisions, enables versioning)
  # Format: domain_name_version (e.g., TCM_Herbs_v1, Python_Basics_v2)
  # Required: YES - without this, can't track what capsule a note belongs to

name: "Human Readable Capsule Name"
  # Purpose: Display name for dashboards and UI
  # Required: YES - users need to know what this capsule is

version: "1.0.0"
  # Purpose: Semantic versioning for updates/compatibility
  # Required: YES - enables update detection and merge strategies

# === CONTENT DECLARATION ===
domain_type: "subject_domain"
  # Purpose: Declares subject area (tcm, cooking, programming, etc.)
  # Required: YES - tells system what kind of knowledge this contains

# === STRUCTURE ===
folder_structure:
  root_notes: "path/to/root_notes"
  study_material: "path/to/study_material"  # optional
  resources: "path/to/resources"  # optional
  # Purpose: Declares where content lives
  # Required: YES - import/export needs to know where files are

# === MANIFEST (File Inventory) ===
contents:
  root_notes:
    - file: "root_notes/note1.md"
      id: "note-unique-id-1"
    - file: "root_notes/note2.md"
      id: "note-unique-id-2"
  
  study_material:  # optional section
    flashcards:
      - file: "study_material/flashcards/deck1.md"
    quizzes:
      - file: "study_material/quizzes/quiz1.md"
  
  resources:  # optional section
    - file: "resources/diagram.png"
    - file: "resources/reference.pdf"
  # Purpose: Complete inventory of all files in capsule
  # Required: YES - import needs to know exactly what to copy

# === SCHEMA DEFINITION ===
data_schemas:
  # Defines domain-specific frontmatter sections this capsule uses
  herb_data:
    hanzi: string
    pinyin: string
    temperature: string
    # ... all fields this capsule's notes will have
  
  pattern_data:
    etiology: string
    symptoms: array
    # ... etc
  # Purpose: Type system for this capsule's domain
  # Required: YES - enables validation, tooling, cross-capsule compatibility

# === SEQUENCE (if applicable) ===
sequence_mode: "freeform"  # or "sequenced" or "hybrid"
  # Purpose: Declares if capsule has timeline/ordering
  # Required: YES - determines if tasks are auto-generated

timeline:  # only if sequence_mode = "sequenced"
  start_offset_variable: "capsule_start_date"
  events:
    - day: 1
      material: "note-unique-id-1"
      estimated_minutes: 30
    - day: 3
      material: "quiz-1"
      estimated_minutes: 15
  # Purpose: Maps content to calendar
  # Required: CONDITIONAL - only if sequenced

# === DEPENDENCIES ===
required_plugins:
  - name: "dataview"
    min_version: "0.5.0"
  - name: "obsidian-tasks-plugin"
    min_version: "1.0.0"
  # Purpose: Declares what plugins are needed
  # Required: NO - but recommended for enhanced functionality

recommended_plugins:
  - name: "advanced-slides"
  - name: "spaced-repetition"
  # Purpose: Optional plugins that enhance experience
  # Required: NO

# === METADATA ===
author: "Creator Name"
created: "2025-11-15"
updated: "2025-11-15"
description: "Brief description of what this capsule teaches/contains"
tags: [tag1, tag2, domain_tag]
  # Purpose: Discovery, categorization, search
  # Required: RECOMMENDED - helps users find and understand capsule

# === DASHBOARD ===
dashboard_file: "capsule-dashboard.md"
  # Purpose: Points to the capsule's navigation file
  # Required: RECOMMENDED - provides entry point for users


```

---

### SYNTHESIS: The Complete Capsule Author Template

**From First Principles, the absolute minimum viable capsule is:**

```
/MyCapsule_v1/
├── capsule-cypher.yaml          # THE CONTRACT (required)
└── root_notes/
    └── single-note.md            # THE CONTENT (minimum 1 file)
```

**That's it. Everything else is enhancement.**

---

#### The Universal Note Template

**Every note in every capsule must have these universal fields:**

```yaml
---
# === UNIVERSAL FIELDS (REQUIRED) ===
id: "note-unique-identifier-20251115"
name: "Human Readable Note Title"
type: root_note  # or flashcard, quiz_bank, study_material, etc.
tags: [domain, topic, subtopic]
created: 2025-11-15
updated: 2025-11-15

# === CAPSULE PROVENANCE (REQUIRED) ===
source_capsules:
  - MyCapsule_v1

# === DOMAIN-SPECIFIC SECTIONS (OPTIONAL, defined in cypher) ===
domain_data:
  field1: value
  field2: value
  # ... as many domain sections as needed

---

# Note Content (Markdown)

Your actual content goes here...
```

---

### Final Architecture Principles

**1. Separation of Concerns**
- Universal fields = identity, type, provenance
- Domain sections = subject-specific metadata
- Body content = the actual knowledge

**2. Composability**
- Multiple capsules can enhance the same note
- Each adds its own domain section
- Never conflicts, only extends

**3. Portability**
- Pure markdown text files
- Self-describing via cypher
- Works anywhere markdown works

**4. Scalability**
- Minimal: 1 note + cypher
- Complex: 1000s of notes + full study system
- Same architecture, different scale

**5. Versioning**
- Semantic versioning in cypher
- Enables update detection
- Supports migration paths

---

### The Three-Tier System

**Tier 1: Note Level**
- Universal frontmatter fields
- Domain-specific data sections
- Markdown content body

**Tier 2: Capsule Level**
- Capsule cypher (the contract)
- Folder structure (organized content)
- Dashboard (navigation/overview)

**Tier 3: Vault Level**
- Master dashboard (portal to all capsules)
- Cross-capsule queries
- Aggregate progress/analytics

---

## Session Complete! 🎉

### What We Discovered

**Phase 1: Metaphor Mapping**
- Musical score metaphor unlocked the architecture
- Universal notation + domain flexibility
- Composable, extensible design

**Phase 2: Morphological Analysis**
- Validated design parameter combinations
- Tested real-world scenarios
- Confirmed architecture robustness

**Phase 3: First Principles**
- Distilled to irreducible minimum
- Text files = universal portability
- Cypher = the contract that enables everything

---

### Key Deliverables

1. **Universal Note Frontmatter Template** ✓
2. **Capsule Cypher Structure** ✓
3. **Folder Organization Pattern** ✓
4. **Import/Export Merge Strategy** ✓
5. **Dashboard Architecture** (universal + domain-specific) ✓
6. **Cross-Domain Composability Model** ✓

---

### Next Steps for Implementation

**Immediate:**
1. Create capsule-cypher-template.yaml
2. Create universal-note-template.md
3. Update OCDS documentation with new architecture

**Short-term:**
4. Build capsule import/export CLI commands
5. Create dashboard templates (master + capsule)
6. Implement section-level merge logic

**Medium-term:**
7. Build capsule authoring wizard
8. Create validation tools
9. Set up capsule repository/sharing system

---

**Session Duration:** ~90 minutes
**Techniques Used:** Metaphor Mapping → Morphological Analysis → First Principles
**Output:** Complete capsule metadata architecture specification

**Status:** COMPLETE ✓

---

*Saved to: /docs/bmm-brainstorming-session-2025-11-15.md*

