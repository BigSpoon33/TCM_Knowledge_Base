# Technical Specification: Epic 13

**Epic Name:** Cross-Cutting Concerns & Polish
**Date:** 2025-11-22
**Author:** Shuma
**Status:** Draft

## 1. Executive Summary

### 1.1 Purpose
The purpose of this epic is to elevate the Obsidian Capsule Delivery System (OCDS) from a functional prototype to a production-grade CLI tool. It focuses on "cross-cutting concerns"—aspects that affect the entire system—to ensure reliability, usability, and safety. Specifically, it aims to implement consistent error handling, structured logging, visual progress indicators, and a safety-first "dry-run" mode, providing users with confidence and clarity during complex operations like content generation and capsule import.

### 1.2 Scope
**In Scope:**
- **Error Handling:** Implementation of a unified exception hierarchy (`CapsuleError`) and a global error handling strategy for the CLI.
- **Logging:** Setup of a structured logging system with file rotation and console output, respecting verbosity levels.
- **Progress Indicators:** Integration of the `rich` library to provide visual feedback (spinners, progress bars) for long-running tasks (generation, import/export).
- **Dry-Run Mode:** Implementation of a `--dry-run` flag for all state-changing commands (`generate`, `import`, `export`) to preview actions without side effects.
- **Documentation:** Enhancement of CLI help text (`--help`) with practical examples and usage guides.

**Out of Scope:**
- New functional features for content generation or packaging.
- Dashboard implementation (covered in Epics 11 & 12).
- Changes to the core data models (Capsule, Note, etc.), except where needed to support dry-run logic.

### 1.3 Key Technical Decisions
- **Exception Hierarchy:** Define a base `CapsuleError` with specific subclasses (`ValidationError`, `FileError`, `NetworkError`) to map exceptions to specific exit codes and user-friendly messages.
- **Rich Integration:** Leverage the `rich` library for all CLI output, replacing standard `print` statements to ensure consistent formatting, coloring, and progress visualization.
- **Logging Strategy:** Use Python's standard `logging` module. Logs will be written to `~/.capsule/logs/` with rotation, while console output will be handled by `rich` to avoid interference with progress bars.
- **Dry-Run Architecture:** Pass a `dry_run` boolean flag down from the CLI layer to core logic classes (`Generator`, `Importer`). Core classes will wrap side-effect operations (file writes, deletions) in conditional checks or use a "DryRunFileManager" abstraction if complexity warrants it.
- **Typer Help:** Utilize `Typer`'s built-in support for rich help text and epilogues to embed examples directly in the CLI help output.


## 2. Architecture & Design

### 2.1 Component Architecture

The implementation introduces shared utilities that cross-cut all existing modules.

```mermaid
graph TD
    CLI[CLI Layer (cli.py)] --> ErrorHandler[Error Handler]
    CLI --> Logger[Logger Setup]
    
    subgraph "Cross-Cutting Utilities"
        ErrorHandler --> Exceptions[exceptions.py]
        Logger --> LogUtils[utils/logger.py]
        Progress[utils/progress.py]
    end
    
    subgraph "Core Logic"
        Generator[Generator]
        Importer[Importer]
        Exporter[Exporter]
    end
    
    CLI --> Generator
    CLI --> Importer
    
    Generator --> Progress
    Importer --> Progress
    
    Generator -.-> Exceptions
    Importer -.-> Exceptions
    
    Generator -.-> LogUtils
    Importer -.-> LogUtils
```

- **`capsule/exceptions.py`**: Defines the canonical set of errors that the system can raise.
- **`capsule/utils/logger.py`**: Configures the logging handlers (file and console).
- **`capsule/utils/progress.py`**: Provides a unified interface for creating `rich` progress bars, ensuring consistent styling across commands.
- **`capsule/cli.py`**: Acts as the top-level exception handler, catching `CapsuleError` and rendering user-friendly error messages before exiting.

### 2.2 Data Models

No changes to the core domain models (`Capsule`, `Note`, `CapsuleCypher`) are required.

**Configuration Model Updates (`capsule/models/config.py`):**
The `Config` model will be updated to support logging preferences:
```python
class Config:
    # ... existing fields ...
    logging:
        level: str = "INFO"
        file_path: Path = "~/.capsule/logs/capsule.log"
        rotate_bytes: int = 5 * 1024 * 1024  # 5MB
        backup_count: int = 3
```

### 2.3 API Design

#### 2.3.1 Exception Hierarchy
```python
class CapsuleError(Exception):
    """Base class for all OCDS exceptions."""
    def __init__(self, message: str, exit_code: int = 1, hint: str = None):
        self.exit_code = exit_code
        self.hint = hint
        super().__init__(message)

class ValidationError(CapsuleError):
    """Raised when schema or data validation fails."""
    exit_code = 1

class FileError(CapsuleError):
    """Raised when file operations fail (permissions, not found)."""
    exit_code = 2

class NetworkError(CapsuleError):
    """Raised when network requests fail (research, API)."""
    exit_code = 3

class UserCancelledError(CapsuleError):
    """Raised when user aborts an operation."""
    exit_code = 4
```

#### 2.3.2 Logging Interface
```python
# capsule/utils/logger.py
def setup_logging(verbose: bool = False) -> logging.Logger:
    """
    Configures root logger with:
    1. RotatingFileHandler (JSON or formatted text) for debugging.
    2. RichHandler for console output (if not interfering with progress).
    """
```

#### 2.3.3 Dry-Run Interface
All core logic classes (`ContentGenerator`, `CapsuleImporter`, `CapsuleExporter`) will accept a `dry_run` boolean in their `__init__` or method signatures.

