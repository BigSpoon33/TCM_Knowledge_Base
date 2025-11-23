# Story 11.5: dataview-query-pattern-library

Status: review

## Story

As a developer,
I want a documented library of standard query patterns for dashboard development,
so that I can build consistent and performant dashboards without re-inventing common queries.

## Acceptance Criteria

1. Create `capsule/utils/dataview_queries.py` utility module.
2. Implement `build_file_list_query()` function.
3. Implement `build_metadata_filter_query()` function.
4. Implement `build_heading_extraction_query()` function.
5. Document query patterns with examples and performance notes.

## Tasks / Subtasks

- [x] Task 1: Create `dataview_queries.py` module (AC: #1)
    - [x] Subtask 1.1: Create the file `capsule/utils/dataview_queries.py`.
    - [x] Subtask 1.2: Create the test file `tests/test_utils/test_dataview_queries.py`.
- [x] Task 2: Implement `build_file_list_query` (AC: #2)
    - [x] Subtask 2.1: Implement the function in the module.
    - [x] Subtask 2.2: Add unit tests for the function.
- [x] Task 3: Implement `build_metadata_filter_query` (AC: #3)
    - [x] Subtask 3.1: Implement the function in the module.
    - [x] Subtask 3.2: Add unit tests for the function.
- [x] Task 4: Implement `build_heading_extraction_query` (AC: #4)
    - [x] Subtask 4.1: Implement the function in the module.
    - [x] Subtask 4.2: Add unit tests for the function.
- [x] Task 5: Document query patterns (AC: #5)
    - [x] Subtask 5.1: Add docstrings to the functions with examples.
    - [x] Subtask 5.2: Add a section to the developer documentation about the query pattern library.

## Dev Notes

### Requirements Context Summary

This story implements the creation of a utility module, `capsule/utils/dataview_queries.py`, to house a library of standard Dataview and DataviewJS query patterns. The requirements are derived from the "Epic 11: Dashboard Functionality (Core/Data Layer)" technical specification. The module will include functions to build queries for file lists, metadata filtering, and heading extraction. The acceptance criteria also require documentation for these patterns, including examples and performance notes.

The architecture specifies that dashboards are static Markdown files with dynamic queries, and this library will provide a consistent way to generate those queries. The new module will be tested with unit tests.

### Project Structure Alignment and Lessons Learned

*   **Previous Story Learnings:**
    *   The previous story (11-4) modified the dashboard template to include progress tracking. This story will not modify the template, but the queries created will be used in it.
    *   The architectural decision to use a hybrid DQL/DataviewJS approach and to optimize queries for performance is directly relevant to this story. The query pattern library should reflect this.
*   **Project Structure Alignment:**
    *   This story will create a new utility module: `capsule/utils/dataview_queries.py`.
    *   A corresponding test file will be created: `tests/test_utils/test_dataview_queries.py`.
    *   This aligns with the existing project structure.

### References

- [Source: docs/sprint-artifacts/tech-spec-epic-11.md#Acceptance-Criteria-Authoritative]
- [Source: docs/architecture.md#Implementation-Patterns-Consistency-Rules]
- [Source: docs/sprint-artifacts/11-4-progress-tracking-tasknotes-integration.md]

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->
- docs/sprint-artifacts/stories/11-5-dataview-query-pattern-library.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

- Implemented `capsule/utils/dataview_queries.py` with functions to build Dataview and DataviewJS queries.
- Added unit tests in `tests/test_utils/test_dataview_queries.py`.
- Created developer documentation in `docs/guides/dataview_query_library.md`.

### File List

- capsule/utils/dataview_queries.py
- tests/test_utils/test_dataview_queries.py
- docs/guides/dataview_query_library.md

## Change Log
- 2025-11-22: Senior Developer Review notes appended.


---
## Senior Developer Review (AI)
- **Reviewer**: BMad
- **Date**: 2025-11-22
- **Outcome**: Approve
- **Summary**: The implementation is excellent. All acceptance criteria have been met, and all tasks marked as complete have been verified. The code is clean, well-documented, and includes appropriate tests. The new `dataview_queries` module is a valuable addition to the project.
- **Key Findings**: None.
- **Acceptance Criteria Coverage**:
    - **AC1: Create `capsule/utils/dataview_queries.py` utility module.** - IMPLEMENTED
    - **AC2: Implement `build_file_list_query()` function.** - IMPLEMENTED
    - **AC3: Implement `build_metadata_filter_query()` function.** - IMPLEMENTED
    - **AC4: Implement `build_heading_extraction_query()` function.** - IMPLEMENTED
    - **AC5: Document query patterns with examples and performance notes.** - IMPLEMENTED
- **Task Completion Validation**:
    - **Task 1: Create `dataview_queries.py` module (AC: #1)** - VERIFIED COMPLETE
    - **Task 2: Implement `build_file_list_query` (AC: #2)** - VERIFIED COMPLETE
    - **Task 3: Implement `build_metadata_filter_query` (AC: #3)** - VERIFIED COMPLETE
    - **Task 4: Implement `build_heading_extraction_query` (AC: #4)** - VERIFIED COMPLETE
    - **Task 5: Document query patterns (AC: #5)** - VERIFIED COMPLETE
- **Action Items**: None.

