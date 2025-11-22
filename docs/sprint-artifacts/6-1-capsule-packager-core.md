# Story 6.1: capsule-packager-core

Status: review

## Story

As a developer,
I want to implement the core logic for packaging capsules,
so that I can prepare capsules for distribution.

## Dev Notes

### Requirements Context Summary

- **Epic:** 6: Capsule Packaging
- **Summary:** Cypher generation, file inventory management, export to folder/zip.
- **Source:** `docs/epics.md`

- **Relevant architecture patterns and constraints:** The implementation must adhere to the architecture's definition of the `packager.py`, `cypher.py`, and `validator.py` components. Specifically, the `CapsulePackager` class should encapsulate the logic for generating the cypher and packaging the capsule, as defined in the architecture document under "Epic Group 3: Capsule Packaging".
- **Testing standards summary:** Unit tests should cover the core packaging logic, including cypher generation and folder bundle creation.


### Project Structure Notes

- **Existing File to be Modified:** `capsule/core/packager.py` (to implement the core packaging logic).
- **Existing File to be Modified:** `capsule/models/cypher.py` (to define the cypher model).
- **Existing File to be Modified:** `capsule/core/validator.py` (to add validation for packaging).
- **Existing File to be Modified:** `capsule/commands/export.py` (to use the packager).
- **New Test File to be Created:** `tests/test_core/test_packager.py` (to add unit tests for the packager).

### Learnings from Previous Story

The previous story (5.6) modified the following files:
- `capsule/commands/validate.py`
- `capsule/core/validator.py`
- `tests/test_core/test_validator.py`

This indicates that the validation component is under active development and should be considered when implementing the packaging logic. The previous story did not contain any specific completion notes or warnings.

[Source: stories/5-6-validation-report-generation.md]

### References

