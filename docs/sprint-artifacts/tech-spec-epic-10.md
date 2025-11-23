# Epic Technical Specification: {{epic_title}}

Date: {{date}}
Author: BMad
Epic ID: 10
Status: Draft

---

## Overview

This epic focuses on implementing the remaining core user-facing commands for the Capsule CLI: `validate`, `export`, `import`, `status`, and `list`. These commands provide the primary interface for users to manage the lifecycle of capsules, ensuring data integrity, enabling distribution, and providing visibility into the vault's contents. This work builds directly upon the foundational CLI structure established in Epic 9 and leverages the core logic for packaging, validation, and merging developed in prior epics.

## Objectives and Scope

**In Scope:**
- Implementing the `capsule validate` command to run the validation engine against a capsule.
- Implementing the `capsule export` command to package a capsule into a distributable format.
- Implementing the `capsule import` command, including the interactive preview and backup process.
- Implementing the `capsule status` command to provide a high-level overview of the vault.
- Implementing the `capsule list` command to detail all installed capsules.
- Integrating these commands into the main Typer CLI application.
- Ensuring consistent error handling, progress indicators, and help documentation for all new commands.

**Out of Scope:**
- Implementing the core logic for validation, packaging, or merging (these are dependencies from other epics).
- Creating new merge strategies.
- GUI integrations for these commands.
- Advanced status analytics beyond a simple summary.

## System Architecture Alignment

This epic directly aligns with the "CLI Interface" (Epic Group 8) and "Import/Export Operations" (Epic Group 4) sections of the architecture. It involves creating the command-line entry points (`capsule/commands/*.py`) that orchestrate the core logic modules:
- `capsule/core/validator.py` is invoked by the `validate` command.
- `capsule/core/exporter.py` and `packager.py` are invoked by the `export` command.
- `capsule/core/importer.py`, `merger.py`, and `utils/backup.py` are invoked by the `import` command.
The implementation will follow the established patterns for Typer commands, including structured error handling, use of the `rich` library for output, and clear, example-driven help messages as defined in the architecture.

## Detailed Design

### Services and Modules

| Service/Module | Responsibilities | Inputs | Outputs | Owner |
| --- | --- | --- | --- | --- |
| `capsule.commands.validate` | Provides the `capsule validate` command. | Capsule path | Validation report (stdout) | Dev |
| `capsule.commands.export` | Provides the `capsule export` command. | Capsule path, output format | Packaged capsule file (.zip or folder) | Dev |
| `capsule.commands.import_cmd` | Provides the `capsule import` command. | Path to capsule file/folder | Import summary (stdout) | Dev |
| `capsule.commands.status` | Provides `status` and `list` commands. | Vault path (from config) | Formatted status/list (stdout) | Dev |
| `capsule.core.validator` | (Existing) Core validation logic. | Capsule object | ValidationResult object | Epic 5 |
| `capsule.core.exporter` | (Existing) Orchestrates capsule packaging. | Capsule object | Path to exported file | Epic 7 |
| `capsule.core.importer` | (Existing) Orchestrates capsule import. | Path to capsule | ImportResult object | Epic 7 |

### Data Models and Contracts

No new data models are introduced in this epic. The commands will use existing models:
- `capsule.models.Capsule`: Represents a capsule to be validated, exported, or imported.
- `capsule.models.cypher.CapsuleCypher`: Read during import and validation.
- `ValidationResult` (from `validator.py`): The data structure returned by the validation engine and formatted by the `validate` command.
- `ImportPreview` (from `importer.py`): The data structure used to render the interactive import preview.

### APIs and Interfaces

The primary interfaces are the CLI command signatures defined using Typer.

**`capsule validate`**
```python
def validate(
    path: Path = typer.Argument(..., help="Path to the capsule directory to validate."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output.")
):
    """Validates a capsule's structure, cypher, and contents against its schema."""
```

**`capsule export`**
```python
def export(
    path: Path = typer.Argument(..., help="Path to the capsule directory to export."),
    output_dir: Path = typer.Option(Path("."), "--output", "-o", help="Output directory for the exported file."),
    as_zip: bool = typer.Option(True, "--zip/--no-zip", help="Export as a .zip archive or a folder.")
):
    """Packages a capsule into a distributable format."""
```

**`capsule import`**
```python
def import_capsule(
    path: Path = typer.Argument(..., help="Path to the capsule file (.zip) or directory to import."),
    auto_approve: bool = typer.Option(False, "--yes", "-y", help="Automatically approve the import without a preview."),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show the import preview without performing the import.")
):
    """Imports a capsule into the vault, with an interactive preview."""
```

**`capsule status`**
```python
def status():
    """Shows a high-level status of the Obsidian vault, including number of capsules and notes."""
```

**`capsule list`**
```python
def list_capsules():
    """Lists all installed capsules with their version and domain."""
```

### Workflows and Sequencing

