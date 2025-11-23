# Architecture Document
# Obsidian Capsule Delivery System (OCDS)

**Version:** 1.0  
**Date:** 2025-11-15  
**Architect:** BMad (Architect Agent)  
**Project:** Obsidian_Capsule_Delivery  
**Track:** BMad Method (Brownfield)

---

## Executive Summary

The Obsidian Capsule Delivery System architecture is built on a **template-driven Python CLI framework** that ensures consistency across AI-generated content, manual authoring, and distribution workflows. The architecture uses **Typer** for modern CLI handling with type safety, **python-frontmatter** and **ruamel.yaml** for safe YAML manipulation, and **Jinja2** for template rendering. The system implements a **section-level merge strategy** for safe capsule imports and a **universal frontmatter schema** that enables cross-domain composability while maintaining data integrity through transactional operations.

---

## Project Initialization

**First Implementation Story: Project Scaffolding**

```bash
# Initialize modern Python project structure
pip install cookiecutter
cookiecutter gh:audreyfeldroy/cookiecutter-pypackage

# Project name: obsidian-capsule-cli
# Package name: capsule
# Author: BMad
# Python version: 3.8+

# Install core dependencies
pip install typer[all] python-frontmatter ruamel.yaml jinja2 pyyaml

# Install development dependencies
pip install pytest pytest-cov black flake8 mypy
```

**This establishes:**
- ✅ Modern Python package structure (pyproject.toml, src layout)
- ✅ CLI framework (Typer with rich output formatting)
- ✅ Testing infrastructure (pytest with coverage)
- ✅ Code quality tools (black, flake8, mypy)
- ✅ Documentation structure (Sphinx)
- ✅ Version management (semantic versioning)

---

## Decision Summary Table

| Category | Decision | Version/Choice | Rationale | Affects Epics | Provided By |
|----------|----------|----------------|-----------|---------------|-------------|
| **CLI Framework** | Typer | 0.9.0+ | Type-safe, modern, includes rich formatting | All CLI commands | Choice |
| **Project Structure** | Cookiecutter PyPackage | Latest | Professional structure, testing, docs | All | Starter |
| **YAML Manipulation** | python-frontmatter | 1.0.0+ | Safe frontmatter parsing, production-stable | Import/Export, Merge | Research |
| **YAML Cypher Handling** | ruamel.yaml | 0.17.0+ | Comment preservation, roundtrip safety | Template Management, Validation | Research |
| **Template Engine** | Jinja2 | 3.1.0+ | Industry standard, powerful, well-documented | Content Generation | PRD |
| **Testing Framework** | pytest | 7.0+ | De facto standard, fixtures, parametrization | All | Starter |
| **Code Formatting** | black | 23.0+ | Uncompromising formatter, team consistency | All | Starter |
| **Linting** | flake8 + mypy | Latest | Style + type checking | All | Starter |
| **Progress Indicators** | rich (via Typer) | 13.0+ | Beautiful CLI output, progress bars | Generation, Import/Export | Typer |
| **HTTP Requests** | requests | 2.31.0+ | Deep research API calls | Content Generation | Choice |
| **File Operations** | pathlib + shutil | stdlib | Safe cross-platform file handling | All file operations | stdlib |
| **Backup Management** | zipfile + datetime | stdlib | Timestamped vault backups | Import operations | stdlib |
| **Configuration** | PyYAML | 6.0+ | User config parsing (~/.capsule/config.yaml) | All | Choice |
| **Version Management** | semantic versioning | 2.0.0 spec | Capsule version tracking, conflict detection | Packaging, Import/Export | Standard |

---

## Complete Project Structure

```
obsidian-capsule-delivery/
├── .github/
│   └── workflows/
│       ├── ci.yml                    # CI/CD pipeline
│       └── release.yml               # Release automation
│
├── docs/
│   ├── PRD.md                        # Product requirements
│   ├── architecture.md               # This document
│   ├── bmm-brainstorming-session-2025-11-15.md
│   ├── technical-research-capsules.md
│   ├── bmm-workflow-status.yaml      # Workflow tracking
│   └── api/                          # Sphinx API docs (generated)
│
├── capsule/                          # Main package (renamed from src/capsule)
│   ├── __init__.py
│   ├── __main__.py                   # Entry point: python -m capsule
│   ├── cli.py                        # Typer CLI app definition
│   │
│   ├── commands/                     # CLI command implementations
│   │   ├── __init__.py
│   │   ├── generate.py               # capsule generate
│   │   ├── template.py               # capsule template *
│   │   ├── export.py                 # capsule export
│   │   ├── import_cmd.py             # capsule import (avoid keyword)
│   │   ├── validate.py               # capsule validate
│   │   ├── status.py                 # capsule status/list/update
│   │   └── init.py                   # capsule init (first-time setup)
│   │
│   ├── core/                         # Core business logic
│   │   ├── __init__.py
│   │   ├── generator.py              # Content generation orchestration
│   │   ├── researcher.py             # Deep research implementation
│   │   ├── packager.py               # Capsule packaging logic
│   │   ├── importer.py               # Import logic with merge strategies
│   │   ├── exporter.py               # Export logic
│   │   ├── validator.py              # Schema validation engine
│   │   └── merger.py                 # Frontmatter merge controller
│   │
│   ├── models/                       # Data models
│   │   ├── __init__.py
│   │   ├── capsule.py                # Capsule data model
│   │   ├── cypher.py                 # CapsuleCypher model
│   │   ├── note.py                   # Note with frontmatter model
│   │   ├── template.py               # Template schema model
│   │   └── config.py                 # User config model
│   │
│   ├── templates/                    # Jinja2 templates
│   │   ├── capsule-cypher.yaml.j2    # Cypher template
│   │   ├── universal-note.md.j2      # Universal note template
│   │   ├── dashboard.md.j2           # Dashboard template
│   │   ├── master-dashboard.md.j2    # Master dashboard template
│   │   └── domains/                  # Domain-specific templates
│   │       ├── education.yaml        # Education domain schema
│   │       ├── reference.yaml        # Reference domain schema
│   │       └── tcm.yaml              # TCM domain schema (existing)
│   │
│   ├── utils/                        # Utility modules
│   │   ├── __init__.py
│   │   ├── frontmatter.py            # Frontmatter parsing utilities
│   │   ├── yaml_handler.py           # YAML read/write with ruamel
│   │   ├── file_ops.py               # Safe file operations
│   │   ├── backup.py                 # Backup creation/management
│   │   ├── progress.py               # Progress bar wrappers
│   │   └── validators.py             # Common validation functions
│   │
│   └── exceptions.py                 # Custom exceptions
│
├── tests/                            # Test suite
│   ├── __init__.py
│   ├── conftest.py                   # Pytest fixtures
│   ├── test_commands/                # Command tests
│   │   ├── test_generate.py
│   │   ├── test_import.py
│   │   ├── test_export.py
│   │   └── test_validate.py
│   ├── test_core/                    # Core logic tests
│   │   ├── test_generator.py
│   │   ├── test_merger.py
│   │   ├── test_validator.py
│   │   └── test_researcher.py
│   ├── test_models/                  # Model tests
│   │   ├── test_capsule.py
│   │   ├── test_cypher.py
│   │   └── test_note.py
│   ├── test_utils/                   # Utility tests
│   │   ├── test_frontmatter.py
│   │   ├── test_yaml_handler.py
│   │   └── test_file_ops.py
│   └── fixtures/                     # Test data
│       ├── sample_capsules/
│       ├── sample_notes/
│       └── sample_cyphers/
│
├── scripts/                          # Existing scripts (to be refactored)
│   ├── [existing scripts remain during migration]
│   └── migrate_to_new_structure.py   # Migration helper
│
├── OCDS_Documentation/               # Existing documentation (preserved)
│   └── [86 existing files preserved]
│
├── .gitignore
├── .python-version                   # pyenv version pinning
├── pyproject.toml                    # Modern Python project config
├── setup.py                          # Backward compatibility
├── setup.cfg                         # Tool configurations
├── README.md
├── CHANGELOG.md
├── LICENSE
└── requirements/                     # Dependency management
    ├── base.txt                      # Core dependencies
    ├── dev.txt                       # Development dependencies
    └── test.txt                      # Testing dependencies
```

---

## Technology Stack Details

### Core Dependencies


```python
# requirements/base.txt
typer[all]>=0.9.0        # CLI framework with rich output
python-frontmatter>=1.0.0 # Frontmatter parsing
ruamel.yaml>=0.17.0      # YAML handling with comment preservation
jinja2>=3.1.0            # Template rendering
pyyaml>=6.0              # Config file parsing
requests>=2.31.0         # HTTP for future APIs
google-generativeai>=0.3.0  # Gemini API for research

# requirements/dev.txt
pytest>=7.0
pytest-cov>=4.0
black>=23.0
flake8>=6.0
mypy>=1.0

# requirements/test.txt
pytest-mock>=3.10
```

