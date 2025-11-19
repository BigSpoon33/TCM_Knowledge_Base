# Product Requirements Document
# BMM - Bio-Medically Aware Development
# Obsidian Capsule Delivery System (OCDS)

**Version:** 1.1  
**Date:** 2025-11-17
**Author:** BMad (PM Agent)  
**Project:** Obsidian_Capsule_Delivery  
**Track:** BMad Method (Brownfield)
**Reference:** [bmm-brainstorming-session-2025-11-15.md](bmm-brainstorming-session-2025-11-15.md)

---

## Vision & Purpose

### What Makes This Special

**Obsidian Capsule Delivery System** is the first **standardized educational content platform** for Obsidian that combines AI-powered content generation with universal packaging and distribution.

**The Core Innovation:** A template-driven architecture where the **capsule template** serves as the universal contract connecting:
- Manual knowledge authoring by experts
- AI-generated content from deep research
- Standardized packaging (first of its kind in Obsidian ecosystem)
- Safe cross-vault distribution with version-aware merging

**What Users Will Love:**
- **Creators**: "Research and generate a complete course in hours, not weeks"
- **Learners**: "Import expert knowledge capsules that just work in my vault"
- **Domain Experts**: "My TCM knowledge can enhance someone's cooking notes (cross-domain composability)"

### Vision Alignment

**Problem Being Solved:**

1. **For Content Creators:**
   - Creating educational materials is time-consuming and repetitive
   - No standard format for sharing Obsidian knowledge bases
   - Manual research and material synthesis is slow
   - Hard to maintain consistency across large content collections

2. **For Content Consumers:**
   - Importing external Obsidian content is risky (breaks existing notes)
   - No version management for knowledge updates
   - Can't combine knowledge from multiple sources safely
   - Missing structure for progressive learning

3. **For the Obsidian Ecosystem:**
   - No standardized packaging format (299 repos surveyed, all ad-hoc)
   - Plugin integration is fragmented
   - Knowledge sharing is manual and error-prone

**Solution:**

A unified platform with three integrated capabilities:

1. **Content Generation** (Capsule CLI + Deep Research)
   - AI-powered deep research on any topic
   - Template-driven material generation (flashcards, quizzes, slides, guided conversations)
   - Hybrid mode: User notes + AI enhancement

2. **Content Packaging** (Capsule Template System)
   - Universal frontmatter schema (works across any domain)
   - Capsule cypher (manifest defining structure, schemas, sequence)
   - Cross-domain composability (notes can belong to multiple capsules)
   - Validation and quality assurance

3. **Content Distribution** (Import/Export with Smart Merging)
   - Section-level merge (safe updates, preserves user customizations)
   - Version-aware conflict resolution
   - Dashboard integration (Master → Capsule hierarchy)
   - Plugin ecosystem compatibility (Dataview, TaskNotes, Templater, etc.)

---

## Project Classification

**Project Type:** CLI Tool + Developer Framework (Hybrid)

**Detection Signals:**
- Python-based command-line interface
- Template/schema system (developer framework)
- Scriptable automation
- Package-based distribution

**Domain Type:** Educational Technology (EdTech)

**Complexity Level:** Medium-High
- Multi-component system (CLI, templates, schemas, AI integration)
- Plugin ecosystem integration (5+ Obsidian plugins)
- AI/LLM integration (deep research, content generation)
- Cross-domain data modeling

**Field Type:** Brownfield
- Existing codebase in `capsule/` and `scripts/`
- Working TCM prototype
- 86 documentation files in OCDS_Documentation/
- Active usage and iteration

---

## Success Criteria

### What Winning Looks Like

**For v1.0 Launch:**

1. **Content Generation Success:**
   - Generate a complete 10-note capsule (root + study materials) in <30 minutes
   - Deep research produces accurate, cited content for specified topics
   - Generated materials match template schemas without manual fixes
   - Users can create custom capsule templates and generate content from them

2. **Packaging Success:**
   - Capsule validates against cypher schema (100% compliance)
   - Cross-domain notes work (one note enhanced by 2+ capsules)
   - Manual and AI-generated capsules are indistinguishable in structure

3. **Distribution Success:**
   - Import capsule into vault without breaking existing notes
   - Section-level merge works (updates without data loss)
   - Version detection prevents accidental downgrades
   - User customizations preserved through capsule updates

