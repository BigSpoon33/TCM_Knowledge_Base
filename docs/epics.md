# Project Epics

This document outlines the major epics for the Obsidian_Capsule_Delivery project.

---

## Epic 0: Foundation & Project Setup
**Summary:** Establishes modern Python project structure, dependencies, and development tools.

### Stories
- **0-1-project-scaffolding:** Create the initial project structure using Cookiecutter.
- **0-2-core-dependencies-installation:** Install all necessary core and development dependencies.
- **0-3-ci-cd-pipeline-setup:** Configure GitHub Actions for continuous integration and delivery.
- **0-4-development-tools-configuration:** Set up and configure tools like black, flake8, and mypy.

---

## Epic 1: Core Data Models
**Summary:** Implements fundamental data models for Capsule, Cypher, Note, Template, Config.

### Stories
- **1-1-capsule-model-implementation:** Implement the core `Capsule` data model.
- **1-2-capsule-cypher-model-implementation:** Implement the `CapsuleCypher` model for metadata.
- **1-3-note-model-with-frontmatter:** Implement the `Note` model, including frontmatter handling.
- **1-4-template-schema-model:** Implement the model for defining template schemas.
- **1-5-config-model:** Implement the user configuration model.

---

## Epic 2: Configuration Management
**Summary:** User configuration system, YAML handling, file operations, first-time setup.

### Stories
- **2-1-yaml-handler-with-ruamel:** Implement a YAML handler that preserves comments.
- **2-2-file-operations-utilities:** Create utility functions for safe file operations.
- **2-3-user-config-system:** Develop the system for managing user-specific configurations.
- **2-4-first-time-setup-command:** Create a `capsule init` command for first-time setup.

---

## Epic 3: Deep Research Implementation
**Summary:** AI-powered deep research with Gemini API, citation tracking.

### Stories
- **3-1-research-provider-abstract-base:** Create an abstract base class for research providers.
- **3-2-gemini-research-provider:** Implement a research provider using the Gemini API.
- **3-3-citation-tracking-system:** Develop a system for tracking and managing citations.
- **3-4-research-result-data-model:** Implement a data model for storing research results.

---

## Epic 4: Template System & Content Generation
**Summary:** Jinja2 templates, content generation pipeline, study material creation.

### Stories
- **4-1-jinja2-template-engine-setup:** Set up and configure the Jinja2 template engine.
- **4-2-universal-note-template:** Create a universal Jinja2 template for standard notes.
- **4-3-study-material-templates:** Develop templates for various study materials (flashcards, quizzes).
- **4-4-content-generator-core-logic:** Implement the core logic for the content generator.
- **4-5-template-driven-generation-pipeline:** Build the pipeline that drives content generation from templates.

---

## Epic 5: Validation Engine
**Summary:** Schema validation, file inventory checks, data type validation, reporting.

### Stories
- **5-1-core-validator-implementation:** Implement the core validation engine.
- **5-2-schema-validation-logic:** Add logic for validating against frontmatter schemas.
- **5-3-file-inventory-validation:** Implement validation for file inventories in capsules.
- **5-4-data-type-validation:** Add data type validation for schema fields.
- **5-5-utf8-encoding-validation:** Implement checks for UTF-8 encoding.
- **5-6-validation-report-generation:** Create functionality to generate validation reports.

---

## Epic 6: Capsule Packaging
**Summary:** Cypher generation, file inventory management, export to folder/zip.

### Stories
- **6-1-capsule-packager-core:** Implement the core logic for packaging capsules.
- **6-2-cypher-generation-from-capsule:** Generate `capsule-cypher.yaml` from capsule contents.
- **6-3-file-inventory-management:** Manage the file inventory within the cypher.
- **6-4-export-to-folder-bundle:** Implement functionality to export a capsule as a folder.
- **6-5-export-to-capsule-zip:** Implement functionality to export a capsule as a .zip archive.

---

## Epic 7: Import/Export Operations
**Summary:** Backup management, import/export commands, version conflict detection, preview.

