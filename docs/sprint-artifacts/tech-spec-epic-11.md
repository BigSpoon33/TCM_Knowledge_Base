# Epic Technical Specification: Dashboard Functionality (Core/Data Layer)

Date: 2025-11-22
Author: BMad
Epic ID: 11
Status: Draft

---

## Overview

Epic 11 implements a **hierarchical dashboard navigation system** for the Obsidian Capsule Delivery System, enabling users to manage and navigate multiple capsules within their vault. This epic delivers the **Core/Data Layer** of the dashboard functionality, focusing on:

- **Master Dashboard**: Vault-wide view that aggregates and filters all installed capsule dashboards
- **Capsule Dashboards**: Per-capsule navigation hubs with metadata, progress tracking, and content links
- **Filtered Content Views**: Domain-specific study aggregations using advanced Dataview queries

The system leverages **Dataview** for standard queries (file lists, metadata filtering) and **DataviewJS** for advanced features (heading extraction, progress calculations, TaskNotes integration). All dashboard templates are generated as Markdown files with embedded query code blocks, ensuring content remains readable even without plugins installed.

**Key Architectural Pattern**: Dashboards are **generated at capsule import time** and stored as static Markdown files with dynamic Dataview queries. This aligns with the existing capsule packaging and import infrastructure established in Epics 6-10.

This epic explicitly **excludes** visual polish (CSS theming, interactive widgets, aesthetic enhancements), which is deferred to Epic 12.

## Objectives and Scope

### In-Scope

**Dashboard Generation Infrastructure:**
- Template system for master and capsule dashboards (Jinja2 templates)
- Dashboard generation during capsule import workflow
- Dashboard frontmatter schema with metadata fields (class, topic, category, active status)

**Query Capabilities:**
- Dataview queries for file lists, metadata filtering, task aggregation
- DataviewJS queries for heading extraction, progress calculations, complex data manipulation
- Cross-capsule connection queries (notes belonging to multiple capsules)

**Navigation Features:**
- Hierarchical navigation (Master → Capsule → Content)
- Master dashboard filtering by capsule metadata (class, topic, category, active)
- Capsule dashboard content organization (root notes, study materials, tasks)
- Domain-specific filtered views (e.g., all formulas → ingredients aggregation)

**Progress Tracking:**
- TaskNotes integration for due dates and completion tracking
- Progress percentage calculations via DataviewJS
- Active timeline display for sequenced capsules

**Pattern Library:**
- Documented query patterns for dashboard development
- Best practices for Dataview/DataviewJS performance
- Reusable query snippets for common dashboard use cases

### Out-of-Scope (Deferred to Epic 12)

**Visual Design & Polish:**
- CSS theming and custom styling
- Neon themes, custom separators, visual hierarchy
- Responsive layout design
- Interactive widgets (Meta-Bind forms/buttons)

**Advanced Plugin Integrations:**
- Templater dynamic content generation (beyond import-time generation)
- Spaced Repetition dashboard integration
- Custom JavaScript enhancements

**User Customization:**
- Dashboard customization UI
- User-defined dashboard layouts
- Dashboard template marketplace

### Success Criteria

1. **Master Dashboard** displays all capsule dashboards with working metadata filters
2. **Capsule Dashboards** show accurate file counts, progress tracking, and navigation links
3. **DataviewJS queries** successfully extract headings from note bodies for filtered views
4. **Dashboard generation** integrates seamlessly into existing `capsule import` workflow
5. **Query performance** remains responsive with realistic capsule sizes (<500 notes per capsule)
6. **Dashboards remain readable** when Dataview plugin is disabled (graceful degradation)

## System Architecture Alignment

Epic 11 directly implements **FR Group 9: Dashboard Integration** (FR59-FR65) from the PRD and **Epic Group 9: Dashboard Integration** from the Architecture document.

### PRD Alignment

- **FR59**: Each capsule includes a dashboard template ✅ (Story 11-3)
- **FR60**: Capsule dashboards display metadata ✅ (Story 11-1, 11-3)
- **FR61**: Capsule dashboards link to master dashboard ✅ (Story 11-2, 11-3)
- **FR62**: Capsule dashboards use Dataview queries ✅ (Story 11-3, 11-5)
- **FR63**: Master dashboard aggregates all capsules ✅ (Story 11-2)
- **FR64**: Master dashboard displays active timelines ✅ (Story 11-4)
- **FR65**: Master dashboard shows cross-capsule connections ✅ (Story 11-2)

### Architecture Alignment

**Builds on Existing Components:**
- `capsule/core/importer.py` - Extended to generate dashboards during import (Story 11-8)
- `capsule/templates/` directory - New Jinja2 dashboard templates added (Story 11-2, 11-3)
- `capsule/models/cypher.py` - Capsule metadata model used for dashboard generation

**Leverages Established Patterns:**
- **Template-driven generation**: Dashboards use same Jinja2 pattern as note generation (Epic 4)
- **Import-time generation**: Dashboards generated during `capsule import`, consistent with cypher validation and file placement
- **Frontmatter-based metadata**: Dashboard frontmatter follows universal schema pattern

**Plugin Ecosystem Integration:**
- **Dataview v0.5.0+** (NFR25): Standard query engine for file lists and metadata filtering
- **TaskNotes v1.0.0+** (NFR26): Progress tracking and task completion (Story 11-4)
- **Graceful degradation** (NFR30): Dashboard Markdown remains readable without plugins

### Architectural Constraints

1. **No Runtime Code Execution**: Dashboards are static Markdown files with query blocks, not dynamic scripts
2. **Plugin-Dependent Features**: Advanced features require Dataview/DataviewJS installation (documented in dashboard headers)
3. **Performance Limits**: Query complexity constrained by Dataview performance (NFR6: responsive with <500 notes)
4. **File System Integration**: Dashboards stored in capsule folders alongside content (e.g., `TCM_Herbs_v1/capsule-dashboard.md`)

## Detailed Design

### Services and Modules

#### New Template Files

**`capsule/templates/master-dashboard.md.j2`**
- **Responsibility**: Master dashboard template for vault-wide capsule aggregation
- **Inputs**: None (queries all capsule dashboards dynamically)
- **Outputs**: Rendered Markdown file with Dataview/DataviewJS queries
- **Owner**: Template system (Epic 4 infrastructure)

**`capsule/templates/capsule-dashboard.md.j2`**
- **Responsibility**: Per-capsule dashboard template with metadata, navigation, and progress tracking
- **Inputs**: 
  - `capsule.id` (string)
  - `capsule.name` (string)
  - `capsule.version` (string)
  - `capsule.domain_type` (string)
  - `capsule.sequence_mode` (string: "freeform" | "sequenced" | "hybrid")
  - `domain_sections` (dict: domain-specific dashboard sections)
- **Outputs**: Rendered Markdown file with capsule-specific queries
- **Owner**: Template system

#### Modified Modules

**`capsule/core/importer.py`**
- **New Method**: `generate_dashboards(capsule: Capsule, vault_path: Path) -> List[Path]`
  - **Inputs**: Capsule model, vault destination path
  - **Outputs**: List of generated dashboard file paths
  - **Responsibility**: Generate master and capsule dashboards during import workflow
  - **Integration Point**: Called after file extraction, before merge operations

**`capsule/models/cypher.py`**
- **New Fields** (optional in cypher schema):
  ```yaml
  dashboard_metadata:
    class: string        # e.g., "TCM101"
    topic: string        # e.g., "Herbal Medicine"
    category: string     # e.g., "CALE", "NCCAOM"
    active: boolean      # Is this capsule currently being studied?
  ```
- **Responsibility**: Store dashboard-specific metadata in cypher for query filtering
- **Owner**: Data model (Epic 1 infrastructure)

#### New Utility Module