### Deep Research Provider Architecture

**Decision:** Plugin-based provider abstraction with Gemini as v1.0 default

**Provider Interface:**
```python
class ResearchProvider(ABC):
    """Abstract base for research providers"""
    
    @abstractmethod
    def research(self, topic: str, max_sources: int = 10) -> Dict:
        """Returns: {content: str, citations: List[Citation], metadata: Dict}"""
        pass
```

**v1.0 Implementation:**
- **GeminiResearchProvider** - Uses Gemini Pro with Google Search grounding
- Built-in real-time web search (no separate search API needed)
- Automatic citation generation
- Handles FR2 (multi-source synthesis) and FR3 (citation generation)

**Future Providers (v1.5+):**
- PerplexityProvider (specialized research AI)
- OpenAI + Search API combo
- CustomLLMProvider (local LLMs like Ollama with configurable endpoints)

**Configuration:**
```yaml
research:
  provider: "gemini"  # v1.0: only gemini supported
  api_key: "YOUR_GEMINI_API_KEY"
  max_sources: 10
  enable_grounding: true  # Use real-time Google Search
  citation_style: "APA"
```

**Rationale:** Start simple with best-in-class solution (Gemini), architecture ready for future expansion without refactoring.

---

## Epic to Architecture Mapping

### Epic Group 1: Content Generation (FR1-FR10)

**Epics:**
- Deep Research Implementation
- Template-Driven Generation
- Content Validation
- Hybrid Mode (User Notes + AI Enhancement)

**Architecture Components:**
```
capsule/core/researcher.py
  └─ GeminiResearchProvider → Handles web research + synthesis
  
capsule/core/generator.py
  └─ ContentGenerator
      ├─ Uses researcher.py for deep research
      ├─ Uses Jinja2 templates for content generation
      └─ Uses validator.py for schema compliance

capsule/templates/
  └─ Jinja2 templates for all content types
      ├─ universal-note.md.j2 (root notes)
      ├─ flashcard.md.j2
      ├─ quiz.md.j2
      ├─ slide.md.j2
      └─ guided-conversation.md.j2

capsule/commands/generate.py
  └─ CLI entry point
      ├─ Parses user input
      ├─ Orchestrates generator workflow
      └─ Displays progress with rich library
```

**Data Flow:**
```
User: capsule generate "TCM Herbs"
  ↓
generate.py (CLI command)
  ↓
generator.py (ContentGenerator)
  ├─→ researcher.py → Gemini API (web research)
  ├─→ Load template from templates/
  ├─→ Render template with research data
  ├─→ validator.py (validate against schema)
  └─→ Write files to disk
  ↓
Output: Capsule folder with validated content
```

---

### Epic Group 2: Template Management (FR11-FR16)

**Epics:**
- Custom Template Creation
- Template Validation
- Domain Schema Definition
- Template Sharing

**Architecture Components:**
```
capsule/models/template.py
  └─ TemplateSchema model
      ├─ Defines frontmatter schema structure
      ├─ Validates required vs optional fields
      └─ Type checking for field definitions

capsule/commands/template.py
  └─ CLI commands
      ├─ create: Create new template
      ├─ list: Show available templates
      ├─ validate: Check template structure

capsule/templates/domains/
  └─ Pre-built domain templates
      ├─ education.yaml
      ├─ reference.yaml
      └─ tcm.yaml (existing)
```

**Template Schema Format:**
```yaml
# capsule/templates/domains/tcm.yaml
domain_type: "traditional_chinese_medicine"
version: "1.0.0"

frontmatter_schema:
  required_fields:
    - id
    - name
    - type
    - created
    - updated
  
  optional_fields:
    - tags
    - aliases
  
  domain_sections:
    herb_data:
      required:
        - hanzi: string
        - pinyin: string
        - temperature: string
      optional:
        - dosage: string
        - contraindications: array
```

---

### Epic Group 3: Capsule Packaging (FR17-FR25)

**Epics:**
- Capsule Cypher Generation
- File Inventory Management
- Schema Validation
- Export to Distributable Format

**Architecture Components:**
```
capsule/models/cypher.py
  └─ CapsuleCypher model
      ├─ Parse/validate cypher YAML
      ├─ Track file inventory
      └─ Define domain schemas

capsule/core/packager.py
  └─ Handles capsule packaging
      ├─ Generate cypher from capsule contents
      ├─ Validate all files against cypher
      ├─ Create folder structure
      └─ Create .capsule zip archive

capsule/core/validator.py
  └─ Schema validation engine
      ├─ Validate cypher structure
      ├─ Validate notes against frontmatter schemas
      ├─ Check file inventory completeness
      └─ Generate validation reports

capsule/commands/export.py
  └─ CLI export command
      ├─ Read capsule directory
      ├─ Run validation
      ├─ Package as folder or zip
      └─ Save to output location
```

**Capsule Cypher Structure (Implementation Detail):**
```yaml
# capsule-cypher.yaml (generated by packager.py)
capsule_id: "TCM_Herbs_v1"
name: "TCM Materia Medica - Herbs"
version: "1.0.0"
domain_type: "traditional_chinese_medicine"

folder_structure:
  root_notes: "root_notes/"
  study_material: "study_material/"
  resources: "resources/"

contents:
  root_notes:
    - file: "root_notes/Ai_Ye.md"
      id: "note-ai-ye-001"
    - file: "root_notes/Dang_Gui.md"
      id: "note-dang-gui-002"
  
  study_material:
    flashcards:
      - file: "study_material/flashcards/herbs-week1.md"
    quizzes:
      - file: "study_material/quizzes/herbs-quiz1.md"

data_schemas:
  herb_data:
    hanzi: string
    pinyin: string
    temperature: string
    # ... full schema definition

sequence_mode: "freeform"
required_plugins:
  - name: "dataview"
    min_version: "0.5.0"
```

---

### Epic Group 4: Import/Export Operations (FR26-FR31)

**Epics:**
- Export Capsule to Distribution Format
- Import Capsule with Preview
- Backup Management
- Version Conflict Detection

**Architecture Components:**
```
capsule/core/exporter.py
  └─ Export orchestration
      ├─ Validate capsule before export
      ├─ Create folder bundle or zip
      └─ Generate export manifest

capsule/core/importer.py
  └─ Import orchestration
      ├─ Extract .capsule archive
      ├─ Load cypher and analyze
      ├─ Preview changes (what will be added/modified)
      ├─ Detect version conflicts
      ├─ Create backup before import
      └─ Execute import with merge strategy

capsule/utils/backup.py
  └─ Backup management
      ├─ Create timestamped vault backups
      ├─ Use zipfile for compression
      └─ Manage backup retention (cleanup old backups)

capsule/commands/import_cmd.py
  └─ CLI import command
      ├─ Parse capsule file
      ├─ Show preview
      ├─ Get user approval
      └─ Execute import
```

**Import Preview Data Structure:**
```python
# Generated by importer.py for display
{
    'capsule_info': {
        'id': 'TCM_Herbs_v1',
        'version': '1.0.0',
        'file_count': 45
    },
    'impact': {
        'new_files': 40,
        'updated_files': 3,
        'conflicts': 2
    },
    'new_files': [
        'TCM_Herbs_v1/root_notes/Ai_Ye.md',
        # ...
    ],
    'updates': [
        {
            'file': 'existing_notes/Ginger.md',
            'strategy': 'additive_merge',
            'changes': 'Will add herb_data section'
        }
    ],
    'conflicts': [
        {
            'file': 'existing_notes/Turmeric.md',
            'reason': 'Both capsules define herb_data',
            'sources': ['Culinary_v1', 'TCM_v1']
        }
    ]
}
```

---

### Epic Group 5: Merge Strategies (FR32-FR38)

**Epics:**
- Section-Level Merge Implementation
- Additive Merge Implementation
- Conflict Detection
- User Customization Preservation

**Architecture Components:**
```
capsule/core/merger.py
  └─ Frontmatter merge controller
      ├─ parse_note() → Extract frontmatter + body
      ├─ section_level_merge() → Same capsule updates
      ├─ additive_merge() → Different capsule enhancement
      ├─ detect_conflicts() → Find overlapping sections
      └─ preserve_user_content() → Keep body intact

capsule/utils/frontmatter.py
  └─ Frontmatter utilities
      ├─ Uses python-frontmatter library
      ├─ Safe parsing/writing
      └─ UTF-8 encoding handling

capsule/models/note.py
  └─ Note model
      ├─ Frontmatter dict
      ├─ Body content string
      ├─ File path
      └─ Provenance tracking (source_capsules)
```

**Merge Algorithm (Critical Implementation Pattern):**

