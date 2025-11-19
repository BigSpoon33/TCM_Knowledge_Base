# Engineering Backlog

This backlog collects cross-cutting or future action items that emerge from reviews and planning.

Routing guidance:

- Use this file for non-urgent optimizations, refactors, or follow-ups that span multiple stories/epics.
- Must-fix items to ship a story belong in that story’s `Tasks / Subtasks`.
- Same-epic improvements may also be captured under the epic Tech Spec `Post-Review Follow-ups` section.

| Date | Story | Epic | Type | Severity | Owner | Status | Notes |
| ---- | ----- | ---- | ---- | -------- | ----- | ------ | ----- |
| 2025-11-18 | 5.1 | 5 | Bug | High | TBD | Open | Implement the `validate_data_types` method in the `Validator` class. |
| 2025-11-18 | 5.1 | 5 | Bug | Medium | TBD | Open | Implement the `validate_frontmatter_schema` method in the `Validator` class to actually validate the frontmatter schema. |
| 2025-11-18 | 5.1 | 5 | Test | Medium | TBD | Open | Add more test cases to `tests/test_core/test_validator.py` to cover different validation scenarios (e.g., invalid cypher, extra files, invalid frontmatter). |
| 2025-11-18 | 5.1 | 5 | TechDebt | Low | TBD | Open | Refactor the `Validator` class to parse the `capsule-cypher.yaml` file only once. |
| 2025-11-18 | 5.1 | 5 | Test | Low | TBD | Open | Add explicit assertions to the `test_validate_capsule_with_valid_capsule` test. |