4. **User Love Indicators:**
   - "I created a course in hours that would've taken weeks"
   - "I can finally share my vault content safely"
   - "Multiple capsules enhanced the same notes - this is magic"

### Business/Adoption Metrics

**Primary:**
- 10 early adopters successfully create + share custom capsules
- TCM capsule exported and imported into 3+ different vaults without issues
- 80% of generated content requires zero manual correction

**Secondary:**
- Community creates 5+ domain-specific capsule templates
- OCDS becomes referenced standard in Obsidian sharing discussions
- GitHub stars/forks indicate ecosystem adoption

---

## Scope Definition

### MVP Scope (v1.0) - Must Have


**Content Generation Core:**
- Deep research integration (web search APIs, multi-source synthesis, citation tracking)
- Template-driven material generation (root notes, flashcards, quizzes, slides, guided conversations)
- Hybrid generation mode (user-provided notes + AI enhancement)
- Custom capsule template creation and management
- Validation of generated content against template schemas

**Packaging System:**
- Capsule cypher manifest (YAML format with schema definitions, file inventory, metadata)
- Universal frontmatter template (6 universal fields + domain-specific sections)
- Section-level data organization (nested YAML for domain data)
- Schema validation and compliance checking
- Cross-domain composability support (notes can belong to multiple capsules)

**Distribution & Import/Export:**
- Export capsule to distributable format (folder bundle or .capsule zip)
- Import capsule with preview and safety checks
- Section-level merge strategy (same capsule updates preserve user data)
- Additive merge strategy (different capsules enhance notes without conflicts)
- Conflict detection with user resolution prompts
- Version-aware update detection
- Backup creation before import operations

**CLI Commands (Minimum Viable Interface):**
- `capsule generate <topic> [--template=<name>]` - Create new capsule from template + research
- `capsule validate <path>` - Check capsule cypher compliance and schema validation
- `capsule export <capsule-path>` - Package capsule for distribution
- `capsule import <capsule-file>` - Install capsule to vault with merge handling

**Essential Infrastructure:**
- Python-frontmatter library integration (note manipulation)
- Ruamel.yaml library integration (cypher file handling)
- Template system (Jinja2 or similar for material generation)
- File system utilities (safe file operations, backup management)

### Growth Features (v1.5 - v2.0)

**Enhanced Automation:**
- Dashboard auto-generation from cypher
- Timeline auto-scheduling via TaskNotes integration
- Batch capsule operations (update all, validate all)

**Discovery & Sharing:**
- Capsule registry/marketplace (community sharing)
- Capsule search and discovery
- Template marketplace (community templates)
- Update notifications for installed capsules

**Advanced Merging:**
- Field-level merge strategies
- Smart conflict resolution (ML-based suggestions)
- Merge preview with diff visualization

### Vision Features (v3.0+)

**Platform Expansion:**
- Obsidian plugin version (GUI interface)
- Web-based capsule browser
- Mobile app integration

**Collaboration:**
- Real-time multi-author capsule editing
- Version control integration (git-based)
- Team capsule management

**Intelligence & Analytics:**
- Capsule usage analytics
- Learning progress tracking
- AI tutoring via guided conversations
- Adaptive content difficulty

**Gamification Layer:**
- Achievement system
- Learning streaks and rewards
- Community challenges
- Leaderboards for course completion

---

## Domain-Specific Considerations

### Educational Technology Requirements

**Content Quality:**
- Generated materials must be factually accurate (citation verification)
- Learning progression must be pedagogically sound
- Assessment materials (quizzes) need answer validation
- Accessibility considerations for diverse learners

**Content Licensing:**
- Clear attribution for AI-generated content
- Citation preservation through capsule lifecycle
- License declaration in capsule cypher
- Respect for source material copyright

**Data Privacy:**
- Local-first architecture (no cloud dependency for core features)
- User data stays in vault (import/export is user-controlled)
- No telemetry without explicit user consent

### Integration Requirements

**Obsidian Plugin Ecosystem:**
- Dataview queries must work with capsule frontmatter
- TaskNotes compatibility for scheduled content
- Templater integration for dynamic content
- Spaced Repetition support for flashcards
- Advanced Slides compatibility for presentations

