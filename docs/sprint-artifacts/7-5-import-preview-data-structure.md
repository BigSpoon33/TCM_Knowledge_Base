# Story 7.5: import-preview-data-structure

Status: done

## Story

As a developer,
I want a well-defined data structure for the import preview,
so that I can accurately represent the impact of an import to the user.

## Acceptance Criteria

1. A main `ImportPreview` dataclass is defined in `capsule/core/importer.py`.
2. The `ImportPreview` class contains nested dataclasses for structured data: `CapsuleInfo`, `Impact`, `UpdateDetail`, and `ConflictDetail`.
3. The `CapsuleInfo` dataclass contains `id` (str), `version` (str), and `file_count` (int).
4. The `Impact` dataclass contains counts for `new_files` (int), `updated_files` (int), and `conflicts` (int).
5. The `UpdateDetail` dataclass contains `file` (str), `strategy` (str), and `changes` (str).
6. The `ConflictDetail` dataclass contains `file` (str), `reason` (str), and `sources` (List[str]).
7. The `CapsuleImporter.analyze_impact()` method is refactored to return a fully populated `ImportPreview` object.
8. The CLI preview display logic in `importer.py` is updated to read its data from the `ImportPreview` object.

## Tasks / Subtasks

- [x] **Task 1: Define Nested Dataclasses** (AC: #2, #3, #4, #5, #6)
  - [x] Subtask 1.1: In `capsule/core/importer.py`, create the `CapsuleInfo` dataclass.
  - [x] Subtask 1.2: Create the `Impact` dataclass.
  - [x] Subtask 1.3: Create the `UpdateDetail` dataclass.
  - [x] Subtask 1.4: Create the `ConflictDetail` dataclass.

- [x] **Task 2: Define Main `ImportPreview` Dataclass** (AC: #1)
  - [x] Subtask 2.1: In `capsule/core/importer.py`, create the `ImportPreview` dataclass, composing it from the nested dataclasses and `List` types.

- [x] **Task 3: Integrate Data Structure into Importer** (AC: #7)
  - [x] Subtask 3.1: Refactor the `analyze_impact` method in `CapsuleImporter` to build and return an instance of `ImportPreview`.
  - [x] Subtask 3.2: Ensure all logic for detecting new files, updates, and conflicts correctly populates the new data structure.

- [x] **Task 4: Update CLI Display Logic** (AC: #8)
  - [x] Subtask 4.1: Modify the `_display_preview` (or equivalent) method in `CapsuleImporter` to take an `ImportPreview` object as input.
  - [x] Subtask 4.2: Update the `rich` table and panel generation to source all data from the `ImportPreview` object.

- [x] **Task 5: Update Unit Tests** (AC: #1-#8)
  - [x] Subtask 5.1: In `tests/test_core/test_importer.py`, update the tests for `analyze_impact` to check the returned `ImportPreview` object's attributes.
  - [x] Subtask 5.2: Add assertions to verify the structure and content of the nested dataclasses for various import scenarios.

## Change Log

- **2025-11-21**: Story drafted by BMad (SM Agent). Status set to `drafted`.
- **2025-11-21**: Implemented `ImportPreview` dataclasses and updated importer logic. (BMad)
- **2025-11-21**: Senior Developer Review notes appended. (BMad)


# Senior Developer Review (AI)

## Reviewer: BMad
## Date: 2025-11-21
## Outcome: Approve

## Summary

The implementation of the `ImportPreview` data structure is excellent. The code is well-structured, follows best practices, and includes thorough unit tests. All acceptance criteria have been met, and all tasks have been verified as complete.

## Key Findings

No high or medium severity findings.

### Low Severity
- **No Epic 7 Tech Spec**: The tech spec for Epic 7 was not found. This is a low-severity finding as the implementation appears correct based on the story and architecture documents, but it's important to ensure that all work is grounded in a tech spec.

## Acceptance Criteria Coverage

| AC# | Description | Status | Evidence |
|---|---|---|---|
| 1 | A main `ImportPreview` dataclass is defined in `capsule/core/importer.py`. | IMPLEMENTED | `capsule/core/importer.py:64-78` |
| 2 | The `ImportPreview` class contains nested dataclasses for structured data: `CapsuleInfo`, `Impact`, `UpdateDetail`, and `ConflictDetail`. | IMPLEMENTED | `capsule/core/importer.py:71-75` |
| 3 | The `CapsuleInfo` dataclass contains `id` (str), `version` (str), and `file_count` (int). | IMPLEMENTED | `capsule/core/importer.py:26-34` |
| 4 | The `Impact` dataclass contains counts for `new_files` (int), `updated_files` (int), and `conflicts` (int). | IMPLEMENTED | `capsule/core/importer.py:37-43` |
| 5 | The `UpdateDetail` dataclass contains `file` (str), `strategy` (str), and `changes` (str). | IMPLEMENTED | `capsule/core/importer.py:46-52` |
| 6 | The `ConflictDetail` dataclass contains `file` (str), `reason` (str), and `sources` (List[str]). | IMPLEMENTED | `capsule/core/importer.py:55-61` |
| 7 | The `CapsuleImporter.analyze_impact()` method is refactored to return a fully populated `ImportPreview` object. | IMPLEMENTED | `capsule/core/importer.py:238-350` |
| 8 | The CLI preview display logic in `importer.py` is updated to read its data from the `ImportPreview` object. | IMPLEMENTED | `capsule/core/importer.py:474-572` |

**Summary**: 8 of 8 acceptance criteria fully implemented.

## Task Completion Validation

| Task | Marked As | Verified As | Evidence |
|---|---|---|---|
| Task 1: Define Nested Dataclasses | [x] | VERIFIED COMPLETE | `capsule/core/importer.py:26-61` |
| Task 2: Define Main `ImportPreview` Dataclass | [x] | VERIFIED COMPLETE | `capsule/core/importer.py:64-78` |
| Task 3: Integrate Data Structure into Importer | [x] | VERIFIED COMPLETE | `capsule/core/importer.py:238-350` |
| Task 4: Update CLI Display Logic | [x] | VERIFIED COMPLETE | `capsule/core/importer.py:474-572` |
| Task 5: Update Unit Tests | [x] | VERIFIED COMPLETE | `tests/test_core/test_importer.py:288-427` |

**Summary**: 5 of 5 completed tasks verified.

## Test Coverage and Gaps

The unit tests in `tests/test_core/test_importer.py` are comprehensive and cover the new data structure and the `analyze_impact` method. There are no obvious gaps in test coverage.

## Architectural Alignment

The implementation aligns with the architecture document. The `ImportPreview` data structure is implemented as described, and the `Importer` class correctly uses it.

## Security Notes

The code includes a check for path traversal attacks in zip files, which is good practice. The use of `capsule_id` to construct a file path is a potential risk, but it is low in this context. It is recommended to sanitize the `capsule_id` before using it to construct a path in the future.

## Best-Practices and References

The code follows modern Python best practices, including the use of dataclasses, type hinting, and dependency injection.

## Action Items

**Advisory Notes:**
- Note: Create a tech spec for Epic 7 to ensure all future stories have a clear technical grounding.
- Note: Consider sanitizing the `capsule_id` before using it to construct file paths to further mitigate security risks.

