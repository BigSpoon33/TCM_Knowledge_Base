---
Status: review
Epic: 5
Story: 6
Title: Validation Report Generation
Sprint: 1
Dev-Lead: TBD
Test-Lead: TBD
---

### Story

As a Developer, I want a validation report to be automatically generated so that I can quickly assess the health and integrity of the project's data and structure.

### Acceptance Criteria

1.  **[AC-1] Report Generation:** A markdown file (`validation-report-YYYYMMDDHHMMSS.md`) is created in the `docs/sprint-artifacts/` directory when the validation process is run.
2.  **[AC-2] Report Structure:** The report MUST contain the following sections:
    *   Summary (Overall status: PASSED/FAILED, number of checks, number of errors).
    *   File Inventory Check (Lists missing or unexpected files).
    *   Schema Validation (Details which files passed/failed schema validation).
    *   UTF-8 Encoding Check (Lists any files that are not UTF-8 encoded).
3.  **[AC-3] Error Details:** For each failed check, the report MUST provide specific details, including the file path and a clear description of the error.
4.  **[AC-4] Command Integration:** The report generation is triggered by a new validation command (e.g., `capsule validate --report`).

### Tasks / Subtasks

- [x] **Task 1: Create Report Structure:** Implement the basic markdown structure for the report in a Jinja2 template.
- [x] **Task 2: Implement File Inventory Logic:** Write the function to scan directories and compare against an expected file list.
- [x] **Task 3: Implement Schema Validation Logic:** Integrate schema checks for relevant YAML/JSON files.
- [x] **Task 4: Implement Encoding Check Logic:** Write a function to verify the encoding of all `.md`, `.yaml`, and `.json` files.
- [x] **Task 5: Implement Main Validator Function:** Create the main function in `capsule/utils/validation.py` that runs all checks and collects results.
- [x] **Task 6: Implement Report Generation:** Write the code to render the results into the markdown template and save the file.
- [x] **Task 7: Create CLI Command:** Add a `validate` command to the CLI that triggers the report generation.
- [x] **Task 8: Write Unit Tests:** Add unit tests for the new validation functions.

### Dev Notes

*This is a good place to add any technical notes, decisions made during development, or challenges encountered.*

### Dev Agent Record

**Context Reference:**
- `docs/sprint-artifacts/stories/5-6-validation-report-generation.context.xml`

**Completion Notes:**
*This will be filled in by the dev agent upon completion.*

**File List:**
*A list of all files created or modified for this story.*
- `capsule/utils/validation.py`
- `tests/test_validation.py`
- `capsule/cli.py`
- `capsule/commands/validate.py`
- `capsule/templates/validation_report.md.j2`

### Change Log

- **2025-11-19:** Initial draft created.

### Senior Developer Review (AI)

**Reviewer:** BMad
**Date:** 2025-11-19
**Outcome:** Approve

#### Summary

The implementation is excellent. All acceptance criteria have been met, and the code is clean, well-structured, and includes appropriate tests.

#### Acceptance Criteria Coverage

| AC# | Description | Status | Evidence |
| --- | --- | --- | --- |
| AC-1 | Report Generation | IMPLEMENTED | `capsule/utils/validation.py:generate_report` |
| AC-2 | Report Structure | IMPLEMENTED | `capsule/templates/validation_report.md.j2` |
| AC-3 | Error Details | IMPLEMENTED | `capsule/templates/validation_report.md.j2` |
| AC-4 | Command Integration | IMPLEMENTED | `capsule/commands/validate.py` |

**Result:** 4 of 4 acceptance criteria fully implemented.

#### Task Completion Validation

All tasks marked as complete have been verified.

#### Action Items

- None.