**File Format Constraints:**
- Pure markdown (no proprietary formats)
- UTF-8 encoding (support international characters, e.g., Chinese for TCM)
- Cross-platform compatibility (Windows, Mac, Linux)
- Git-friendly (text-based, diff-able)

---

## Functional Requirements

### FR Group 1: Content Generation

**FR1:** Users can initiate deep research on any topic via CLI command  
**FR2:** System synthesizes information from multiple web sources into coherent content  
**FR3:** System generates citations and references for all researched information  
**FR4:** Users can specify which study materials to generate (flashcards, quizzes, slides, guided conversations)  
**FR5:** System generates content compliant with specified capsule template schema  
**FR6:** Users can provide existing notes for AI enhancement (hybrid mode)  
**FR7:** System validates generated content against template requirements before saving  
**FR8:** Users can create custom capsule templates with domain-specific schemas  
**FR9:** System generates root notes with universal frontmatter + domain-specific sections  
**FR10:** System generates study materials (flashcards, quizzes, slides) matching template structure  

### FR Group 2: Template Management

**FR11:** Users can define capsule templates with custom frontmatter schemas  
**FR12:** Users can specify required vs optional frontmatter sections in templates  
**FR13:** Users can define data types for frontmatter fields (string, array, number, etc.)  
**FR14:** System validates user-created templates for structural correctness  
**FR15:** Users can share capsule templates as standalone files  
**FR16:** System provides default templates for common domains (education, reference, courses)  

### FR Group 3: Capsule Packaging

**FR17:** System generates capsule cypher (manifest) for every capsule  
**FR18:** Capsule cypher declares capsule identity (ID, name, version)  
**FR19:** Capsule cypher specifies folder structure and file inventory  
**FR20:** Capsule cypher defines domain-specific data schemas  
**FR21:** Capsule cypher declares sequence mode (freeform, sequenced, hybrid)  
**FR22:** Capsule cypher lists required and recommended Obsidian plugins  
**FR23:** System validates all capsule files against cypher specifications  
**FR24:** Users can package capsules as folder bundles or .capsule zip files  
**FR25:** System includes capsule dashboard template in package  

### FR Group 4: Import/Export Operations

**FR26:** Users can export capsules to distributable format via CLI  
**FR27:** Users can import capsules from .capsule files or folder paths  
**FR28:** System displays import preview showing files to be added/modified  
**FR29:** System creates backup of vault before import operations  
**FR30:** System detects version conflicts (importing older version over newer)  
**FR31:** Users can review and approve/reject imports after preview  

### FR Group 5: Merge Strategies

**FR32:** System performs section-level merge for same-capsule updates  
**FR33:** System performs additive merge when different capsules enhance same note  
**FR34:** System preserves user content outside frontmatter during merges  
**FR35:** System detects frontmatter section conflicts from different capsules  
**FR36:** Users receive conflict resolution prompts with merge options  
**FR37:** System tracks capsule provenance via source_capsules frontmatter field  
**FR38:** System updates version information in frontmatter during updates  

### FR Group 6: Validation & Quality

**FR39:** Users can validate capsule structure and compliance via CLI  
**FR40:** System validates frontmatter against capsule cypher schemas  
**FR41:** System validates file inventory matches cypher manifest  
**FR42:** System validates required frontmatter fields are present  
**FR43:** System validates data types match schema specifications  
**FR44:** System reports validation errors with specific file and field references  
**FR45:** System validates UTF-8 encoding for international character support  

### FR Group 7: Cross-Domain Composability

**FR46:** Notes can belong to multiple capsules simultaneously  
**FR47:** Notes can have multiple domain-specific data sections in frontmatter  
**FR48:** System tracks which capsules have contributed to each note  
**FR49:** Users can query notes by capsule membership via Dataview  
**FR50:** System prevents data section conflicts when different capsules define same section  

### FR Group 8: CLI Interface

**FR51:** Users can generate capsules via `capsule generate` command  
**FR52:** Users can validate capsules via `capsule validate` command  
**FR53:** Users can export capsules via `capsule export` command  
**FR54:** Users can import capsules via `capsule import` command  
**FR55:** CLI provides progress indicators for long-running operations  
**FR56:** CLI provides clear error messages with actionable guidance  
**FR57:** Users can access help documentation via `capsule --help`  
**FR58:** CLI supports dry-run mode for preview without execution  

