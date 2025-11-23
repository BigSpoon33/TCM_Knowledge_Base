# Story 10.3: Implement `import` Command

Status: done

## Story

As a user,
I want to import a capsule into my vault with a preview and backup safety,
so that I can safely and confidently add new knowledge to my vault.

## Acceptance Criteria

1.  **AC-10.6**: The `capsule import <path>` command displays an accurate preview of changes (new files, updates, conflicts) and waits for user confirmation.
2.  **AC-10.7**: The import proceeds successfully after the user confirms the preview, creating a backup, and applying changes to the vault.
3.  **AC-10.8**: The `capsule import <path> --yes` command proceeds with the import without an interactive prompt.
4.  **AC-10.9**: The `capsule import <path> --dry-run` command displays the preview and exits without making any changes.
5.  **AC-10.10**: A backup of the vault is automatically created before the import process begins (unless `--no-backup` is specified).

## Tasks / Subtasks

- [x] **Task 1: Implement `import_capsule` Command Structure** (AC: #1, #3, #4)
    - [x] Subtask 1.1: Create `capsule/commands/import_cmd.py`.
    - [x] Subtask 1.2: Define the `import_capsule` function with Typer arguments: `path`, `auto_approve`, and `dry_run`.
    - [x] Subtask 1.3: Add the new command to the main CLI app in `capsule/cli.py`.
- [x] **Task 2: Integrate Core Importer and Preview Logic** (AC: #1, #4)
    - [x] Subtask 2.1: In the command, instantiate the `Importer` service from `capsule.core.importer`.
    - [x] Subtask 2.2: Call the `importer.get_preview()` method to get the `ImportPreview` data.
    - [x] Subtask 2.3: Implement a `rich`-based display function to format and print the preview attractively.
    - [x] Subtask 2.4: Implement the `--dry-run` logic to show the preview and exit.
- [x] **Task 3: Implement Interactive Approval and Execution** (AC: #2, #3)
    - [x] Subtask 3.1: If not `--yes` or `--dry-run`, use the `questionary` library to prompt the user for confirmation.
    - [x] Subtask 3.2: If the user confirms, call the `importer.execute_import()` method.
    - [x] Subtask 3.3: Handle user cancellation gracefully, exiting with a clear message.
- [x] **Task 4: Implement Comprehensive Testing** (AC: #1, #2, #3, #4, #5)
    - [x] Subtask 4.1: Create `tests/commands/test_import.py`.
    - [x] Subtask 4.2: Write unit tests, mocking the `Importer` service to verify it's called correctly based on flags (`--yes`, `--dry-run`).
    - [x] Subtask 4.3: Write an E2E test that runs `capsule import` on a fixture capsule against a temporary vault.
    - [x] Subtask 4.4: In the E2E test, verify that the backup is created, files are correctly added/merged, and the final vault state is as expected.
    - [x] Subtask 4.5: Add an E2E test for the `--dry-run` flag to ensure no changes are made.
- [x] **Task 5: Finalize Documentation and Error Handling**
    - [x] Subtask 5.1: Add a detailed docstring with examples to the `import_capsule` command.
    - [x] Subtask 5.2: Implement robust error handling for `CapsuleError` exceptions raised by the core services.

### Review Follow-ups (AI)
- [x] [AI-Review][Low] Add examples to the docstring of the import_capsule function in capsule/commands/import_cmd.py.
- [x] [AI-Review][Low] Add an explicit E2E test to verify that a backup file is created during a standard import.

## Dev Notes

### Requirements Context Summary

*   **Epic**: CLI Commands - Validation & Import/Export
*   **User Story**: As a user, I want to import a capsule into my vault with a preview and backup safety, so that I can safely and confidently add new knowledge to my vault.
*   **Acceptance Criteria**:
    *   The `capsule import <path>` command displays an accurate preview of changes (new files, updates, conflicts) and waits for user confirmation.
    *   The import proceeds successfully after the user confirms the preview.
    *   The `capsule import <path> --yes` command proceeds with the import without an interactive prompt.
    *   The `capsule import <path> --dry-run` command displays the preview and exits without making any changes.
    *   A backup of the vault is automatically created before the import process begins.
*   **Component References**: `capsule.commands.import_cmd`, `capsule.core.importer`, `capsule.core.merger`, `capsule.utils.backup`.
*   **Constraints**: Must use `Importer`, `Merger`, and `Backup` services. Must follow Typer CLI patterns.
*   **Testing**: Unit tests with mocking, E2E tests with fixtures.

- **Architectural Pattern**: Follow the standard CLI command pattern: the command function in `capsule/commands/import_cmd.py` should be a thin wrapper that parses inputs and orchestrates calls to the core `Importer` service. All business logic belongs in the core services.
- **Source Tree Components**:
    - **Create**: `capsule/commands/import_cmd.py`, `tests/commands/test_import.py`
    - **Modify**: `capsule/cli.py` (to register the new command)
    - **Use**: `capsule/core/importer.py`, `capsule/core/merger.py`, `capsule/utils/backup.py`, `capsule/exceptions.py`
- **Testing Standards**: A strong emphasis is required on E2E tests for this command, as it involves file system changes and user interaction. Use a temporary directory (`tmp_path` fixture in pytest) as a simulated vault for E2E tests to ensure they are isolated and repeatable.

### Project Structure Notes

*   **Alignment**: This story follows the established architectural pattern for CLI commands. The new command will be implemented in `capsule/commands/import_cmd.py` (named to avoid conflict with the Python `import` keyword), with corresponding tests in `tests/commands/test_import.py`.
*   **Dependencies**: The command will act as an orchestrator, invoking the core logic from existing services: `capsule.core.importer.Importer`, `capsule.core.merger.Merger`, and `capsule.utils.backup.BackupManager`. This maintains a clean separation of concerns.
*   **Learnings from Previous Story (10-2-export-command)**:
    *   **Mocking is critical**: Unit tests *must* correctly mock the core service (`Importer`) to isolate the command's logic, similar to how `Packager` was mocked for the `export` command.
    *   **Specific Error Handling**: The implementation must catch specific exceptions from the importer and merger services (e.g., `MergeConflict`, `BackupFailedError`, `InvalidCapsuleError`) and provide user-friendly error messages.
    *   **Structured Logging**: All user feedback (previews, summaries, errors) must be routed through the established `logger` with `RichHandler`, not `print()` or `console.print()`.

### References

- **Primary Spec**: [docs/sprint-artifacts/tech-spec-epic-10.md#APIs-and-Interfaces](docs/sprint-artifacts/tech-spec-epic-10.md#APIs-and-Interfaces)
- **Architecture Guide**: [docs/architecture.md#Epic-Group-4-ImportExport-Operations-FR26-FR31](docs/architecture.md#Epic-Group-4-ImportExport-Operations-FR26-FR31)
- **CLI Pattern**: [docs/architecture.md#CLI-Command-Structure-Pattern](docs/architecture.md#CLI-Command-Structure-Pattern)

## Dev Agent Record

### Context Reference

### Context Reference

- docs/sprint-artifacts/stories/10-3-import-command-implementation.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List
- Implemented `capsule import` command with interactive preview using `questionary` and `rich`.
- Integrated with `Importer` service for extraction, validation, preview, and execution.
- Added support for `--yes` (auto-approve), `--dry-run`, and `--no-backup` flags.
- Updated `Config` model to support `import` settings (mapped to `import_settings` to avoid keyword conflict).
- Added comprehensive unit tests and E2E tests covering all scenarios.
- ✅ Resolved review finding [Low]: Add examples to the docstring of the import_capsule function in capsule/commands/import_cmd.py.
- ✅ Resolved review finding [Low]: Add an explicit E2E test to verify that a backup file is created during a standard import.

### File List
- capsule/commands/import_cmd.py
- capsule/models/config.py
- tests/commands/test_import.py
- tests/commands/test_import_e2e.py

## Change Log
- 2025-11-22: Story drafted by BMad.
- 2025-11-22: Implementation completed by Dev Agent.
- 2025-11-22: Addressed code review findings - 2 items resolved (Date: 2025-11-22)
- 2025-11-22: Story approved by BMad.

---
# Senior Developer Review (AI)

- **Reviewer:** BMad
- **Date:** 2025-11-22
- **Outcome:** Approve
- **Summary:** The implementation of the `import` command is well-executed and adheres to the project's architecture. The code is clean, the command structure is correct, and the core logic is properly delegated to the `Importer` service. The previous review's minor findings have been addressed, and the command is ready for use.
- **Key Findings:**
    - **LOW:** The docstring for the `import_capsule` function in `capsule/commands/import_cmd.py` is missing examples.
    - **LOW:** There is no explicit E2E test to verify that a backup is created during a standard import.
- **Acceptance Criteria Coverage:**
    - **AC-10.6:** IMPLEMENTED
    - **AC-10.7:** IMPLEMENTED
    - **AC-10.8:** IMPLEMENTED
    - **AC-10.9:** IMPLEMENTED
    - **AC-10.10:** IMPLEMENTED
- **Task Completion Validation:** All tasks are verified complete.
- **Action Items:**
    - `[x] [Low] Add examples to the docstring of the import_capsule function in capsule/commands/import_cmd.py.`
    - `[x] [Low] Add an explicit E2E test to verify that a backup file is created during a standard import.`

