# Ad-Hoc Code Review

**Reviewer:** BMad
**Date:** 2025-11-22
**Files Reviewed:** `capsule/` directory
**Review Focus:** General quality and standards

## Outcome: Changes Requested

The codebase is functional and has a good structure, but there are several areas where the code quality can be improved. The most significant issues are the inconsistent error handling, the "god" functions/methods, and the hardcoded logic.

## Key Findings

### High Severity

*   None

### Medium Severity

*   **Inconsistent Error Handling:** The error handling strategy is inconsistent. Some functions print warnings, while others catch broad exceptions. This makes it difficult to debug issues and provide clear feedback to the user. A centralized error handling strategy with custom exceptions is recommended.
*   **"God" Functions/Methods:** Several functions and methods are doing too much, making them difficult to read, test, and maintain. Specifically, `capsule/commands/generate.py:generate` and `capsule/core/generator.py:ContentGenerator.generate` should be refactored into smaller, more focused units.
*   **Hardcoded Logic:** There is a significant amount of hardcoded logic, especially related to file naming conventions and the types of materials that can be generated. This should be refactored to be more data-driven and extensible.

### Low Severity

*   **Brittle JSON Parsing:** The code that cleans up JSON responses from the LLM is brittle and could fail if the LLM's output changes slightly. A more robust parsing method should be used.
*   **Configuration Management:** Configuration is loaded within each command. It would be better to load the configuration once in the main CLI entry point and pass it down to the commands.

## Action Items

### Code Changes Required

*   `[ ]` **[Medium]** Refactor the error handling to use a consistent strategy with custom exceptions.
*   `[ ]` **[Medium]** Refactor the `generate` command and the `ContentGenerator.generate` method to reduce their complexity and improve separation of concerns.
*   `[ ]` **[Medium]** Refactor the hardcoded logic for material types and file naming into a more data-driven or plugin-based architecture.
*   `[ ]` **[Low]** Implement a more robust method for parsing JSON from LLM responses.
*   `[ ]` **[Low]** Refactor the configuration management to load the configuration once and pass it to the commands.

### Advisory Notes

*   Note: The project has a solid foundation with a well-structured CLI and modern tooling. These changes will help to improve the long-term maintainability and extensibility of the codebase.

---
# Ad-Hoc Code Review Report (Story 11-8)

**Review Details:**
- **Review Type**: Ad-Hoc Code Review
- **Reviewer**: BMad
- **Date**: 2025-11-22
- **Files Reviewed**: 
  - `capsule/core/importer.py`
  - `capsule/models/cypher.py`
  - `capsule/utils/dataview_queries.py`
  - `capsule/templates/master-dashboard.md.j2`
  - `capsule/templates/capsule-dashboard.md.j2`
- **Review Focus**: General quality, standards, and correctness.

**Outcome**: Changes Requested

**Summary**:
The review focused on the core logic for dashboard generation during capsule import. While the implementation appears functional, several areas require improvement to enhance maintainability, robustness, and adherence to best practices. The most critical issue is the incomplete story file, which prevents a full review against acceptance criteria.

**Key Findings**:

| Severity | File | Issue |
|---|---|---|
| **High** | `docs/sprint-artifacts/stories/11-8-dashboard-generation-during-import.md` | **Incomplete Story File**: The story file is missing the `Story`, `Acceptance Criteria`, and `Tasks` sections. This is a critical process issue that blocks systematic review and validation. |
| **Medium** | `capsule/core/importer.py` | **Hardcoded Template Path**: The path to templates (`capsule/templates`) is hardcoded in `generate_dashboards` and `load_domain_sections`. This reduces flexibility and makes the code harder to test and maintain. The path should be configurable or dynamically located. |
| **Low** | `capsule/core/importer.py` | **Redundant Method**: The `generate_preview` method is a direct alias for `analyze_impact`. This adds unnecessary code and can cause confusion. |
| **Low** | `capsule/models/cypher.py` | **Unused Import**: The `io` module is imported but never used. |
| **Low** | `capsule/utils/dataview_queries.py`| **Query Construction**: Dataview queries are built using f-strings. While not a direct security risk here, this is poor practice and can be brittle. A safer, more structured approach should be used. |

**Action Items**:

**Code Changes Required:**
- [ ] **[High]** Populate the story file `docs/sprint-artifacts/stories/11-8-dashboard-generation-during-import.md` with the complete user story, acceptance criteria, and implementation tasks.
- [ ] **[Medium]** Refactor `importer.py` to remove the hardcoded `capsule/templates` path. Pass the template directory as a configuration parameter or discover it dynamically. [file: `capsule/core/importer.py`:690, 781]
- [ ] **[Low]** Remove the redundant `generate_preview` method from `importer.py`. [file: `capsule/core/importer.py`:609-622]
- [ ] **[Low]** Remove the unused `import io` statement from `cypher.py`. [file: `capsule/models/cypher.py`:3]

**Advisory Notes:**
- Note: Consider refactoring the query-building functions in `dataview_queries.py` to avoid direct string formatting, improving robustness.
- Note: The DataviewJS queries in the dashboard templates are complex. Adding comments or breaking them into smaller, more manageable functions would improve maintainability.
