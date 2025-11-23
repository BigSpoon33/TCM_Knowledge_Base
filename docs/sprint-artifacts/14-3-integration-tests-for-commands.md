# Story 14.3: integration-tests-for-commands

Status: review

## Story

As a Developer,
I want to write integration tests for the CLI commands,
so that I can ensure the command-line interface works correctly, handles arguments properly, and integrates with the core logic as expected.

## Acceptance Criteria

1. Integration tests implemented for `capsule generate` command (mocking research API).
2. Integration tests implemented for `capsule template` commands (create, list, validate).
3. Integration tests implemented for `capsule export` command.
4. Integration tests implemented for `capsule import` command (handling user input/prompts).
5. Integration tests implemented for `capsule validate` command.
6. Integration tests implemented for `capsule status` and `capsule list` commands.
7. Tests verify correct exit codes (0 for success, non-zero for failure).
8. Tests verify expected output messages (stdout/stderr).
9. Tests verify file system side effects (files created/modified) using temporary directories.

## Tasks / Subtasks

- [x] Create `tests/test_commands/test_generate.py` (AC: 1)
  - [x] Test `generate` with valid arguments
  - [x] Test `generate` with missing/invalid arguments
  - [x] Test `generate` with `--dry-run`
- [x] Create `tests/test_commands/test_template.py` (AC: 2)
  - [x] Test `template create`
  - [x] Test `template list`
  - [x] Test `template validate`
- [x] Create `tests/test_commands/test_export.py` (AC: 3)
  - [x] Test `export` to zip
  - [x] Test `export` to folder
- [x] Create `tests/test_commands/test_import.py` (AC: 4)
  - [x] Test `import` with auto-approve
  - [x] Test `import` with interactive prompts (mocked input)
- [x] Create `tests/test_commands/test_validate.py` (AC: 5)
  - [x] Test `validate` on valid capsule
  - [x] Test `validate` on invalid capsule
- [x] Create `tests/test_commands/test_status_list.py` (AC: 6)
  - [x] Test `status` command
  - [x] Test `list` command
- [x] Run full test suite and verify all tests pass (AC: 7, 8, 9)

## Dev Notes

- **Architecture**: Follow the testing strategy defined in `architecture.md`. Use `typer.testing.CliRunner` for command testing.
- **Integration Level**: These tests should verify the integration between the CLI layer and the Core layer. Use real core components where possible, but mock external APIs (like Gemini) and use temporary directories (`tmp_path` fixture) for file operations.
- **Structure**: Tests should be placed in `tests/test_commands/`.
- **Mocking**: Use `unittest.mock.patch` or `pytest-mock` to mock `ResearchProvider` or other external dependencies.

### Project Structure Notes

- Alignment with unified project structure: Tests go in `tests/test_commands/`.
- No conflicts detected.

### References

- [Source: docs/architecture.md#Testing-Strategy]
- [Source: docs/epics.md#Epic-14-Testing-Infrastructure]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/14-3-integration-tests-for-commands.context.xml

### Agent Model Used

Claude 3.5 Sonnet

### Debug Log References

- Fixed `Packager` to generate `contents` as list of dicts to match `Validator` expectations.
- Updated test fixtures to include `data_schemas` and correct `contents` structure.

### Completion Notes List

- All integration tests implemented and passing.
- `Packager` bug fixed.

### File List

- tests/test_commands/test_generate.py
- tests/test_commands/test_template.py
- tests/test_commands/test_export.py
- tests/test_commands/test_import.py
- tests/test_commands/test_validate.py
- tests/test_commands/test_status.py
- tests/test_commands/test_list.py
- capsule/core/packager.py