```python
class ContentGenerator:
    def generate(self, topic: str, dry_run: bool = False) -> Capsule:
        # ...
        if dry_run:
            logger.info(f"[DRY RUN] Would write file: {file_path}")
            return mock_capsule
        # ...
```

### 2.4 Security Considerations

- **Log Sanitization:** The logging system must include a filter to redact sensitive information (API keys, auth tokens) before writing to disk or console.
- **Dry-Run Integrity:** The dry-run mode must strictly guarantee that no file system modifications occur. This is critical for user trust. We will implement this by wrapping all `pathlib.Path.write_text`, `shutil.copy`, and `os.remove` calls in a `FileOps` utility that checks the `dry_run` flag.
- **Error Information Leakage:** Error messages displayed to the user should be helpful but not reveal internal stack traces or sensitive system paths unless `--verbose` is used. Stack traces will be logged to the file but hidden from the console by default.


## 3. Implementation Plan

### 3.1 Development Phases

#### Phase 1: Foundation (Error Handling & Logging)
- **Goal:** Establish the safety net and observability layer.
- **Tasks:**
  1. Create `capsule/exceptions.py` with the `CapsuleError` hierarchy.
  2. Implement `capsule/utils/logger.py` with rotation and sanitization.
  3. Update `capsule/cli.py` to wrap the main entry point in a `try/except` block that catches `CapsuleError` and prints formatted messages.
  4. Replace all `print()` calls with `logger` calls or `typer.echo` throughout the codebase.

#### Phase 2: Progress Indicators
- **Goal:** Improve user experience for long-running tasks.
- **Tasks:**
  1. Create `capsule/utils/progress.py` wrapping `rich.progress`.
  2. Update `capsule/commands/generate.py` to show progress for research and generation steps.
  3. Update `capsule/commands/import_cmd.py` to show progress for backup and file extraction.
  4. Ensure progress bars clean up correctly on errors.

#### Phase 3: Dry-Run & Safety
- **Goal:** Implement safe preview capabilities.
- **Tasks:**
  1. Create a `FileOps` utility class (or extend `capsule/utils/file_ops.py`) that accepts a `dry_run` context.
  2. Refactor `Generator`, `Importer`, and `Exporter` to use this utility for all file writes.
  3. Add `--dry-run` flag to `generate`, `import`, and `export` commands.
  4. Verify that `--dry-run` produces log output ("Would write...") but no files.

#### Phase 4: Documentation & Polish
- **Goal:** Make the tool self-documenting and easy to learn.
- **Tasks:**
  1. Update Typer command definitions with `help` strings containing examples.
  2. Add `epilog` to commands showing common usage patterns.
  3. Verify all error messages include actionable hints.

### 3.2 Dependencies
- **Runtime:**
  - `rich>=13.0`: For progress bars, spinners, and colored output.
  - `typer>=0.9.0`: For CLI command structure and help generation.
- **Standard Library:**
  - `logging`: For structured logging.
  - `logging.handlers`: For rotating file handlers.

### 3.3 Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Dry-Run Leakage** | High | If dry-run fails to prevent a write, user trust is damaged. **Mitigation:** Centralize ALL file operations in a single `FileOps` utility that checks the flag. Unit test this utility extensively. |
| **Console/Log Conflict** | Medium | Progress bars and log messages fighting for stdout can cause visual artifacts. **Mitigation:** Configure `rich` to handle logging integration, or redirect logs to file only during active progress bars. |
| **Performance Overhead** | Low | Excessive logging could slow down operations. **Mitigation:** Set default log level to INFO. Use efficient log rotation. |
| **Sensitive Data in Logs** | High | API keys or personal paths in logs. **Mitigation:** Implement a `LogFilter` that regex-matches and redacts known sensitive patterns (API keys) before writing. |


## 4. Testing Strategy

### 4.1 Unit Testing

- **Exception Handling:**
  - Verify that `CapsuleError` subclasses set the correct `exit_code`.
  - Verify that `cli.py` catches exceptions and formats them correctly (using `capsys` fixture).
- **Logging:**
  - Test `LogSanitizer` with sample strings containing dummy API keys to ensure redaction works.
  - Verify log rotation logic (mocking file size).
- **FileOps (Dry-Run):**
  - Mock `pathlib.Path.write_text` and `shutil.copy`.
  - Call `FileOps.write(..., dry_run=True)` and assert mocks were NOT called.
  - Call `FileOps.write(..., dry_run=False)` and assert mocks WERE called.

### 4.2 Integration Testing

- **Dry-Run Verification:**
  - Run `capsule generate "Test Topic" --dry-run`.
  - Assert that the output directory does NOT contain the capsule folder.
  - Assert that the console output contains "[DRY RUN]" messages.
- **Error Scenarios:**
  - Run `capsule validate non_existent_path`.
  - Assert exit code is 2 (FileError).
  - Assert output contains "Error: File not found".
- **Progress Bars:**
  - (Manual/Visual) Run a dummy long-running command and verify spinner/bar appears and disappears correctly.

### 4.3 Acceptance Criteria Mapping

| Story | Requirement | Verification Method |
|-------|-------------|---------------------|
| **13-1** | Consistent error handling | Unit test `cli.py` exception handler; Integration test invalid inputs. |
| **13-2** | Structured logging | Check `~/.capsule/logs/capsule.log` after running commands. |
| **13-3** | Progress indicators | Visual verification during `generate` and `import`. |
| **13-4** | Dry-run mode | Integration test: `generate --dry-run` creates no files. |

## Post-Review Follow-ups

- [ ] [TechDebt][Low] Consider consolidating backup creation logic between `capsule/commands/import_cmd.py` and `capsule/core/importer.py` to avoid duplication. (Story 13.4)


