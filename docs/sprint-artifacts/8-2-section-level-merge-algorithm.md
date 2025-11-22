# Story 8.2: section-level-merge-algorithm

Status: done

## Story

As a developer, I want to implement the section-level merge strategy, so that capsule updates can be applied safely without losing data from other sections.

## Requirements Context Summary

This story focuses on implementing the `section_level_merge` function, a critical component of the capsule import process. The primary goal is to allow for safe updates of existing notes from a newer version of the same capsule.

**Source Documents:**
- `docs/epics.md`
- `docs/architecture.md`

**Key Requirements:**
- The implementation must follow the algorithm outlined in the architecture document.
- The function should be placed in `capsule/core/merger.py`.
- The merge logic must only apply when the incoming note is from the same capsule as the existing note.
- The function must update sections present in the incoming frontmatter and preserve all other sections.

## Structure Alignment Summary

- **New Module:** The core logic for this story will be implemented in `capsule/core/merger.py`, which is consistent with the project architecture.
- **Dependency:** The implementation will depend on the `FrontmatterHandler` class from `capsule/utils/frontmatter.py`, which was created in the previous story (8-1).
- **Testing:** Unit tests should be created in `tests/test_core/test_merger.py`, mirroring the project structure.

## Acceptance Criteria

1. A function `section_level_merge(existing: dict, incoming: dict) -> dict` is implemented in `capsule/core/merger.py`.
2. The function correctly updates existing sections in the frontmatter with values from the incoming frontmatter.
3. The function preserves sections that are present in the existing frontmatter but not in the incoming frontmatter.
4. The function is covered by unit tests with various scenarios, including updating existing keys, adding new keys to a section, and preserving other sections.

## Tasks / Subtasks