### FR Group 9: Dashboard Integration

**FR59:** Each capsule includes a dashboard template for navigation  
**FR60:** Capsule dashboards display capsule metadata (ID, version, progress)  
**FR61:** Capsule dashboards link to master dashboard for vault-wide view  
**FR62:** Capsule dashboards use Dataview queries to aggregate capsule content  
**FR63:** Master dashboard aggregates data from all installed capsules  
**FR64:** Master dashboard displays active timelines for sequenced capsules  
**FR65:** Master dashboard shows cross-capsule connections and shared notes  

---

## Non-Functional Requirements

### Performance Requirements

**NFR1:** Capsule generation completes in <30 minutes for 10-note capsules  
**NFR2:** Deep research phase completes in <10 minutes per topic  
**NFR3:** Import operations complete in <60 seconds for 100-file capsules  
**NFR4:** Validation operations complete in <5 seconds for typical capsules  
**NFR5:** Merge operations handle conflicts in <30 seconds with user prompts  
**NFR6:** Dataview queries on capsule frontmatter remain responsive with <500 notes per capsule  

**Rationale:** Content generation is acceptable as background task; interactive operations (import, validate) must feel immediate to maintain workflow momentum.

### Security Requirements

**NFR7:** All capsule operations preserve data integrity (no data loss)  
**NFR8:** Import operations create timestamped backups before modifications  
**NFR9:** System validates capsule contents before execution (no arbitrary code execution)  
**NFR10:** System sanitizes user inputs to prevent injection attacks  
**NFR11:** System respects file permissions and ownership  
**NFR12:** Sensitive data (API keys) stored securely in user config, not in capsules  

**Rationale:** Users trust system with their knowledge bases; data loss is unacceptable. Templater plugin already allows code execution, so sandboxing is beyond scope, but input validation prevents accidental damage.

### Reliability Requirements

**NFR13:** Backup operations succeed or operation aborts (atomic backup)  
**NFR14:** Import operations are transactional (all-or-nothing, rollback on failure)  
**NFR15:** System gracefully handles network failures during deep research  
**NFR16:** System validates file integrity after write operations  
**NFR17:** System provides detailed logs for debugging failed operations  

**Rationale:** Educational content represents significant time investment; reliability is critical for user trust.

### Usability Requirements

**NFR18:** CLI commands follow standard Unix conventions (flags, arguments)  
**NFR19:** Error messages include specific problem and suggested fix  
**NFR20:** Progress indicators show percentage and estimated time remaining  
**NFR21:** Validation reports highlight specific files/fields with issues  
**NFR22:** Import previews clearly show what will change  
**NFR23:** Help documentation includes examples for each command  

**Rationale:** CLI users expect consistency with standard tools; clear feedback reduces support burden.

### Compatibility Requirements

**NFR24:** Works with Obsidian v1.0.0 and later  
**NFR25:** Compatible with Dataview plugin v0.5.0+  
**NFR26:** Compatible with TaskNotes plugin v1.0.0+  
**NFR27:** Compatible with Templater plugin v1.0.0+  
**NFR28:** Works on Windows, macOS, and Linux  
**NFR29:** Supports Python 3.8+ runtime environments  
**NFR30:** Markdown files remain valid when plugins are disabled  

**Rationale:** Cross-platform compatibility maximizes reach; graceful degradation ensures content accessibility without plugins.

### Maintainability Requirements

**NFR31:** Codebase follows PEP 8 style guidelines  
**NFR32:** All public functions include docstrings with examples  
**NFR33:** Template system uses well-documented format (Jinja2)  
**NFR34:** Capsule cypher uses standard YAML format  
**NFR35:** Version numbers follow semantic versioning (MAJOR.MINOR.PATCH)  

**Rationale:** Open-source project benefits from contributor-friendly code; standard formats ensure long-term maintainability.

---

## CLI Tool Specifications

### Command Structure

**Primary Commands:**

