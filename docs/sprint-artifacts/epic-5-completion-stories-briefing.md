# Briefing: Epic 5 Completion Stories

**Objective:** To complete the remaining implementation and testing work for Epic 5, "Validation Engine," to ensure it is robust, fully functional, and ready to be a dependency for Epic 6.

**Source of Truth:** The action items from the AI Senior Developer Review on story `5-1-core-validator-implementation`.

## Required Tasks

Execute the following implementation and testing tasks. Treat these as the acceptance criteria for this work.

### 1. Implement Core Validation Logic (High Priority)
- **Task:** Implement the `validate_data_types` method in `capsule/core/validator.py`. This method was left as a placeholder and is a critical gap.
- **Task:** Implement the full logic for the `validate_frontmatter_schema` method. It should correctly parse the schema from the cypher and validate each note's frontmatter against it.

### 2. Expand Test Suite (High Priority)
- **Task:** Add comprehensive unit tests in `tests/test_core/test_validator.py` to cover the following failure scenarios:
    - A capsule with an invalid `capsule-cypher.yaml` file.
    - A capsule with files listed in the cypher that are missing from the directory.
    - A capsule with extra files in the directory that are not listed in the cypher.
    - A note with frontmatter that is missing required fields.
    - A note with frontmatter that has fields with incorrect data types.

### 3. Code Quality Improvements (Medium Priority)
- **Task:** Refactor the `Validator` class to parse the `capsule-cypher.yaml` file only once at initialization, rather than multiple times in different methods.
- **Task:** Add explicit assertions to the `test_validate_capsule_with_valid_capsule` test to ensure it is correctly verifying success.

**Expected Output:**
- Modified Python files with the completed logic.
- New and updated test files.
- All existing and new tests passing with 100% success.