```python
def merge_notes(existing_note: Note, incoming_note: Note, capsule_id: str) -> Note:
    """
    Merge frontmatter from incoming note into existing note.
    
    Rules:
    1. Same capsule ID + newer version → UPDATE sections
    2. Different capsule ID → ADD sections (additive merge)
    3. User content (body) → ALWAYS PRESERVE
    4. Conflicts → Prompt user for resolution
    """
    
    # Parse existing note
    existing_fm = existing_note.frontmatter
    existing_body = existing_note.body
    
    # Check capsule provenance
    existing_sources = existing_fm.get('source_capsules', [])
    
    if capsule_id in existing_sources:
        # Same capsule update - section-level merge
        merged_fm = section_level_merge(existing_fm, incoming_note.frontmatter)
    else:
        # Different capsule - additive merge
        merged_fm = additive_merge(existing_fm, incoming_note.frontmatter, capsule_id)
        merged_fm['source_capsules'].append(capsule_id)
    
    # ALWAYS preserve user content
    return Note(frontmatter=merged_fm, body=existing_body, path=existing_note.path)

def section_level_merge(existing: dict, incoming: dict) -> dict:
    """Update matching sections, preserve others"""
    merged = existing.copy()
    
    for section_key, section_value in incoming.items():
        if section_key.endswith('_data'):  # Domain section
            merged[section_key] = section_value  # Replace with new version
        elif section_key in ['id', 'name', 'type', 'tags']:  # Universal fields
            merged[section_key] = section_value  # Update universal fields
        # Updated timestamp handled automatically
    
    return merged

def additive_merge(existing: dict, incoming: dict, capsule_id: str) -> dict:
    """Add new sections without overwriting existing"""
    merged = existing.copy()
    
    for section_key, section_value in incoming.items():
        if section_key.endswith('_data'):  # Domain section
            if section_key in existing:
                # CONFLICT: Both capsules define same section
                raise MergeConflict(
                    file=note.path,
                    section=section_key,
                    existing_source=existing.get('source_capsules'),
                    incoming_source=capsule_id
                )
            else:
                # Safe to add new section
                merged[section_key] = section_value
    
    return merged
```

**This algorithm ensures:**
- ✅ FR32: Section-level merge for updates
- ✅ FR33: Additive merge for multi-capsule enhancement
- ✅ FR34: User body content never touched
- ✅ FR35: Conflicts detected before writing
- ✅ FR37: Provenance tracked via source_capsules
- ✅ FR38: Version info updated correctly

---

### Epic Group 6: Validation & Quality (FR39-FR45)

**Epics:**
- Capsule Structure Validation
- Frontmatter Schema Validation
- File Inventory Validation
- UTF-8 Encoding Validation

**Architecture Components:**
```
capsule/core/validator.py
  └─ Validation engine
      ├─ validate_capsule() → Overall validation
      ├─ validate_cypher_structure()
      ├─ validate_frontmatter_against_schema()
      ├─ validate_file_inventory()
      ├─ validate_data_types()
      └─ generate_validation_report()

capsule/utils/validators.py
  └─ Common validation functions
      ├─ is_valid_semver()
      ├─ is_valid_yaml()
      ├─ is_utf8_encoded()
      └─ check_required_fields()
```

**Validation Report Format:**
```python
{
    'capsule_id': 'TCM_Herbs_v1',
    'validation_status': 'ERRORS',  # or 'WARNINGS' or 'PASSED'
    'summary': {
        'total_files': 45,
        'passed': 40,
        'warnings': 3,
        'errors': 2
    },
    'errors': [
        {
            'file': 'root_notes/Dang_Gui.md',
            'field': 'herb_data.temperature',
            'issue': 'Missing required field',
            'severity': 'ERROR'
        }
    ],
    'warnings': [
        {
            'file': 'root_notes/Ai_Ye.md',
            'field': 'herb_data.contraindications',
            'issue': 'Recommended field missing',
            'severity': 'WARNING'
        }
    ]
}
```

---

### Epic Group 7: Cross-Domain Composability (FR46-FR50)

**Epics:**
- Multi-Capsule Note Ownership
- Multiple Domain Sections Support
- Capsule Provenance Tracking
- Dataview Query Integration
- Section Conflict Prevention

**Architecture Components:**
```
capsule/models/note.py
  └─ Enhanced Note model
      ├─ source_capsules: List[str]  # Tracks all contributing capsules
      ├─ frontmatter: Dict[str, Any]  # Can have multiple *_data sections
      └─ validate_no_duplicate_sections()

capsule/core/merger.py
  └─ Cross-domain merge logic
      ├─ Detects when different capsules contribute same section
      ├─ Prevents overwriting other capsule's data
      └─ Maintains clear provenance chain
```

**Universal Frontmatter Pattern for Cross-Domain Notes:**
```yaml
---
# Universal fields (always present)
id: "note-ginger-20251115"
name: "Ginger / 生姜 (Shēng Jiāng)"
type: herb
tags: [herb, spice, tcm, culinary, medicinal]
created: 2025-11-15
updated: 2025-11-15

# Provenance (which capsules contributed to this note)
source_capsules:
  - TCM_Materia_Medica_v1
  - Culinary_Herbs_v2
  - Home_Remedies_v1

# Domain section 1 (from TCM capsule)
herb_data:
  hanzi: "生姜"
  pinyin: "Shēng Jiāng"
  temperature: warm
  taste: [acrid]
  channels: [Lung, Spleen, Stomach]
  functions:
    - releases the exterior
    - warms the middle jiao

# Domain section 2 (from Culinary capsule)
recipe_data:
  cuisine: asian
  flavor_profile: [spicy, warming, aromatic]
  common_uses: [stir_fry, tea, marinades]
  pairs_with: [garlic, soy_sauce, honey]

# Domain section 3 (from Remedies capsule)
remedy_data:
  conditions: [nausea, cold, indigestion]
  preparations: [tea, compress, tincture]
  dosage_home_use: "1-2 slices fresh"
---

# Note body content (user can add their own notes here)
Ginger is incredibly versatile...
```

**Dataview Integration Pattern:**
```markdown
<!-- In any Obsidian note, query cross-domain notes -->

# All herbs that are also culinary ingredients
```dataview
TABLE herb_data.temperature, recipe_data.cuisine
FROM "root_notes"
WHERE type = "herb" AND recipe_data
SORT name ASC
```

# Notes enhanced by multiple capsules
```dataview
LIST source_capsules
WHERE length(source_capsules) > 1
SORT length(source_capsules) DESC
```

# All TCM content in my vault
```dataview
TABLE type, tags
WHERE contains(source_capsules, "TCM")
```
```

**This architecture ensures:**
- ✅ FR46: Notes can belong to multiple capsules
- ✅ FR47: Multiple domain sections in single note
- ✅ FR48: Provenance tracked via source_capsules array
- ✅ FR49: Dataview queries work seamlessly
- ✅ FR50: Conflicts prevented by merger.py validation

---

### Epic Group 8: CLI Interface (FR51-FR58)

**Epics:**
- Command Implementation
- Progress Indicators
- Error Handling
- Help Documentation
- Dry-Run Mode

**Architecture Components:**
```
capsule/cli.py
  └─ Main Typer app
      ├─ Command registration
      ├─ Global options (--verbose, --config-path)
      └─ Version display

capsule/commands/*.py
  └─ Individual command modules
      ├─ Each command is a Typer function
      ├─ Uses rich for output formatting
      └─ Consistent error handling pattern
```

**CLI Command Structure Pattern:**
```python
# capsule/commands/generate.py
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn
from capsule.core.generator import ContentGenerator
from capsule.utils.progress import create_progress_bar

app = typer.Typer()

@app.command()
def generate(
    topic: str = typer.Argument(..., help="Topic to research and generate content about"),
    template: str = typer.Option("education", "--template", "-t", help="Template name to use"),
    output: str = typer.Option(".", "--output", "-o", help="Output directory"),
    materials: str = typer.Option("all", "--materials", "-m", help="Materials to generate: flashcards,quizzes,slides,conversations"),
    hybrid: str = typer.Option(None, "--hybrid", help="Path to existing note for AI enhancement"),
    no_research: bool = typer.Option(False, "--no-research", help="Skip deep research, use template only"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview without creating files"),
):
    """
    Generate a new capsule from research and templates.
    
    Example:
        capsule generate "Introduction to TCM Herbs" --template tcm
    """
    
    try:
        # Load config
        config = load_config()
        
        # Show what will happen
        if dry_run:
            typer.echo(f"[DRY RUN] Would generate capsule about: {topic}")
            typer.echo(f"Template: {template}")
            typer.echo(f"Output: {output}")
            return
        
        # Create generator
        generator = ContentGenerator(config)
        
        # Progress tracking with rich
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=False,
        ) as progress:
            
            # Research phase
            research_task = progress.add_task("Deep research...", total=None)
            research_data = generator.research(topic)
            progress.update(research_task, completed=True)
            
            # Generation phase
            gen_task = progress.add_task("Generating content...", total=100)
            capsule = generator.generate(
                topic=topic,
                template=template,
                research_data=research_data,
                materials=materials.split(","),
                progress_callback=lambda p: progress.update(gen_task, completed=p)
            )
            
            # Validation phase
            val_task = progress.add_task("Validating...", total=None)
            generator.validate(capsule)
            progress.update(val_task, completed=True)
        
        # Success message
        typer.secho(f"✅ Capsule generated successfully!", fg=typer.colors.GREEN)
        typer.echo(f"Location: {capsule.path}")
        typer.echo(f"Files created: {capsule.file_count}")
        
    except Exception as e:
        # Consistent error handling
        typer.secho(f"❌ Error: {str(e)}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)
```

