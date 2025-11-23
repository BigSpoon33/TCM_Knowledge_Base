# Story 11.7: domain-specific-dashboard-sections

Status: review

## Story

As a user of a TCM capsule,
I want to see domain-specific sections on my capsule dashboard, such as lists of formulas, herbs, and patterns,
so that I can quickly navigate to the most relevant content for my studies.

## Acceptance Criteria

1.  Implement domain-specific sections for TCM capsules (formulas, herbs, patterns).
2.  Create domain section rendering logic (load from domain templates).
3.  Integrate domain sections into capsule dashboard template.
4.  Test with TCM capsule (existing vault data).
5.  Document pattern for adding new domain-specific sections.

## Tasks / Subtasks

- [x] Task 1: Implement Domain Section Rendering Logic (AC: #2)
  - [x] Subtask 1.1: In `capsule/core/importer.py`, create a function `load_domain_sections(domain_type)` that loads a domain-specific template.
  - [x] Subtask 1.2: Create a new directory `capsule/templates/domains/` for domain-specific templates.
  - [x] Subtask 1.3: Create a template file `capsule/templates/domains/tcm.md.j2` for the TCM domain.
- [x] Task 2: Implement TCM Domain Sections (AC: #1)
  - [x] Subtask 2.1: In `capsule/templates/domains/tcm.md.j2`, add Dataview queries to list formulas, herbs, and patterns.
  - [x] Subtask 2.2: Use the `dataview_queries.py` utility to build the queries.
- [x] Task 3: Integrate Domain Sections into Dashboard (AC: #3)
  - [x] Subtask 3.1: In `capsule/core/importer.py`, modify the `generate_dashboards` function to call `load_domain_sections` and pass the rendered content to the capsule dashboard template.
  - [x] Subtask 3.2: In `capsule/templates/capsule-dashboard.md.j2`, add a placeholder for the domain-specific sections.
- [x] Task 4: Testing and Documentation (AC: #4, #5)
  - [x] Subtask 4.1: Create a test that imports a TCM capsule and verifies that the domain-specific sections are present in the generated dashboard.
  - [x] Subtask 4.2: Create a guide in `docs/guides/` explaining how to add new domain-specific dashboard sections.

## Dev Notes

### Learnings from Previous Story

**From Story 11-6-advanced-filtering-heading-extraction (Status: done)**

- **New Service Created**: `capsule/utils/dataview_queries.py` with functions to build Dataview and DataviewJS queries. This will be useful for creating the domain-specific sections.
- **Architectural Change**: Use a hybrid DQL/DataviewJS approach and optimize queries for performance.
- **New Files Created**:
    - `docs/guides/filtered_view_example.md`
    - `tests/fixtures/sample_notes/formula_1.md`
    - `tests/fixtures/sample_notes/formula_2.md`
    - `tests/performance/test_heading_extraction_perf.py`
- **Files Modified**:
    - `capsule/utils/dataview_queries.py`
    - `tests/test_utils/test_dataview_queries.py`
    - `docs/guides/dataview_query_library.md`

[Source: docs/sprint-artifacts/11-6-advanced-filtering-heading-extraction.md#Dev-Agent-Record]

### References

- [Source: docs/sprint-artifacts/tech-spec-epic-11.md]
- [Source: docs/epics.md]
- [Source: docs/architecture.md]

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->
- docs/sprint-artifacts/stories/11-7-domain-specific-dashboard-sections.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

- Implemented `generate_dashboards` and `load_domain_sections` in `capsule/core/importer.py`.
- Created `capsule/templates/domains/tcm.md.j2` with Dataview queries for TCM domain.
- Added `docs/guides/domain_specific_dashboard_sections.md` documentation.
- Added tests in `tests/test_core/test_dashboard_generation.py`.
- Updated `capsule/core/importer.py` to support dynamic domain template loading.

### File List

- capsule/core/importer.py
- capsule/templates/domains/tcm.md.j2
- docs/guides/domain_specific_dashboard_sections.md
- tests/test_core/test_dashboard_generation.py

---
# Senior Developer Review (AI)
- Reviewer: BMad
- Date: 2025-11-22
- Outcome: Approve
- Summary: The implementation is correct and complete according to the acceptance criteria and tasks. The code is well-written, tested, and documented.
- Key Findings: None
- Acceptance Criteria Coverage: 5 of 5 acceptance criteria fully implemented.
- Task Completion Validation: 9 of 9 completed tasks verified.
- Test Coverage and Gaps: The new functionality is well-tested.
- Architectural Alignment: The implementation aligns with the tech spec for Epic 11.
- Security Notes: No security issues found.
- Best-Practices and References: The code follows modern Python best practices.
- Action Items: None

