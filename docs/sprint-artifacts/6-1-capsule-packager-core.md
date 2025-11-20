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

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/stories/6-1-capsule-packager-core.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

- `capsule/core/packager.py`
- `capsule/models/cypher.py`
- `tests/test_core/test_packager.py`

## Change Log

- 2025-11-19: Story drafted by BMad.