**`capsule/utils/dataview_queries.py`**
- **Responsibility**: Dataview/DataviewJS query pattern library
- **Functions**:
  - `build_file_list_query(source_capsule: str, file_type: str) -> str`
  - `build_metadata_filter_query(filters: Dict) -> str`
  - `build_heading_extraction_query(tag: str, heading: str) -> str`
  - `build_progress_calculation_query(capsule_id: str) -> str`
- **Inputs**: Query parameters (capsule IDs, filters, tags, headings)
- **Outputs**: Formatted Dataview/DataviewJS query strings
- **Owner**: New utility module (Story 11-5)

#### Component Diagram

```
capsule import command
    ↓
capsule/core/importer.py
    ├─→ Extract files to vault
    ├─→ Validate cypher
    ├─→ generate_dashboards() ← NEW
    │     ├─→ Load templates/master-dashboard.md.j2
    │     ├─→ Load templates/capsule-dashboard.md.j2
    │     ├─→ Render with capsule metadata
    │     └─→ Write dashboard files to vault
    └─→ Merge notes (existing logic)
```

### Data Models and Contracts

#### Capsule Dashboard Frontmatter Schema

```yaml
---
# Universal Dashboard Fields (required)
type: capsule_dashboard
capsule_id: "TCM_Herbs_v1"
version: "1.0.0"
created: "2025-11-22T10:00:00Z"
updated: "2025-11-22T10:00:00Z"

# Dashboard Metadata (optional, used for filtering)
dashboard_metadata:
  class: "TCM101"           # Course/subject identifier
  topic: "Herbal Medicine"  # Topic description
  category: "CALE"          # Certification category (CALE, NCCAOM, etc.)
  active: true              # Is this capsule actively being studied?
  
# Provenance (generated by import workflow)
source_capsules: ["TCM_Herbs_v1"]
---
```

**Field Definitions:**

| Field | Type | Required | Description | Used For |
|-------|------|----------|-------------|----------|
| `type` | string | Yes | Always `"capsule_dashboard"` | Dataview query filtering |
| `capsule_id` | string | Yes | Unique capsule identifier | Linking to capsule content |
| `version` | string | Yes | Capsule version (semver) | Version tracking |
| `dashboard_metadata.class` | string | No | Course/subject code | Master dashboard filtering |
| `dashboard_metadata.topic` | string | No | Topic description | Master dashboard filtering |
| `dashboard_metadata.category` | string | No | Certification/category | Master dashboard filtering |
| `dashboard_metadata.active` | boolean | No | Active study status | Master dashboard filtering |

#### Master Dashboard Frontmatter Schema

```yaml
---
type: master_dashboard
title: "My Knowledge System"
created: "2025-11-22T10:00:00Z"
updated: "2025-11-22T10:00:00Z"
---
```

**Note**: Master dashboard does not belong to any capsule; it aggregates all capsule dashboards.

#### TaskNotes Integration Data Model

For capsules with `sequence_mode: "sequenced"`, tasks are generated with the following structure:

```markdown
- [ ] Study: Ai Ye (Mugwort) #tasknotes 📅 2025-11-25
- [ ] Quiz: Herbs Week 1 #tasknotes 📅 2025-11-28
- [ ] Review: Flashcards Set 1 #tasknotes 📅 2025-12-01
```

**TaskNotes Metadata** (stored in capsule cypher):

```yaml
timeline:
  - note: "root_notes/Ai_Ye.md"
    due_date: "2025-11-25"
    task_type: "study"
  - note: "study_materials/quizzes/week1.md"
    due_date: "2025-11-28"
    task_type: "quiz"
```

**Note**: Timeline data is read from cypher at import time and converted to TaskNotes-compatible task Markdown.

#### Heading Extraction Data Structure (DataviewJS)

For filtered content views (Story 11-6), heading extraction returns:

```javascript
// Example: Extract #ingredients from all #formula notes
{
  "formula_note_1": {
    "file": "root_notes/Ba_Zhen_Tang.md",
    "headings": ["Ingredients", "Preparation"],
    "content": {
      "Ingredients": "Dang Gui 当归, Chuan Xiong 川芎, ..."
    }
  },
  "formula_note_2": {
    "file": "root_notes/Si_Jun_Zi_Tang.md",
    "headings": ["Ingredients", "Actions"],
    "content": {
      "Ingredients": "Ren Shen 人参, Bai Zhu 白术, ..."
    }
  }
}
```

**Query Pattern** (DataviewJS):

```javascript
const formulaNotes = dv.pages('#formula')
  .where(p => p.source_capsules?.includes("TCM_Formulas_v1"));

for (let note of formulaNotes) {
  const content = await dv.io.load(note.file.path);
  const ingredientsSection = extractHeading(content, "Ingredients");
  // Render extracted content
}
```

### APIs and Interfaces

#### Importer API Extension

**Method**: `generate_dashboards(capsule: Capsule, vault_path: Path) -> List[Path]`

**Location**: `capsule/core/importer.py`

**Request Model**:
```python
capsule: Capsule  # Capsule model with metadata
vault_path: Path  # Vault destination path
```

**Response Model**:
```python
List[Path]  # Paths to generated dashboard files
# Example: [
#   Path("/vault/TCM_Herbs_v1/capsule-dashboard.md"),
#   Path("/vault/Master Dashboard.md")
# ]
```

**Error Conditions**:
- `TemplateNotFoundError`: Dashboard template file missing
- `FileWriteError`: Cannot write dashboard to vault
- `InvalidCapsuleMetadataError`: Missing required capsule metadata

**Implementation Pattern**:
```python
def generate_dashboards(capsule: Capsule, vault_path: Path) -> List[Path]:
    """Generate master and capsule dashboards during import."""
    
    # Load templates
    env = Environment(loader=FileSystemLoader('capsule/templates'))
    capsule_template = env.get_template('capsule-dashboard.md.j2')
    master_template = env.get_template('master-dashboard.md.j2')
    
    # Render capsule dashboard
    capsule_dashboard_content = capsule_template.render(
        capsule=capsule,
        domain_sections=load_domain_sections(capsule.domain_type)
    )
    
    # Write capsule dashboard
    capsule_dashboard_path = vault_path / capsule.id / "capsule-dashboard.md"
    capsule_dashboard_path.write_text(capsule_dashboard_content, encoding='utf-8')
    
    # Update or create master dashboard
    master_dashboard_path = vault_path / "Master Dashboard.md"
    if not master_dashboard_path.exists():
        master_content = master_template.render()
        master_dashboard_path.write_text(master_content, encoding='utf-8')
    
    return [capsule_dashboard_path, master_dashboard_path]
```

#### Dataview Query Builder API

**Module**: `capsule/utils/dataview_queries.py`

**Function**: `build_file_list_query(source_capsule: str, file_type: str) -> str`

**Request**:
```python
source_capsule: str  # Capsule ID (e.g., "TCM_Herbs_v1")
file_type: str       # Filter by type field (e.g., "root_note", "flashcard")
```

**Response**:
```python
str  # Formatted Dataview query
```

**Example Output**:
```markdown
```dataview
TABLE type, tags, updated
FROM ""
WHERE contains(source_capsules, "TCM_Herbs_v1")
  AND type = "root_note"
SORT name ASC
```
```

**Function**: `build_metadata_filter_query(filters: Dict) -> str`

**Request**:
```python
filters: Dict[str, Any]
# Example: {
#   "class": "TCM101",
#   "active": True,
#   "category": "CALE"
# }
```

**Response**:
```python
str  # Formatted Dataview query with WHERE clauses
```

**Example Output**:
```markdown
```dataview
TABLE capsule_id, version, dashboard_metadata.topic
FROM ""
WHERE type = "capsule_dashboard"
  AND dashboard_metadata.class = "TCM101"
  AND dashboard_metadata.active = true
  AND dashboard_metadata.category = "CALE"
SORT file.name ASC
```
```

**Function**: `build_heading_extraction_query(tag: str, heading: str) -> str`

**Request**:
```python
tag: str       # Note tag filter (e.g., "formula")
heading: str   # Heading to extract (e.g., "Ingredients")
```

