# Story 13.5: help-documentation-and-examples

Status: done

## Story

As a user of the `obsidian-capsule-cli`,
I want to see clear help documentation with practical examples for every command,
so that I can understand how to use the tool effectively without consulting external docs.

## Acceptance Criteria

1.  **Global Help**: Running `capsule --help` displays a clear overview of the application, available commands, and version information.
2.  **Command Help**: Running `capsule [command] --help` displays detailed description, arguments, options, and **examples** for:
    - `generate`
    - `import`
    - `export`
    - `validate`
    - `template` (and subcommands `create`, `list`, `validate`)
    - `status`
    - `list`
    - `init`
3.  **Examples Section**: Every command help output includes an "Examples" section (using `epilog`) showing common usage patterns.
4.  **Option Descriptions**: All options (including `--dry-run`, `--verbose`, `--json`) have clear, descriptive help text.
5.  **Rich Formatting**: Help output uses `rich` formatting (colors/styles) where appropriate to improve readability.
6.  **Consistency**: All commands follow a consistent help format (Description -> Arguments -> Options -> Examples).
7.  **Verification**: Manual verification (via `typer.testing.CliRunner`) confirms help output contains expected sections and examples.

## Tasks / Subtasks

- [x] **Task 1: Update Main App Help** (AC: #1)
    - [x] Update `capsule/cli.py` with a comprehensive description and global examples.
    - [x] Configure `typer.Typer` to show a helpful epilog.

- [x] **Task 2: Update `generate` Command Help** (AC: #2, #3, #4)
    - [x] Add detailed description to `generate` command.
    - [x] Add examples: basic generation, template selection, dry-run, hybrid mode.
    - [x] Group options using `rich_help_panel` (e.g., "Generation Options", "Output Options").

- [x] **Task 3: Update `import` and `export` Command Help** (AC: #2, #3, #4)
    - [x] Add detailed description and examples to `import` (preview, dry-run, backup).
    - [x] Add detailed description and examples to `export` (formats, dry-run).

- [x] **Task 4: Update `template` Command Group Help** (AC: #2, #3, #4)
    - [x] Update `template` group description.
    - [x] Update `template create`, `template list`, `template validate` with examples.

- [x] **Task 5: Update Utility Commands Help** (AC: #2, #3, #4)
    - [x] Update `validate`, `status`, `list`, `init` with descriptions and examples.

- [x] **Task 6: Verification** (AC: #7)
    - [x] Create a test script or use `pytest` to verify help output contains "Examples" and specific keywords for each command.

## Dev Notes

- **Typer Epilog**: Use the `epilog` parameter in `@app.command()` to add the examples section.
- **Rich Markup**: Typer supports rich markup in help strings (e.g., `[bold]Example:[/bold]`).
- **Consistency**: Ensure all examples use the same style (e.g., `capsule generate ...`).
- **Dry Run**: Explicitly mention `--dry-run` in examples for commands that support it.

### Learnings from Previous Story

**From Story 13-4 (Status: done)**

- **Rich Integration**: We successfully integrated `rich.progress`. Dry-run output uses `rich`. Help output should also leverage `rich` for consistency.
- **Dry Run**: The `--dry-run` flag is implemented. We must document it in the help for `generate`, `import`, and `export`.
- **Testing**: `CliRunner` is effective for verifying console output. We can use it to assert that `--help` output contains our new examples.

[Source: stories/13-4-dry-run-mode-implementation.md#Dev-Agent-Record]

### References

- [Typer Documentation - Help and Docstrings](https://typer.tiangolo.com/tutorial/commands/help/)
- [Rich Documentation - Markup](https://rich.readthedocs.io/en/stable/markup.html)

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/stories/13-5-help-documentation-and-examples.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

- Plan: Update `capsule/cli.py` and command modules to add `epilog` with examples and `rich_help_panel` for options.
- Verification: Created `tests/test_cli_help.py` to assert presence of "Examples:" and command-specific keywords in help output.

### Completion Notes List

- Updated all CLI commands to include detailed help descriptions, examples (via epilog), and rich help panels for options.
- Verified help output using `typer.testing.CliRunner`.
- Ensured consistent formatting across all commands.

### File List

- capsule/cli.py
- capsule/commands/generate.py
- capsule/commands/import_cmd.py
- capsule/commands/export.py
- capsule/commands/template.py
- capsule/commands/validate.py
- capsule/commands/status.py
- capsule/commands/init.py
- tests/test_cli_help.py

## Change Log

- Updated `capsule/cli.py` to add global examples and epilogs for core commands.
- Updated `capsule/commands/*.py` to add detailed docstrings, examples, and rich help panels.
- Added `tests/test_cli_help.py` to verify help output.
- 2025-11-23: Senior Developer Review notes appended. Status updated to done.

## Senior Developer Review (AI)

### Reviewer: BMad
### Date: 2025-11-23
### Outcome: Approve

**Justification:** All acceptance criteria are fully met. The help documentation is comprehensive, consistent, and uses rich formatting as requested. Examples are provided for all commands, including dry-run scenarios. Verification tests are in place.

### Summary
The implementation successfully enhances the CLI help documentation with detailed descriptions, rich formatting, and practical examples for all commands. The use of `epilog` and `rich_help_panel` ensures a professional and user-friendly experience.

### Key Findings
- **High Severity**: None.
- **Medium Severity**: None.
- **Low Severity**: None.

### Acceptance Criteria Coverage

| AC# | Description | Status | Evidence |
|-----|-------------|--------|----------|
| 1 | Global Help | IMPLEMENTED | `capsule/cli.py`:12-35 |
| 2 | Command Help | IMPLEMENTED | `capsule/cli.py`, `capsule/commands/*.py` |
| 3 | Examples Section | IMPLEMENTED | All commands have `epilog` with examples |
| 4 | Option Descriptions | IMPLEMENTED | `rich_help_panel` used in command definitions |
| 5 | Rich Formatting | IMPLEMENTED | `rich_markup_mode="rich"` enabled |
| 6 | Consistency | IMPLEMENTED | Consistent format across all commands |
| 7 | Verification | IMPLEMENTED | `tests/test_cli_help.py` |

**Summary:** 7 of 7 acceptance criteria fully implemented.

### Task Completion Validation

| Task | Marked As | Verified As | Evidence |
|------|-----------|-------------|----------|
| Task 1: Update Main App Help | [x] | VERIFIED COMPLETE | `capsule/cli.py` |
| Task 2: Update `generate` Command Help | [x] | VERIFIED COMPLETE | `capsule/cli.py`:37-55 |
| Task 3: Update `import` and `export` Command Help | [x] | VERIFIED COMPLETE | `capsule/commands/import_cmd.py`, `capsule/commands/export.py` |
| Task 4: Update `template` Command Group Help | [x] | VERIFIED COMPLETE | `capsule/commands/template.py` |
| Task 5: Update Utility Commands Help | [x] | VERIFIED COMPLETE | `capsule/cli.py`, `capsule/commands/validate.py`, etc. |
| Task 6: Verification | [x] | VERIFIED COMPLETE | `tests/test_cli_help.py` |

**Summary:** 6 of 6 completed tasks verified.

### Test Coverage and Gaps
- `tests/test_cli_help.py` covers help output verification for all commands.
- No gaps identified.

### Architectural Alignment
- Follows the CLI Command Structure Pattern defined in `architecture.md`.
- Uses `typer` and `rich` as specified.

### Security Notes
- No security concerns identified in help documentation.

### Best-Practices and References
- [Typer Help](https://typer.tiangolo.com/tutorial/commands/help/)
- [Rich Markup](https://rich.readthedocs.io/en/stable/markup.html)

### Action Items
**Advisory Notes:**
- Note: Ensure future commands follow this help documentation pattern.
