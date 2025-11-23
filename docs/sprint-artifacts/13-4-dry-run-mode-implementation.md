# Story 13.4: dry-run-mode-implementation

Status: done

## Story

As a user of the `obsidian-capsule-cli`,
I want to run commands in a "dry-run" mode,
so that I can preview what changes will be made to my file system without actually modifying anything.

## Acceptance Criteria

1. `capsule/utils/file_ops.py` is refactored to support dry-run mode, logging actions to console/log instead of executing them when enabled.
2. `capsule/commands/generate.py` accepts `--dry-run` flag and passes it to `ContentGenerator`.
3. `capsule/commands/import_cmd.py` accepts `--dry-run` flag and passes it to `CapsuleImporter`.
4. `capsule/commands/export.py` accepts `--dry-run` flag and passes it to `CapsuleExporter`.
5. Core logic classes (`ContentGenerator`, `CapsuleImporter`, `CapsuleExporter`) are updated to use the dry-run aware file operations for all side effects.
6. When `--dry-run` is used, console output clearly indicates "[DRY RUN]" for would-be actions (e.g., "Would write file: ...").
7. Unit tests verify `FileOps` behaves correctly in both normal and dry-run modes.
8. Integration tests verify commands with `--dry-run` do not create, modify, or delete files on the filesystem.

## Tasks / Subtasks