### Stories
- **7-1-backup-management-system:** Create a system for backing up the vault before imports.
- **7-2-capsule-exporter-implementation:** Implement the `capsule export` command.
- **7-3-capsule-importer-with-preview:** Implement the `capsule import` command with a preview feature.
- **7-4-version-conflict-detection:** Add logic to detect version conflicts during import.
- **7-5-import-preview-data-structure:** Design the data structure for the import preview.
- **7-6-interactive-approval-workflow:** Implement an interactive approval step for imports.

---

## Epic 8: Merge Strategies
**Summary:** Section-level merge, additive merge, conflict detection, provenance tracking.

### Stories
- **8-1-frontmatter-parser-utilities:** Create utility functions for parsing frontmatter.
- **8-2-section-level-merge-algorithm:** Implement the section-level merge strategy.
- **8-3-additive-merge-algorithm:** Implement the additive merge strategy.
- **8-4-conflict-detection-logic:** Add logic to detect merge conflicts.
- **8-5-user-content-preservation:** Ensure user content in the note body is always preserved.
- **8-6-provenance-tracking:** Implement provenance tracking in the frontmatter.

### Post-Review Follow-ups
- [ ] **From Story 11-1**: Consider creating a Tech Spec for Epic 11 to formally document the dashboard system's architecture.
- [ ] **From Story 8-6**: Create a Tech Spec for Epic 8 to formally document the merge strategies and their implementation details.


---

## Epic 9: CLI Commands - Generation & Templates
**Summary:** Main CLI app, generate command, template management commands.

### Stories
- **9-1-main-cli-app-typer-setup:** Set up the main Typer application for the CLI.
- **9-2-generate-command-implementation:** Implement the `capsule generate` command.
- **9-3-template-create-command:** Implement the `capsule template create` command.
- **9-4-template-list-command:** Implement the `capsule template list` command.
- **9-5-template-validate-command:** Implement the `capsule template validate` command.

---

## Epic 10: CLI Commands - Validation & Import/Export
**Summary:** Validate, export, import, status, list commands.

### Stories
- **10-1-validate-command-implementation:** Implement the `capsule validate` command.
- **10-2-export-command-implementation:** Implement the `capsule export` command.
- **10-3-import-command-implementation:** Implement the `capsule import` command.
- **10-4-status-command-implementation:** Implement the `capsule status` command.
- **10-5-list-command-implementation:** Implement the `capsule list` command.

---

## Epic 11: Dashboard Functionality (Core/Data Layer)
**Summary:** Hierarchical dashboard system with functional capabilities - get it working.

**Status:** Next epic (ready for planning)
**Decision Date:** 2025-11-22 (Epic 10 Retrospective)
**Background:** Originally planned as single dashboard epic, split into Epic 11 (functionality) and Epic 12 (polish) based on expanded scope and different skill requirements.

