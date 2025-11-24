# OCDS Folder Structure & Organization

**Version:** 1.0.0  
**Last Updated:** 2025-11-10  
**Purpose:** Comprehensive guide to organizing content in the OCDS ecosystem

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Core Folder Architecture](#core-folder-architecture)
3. [Root Note Discovery System](#root-note-discovery-system)
4. [Content Organization Strategies](#content-organization-strategies)
5. [Material Linking System](#material-linking-system)
6. [Capsule CLI Integration](#capsule-cli-integration)
7. [Best Practices](#best-practices)
8. [Migration Guide](#migration-guide)

---

## Overview

The OCDS system uses a **hybrid directory + tag-based** approach for organizing educational content. This provides the flexibility of free-form organization while maintaining the discoverability needed for automation.

### Key Principles

1. **Root Notes** are the source of truth
2. **Generated Materials** link back to root notes
3. **Discovery** works across the entire vault
4. **Organization** is flexible but follows conventions
5. **Metadata** enables automation and linking

---

## Core Folder Architecture

### Complete Vault Structure

```
TCM_Knowledge_Base/                    # Root vault directory
│
├── capsule/                           # Capsule CLI tool (Python package)
│   ├── commands/                      # CLI command implementations
│   │   ├── config.py                 # Configuration management
│   │   ├── list.py                   # List root notes
│   │   ├── conversation.py           # Guided conversations
│   │   ├── generate.py               # Material generation
│   │   └── research.py               # Deep research pipeline
│   └── utils/                        # Utility functions
│       ├── config.py                 # Config loader
│       ├── validation.py             # Pattern/file validation
│       └── output.py                 # CLI output formatting
│
├── scripts/                          # Automation scripts
│   ├── deep_research_pipeline.py    # Full research → materials
│   ├── gemini_research.py           # Simple research
│   ├── conversation_engine.py       # Guided learning
│   ├── content_generator.py         # Material generation
│   └── generate_all_materials.py    # Batch generation
│
├── TCM_Patterns/                     # 🎯 CURATED ROOT NOTES
│   ├── Zang Fu Patterns/            # Organized by category
│   │   ├── Heart Blood Deficiency.md
│   │   ├── Spleen Qi Deficiency.md
│   │   └── ...
│   ├── Channel Patterns/
│   ├── Eight Principles Patterns/
│   ├── Qi, Blood, and Body Fluids Patterns/
│   ├── Shang Han Lun Patterns/
│   ├── Wen Bing Lun Patterns/
│   └── San Jiao Patterns/
│
├── Materials/                        # 🎯 GENERATED CONTENT
│   ├── TCM_101/                     # Class-specific materials
│   │   ├── Root_Note_*.md          # Generated root notes
│   │   ├── *_Flashcards.md         # Auto-generated flashcards
│   │   ├── *_Quiz.md               # Auto-generated quizzes
│   │   ├── *_Slides.md             # Auto-generated slides
│   │   ├── *_Study_Material.md     # Study guides
│   │   └── *_Tasks.md              # Task lists
│   │
│   ├── TCM_Patterns/                # Legacy materials
│   │   ├── Quiz.md
│   │   └── Flashcards.md
│   │
│   └── Traditional_Chinese_Medicine_*/  # Research output folders
│       ├── Root_Note.md            # Deep research root note
│       ├── Study_Material.md       # Auto-generated study guide
│       ├── Flashcards.md           # Auto-generated cards
│       ├── Quiz.md                 # Auto-generated quiz
│       └── Slides.md               # Auto-generated slides
│
├── TCM_Formulas/                     # Formula database
│   ├── Ba Zhen Tang.md
│   ├── Si Jun Zi Tang.md
│   └── ...
│
├── TCM_Herbs/                        # Herb database
│   ├── Ren Shen.md
│   ├── Huang Qi.md
│   └── ...
│
├── TCM_Points/                       # Acupuncture points database
│   ├── BL-13 (Fei Shu).md
│   ├── ST-36 (Zu San Li).md
│   └── ...
│
├── Flashcards/                       # Structured flashcard library
│   ├── Acupuncture_Points/
│   ├── Formulas/
│   ├── Herbs/
│   └── Chinese_Characters/
│
├── Board Exams/                      # Exam prep materials
│   ├── NCCAOM/
│   ├── CALE/
│   └── Sample_Questions_Bank.md
│
├── Books/                            # Reference textbooks (PDFs)
│
├── Research/                         # Research notes
│
├── OCDS_Documentation/               # 📚 System documentation
│   ├── 01_System_Overview/
│   ├── 02_Plugin_Integration/
│   ├── 03_Data_Standards/
│   ├── 04_Folder_Structure/         # 👈 This document
│   ├── 05_Material_Templates/
│   ├── 06_Automation_Scripts/
│   ├── 07_Grading_System/
│   ├── 08_Unlock_System/
│   ├── 09_Dashboard_Design/
│   ├── 10_Class_Creation/
│   ├── 11_Distribution/
│   ├── 12_Best_Practices/
│   └── 13_Examples/
│
└── .obsidian/                        # Obsidian configuration
    ├── plugins/                     # Installed plugins
    └── snippets/                    # CSS snippets
```

---

## Root Note Discovery System

### How Capsule Finds Root Notes

The Capsule CLI uses a **hybrid discovery system** that combines directory scanning with metadata-based tagging:

#### **Method 1: Directory Scanning** (Current Implementation)

```python
# capsule/commands/list.py
patterns_dir = kb_path / "TCM_Patterns"

# Scans recursively:
TCM_Patterns/
├── *.md                            # Direct children
└── */                              # Subdirectories
    └── *.md                        # Nested patterns
```

**Searched locations:**
1. `TCM_Patterns/` (primary)
2. `TCM_Patterns/*/` (all subdirectories)
3. `Materials/TCM_Patterns/` (fallback)

**How it works:**
```bash
cap list
# → Finds: Heart Blood Deficiency.md in TCM_Patterns/Zang Fu Patterns/
# → Shows: "Heart Blood Deficiency"
```

#### **Method 2: Tag-Based Discovery** (Recommended Enhancement)

Root notes can be discovered **anywhere** in the vault using YAML frontmatter:

```yaml
---
ocds_type: "root_note"              # Identifies as discoverable root note
material_id: "pattern-xyz"          # Unique identifier
type: "pattern"                     # Content type
category: ["Zang Fu Pattern"]       # Category tags
status: "published"                 # published | draft | archived
source: "curated"                   # curated | generated | research
---
```

**Future implementation:**
```bash
cap list --method tag
# → Finds root notes in TCM_Patterns/, Materials/, Research/, anywhere!
```

---

## Content Organization Strategies

### Strategy 1: Curated Hierarchical (Recommended for Course Creators)

**Use case:** Building structured curriculum with organized topics

```
TCM_Patterns/
├── Zang Fu Patterns/
│   ├── 01_Heart_Patterns/
│   │   ├── Heart Qi Deficiency.md
│   │   ├── Heart Blood Deficiency.md
│   │   └── Heart Fire Blazing.md
│   ├── 02_Lung_Patterns/
│   └── 03_Spleen_Patterns/
├── Channel Patterns/
└── Six Stages Theory/
```

**Pros:**
- Clear visual organization
- Easy to browse
- Natural curriculum flow
- Good for beginners

**Cons:**
- Rigid structure
- Hard to cross-categorize
- Doesn't fit multi-dimensional topics

---

### Strategy 2: Flat + Tags (Recommended for Generated Content)

**Use case:** Research pipeline, AI-generated content, flexible organization

```
Materials/
└── Generated_Patterns/
    ├── Insomnia_Pattern.md
    ├── Chronic_Fatigue_Pattern.md
    └── Migraine_Pattern.md
```

**Metadata enables discovery:**
```yaml
---
ocds_type: "root_note"
tags: ['pattern', 'zang-fu', 'heart', 'blood', 'deficiency']
category: ['Zang Fu', 'Blood Deficiency']
western_conditions: ['Insomnia', 'Anxiety', 'Palpitations']
---
```

**Pros:**
- Flexible organization
- Multi-dimensional categorization
- Works with AI generation
- Cross-referencing via tags

**Cons:**
- Requires metadata discipline
- Harder to browse manually
- Needs good search tools

---

### Strategy 3: Hybrid (Recommended for OCDS)

**Use case:** Best of both worlds - curated + generated content

```
TCM_Knowledge_Base/
├── TCM_Patterns/                    # Curated, organized by hierarchy
│   └── [Hierarchical structure]
│
└── Materials/                       # Generated, organized by class/project
    ├── TCM_101/                    # Class materials
    ├── TCM_201/
    └── Research_*/                  # Research outputs
```

**Discovery works across both:**
```bash
cap list
# Shows patterns from BOTH locations
```

**Key insight:** Location indicates **purpose**, not **discoverability**
- `TCM_Patterns/` = Curated, reviewed, course-ready
- `Materials/` = Generated, working, class-specific

---

## Material Linking System

### How Materials Connect to Root Notes

Each root note can have associated materials:

```
Root Note (Heart Blood Deficiency.md)
├── Flashcards
├── Quiz
├── Slides
├── Study Material
├── Conversation Script
└── Tasks
```

### Linking Methods

#### **Method 1: File Naming Convention** (Current)

```
Materials/TCM_101/
├── Root_Note_Heart_Blood_Deficiency.md
├── Heart_Blood_Deficiency_Flashcards.md    # Pattern: {RootNote}_Flashcards.md
├── Heart_Blood_Deficiency_Quiz.md          # Pattern: {RootNote}_Quiz.md
├── Heart_Blood_Deficiency_Slides.md        # Pattern: {RootNote}_Slides.md
└── Heart_Blood_Deficiency_Study_Material.md
```

**Discovery logic:**
```python
# Find materials for "Heart Blood Deficiency"
pattern_safe = pattern.replace(" ", "_")
materials = {
    "flashcards": f"{pattern_safe}_Flashcards.md",
    "quiz": f"{pattern_safe}_Quiz.md",
    "slides": f"{pattern_safe}_Slides.md",
}
```

#### **Method 2: Metadata Linking** (Recommended)

```yaml
# In Heart_Blood_Deficiency_Flashcards.md
---
ocds_type: "flashcards"
material_id: "pattern-20251010183503"        # Links to root note
root_note: "Heart Blood Deficiency"
class_id: "TCM_101"
generated_from: "Materials/TCM_101/Root_Note_Heart_Blood_Deficiency.md"
---
```

**Benefits:**
- Works regardless of file location
- Supports multiple classes using same root
- Enables version tracking
- Allows material reuse

#### **Method 3: Folder Grouping** (Deep Research)

```
Materials/Traditional_Chinese_Medicine_Impotence/
├── Root_Note.md                    # Main content
├── Study_Material.md               # Generated from root
├── Flashcards.md                   # Generated from root
├── Quiz.md                         # Generated from root
└── Slides.md                       # Generated from root
```

**Discovery logic:**
```python
# All materials in same folder = linked
materials_dir = root_note_path.parent
flashcards = materials_dir / "Flashcards.md"
```

---

## Capsule CLI Integration

### How Commands Interact with Folders

#### `cap list` - Discovery

```bash
cap list
```

**Search behavior:**
1. Checks `config['paths.knowledge_base']/TCM_Patterns/`
2. Scans recursively for `*.md` files
3. Extracts pattern names from filenames
4. Displays organized list

**Configuration:**
```yaml
# ~/.config/capsule/config.yaml
paths:
  knowledge_base: "/path/to/TCM_Knowledge_Base"
  pattern_dirs:
    - "TCM_Patterns"
    - "Materials/TCM_Patterns"
```

---

#### `cap research` - Content Generation

```bash
cap research "Impotence" --deep
```

**Output structure:**
```
Materials/Traditional_Chinese_Medicine_Impotence/
├── Root_Note.md                    # Step 1: Research
├── Study_Material.md               # Step 2: Generate materials
├── Flashcards.md
├── Quiz.md
└── Slides.md
```

**With class ID:**
```bash
cap research "Edema" --deep --class-id TCM_101
```

**Output structure:**
```
Materials/TCM_101/
├── Root_Note_Edema.md              # Root note
├── Edema_Study_Material.md         # Materials
├── Edema_Flashcards.md
└── Edema_Quiz.md
```

---

#### `cap chat` - Interactive Learning

```bash
cap chat "Heart Blood Deficiency"
```

**File resolution:**
1. Searches `TCM_Patterns/` for `Heart Blood Deficiency.md`
2. Checks subdirectories if not found
3. Fuzzy matching if no exact match
4. Loads root note for conversation

**Material lookup:**
```python
# Finds associated materials in same directory or Materials/class_id/
flashcards = find_material(pattern, "flashcards")
quiz = find_material(pattern, "quiz")
```

---

#### `cap generate` - Material Creation

```bash
cap generate "Spleen Qi Deficiency" --class-id TCM_101
```

**Input:** Root note from `TCM_Patterns/`  
**Output:** Materials to `Materials/TCM_101/`

```
TCM_Patterns/Zang Fu Patterns/Spleen Qi Deficiency.md
                    ↓
          [Content Generator]
                    ↓
Materials/TCM_101/
├── Spleen_Qi_Deficiency_Flashcards.md
├── Spleen_Qi_Deficiency_Quiz.md
└── Spleen_Qi_Deficiency_Slides.md
```

---

## Best Practices

### For Course Creators

1. **Curate in `TCM_Patterns/`**
   - Use hierarchical folders
   - Review and polish content
   - Mark as `status: published`

2. **Generate to `Materials/{class_id}/`**
   - Keep class materials together
   - Use consistent naming
   - Link back to source root notes

3. **Use metadata consistently**
   ```yaml
   ocds_type: "root_note"
   material_id: "unique-id"
   class_id: "TCM_101"
   status: "published"
   ```

4. **Version your content**
   ```yaml
   version: "1.2.0"
   updated: 2025-11-10
   ```

---

### For Students

1. **Don't modify `TCM_Patterns/`**
   - This is the source library
   - Changes will be overwritten

2. **Work in `Materials/{class_id}/`**
   - Your generated materials
   - Safe to annotate and customize

3. **Use separate folders for personal notes**
   ```
   My_Notes/
   ├── Heart_Blood_Deficiency_Notes.md
   └── Study_Journal.md
   ```

4. **Link to root notes, don't duplicate**
   ```markdown
   See: [[TCM_Patterns/Zang Fu Patterns/Heart Blood Deficiency]]
   ```

---

### For Developers

1. **Make discovery flexible**
   - Support directory scanning
   - Support tag-based search
   - Allow configuration

2. **Use relative paths in code**
   ```python
   kb_path = Path(config.get('paths.knowledge_base'))
   patterns_dir = kb_path / "TCM_Patterns"
   ```

3. **Handle multiple locations gracefully**
   ```python
   search_paths = [
       kb_path / "TCM_Patterns",
       kb_path / "Materials",
   ]
   ```

4. **Validate with metadata**
   ```python
   if frontmatter.get("ocds_type") == "root_note":
       # This is a valid root note
   ```

---

## Migration Guide

### Migrating Existing Content

#### From Flat Structure

**Before:**
```
Materials/
├── Heart_Blood_Deficiency.md
├── Spleen_Qi_Deficiency.md
└── Lung_Yin_Deficiency.md
```

**After (Hierarchical):**
```
TCM_Patterns/
└── Zang Fu Patterns/
    ├── Heart_Patterns/
    │   └── Heart Blood Deficiency.md
    ├── Spleen_Patterns/
    │   └── Spleen Qi Deficiency.md
    └── Lung_Patterns/
        └── Lung Yin Deficiency.md
```

**After (Flat + Tags):**
```
TCM_Patterns/
├── Heart Blood Deficiency.md
├── Spleen Qi Deficiency.md
└── Lung Yin Deficiency.md
```
+ Add metadata tags:
```yaml
category: ['Zang Fu', 'Heart', 'Blood Deficiency']
```

---

#### Adding Metadata to Existing Files

**Script: `scripts/add_metadata.py`**

```python
#!/usr/bin/env python3
"""Add OCDS metadata to existing pattern files."""

import yaml
from pathlib import Path

def add_metadata(file_path: Path):
    """Add ocds_type to existing files."""
    
    # Read existing content
    content = file_path.read_text()
    
    # Parse frontmatter
    if content.startswith('---'):
        # Has frontmatter
        parts = content.split('---', 2)
        frontmatter = yaml.safe_load(parts[1])
        body = parts[2]
    else:
        # No frontmatter
        frontmatter = {}
        body = content
    
    # Add OCDS metadata
    frontmatter['ocds_type'] = 'root_note'
    frontmatter.setdefault('material_id', generate_id())
    frontmatter.setdefault('status', 'published')
    frontmatter.setdefault('source', 'curated')
    
    # Write back
    new_content = f"---\n{yaml.dump(frontmatter)}---\n{body}"
    file_path.write_text(new_content)

# Run on all patterns
patterns_dir = Path("TCM_Patterns")
for pattern_file in patterns_dir.rglob("*.md"):
    add_metadata(pattern_file)
```

---

## Configuration Reference

### Capsule Config (`~/.config/capsule/config.yaml`)

```yaml
api:
  gemini_key: "your-api-key"

paths:
  knowledge_base: "/home/user/TCM_Knowledge_Base"
  output_dir: "Materials"                    # Where to save generated content
  pattern_dirs:                              # Where to find root notes
    - "TCM_Patterns"
    - "Materials"

defaults:
  class_id: "TCM_101"                        # Default class for materials
  template: "TCM_Pattern_Template_Simple.md"
  max_attempts: 3

search:
  method: "hybrid"                           # directory | tag | hybrid
  recursive: true                            # Search subdirectories
  require_frontmatter: false                 # Only find tagged notes
  
preferences:
  theme: "dark"
  verbose: false
  save_logs: true
```

---

## Folder Permissions & Git

### What to Version Control

✅ **Include in git:**
- `TCM_Patterns/` - Curated source content
- `OCDS_Documentation/` - Documentation
- `scripts/` - Automation scripts
- `capsule/` - CLI tool
- `.obsidian/plugins/` - Plugin configs (for distribution)

❌ **Exclude from git:**
- `Materials/` - Generated content (user-specific)
- `.obsidian/workspace*.json` - User workspace state
- Personal notes and journals

### `.gitignore` Example

```gitignore
# Generated materials
Materials/

# User-specific Obsidian files
.obsidian/workspace*.json
.obsidian/graph.json

# Python
__pycache__/
*.pyc
.venv/

# OS
.DS_Store
Thumbs.db

# Logs
*.log
conversation_logs/
```

---

## Advanced Topics

### Multi-Vault Setup

For power users managing multiple knowledge bases:

```
~/Obsidian/
├── TCM_Vault/
│   ├── TCM_Patterns/
│   └── Materials/
│
├── Herbalism_Vault/
│   ├── Herb_Monographs/
│   └── Materials/
│
└── Acupuncture_Vault/
    ├── Point_Database/
    └── Materials/
```

**Capsule config:**
```yaml
# Switch between vaults
vaults:
  tcm:
    knowledge_base: "~/Obsidian/TCM_Vault"
    pattern_dirs: ["TCM_Patterns"]
  
  herbalism:
    knowledge_base: "~/Obsidian/Herbalism_Vault"
    pattern_dirs: ["Herb_Monographs"]

# Set active vault
active_vault: "tcm"
```

```bash
cap config set active_vault herbalism
cap list  # Now shows herbalism patterns
```

---

### Symbolic Links for Shared Content

Share content between vaults without duplication:

```bash
# Link shared formulas into vault
cd TCM_Knowledge_Base
ln -s ~/Shared/TCM_Formulas ./TCM_Formulas

# Now both vaults access same formulas
```

---

## Summary

### Key Takeaways

1. **Root notes** are the source of truth - everything generates from them
2. **Hybrid organization** works best - directories for structure, tags for discovery
3. **Separation of concerns** - curated content in `TCM_Patterns/`, generated in `Materials/`
4. **Metadata enables automation** - consistent frontmatter is critical
5. **Capsule CLI** provides unified interface across organization methods

### Quick Reference

| Task | Command | Input Location | Output Location |
|------|---------|----------------|-----------------|
| List patterns | `cap list` | `TCM_Patterns/` | Console |
| Research topic | `cap research "X" --deep` | API | `Materials/Project_X/` |
| Generate materials | `cap generate "X"` | `TCM_Patterns/` | `Materials/{class_id}/` |
| Start conversation | `cap chat "X"` | `TCM_Patterns/` | Interactive |
| Configure | `cap config set key value` | - | `~/.config/capsule/` |

---

## Next Steps

1. **Read:** `05_Material_Templates/` - Learn root note structure
2. **Read:** `03_Data_Standards/Frontmatter_Schema.md` - Understand metadata
3. **Try:** `cap list` - See your current patterns
4. **Organize:** Move patterns into hierarchical folders (optional)
5. **Enhance:** Add metadata to existing patterns
6. **Generate:** Create materials from root notes

---

**Related Documentation:**
- `01_System_Overview/README.md` - OCDS architecture
- `03_Data_Standards/Frontmatter_Schema.md` - Metadata reference
- `05_Material_Templates/Root_Note_Template.md` - Root note format
- `06_Automation_Scripts/Script_Overview.md` - Automation tools
- `12_Best_Practices/Content_Organization.md` - Organization tips

---

*Last updated: 2025-11-10*  
*Version: 1.0.0*