**Error Handling Pattern (Consistent Across All Commands):**
```python
# capsule/exceptions.py

class CapsuleError(Exception):
    """Base exception for all capsule errors"""
    exit_code = 1

class ValidationError(CapsuleError):
    """Schema validation failed"""
    exit_code = 1

class FileError(CapsuleError):
    """File operation failed"""
    exit_code = 2

class NetworkError(CapsuleError):
    """Network/API error"""
    exit_code = 3

class UserCancelledError(CapsuleError):
    """User cancelled operation"""
    exit_code = 4

class ConfigError(CapsuleError):
    """Configuration error"""
    exit_code = 5

# All commands use this pattern:
def handle_error(e: Exception):
    """Consistent error display"""
    if isinstance(e, CapsuleError):
        typer.secho(f"❌ Error: {str(e)}", fg=typer.colors.RED, err=True)
        
        # Show helpful hint if available
        if hasattr(e, 'hint'):
            typer.echo(f"\n💡 Hint: {e.hint}")
        
        raise typer.Exit(code=e.exit_code)
    else:
        # Unexpected error
        typer.secho(f"❌ Unexpected error: {str(e)}", fg=typer.colors.RED, err=True)
        typer.echo("\nPlease report this issue with the full error message.")
        raise typer.Exit(code=1)
```

---

### Epic Group 9: Dashboard Integration (FR59-FR65)

**Epics:**
- Capsule Dashboard Templates
- Master Dashboard Aggregation
- Dataview Query Patterns
- Timeline Display
- Cross-Capsule Analytics

**Architecture Components:**
```
capsule/templates/dashboard.md.j2
  └─ Capsule dashboard template (Jinja2)
      ├─ Metadata display
      ├─ Dataview queries for capsule content
      └─ Links to master dashboard

capsule/templates/master-dashboard.md.j2
  └─ Master dashboard template (Jinja2)
      ├─ Aggregate queries across all capsules
      ├─ Timeline view for sequenced capsules
      └─ Cross-capsule connections
```

**Capsule Dashboard Template:**
```jinja2
{# capsule/templates/dashboard.md.j2 #}
---
type: capsule_dashboard
capsule_id: "{{ capsule.id }}"
version: "{{ capsule.version }}"
created: "{{ capsule.created | default(now()) }}"
updated: "{{ capsule.updated | default(now()) }}"

# Dashboard Metadata (optional - for filtering in master dashboard)
{% if capsule.dashboard_metadata %}
dashboard_metadata:
  class: "{{ capsule.dashboard_metadata.class | default('') }}"
  topic: "{{ capsule.dashboard_metadata.topic | default('') }}"
  category: "{{ capsule.dashboard_metadata.category | default('') }}"
  active: {{ capsule.dashboard_metadata.active | default(true) }}
{% endif %}

# Provenance Tracking
source_capsules: ["{{ capsule.id }}"]
---

# Capsule Dashboard: {{ capsule.name }}

## Overview

- **Capsule ID:** `{{ capsule.id }}`
- **Version:** {{ capsule.version }}
- **Domain:** {{ capsule.domain_type }}
- **Sequence Mode:** {{ capsule.sequence_mode }}

**Quick Links:**
- [[Master Dashboard|← Back to All Capsules]]
- Total Root Notes: `$= dv.pages().where(p => p.source_capsules?.includes("{{ capsule.id }}") && p.type != "dashboard").length`
- Total Study Materials: `$= dv.pages('"study_material"').where(p => p.source_capsules?.includes("{{ capsule.id }}")).length`

---

## Root Notes

```dataview
TABLE type, tags, updated
FROM ""
WHERE contains(source_capsules, "{{ capsule.id }}")
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
WHERE contains(source_capsules, "{{ capsule.id }}")
  AND type = "flashcard"
SORT file.name ASC
```

### Quizzes
```dataview
TABLE quiz_data.difficulty, quiz_data.topic
FROM ""
WHERE contains(source_capsules, "{{ capsule.id }}")
  AND type = "quiz"
SORT file.name ASC
```

---

{% if capsule.sequence_mode == "sequenced" %}
## Active Timeline

```dataview
TASK
WHERE contains(source_capsules, "{{ capsule.id }}")
  AND !completed
SORT due ASC
LIMIT 10
```
{% endif %}

---

## Recent Activity

```dataview
TABLE type, updated
FROM ""
WHERE contains(source_capsules, "{{ capsule.id }}")
SORT updated DESC
LIMIT 10
```

---

## Domain-Specific Sections
{# Custom sections added here based on domain template #}
{{ domain_sections }}
```

**Master Dashboard Template:**
```jinja2
{# capsule/templates/master-dashboard.md.j2 #}
---
type: master_dashboard
title: "My Knowledge System"
---

# Master Dashboard - My Knowledge System

## 📚 Installed Capsules

```dataview
TABLE 
  capsule_id as "ID",
  version as "Version",
  domain_type as "Domain",
  sequence_mode as "Mode"
FROM ""
WHERE type = "capsule_dashboard"
SORT file.name ASC
```

---

## 📊 Progress Overview

```dataviewjs
// Calculate aggregate progress across all capsules
const capsules = dv.pages('"capsule_dashboard"');
let totalNotes = 0;
let totalStudyMaterials = 0;

for (let capsule of capsules) {
    totalNotes += dv.pages()
        .where(p => p.source_capsules?.includes(capsule.capsule_id))
        .where(p => p.type != "dashboard")
        .length;
    
    totalStudyMaterials += dv.pages()
        .where(p => p.source_capsules?.includes(capsule.capsule_id))
        .where(p => ["flashcard", "quiz", "slide"].includes(p.type))
        .length;
}

dv.paragraph(`
**Total Notes:** ${totalNotes}
**Total Study Materials:** ${totalStudyMaterials}
**Capsules Installed:** ${capsules.length}
`);
```

---

## 🗓️ Active Timelines (Sequenced Capsules)

```dataview
TASK
WHERE !completed
  AND source_capsules
SORT due ASC
LIMIT 20
```

---

## 🔗 Cross-Capsule Connections

### Notes Enhanced by Multiple Capsules
```dataview
TABLE 
  source_capsules as "Contributing Capsules",
  type as "Type",
  tags
FROM ""
WHERE source_capsules
  AND length(source_capsules) > 1
SORT length(source_capsules) DESC
LIMIT 20
```

---

## 📈 This Week's Activity

```dataview
TABLE type, file.mtime as "Last Updated"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
  AND source_capsules
SORT file.mtime DESC
LIMIT 30
```

---

## 🎯 Capsule Directories

{% for capsule in capsules %}
- [[{{ capsule.dashboard_file }}|{{ capsule.name }}]] ({{ capsule.sequence_mode }})
{% endfor %}
```

**Dashboard Generation During Import:**
```python
# In capsule/core/importer.py

def generate_dashboard(capsule: Capsule, vault_path: Path):
    """Generate dashboard from template during import"""
    
    # Load template
    env = Environment(loader=FileSystemLoader('capsule/templates'))
    template = env.get_template('dashboard.md.j2')
    
    # Render with capsule data
    dashboard_content = template.render(
        capsule=capsule,
        domain_sections=load_domain_sections(capsule.domain_type)
    )
    
    # Write to vault
    dashboard_path = vault_path / capsule.id / "capsule-dashboard.md"
    dashboard_path.write_text(dashboard_content, encoding='utf-8')
    
    return dashboard_path
```

**Capsule Dashboard Metadata Schema:**

The dashboard frontmatter schema provides a standardized set of metadata fields that enable filtering, querying, and managing capsules in the master dashboard. This schema was defined in Story 11-1 to support the dashboard functionality outlined in Epic 11.

**Schema Definition:**