- [Source: docs/epics.md#Epic-6-Capsule-Packaging]
- [Source: docs/PRD.md#FR-Group-3-Capsule-Packaging]
- [Source: docs/architecture.md#Epic-Group-3-Capsule-Packaging-FR17-FR25]

## Acceptance Criteria

1. A `CapsulePackager` class is created in `capsule/core/packager.py`.
2. The `CapsulePackager` can generate a `capsule-cypher.yaml` file.
3. The generated cypher file includes capsule identity, folder structure, file inventory, and data schemas.
4. The `CapsulePackager` can package a capsule into a folder bundle.
5. Unit tests are added to `tests/test_core/test_packager.py` to verify the packaging logic.

## Tasks / Subtasks

- [x] **Task 1: Implement CapsulePackager Class** (AC: #1)
  - [x] Subtask 1.1: Create the `CapsulePackager` class in `capsule/core/packager.py`.
  - [x] Subtask 1.2: Add unit tests for the `CapsulePackager` class.
- [x] **Task 2: Implement Cypher Generation** (AC: #2, #3)
  - [x] Subtask 2.1: Add a method to `CapsulePackager` to generate the `capsule-cypher.yaml` file.
  - [x] Subtask 2.2: Ensure the cypher includes all required sections.
  - [x] Subtask 2.3: Add unit tests for cypher generation.
- [x] **Task 3: Implement Folder Bundle Packaging** (AC: #4)
  - [x] Subtask 3.1: Add a method to `CapsulePackager` to create a folder bundle.
  - [x] Subtask 3.2: Add unit tests for folder bundle packaging.
- [x] **Task 4: Add Unit Tests for All ACs** (AC: #5)
  - [x] Subtask 4.1: Create `tests/test_core/test_packager.py`.
  - [x] Subtask 4.2: Add tests for cypher generation and folder packaging.
  - [x] Subtask 4.3: Add tests for cypher content verification.
  - [x] Subtask 4.4: Add tests for folder bundle content verification.
  - [x] Subtask 4.5: Add tests for edge cases and error handling.

### Review Follow-ups (AI)
- [x] [AI-Review][Medium] Refactor `CapsulePackager.generate_cypher` to not use hardcoded values.
- [x] [AI-Review][Medium] Add error handling to `CapsulePackager`.
- [x] [AI-Review][Medium] Add more comprehensive tests to `test_packager.py`.
- [x] [AI-Review][Low] Add logging to `CapsulePackager`.


## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/stories/6-1-capsule-packager-core.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

- ✅ Resolved review finding [Medium]: Refactor `CapsulePackager.generate_cypher` to not use hardcoded values.
- ✅ Resolved review finding [Medium]: Add error handling to `CapsulePackager`.
- ✅ Resolved review finding [Medium]: Add more comprehensive tests to `test_packager.py`.
- ✅ Resolved review finding [Low]: Add logging to `CapsulePackager`.

### File List

- `capsule/core/packager.py`
- `tests/test_core/test_packager.py`

## Change Log

- 2025-11-19: Story drafted by BMad.
- 2025-11-19: Addressed code review findings - 4 items resolved.


## Senior Developer Review (AI)

- **Reviewer**: BMad
- **Date**: 2025-11-19
- **Outcome**: Changes Requested

### Summary

The core functionality for the `CapsulePackager` has been implemented and meets the basic acceptance criteria. However, the implementation has several shortcomings that need to be addressed before it can be approved. The main issues are the use of hardcoded values in the cypher generation, a lack of error handling, and insufficient test coverage for edge cases.

### Key Findings

- **[Medium]** Hardcoded values in `generate_cypher` method in `capsule/core/packager.py`.
- **[Medium]** Lack of error handling in `CapsulePackager`.
- **[Medium]** Insufficient test coverage for edge cases and error handling in `tests/test_core/test_packager.py`.
- **[Low]** No logging in `CapsulePackager`.

### Acceptance Criteria Coverage

| AC# | Description | Status | Evidence |
| :-- | :--- | :--- | :--- |
| 1 | A `CapsulePackager` class is created in `capsule/core/packager.py`. | IMPLEMENTED | `capsule/core/packager.py:7` |
| 2 | The `CapsulePackager` can generate a `capsule-cypher.yaml` file. | IMPLEMENTED | `capsule/core/packager.py:21`, `capsule/core/packager.py:61-66` |
| 3 | The generated cypher file includes capsule identity, folder structure, file inventory, and data schemas. | IMPLEMENTED | `capsule/core/packager.py:29-38` |
| 4 | The `CapsulePackager` can package a capsule into a folder bundle. | IMPLEMENTED | `capsule/core/packager.py:57-67` |
| 5 | Unit tests are added to `tests/test_core/test_packager.py` to verify the packaging logic. | IMPLEMENTED | `tests/test_core/test_packager.py` |

**Summary**: 5 of 5 acceptance criteria fully implemented.

### Task Completion Validation

| Task | Marked As | Verified As | Evidence |
| :--- | :--- | :--- | :--- |
| **Task 1: Implement CapsulePackager Class** | Completed | VERIFIED COMPLETE | `capsule/core/packager.py` |
| Subtask 1.1: Create the `CapsulePackager` class | Completed | VERIFIED COMPLETE | `capsule/core/packager.py:7` |
| Subtask 1.2: Add unit tests for the `CapsulePackager` class | Completed | VERIFIED COMPLETE | `tests/test_core/test_packager.py:21` |
| **Task 2: Implement Cypher Generation** | Completed | VERIFIED COMPLETE | `capsule/core/packager.py:21` |
| Subtask 2.1: Add a method to `CapsulePackager` to generate the `capsule-cypher.yaml` file | Completed | VERIFIED COMPLETE | `capsule/core/packager.py:21` |
| Subtask 2.2: Ensure the cypher includes all required sections | Completed | VERIFIED COMPLETE | `capsule/core/packager.py:29-38` |
| Subtask 2.3: Add unit tests for cypher generation | Completed | VERIFIED COMPLETE | `tests/test_core/test_packager.py:28` |
| **Task 3: Implement Folder Bundle Packaging** | Completed | VERIFIED COMPLETE | `capsule/core/packager.py:57` |
| Subtask 3.1: Add a method to `CapsulePackager` to create a folder bundle | Completed | VERIFIED COMPLETE | `capsule/core/packager.py:57` |
| Subtask 3.2: Add unit tests for folder bundle packaging | Completed | VERIFIED COMPLETE | `tests/test_core/test_packager.py:38` |
| **Task 4: Add Unit Tests for All ACs** | Completed | VERIFIED COMPLETE | `tests/test_core/test_packager.py` |
| Subtask 4.1: Create `tests/test_core/test_packager.py` | Completed | VERIFIED COMPLETE | `tests/test_core/test_packager.py` |
| Subtask 4.2: Add tests for cypher generation and folder packaging | Completed | VERIFIED COMPLETE | `tests/test_core/test_packager.py:28`, `tests/test_core/test_packager.py:38` |
| Subtask 4.3: Add tests for cypher content verification | Completed | VERIFIED COMPLETE | `tests/test_core/test_packager.py:31-35`, `tests/test_core/test_packager.py:47-50` |
| Subtask 4.4: Add tests for folder bundle content verification | Completed | VERIFIED COMPLETE | `tests/test_core/test_packager.py:43-50` |
| Subtask 4.5: Add tests for edge cases and error handling | Completed | QUESTIONABLE | No specific tests for edge cases or error handling were found. |

**Summary**: 13 of 14 completed tasks verified, 1 questionable, 0 falsely marked complete.

### Test Coverage and Gaps

- The existing tests cover the basic functionality of the `CapsulePackager` class.
- There is a gap in testing for edge cases and error handling.

### Architectural Alignment

- No Epic Tech Spec was found, so alignment could not be verified.
- No story context file was found.

### Security Notes

- No security issues were found.

### Best-Practices and References

The project follows modern Python best practices, utilizing `pyproject.toml` for dependency management and tool configuration. Key aspects include:

- **CLI**: A Typer-based command-line interface.
- **Code Quality**: Enforced through `ruff` for linting and `black` for formatting. Type safety is encouraged with `mypy`.
- **Testing**: `pytest` is the testing framework, with `coverage` for measuring test coverage.
- **YAML Handling**: `ruamel.yaml` is used for its ability to preserve comments and formatting in YAML files, which is crucial for the `capsule-cypher.yaml`.
- **Frontmatter**: `python-frontmatter` is used for parsing frontmatter from Markdown files.
- **Templating**: `Jinja2` is the templating engine for content generation.

### Action Items

**Code Changes Required:**
- [x] [Medium] Refactor `CapsulePackager.generate_cypher` to not use hardcoded values. These values should be passed in or read from a configuration file. (AC #3) [file: capsule/core/packager.py]
- [x] [Medium] Add error handling to `CapsulePackager` for cases like missing capsule directory or unwritable output directory. [file: capsule/core/packager.py]
- [x] [Medium] Add more comprehensive tests to `test_packager.py` to cover edge cases and error conditions. (AC #5) [file: tests/test_core/test_packager.py]
- [x] [Low] Add logging to `CapsulePackager` to provide visibility into the packaging process. [file: capsule/core/packager.py]

**Advisory Notes:**
- Note: No Epic Tech Spec was found for epic 6.
- Note: No story context file was found for story 6.1.