**Response**:
```python
str  # Formatted DataviewJS query
```

**Example Output**:
````markdown
```dataviewjs
const notes = dv.pages('#formula');
const results = [];

for (let note of notes) {
  const content = await dv.io.load(note.file.path);
  const headingContent = extractHeading(content, "Ingredients");
  if (headingContent) {
    results.push({
      name: note.file.name,
      content: headingContent
    });
  }
}

dv.table(["Formula", "Ingredients"], 
  results.map(r => [r.name, r.content]));
```
````

#### Template Rendering Interface

**Jinja2 Template Variables** (Capsule Dashboard):

```python
{
  "capsule": {
    "id": str,              # "TCM_Herbs_v1"
    "name": str,            # "TCM Materia Medica - Herbs"
    "version": str,         # "1.0.0"
    "domain_type": str,     # "traditional_chinese_medicine"
    "sequence_mode": str    # "freeform" | "sequenced" | "hybrid"
  },
  "domain_sections": str    # Rendered domain-specific dashboard content
}
```

**Jinja2 Template Variables** (Master Dashboard):

```python
{
  # No variables - queries all capsule dashboards dynamically
}
```

### Workflows and Sequencing

#### Dashboard Generation Workflow (Import Time)

```
User executes: capsule import TCM_Herbs_v1.capsule
    ↓
CLI: import_cmd.py
    ↓
Importer: capsule/core/importer.py
    ├─→ [1] Extract capsule archive
    ├─→ [2] Load and validate capsule-cypher.yaml
    ├─→ [3] Display import preview
    ├─→ [4] User approval
    ├─→ [5] Create vault backup
    ├─→ [6] Copy files to vault
    ├─→ [7] generate_dashboards() ← NEW STEP
    │       ├─→ Load master-dashboard.md.j2
    │       ├─→ Load capsule-dashboard.md.j2
    │       ├─→ Render capsule dashboard with metadata
    │       ├─→ Write: vault/TCM_Herbs_v1/capsule-dashboard.md
    │       └─→ Update/create: vault/Master Dashboard.md
    ├─→ [8] Merge notes with existing vault
    └─→ [9] Report import success
```

**Key Sequencing Decision**: Dashboards are generated **after** files are copied but **before** merge operations. This ensures:
- Dashboard files are included in merge conflict detection
- Dashboard generation can reference newly imported files
- Failed imports roll back dashboard generation

#### Master Dashboard Query Workflow (Runtime)

```
User opens: Master Dashboard.md in Obsidian
    ↓
Obsidian renders Markdown
    ↓
Dataview plugin detects query blocks
    ↓
For each Dataview query:
    ├─→ Parse WHERE clauses (metadata filters)
    ├─→ Scan vault for type = "capsule_dashboard"
    ├─→ Apply filters (class, topic, category, active)
    ├─→ Sort results
    └─→ Render table/list
    ↓
For each DataviewJS query:
    ├─→ Execute JavaScript
    ├─→ Access dv.pages() API
    ├─→ Calculate aggregations (file counts, progress %)
    └─→ Render custom HTML/Markdown
    ↓
User sees: Filtered capsule dashboard list
```

**Performance Consideration**: Dataview caches file metadata, so subsequent query executions are fast (<100ms for typical vaults).

#### Capsule Dashboard Navigation Workflow (Runtime)

```
User clicks: Link to capsule dashboard from master
    ↓
Obsidian opens: vault/TCM_Herbs_v1/capsule-dashboard.md
    ↓
Dataview renders queries:
    ├─→ Root notes query (WHERE source_capsules includes capsule_id)
    ├─→ Study materials query (filtered by type)
    ├─→ Recent activity query (SORT by updated DESC)
    └─→ (If sequenced) Active timeline query (TaskNotes integration)
    ↓
DataviewJS calculates:
    ├─→ File counts (dv.pages().length)
    ├─→ Progress percentage (completed tasks / total tasks)
    └─→ Last updated timestamp
    ↓
User sees: Capsule overview with navigation links
    ↓
User clicks: Link to specific note or study material
    ↓
Obsidian opens: Linked note
```

#### Heading Extraction Workflow (Advanced Filtering)

```
User opens: Domain-specific filtered view (e.g., "All Ingredients.md")
    ↓
DataviewJS query executes:
    ↓
For each note matching tag filter (#formula):
    ├─→ Load note content: dv.io.load(note.file.path)
    ├─→ Parse Markdown headings (regex or parser)
    ├─→ Extract content under target heading ("## Ingredients")
    ├─→ Store in results array
    ↓
Render aggregated view:
    └─→ Display table: [Formula Name] | [Ingredients]
    ↓
User sees: Consolidated ingredient list from all formulas
```

**Technical Note**: Heading extraction requires reading file contents, which is slower than metadata-only queries. Recommended limit: <100 notes per query for acceptable performance.

#### Dashboard Update Workflow (Capsule Update)

```
User executes: capsule import TCM_Herbs_v2.capsule (updated version)
    ↓
Importer detects: Existing capsule_id with older version
    ↓
Import workflow:
    ├─→ Extract and validate v2 capsule
    ├─→ Preview shows: "Update existing capsule dashboard"
    ├─→ User approval
    ├─→ Backup vault
    ├─→ Copy files
    ├─→ generate_dashboards()
    │       ├─→ Detect existing capsule-dashboard.md
    │       ├─→ Perform section-level merge on dashboard frontmatter
    │       │   (Updates version, preserves user-added metadata)
    │       └─→ Write updated dashboard
    └─→ Merge notes
    ↓
Result: Capsule dashboard updated to v2, metadata preserved
```

**Merge Strategy for Dashboards**: Dashboards follow same merge rules as notes:
- **Same capsule update**: Section-level merge (update version, preserve custom metadata)
- **User modifications**: Body content preserved (user can add notes below queries)

## Non-Functional Requirements

### Performance

**NFR6 (from PRD)**: Dataview queries on capsule frontmatter remain responsive with <500 notes per capsule

**Epic 11 Specific Performance Targets:**

1. **Master Dashboard Load Time**: <2 seconds with up to 50 installed capsules
   - **Rationale**: Master dashboard queries only scan capsule dashboard files (not all notes)
   - **Implementation**: Use `FROM ""` with `type = "capsule_dashboard"` filter to limit scope

2. **Capsule Dashboard Query Execution**: <1 second for standard queries (file lists, task aggregation)
   - **Rationale**: Standard Dataview queries use indexed metadata, not file content
   - **Implementation**: Avoid complex WHERE clauses; use simple metadata filters

3. **DataviewJS Heading Extraction**: <5 seconds for queries processing <100 notes
   - **Rationale**: Heading extraction requires reading file contents (slow I/O operation)
   - **Implementation**: 
     - Limit heading extraction queries to specific tag filters
     - Document performance warning in query comments
     - Use pagination if >100 results

4. **Dashboard Generation Time** (during import): <3 seconds for typical capsule
   - **Rationale**: Template rendering and file writes are fast operations
   - **Implementation**: Single-pass template rendering, atomic file writes

**Performance Monitoring Strategy:**

- **Story 11-0 (Technical Spike)**: Benchmark Dataview query performance with realistic data sets
- **Story 11-6 (Heading Extraction)**: Measure DataviewJS performance with varying note counts (10, 50, 100, 500)
- **Story 11-5 (Query Pattern Library)**: Document query complexity and expected performance for each pattern

**Performance Degradation Handling:**

```markdown
<!-- Performance warning example in dashboard -->
⚠️ **Performance Note**: This query extracts headings from all formula notes. 
Expected load time with 100 formulas: ~5 seconds. 
If vault has >200 formulas, consider filtering by subcategory.
```

### Security

**NFR7 (from PRD)**: All capsule operations preserve data integrity (no data loss)

**Epic 11 Specific Security Considerations:**