| Field | Type | Required | Default | Purpose | Queryable by Dataview |
|-------|------|----------|---------|---------|----------------------|
| `type` | string | Yes | N/A | Identifies note as capsule dashboard (`"capsule_dashboard"`) | ✅ Yes |
| `capsule_id` | string | Yes | N/A | Unique capsule identifier linking dashboard to capsule | ✅ Yes |
| `version` | string | Yes | N/A | Capsule version (semver format) | ✅ Yes |
| `created` | string (ISO 8601) | No | Import timestamp | Dashboard creation timestamp | ✅ Yes |
| `updated` | string (ISO 8601) | No | Import timestamp | Dashboard last update timestamp | ✅ Yes |
| `dashboard_metadata.class` | string | No | `null` | Class/course identifier (e.g., "TCM101", "Advanced-Herbology") | ✅ Yes |
| `dashboard_metadata.topic` | string | No | `null` | Topic description (e.g., "Herbal Medicine", "Point Location") | ✅ Yes |
| `dashboard_metadata.category` | string | No | `null` | Category/certification (e.g., "CALE", "NCCAOM", "General") | ✅ Yes |
| `dashboard_metadata.active` | boolean | No | `true` | Active study status flag | ✅ Yes |
| `source_capsules` | array[string] | No | `[capsule_id]` | List of contributing capsule IDs (provenance tracking) | ✅ Yes |

**Field Descriptions:**

**Required Fields:**
- **`type`**: Always set to `"capsule_dashboard"` to distinguish dashboard notes from regular notes. This enables Dataview queries to filter for dashboards specifically.
  
- **`capsule_id`**: The unique identifier for the capsule (e.g., `"TCM_Herbs_v1"`). This field links the dashboard to its capsule and is used in queries to filter capsule-specific content.
  
- **`version`**: Capsule version in semantic versioning format (e.g., `"1.0.0"`). Used for version tracking and update detection.

**Optional Filterable Metadata Fields:**

These fields enable powerful filtering and organization in the master dashboard:

- **`dashboard_metadata.class`**: Course or class identifier. Use cases:
  - Filtering capsules by academic course (e.g., show all "TCM101" capsules)
  - Grouping study materials by class level
  - Example values: `"TCM101"`, `"Advanced-Herbology"`, `"Point-Location-Certification"`

- **`dashboard_metadata.topic`**: Descriptive topic or subject matter. Use cases:
  - Topic-based filtering (e.g., show all "Herbal Medicine" capsules)
  - Cross-capsule topic aggregation
  - Example values: `"Herbal Medicine"`, `"Acupuncture Points"`, `"Diagnostic Methods"`

- **`dashboard_metadata.category`**: Certification, exam, or organizational category. Use cases:
  - Filtering by certification track (e.g., "CALE" vs "NCCAOM")
  - Exam preparation grouping
  - Example values: `"CALE"`, `"NCCAOM"`, `"General"`, `"Board-Exam"`

- **`dashboard_metadata.active`**: Boolean flag indicating whether the capsule is currently being studied. Use cases:
  - Show only active capsules in master dashboard
  - Archive completed/inactive capsules
  - Progress tracking focus
  - Example values: `true`, `false`

**Complete Example:**

```yaml
---
# Universal Dashboard Fields (Required)
type: capsule_dashboard
capsule_id: "TCM_Herbs_v1"
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
source_capsules: ["TCM_Herbs_v1"]
---
```

**Schema Validation:**

The schema supports the following Dataview query patterns (validated in Story 11-0 technical spike):

**Filter by active status:**
```dataview
TABLE capsule_id, dashboard_metadata.topic
FROM ""
WHERE type = "capsule_dashboard"
  AND dashboard_metadata.active = true
SORT file.name ASC
```

**Filter by class and topic:**
```dataview
TABLE capsule_id, version, dashboard_metadata.category
FROM ""
WHERE type = "capsule_dashboard"
  AND dashboard_metadata.class = "TCM101"
  AND dashboard_metadata.topic = "Herbal Medicine"
```

**Filter by category:**
```dataview
TABLE capsule_id, dashboard_metadata.class, dashboard_metadata.topic
FROM ""
WHERE type = "capsule_dashboard"
  AND dashboard_metadata.category = "CALE"
  AND dashboard_metadata.active = true
```

**Complex filtering with DataviewJS:**
```dataviewjs
const capsules = dv.pages('"capsules"')
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
  ["Capsule ID", "Class", "Category", "Installed"],
  filtered.map(p => [
    p.capsule_id,
    p.dashboard_metadata?.class,
    p.dashboard_metadata?.category,
    p.file.ctime
  ])
);
```

**Design Rationale:**

1. **Nested `dashboard_metadata` object**: Groups filterable fields together to distinguish them from universal capsule fields. This prevents namespace pollution and makes it clear which fields are for filtering vs. core identification.

2. **All metadata fields optional**: Allows simple capsules without categorization to work without modification. Core dashboard functionality (navigation, file lists) doesn't depend on metadata.

3. **String types for class/topic/category**: Provides maximum flexibility for user-defined categorization schemes. No enum constraints.

4. **Boolean `active` field**: Simple true/false is more intuitive than status strings for filtering.

5. **ISO 8601 timestamps**: Standard format for `created` and `updated` fields ensures consistency with universal frontmatter schema.

**Schema Evolution:**

Future enhancements may add:
- `dashboard_metadata.tags` (array[string]): Freeform tags for additional filtering
- `dashboard_metadata.priority` (number): Numeric priority for sorting
- `dashboard_metadata.difficulty` (string): Difficulty level indicator
- Custom domain-specific metadata fields (e.g., `tcm_metadata.pattern_category`)

These can be added without breaking existing dashboards due to the optional nature of the `dashboard_metadata` section.

**References:**
- PoC validation: `docs/sprint-artifacts/11-0-dataview-spike-poc.md` (lines 583-651)
- Technical specification: `docs/sprint-artifacts/tech-spec-epic-11.md`
- Universal frontmatter schema: See "Epic Group 1: Data Models" section above

**Master Dashboard Usage Guide:**

The Master Dashboard serves as the central navigation hub for all installed capsules in your Obsidian vault. It provides powerful filtering capabilities to help you manage and organize your knowledge system.

**Location:** The Master Dashboard is automatically generated at the root of your vault as `Master Dashboard.md` during the first capsule import.

**Key Features:**

1. **View All Capsules**
   - The "Installed Capsules" section displays all capsule dashboards with their ID, version, topic, and category
   - Use this to get an overview of your entire knowledge system at a glance

2. **Filter by Active Status**
   - The "Active Capsules" section shows only capsules currently being studied (where `dashboard_metadata.active = true`)
   - Update a capsule's active status by editing its dashboard frontmatter

3. **Filter by Metadata**
   - **By Class:** Filter capsules by course/class identifier (e.g., "TCM101", "Advanced-Herbology")
     - Edit the query to change the class name: `WHERE dashboard_metadata.class = "YOUR_CLASS"`
   - **By Topic:** Filter by subject matter (e.g., "Herbal Medicine", "Point Location")
     - Edit the query to change the topic: `WHERE dashboard_metadata.topic = "YOUR_TOPIC"`
   - **By Category:** Filter by certification or category (e.g., "CALE", "NCCAOM")
     - Edit the query to change the category: `WHERE dashboard_metadata.category = "YOUR_CATEGORY"`

4. **Progress Tracking**
   - The "Progress Overview" section uses DataviewJS to calculate:
     - Total notes across all capsules
     - Total study materials (flashcards, quizzes, slides, conversations)
     - Number of installed capsules
   - This provides a quick snapshot of your knowledge system's size and scope

5. **Task Management**
   - The "Active Timelines" section shows incomplete tasks from all sequenced capsules
   - Tasks are sorted by due date (requires TaskNotes plugin for scheduling)

6. **Cross-Capsule Discovery**
   - The "Cross-Capsule Connections" section identifies notes that belong to multiple capsules
   - This helps you discover enriched notes with data from different domains
   - Example: A "Ginger" note might have both TCM herb data and culinary recipe data

7. **Recent Activity**
   - Shows notes modified in the last 7 days
   - Helps you quickly return to recently edited content

**Customization:**

You can customize the filter queries by editing the Dataview code blocks in the dashboard. Common customizations include:

- Changing filter values (class, topic, category names)
- Adjusting time ranges (e.g., change `dur(7 days)` to `dur(30 days)` for monthly activity)
- Modifying result limits (e.g., change `LIMIT 20` to show more/fewer results)
- Adding additional filters by combining WHERE clauses with AND/OR operators

**Example Combination Filter:**

```dataview
TABLE 
  capsule_id as "ID",
  dashboard_metadata.topic as "Topic"
FROM ""
WHERE type = "capsule_dashboard"
  AND dashboard_metadata.active = true
  AND (dashboard_metadata.class = "TCM101" OR dashboard_metadata.category = "CALE")
```

This shows active capsules that are either in class "TCM101" OR in category "CALE".

**Plugin Requirements:**

- **Dataview v0.5.0+** (required): Standard queries (TABLE, LIST, TASK)
- **TaskNotes v1.0.0+** (optional): Task scheduling and due dates

**Graceful Degradation:**

If Dataview plugin is not installed, the master dashboard remains readable as a Markdown document with code blocks. All queries will be visible as formatted code, and you can still navigate to capsule dashboards via the "Capsule Links" section at the bottom.


---

## Cross-Cutting Concerns

### Error Handling Strategy

