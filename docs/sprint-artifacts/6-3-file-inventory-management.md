# Story 6.3: file-inventory-management

Status: review

## Story

As a developer,
I want to manage the file inventory within the `capsule-cypher.yaml` file,
so that I can accurately track all the files that are part of a capsule.

## Acceptance Criteria

1. A method exists in `CapsulePackager` that scans a capsule directory and generates a file inventory.
2. The file inventory is stored in the `contents` section of the `capsule-cypher.yaml` file.
3. The `contents` section is a dictionary where keys are folder names and values are lists of file entries.
4. Each file entry in the inventory contains the file's relative path and a unique ID.
5. The file inventory accurately reflects the complete file and folder structure of the capsule.
6. Unit tests are added to verify the file inventory generation for various directory structures.

## Tasks / Subtasks

- [x] **Task 1: Implement File Inventory Generation** (AC: #1, #2, #3, #4, #5)
    - [x] Subtask 1.1: Create a method in `CapsulePackager` to scan the capsule directory.
    - [x] Subtask 1.2: Implement logic to generate a unique ID for each file.
    - [x] Subtask 1.3: Implement logic to create the `contents` dictionary with folder and file entries.
    - [x] Subtask 1.4: Integrate the file inventory generation into the main cypher generation process.
- [x] **Task 2: Add Unit Tests** (AC: #6)
    - [x] Subtask 2.1: Add unit tests for a simple capsule with a flat file structure.
    - [x] Subtask 2.2: Add unit tests for a capsule with nested folders.
    - [x] Subtask 2.3: Add unit tests for a capsule with various file types.
    - [x] Subtask 2.4: Add unit tests for an empty capsule.

## Dev Notes

- Epic: 6: Capsule Packaging
- Summary: This story focuses on implementing the file inventory management within the `capsule-cypher.yaml` file. The core task is to create a robust mechanism to scan a capsule's directory, identify all files, and accurately record them in the `contents` section of the cypher, following the structure defined in the architecture document.
- Source: `docs/epics.md`
- Relevant architecture patterns and constraints: The implementation must adhere to the `Capsule Cypher Structure` defined in `docs/architecture.md`. Specifically, the `contents` section should be a dictionary where keys are the folder names (e.g., `root_notes`, `study_material`) and values are lists of file entries. Each file entry should be a dictionary containing the `file` path and a unique `id`.
- Testing standards summary: Unit tests are required to verify that the file inventory is generated correctly for various capsule structures, including nested folders and different file types.

### Project Structure Notes

- **Learnings from Previous Story (6.2):**
    - The previous story established the core `CapsulePackager` class in `capsule/core/packager.py` and the `CapsuleCypher` model in `capsule/models/cypher.py`. This story will extend the `CapsulePackager` to include file inventory management.
    - A key consideration is the ongoing development of the validation component, which will be needed to validate the generated file inventory.
    - The test suite for the packager is located at `tests/test_core/test_packager.py`, and new tests for file inventory management should be added there or in a new dedicated test file.
- **Project Structure Alignment:**
    - The logic for file inventory management should be implemented within the `CapsulePackager` class in `capsule/core/packager.py`.
    - The `CapsuleCypher` model in `capsule/models/cypher.py` will be used to store the file inventory data.
    - Unit tests should be added to `tests/test_core/test_packager.py` or a new file `tests/test_core/test_file_inventory.py` to verify the correctness of the file inventory generation.

### References

- [Source: docs/epics.md#Epic-6-Capsule-Packaging]
- [Source: docs/architecture.md#Capsule-Cypher-Structure-Implementation-Detail]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/stories/6-3-file-inventory-management.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

- `capsule/core/packager.py` (Modified)
- `tests/test_core/test_file_inventory.py` (New)

---
# Senior Developer Review (AI)
## Reviewer: BMad
## Date: 2025-11-19
## Outcome: Approve
This story is approved. All acceptance criteria are met and verified, and all completed tasks have been validated. The implementation is clean and the unit tests are thorough.

## Key Findings
- **[Low]** In `capsule/core/packager.py`, the `_scan_schemas` method logs a warning but continues if a domain schema is not found. It would be more robust to raise an exception in this case, as a missing schema could lead to silent failures downstream.

## Acceptance Criteria Coverage
**Summary: 6 of 6 acceptance criteria fully implemented.**

| AC# | Description | Status | Evidence |
|---|---|---|---|
| 1 | A method exists in `CapsulePackager` that scans a capsule directory and generates a file inventory. | IMPLEMENTED | `capsule/core/packager.py:82` |
| 2 | The file inventory is stored in the `contents` section of the `capsule-cypher.yaml` file. | IMPLEMENTED | `capsule/core/packager.py:65` |
| 3 | The `contents` section is a dictionary where keys are folder names and values are lists of file entries. | IMPLEMENTED | `capsule/core/packager.py:85`, `capsule/core/packager.py:112` |
| 4 | Each file entry in the inventory contains the file's relative path and a unique ID. | IMPLEMENTED | `capsule/core/packager.py:114-119` |
| 5 | The file inventory accurately reflects the complete file and folder structure of the capsule. | IMPLEMENTED | `capsule/core/packager.py:87` |
| 6 | Unit tests are added to verify the file inventory generation for various directory structures. | IMPLEMENTED | `tests/test_core/test_file_inventory.py` |

## Task Completion Validation
**Summary: 8 of 8 completed tasks verified.**

| Task | Marked As | Verified As | Evidence |
|---|---|---|---|
| Subtask 1.1: Create a method in `CapsulePackager` to scan the capsule directory. | [x] | VERIFIED COMPLETE | `capsule/core/packager.py:82` |
| Subtask 1.2: Implement logic to generate a unique ID for each file. | [x] | VERIFIED COMPLETE | `capsule/core/packager.py:78` |
| Subtask 1.3: Implement logic to create the `contents` dictionary with folder and file entries. | [x] | VERIFIED COMPLETE | `capsule/core/packager.py:82-121` |
| Subtask 1.4: Integrate the file inventory generation into the main cypher generation process. | [x] | VERIFIED COMPLETE | `capsule/core/packager.py:63` |
| Subtask 2.1: Add unit tests for a simple capsule with a flat file structure. | [x] | VERIFIED COMPLETE | `tests/test_core/test_file_inventory.py:18` |
| Subtask 2.2: Add unit tests for a capsule with nested folders. | [x] | VERIFIED COMPLETE | `tests/test_core/test_file_inventory.py:40` |
| Subtask 2.3: Add unit tests for a capsule with various file types. | [x] | VERIFIED COMPLETE | `tests/test_core/test_file_inventory.py:70` |
| Subtask 2.4: Add unit tests for an empty capsule. | [x] | VERIFIED COMPLETE | `tests/test_core/test_file_inventory.py:90` |

## Architectural Alignment
- **Tech Spec:** No tech spec was found for Epic 6.
- **Architecture Document:** The implementation correctly follows the `Capsule Cypher Structure` defined in `docs/architecture.md`.

## Action Items
**Advisory Notes:**
- Note: Consider making the `_scan_schemas` method in `capsule/core/packager.py` raise an exception if the domain schema is not found to prevent silent failures.