1. **Dashboard File Overwrite Protection**
   - **Risk**: Import overwrites user-modified dashboard without warning
   - **Mitigation**: Dashboard merge follows same section-level merge as notes
   - **Implementation**: Dashboard frontmatter merge preserves user-added metadata fields

2. **DataviewJS Code Injection**
   - **Risk**: Malicious capsule includes DataviewJS code that executes arbitrary JavaScript
   - **Mitigation**: 
     - DataviewJS runs in Obsidian sandbox (limited API surface)
     - Dashboards generated from trusted Jinja2 templates, not user-supplied code
     - Import preview shows dashboard content before execution
   - **Note**: DataviewJS security is delegated to Obsidian/Dataview plugin (outside OCDS control)

3. **Template Injection**
   - **Risk**: Capsule metadata contains Jinja2 syntax that executes during template rendering
   - **Mitigation**: 
     - Use Jinja2 autoescaping for all capsule metadata variables
     - Validate capsule metadata before template rendering
   - **Implementation**:
     ```python
     env = Environment(
         loader=FileSystemLoader('capsule/templates'),
         autoescape=select_autoescape(['html', 'xml', 'md'])
     )
     ```

4. **File Path Traversal**
   - **Risk**: Dashboard generation writes to paths outside capsule directory
   - **Mitigation**: 
     - Validate dashboard paths are within vault boundaries
     - Use `Path.resolve()` to detect `..` traversal attempts
   - **Implementation**:
     ```python
     dashboard_path = vault_path / capsule.id / "capsule-dashboard.md"
     if not dashboard_path.resolve().is_relative_to(vault_path.resolve()):
         raise SecurityError("Dashboard path outside vault boundary")
     ```

5. **Sensitive Data in Dashboard Metadata**
   - **Risk**: User accidentally adds API keys or passwords to dashboard frontmatter
   - **Mitigation**: 
     - Document recommended metadata fields (no sensitive data)
     - Dashboard metadata is optional (default empty)
   - **Note**: OCDS does not validate metadata content (user responsibility)

**Security Checklist for Dashboard Implementation:**

- [ ] Jinja2 templates use autoescaping
- [ ] Dashboard file paths validated before write
- [ ] Dashboard merge follows section-level merge rules
- [ ] Import preview shows dashboard content before execution
- [ ] Documentation warns against sensitive data in metadata

### Reliability/Availability

**NFR14 (from PRD)**: Import operations are transactional (all-or-nothing, rollback on failure)

**Epic 11 Reliability Requirements:**

1. **Dashboard Generation Failure Handling**
   - **Scenario**: Template rendering fails during import
   - **Behavior**: 
     - Log error with detailed message
     - Rollback entire import transaction (delete copied files, restore backup)
     - Report to user: "Dashboard generation failed: [reason]"
   - **Implementation**: Dashboard generation wrapped in try/except within import transaction

2. **Partial Dashboard Generation**
   - **Scenario**: Capsule dashboard generates successfully, but master dashboard update fails
   - **Behavior**: 
     - Treat as partial failure
     - Options:
       - (Preferred) Continue import, log warning: "Master dashboard update failed, capsule dashboard created"
       - (Strict) Rollback entire import
   - **Decision**: Preferred behavior (continue import) because master dashboard is vault-level (not capsule-specific)

3. **Dataview Plugin Missing**
   - **Scenario**: User imports capsule but doesn't have Dataview installed
   - **Behavior**: 
     - Dashboard files are still created (graceful degradation)
     - Queries render as code blocks (readable but non-functional)
     - Dashboard header includes plugin requirement notice
   - **Implementation**:
     ```markdown
     ---
     type: capsule_dashboard
     ---
     
     > **Plugin Required**: This dashboard requires [Dataview](https://github.com/blacksmithgu/obsidian-dataview) v0.5.0+.
     > Queries below will appear as code blocks until plugin is installed.
     
     # Capsule Dashboard: TCM Herbs
     ...
     ```

4. **Corrupted Dashboard File**
   - **Scenario**: User manually edits dashboard and breaks YAML frontmatter
   - **Behavior**: 
     - Dataview queries still execute (only frontmatter affected)
     - Next capsule update detects corrupted frontmatter
     - Options:
       - (Preferred) Regenerate dashboard with warning: "Dashboard frontmatter corrupted, regenerating..."
       - (Safe) Skip dashboard update, log warning
   - **Decision**: Regenerate with user confirmation during import preview

5. **Master Dashboard Merge Conflicts**
   - **Scenario**: Two capsule imports try to update master dashboard simultaneously
   - **Behavior**: 
     - Master dashboard updates are file-append operations (low conflict risk)
     - If conflict detected, regenerate entire master dashboard from scratch
   - **Implementation**: Master dashboard queries dynamically scan all capsule dashboards (no stored state)

**Reliability Testing Strategy:**

- **Story 11-8**: Test dashboard generation failure scenarios (missing template, write permissions)
- **Story 11-8**: Test import rollback when dashboard generation fails
- **Story 11-2**: Test master dashboard regeneration from multiple capsule dashboards
- **Integration Tests**: Import capsule with Dataview disabled, verify graceful degradation

### Observability

**NFR17 (from PRD)**: System provides detailed logs for debugging failed operations

**Epic 11 Logging Strategy:**

1. **Dashboard Generation Logging**
   ```python
   # capsule/core/importer.py
   logger.info(f"Generating dashboards for capsule: {capsule.id}")
   logger.debug(f"Loading template: capsule-dashboard.md.j2")
   logger.debug(f"Rendering with metadata: {capsule.dashboard_metadata}")
   logger.info(f"Dashboard written: {dashboard_path}")
   logger.warning(f"Master dashboard already exists, updating...")
   ```

2. **Query Performance Monitoring**
   - **Metric**: Dashboard load time (measured by Dataview plugin, not OCDS)
   - **Logging**: Not applicable (runtime query execution happens in Obsidian)
   - **Observability**: User-facing performance warnings in dashboard comments

3. **Template Rendering Errors**
   ```python
   logger.error(f"Template rendering failed: {template_name}")
   logger.error(f"Jinja2 error: {str(e)}")
   logger.debug(f"Template variables: {template_vars}")
   ```

4. **Dashboard File Writes**
   ```python
   logger.debug(f"Writing dashboard: {dashboard_path}")
   logger.debug(f"Dashboard size: {len(content)} bytes")
   logger.info(f"Dashboard created successfully: {dashboard_path.name}")
   ```

**Debug Information in Dashboards:**

```markdown
---
type: capsule_dashboard
capsule_id: "TCM_Herbs_v1"
version: "1.0.0"

# Generated by OCDS v1.0.0 on 2025-11-22T10:00:00Z
# Template: capsule-dashboard.md.j2
# Import session: import-20251122-100000
---

<!-- Dashboard Metadata for Debugging -->
<!-- Capsule: TCM_Herbs_v1 -->
<!-- Domain: traditional_chinese_medicine -->
<!-- Sequence Mode: freeform -->
```

**Operational Metrics** (visible in logs):

- Dashboard generation count per import
- Template rendering time (milliseconds)
- Dashboard file size (bytes)
- Master dashboard update count

**Error Reporting** (user-facing):

```bash
# Example error output
❌ Error: Dashboard generation failed

Problem: Template 'capsule-dashboard.md.j2' not found
  Capsule: TCM_Herbs_v1
  Expected path: capsule/templates/capsule-dashboard.md.j2

Fix: Verify OCDS installation is complete. Reinstall if necessary:
  pip install --force-reinstall obsidian-capsule-cli

For debugging logs, see: ~/.capsule/logs/capsule.log
```

**Story-Specific Logging Requirements:**

- **Story 11-0**: Log query execution times during spike
- **Story 11-6**: Log heading extraction performance (notes processed, time elapsed)
- **Story 11-8**: Log dashboard generation as part of import workflow

## Dependencies and Integrations

### Python Dependencies

**Existing Dependencies** (already in `pyproject.toml`):

