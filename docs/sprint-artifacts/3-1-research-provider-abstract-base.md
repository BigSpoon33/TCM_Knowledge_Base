---
story_id: "3.1"
epic_id: "3"
title: "Research Provider Abstract Base"
status: "done"
---

## 1. Story Description

As a developer, I want a `ResearchProvider` abstract base class (ABC) that defines a common interface for all research providers, so that new providers (like Gemini, Perplexity, etc.) can be added in a pluggable way without changing the core research logic.

## 2. Acceptance Criteria

1.  **Abstract Base Class:** A `ResearchProvider` abstract base class is created in `capsule/core/researcher.py`.
2.  **Interface Definition:** The `ResearchProvider` class defines an abstract method `research(self, topic: str, max_sources: int = 10) -> Dict`.
3.  **Data Structure:** The `research` method's return type is a dictionary containing `content`, `citations`, and `metadata`.
4.  **Type Hinting:** All methods and arguments are fully type-hinted.
5.  **Unit Tests:** Basic unit tests are created in `tests/test_core/test_researcher.py` to ensure the ABC cannot be instantiated and that subclasses must implement the `research` method.

## 3. Tasks

### Task 3.1: Implement Abstract Base Class

-   [x] **Subtask 3.1.1:** Create the file `capsule/core/researcher.py`.
-   [x] **Subtask 3.1.2:** Implement the `ResearchProvider` abstract base class using Python's `abc` module.
-   [x] **Subtask 3.1.3:** Define the `research` abstract method with the specified signature.

### Task 3.2: Develop Unit Tests

-   [x] **Subtask 3.2.1:** Create the test file `tests/test_core/test_researcher.py`.
-   [x] **Subtask 3.2.2:** Write a test that attempts to instantiate `ResearchProvider` directly and asserts that a `TypeError` is raised.
-   [x] **Subtask 3.2.3:** Write a test with a mock subclass that fails to implement the `research` method and assert that a `TypeError` is raised upon instantiation.
-   [x] **Subtask 3.2.4:** Write a test with a mock subclass that correctly implements the `research` method and assert that it can be instantiated successfully.

## 4. Dev Notes

-   This story lays the foundation for the entire research system. The interface defined here will be critical for all future research providers.
-   The use of Python's `abc` module is a core requirement.

### Learnings from Previous Story

**From Story 2.4 (Status: review)**

-   **CLI Framework**: The project uses `click`, not `Typer`. While this story is not a CLI command, it's a good reminder of the established framework.
-   **Explicit Save**: The refactoring of the `Config` model to have an explicit `save()` method is a good pattern to keep in mind for models that interact with the filesystem.

[Source: docs/sprint-artifacts/2-4-first-time-setup-command.md#Dev-Agent-Record]

### References

-   [Source: docs/architecture.md#Deep-Research-Provider-Architecture]

## 5. Dev Agent Record

- **Context Reference:** [3-1-research-provider-abstract-base.context.xml](./stories/3-1-research-provider-abstract-base.context.xml)
- **Completion Notes:**
    - Created the `ResearchProvider` abstract base class in `capsule/core/researcher.py`.
    - Wrote a test suite in `tests/test_core/test_researcher.py` to verify the abstract base class behavior.
- **File List:**
    - `A capsule/core/researcher.py`
    - `A tests/test_core/test_researcher.py`
- **Change Log:**
    - Implemented the abstract base class for research providers. (2025-11-16)