- [x] **Task 1: Refactor File Operations for Dry-Run** (AC: #1, #7)
  - [x] Update `capsule/utils/file_ops.py` to include a `FileContext` class or updated functions accepting `dry_run` state
  - [x] Implement safe wrappers for `write_text`, `mkdir`, `copy`, `remove`, etc.
  - [x] Add logging/console output for dry-run actions (using `rich` markup like `[yellow][DRY RUN][/yellow]`)
  - [x] Create unit tests in `tests/test_utils/test_file_ops.py` verifying both modes

- [x] **Task 2: Update Content Generator** (AC: #2, #5, #6)
  - [x] Update `ContentGenerator.__init__` or `generate` method to accept `dry_run` flag
  - [x] Replace direct file operations with `FileOps` calls
  - [x] Update `capsule/commands/generate.py` to add `--dry-run` option
  - [x] Verify "[DRY RUN]" output during generation preview

- [x] **Task 3: Update Capsule Importer** (AC: #3, #5, #6)
  - [x] Update `CapsuleImporter` to accept `dry_run` flag
  - [x] Replace direct file operations (backup, extract, merge writes) with `FileOps` calls
  - [x] Update `capsule/commands/import_cmd.py` to add `--dry-run` option
  - [x] Verify "[DRY RUN]" output during import preview

- [x] **Task 4: Update Capsule Exporter** (AC: #4, #5, #6)
  - [x] Update `CapsuleExporter` to accept `dry_run` flag
  - [x] Replace direct file operations (zip creation, folder copy) with `FileOps` calls
  - [x] Update `capsule/commands/export.py` to add `--dry-run` option
  - [x] Verify "[DRY RUN]" output during export preview

- [x] **Task 5: Integration Testing** (AC: #8)
  - [x] Create `tests/test_commands/test_dry_run_integration.py`
  - [x] Test `generate --dry-run` (assert no files created)
  - [x] Test `import --dry-run` (assert no backup/files created)
  - [x] Test `export --dry-run` (assert no zip/folder created)
  - [x] Verify console output contains expected dry-run messages

## Dev Notes

### Architecture Patterns and Constraints

- **FileOps Centralization**: All file system side effects MUST go through `capsule/utils/file_ops.py`. This is the single point of control for dry-run safety.
- **Dependency Injection**: Pass the `dry_run` state (or a configured `FileContext` object) down from the CLI command to the core logic classes. Avoid global state if possible.
- **Rich Integration**: Use `rich` for dry-run messages to make them distinct (e.g., yellow or dim color).
- **Logging**: Ensure dry-run actions are also logged to the file log (at INFO level) for auditability.

### Project Structure Notes

- **Refactoring**: `capsule/utils/file_ops.py` is currently a set of functions. Converting it to a class or adding a context manager might be cleaner for passing state, but simple function arguments are also acceptable if consistent.
- **Testing**: Ensure `tests/test_utils/test_file_ops.py` covers all mocked file operations to guarantee safety.

### References

- [Source: docs/sprint-artifacts/tech-spec-epic-13.md#2.3.3-Dry-Run-Interface]
- [Source: docs/architecture.md#CLI-Command-Structure-Pattern]
- [Source: docs/PRD.md#FR58]

## Dev Agent Record

### Context Reference

- [Story Context](stories/13-4-dry-run-mode-implementation.context.xml)

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List
- capsule/utils/file_ops.py
- capsule/core/generator.py
- capsule/commands/generate.py
- capsule/core/importer.py
- capsule/commands/import_cmd.py
- capsule/core/exporter.py
- capsule/commands/export.py
- capsule/core/packager.py
- tests/test_utils/test_file_ops.py
- tests/test_commands/test_dry_run_integration.py
- tests/test_commands/test_generate.py
- tests/test_commands/test_import.py
- tests/test_templates/test_capsule_dashboard.py
- tests/test_templates/test_master_dashboard.py
- tests/test_templates.py

## Learnings from Previous Story

**From Story 13-3 (Status: done)**

- **Rich Integration**: We successfully integrated `rich.progress`. Dry-run output should use `rich.console` or `typer.echo` with rich markup to be consistent.
- **Testing**: Integration tests using `CliRunner` are effective for verifying console output. We should use this to verify "[DRY RUN]" messages appear.
- **Cleanup**: `transient=False` was used for progress bars. For dry-run, we might want to ensure progress bars still show up (simulated) or are skipped/fast-forwarded. *Decision: Progress bars should probably still show to simulate the time/steps, or be skipped if operations are instant in dry-run. Let's keep them for realism but maybe speed them up if possible, or just let them run normally since no IO happens.*

[Source: stories/13-3-progress-indicators-rich-integration.md#Dev-Agent-Record]

## Senior Developer Review (AI)

### Reviewer: BMad
### Date: 2025-11-23
### Outcome: Approve

The implementation successfully introduces a robust dry-run mode across all major CLI commands (`generate`, `import`, `export`). The `FileOps` class provides a centralized and safe mechanism for handling file system side effects, ensuring that dry-run mode is respected. Comprehensive testing covers both unit-level file operations and integration-level command execution.

### Key Findings

- **Low Severity**:
  - Potential logic duplication for backup creation between `capsule/commands/import_cmd.py` and `capsule/core/importer.py` (`run` method). `import_cmd.py` handles it explicitly, while `importer.run` also has logic for it. Consider consolidating or deprecating `importer.run` if it's not used.

### Acceptance Criteria Coverage

| AC# | Description | Status | Evidence |
|-----|-------------|--------|----------|
| 1 | `capsule/utils/file_ops.py` refactored for dry-run | IMPLEMENTED | `capsule/utils/file_ops.py:14-123` |
| 2 | `generate` command accepts `--dry-run` | IMPLEMENTED | `capsule/commands/generate.py:23` |
| 3 | `import` command accepts `--dry-run` | IMPLEMENTED | `capsule/commands/import_cmd.py:23` |
| 4 | `export` command accepts `--dry-run` | IMPLEMENTED | `capsule/commands/export.py:21` |
| 5 | Core logic classes updated to use `FileOps` | IMPLEMENTED | `capsule/core/generator.py:26`, `capsule/core/importer.py:108`, `capsule/core/exporter.py:25`, `capsule/core/packager.py:23` |
| 6 | Console output indicates `[DRY RUN]` | IMPLEMENTED | `capsule/utils/file_ops.py:27`, `capsule/commands/generate.py:49` |
| 7 | Unit tests for `FileOps` | IMPLEMENTED | `tests/test_utils/test_file_ops.py` |
| 8 | Integration tests for dry-run | IMPLEMENTED | `tests/test_commands/test_dry_run_integration.py` |

**Summary:** 8 of 8 acceptance criteria fully implemented.

### Task Completion Validation

| Task | Marked As | Verified As | Evidence |
|------|-----------|-------------|----------|
| Refactor File Operations for Dry-Run | [x] | VERIFIED COMPLETE | `capsule/utils/file_ops.py` |
| Update Content Generator | [x] | VERIFIED COMPLETE | `capsule/core/generator.py`, `capsule/commands/generate.py` |
| Update Capsule Importer | [x] | VERIFIED COMPLETE | `capsule/core/importer.py`, `capsule/commands/import_cmd.py` |
| Update Capsule Exporter | [x] | VERIFIED COMPLETE | `capsule/core/exporter.py`, `capsule/commands/export.py` |
| Integration Testing | [x] | VERIFIED COMPLETE | `tests/test_commands/test_dry_run_integration.py` |

**Summary:** 5 of 5 completed tasks verified.

### Test Coverage and Gaps
- **Coverage**: Excellent coverage for the new functionality.
- **Gaps**: None identified for this specific feature.

### Architectural Alignment
- **Alignment**: Fully aligned with the architecture decision to centralize file operations in `FileOps` and pass `dry_run` state via dependency injection.
- **Violations**: None.

### Security Notes
- **Safety**: The implementation correctly prevents file system modifications when `dry_run` is enabled, which is the primary security concern for this feature.

### Best-Practices and References
- **Reference**: [Rich Library Documentation](https://rich.readthedocs.io/en/stable/) for console output.
- **Reference**: [Typer Documentation](https://typer.tiangolo.com/) for CLI options.

### Action Items

**Advisory Notes:**

## Change Log

- 2025-11-23: Senior Developer Review notes appended.


