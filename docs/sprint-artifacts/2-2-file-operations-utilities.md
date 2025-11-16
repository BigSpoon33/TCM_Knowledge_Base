---
story_id: "2.2"
epic_id: "2"
title: "File Operations Utilities"
status: "drafted"
---

## 1. Story Description

As a developer, I want a centralized file operations utility module that provides safe, consistent, and well-tested functions for common file tasks like reading, writing, and copying. This will ensure that all file manipulations across the application are robust, handle errors gracefully, and follow standard practices like using UTF-8 encoding and atomic writes.

## 2. Acceptance Criteria

1.  **FileOps Utility Module:** A module is created at `capsule/utils/file_ops.py` containing static utility functions.
2.  **Safe Write Function:** A `safe_write(path, content)` function is implemented that performs an atomic write by writing to a temporary file and then renaming it.
3.  **UTF-8 Enforcement:** All file reading and writing functions must enforce UTF-8 encoding.
4.  **Robust Error Handling:** Functions should raise custom `FileError` exceptions (defined in `capsule/utils/exceptions.py`) for issues like permissions errors or file not found.
5.  **Comprehensive Testing:** The module is fully tested in `tests/test_utils/test_file_ops.py`, covering success cases, error conditions, and edge cases.

## 3. Tasks

### Task 3.1: Create FileOps Module and Exceptions

-   **Subtask 3.1.1:** Create the file `capsule/utils/file_ops.py`.
-   **Subtask 3.1.2:** Add a `FileError` exception to `capsule/utils/exceptions.py`.

### Task 3.2: Implement Core File Functions

-   **Subtask 3.2.1:** Implement `safe_write(path: Path, content: str) -> None`.
-   **Subtask 3.2.2:** Implement `read_file(path: Path) -> str`.
-   **Subtask 3.2.3:** Ensure all file operations are wrapped in `try...except` blocks that raise `FileError`.

### Task 3.3: Develop Unit Tests

-   **Subtask 3.3.1:** Create the test file `tests/test_utils/test_file_ops.py`.
-   **Subtask 3.3.2:** Write tests for `safe_write` to confirm atomicity and correct content.
-   **Subtask 3.3.3:** Write tests for `read_file` for both success and file-not-found cases.
-   **Subtask 3.3.4:** Write tests to verify that `FileError` is raised appropriately on permissions errors (using mocks).

## 4. Dev Notes

-   This utility will build upon the principles outlined in the `architecture.md` document, specifically the sections on "File Operations" and "Security (NFR7: Data integrity)".
-   The `safe_write` function is critical for ensuring transactional integrity during capsule import and generation operations.
-   **Reference:** [Source: docs/architecture.md#NFR7-NFR12]
