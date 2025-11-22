# Story 9.1: main-cli-app-typer-setup

Status: done

## Story

As a developer,
I want to set up the main Typer application for the CLI,
so that I can start implementing the various CLI commands.

## Acceptance Criteria

1. A `cli.py` file MUST be created in the `capsule/` directory.
2. The `cli.py` file MUST contain a Typer application instance.
3. The main CLI app MUST be registered as an entry point in `pyproject.toml`.
4. The Typer app MUST include global options for `--verbose` and `--config-path`.
5. The Typer app MUST have a mechanism for version display.
6. The `__main__.py` file in `capsule/` MUST be updated to call the Typer app.


## Tasks / Subtasks

- [x] **Task 1 (AC: #1, #2)**: Create the main Typer application in `capsule/cli.py`.
- [x] **Task 2 (AC: #6)**: Update `capsule/__main__.py` to call the Typer app.
- [x] **Task 3 (AC: #3)**: Register the CLI application as an entry point in `pyproject.toml`.
- [x] **Task 4 (AC: #4, #5)**: Add global options for `--verbose`, `--config-path`, and version display.
- [x] **Task 5**: Create initial unit tests for the CLI app in `tests/test_commands/test_cli.py`.


## Dev Notes

- **Relevant architecture patterns and constraints**: The architecture specifies using Typer for the CLI framework. The `architecture.md` document provides a clear pattern for structuring the main CLI application in `capsule/cli.py`.
- **Source tree components to touch**: `capsule/cli.py` (new file), `capsule/__main__.py`, and `pyproject.toml`.
- **Testing standards summary**: Unit tests for the new CLI commands should be created in the `tests/test_commands/` directory.


### Project Structure Notes

- No `unified-project-structure.md` file was found. The project structure should be inferred from the existing file layout and `architecture.md`.
- This story will create a new file: `capsule/cli.py`.

### Learnings from Previous Story

**From Story 8.6: provenance-tracking (Status: done)**

- The `Note` model and `merger.py` are stable and well-tested.
- A technical debt item was identified to consider creating a Tech Spec for Epic 8. This does not impact the current story.

[Source: docs/sprint-artifacts/8-6-provenance-tracking.md#Dev-Agent-Record]


### References

- [Source: docs/architecture.md#CLI-Framework]
- [Source: docs/architecture.md#Complete-Project-Structure]
- [Source: docs/architecture.md#CLI-Command-Structure-Pattern]
- [Source: docs/epics.md#Epic-9-CLI-Commands---Generation--Templates]


## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->
- docs/sprint-artifacts/stories/9-1-main-cli-app-typer-setup.context.xml

### Agent Model Used

Claude 3.5 Sonnet (claude-3-5-sonnet-20241022)

### Debug Log References

**Implementation Plan (2025-11-21):**
1. ✅ Analyzed existing `capsule/cli.py` - basic Typer app already exists
2. ✅ Identified missing features: `--verbose` and `--config-path` global options
3. ✅ Added `--verbose` flag to control logging level (INFO vs DEBUG)
4. ✅ Added `--config-path` option to accept custom config file path
5. ✅ Implemented context storage for downstream command access
6. 🔄 Next: Create comprehensive unit tests

**Key Implementation Details:**
- Used Typer's Option with validation (exists, file_okay, readable) for config_path
- Configured logging dynamically based on verbose flag
- Stored global options in Typer context (ctx.obj) for subcommand access
- Version callback already existed and works correctly

### Completion Notes List

**Implementation Completed (2025-11-21):**
- ✅ Enhanced `capsule/cli.py` with `--verbose` and `--config-path` global options
- ✅ Implemented context storage for downstream command access via `ctx.obj`
- ✅ Created comprehensive test suite in `tests/test_commands/test_cli.py` (18 test cases)
- ✅ All acceptance criteria met and validated
- ✅ All tests passing (18/18 in test_cli.py, 0 regressions)

**Technical Details:**
- Verbose flag controls logging level (DEBUG vs INFO)
- Config path stored in Typer context for command access
- Validation deferred to actual config usage (lightweight global options)
- Version display working via callback with is_eager=True

## File List

**Modified Files:**
- `capsule/cli.py` - Added `--verbose` and `--config-path` global options, context storage

**New Files:**
- `tests/test_commands/test_cli.py` - Comprehensive test suite for CLI app (18 test cases)

**Verified Existing Files (No Changes Needed):**
- `capsule/__main__.py` - Already correctly calls the Typer app
- `pyproject.toml` - Entry points already configured correctly

## Change Log

- 2025-11-21: Story drafted by BMad agent.
- 2025-11-21: Implementation completed - Added global options (`--verbose`, `--config-path`) and comprehensive tests
- 2025-11-21: Senior Developer Review completed. Status changed to 'done'.

---

## Senior Developer Review (AI)

### Reviewer: BMad
### Date: 2025-11-21
### Outcome: ✅ Approve

### Summary
The implementation for setting up the main Typer CLI application is excellent. All acceptance criteria have been met, and all tasks marked as complete were verified. The code adheres to the established architectural patterns and demonstrates high quality. A minor, non-blocking opportunity to enhance test robustness was identified and is noted as an advisory action item.

### Key Findings
- **[Low] Test Coverage Enhancement:** The unit tests for global options could be improved to assert the *effects* of the options (e.g., verifying the logger level after `--verbose` is used), rather than just their presence.

### Acceptance Criteria Coverage
**Summary: 6 of 6 acceptance criteria fully implemented.**

| AC# | Description | Status | Evidence |
|---|---|---|---|
| 1 | A `cli.py` file MUST be created in the `capsule/` directory. | IMPLEMENTED | File `capsule/cli.py` exists. |
| 2 | The `cli.py` file MUST contain a Typer application instance. | IMPLEMENTED | `capsule/cli.py:10` |
| 3 | The main CLI app MUST be registered as an entry point in `pyproject.toml`. | IMPLEMENTED | `pyproject.toml:43` |
| 4 | The Typer app MUST include global options for `--verbose` and `--config-path`. | IMPLEMENTED | `capsule/cli.py:41-54` |
| 5 | The Typer app MUST have a mechanism for version display. | IMPLEMENTED | `capsule/cli.py:23-27` |
| 6 | The `__main__.py` file in `capsule/` MUST be updated to call the Typer app. | IMPLEMENTED | `capsule/__main__.py:5` |

### Task Completion Validation
**Summary: 5 of 5 completed tasks verified.**

| Task | Marked As | Verified As | Evidence |
|---|---|---|---|
| 1: Create Typer app | [x] | VERIFIED COMPLETE | `capsule/cli.py` exists and is correctly configured. |
| 2: Update `__main__.py` | [x] | VERIFIED COMPLETE | `capsule/__main__.py` correctly calls the Typer app. |
| 3: Register entry point | [x] | VERIFIED COMPLETE | `pyproject.toml` contains the correct script entry point. |
| 4: Add global options | [x] | VERIFIED COMPLETE | Global options are implemented in `capsule/cli.py`. |
| 5: Create unit tests | [x] | VERIFIED COMPLETE | `tests/test_commands/test_cli.py` exists and provides good coverage. |

### Test Coverage and Gaps
- The new test suite in `tests/test_commands/test_cli.py` provides solid coverage for the existence and acceptance of the new global options.
- As noted in Key Findings, the tests could be strengthened by asserting the side-effects of these options.

### Architectural Alignment
- The implementation is fully compliant with the patterns defined in `architecture.md`.
- **Warning:** No Tech Spec was found for Epic 9. While not a blocker for this foundational story, one should be considered for the epic as a whole.

### Action Items

**Advisory Notes:**
- Note: Consider enhancing the unit tests in `tests/test_commands/test_cli.py` to assert the side-effects of global options, such as verifying the logger level after `--verbose` is used.


