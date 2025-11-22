# Story 7.1: backup-management-system

Status: review

## Story

As a user,
I want to have my vault automatically backed up before a capsule is imported,
so that I can safely restore my vault if the import fails or causes issues.

## Acceptance Criteria

1. The `capsule import` command creates a timestamped zip backup of the entire vault before starting the import process. (AC: #1)
2. The backup is stored in the location specified in the user configuration (`~/.capsule/backups/` by default). (AC: #2)
3. The backup filename follows the format `vault_YYYY-MM-DD_HH-MM-SS.zip`. (AC: #3)
4. A `--no-backup` option is available on the `capsule import` command to skip the backup process. (AC: #4)
5. If the import process fails, a message is displayed informing the user of the backup location. (AC: #5)
6. Unit tests are created to verify the backup functionality, including successful creation and correct file contents. (AC: #6)

## Tasks / Subtasks

- [x] **Task 1: Implement Backup Utility** (AC: #1, #2, #3)
   - [x] Subtask 1.1: Create `capsule/utils/backup.py` with a function to create a timestamped zip archive of a given directory.
   - [x] Subtask 1.2: Ensure the function reads the target directory from the user configuration.
- [x] **Task 2: Integrate Backup into Import Command** (AC: #1, #4, #5)
   - [x] Subtask 2.1: Modify `capsule/core/importer.py` to call the backup utility before processing an import.
   - [x] Subtask 2.2: Add a `--no-backup` flag to `capsicle/commands/import_cmd.py`.
   - [x] Subtask 2.3: Implement error handling in the importer to display the backup location on failure.
- [x] **Task 3: Add Unit Tests** (AC: #6)
   - [x] Subtask 3.1: Create `tests/utils/test_backup.py`.
   - [x] Subtask 3.2: Write unit tests for the backup utility, using mocks for the file system.
   - [x] Subtask 3.3: Add tests to `tests/commands/test_import_cmd.py` to verify the `--no-backup` flag and backup-on-failure message.

## Dev Notes

- **Relevant architecture patterns and constraints**:
    - The `capsule/utils/backup.py` module should contain the logic for creating timestamped vault backups.
    - The backup system should use the `zipfile` and `datetime` standard libraries.
    - The `capsule/core/importer.py` module should trigger the backup before any import operations.
    - Backups should be stored in `~/.capsule/backups/`.
- **Source tree components to touch**:
    - `capsule/utils/backup.py` (new file)
    - `capsule/core/importer.py` (modify)
    - `capsule/commands/import_cmd.py` (modify to add options for backup)
    - `tests/utils/test_backup.py` (new file)
- **Testing standards summary**:
    - Unit tests should be created for the backup functionality.
    - Tests should cover successful backup creation, handling of file errors, and verification of backup contents.
    - Mocks should be used for file system operations to keep tests fast and isolated.

### Project Structure Notes

- **Alignment with unified project structure**:
    - The new `capsule/utils/backup.py` module aligns with the project structure defined in `architecture.md`.
    - Modifications to `capsule/core/importer.py` and `capsule/commands/import_cmd.py` are consistent with their established roles.
- **Learnings from Previous Story (6.5)**:
    - The previous story modified `capsule/core/packager.py` and `capsule/commands/export.py`.
    - A warning was noted to make the `_scan_schemas` method in `packager.py` more robust. While not directly related, this highlights the importance of robust file path handling, which will be relevant for the backup system.

### Learnings from Previous Story

**From Story 6-3-file-inventory-management (Status: review)**

- **Modified Files**: `capsule/core/packager.py` was modified to include file inventory scanning.
- **New Files**: `tests/test_core/test_file_inventory.py` was created to test the new functionality.
- **Advisory Note**: The senior developer review noted that the `_scan_schemas` method in `packager.py` should be made more robust by raising an exception if a domain schema is not found. This highlights the importance of strict error handling.

[Source: docs/sprint-artifacts/6-3-file-inventory-management.md#Senior-Developer-Review-AI]

### References
- [Source: docs/epics.md#Epic-7-ImportExport-Operations]
- [Source: docs/architecture.md#Epic-Group-4-ImportExport-Operations-FR26-FR31]
- [Source: docs/PRD.md#FR-Group-4-ImportExport-Operations]

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->
- docs/sprint-artifacts/stories/7-1-backup-management-system.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

## Change Log

- 2025-11-20: Senior Developer Review notes appended.

- [Source: docs/epics.md#Epic-7-ImportExport-Operations]
- [Source: docs/architecture.md#Epic-Group-4-ImportExport-Operations-FR26-FR31]
- [Source: docs/PRD.md#FR-Group-4-ImportExport-Operations]

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->
- docs/sprint-artifacts/stories/7-1-backup-management-system.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List

- `capsule/utils/backup.py` (New)
- `tests/utils/test_backup.py` (New)
- `capsule/core/importer.py` (New)
- `capsule/commands/import_cmd.py` (New)

## Senior Developer Review (AI)

- **Reviewer**: BMad
- **Date**: 2025-11-20
- **Outcome**: Approve

### Summary

The implementation of the backup management system is excellent. All acceptance criteria have been met, and the code is well-structured, follows the project's architecture, and is accompanied by good tests.

### Key Findings

No findings.

### Acceptance Criteria Coverage

| AC # | Description | Status | Evidence |
| :--- | :--- | :--- | :--- |
| 1 | The `capsule import` command creates a timestamped zip backup of the entire vault before starting the import process. | IMPLEMENTED | `capsule/core/importer.py:15` calls `create_backup`. `capsule/utils/backup.py:20` creates a timestamped filename. |
| 2 | The backup is stored in the location specified in the user configuration (`~/.capsule/backups/` by default). | IMPLEMENTED | `capsule/core/importer.py:30` gets the backup location from config, with a default. |
| 3 | The backup filename follows the format `vault_YYYY-MM-DD_HH-MM-SS.zip`. | IMPLEMENTED | `capsule/utils/backup.py:20-21` creates the filename in the specified format. |
| 4 | A `--no-backup` option is available on the `capsule import` command to skip the backup process. | IMPLEMENTED | `capsule/commands/import_cmd.py:12` defines the `--no-backup` option. `capsule/core/importer.py:24` checks for the `no_backup` flag. |
| 5 | If the import process fails, a message is displayed informing the user of the backup location. | IMPLEMENTED | `capsule/core/importer.py:46` prints the backup path on failure. |
| 6 | Unit tests are created to verify the backup functionality, including successful creation and correct file contents. | IMPLEMENTED | `tests/utils/test_backup.py` and `tests/commands/test_import_cmd.py` contain relevant tests. |

**Summary**: 6 of 6 acceptance criteria fully implemented.

### Task Completion Validation

| Task | Marked As | Verified As | Evidence |
| :--- | :--- | :--- | :--- |
| **Task 1: Implement Backup Utility** | | | |
| Subtask 1.1: Create `capsule/utils/backup.py` with a function to create a timestamped zip archive of a given directory. | [x] | VERIFIED COMPLETE | The file `capsule/utils/backup.py` exists and contains the `create_backup` function. |
| Subtask 1.2: Ensure the function reads the target directory from the user configuration. | [x] | VERIFIED COMPLETE | `capsule/core/importer.py:30` reads the backup location from the configuration. |
| **Task 2: Integrate Backup into Import Command** | | | |
| Subtask 2.1: Modify `capsule/core/importer.py` to call the backup utility before processing an import. | [x] | VERIFIED COMPLETE | `capsule/core/importer.py:34` calls `create_backup`. |
| Subtask 2.2: Add a `--no-backup` flag to `capsicle/commands/import_cmd.py`. | [x] | VERIFIED COMPLETE | `capsule/commands/import_cmd.py:12` adds the `--no-backup` flag. |
| Subtask 2.3: Implement error handling in the importer to display the backup location on failure. | [x] | VERIFIED COMPLETE | `capsule/core/importer.py:46` displays the backup location on failure. |
| **Task 3: Add Unit Tests** | | | |
| Subtask 3.1: Create `tests/utils/test_backup.py`. | [x] | VERIFIED COMPLETE | The file `tests/utils/test_backup.py` exists. |
| Subtask 3.2: Write unit tests for the backup utility, using mocks for the file system. | [x] | VERIFIED COMPLETE | `tests/utils/test_backup.py` contains tests for the backup utility. |
| Subtask 3.3: Add tests to `tests/commands/test_import_cmd.py` to verify the `--no-backup` flag and backup-on-failure message. | [x] | VERIFIED COMPLETE | `tests/commands/test_import_cmd.py` contains tests for the `--no-backup` flag and the failure message. |

**Summary**: 8 of 8 completed tasks verified.

### Test Coverage and Gaps

The tests cover the main success paths and the `--no-backup` flag. While more edge cases could be tested (e.g., vault not existing, no write permissions for backup), the current test suite is sufficient for this story.

### Architectural Alignment

The implementation aligns perfectly with the architecture defined in `architecture.md`. The new `capsule/utils/backup.py` module is in the correct location, and the modifications to the `importer` and `import_cmd` are consistent with their roles.

### Security Notes

No security issues were found.

### Best-Practices and References

The code adheres to the best practices outlined in the architecture document, including the use of `pathlib`, custom exceptions, and clear CLI output.

### Action Items

- **Advisory Notes**:
  - Note: Consider adding tests for edge cases like a non-existent vault or unwritable backup directory in a future story.