```bash
# Content Generation
capsule generate <topic> [options]
  --template=<name>      # Use specific capsule template
  --output=<path>        # Output directory (default: current)
  --materials=<types>    # Comma-separated: flashcards,quizzes,slides,conversations
  --hybrid=<note-path>   # Enhance existing note with AI research
  --no-research          # Skip deep research, use template only
  --dry-run              # Preview without creating files

# Template Management
capsule template create <name> [options]
  --domain=<type>        # Domain type (tcm, cooking, programming, etc.)
  --from=<existing>      # Copy from existing template
capsule template list               # Show available templates
capsule template validate <path>    # Validate template structure

# Packaging & Distribution
capsule export <capsule-path> [options]
  --format=zip           # Create .capsule zip (default)
  --format=folder        # Keep as folder bundle
  --output=<path>        # Export destination

capsule import <capsule-file> [options]
  --preview              # Show what will change (default)
  --no-backup            # Skip backup creation (not recommended)
  --auto-approve         # Skip confirmation prompts
  --merge-strategy=<strategy>  # section-level (default) | additive | manual

# Validation & Maintenance
capsule validate <path> [options]
  --strict               # Fail on warnings
  --fix                  # Auto-fix common issues
  --report=<format>      # json | text | html

capsule status                     # Show installed capsules
capsule update <capsule-id>        # Update to latest version
capsule list                       # List all capsules in vault
```

### Configuration

**Config File Location:** `~/.capsule/config.yaml`

```yaml
# User Configuration
user:
  name: "BMad"
  email: "user@example.com"
  vault_path: "/path/to/obsidian/vault"

# Deep Research Settings
research:
  api_key: "YOUR_API_KEY"  # For web search
  max_sources: 10
  citation_style: "APA"    # APA, MLA, Chicago
  timeout_seconds: 300

# Generation Settings
generation:
  default_template: "education"
  ai_model: "gpt-4"
  temperature: 0.7
  max_tokens: 2000

# Import/Export Settings
import:
  auto_backup: true
  backup_location: "~/.capsule/backups"
  default_merge_strategy: "section-level"
  max_backup_age_days: 30

# Plugin Integration
plugins:
  dataview_enabled: true
  tasknotes_enabled: true
  templater_enabled: true
```

### Output Formats

**Progress Indicators:**
```
Generating capsule: TCM Herbs Fundamentals
├─ [████████░░] 80% Deep research (8/10 sources processed)
├─ [██████████] 100% Root notes generation (5/5 complete)
├─ [████░░░░░░] 40% Study materials (2/5 complete)
│  ├─ [██████████] Flashcards (24 cards created)
│  ├─ [██████████] Quizzes (3 quizzes created)
│  ├─ [░░░░░░░░░░] Slides (pending)
│  ├─ [░░░░░░░░░░] Guided conversations (pending)
└─ Estimated time remaining: 8 minutes
```

**Validation Reports:**
```
Capsule Validation Report: TCM_Herbs_v1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Capsule cypher structure valid
✓ All required fields present
✓ Version format correct (1.0.0)

Files: 45/45 validated
├─ ✓ 40 files passed all checks
├─ ⚠ 3 files have warnings
└─ ✗ 2 files have errors

ERRORS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 root_notes/Dang_Gui.md
  ✗ Missing required field: herb_data.temperature
  ✗ Invalid data type: herb_data.dosage (expected string, got number)

📄 study_materials/flashcards/week1.md
  ✗ Frontmatter section 'flashcard_data' not defined in cypher schema

WARNINGS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 root_notes/Ai_Ye.md
  ⚠ Recommended field missing: herb_data.contraindications
  ⚠ Field 'aliases' is empty

Summary: 2 errors, 3 warnings
Run with --fix to attempt automatic repairs
```

**Import Preview:**
```
Import Preview: TCM_Herbs_v1.0.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 Capsule Info:
  Name: TCM Materia Medica - Herbs
  Version: 1.0.0
  Author: BMad
  Files: 45 total

📊 Impact Analysis:
  ✨ 40 new files (will be created)
  📝 3 files will be updated
  ⚠️ 2 potential conflicts detected
  💾 Backup will be created: ~/.capsule/backups/vault_2025-11-15_14-30-22

NEW FILES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📁 TCM_Herbs_v1/
  ├─ capsule-cypher.yaml
  ├─ capsule-dashboard.md
  ├─ root_notes/ (38 files)
  └─ study_materials/ (5 files)

UPDATES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 existing_notes/Ginger.md
  Strategy: Additive merge (different capsule)
  Changes: Will add 'herb_data' section
  Your content: Preserved

📄 existing_notes/Cinnamon.md
  Strategy: Additive merge (different capsule)
  Changes: Will add 'herb_data' section
  Your content: Preserved

CONFLICTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 existing_notes/Turmeric.md
  ⚠️ Conflict: Both capsules define 'herb_data' section
  Current source: Culinary_Herbs_v1
  New source: TCM_Herbs_v1
  
  Options:
  [k] Keep current (Culinary_Herbs_v1)
  [r] Replace with new (TCM_Herbs_v1)
  [m] Merge both (rename to herb_data_culinary and herb_data_tcm)
  [s] Skip this file

Continue with import? [y/N]:
```

