# Story 9.5: template-validate-command

Status: done

## Story

As a content creator,
I want to implement the capsule template validate command,
so that I can ensure my custom templates are well-formed and comply with the project's schema.

## Acceptance Criteria

1. The `validate` command MUST be implemented under the `template` subcommand.
2. The command MUST accept a file path to a template schema YAML file as an argument.
3. The command MUST validate the schema for correct structure, required fields, and data types.
4. The command MUST output a success message if the template is valid.
5. The command MUST output a detailed error message if the template is invalid, specifying the issue.
6. The command's implementation MUST follow the CLI command structure pattern defined in the architecture.

## Tasks / Subtasks

- [x] **Task 1 (AC: #1-6)**: Implement the `validate` command logic in `capsule/commands/template.py`.
  - [x] Subtask 1.1: Add the Typer command function that accepts a file path.
  - [x] Subtask 1.2: Implement the core validation logic (likely in `capsule/core/validator.py` or a new utility).
  - [x] Subtask 1.3: Add success and error output messages using `rich`.
- [x] **Task 2 (AC: #1-6)**: Add unit tests for the `validate` command in `tests/test_commands/test_template.py`.
  - [x] Subtask 2.1: Create a valid sample template for testing.
  - [x] Subtask 2.2: Create an invalid sample template with errors.
  - [x] Subtask 2.3: Write a test case to verify the success output for the valid template.
  - [x] Subtask 2.4: Write a test case to verify the error output for the invalid template.

## Dev Notes

- Relevant architecture patterns and constraints: The `architecture.md` document specifies that CLI commands should be implemented using Typer. The command should be added to the `template` subcommand group. Unit tests should be written for the new command.
- Source tree components to touch: `capsule/commands/template.py`, `tests/test_commands/test_template.py`.
- Testing standards summary: Unit tests should cover validation of a valid template and a template with errors.

### Project Structure Notes

- The new `validate` command should be added to the existing `template.py` file in the `caps.le/commands` directory, following the pattern of other commands in that file.
- Unit tests should be added to the existing `test_template.py` file in `tests/test_commands`.
- **Clarification**: This command (`template validate`) is distinct from the main `validate` command. `template validate` checks the schema of a single template file, while the top-level `validate` command checks the integrity of an entire generated capsule.

### Learnings from Previous Story

**From Story 9-4-template-list-command (Status: done)**

- **File Modification Pattern**: The previous story successfully modified `capsule/commands/template.py` to add a new command and `tests/test_commands/test_template.py` for its tests. This confirms the correct locations for the current story's changes.
- **Output Formatting**: The use of the `rich` library for formatted table output is the established pattern for CLI commands.

[Source: docs/sprint-artifacts/9-4-template-list-command.md#Dev-Agent-Record]

### References

- [Source: docs/architecture.md#CLI-Command-Structure-Pattern]
- [Source: docs/epics.md#Epic-9-CLI-Commands---Generation--Templates]

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->
- docs/sprint-artifacts/stories/9-5-template-validate-command.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

- **Plan**:
  1.  **Implement `validate` command**: Add `validate` command to `capsule/commands/template.py`.
      -   Use `typer` to define the command.
      -   Accept `filepath` argument.
      -   Load the YAML file.
      -   Validate against `TemplateSchema` structure (domain_type, version, etc.).
      -   Use `rich` for output (Success/Error).
  2.  **Add Unit Tests**: Create `tests/test_commands/test_template.py` (or update if exists).
      -   Test with valid schema.
      -   Test with invalid schema (missing fields, wrong types).
      -   Test with non-existent file.

### Completion Notes List

- Implemented `validate` command in `capsule/commands/template.py` using `TemplateSchema` for validation.
- Added comprehensive unit tests in `tests/test_commands/test_template.py` covering success, missing fields, invalid YAML, and file not found scenarios.
- Verified all tests pass.

### File List

- capsule/commands/template.py
- tests/test_commands/test_template.py