- [x] **Task 1: Implement `section_level_merge` function** (AC: #1)
  - [x] Subtask 1.1: Create the file `capsule/core/merger.py` if it doesn't exist.
  - [x] Subtask 1.2: Implement the `section_level_merge` function with the specified signature.
- [x] **Task 2: Implement Merge Logic** (AC: #2, #3)
  - [x] Subtask 2.1: Implement the logic to update existing sections.
  - [x] Subtask 2.2: Implement the logic to preserve other sections.
- [x] **Task 3: Add Unit Test Coverage** (AC: #4)
  - [x] Subtask 3.1: Create the file `tests/test_core/test_merger.py`.
  - [x] Subtask 3.2: Write unit tests for the `section_level_merge` function, covering all scenarios.

## Dev Notes

- **Architecture:** This story implements a critical pattern defined in the architecture document for handling capsule updates. [Source: docs/architecture.md#Merge-Algorithm-(Critical-Implementation-Pattern)]
- **Dependencies:** This implementation will rely on the `FrontmatterHandler` from `capsule/utils/frontmatter.py` to read and write notes safely.
- **Testing:** It is crucial to test against a variety of frontmatter structures to ensure the merge is robust.

### Learnings from Previous Story

**From Story 8-1-frontmatter-parser-utilities (Status: done)**

- **New Service Created**: `FrontmatterHandler` class is available at `capsule/utils/frontmatter.py` - use this for all frontmatter parsing.
- **Dependency Added**: `ruamel.yaml` was added to `pyproject.toml` and is available for use.
- **Testing Pattern**: The previous story established a testing pattern with fixtures for sample notes (`tests/fixtures/sample_notes/`). This pattern should be continued.
- **Technical Debt**: A deprecated `_cleanup()` method was noted in `capsule/core/importer.py`. This is not directly related but good to be aware of. (Update: Resolved in Prep Sprint 2025-11-21)

[Source: docs/sprint-artifacts/8-1-frontmatter-parser-utilities.md#Dev-Agent-Record]

## Dev Agent Record

### Context Reference

- `docs/sprint-artifacts/stories/8-2-section-level-merge-algorithm.context.xml`

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

- Implemented `section_level_merge` function in `capsule/core/merger.py`.
- Created unit tests in `tests/test_core/test_merger.py` covering all acceptance criteria.
- Verified that domain sections are replaced, universal fields are updated, and other sections are preserved.

### File List

- capsule/core/merger.py
- tests/test_core/test_merger.py

## Change Log

- 2025-11-21: Story created by BMad.
- 2025-11-21: Implemented section-level merge algorithm and tests.
- 2025-11-21: Senior Developer Review notes appended.

# Senior Developer Review (AI)

- **Reviewer**: BMad
- **Date**: 2025-11-21
- **Outcome**: Approve

## Summary

The implementation of the `section_level_merge` function is excellent. It is clean, correct, and well-tested. The code adheres to the architecture and best practices outlined in the project documentation.

## Key Findings

No findings.

## Acceptance Criteria Coverage

| AC# | Description | Status | Evidence |
| :-- | :--- | :--- | :--- |
| 1 | A function `section_level_merge(existing: dict, incoming: dict) -> dict` is implemented in `capsule/core/merger.py`. | IMPLEMENTED | `capsule/core/merger.py:4` |
| 2 | The function correctly updates existing sections in the frontmatter with values from the incoming frontmatter. | IMPLEMENTED | `tests/test_core/test_merger.py:8` (`test_updates_domain_section`), `tests/test_core/test_merger.py:34` (`test_updates_universal_fields`) |
| 3 | The function preserves sections that are present in the existing frontmatter but not in the incoming frontmatter. | IMPLEMENTED | `tests/test_core/test_merger.py:24` (`test_preserves_other_sections`) |
| 4 | The function is covered by unit tests with various scenarios, including updating existing keys, adding new keys to a section, and preserving other sections. | IMPLEMENTED | `tests/test_core/test_merger.py` contains 6 tests covering various scenarios. |

**Summary**: 4 of 4 acceptance criteria fully implemented.

## Task Completion Validation

| Task | Marked As | Verified As | Evidence |
| :--- | :--- | :--- | :--- |
| **Task 1: Implement `section_level_merge` function** | [x] | VERIFIED COMPLETE | `capsule/core/merger.py` exists and contains the function. |
| Subtask 1.1: Create the file `capsule/core/merger.py` if it doesn't exist. | [x] | VERIFIED COMPLETE | The file `capsule/core/merger.py` exists. |
| Subtask 1.2: Implement the `section_level_merge` function with the specified signature. | [x] | VERIFIED COMPLETE | The function `section_level_merge` exists in `capsule/core/merger.py` with the correct signature. |
| **Task 2: Implement Merge Logic** | [x] | VERIFIED COMPLETE | The logic in `section_level_merge` correctly updates and preserves sections. |
| Subtask 2.1: Implement the logic to update existing sections. | [x] | VERIFIED COMPLETE | The loop in `section_level_merge` iterates through incoming items and updates `merged` dictionary. |
| Subtask 2.2: Implement the logic to preserve other sections. | [x] | VERIFIED COMPLETE | The function initializes `merged` with a copy of `existing`, preserving all sections not in `incoming`. |
| **Task 3: Add Unit Test Coverage** | [x] | VERIFIED COMPLETE | `tests/test_core/test_merger.py` exists and contains relevant tests. |
| Subtask 3.1: Create the file `tests/test_core/test_merger.py`. | [x] | VERIFIED COMPLETE | The file `tests/test_core/test_merger.py` exists. |
| Subtask 3.2: Write unit tests for the `section_level_merge` function, covering all scenarios. | [x] | VERIFIED COMPLETE | The test file contains 6 tests covering various scenarios. |

**Summary**: 8 of 8 completed tasks verified.

## Test Coverage and Gaps

Test coverage is excellent. All acceptance criteria are covered by unit tests, and edge cases are considered.

## Architectural Alignment

The implementation is fully aligned with the architecture document, including the pseudo-code for the merge algorithm.

## Security Notes

No security concerns.

## Best-Practices and References

The code adheres to the project's best practices.

## Action Items

No action items.





