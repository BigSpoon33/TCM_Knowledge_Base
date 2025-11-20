# Story 6.2: cypher-generation-from-capsule

Status: Done

## Story

As a developer,
I want to generate a `capsule-cypher.yaml` file from the contents of a capsule,
so that I can create a manifest of the capsule's contents and metadata.

## Acceptance Criteria

1. A method exists in `CapsulePackager` to generate a `capsule-cypher.yaml` file from a given capsule directory.
2. The generated cypher file contains the correct `capsule_id`, `name`, `version`, and `domain_type`.
3. The generated cypher file accurately lists the folder structure of the capsule.
4. The generated cypher file accurately inventories all files in the capsule, including their paths and IDs.
5. The generated cypher file includes the data schemas defined in the capsule.
6. Unit tests are added to `tests/test_core/test_cypher_generation.py` to verify the cypher generation logic.

## Tasks / Subtasks

- [x] **Task 1: Implement Cypher Generation Method** (AC: #1)
  - [x] Subtask 1.1: Create a method in `CapsulePackager` to generate the cypher.
  - [x] Subtask 1.2: Add unit tests for the cypher generation method.
- [x] **Task 2: Populate Cypher Metadata** (AC: #2)
  - [x] Subtask 2.1: Extract metadata from the capsule and add it to the cypher.
  - [x] Subtask 2.2: Add unit tests to verify the metadata in the cypher.
- [x] **Task 3: Populate Folder Structure** (AC: #3)
  - [x] Subtask 3.1: Scan the capsule directory and add the folder structure to the cypher.
  - [x] Subtask 3.2: Add unit tests to verify the folder structure in the cypher.
- [x] **Task 4: Populate File Inventory** (AC: #4)
  - [x] Subtask 4.1: Scan the capsule directory and add the file inventory to the cypher.
  - [x] Subtask 4.2: Add unit tests to verify the file inventory in the cypher.
- [x] **Task 5: Populate Data Schemas** (AC: #5)
  - [x] Subtask 5.1: Extract data schemas from the capsule and add them to the cypher.
  - [x] Subtask 5.2: Add unit tests to verify the data schemas in the cypher.
- [x] **Task 6: Add Unit Tests for All ACs** (AC: #6)
  - [x] Subtask 6.1: Create `tests/test_core/test_cypher_generation.py`.
  - [x] Subtask 6.2: Add tests for all aspects of cypher generation.
- [x] **[AI-Review][High]** Implement the logic to extract data schemas from the capsule and add them to the cypher. (AC #5)
- [x] **[AI-Review][Medium]** Improve the unit test for data schema validation to check for correct schema extraction, not just an empty dictionary.


## Dev Notes

### Requirements Context Summary

- **Epic:** 6: Capsule Packaging
- **Summary:** Generate `capsule-cypher.yaml` from capsule contents.
- **Source:** `docs/epics.md`

- **Relevant architecture patterns and constraints:** The generated `capsule-cypher.yaml` must match the structure defined in the architecture document, including `capsule_id`, `name`, `version`, `domain_type`, `folder_structure`, `contents`, `data_schemas`, `sequence_mode`, and `required_plugins`.
- **Testing standards summary:** Unit tests should verify that the generated cypher file is well-formed and accurately reflects the contents of the capsule.


### Project Structure Notes

- **Existing File to be Modified:** `capsule/core/packager.py` (to implement the cypher generation logic).
- **Existing File to be Modified:** `capsule/models/cypher.py` (to define the cypher model).
- **New Test File to be Created:** `tests/test_core/test_cypher_generation.py` (to add unit tests for cypher generation).

### Learnings from Previous Story

The previous story (6.1) created the core `CapsulePackager` class and the initial `cypher.py` model. This story will build upon that foundation.
The validation component is under active development and should be considered when implementing the cypher generation.
New files created in the previous story: `capsule/core/packager.py`, `capsule/models/cypher.py`, `tests/test_core/test_packager.py`.

[Source: stories/6-1-capsule-packager-core.md]

### References

- [Source: docs/epics.md#Epic-6-Capsule-Packaging]
- [Source: docs/architecture.md#Capsule-Cypher-Structure-Implementation-Detail]

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->
- docs/sprint-artifacts/stories/6-2-cypher-generation-from-capsule.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

---
## Senior Developer Review (AI)
- **Reviewer:** BMad
- **Date:** 2025-11-19
- **Outcome:** Blocked
  - **Justification:** A high-severity finding (AC5 not implemented, Task 5 falsely marked complete) prevents the story from being approved.

### Summary
The implementation of the cypher generation from a capsule is mostly complete and well-tested. However, the key feature of including data schemas in the cypher is missing, and the associated task was incorrectly marked as complete.

### Key Findings
- **HIGH:** AC#5 is not implemented. The `data_schemas` field in the generated cypher is hardcoded to an empty dictionary.
- **HIGH:** Task 5, "Populate Data Schemas," was marked as complete, but the implementation is missing.

### Acceptance Criteria Coverage
| AC# | Description | Status | Evidence |
|---|---|---|---|
| 1 | A method exists in `CapsulePackager` to generate a `capsule-cypher.yaml` file from a given capsule directory. | IMPLEMENTED | `capsule/core/packager.py:50` |
| 2 | The generated cypher file contains the correct `capsule_id`, `name`, `version`, and `domain_type`. | IMPLEMENTED | `capsule/core/packager.py:59-63` |
| 3 | The generated cypher file accurately lists the folder structure of the capsule. | IMPLEMENTED | `capsule/core/packager.py:72` |
| 4 | The generated cypher file accurately inventories all files in the capsule, including their paths and IDs. | IMPLEMENTED | `capsule/core/packager.py:72` |
| 5 | The generated cypher file includes the data schemas defined in the capsule. | NOT IMPLEMENTED | `capsule/core/packager.py:66` |
| 6 | Unit tests are added to `tests/test_core/test_cypher_generation.py` to verify the cypher generation logic. | IMPLEMENTED | `tests/test_core/test_cypher_generation.py` |

**Summary:** 5 of 6 acceptance criteria fully implemented.

### Task Completion Validation
| Task | Marked As | Verified As | Evidence |
|---|---|---|---|
| 1: Implement Cypher Generation Method | Complete | VERIFIED COMPLETE | `capsule/core/packager.py:50` |
| 2: Populate Cypher Metadata | Complete | VERIFIED COMPLETE | `capsule/core/packager.py:59-63` |
| 3: Populate Folder Structure | Complete | VERIFIED COMPLETE | `capsule/core/packager.py:72` |
| 4: Populate File Inventory | Complete | VERIFIED COMPLETE | `capsule/core/packager.py:72` |
| 5: Populate Data Schemas | Complete | NOT DONE | `capsule/core/packager.py:66` |
| 6: Add Unit Tests for All ACs | Complete | VERIFIED COMPLETE | `tests/test_core/test_cypher_generation.py` |

**Summary:** 5 of 6 completed tasks verified, 1 falsely marked complete.

### Test Coverage and Gaps
- The test for AC5 is weak and only checks for an empty dictionary.

### Action Items
**Code Changes Required:**
- [ ] [High] Implement the logic to extract data schemas from the capsule and add them to the cypher. (AC #5) [file: capsule/core/packager.py]
- [ ] [Medium] Improve the unit test for data schema validation to check for correct schema extraction, not just an empty dictionary. [file: tests/test_core/test_cypher_generation.py]
