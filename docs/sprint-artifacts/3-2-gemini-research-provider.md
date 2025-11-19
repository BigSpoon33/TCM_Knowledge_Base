---
story_id: "3.2"
epic_id: "3"
title: "Gemini Research Provider"
status: "done"
---

## 1. Story Description

As a developer, I want a concrete `GeminiResearchProvider` that implements the `ResearchProvider` interface, so that the application can perform deep research using the Google Gemini API.

## 2. Acceptance Criteria

1.  **Concrete Implementation:** A `GeminiResearchProvider` class is created in `capsule/core/researcher.py` that inherits from `ResearchProvider`.
2.  **API Integration:** The `research` method is implemented to call the Google Gemini API using the `google-generativeai` library.
3.  **API Key Handling:** The provider retrieves the API key from the user's configuration via the `Config` model.
4.  **Error Handling:** A `NetworkError` is raised if the API call fails.
5.  **Data Transformation:** The response from the Gemini API is transformed into the required dictionary format (`content`, `citations`, `metadata`).
6.  **Unit Tests:** The `GeminiResearchProvider` is tested in `tests/test_core/test_researcher.py`, using mocks to simulate the API call.

## 3. Tasks

### Task 3.1: Implement Gemini Research Provider

-   [x] **Subtask 3.1.1:** Implement the `GeminiResearchProvider` class in `capsule/core/researcher.py`.
-   [x] **Subtask 3.1.2:** In the `__init__` method, load the `Config` and retrieve the `research.api_key`.
-   [x] **Subtask 3.1.3:** Implement the `research` method to construct a prompt, call the Gemini API, and handle the response.
-   [x] **Subtask 3.1.4:** Add a `NetworkError` to `capsule/utils/exceptions.py`.

### Task 3.2: Develop Unit Tests

-   [x] **Subtask 3.2.1:** Add tests to `tests/test_core/test_researcher.py` for the `GeminiResearchProvider`.
-   [x] **Subtask 3.2.2:** Write a test that mocks a successful API call and verifies that the data is transformed correctly.
-   [x] **Subtask 3.2.3:** Write a test that mocks a failed API call and asserts that a `NetworkError` is raised.
-   [x] **Subtask 3.2.4:** Write a test to ensure the provider correctly reads the API key from the mocked `Config`.

## 4. Dev Notes

-   The `google-generativeai` library is already a dependency and should be used for the API calls.
-   The `Config` model should be used to retrieve the API key.
-   Error handling should be consistent with the patterns established in the architecture.

### Learnings from Previous Story

**From Story 3.1 (Status: done)**

-   **Interface Defined**: The `ResearchProvider` abstract base class provides the exact interface that `GeminiResearchProvider` must implement.

[Source: docs/sprint-artifacts/3-1-research-provider-abstract-base.md#Dev-Agent-Record]

### References

-   [Source: docs/architecture.md#Deep-Research-Provider-Architecture]

## 5. Dev Agent Record

- **Context Reference:** [3-2-gemini-research-provider.context.xml](./stories/3-2-gemini-research-provider.context.xml)
- **Completion Notes:**
    - Implemented the `GeminiResearchProvider` in `capsule/core/researcher.py`.
    - Added the `NetworkError` exception.
    - Wrote a comprehensive test suite for the new provider, which passed successfully.
- **File List:**
    - `M capsule/core/researcher.py`
    - `M capsule/utils/exceptions.py`
    - `M tests/test_core/test_researcher.py`
- **Change Log:**
    - Implemented the Gemini research provider. (2025-11-16)

---

## Senior Developer Review (AI)

**Reviewer:** BMad
**Date:** 2025-11-16
**Outcome:** Approve

### Summary
The implementation is excellent. All acceptance criteria are fully met, and all tasks marked as complete have been verified. The code is clean, well-tested, and adheres to the architectural guidelines.

### Key Findings
No significant findings. The work is of high quality.

### Acceptance Criteria Coverage
| AC# | Description | Status | Evidence |
|---|---|---|---|
| 1 | Concrete Implementation | IMPLEMENTED | `capsule/core/researcher.py:30` |
| 2 | API Integration | IMPLEMENTED | `capsule/core/researcher.py:48` |
| 3 | API Key Handling | IMPLEMENTED | `capsule/core/researcher.py:34-36` |
| 4 | Error Handling | IMPLEMENTED | `capsule/core/researcher.py:62` |
| 5 | Data Transformation | IMPLEMENTED | `capsule/core/researcher.py:56-60` |
| 6 | Unit Tests | IMPLEMENTED | `tests/test_core/test_researcher.py:38-79` |

**Summary:** 6 of 6 acceptance criteria fully implemented.

### Task Completion Validation
| Task | Marked As | Verified As | Evidence |
|---|---|---|---|
| 3.1.1 | [x] | VERIFIED COMPLETE | `capsule/core/researcher.py:30` |
| 3.1.2 | [x] | VERIFIED COMPLETE | `capsule/core/researcher.py:34-36` |
| 3.1.3 | [x] | VERIFIED COMPLETE | `capsule/core/researcher.py:41-63` |
| 3.1.4 | [x] | VERIFIED COMPLETE | `capsule/utils/exceptions.py:19` |
| 3.2.1 | [x] | VERIFIED COMPLETE | `tests/test_core/test_researcher.py:38-79` |
| 3.2.2 | [x] | VERIFIED COMPLETE | `tests/test_core/test_researcher.py:38-57` |
| 3.2.3 | [x] | VERIFIED COMPLETE | `tests/test_core/test_researcher.py:59-72` |
| 3.2.4 | [x] | VERIFIED COMPLETE | `tests/test_core/test_researcher.py:74-79` |

**Summary:** 8 of 8 completed tasks verified.

### Action Items
**Advisory Notes:**
- Note: No action items. The implementation is solid.