### Error Handling

**Error Categories:**

```python
# Exit Codes
EXIT_SUCCESS = 0
EXIT_VALIDATION_ERROR = 1
EXIT_FILE_ERROR = 2
EXIT_NETWORK_ERROR = 3
EXIT_USER_CANCELLED = 4
EXIT_CONFIG_ERROR = 5
```

**Example Error Messages:**

```bash
# Clear problem statement + actionable fix
❌ Error: Capsule validation failed

Problem: Missing required field in capsule cypher
  File: capsule-cypher.yaml
  Field: data_schemas.herb_data

Fix: Add the 'herb_data' schema definition to your cypher file:

  data_schemas:
    herb_data:
      hanzi: string
      pinyin: string
      temperature: string

For template examples, run: capsule template list
```

### Installation & Setup

**Installation:**
```bash
# Via pip
pip install obsidian-capsule-cli

# Via git (development)
git clone https://github.com/user/obsidian-capsule-delivery
cd obsidian-capsule-delivery
pip install -e .

# Verify installation
capsule --version
```

**First-Time Setup:**
```bash
# Initialize configuration
capsule init

# Interactive setup wizard
? Vault path: /Users/bmad/Documents/Obsidian
? Research API key: ******************
? Default template: education
? Enable auto-backup: Yes

✓ Configuration saved to ~/.capsule/config.yaml
✓ Default templates installed
✓ Ready to create capsules!

Try: capsule generate "Introduction to Python"
```

---

## Project-Specific Deep Dive

### CLI Tool Architecture

**Core Components:**

1. **Command Parser** (`cli.py`)
   - Argument parsing and validation
   - Command routing
   - Help documentation

2. **Content Generator** (`commands/generate.py`)
   - Deep research orchestration
   - Template rendering
   - Material synthesis

3. **Template Engine** (`utils/templates.py`)
   - Template loading and validation
   - Schema enforcement
   - Jinja2 integration

4. **Import/Export Manager** (`commands/import_export.py`)
   - Capsule packaging
   - File extraction
   - Backup management

5. **Merge Controller** (`utils/merge.py`)
   - Frontmatter parsing
   - Conflict detection
   - Strategy execution

6. **Validation Engine** (`utils/validator.py`)
   - Schema validation
   - File integrity checks
   - Report generation

**Data Flow:**

```
User Command
    ↓
CLI Parser
    ↓
Command Handler
    ├─→ Generator → Deep Research → Template Render → Write Files
    ├─→ Validator → Load Cypher → Check Files → Report
    ├─→ Exporter → Gather Files → Create Archive → Save
    └─→ Importer → Extract → Preview → Backup → Merge → Commit
```

### Integration Points

**Obsidian Plugin Integration:**

```yaml
# How capsules work with plugins

Dataview:
  - Reads universal frontmatter fields (id, name, type, tags)
  - Reads domain-specific sections (herb_data, pattern_data, etc.)
  - Aggregates across capsules via source_capsules field
  - Example query: LIST WHERE contains(source_capsules, "TCM_v1")

TaskNotes:
  - Reads timeline from capsule cypher (if sequenced mode)
  - Creates tasks with scheduled dates
  - Links tasks to capsule materials
  - Note: Tasks generated at import time, not dynamically

Templater:
  - Used to pre-generate dashboard templates
  - Populates variables from cypher at import
  - Creates dynamic links between notes
  - Note: Executes once at import, not on-demand

Spaced Repetition:
  - Reads flashcard files from study_material folder
  - Applies scheduling algorithm
  - Stores scheduling data in separate frontmatter fields
  - Note: SR data kept separate from capsule data

Advanced Slides:
  - Reads slide files with special frontmatter
  - Applies reveal.js configuration
  - Presents slide decks
  - Note: Slide structure defined in capsule template
```