**Validation Workflow:**
1.  User runs `capsule validate <path>`.
2.  The `validate` command in `validate.py` is invoked.
3.  It instantiates the `Validator` from `core/validator.py`.
4.  The `Validator`'s `validate_capsule` method is called with the given path.
5.  The command receives a `ValidationResult` object.
6.  The command formats the result (using `rich` tables) and prints it to stdout.
7.  The process exits with code 0 on success or a non-zero code on validation failure.

**Import Workflow:**
1.  User runs `capsule import <path>`.
2.  The `import_capsule` command in `import_cmd.py` is invoked.
3.  It instantiates the `Importer` from `core/importer.py`.
4.  The `Importer.get_preview()` method is called.
5.  The command formats and displays the preview of changes.
6.  If not `--yes`, it prompts the user for confirmation.
7.  If confirmed, the `Importer.execute_import()` method is called.
    - This triggers the backup creation (`utils/backup.py`).
    - It then proceeds with the file operations and merging (`core/merger.py`).
8.  A final summary is printed to stdout.

## Non-Functional Requirements

### Performance
- **`validate`:** Should complete validation on a 100-note capsule in under 5 seconds.
- **`import` / `export`:** Should process a 100-note capsule in under 60 seconds, with the majority of the time expected for file I/O and zipping.
- **`status` / `list`:** Should return results almost instantly (<1 second) by scanning for capsule dashboard files rather than reading every note.

### Security
- **Input Sanitization:** All file paths provided by the user must be sanitized to prevent path traversal attacks.
- **Backup Integrity:** The pre-import backup process is critical and must complete successfully before any vault modifications are made.
- **No Arbitrary Execution:** The import process must not execute any code embedded within imported notes.

### Reliability/Availability
- **Transactional Imports:** Imports must be atomic. If any step fails (e.g., a file write error, a merge conflict), the entire operation should be rolled back by restoring the backup.
- **Idempotency:** Re-importing the same version of a capsule should result in no changes to the vault.
- **Clear Error States:** The CLI must exit with a non-zero status code on any failure, clearly indicating that the operation was not successful.

### Observability
- **Logging:** All command executions, especially `import` and `export`, will be logged to `~/.capsule/logs/operations.log` with details of the files processed. Validation errors will be logged to `~/.capsule/logs/validation.log`.
- **Progress Indicators:** Long-running operations (`import`, `export`) must use `rich` progress bars to provide real-time feedback to the user.
- **Verbose Mode:** A `--verbose` flag should provide detailed, step-by-step output for debugging purposes.

## Dependencies and Integrations

The implementation of these CLI commands relies entirely on the existing project dependencies. No new libraries are required. The primary integrations are between the new command modules and the existing core logic modules.

**Project Dependencies (from `pyproject.toml`):**
- **`typer`**: The core CLI framework used to define the commands, arguments, and options.
- **`rich`**: Used for formatted output, including tables for `list` and `status`, and progress bars for `import`/`export`.
- **`python-frontmatter`**: Used by the core logic to parse and handle note frontmatter.
- **`ruamel.yaml`**: Used by the core logic for safe YAML handling, especially in the cypher.
- **`pyyaml`**: Used for standard YAML parsing.
- **`questionary`**: Used by the `import` command to present the interactive confirmation prompt.
- **`google-generativeai`**: Not directly used by these commands, but a core project dependency.

**Internal Integrations:**
- `capsule.commands.validate` -> `capsule.core.validator.Validator`
- `capsule.commands.export` -> `capsule.core.exporter.Exporter`
- `capsule.commands.import_cmd` -> `capsule.core.importer.Importer`
- All commands integrate with `capsule.models.config.Config` to get vault settings.
- All commands use the custom exception classes defined in `capsule.exceptions`.

## Acceptance Criteria (Authoritative)

1.  **AC-10.1 (`validate`):** The `capsule validate <path>` command successfully invokes the core validation engine on the specified capsule path.
2.  **AC-10.2 (`validate`):** When validating a valid capsule, the command prints a success message and exits with status code 0.
3.  **AC-10.3 (`validate`):** When validating an invalid capsule, the command prints a formatted report of all errors and warnings and exits with a non-zero status code.
4.  **AC-10.4 (`export`):** The `capsule export <path>` command successfully packages the specified capsule into a `.zip` archive by default.
5.  **AC-10.5 (`export`):** The `capsule export <path> --no-zip` command successfully packages the specified capsule into a folder bundle.
6.  **AC-10.6 (`import`):** The `capsule import <path>` command displays an accurate preview of changes (new files, updates, conflicts) and waits for user confirmation.
7.  **AC-10.7 (`import`):** The import proceeds successfully after the user confirms the preview.
8.  **AC-10.8 (`import`):** The `capsule import <path> --yes` command proceeds with the import without an interactive prompt.
9.  **AC-10.9 (`import`):** The `capsule import <path> --dry-run` command displays the preview and exits without making any changes.
10. **AC-10.10 (`import`):** A backup of the vault is automatically created before the import process begins.
11. **AC-10.11 (`status`):** The `capsule status` command displays a summary of the vault, including the total number of notes and installed capsules.
12. **AC-10.12 (`list`):** The `capsule list` command displays a table of all installed capsules, showing their ID, version, and domain.

