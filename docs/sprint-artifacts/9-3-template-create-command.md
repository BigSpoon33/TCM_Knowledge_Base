# Story 9.3: template-create-command

Status: drafted

## Story

As a content creator,
I want to implement the `capsule template create` command,
so that I can easily create new templates for content generation.

## Acceptance Criteria

1. The `create` command MUST accept a `name` argument for the new template.
2. The command MUST support a `--fields` option to specify the frontmatter fields.
3. The command MUST support a `--domain` option to specify the template's domain.
4. The command MUST support a `--force` flag to overwrite an existing template.
5. The command MUST create a new Jinja2 template file in the `capsule/templates` directory.
6. The command MUST handle errors gracefully, such as when a template already exists.
7. The command's design and user interaction MUST align with the existing `generate` command.

## Tasks / Subtasks

- [ ] **Task 1 (AC: #1-7)**: Implement the `create` command logic in `capsule/commands/template.py`.
- [ ] **Task 2 (AC: #1-7)**: Register the `create` command in `capsule/cli.py`.
- [ ] **Task 3 (AC: #1-7)**: Create unit tests for the `create` command in `tests/test_commands/test_template.py`.

## Dev Notes

- **Relevant architecture patterns and constraints**: The `architecture.md` document specifies that the `template create` command should be implemented in `capsule/commands/template.py`. It should follow the established Typer command structure pattern, including the use of `rich` for output and consistent error handling. The design should mirror the `generate` command for a cohesive user experience.
- **Source tree components to touch**: `capsule/commands/template.py` (new or modified file), `capsule/cli.py` (to register the new command), and `tests/test_commands/test_template.py` (new file).
- **Testing standards summary**: Unit tests for the new command should be created in the `tests/test_commands/` directory.

### References

- [Source: docs/architecture.md#CLI-Command-Structure-Pattern]
- [Source: docs/epics.md#Epic-9-CLI-Commands---Generation--Templates]
- [Source: capsule/commands/generate.py]
