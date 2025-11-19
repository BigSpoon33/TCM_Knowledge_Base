---
story_id: "3.4"
epic_id: "3"
title: "Research Result Data Model"
status: "review"
---

## 1. Story Description

As a developer, I want a data model to structure the results of a research task,
so that the content, citations, and metadata can be handled in a standardized way.

## 2. Acceptance Criteria

1.  **ResearchResult Data Model:** A new data model, `ResearchResult`, is created in `capsule/models/research.py` to store the results of a research task.
2.  **Data Model Fields:** The `ResearchResult` model includes fields for `content` (str), `citations` (List[Citation]), and `metadata` (Dict).
3.  **Interface Update:** The `ResearchProvider` abstract base class in `capsule/core/researcher.py` is updated to reflect that its `research` method will return a `ResearchResult` object.
4.  **Implementation Update:** The `GeminiResearchProvider` is modified to return an instance of the `ResearchResult` model.
5.  **Model Unit Tests:** Unit tests are created in `tests/test_models/test_research.py` to validate the `ResearchResult` model.
6.  **Provider Unit Tests:** The unit tests for `GeminiResearchProvider` in `tests/test_core/test_researcher.py` are updated to verify that the provider correctly returns a `ResearchResult` object.

## 3. Tasks

### Task 3.1: Implement `ResearchResult` Data Model

-   [x] **Subtask 3.1.1:** Create the file `capsule/models/research.py`.
-   [x] **Subtask 3.1.2:** Implement the `ResearchResult` data model with fields for `content`, `citations`, and `metadata`.
-   [x] **Subtask 3.1.3:** Create the test file `tests/test_models/test_research.py`.
-   [x] **Subtask 3.1.4:** Write unit tests to validate the `ResearchResult` model.

### Task 3.2: Update Research Provider

-   [x] **Subtask 3.2.1:** Update the `ResearchProvider` ABC in `capsule/core/researcher.py` to return a `ResearchResult` object.
-   [x] **Subtask 3.2.2:** Update the `GeminiResearchProvider` to return a `ResearchResult` object.
-   [x] **Subtask 3.2.3:** Update the tests for `GeminiResearchProvider` in `tests/test_core/test_researcher.py` to assert that the returned object is a valid `ResearchResult` instance.

## 5. Dev Agent Record

### File List

- `A capsule/models/research.py`
- `A tests/test_models/test_research.py`
- `M capsule/core/researcher.py`
- `M tests/test_core/test_researcher.py`


-   The `ResearchResult` model should be a simple data class, consistent with other models in `capsule/models/`.
-   The `Citation` model from the previous story should be used for the `citations` field.

### Learnings from Previous Story

**From Story 3.3 (Status: done)**

-   **New Service Created**: The `Citation` data model in `capsule/models/citation.py` is now available and should be used to manage citations.
-   **Architectural Change**: The `ResearchProvider` interface now includes citation tracking.
-   **Files Modified**: The previous story modified `capsule/core/researcher.py` and `tests/test_core/test_researcher.py`, which are the same files that will be updated in this story.

[Source: docs/sprint-artifacts/3-3-citation-tracking-system.md#Dev-Agent-Record]

### References

-   [Source: docs/architecture.md#Deep-Research-Provider-Architecture]

---

## Senior Developer Review (AI)

**Reviewer:** BMad
**Date:** 2025-11-18
**Outcome:** Approve

### Summary
The implementation of the `ResearchResult` data model is complete and of high quality. The `ResearchProvider` interface and the `GeminiResearchProvider` have been successfully updated to use the new data model. The test suite has been updated to reflect these changes and all tests are passing.

### Key Findings
- No issues were found. The implementation is of high quality.

### Acceptance Criteria Coverage
| AC# | Description | Status | Evidence |
|---|---|---|---|
| 1 | ResearchResult Data Model | IMPLEMENTED | `capsule/models/research.py:7` |
| 2 | Data Model Fields | IMPLEMENTED | `capsule/models/research.py:9-11` |
| 3 | Interface Update | IMPLEMENTED | `capsule/core/researcher.py:14` |
| 4 | Implementation Update | IMPLEMENTED | `capsule/core/researcher.py:56` |
| 5 | Model Unit Tests | IMPLEMENTED | `tests/test_models/test_research.py:6` |
| 6 | Provider Unit Tests | IMPLEMENTED | `tests/test_core/test_researcher.py:14` |

**Summary:** 6 of 6 acceptance criteria fully implemented.

### Task Completion Validation
| Task | Marked As | Verified As | Evidence |
|---|---|---|---|
| 3.1.1 | [x] | VERIFIED COMPLETE | `capsule/models/research.py` exists |
| 3.1.2 | [x] | VERIFIED COMPLETE | `ResearchResult` dataclass has correct fields |
| 3.1.3 | [x] | VERIFIED COMPLETE | `tests/test_models/test_research.py` exists |
| 3.1.4 | [x] | VERIFIED COMPLETE | `test_research_result_instantiation` validates the model |
| 3.2.1 | [x] | VERIFIED COMPLETE | `ResearchProvider` ABC has correct return type hint |
| 3.2.2 | [x] | VERIFIED COMPLETE | `research` method now correctly returns a `ResearchResult` object |
| 3.2.3 | [x] | VERIFIED COMPLETE | Test asserts that the returned object is an instance of `ResearchResult` |

**Summary:** 7 of 7 completed tasks verified.

### Action Items
**Code Changes Required:**
- None

**Advisory Notes:**
- None