**Principle:** Fail fast with clear, actionable errors

**Implementation:**
```python
# All errors inherit from CapsuleError
# All commands use try/except with handle_error()
# All validation happens BEFORE file writes
# All user-facing errors include hints

# Example:
class MissingRequiredFieldError(ValidationError):
    def __init__(self, file: str, field: str, schema: str):
        self.hint = f"Add '{field}' to the frontmatter. See schema: {schema}"
        super().__init__(f"Missing required field '{field}' in {file}")
```

**Error Recovery:**
- Import operations: Rollback on error (delete extracted files, restore backup if needed)
- Generation operations: Delete partial output on error
- Export operations: Leave original capsule untouched on error

---

### Logging Strategy

**Principle:** Structured logging for debugging, clean output for users

**Implementation:**
```python
# capsule/utils/logger.py
import logging
from pathlib import Path

def setup_logging(verbose: bool = False):
    """Configure logging based on verbosity"""
    
    level = logging.DEBUG if verbose else logging.INFO
    
    # File handler (always detailed)
    log_file = Path.home() / '.capsule' / 'logs' / 'capsule.log'
    log_file.parent.mkdir(parents=True, exist_ok=True)
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    
    # Console handler (respects verbose flag)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(logging.Formatter(
        '%(levelname)s: %(message)s'
    ))
    
    # Root logger
    logger = logging.getLogger('capsule')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Usage in commands:
logger = logging.getLogger('capsule.commands.generate')
logger.debug(f"Loaded template: {template_path}")
logger.info("Generation complete")
```

**Log Locations:**
- `~/.capsule/logs/capsule.log` - Full debug log
- `~/.capsule/logs/operations.log` - Import/export operations only
- `~/.capsule/logs/validation.log` - Validation results

---

### Date/Time Handling

**Principle:** Always use ISO 8601 format, UTC timezone

**Implementation:**
```python
from datetime import datetime, timezone

def now_iso():
    """Get current time in ISO 8601 format (UTC)"""
    return datetime.now(timezone.utc).isoformat()

# In frontmatter:
created: 2025-11-15T14:30:22Z
updated: 2025-11-15T14:30:22Z

# In backup filenames:
vault_backup_2025-11-15_14-30-22.zip

# In logs:
2025-11-15 14:30:22,123 - INFO - Import started
```

**Rationale:** ISO 8601 is sortable, unambiguous, widely supported

---

### Configuration Management

**Principle:** Sensible defaults, easy overrides, validation

**Implementation:**
```python
# capsule/models/config.py
from pathlib import Path
from typing import Optional
import yaml

class Config:
    """User configuration model"""
    
    DEFAULT_CONFIG_PATH = Path.home() / '.capsule' / 'config.yaml'
    
    def __init__(self, config_path: Optional[Path] = None):
        self.path = config_path or self.DEFAULT_CONFIG_PATH
        self.data = self.load()
    
    def load(self) -> dict:
        """Load config from file or create default"""
        if not self.path.exists():
            return self.create_default()
        
        with open(self.path) as f:
            return yaml.safe_load(f)
    
    def create_default(self) -> dict:
        """Create default configuration"""
        default = {
            'user': {
                'name': 'User',
                'vault_path': str(Path.home() / 'Documents' / 'Obsidian')
            },
            'research': {
                'provider': 'gemini',
                'api_key': '',
                'max_sources': 10,
                'enable_grounding': True
            },
            'generation': {
                'default_template': 'education',
                'ai_model': 'gemini-pro',
            },
            'import': {
                'auto_backup': True,
                'backup_location': str(Path.home() / '.capsule' / 'backups'),
                'default_merge_strategy': 'section-level'
            }
        }
        
        # Write default config
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, 'w') as f:
            yaml.dump(default, f, default_flow_style=False)
        
        return default
    
    def get(self, key: str, default=None):
        """Get config value with dot notation"""
        keys = key.split('.')
        value = self.data
        for k in keys:
            value = value.get(k, default)
            if value is None:
                return default
        return value
```

**Config File Initialization:**
```bash
# On first run: capsule init
? Vault path: /Users/bmad/Documents/Obsidian
? Research API key: ********************
? Default template: education
? Enable auto-backup: Yes

✓ Configuration saved to ~/.capsule/config.yaml
```

---

### Testing Strategy

**Principle:** Test contracts, not implementations

**Test Pyramid:**
```
        /\
       /  \     E2E Tests (5%)
      /----\    - Full command execution
     /      \   - Real file operations (in temp dirs)
    /--------\  
   / Integration\ Integration Tests (15%)
  /--------------\ - Component interaction
 /                \ - Mocked external APIs
/------------------\
   Unit Tests (80%)  Unit Tests
   - Pure functions
   - Model validation
   - Utility functions
```

**Test Organization:**
```python
# tests/test_core/test_merger.py
import pytest
from capsule.core.merger import section_level_merge, additive_merge
from capsule.models.note import Note

class TestSectionLevelMerge:
    """Test same-capsule update scenarios"""
    
    def test_updates_domain_section(self):
        existing = {
            'id': 'note-1',
            'source_capsules': ['TCM_v1'],
            'herb_data': {'temperature': 'warm'}
        }
        incoming = {
            'herb_data': {'temperature': 'warm', 'dosage': '3-9g'}
        }
        
        result = section_level_merge(existing, incoming)
        
        assert result['herb_data']['dosage'] == '3-9g'
        assert result['herb_data']['temperature'] == 'warm'
    
    def test_preserves_other_sections(self):
        existing = {
            'herb_data': {'temperature': 'warm'},
            'recipe_data': {'cuisine': 'asian'}
        }
        incoming = {
            'herb_data': {'temperature': 'cool'}
        }
        
        result = section_level_merge(existing, incoming)
        
        assert result['recipe_data'] == {'cuisine': 'asian'}

class TestAdditiveMerge:
    """Test cross-capsule enhancement scenarios"""
    
    def test_adds_new_section_from_different_capsule(self):
        existing = {
            'source_capsules': ['TCM_v1'],
            'herb_data': {'temperature': 'warm'}
        }
        incoming = {
            'recipe_data': {'cuisine': 'asian'}
        }
        
        result = additive_merge(existing, incoming, 'Culinary_v1')
        
        assert 'recipe_data' in result
        assert result['recipe_data']['cuisine'] == 'asian'
        assert result['herb_data'] == {'temperature': 'warm'}
    
    def test_detects_conflict_when_same_section_exists(self):
        existing = {
            'source_capsules': ['TCM_v1'],
            'herb_data': {'temperature': 'warm'}
        }
        incoming = {
            'herb_data': {'temperature': 'cool'}
        }
        
        with pytest.raises(MergeConflict) as exc:
            additive_merge(existing, incoming, 'Culinary_v1')
        
        assert 'herb_data' in str(exc.value)
```

**Fixtures for Testing:**
```python
# tests/conftest.py
import pytest
from pathlib import Path
import tempfile
import shutil

@pytest.fixture
def temp_vault():
    """Create temporary Obsidian vault for testing"""
    with tempfile.TemporaryDirectory() as tmpdir:
        vault_path = Path(tmpdir) / "test_vault"
        vault_path.mkdir()
        yield vault_path

@pytest.fixture
def sample_capsule(temp_vault):
    """Create sample capsule for testing"""
    capsule_path = temp_vault / "TCM_Test_v1"
    capsule_path.mkdir()
    
    # Create cypher
    cypher_content = """
capsule_id: "TCM_Test_v1"
name: "Test Capsule"
version: "1.0.0"
"""
    (capsule_path / "capsule-cypher.yaml").write_text(cypher_content)
    
    # Create sample note
    note_content = """---
id: test-note-1
name: Test Note
type: root_note
tags: [test]
created: 2025-11-15
updated: 2025-11-15
source_capsules: [TCM_Test_v1]

herb_data:
  temperature: warm
---

# Test Note Content
"""
    (capsule_path / "test-note.md").write_text(note_content)
    
    return capsule_path
```

---

## Implementation Patterns (Consistency Rules)

### Naming Conventions

**Files:**
- Python modules: `snake_case.py`
- Test files: `test_<module_name>.py`
- Config files: `kebab-case.yaml`
- Markdown files: `Title Case With Spaces.md` or `kebab-case.md`

**Code:**
- Classes: `PascalCase`
- Functions/methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private: `_leading_underscore`

**Frontmatter:**
- Field names: `snake_case`
- Domain sections: `<domain>_data` (e.g., `herb_data`, `recipe_data`)
- Universal fields: `id`, `name`, `type`, `tags`, `created`, `updated`, `source_capsules`

**CLI:**
- Commands: `kebab-case` (e.g., `capsule template create`)
- Flags: `--kebab-case` or `-s` (short)
- Arguments: `positional_name`

---

### File Organization Patterns

