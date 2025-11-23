| 2025-11-19 | 6.1 | 6 | TechDebt | Medium | TBD | Open | Refactor `CapsulePackager.generate_cypher` to not use hardcoded values. |
| 2025-11-19 | 6.1 | 6 | Bug | Medium | TBD | Open | Add error handling to `CapsulePackager`. |
| 2025-11-19 | 6.1 | 6 | TechDebt | Medium | TBD | Open | Add more comprehensive tests to `test_packager.py`. |
| 2025-11-19 | 6.1 | 6 | Enhancement | Low | TBD | Open | Add logging to `CapsulePackager`. |
| 2025-11-19 | Ad-Hoc Review | N/A | Bug | High | TBD | Closed | Refactor `capsule/core/packager.py` to generate cypher from actual capsule content. |
| 2025-11-19 | Ad-Hoc Review | N/A | TechDebt | Medium | TBD | Open | Refactor `capsule/core/generator.py` to remove the `MockCapsule` dependency. |
| 2025-11-19 | Ad-Hoc Review | N/A | Enhancement | Low | TBD | Open | Implement the `validate_data_types` method in `capsule/core/validator.py`. |
| 2025-11-19 | Ad-Hoc Review | N/A | TechDebt | Low | TBD | Open | Make `cypher_data` in `capsule/core/generator.py` dynamic. |
| 2025-11-19 | Ad-Hoc Review | N/A | TechDebt | Medium | TBD | Closed | Implement the full `Validator` class to replace the placeholder. |
| 2025-11-19 | Ad-Hoc Review | N/A | TechDebt | Low | TBD | Open | Create a centralized configuration model for constants and settings. |
| 2025-11-19 | Ad-Hoc Review | N/A | Security | Medium | TBD | Open | Perform a security review of the `capsule init` command. |
| 2025-11-20 | 7.1 | 7 | Tech Debt | Low | TBD | Open | Consider adding tests for edge cases like a non-existent vault or unwritable backup directory in a future story. |
| 2025-11-21 | 7.2 | 7 | TechDebt | Low | TBD | Open | Replace `print()` with `typer.echo()` in capsule/core/exporter.py for CLI output consistency (lines 36, 77, 101). |
| 2025-11-21 | 7.2 | 7 | TechDebt | Low | TBD | Open | Move `import shutil` to module level in capsule/core/exporter.py (line 86) per PEP 8. |
| 2025-11-21 | 7.3 | 7 | Bug | High | TBD | Closed | Remove outdated test file `tests/commands/test_import_cmd.py` that conflicts with new tests in `tests/test_commands/test_import_cmd.py`. |
| 2025-11-21 | 7.3 | 7 | Security | Medium | TBD | Open | Add explicit path traversal validation in `capsule/core/importer.py:147-149` for Python < 3.11.4 compatibility. |
| 2025-11-21 | 7.3 | 7 | TechDebt | Medium | TBD | Open | Improve frontmatter error handling in `capsule/core/importer.py:291-334` with specific exception types (yaml.YAMLError, UnicodeDecodeError). |
| 2025-11-21 | 7.3 | 7 | TechDebt | Low | TBD | Open | Add complete type hints to helper methods in `capsule/core/importer.py:251-355`. |
| 2025-11-21 | 7.3 | 7 | TechDebt | Low | TBD | Open | Standardize error message formatting in `capsule/core/importer.py` (use f"{e}" consistently). |
| 2025-11-21 | 8.1 | 8 | Feature | High | TBD | Closed | Implement `FrontmatterHandler` utilities for safe round-trip YAML editing. |
| 2025-11-21 | 8.2 | 8 | Feature | High | TBD | Closed | Implement Section-Level Merge algorithm in `Merger` class. |
| 2025-11-21 | 8.3 | 8 | Feature | High | TBD | Closed | Implement Additive Merge algorithm in `Merger` class. |
| 2025-11-21 | 8.4 | 8 | Feature | Medium | TBD | Closed | Implement Conflict Detection logic for overlapping capsule data. |
| 2025-11-21 | 8.5 | 8 | Feature | Critical | TBD | Closed | Implement "Safety Wrapper" to ensure markdown body content is immutable. |
| 2025-11-21 | 8.6 | 8 | Feature | Medium | TBD | Closed | Implement Provenance Tracking logic for `source_capsules` list. |
| 2025-11-21 | 9.1 | 9 | TechDebt | Low | TBD | Open | Enhance unit tests in `tests/test_commands/test_cli.py` to assert side-effects of global options (e.g., logger level). |
| 2025-11-22 | 10.3 | 10 | Enhancement | Low | TBD | Open | Add examples to the docstring of the import_capsule function in capsule/commands/import_cmd.py. |
| 2025-11-22 | 10.3 | 10 | Test | Low | TBD | Open | Add an explicit E2E test to verify that a backup file is created during a standard import. |
| 2025-11-22 | 11.6 | 11 | TechDebt | Low | TBD | Open | Consider moving complex Javascript snippets from Python strings to separate .js files. |
| 2025-11-22 | 11.8 | 11 | Bug | High | TBD | Closed | Update `capsule/core/merger.py` to include `dashboard_metadata`, `capsule_id`, `version`, `created`, `updated` in `section_level_merge` (or add specific dashboard merge logic) (AC #3). |
| 2025-11-22 | 13.1 | 13 | TechDebt | Low | TBD | Open | Consider adding more integration tests for different error scenarios in other commands. |
| 2025-11-22 | 11.8 | 11 | Test | Medium | TBD | Closed | Add a test case in `tests/test_core/test_dashboard_generation.py` that specifically verifies `dashboard_metadata` is updated when merging an existing dashboard (AC #3). |
| 2025-11-23 | 13.4 | 13 | TechDebt | Low | TBD | Open | Consider consolidating backup creation logic between `capsule/commands/import_cmd.py` and `capsule/core/importer.py` to avoid duplication. |
| 2025-11-23 | 14.5 | 14 | Bug | Medium | TBD | Closed | Fix test_packager.py::test_generate_cypher assertion error - test expects string in list but gets dict [file: tests/test_core/test_packager.py:64] |
| 2025-11-23 | 14.5 | 14 | Enhancement | Low | TBD | Open | Consider integrating Codecov or Coveralls for automatic coverage badge updates (currently using static badge requiring manual updates) |
| 2025-11-23 | 14.5 | 14 | TechDebt | Low | TBD | Open | Clarify task completion criteria - mark optional tasks as unchecked OR document that optional means "considered but not implemented" |




