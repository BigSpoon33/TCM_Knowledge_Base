---
story_id: "2.3"
epic_id: "2"
title: "User Config System"
status: "review"
---

## 1. Story Description

As a developer, I want a robust configuration system that loads settings from a YAML file, provides default values, and makes them easily accessible throughout the application, so that the CLI can be configured by the user without modifying the source code.

## 2. Acceptance Criteria

1.  **Config Model:** A `Config` class is created in `capsule/models/config.py` that can load, parse, and provide default values for the user's configuration.
2.  **YAML Loading:** The system loads configuration from `~/.capsule/config.yaml` if it exists.
3.  **Default Creation:** If the configuration file does not exist, it is created with a default structure and sensible defaults.
4.  **Value Access:** The `Config` class provides a method to get configuration values using dot notation (e.g., `config.get('user.name')`).
5.  **Error Handling:** A `ConfigError` exception is raised for any issues related to loading or parsing the configuration.
6.  **Unit Tests:** The configuration system is thoroughly tested in `tests/test_models/test_config.py`.

## 3. Tasks

### Task 3.1: Create Config Model and Exceptions

-   [x] **Subtask 3.1.1:** Create the file `capsule/models/config.py`.
-   [x] **Subtask 3.1.2:** Implement the `Config` class with methods for loading, creating defaults, and getting values.
-   [x] **Subtask 3.1.3:** Add a `ConfigError` exception to `capsule/utils/exceptions.py`.

### Task 3.2: Develop Unit Tests

-   [x] **Subtask 3.2.1:** Create the test file `tests/test_models/test_config.py`.
-   [x] **Subtask 3.2.2:** Write a test to verify that a default `config.yaml` is created if one does not exist.
-   [x] **Subtask 3.2.3:** Write a test to confirm that existing values are loaded correctly from a `config.yaml` file.
-   [x] **Subtask 3.2.4:** Write a test for the dot notation access method (`get()`).
-   [x] **Subtask 3.2.5:** Write a test to ensure `ConfigError` is raised on malformed YAML.

## 4. Dev Notes

-   The implementation should follow the `Config` class structure outlined in the architecture document.
-   The `safe_write` function from `capsule.utils.file_ops` should be used to create the default configuration file to ensure atomicity.
-   The `PyYAML` library is the designated tool for this task as per the architecture.

### Learnings from Previous Story

**From Story 2.2 (Status: done)**

-   **New Service Created**: `file_ops.py` is available for safe file writing. Use `safe_write()` when creating the default config file.
-   **New Exception**: `FileError` is available and should be handled if file operations fail.
-   **Testing Pattern**: Follow the testing patterns established in `tests/test_utils/test_file_ops.py` for the new config tests.

[Source: docs/sprint-artifacts/2-2-file-operations-utilities.md#Dev-Agent-Record]

### References

-   [Source: docs/architecture.md#Configuration-Management]
-   [Source: docs/architecture.md#Decision-Summary-Table] (re: PyYAML)

## 5. Dev Agent Record

- **Context Reference:** [2-3-user-config-system.context.xml](./stories/2-3-user-config-system.context.xml)
- **Completion Notes:**
    - Refactored the existing `capsule/models/config.py` to align with the architecture and acceptance criteria.
    - Implemented a deep merge strategy to combine default and user-provided configurations.
    - Added `ConfigError` to `capsule/utils/exceptions.py`.
    - Wrote a comprehensive test suite in `tests/test_models/test_config.py` which passed successfully.
- **File List:**
    - `M capsule/models/config.py`
    - `M capsule/utils/exceptions.py`
    - `M tests/test_models/test_config.py`
- **Change Log:**
    - Implemented user configuration system. (2025-11-16)

---

## Senior Developer Review (AI)

**Reviewer:** BMad
**Date:** 2025-11-17
**Outcome:** Approve

### Summary
The implementation of the user configuration system is excellent. All acceptance criteria have been met, and the code is well-structured and thoroughly tested. The system correctly loads, merges, and saves configurations, and the error handling is robust.

### Key Findings
- **Minor:** The test function `test_load_existing_config` is duplicated in `tests/test_models/test_config.py`. This is a minor code quality issue and does not affect the functionality.

### Acceptance Criteria Coverage
| AC# | Description | Status | Evidence |
|---|---|---|---|
| 1 | Config Model | IMPLEMENTED | `capsule/models/config.py:21` |
| 2 | YAML Loading | IMPLEMENTED | `capsule/models/config.py:35` |
| 3 | Default Creation | IMPLEMENTED | `tests/test_models/test_config.py:21` |
| 4 | Value Access | IMPLEMENTED | `capsule/models/config.py:103` |
| 5 | Error Handling | IMPLEMENTED | `capsule/utils/exceptions.py:15` |
| 6 | Unit Tests | IMPLEMENTED | `tests/test_models/test_config.py` |

**Summary:** 6 of 6 acceptance criteria fully implemented.

### Task Completion Validation
| Task | Marked As | Verified As | Evidence |
|---|---|---|---|
| 3.1.1 | [x] | VERIFIED COMPLETE | `capsule/models/config.py` exists |
| 3.1.2 | [x] | VERIFIED COMPLETE | `Config` class is implemented |
| 3.1.3 | [x] | VERIFIED COMPLETE | `ConfigError` is in `exceptions.py` |
| 3.2.1 | [x] | VERIFIED COMPLETE | `test_config.py` exists |
| 3.2.2 | [x] | VERIFIED COMPLETE | `test_create_default_config` passes |
| 3.2.3 | [x] | VERIFIED COMPLETE | `test_load_existing_config` passes |
| 3.2.4 | [x] | VERIFIED COMPLETE | `test_get_nested_value` passes |
| 3.2.5 | [x] | VERIFIED COMPLETE | `test_malformed_yaml` passes |

**Summary:** 8 of 8 completed tasks verified.

### Action Items
**Advisory Notes:**
- Note: Remove the duplicated `test_load_existing_config` function from `tests/test_models/test_config.py` in a future refactoring.