**Co-location:**
- Tests live in `tests/` mirroring source structure
- Templates live in `capsule/templates/`
- Fixtures live in `tests/fixtures/`

**Import Patterns:**
```python
# Absolute imports only
from capsule.core.generator import ContentGenerator
from capsule.models.note import Note

# Not relative imports
# from ..core.generator import ContentGenerator  # ❌ Don't do this
```

---

### Data Exchange Patterns

**API Response Format (Future APIs):**
```python
{
    "success": True,
    "data": {...},
    "meta": {
        "version": "1.0.0",
        "timestamp": "2025-11-15T14:30:22Z"
    }
}

# Or on error:
{
    "success": False,
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Missing required field",
        "details": {...}
    }
}
```

**Internal Function Returns:**
```python
# Return typed objects, not dicts
def load_capsule(path: Path) -> Capsule:
    return Capsule(...)

# Not:
def load_capsule(path: Path) -> dict:
    return {"id": ..., "name": ...}  # ❌
```

---

### Communication Patterns (Component Interaction)

**Dependency Injection:**
```python
# Good: Inject dependencies
class ContentGenerator:
    def __init__(self, researcher: ResearchProvider, validator: Validator):
        self.researcher = researcher
        self.validator = validator

# Not: Create dependencies internally
class ContentGenerator:
    def __init__(self):
        self.researcher = GeminiResearchProvider()  # ❌ Hard to test
```

**Event Communication (Future):**
```python
# For v2.0+ when adding event system
# Event naming: <noun>_<past_tense_verb>
events = [
    'capsule_generated',
    'capsule_imported',
    'note_merged',
    'validation_failed'
]
```

---

### Lifecycle Patterns

**Resource Management:**
```python
# Always use context managers
with open(file_path) as f:
    content = f.read()

# For capsule operations:
with capsule_transaction(vault_path) as txn:
    txn.import_capsule(capsule)
    txn.merge_notes()
    txn.commit()  # Auto-rollback on exception
```

**Loading States:**
```python
# Use rich progress bars consistently
with Progress() as progress:
    task = progress.add_task("Loading...", total=100)
    # ... work ...
    progress.update(task, advance=10)
```

---

## Non-Functional Requirements Handling

### Performance (NFR1-NFR6)

**NFR1: Generation <30 minutes for 10-note capsules**
- **Strategy:** Parallel research (asyncio for multiple topics)
- **Implementation:** Use `asyncio.gather()` for concurrent Gemini API calls
- **Monitoring:** Log generation time per capsule

**NFR2: Research <10 minutes per topic**
- **Strategy:** Single Gemini API call with grounding (fast)
- **Timeout:** Set 300-second timeout in config
- **Fallback:** Cache research results to avoid re-research on retry

**NFR3: Import <60 seconds for 100-file capsules**
- **Strategy:** Batch file operations, avoid one-by-one writes
- **Implementation:** Collect all file operations, execute in bulk
- **Optimization:** Use `shutil.copy2()` for fast file copying