## Traceability Mapping

| AC # | Spec Section(s) | Component(s)/API(s) | Test Idea |
| --- | --- | --- | --- |
| AC-10.1 | Detailed Design: APIs | `commands.validate.validate()` -> `core.validator.Validator` | Unit test `validate` command, mocking the Validator to ensure it's called. |
| AC-10.2 | Detailed Design: Workflows | `commands.validate.validate()` | E2E test: run `capsule validate` on a known-good fixture capsule. |
| AC-10.3 | Detailed Design: Workflows | `commands.validate.validate()` | E2E test: run `capsule validate` on a fixture with a missing required field. |
| AC-10.4 | Detailed Design: APIs | `commands.export.export()` -> `core.exporter.Exporter` | E2E test: run `capsule export` and verify the `.zip` file is created correctly. |
| AC-10.5 | Detailed Design: APIs | `commands.export.export()` | E2E test: run `capsule export --no-zip` and verify the folder is created. |
| AC-10.6 | Detailed Design: Workflows | `commands.import_cmd.import_capsule()` -> `core.importer.Importer.get_preview()` | E2E test: run `capsule import` and capture stdout to verify the preview text. |
| AC-10.7 | Detailed Design: Workflows | `commands.import_cmd.import_capsule()` -> `core.importer.Importer.execute_import()` | E2E test: run `capsule import` on a test vault and verify files are created. |
| AC-10.8 | Detailed Design: APIs | `commands.import_cmd.import_capsule()` | E2E test: run `capsule import --yes` and verify it doesn't hang on a prompt. |
| AC-10.9 | Detailed Design: APIs | `commands.import_cmd.import_capsule()` | E2E test: run `capsule import --dry-run` and verify no files are changed in the vault. |
| AC-10.10 | NFRs: Reliability | `core.importer.Importer` -> `utils.backup.create_backup()` | Integration test: mock `create_backup` and verify it's called before import logic. |
| AC-10.11 | Detailed Design: APIs | `commands.status.status()` | E2E test: run `capsule status` on a fixture vault and check the output summary. |
| AC-10.12 | Detailed Design: APIs | `commands.status.list_capsules()` | E2E test: run `capsule list` on a fixture vault and check the output table. |

## Risks, Assumptions, Open Questions

- **Risk:** The core logic for import, export, and validation (developed in Epics 5, 6, 7) may have bugs or an unstable API. **Mitigation:** Implementations will be based on the contracts defined in the architecture. Integration tests will be crucial to verify the interaction between the CLI and core layers.
- **Risk:** Performance of `import`/`export` on capsules with thousands of files could be slow. **Mitigation:** The core logic should be optimized for batch file operations. The CLI will use progress bars to manage user expectations during long operations.
- **Assumption:** The core logic modules (`Validator`, `Importer`, `Exporter`) will be completed and available for integration.
- **Assumption:** The `rich` library is sufficient for all required terminal UI, including the import preview.
- **Question:** What is the most efficient way to discover all installed capsules for the `list` command? **Decision:** The command will scan for `capsule-dashboard.md` files within the vault, as this is a reliable and fast method for identifying installed capsules without needing to parse every note.

## Test Strategy Summary

The test strategy will follow the pyramid model defined in the architecture, with a strong emphasis on end-to-end tests for these user-facing commands.

- **Unit Tests:**
    - Test the command functions in isolation (`validate()`, `import_capsule()`, etc.).
    - Mock the core logic classes (`Validator`, `Importer`) to verify they are called with the correct parameters based on user input (e.g., `--dry-run` flag).
    - Test argument parsing and error handling for invalid inputs.

- **Integration Tests:**
    - Test the interaction between the command layer and the core logic layer.
    - For example, ensure the `validate` command correctly formats and displays the `ValidationResult` object returned by the `Validator`.
    - Test that the `import` command correctly handles the `ImportPreview` object.

- **End-to-End (E2E) Tests:**
    - These are the most critical tests for this epic and will cover all acceptance criteria.
    - A temporary, self-contained test vault will be created using pytest fixtures.
    - Sample valid and invalid capsules will be created as test fixtures.
    - The tests will execute the CLI commands as subprocesses (e.g., `runner.invoke(app, ["import", "path/to/capsule"])`).
    - Assertions will be made against the command's exit code, its output (stdout), and the final state of the files in the temporary test vault.

### Post-Review Follow-ups
- **Story 10.3:** Add examples to the docstring of the `import_capsule` function.
- **Story 10.3:** Add an explicit E2E test to verify backup creation during import.
- **Story 10.4:** Consider refactoring the config loading logic into a shared utility to reduce code duplication.
- **Story 10.4:** Consider catching specific `CapsuleError` exceptions before the general `Exception` in commands for more tailored error responses.