- **Jinja2** (via existing template system) - Template rendering for dashboards
  - Version: 3.1.0+ (inherited from Epic 4)
  - Usage: Render `master-dashboard.md.j2` and `capsule-dashboard.md.j2`

- **python-frontmatter** 1.0.0+ - Frontmatter parsing and manipulation
  - Usage: Parse dashboard frontmatter during merge operations

- **ruamel.yaml** 0.17.0+ - YAML handling with comment preservation
  - Usage: Read capsule cypher dashboard metadata

- **typer** - CLI framework
  - Usage: No new commands in Epic 11 (dashboard generation integrated into existing `import` command)

**No New Python Dependencies Required** - Epic 11 leverages existing infrastructure

### Obsidian Plugin Dependencies

**Required Plugins:**

1. **Dataview v0.5.0+** (NFR25)
   - **Functionality**: Standard query execution (TABLE, LIST, TASK)
   - **Usage**: File lists, metadata filtering, task aggregation
   - **Failure Mode**: Graceful degradation (queries render as code blocks)
   - **Installation Check**: Not performed by OCDS (user responsibility)

2. **DataviewJS** (included with Dataview v0.5.0+)
   - **Functionality**: Advanced query execution (JavaScript API)
   - **Usage**: Heading extraction, progress calculations, custom rendering
   - **Failure Mode**: Graceful degradation (queries render as code blocks)
   - **Performance**: Requires manual testing (Story 11-0)

**Optional Plugins:**