### Deep Research Workflow

**Research Pipeline:**

```
1. Topic Analysis
   ├─ Parse user topic/query
   ├─ Extract key concepts
   └─ Generate search queries

2. Source Discovery
   ├─ Execute web searches (API)
   ├─ Rank by relevance
   └─ Fetch top N sources

3. Content Extraction
   ├─ Parse HTML/text
   ├─ Extract key information
   └─ Filter noise/ads

4. Synthesis
   ├─ Combine multiple sources
   ├─ Resolve conflicts
   ├─ Generate coherent narrative
   └─ Create citations

5. Template Population
   ├─ Match content to template structure
   ├─ Fill frontmatter fields
   ├─ Generate markdown body
   └─ Create study materials
```

**Citation Management:**

```yaml
# Citations stored in capsule
citations:
  - id: "source-1"
    title: "Traditional Chinese Medicine: An Introduction"
    author: "Zhang, Wei"
    url: "https://example.com/tcm-intro"
    accessed: "2025-11-15"
    cited_in: ["Ai_Ye.md", "Dang_Gui.md"]
  
  - id: "source-2"
    title: "Herbal Medicine Research Database"
    author: "WHO"
    url: "https://who.int/herbs"
    accessed: "2025-11-15"
    cited_in: ["herb_properties.md"]
```

---

## Summary & Next Steps

### PRD Summary

**What We're Building:**

Obsidian Capsule Delivery System (OCDS) - A CLI-based platform that revolutionizes educational content creation and sharing in Obsidian through:

1. **AI-Powered Generation** - Create complete learning capsules with deep research in <30 minutes
2. **Universal Packaging** - First standardized format for Obsidian content sharing
3. **Safe Distribution** - Version-aware imports with smart merging that preserves user data

**Core Value Proposition:**

*"From research to distributed learning materials in hours, not weeks - with the safety and structure the Obsidian community has been missing."*

**Requirements Count:**
- **65 Functional Requirements** across 9 capability groups
- **35 Non-Functional Requirements** covering performance, security, reliability, usability, compatibility, maintainability

**Project Scope:**
- **v1.0 (MVP):** Complete CLI with generation, packaging, distribution
- **v1.5-2.0 (Growth):** Enhanced automation, marketplace, advanced merging
- **v3.0+ (Vision):** Plugin GUI, collaboration, analytics, gamification

### Technical Foundation

**Built On:**
- Python 3.8+ CLI framework
- python-frontmatter (note manipulation)
- ruamel.yaml (cypher handling)
- Jinja2 (template rendering)
- Deep research integration (web APIs)

**Integrates With:**
- Obsidian v1.0.0+
- Dataview, TaskNotes, Templater, Spaced Repetition, Advanced Slides plugins
- Cross-platform (Windows, macOS, Linux)

### What Makes This Special

The **capsule template** is the universal contract that:
- Enables AI to generate structured content
- Allows manual authoring with consistency
- Ensures safe cross-vault distribution
- Supports cross-domain knowledge composability

This is the **first time** in the Obsidian ecosystem that content generation, packaging, and distribution work together seamlessly.

---

## Next Workflows

**Immediate Next Steps (Required):**

1. **UX Design** (Conditional - for dashboard templates)
   - Design capsule dashboard layout
   - Design master dashboard layout
   - Define Dataview query patterns
   
2. **Architecture** (Recommended - especially for brownfield)
   - Technical architecture decisions
   - Component design
   - Integration patterns
   - Data models

3. **Epic Breakdown** (Required)
   - Decompose 65 FRs into implementable stories
   - Sequence development work
   - Estimate effort

**Recommended Workflow Order:**

```
✓ Brainstorm (Complete)
✓ Research (Complete)
✓ PRD (Complete) ← YOU ARE HERE

→ UX Design (if dashboard UI needs detailed design)
→ Architecture (strongly recommended for integration complexity)
→ Epic Breakdown (required before implementation)
→ Sprint Planning (required before coding)
```

---

**Document Status:** ✅ Complete and ready for review

**Created:** 2025-11-17
**Last Updated:** 2025-11-17
**Next Review:** Before architecture phase