### Key Features
- Hierarchical dashboard system (Master → Capsule → Content)
- Capsule dashboard metadata (class, topic, category, active status)
- Master dashboard filtering (query capsules by metadata, combination filters)
- Progress tracking (TaskNotes integration, completion percentage)
- Content navigation (links to root notes, study materials)
- Dataview + DataviewJS query patterns
- Heading extraction from notes (e.g., all #formula notes → #ingredients headings)
- Domain-specific filtered views
- Dashboard generation during capsule import

### Stories (Draft - To Be Finalized)
- **11-0-dataview-dataviewjs-technical-spike:** Research and validate DataviewJS heading extraction feasibility
- **11-1-capsule-dashboard-metadata-schema:** Define capsule dashboard frontmatter fields for filtering
- **11-2-master-dashboard-template-with-filtering:** Create master dashboard with dynamic capsule filtering
- **11-3-capsule-dashboard-template-core-structure:** Create capsule dashboard with metadata, navigation, file counts
- **11-4-progress-tracking-tasknotes-integration:** Add TaskNotes queries and completion percentage tracking
- **11-5-dataview-query-pattern-library:** Document standard query patterns for dashboard development
- **11-6-advanced-filtering-heading-extraction:** Implement DataviewJS heading extraction for study views
- **11-7-domain-specific-dashboard-sections:** Add domain-specific filtered views (e.g., TCM formulas/herbs)
- **11-8-dashboard-generation-during-import:** Auto-generate dashboards when importing capsules

**Quality Bar:** Functional, readable, navigable dashboards (basic but utilitarian - CSS polish deferred to Epic 12)

### References
- [Epic 10 Retrospective](docs/sprint-artifacts/epic-10-retro-2025-11-22.md) - Decision rationale and scope definition
- [Epic 11 Vision: Hierarchical Dashboard System](docs/sprint-artifacts/epic-10-retro-2025-11-22.md#-epic-11-vision-hierarchical-dashboard-system)

---

## Epic 12: Dashboard Polish & Interactivity (Presentation Layer)
**Summary:** Visual design, CSS theming, interactive widgets - make it beautiful.

**Status:** Backlog (depends on Epic 11 completion)
**Created:** 2025-11-22 (Epic 10 Retrospective)
**Background:** Split from original Epic 11 to separate functional implementation from visual design work, which requires different skills and experimentation.

### Key Features
- CSS theming and visual design
- Interactive widgets (Meta-Bind forms/buttons)
- Advanced plugin integrations (Templater, Spaced Repetition)
- Aesthetic improvements (neon themes, custom separators, visual hierarchy)
- UX refinements based on Epic 11 user feedback
- Responsive layout design
- Documentation with visual examples

### Inspiration Sources
- [HOCA-1/neon-homepage-vault](https://github.com/HOCA-1/neon-homepage-vault)
- [rafaelveiga/obsidian-widgets](https://github.com/rafaelveiga/obsidian-widgets)
- [olrenso/obsidian-home-tab](https://github.com/olrenso/obsidian-home-tab)
- [mirnovov/obsidian-homepage](https://github.com/mirnovov/obsidian-homepage)
- [TfTHacker/DashboardPlusPlus](https://github.com/TfTHacker/DashboardPlusPlus)
- [Obsidian Forum: Fancy Horizontal Rules](https://forum.obsidian.md/t/creating-fancy-horizontal-rule-lines/63700/2)
- [Obsidian Forum: Example Workflows](https://forum.obsidian.md/t/example-workflows-in-obsidian/1093)
- [Reddit: Obsidian Dashboard Example](https://www.reddit.com/r/ObsidianMD/comments/1p15k4n/my_obsidian_dashboard/)

### Stories
- TBD (to be defined after Epic 11 completion and user feedback)

---

## Epic 13: Cross-Cutting Concerns & Polish
**Summary:** Error handling, logging, progress indicators, dry-run mode, help docs.

**Note:** Originally numbered Epic 12, renumbered to Epic 13 after dashboard split.

### Stories
- **13-1-error-handling-system:** Implement a consistent error handling system.
- **13-2-logging-system-setup:** Set up a structured logging system.
- **13-3-progress-indicators-rich-integration:** Integrate `rich` for progress indicators.
- **13-4-dry-run-mode-implementation:** Implement a `--dry-run` mode for commands.
- **13-5-help-documentation-and-examples:** Improve help documentation with examples.

---

## Epic 14: Testing Infrastructure
**Summary:** Test framework, unit tests, integration tests, E2E tests, CI integration.

**Note:** Originally numbered Epic 13, renumbered to Epic 14 after dashboard split.

### Stories
- **14-1-pytest-configuration-and-fixtures:** Configure pytest and create necessary fixtures.
- **14-2-unit-tests-for-core-logic:** Write unit tests for the core business logic.
- **14-3-integration-tests-for-commands:** Write integration tests for the CLI commands.
- **14-4-e2e-tests-for-full-workflows:** Write end-to-end tests for complete user workflows.
- **14-5-test-coverage-and-ci-integration:** Integrate test coverage reporting into the CI pipeline.