3. **TaskNotes v1.0.0+** (NFR26)
   - **Functionality**: Task scheduling and completion tracking
   - **Usage**: Dashboard timeline queries (for `sequence_mode: "sequenced"` capsules)
   - **Failure Mode**: Task queries still work (TaskNotes adds scheduling features)
   - **Integration**: Read-only (dashboards query TaskNotes data, don't modify)

### Integration Points

**Epic 6: Capsule Packaging**
- `capsule/core/packager.py` - Dashboard metadata added to cypher schema
- `capsule/models/cypher.py` - Extended with `dashboard_metadata` fields

**Epic 7: Import/Export Operations**
- `capsule/core/importer.py` - **Extended** with `generate_dashboards()` method
- Dashboard generation integrated into import workflow (after file copy, before merge)

**Epic 8: Merge Strategies**
- `capsule/core/merger.py` - Dashboard frontmatter follows section-level merge rules
- Dashboard body content preserved during capsule updates

**Epic 9: Template System**
- `capsule/templates/` directory - New Jinja2 dashboard templates added
- Template rendering infrastructure reused (no modifications needed)

**Epic 10: CLI Commands**
- `capsule/commands/import_cmd.py` - No changes (dashboard generation transparent to CLI)
- Import preview extended to show dashboard files in preview output

### External Data Sources

**None** - Dashboards query vault data only (no external APIs, databases, or services)

### File System Integration

**Dashboard File Locations:**

```
vault/
├── Master Dashboard.md                    # Vault-level master dashboard
├── TCM_Herbs_v1/
│   ├── capsule-dashboard.md               # Capsule-specific dashboard
│   ├── capsule-cypher.yaml
│   └── root_notes/
│       └── ...
└── Culinary_Herbs_v2/
    ├── capsule-dashboard.md
    └── ...
```

**File Naming Convention:**
- Master dashboard: Always `Master Dashboard.md` (vault root)
- Capsule dashboard: Always `capsule-dashboard.md` (capsule directory)

**Rationale**: Fixed filenames simplify navigation and linking; master dashboard can reliably link to `[[TCM_Herbs_v1/capsule-dashboard]]`

### Version Constraints

| Dependency | Minimum Version | Current Project | Notes |
|------------|-----------------|-----------------|-------|
| Python | 3.10+ | 3.10+ | Already constrained in pyproject.toml |
| Jinja2 | 3.1.0+ | (via dependencies) | Template system |
| python-frontmatter | 1.0.0+ | ✓ | Frontmatter parsing |
| ruamel.yaml | 0.17.0+ | ✓ | YAML handling |
| Obsidian | 1.0.0+ | N/A | User environment |
| Dataview Plugin | 0.5.0+ | N/A | User environment |
| TaskNotes Plugin | 1.0.0+ | N/A | Optional, user environment |

## Acceptance Criteria (Authoritative)

### Epic-Level Acceptance Criteria

**AC1**: Master Dashboard displays all installed capsule dashboards with functional metadata filtering
- **Verification**: Import 3+ capsules with different metadata (class, topic, category, active status), verify master dashboard shows all capsules and filters work correctly

**AC2**: Capsule Dashboards show accurate file counts, progress tracking, and navigation links
- **Verification**: Open capsule dashboard, verify file count queries return correct numbers, progress percentage calculates correctly (if sequenced), all navigation links open correct files

**AC3**: DataviewJS queries successfully extract headings from note bodies for filtered content views
- **Verification**: Create filtered view query extracting specific heading (e.g., "Ingredients" from formula notes), verify all matching notes processed and content displayed correctly

**AC4**: Dashboard generation integrates seamlessly into existing `capsule import` workflow
- **Verification**: Run `capsule import`, verify dashboards generated without errors, import preview shows dashboard files, dashboards included in backup/rollback

**AC5**: Query performance remains responsive with realistic capsule sizes
- **Verification**: Test dashboard queries with capsule containing 100+ notes, measure load time <2s for master dashboard, <1s for capsule dashboard, <5s for heading extraction

**AC6**: Dashboards remain readable when Dataview plugin is disabled (graceful degradation)
- **Verification**: Disable Dataview plugin in Obsidian, open dashboards, verify frontmatter visible, queries render as readable code blocks, navigation links still work

### Story-Level Acceptance Criteria

**Story 11-0: Dataview/DataviewJS Technical Spike**

1. Document Dataview query language (DQL) capabilities for filtering, sorting, displaying frontmatter data
2. Document DataviewJS capabilities for advanced data manipulation and custom rendering
3. Create proof-of-concept examples replicating dashboard templates from architecture document
4. Document limitations, performance considerations with large note counts
5. Provide evidence-based recommendation on DQL vs DataviewJS vs hybrid approach

**Story 11-1: Capsule Dashboard Metadata Schema**

1. Define dashboard frontmatter schema with required fields (type, capsule_id, version)
2. Define optional metadata fields (class, topic, category, active) for filtering
3. Extend `capsule/models/cypher.py` with `dashboard_metadata` section
4. Document schema in architecture and query pattern library
5. Create test fixtures with sample dashboard metadata

**Story 11-2: Master Dashboard Template with Filtering**

1. Create `capsule/templates/master-dashboard.md.j2` Jinja2 template
2. Implement Dataview queries filtering capsule dashboards by metadata
3. Implement aggregation queries (total capsules, active capsules, file counts)
4. Implement cross-capsule connection queries (notes in multiple capsules)
5. Generate master dashboard during first capsule import (create if doesn't exist)

**Story 11-3: Capsule Dashboard Template - Core Structure**

1. Create `capsule/templates/capsule-dashboard.md.j2` Jinja2 template
2. Implement capsule overview section (metadata display, version, sequence mode)
3. Implement root notes query (filter by `source_capsules` field)
4. Implement study materials query (filter by type: flashcard, quiz, slide)
5. Implement recent activity query (sort by updated date)

**Story 11-4: Progress Tracking - TaskNotes Integration**

1. Implement active timeline query for sequenced capsules (TaskNotes compatibility)
2. Implement DataviewJS progress calculation (completed tasks / total tasks)
3. Display progress percentage in capsule dashboard
4. Handle freeform capsules gracefully (no timeline section if not sequenced)
5. Test with both sequenced and freeform capsule types

**Story 11-5: Dataview Query Pattern Library**

1. Create `capsule/utils/dataview_queries.py` utility module
2. Implement `build_file_list_query()` function
3. Implement `build_metadata_filter_query()` function
4. Implement `build_heading_extraction_query()` function
5. Document query patterns with examples and performance notes

**Story 11-6: Advanced Filtering - Heading Extraction**

1. Implement DataviewJS heading extraction function (parse Markdown headings)
2. Create filtered content view example (e.g., all formulas → ingredients)
3. Test heading extraction with varying note counts (10, 50, 100 notes)
4. Document performance characteristics and recommended limits
5. Add performance warning comments to queries processing >50 notes

**Story 11-7: Domain-Specific Dashboard Sections**

1. Implement domain-specific sections for TCM capsules (formulas, herbs, patterns)
2. Create domain section rendering logic (load from domain templates)
3. Integrate domain sections into capsule dashboard template
4. Test with TCM capsule (existing vault data)
5. Document pattern for adding new domain-specific sections

**Story 11-8: Dashboard Generation During Import**

1. Implement `generate_dashboards()` method in `capsule/core/importer.py`
2. Integrate dashboard generation into import workflow (after file copy, before merge)
3. Implement dashboard merge logic (section-level merge for capsule dashboard updates)
4. Include dashboard files in import preview
5. Test dashboard generation failure rollback (ensure transactional behavior)

## Traceability Mapping

| Acceptance Criteria | Spec Section | Component/API | Test Strategy |
|---------------------|--------------|---------------|---------------|
| **AC1: Master Dashboard Filtering** | Detailed Design → APIs → `build_metadata_filter_query()` | `capsule/templates/master-dashboard.md.j2` | E2E test: Import capsules with different metadata, verify filters |
| **AC2: Capsule Dashboard Accuracy** | Detailed Design → Data Models → Capsule Dashboard Schema | `capsule/templates/capsule-dashboard.md.j2` | Integration test: Generate dashboard, verify queries return correct counts |
| **AC3: Heading Extraction** | Detailed Design → APIs → `build_heading_extraction_query()` | `capsule/utils/dataview_queries.py` | Unit test: Mock notes with headings, verify extraction function |
| **AC4: Import Integration** | Detailed Design → Workflows → Dashboard Generation Workflow | `capsule/core/importer.py → generate_dashboards()` | E2E test: Run import, verify dashboards created, preview shows dashboards |
| **AC5: Query Performance** | NFR → Performance | Dataview queries in dashboard templates | Performance test: Benchmark with 100, 500 note capsules |
| **AC6: Graceful Degradation** | NFR → Reliability → Dataview Plugin Missing | Dashboard frontmatter + query code blocks | Manual test: Disable Dataview, verify readability |
| **Story 11-0 AC1: DQL Documentation** | Dependencies → Obsidian Plugin Dependencies → Dataview | Technical spike report | Manual validation: Review spike documentation completeness |
| **Story 11-0 AC2: DataviewJS Documentation** | Dependencies → Obsidian Plugin Dependencies → DataviewJS | Technical spike report | Manual validation: Review spike documentation completeness |
| **Story 11-0 AC3: PoC Examples** | Detailed Design → Workflows → Query Workflows | Spike PoC file | Manual test: Execute PoC queries in Obsidian vault |
| **Story 11-0 AC4: Limitations Documented** | NFR → Performance + Reliability | Spike report | Manual validation: Review performance and limitation notes |
| **Story 11-0 AC5: Recommendation** | Detailed Design → Services → Query Pattern Selection | Spike report | Manual validation: Review recommendation rationale |
| **Story 11-1 AC1: Required Fields** | Data Models → Capsule Dashboard Schema | `capsule/models/cypher.py` | Unit test: Validate schema with required fields |
| **Story 11-1 AC2: Optional Metadata** | Data Models → Dashboard Metadata | `capsule/models/cypher.py` | Unit test: Validate schema with optional metadata |
| **Story 11-1 AC3: Cypher Extension** | Data Models → Capsule Cypher Extension | `capsule/models/cypher.py` | Unit test: Load cypher with dashboard_metadata |
| **Story 11-1 AC4: Documentation** | All Sections | Architecture doc, query library | Manual validation: Review documentation completeness |
| **Story 11-1 AC5: Test Fixtures** | Test Strategy | `tests/fixtures/` | Unit test: Load fixtures, verify valid schema |
| **Story 11-2 AC1: Template Creation** | Services → Template Files → master-dashboard.md.j2 | Template file | Manual test: Render template, verify output |
| **Story 11-2 AC2: Filter Queries** | APIs → Metadata Filter Query | `capsule/utils/dataview_queries.py` | Unit test: Generate filter query, verify WHERE clauses |
| **Story 11-2 AC3: Aggregation Queries** | Workflows → Master Dashboard Query Workflow | `capsule/templates/master-dashboard.md.j2` | E2E test: Import capsules, verify aggregations correct |
| **Story 11-2 AC4: Cross-Capsule Queries** | Data Models → Notes with Multiple Capsules | Dashboard template queries | Integration test: Create note in 2 capsules, verify query |
| **Story 11-2 AC5: First Import Generation** | Workflows → Dashboard Generation Workflow | `capsule/core/importer.py` | E2E test: Import first capsule, verify master dashboard created |
| **Story 11-3 AC1: Template Creation** | Services → Template Files → capsule-dashboard.md.j2 | Template file | Manual test: Render template, verify output |
| **Story 11-3 AC2: Overview Section** | Data Models → Dashboard Frontmatter | Template rendering | Integration test: Render template, verify metadata display |
| **Story 11-3 AC3: Root Notes Query** | APIs → File List Query | `capsule/utils/dataview_queries.py` | Unit test: Generate query, verify WHERE clause |
| **Story 11-3 AC4: Study Materials Query** | APIs → File List Query with Type Filter | Query pattern library | E2E test: Import capsule with study materials, verify query |
| **Story 11-3 AC5: Recent Activity Query** | Workflows → Capsule Dashboard Navigation | Dashboard template | E2E test: Update note, verify appears in recent activity |
| **Story 11-4 AC1: Timeline Query** | Dependencies → TaskNotes Integration | Dashboard template | E2E test: Import sequenced capsule, verify timeline section |
| **Story 11-4 AC2: Progress Calculation** | APIs → DataviewJS Progress Query | `capsule/utils/dataview_queries.py` | Unit test: Mock tasks, verify percentage calculation |
| **Story 11-4 AC3: Progress Display** | Workflows → Dashboard Navigation | Capsule dashboard template | Integration test: Render dashboard, verify progress shown |
| **Story 11-4 AC4: Freeform Handling** | Workflows → Conditional Rendering | Template Jinja2 if-block | E2E test: Import freeform capsule, verify no timeline section |
| **Story 11-4 AC5: Capsule Type Testing** | Test Strategy | Test suite | E2E test: Import both capsule types, verify correct rendering |
| **Story 11-5 AC1: Utility Module** | Services → New Utility Module | `capsule/utils/dataview_queries.py` | Unit test: Import module, verify functions exist |
| **Story 11-5 AC2: File List Function** | APIs → `build_file_list_query()` | Query builder function | Unit test: Call function, verify query string format |
| **Story 11-5 AC3: Filter Function** | APIs → `build_metadata_filter_query()` | Query builder function | Unit test: Pass filters, verify WHERE clauses generated |
| **Story 11-5 AC4: Heading Extraction Function** | APIs → `build_heading_extraction_query()` | Query builder function | Unit test: Call function, verify DataviewJS code |
| **Story 11-5 AC5: Documentation** | All Sections | Query pattern library doc | Manual validation: Review examples and performance notes |
| **Story 11-6 AC1: Extraction Function** | APIs → Heading Extraction | DataviewJS function | Unit test: Mock note content, verify heading extracted |
| **Story 11-6 AC2: Filtered View Example** | Workflows → Heading Extraction Workflow | Example dashboard file | Manual test: Create formulas, verify ingredients aggregation |
| **Story 11-6 AC3: Performance Testing** | NFR → Performance → DataviewJS | Benchmark tests | Performance test: Measure extraction time with varying counts |
| **Story 11-6 AC4: Performance Documentation** | NFR → Performance → Performance Warnings | Query comments in templates | Manual validation: Review performance notes in queries |
| **Story 11-6 AC5: Performance Warnings** | NFR → Performance → Degradation Handling | Dashboard template comments | Manual test: Verify warning comments in queries |
| **Story 11-7 AC1: TCM Domain Sections** | Services → Domain-Specific Templates | Domain template files | E2E test: Import TCM capsule, verify domain sections |
| **Story 11-7 AC2: Rendering Logic** | APIs → Domain Section Loading | `capsule/core/importer.py` | Integration test: Load domain template, verify rendering |
| **Story 11-7 AC3: Template Integration** | Services → Template Files → capsule-dashboard.md.j2 | Template Jinja2 include | Unit test: Render with domain sections, verify output |
| **Story 11-7 AC4: TCM Testing** | Test Strategy | Existing TCM vault | E2E test: Import TCM capsule from existing vault |
| **Story 11-7 AC5: Extension Documentation** | All Sections | Developer documentation | Manual validation: Review domain extension guide |
| **Story 11-8 AC1: Generate Method** | Services → Modified Modules → importer.py | `generate_dashboards()` method | Unit test: Call method, verify dashboard files created |
| **Story 11-8 AC2: Workflow Integration** | Workflows → Dashboard Generation Workflow | Import workflow sequence | E2E test: Run import, verify dashboard generation timing |
| **Story 11-8 AC3: Merge Logic** | Dependencies → Epic 8 Integration | `capsule/core/merger.py` | Integration test: Update capsule, verify dashboard merged |
| **Story 11-8 AC4: Preview Inclusion** | Services → Import Preview | Import command output | E2E test: Run import preview, verify dashboards listed |
| **Story 11-8 AC5: Failure Rollback** | NFR → Reliability → Dashboard Generation Failure | Import transaction | Integration test: Force dashboard failure, verify rollback |

## Risks, Assumptions, Open Questions

### Risks

**RISK-1: DataviewJS Performance Degrades with Large Vaults**
- **Impact**: High (affects user experience)
- **Probability**: Medium (depends on user vault size)
- **Mitigation**: 
  - Story 11-0 spike measures performance with realistic data
  - Document query complexity limits (e.g., <100 notes for heading extraction)
  - Add performance warnings in dashboard comments
  - Provide optimization tips in documentation
- **Contingency**: If performance unacceptable, fall back to simpler Dataview queries (no heading extraction)

**RISK-2: Dataview Plugin Not Installed**
- **Impact**: Medium (dashboards non-functional but readable)
- **Probability**: Low (Dataview is popular plugin)
- **Mitigation**: 
  - Implement graceful degradation (queries as code blocks)
  - Add plugin requirement notice in dashboard headers
  - Document Dataview installation in user guide
- **Contingency**: OCDS can detect plugin absence and warn during import (future enhancement)

**RISK-3: Template Rendering Errors Block Imports**
- **Impact**: High (import failure frustrates users)
- **Probability**: Low (templates well-tested)
- **Mitigation**: 
  - Comprehensive template testing in Story 11-2, 11-3
  - Error handling with detailed logs
  - Rollback on dashboard generation failure
- **Contingency**: Add `--skip-dashboards` flag to import command (future enhancement)

**RISK-4: Heading Extraction Fails with Complex Markdown**
- **Impact**: Medium (filtered views show incomplete data)
- **Probability**: Medium (Markdown syntax varies)
- **Mitigation**: 
  - Use robust Markdown parser for heading detection
  - Test with various heading styles (#, ##, ATX, Setext)
  - Document supported Markdown syntax
- **Contingency**: Provide regex-based fallback if parser fails

**RISK-5: Dashboard Merge Conflicts During Updates**
- **Impact**: Low (dashboards can be regenerated)
- **Probability**: Low (dashboards follow merge rules)
- **Mitigation**: 
  - Dashboard frontmatter merges like note frontmatter (section-level)
  - User content in dashboard body preserved
  - Regeneration option if frontmatter corrupted
- **Contingency**: Offer "regenerate dashboard" command (future enhancement)

### Assumptions

**ASSUMPTION-1**: Users have Dataview plugin installed
- **Validation**: Document plugin requirement in README and import output
- **Impact if False**: Dashboards remain readable but non-functional (graceful degradation)

**ASSUMPTION-2**: Capsule cypher contains valid dashboard metadata
- **Validation**: Schema validation in Story 11-1
- **Impact if False**: Dashboard generation skips invalid metadata, logs warning

**ASSUMPTION-3**: Vault contains <50 capsules (master dashboard performance)
- **Validation**: Story 11-0 spike tests with realistic capsule counts
- **Impact if False**: Master dashboard queries may slow down (still functional)

**ASSUMPTION-4**: Users accept utilitarian dashboard design (Epic 11 scope)
- **Validation**: Epic 10 retrospective explicitly split visual polish into Epic 12
- **Impact if False**: User expectations managed via documentation

**ASSUMPTION-5**: Dataview API remains stable across versions
- **Validation**: Document tested Dataview version (v0.5.0+)
- **Impact if False**: Query syntax may need updates for newer Dataview versions

**ASSUMPTION-6**: Users do not manually edit dashboard frontmatter extensively
- **Validation**: Document dashboard frontmatter as system-managed
- **Impact if False**: User edits may be overwritten during capsule updates (documented behavior)

### Open Questions

**QUESTION-1**: Should master dashboard be vault-global or capsule-specific?
- **Current Decision**: Vault-global (single `Master Dashboard.md` at vault root)
- **Rationale**: Provides central navigation hub for all capsules
- **Alternative**: Per-domain master dashboards (e.g., `TCM Master Dashboard.md`)
- **Resolution**: Defer per-domain dashboards to Epic 12 (user customization)

**QUESTION-2**: How to handle master dashboard updates from multiple imports?
- **Current Decision**: Master dashboard queries dynamically (no stored state), so concurrent imports don't conflict
- **Rationale**: Dataview queries scan vault at runtime, no need to update master dashboard content
- **Alternative**: Append capsule links to master dashboard (requires merge logic)
- **Resolution**: Dynamic queries preferred (simpler, no merge conflicts)

**QUESTION-3**: Should dashboard generation be optional during import?
- **Current Decision**: Dashboard generation always enabled (no flag to disable)
- **Rationale**: Dashboards are core navigation feature, minimal overhead
- **Alternative**: Add `--skip-dashboards` flag for users who don't want them
- **Resolution**: Implement always-on for v1.0, add flag in v1.5 if user feedback requests it

**QUESTION-4**: How to handle capsules without dashboard metadata?
- **Current Decision**: Dashboard generates with empty metadata (queries still work)
- **Rationale**: Metadata is optional (for filtering), core dashboard functionality doesn't require it
- **Alternative**: Require metadata or skip dashboard generation
- **Resolution**: Optional metadata (more flexible)

**QUESTION-5**: Should DataviewJS heading extraction be cached?
- **Current Decision**: No caching in v1.0 (Dataview handles query optimization)
- **Rationale**: Premature optimization, Dataview has built-in caching
- **Alternative**: Implement custom cache for extracted headings
- **Resolution**: Rely on Dataview caching, monitor performance in Story 11-0

**QUESTION-6**: How to handle dashboards for deleted capsules?
- **Current Decision**: Deferred to future enhancement (no auto-cleanup in v1.0)
- **Rationale**: Capsule deletion workflow not yet defined
- **Alternative**: Implement `capsule uninstall` command that removes dashboards
- **Resolution**: Document manual deletion process for v1.0, automate in future epic

### Decision Log

| Decision | Date | Rationale | Status |
|----------|------|-----------|--------|
| Split dashboard work into Epic 11 (function) and Epic 12 (polish) | 2025-11-22 | Separate skill sets, reduce risk, phased delivery | Accepted |
| Use Jinja2 templates for dashboard generation | 2025-11-22 | Leverage existing template infrastructure (Epic 4) | Accepted |
| Generate dashboards at import time (not dynamically) | 2025-11-22 | Consistent with capsule philosophy (static files) | Accepted |
| Master dashboard uses dynamic queries (no stored state) | 2025-11-22 | Avoid merge conflicts, simplify updates | Accepted |
| Dashboard metadata is optional in capsule cypher | 2025-11-22 | Flexibility for simple capsules | Accepted |
| DataviewJS heading extraction for advanced filtering | 2025-11-22 | Required for study aggregation features | Pending validation (Story 11-0) |

## Test Strategy Summary

### Test Levels

**Unit Tests** (80% of test coverage target)

- **`capsule/utils/dataview_queries.py`**: Query builder functions
  - Test `build_file_list_query()` with various filters
  - Test `build_metadata_filter_query()` with multiple filter combinations
  - Test `build_heading_extraction_query()` with edge cases
  - Mock query execution, verify generated query strings

- **`capsule/core/importer.py`**: Dashboard generation method
  - Test `generate_dashboards()` with mock Capsule model
  - Test template loading and rendering
  - Test file write operations with mock filesystem
  - Test error handling (template not found, write failure)

- **`capsule/models/cypher.py`**: Dashboard metadata schema
  - Test cypher loading with dashboard_metadata section
  - Test schema validation (required vs optional fields)
  - Test missing metadata (graceful handling)

**Integration Tests** (15% of test coverage target)

- **Dashboard Template Rendering**
  - Load real templates, render with sample capsule data
  - Verify output Markdown structure and query syntax
  - Test with various capsule types (freeform, sequenced)

- **Import Workflow Integration**
  - Import test capsule, verify dashboards created
  - Verify dashboard files in correct locations
  - Verify dashboard frontmatter matches capsule metadata
  - Test dashboard merge on capsule update

- **Query Pattern Library**
  - Execute query builder functions, verify output queries
  - Validate query syntax (Dataview/DataviewJS)
  - Test query patterns with sample vault data

**E2E Tests** (5% of test coverage target)

- **Full Import with Dashboard Generation**
  - Execute `capsule import TCM_Test_v1.capsule`
  - Verify dashboards appear in vault
  - Open dashboards in test Obsidian instance
  - Verify queries execute (with Dataview enabled)
  - Verify graceful degradation (with Dataview disabled)

- **Master Dashboard Filtering**
  - Import 3+ capsules with different metadata
  - Open master dashboard in Obsidian
  - Verify all capsules listed
  - Test metadata filters (class, topic, category, active)

- **Capsule Dashboard Navigation**
  - Open capsule dashboard in Obsidian
  - Click navigation links (root notes, study materials)
  - Verify links open correct files
  - Verify file counts accurate

- **Heading Extraction Performance**
  - Create capsule with 10, 50, 100 notes with headings
  - Execute heading extraction query
  - Measure query execution time
  - Verify extracted content displayed correctly

### Test Coverage by Story

| Story | Unit Tests | Integration Tests | E2E Tests | Manual Tests |
|-------|-----------|-------------------|-----------|--------------|
| 11-0 | N/A | N/A | N/A | Performance benchmarks, query validation |
| 11-1 | Schema validation | Cypher loading with metadata | N/A | Schema documentation review |
| 11-2 | Query builder | Template rendering | Master dashboard in Obsidian | Filter combinations |
| 11-3 | Query builder | Template rendering | Capsule dashboard in Obsidian | Navigation links |
| 11-4 | Progress calculation | Timeline rendering | Sequenced capsule import | TaskNotes integration |
| 11-5 | All query builder functions | Query pattern execution | N/A | Documentation review |
| 11-6 | Heading extraction function | Filtered view rendering | Heading extraction performance | Complex Markdown |
| 11-7 | Domain section loading | TCM template rendering | TCM capsule import | Domain-specific queries |
| 11-8 | `generate_dashboards()` method | Import workflow integration | Full import E2E | Failure rollback |

### Edge Cases to Test

1. **Capsule without dashboard metadata** (optional metadata)
2. **First capsule import** (master dashboard creation)
3. **Capsule update** (dashboard merge)
4. **Capsule with 500+ notes** (query performance)
5. **Dataview plugin disabled** (graceful degradation)
6. **Dashboard frontmatter manually edited** (merge behavior)
7. **Heading extraction with no matching headings** (empty results)
8. **Concurrent capsule imports** (master dashboard race condition)
9. **Dashboard generation failure** (rollback behavior)
10. **Special characters in capsule metadata** (Jinja2 escaping)

### Performance Benchmarks (Story 11-0 Spike)

| Scenario | Target | Measurement Method |
|----------|--------|-------------------|
| Master dashboard load (10 capsules) | <1 second | Dataview query execution time in Obsidian |
| Master dashboard load (50 capsules) | <2 seconds | Dataview query execution time in Obsidian |
| Capsule dashboard load (100 notes) | <1 second | Dataview query execution time in Obsidian |
| Heading extraction (10 notes) | <1 second | DataviewJS query execution time |
| Heading extraction (50 notes) | <3 seconds | DataviewJS query execution time |
| Heading extraction (100 notes) | <5 seconds | DataviewJS query execution time |
| Dashboard generation (import) | <3 seconds | Python execution time (logged) |

### Test Data Requirements

**Test Capsules:**

1. **TCM_Test_Freeform_v1** - Freeform capsule, 10 root notes, 5 study materials
2. **TCM_Test_Sequenced_v1** - Sequenced capsule, 20 root notes, 10 study materials, timeline data
3. **TCM_Test_Large_v1** - Large capsule, 100+ root notes (performance testing)
4. **Culinary_Test_v1** - Different domain, for cross-capsule testing

**Test Vault Structure:**

```
test_vault/
├── Master Dashboard.md (generated during tests)
├── TCM_Test_Freeform_v1/
│   ├── capsule-dashboard.md
│   ├── capsule-cypher.yaml
│   └── root_notes/ (10 notes)
├── TCM_Test_Sequenced_v1/
│   ├── capsule-dashboard.md
│   ├── capsule-cypher.yaml
│   └── root_notes/ (20 notes with timeline tasks)
└── shared_note.md (belongs to both capsules for cross-capsule testing)
```

### Regression Testing

**Critical Paths to Verify:**

1. **Import workflow** (Epics 7-10) - Verify dashboards don't break existing import logic
2. **Merge strategies** (Epic 8) - Verify dashboard merge follows section-level rules
3. **Validation** (Epic 5) - Verify dashboards included in validation reports
4. **Export** (Epic 7) - Verify dashboards included in exported capsules

**Regression Test Suite** (runs before Epic 11 completion):

- Import TCM capsule (existing fixture from previous epics)
- Verify existing functionality unaffected
- Verify new dashboard files present
- Verify no errors in logs

### Acceptance Testing

**User Acceptance Criteria** (manual testing by Product Owner):

1. Open master dashboard, verify intuitive layout and working filters
2. Open capsule dashboard, verify accurate file counts and navigation
3. Click filtered content view, verify heading extraction works
4. Import capsule update, verify dashboard updates correctly
5. Disable Dataview, verify dashboards still readable

**Success Criteria:**

- All epic-level ACs pass
- All story-level ACs pass
- No regressions in existing functionality
- Performance targets met (validated in Story 11-0)
- User feedback: "Dashboards are functional and useful" (Epic 11 goal)

---
# Post-Review Follow-ups

- **Story 11.6**: Consider moving complex Javascript snippets from Python strings to separate .js files for better maintainability.
- **Story 11.8**: Update `capsule/core/merger.py` to include `dashboard_metadata`, `capsule_id`, `version`, `created`, `updated` in `section_level_merge` (or add specific dashboard merge logic) (AC #3).
- **Story 11.8**: Add a test case in `tests/test_core/test_dashboard_generation.py` that specifically verifies `dashboard_metadata` is updated when merging an existing dashboard (AC #3).


