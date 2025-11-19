# Story 4.4: Content Generator Core Logic

Status: review

## Story

As a developer,
I want to implement the core logic for the content generator,
so that I can orchestrate the research, templating, and validation processes to produce content capsules.

## Acceptance Criteria

1.  A `ContentGenerator` class is created in `capsule/core/generator.py`.
2.  The `ContentGenerator` class initializes and uses the `ResearchProvider` and `Validator`.
3.  The `ContentGenerator` has a method to load Jinja2 templates from the `capsule/templates` directory.
4.  The `ContentGenerator` has a `generate` method that takes a topic, template, and research data as input.
5.  The `generate` method orchestrates the following steps:
    *   Calls the `researcher` to get research data.
    *   Loads the specified Jinja2 template.
    *   Renders the template with the research data.
    *   Calls the `validator` to validate the generated content.
    *   Returns the generated content.
6.  Unit tests are created for the `ContentGenerator` class in `tests/test_core/test_generator.py`.

## Tasks / Subtasks

- [x] **Task 1: Create `ContentGenerator` Class Structure** (AC: #1)
  - [x] Subtask 1.1: Create the file `capsule/core/generator.py`.
  - [x] Subtask 1.2: Define the `ContentGenerator` class.
- [x] **Task 2: Implement Constructor** (AC: #2)
  - [x] Subtask 2.1: Implement the `__init__` method to accept `ResearchProvider` and `Validator` instances.
  - [x] Subtask 2.2: Store the provider and validator as instance attributes.
- [x] **Task 3: Implement Template Loading** (AC: #3)
  - [x] Subtask 3.1: Add a method to load Jinja2 templates from the `capsule/templates` directory.
- [x] **Task 4: Implement the `generate` Method** (AC: #4, #5)
  - [x] Subtask 4.1: Define the `generate` method signature.
  - [x] Subtask 4.2: Implement the orchestration logic: research, load template, render, validate.
  - [x] Subtask 4.3: Ensure the method returns the generated content.
- [x] **Task 5: Write Unit Tests** (AC: #6)
  - [x] Subtask 5.1: Create the test file `tests/test_core/test_generator.py`.
  - [x] Subtask 5.2: Write tests for the constructor and dependency injection.
  - [x] Subtask 5.3: Write tests for the `generate` method, mocking dependencies.

## Dev Notes

- **Architecture:** The `ContentGenerator` class should be implemented in `capsule/core/generator.py` and should orchestrate the research, templating, and validation processes. [Source: docs/architecture.md#Epic-Group-1:-Content-Generation-(FR1-FR10)]
- **Dependencies:** The `ContentGenerator` will depend on the `ResearchProvider` and `Validator` components. [Source: docs/architecture.md#Epic-Group-1:-Content-Generation-(FR1-FR10)]
- **Templates:** The `ContentGenerator` will load Jinja2 templates from the `capsule/templates/` directory. [Source: docs/architecture.md#Epic-Group-1:-Content-Generation-(FR1-FR10)]
- **Testing:** Unit tests are required for the `ContentGenerator` class. [Source: docs/architecture.md#Testing-Strategy]

### Project Structure Notes

- **New File:** `capsule/core/generator.py`
- **New Test File:** `tests/test_core/test_generator.py`

### References

- Cite all technical details with source paths and sections, e.g. [Source: docs/<file>.md#Section]

### Learnings from Previous Story

**From Story 4-3-study-material-templates (Status: review)**

- **New Files Created**: 
  - `capsule/templates/flashcard.md.j2`
  - `capsule/templates/quiz.md.j2`
- **Files Modified**: 
  - `tests/test_utils/test_templates.py` was updated with tests for the new templates.
- **Review Findings**: The previous story was approved with no outstanding action items, indicating the template creation pattern is solid.

[Source: docs/sprint-artifacts/4-3-study-material-templates.md#Dev-Agent-Record]

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->
- docs/sprint-artifacts/stories/4-4-content-generator-core-logic.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

- `capsule/core/generator.py` (new)
- `capsule/utils/validation.py` (modified)
- `tests/test_core/test_generator.py` (new)


## Senior Developer Review (AI)
**Reviewer:** BMad
**Date:** 2025-11-18
**Outcome:** Approve

### Summary
The implementation of the `ContentGenerator` class is well-executed and meets all acceptance criteria. The code is clean, the dependencies are correctly managed, and the unit tests provide good coverage.

### Key Findings
No significant findings.

### Acceptance Criteria Coverage
| AC# | Description | Status | Evidence |
|---|---|---|---|
| 1 | A `ContentGenerator` class is created in `capsule/core/generator.py`. | IMPLEMENTED | `capsule/core/generator.py:7` |
| 2 | The `ContentGenerator` class initializes and uses the `ResearchProvider` and `Validator`. | IMPLEMENTED | `capsule/core/generator.py:8` |
| 3 | The `ContentGenerator` has a method to load Jinja2 templates from the `capsule/templates` directory. | IMPLEMENTED | `capsule/core/generator.py:15` |
| 4 | The `ContentGenerator` has a `generate` method that takes a topic, template, and research data as input. | IMPLEMENTED | `capsule/core/generator.py:18` |
| 5 | The `generate` method orchestrates the research, templating, and validation steps. | IMPLEMENTED | `capsule/core/generator.py:19-23` |
| 6 | Unit tests are created for the `ContentGenerator` class in `tests/test_core/test_generator.py`. | IMPLEMENTED | `tests/test_core/test_generator.py` |

**Summary:** 6 of 6 acceptance criteria fully implemented.

### Task Completion Validation
| Task | Marked As | Verified As | Evidence |
|---|---|---|---|
| Task 1 | [x] | VERIFIED COMPLETE | `capsule/core/generator.py` |
| Task 2 | [x] | VERIFIED COMPLETE | `capsule/core/generator.py:8` |
| Task 3 | [x] | VERIFIED COMPLETE | `capsule/core/generator.py:15` |
| Task 4 | [x] | VERIFIED COMPLETE | `capsule/core/generator.py:18` |
| Task 5 | [x] | VERIFIED COMPLETE | `tests/test_core/test_generator.py` |

**Summary:** 5 of 5 completed tasks verified.

### Action Items
**Advisory Notes:**
- Note: The `Validator` class is a placeholder. A future story should implement proper validation logic.