**NFR4: Validation <5 seconds**
- **Strategy:** Stream validation (don't load all files into memory)
- **Implementation:** Validate files one-by-one, collect errors
- **Early exit:** Stop on first critical error if `--strict` flag

**NFR5: Merge operations <30 seconds**
- **Strategy:** In-memory merge, single write per file
- **Implementation:** Parse → Merge → Write (no intermediate files)

**NFR6: Dataview queries responsive with <500 notes**
- **Strategy:** Use Dataview indexes (DVJS for complex queries)
- **Dashboard design:** Limit query results (e.g., LIMIT 20)
- **Guidance:** Document recommended capsule size limits

---

### Security (NFR7-NFR12)

**NFR7: Data integrity (no data loss)**
- **Implementation:** Atomic file writes (write to temp, then move)
- **Pattern:**
```python
def safe_write(path: Path, content: str):
    temp_path = path.with_suffix('.tmp')
    temp_path.write_text(content, encoding='utf-8')
    temp_path.replace(path)  # Atomic on POSIX
```

**NFR8: Backups before modifications**
- **Implementation:** `capsule/utils/backup.py` creates timestamped zips
- **Trigger:** Every import operation creates backup first
- **Storage:** `~/.capsule/backups/vault_YYYY-MM-DD_HH-MM-SS.zip`

**NFR9: No arbitrary code execution**
- **Implementation:** Validate all YAML before loading
- **Pattern:** Use `yaml.safe_load()` not `yaml.load()`
- **Templater risk:** Document security warning (Templater can execute code)

**NFR10: Input sanitization**
- **Implementation:** Validate all user inputs before file operations
- **Pattern:**
```python
def sanitize_filename(name: str) -> str:
    # Remove path traversal attempts
    name = name.replace('..', '')
    name = name.replace('/', '_')
    name = name.replace('\\', '_')
    return name
```

**NFR11: Respect file permissions**
- **Implementation:** Use Python's standard file operations (respect OS permissions)
- **Check:** Verify write permissions before import

**NFR12: Secure credential storage**
- **Implementation:** API keys in `~/.capsule/config.yaml` (0600 permissions)
- **Warning:** Never commit config.yaml to git
- **Future:** Support environment variables for CI/CD

---

### Reliability (NFR13-NFR17)

**NFR13: Atomic backups**
- **Implementation:** Create full backup before any modifications
- **Pattern:** Backup succeeds or abort operation

**NFR14: Transactional imports**
- **Implementation:**
```python
class ImportTransaction:
    def __init__(self, vault_path):
        self.vault_path = vault_path
        self.backup_path = None
        self.changes = []
    
    def __enter__(self):
        # Create backup
        self.backup_path = create_backup(self.vault_path)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            # Rollback on error
            restore_backup(self.backup_path, self.vault_path)
        return False
```

**NFR15: Graceful network failures**
- **Implementation:** Retry logic with exponential backoff
```python
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def call_gemini_api(prompt):
    # API call here
    pass
```

**NFR16: File integrity validation**
- **Implementation:** Calculate checksums, verify after write
```python
import hashlib

def verify_write(path: Path, expected_content: str):
    actual = path.read_text()
    assert hashlib.sha256(actual.encode()).hexdigest() == \
           hashlib.sha256(expected_content.encode()).hexdigest()
```

**NFR17: Detailed logs**
- **Implementation:** Log all operations to `~/.capsule/logs/`
- **Retention:** Keep last 30 days of logs
- **Verbosity:** Use `--verbose` flag for debug logs

---

### Usability (NFR18-NFR23)

**NFR18: Unix conventions**
- **Implementation:** Follow POSIX standards
- Examples:
  - `-h` / `--help` for help
  - `-v` / `--version` for version
  - Exit codes: 0 = success, non-zero = error
  - Respect `--quiet` flag

**NFR19: Clear error messages**
- **Pattern:**
```
❌ Error: Missing required field

Problem: File 'root_notes/Ai_Ye.md' missing field 'herb_data.temperature'

Fix: Add the temperature field to the herb_data section:

  herb_data:
    temperature: "warm"  # or "cool", "neutral", "hot", "cold"

See schema: capsule/templates/domains/tcm.yaml
```

**NFR20: Progress indicators**
- **Implementation:** Use `rich.progress` consistently
- **Show:** Percentage, item counts, estimated time

**NFR21: Validation reports**
- **Implementation:** Clear summary + detailed errors
- **Format:** See validation report structure (above)

**NFR22: Import previews**
- **Implementation:** Show what will change before executing
- **Require approval:** Interactive prompt (unless `--auto-approve`)

**NFR23: Help with examples**
- **Implementation:** Every command has examples in docstring
```python
@app.command()
def generate(topic: str):
    """
    Generate a new capsule.
    
    Examples:
        # Basic generation
        capsule generate "Introduction to Python"
        
        # With specific template
        capsule generate "TCM Herbs" --template tcm
        
        # Hybrid mode (enhance existing note)
        capsule generate "Ginger" --hybrid notes/ginger.md
    """
```

---

### Compatibility (NFR24-NFR30)

**NFR24-27: Plugin Compatibility**
- **Strategy:** Follow plugin documentation, test against minimum versions
- **Implementation:** Document version requirements in cypher
- **Testing:** Manual testing with each plugin version

**NFR28: Cross-platform (Windows, macOS, Linux)**
- **Implementation:** Use `pathlib.Path` for all file operations
- **Testing:** CI/CD on all three platforms
- **Avoid:** OS-specific commands

**NFR29: Python 3.8+ support**
- **Implementation:** No features requiring Python 3.9+
- **Testing:** CI matrix testing Python 3.8, 3.9, 3.10, 3.11, 3.12

**NFR30: Graceful degradation without plugins**
- **Implementation:** Markdown remains valid without Dataview
- **Fallback:** Static content visible, dynamic queries show as code blocks

---

### Maintainability (NFR31-NFR35)

**NFR31: PEP 8 compliance**
- **Enforcement:** `black` auto-formatter + `flake8` linting
- **CI:** Block PRs that fail lint checks

**NFR32: Docstrings with examples**
- **Pattern:**
```python
def merge_notes(existing: Note, incoming: Note) -> Note:
    """
    Merge incoming note frontmatter into existing note.
    
    Args:
        existing: Current note in vault
        incoming: New note from capsule import
    
    Returns:
        Merged note with combined frontmatter
    
    Example:
        >>> existing = Note(frontmatter={'herb_data': {...}})
        >>> incoming = Note(frontmatter={'recipe_data': {...}})
        >>> merged = merge_notes(existing, incoming)
        >>> assert 'herb_data' in merged.frontmatter
        >>> assert 'recipe_data' in merged.frontmatter
    """
```

**NFR33: Jinja2 templates**
- **Rationale:** Industry standard, well-documented, powerful
- **Location:** `capsule/templates/*.j2`

**NFR34: Standard YAML**
- **Rationale:** Human-readable, widely supported
- **Library:** `ruamel.yaml` for comment preservation

**NFR35: Semantic versioning**
- **Format:** MAJOR.MINOR.PATCH
- **Bumping:**
  - MAJOR: Breaking changes
  - MINOR: New features (backward compatible)
  - PATCH: Bug fixes

---

## Architecture Decision Records (ADRs)

### ADR-001: Typer + Cookiecutter for Python CLI

**Status:** Accepted  
**Date:** 2025-11-15  
**Decision:** Use Typer framework with Cookiecutter PyPackage structure  

**Context:** Need modern Python CLI with type safety, good DX, and professional project structure

**Alternatives Considered:**
- Click (predecessor to Typer)
- argparse (stdlib)
- Manual project structure

**Decision:** Typer + Cookiecutter  

**Rationale:**
- Type hints provide safety and IDE support
- Rich library integration for beautiful output
- Cookiecutter gives professional structure
- Well-maintained, industry-standard tools

**Consequences:**
- Python 3.8+ required (type hints)
- Learning curve for contributors unfamiliar with Typer
- Excellent error messages and help documentation built-in

---

### ADR-002: Gemini API for Deep Research (v1.0)

**Status:** Accepted  
**Date:** 2025-11-15  
**Decision:** Use Google Gemini API with Search grounding as primary research provider

**Context:** Need AI-powered research with citations for content generation

**Alternatives Considered:**
- OpenAI GPT-4 + separate search API
- Perplexity AI (research-focused)
- Web scraping + local LLM

**Decision:** Gemini with built-in grounding  

**Rationale:**
- Single API (no separate search API needed)
- Real-time web search built-in
- Automatic citations
- Free tier for development
- Good quality for educational content

**Consequences:**
- Requires Google API key
- Provider abstraction allows future expansion
- v1.5+ can add Perplexity, OpenAI, local LLMs without architecture changes

---

### ADR-003: Section-Level Merge Strategy

**Status:** Accepted  
**Date:** 2025-11-15  
**Decision:** Implement section-level frontmatter merging for capsule imports

**Context:** Need to safely import capsules without data loss or conflicts

**Alternatives Considered:**
- File-level replacement (dangerous)
- Field-level merge (too complex for v1.0)
- Always create new files (causes duplicates)

**Decision:** Section-level merge with conflict detection  

**Rationale:**
- Same capsule updates: Replace domain sections atomically
- Different capsules: Add new sections without conflicts
- User content (body) always preserved
- Clear conflict detection with user prompts

**Consequences:**
- Enables cross-domain composability (ginger = herb + recipe)
- Requires careful testing of merge logic
- Users can safely update and enhance notes

---

### ADR-004: Universal Frontmatter + Domain Sections

**Status:** Accepted  
**Date:** 2025-11-15  
**Decision:** Universal 6-field frontmatter + extensible domain sections

**Context:** Need structure that works for ANY knowledge domain

**Alternatives Considered:**
- Flat frontmatter (all fields at root)
- Single custom_data section
- No universal fields (all custom)

**Decision:** Universal fields + domain_data sections  

**Rationale:**
- Universal fields (id, name, type, tags, created, updated) work for any domain
- Domain sections (herb_data, recipe_data, etc.) allow specialization
- Multiple sections enable cross-domain composability
- Clear separation of concerns

**Consequences:**
- Notes can belong to multiple capsules
- Dataview queries work consistently
- Template system can validate against schemas
- Future-proof for any knowledge domain

---

## Deployment Architecture

### Development Environment

**Requirements:**
- Python 3.8+
- Git
- Text editor / IDE
- Obsidian (for testing dashboards)

**Setup:**
```bash
# Clone repository
git clone https://github.com/user/obsidian-capsule-delivery
cd obsidian-capsule-delivery

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linting
black capsule tests
flake8 capsule tests
mypy capsule
```

---

### Production Distribution

**Package Distribution:**
```bash
# Build package
python -m build

# Upload to PyPI
twine upload dist/*

# Users install via:
pip install obsidian-capsule-cli
```

**Configuration:**
```bash
# First-time setup
capsule init

# Creates:
# ~/.capsule/config.yaml
# ~/.capsule/backups/
# ~/.capsule/logs/
```

---

### CI/CD Pipeline

**GitHub Actions Workflow:**
```yaml
# .github/workflows/ci.yml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: [3.8, 3.9, '3.10', 3.11, 3.12]
    
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          pip install -e ".[dev]"
      
      - name: Run linting
        run: |
          black --check capsule tests
          flake8 capsule tests
          mypy capsule
      
      - name: Run tests
        run: |
          pytest --cov=capsule --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

---

## Summary & Validation

### Architecture Completeness Checklist

✅ **Foundation:**
- [x] Project initialization command documented
- [x] Technology stack specified with versions
- [x] Complete project structure defined
- [x] Decision summary table complete

✅ **Epic Coverage:**
- [x] All 65 Functional Requirements mapped to architecture
- [x] All 9 FR groups have component designs
- [x] Data flows documented for complex operations
- [x] Integration points defined

✅ **Implementation Guidance:**
- [x] Merge algorithm specified (critical for FR32-38)
- [x] Validation engine design complete
- [x] CLI command patterns defined
- [x] Error handling strategy documented

✅ **Cross-Cutting Concerns:**
- [x] Error handling strategy
- [x] Logging strategy
- [x] Date/time handling
- [x] Configuration management
- [x] Testing strategy

✅ **Consistency Patterns:**
- [x] Naming conventions (files, code, frontmatter, CLI)
- [x] File organization patterns
- [x] Data exchange patterns
- [x] Communication patterns

✅ **NFR Handling:**
- [x] Performance requirements addressed (NFR1-6)
- [x] Security requirements addressed (NFR7-12)
- [x] Reliability requirements addressed (NFR13-17)
- [x] Usability requirements addressed (NFR18-23)
- [x] Compatibility requirements addressed (NFR24-30)
- [x] Maintainability requirements addressed (NFR31-35)

✅ **Novel Patterns:**
- [x] Template-driven architecture documented
- [x] Capsule cypher as "universal contract"
- [x] Cross-domain composability pattern
- [x] Section-level merge strategy

✅ **Decision Records:**
- [x] Key architectural decisions documented
- [x] Alternatives considered
- [x] Rationale provided
- [x] Consequences noted

---

## Next Steps

### Immediate Actions (Before Implementation)

1. **Review Architecture Document**
   - Stakeholder review of decisions
   - Validate against PRD requirements
   - Confirm technical approach

2. **Set Up Development Environment**
   - Initialize repository
   - Run cookiecutter
   - Set up CI/CD pipeline

3. **Create Epic Breakdown**
   - Decompose 65 FRs into implementable stories
   - Sequence development work
   - Estimate effort

### Implementation Sequence Recommendation

**Phase 1: Foundation (Sprint 1-2)**
- Project scaffolding (Cookiecutter + Typer)
- Config management
- Core models (Capsule, Note, Cypher, Template)
- Testing infrastructure

**Phase 2: Content Generation (Sprint 3-5)**
- Gemini research provider
- Template engine integration
- Content generator
- Validation engine

**Phase 3: Packaging & Distribution (Sprint 6-8)**
- Capsule packager
- Export functionality
- Import with preview
- Merge strategies

**Phase 4: CLI & Polish (Sprint 9-10)**
- All CLI commands
- Dashboard generation
- Error handling refinement
- Documentation

---

## Document Metadata

**Version:** 1.0  
**Status:** Complete  
**Last Updated:** 2025-11-15  
**Author:** BMad (Architect Agent)  
**Reviewers:** [Pending]  
**Next Review:** Before epic breakdown  

**Related Documents:**
- PRD.md - Product Requirements (65 FRs, 35 NFRs)
- technical-research-capsules.md - Technical validation research
- bmm-brainstorming-session-2025-11-15.md - Architecture design session

**Changes Since Last Version:**
- Initial version - comprehensive architecture for OCDS v1.0

---

**END OF ARCHITECTURE DOCUMENT**

