---
story_id: "1.5"
epic_id: "1"
title: "Config Model"
status: "drafted"
---

## 1. Story Description

As a developer, I want a robust `Config` model to manage user-level and project-level configurations for the Capsule CLI. This model should handle loading, validation, and access to configuration settings, ensuring a clear separation between user preferences and project-specific settings.

## 2. Acceptance Criteria

1.  **Config Model Definition:** A `Config` dataclass is created in `capsule/models/config.py` that defines the structure of the configuration.
2.  **Hierarchical Loading:** The system can load configurations from both a global (`~/.config/capsule/config.yaml`) and a local (`<project_root>/.capsule/config.yaml`) file, with local settings overriding global ones.
3.  **YAML Persistence:** The model includes `from_yaml_file()` and `to_yaml_file()` methods for loading from and saving to YAML files using `ruamel.yaml` to preserve comments.
4.  **Validation:** A `validate()` method ensures that critical configuration fields (e.g., `api_key`) are present and correctly formatted.
5.  **Comprehensive Testing:** The model is accompanied by a full suite of tests in `tests/test_models/test_config.py`, achieving at least 95% code coverage.

## 3. Tasks

### Task 3.1: Define the Config Model

-   **Subtask 3.1.1:** Create `capsule/models/config.py`.
-   **Subtask 3.1.2:** Implement the `Config` dataclass with fields for settings like `llm_provider`, `api_key`, `default_model`, and `project_dir`.
-   **Subtask 3.1.3:** Add `__post_init__` to handle default value initialization.

### Task 3.2: Implement YAML I/O

-   **Subtask 3.2.1:** Add a `from_yaml_file(cls, path)` class method to load a config from a given path.
-   **Subtask 3.2.2:** Implement a `to_yaml_file(self, path)` method to save the current configuration state.
-   **Subtask 3.2.3:** Ensure `ruamel.yaml` is used for both methods to preserve comments and formatting.

### Task 3.3: Implement Hierarchical Config Loading

-   **Subtask 3.3.1:** Create a helper function or a dedicated class method that identifies the global and local config file paths.
-   **Subtask 3.3.2:** Implement the logic to load the global config first, then the local config, merging them so that local settings take precedence.

### Task 3.4: Implement Validation Logic

-   **Subtask 3.4.1:** Implement the `validate()` method within the `Config` model.
-   **Subtask 3.4.2:** The method should raise a `ValueError` or a custom `ConfigError` if required fields are missing or invalid.

### Task 3.5: Develop Unit Tests

-   **Subtask 3.5.1:** Create `tests/test_models/test_config.py`.
-   **Subtask 3.5.2:** Write tests for successful loading of a single config file.
-   **Subtask 3.5.3:** Write tests for the hierarchical loading logic (global, local, and merged).
-   **Subtask 3.5.4:** Write tests for the validation logic, checking both valid and invalid configurations.
-   **Subtask 3.5.5:** Write tests for saving the configuration to a file.

## 4. Definition of Done

-   The `Config` model and all associated logic are fully implemented.
-   All unit tests are passing with at least 95% coverage.
-   Code quality checks (Black, Mypy) pass without errors.
-   The code has been reviewed and approved by another developer.
-   The feature branch is merged into `main`.
