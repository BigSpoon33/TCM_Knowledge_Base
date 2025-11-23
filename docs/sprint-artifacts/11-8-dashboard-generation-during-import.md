# Story 11.8: dashboard-generation-during-import

Status: done

## Story

As a user importing a capsule,
I want the system to automatically generate master and capsule dashboards,
so that I can immediately start navigating and managing my new content.

## Acceptance Criteria

1.  Implement `generate_dashboards()` method in `capsule/core/importer.py`.
2.  Integrate dashboard generation into import workflow (after file copy, before merge).
3.  Implement dashboard merge logic (section-level merge for capsule dashboard updates).
4.  Include dashboard files in import preview.
5.  Test dashboard generation failure rollback (ensure transactional behavior).

## Tasks / Subtasks

- [x] Task 1: Implement `generate_dashboards()` method (AC: #1)
  - [x] Subtask 1.1: In `capsule/core/importer.py`, create the `generate_dashboards` method that takes a `Capsule` object and the vault path as input.
  - [x] Subtask 1.2: Implement logic to load the `master-dashboard.md.j2` and `capsule-dashboard.md.j2` templates.
  - [x] Subtask 1.3: Implement logic to render the templates with the capsule's metadata.
  - [x] Subtask 1.4: Implement logic to write the rendered dashboards to the correct locations in the vault.
- [x] Task 2: Integrate into import workflow (AC: #2)
  - [x] Subtask 2.1: In `capsule/core/importer.py`, call the `generate_dashboards` method from the `execute_import` method, after the file copy and before the merge operations.
- [x] Task 3: Implement dashboard merge logic (AC: #3)
  - [x] Subtask 3.1: In `capsule/core/merger.py`, add logic to handle the merging of dashboard files.
  - [x] Subtask 3.2: Ensure that the merge logic follows the section-level merge strategy for the dashboard's frontmatter.
- [x] Task 4: Include dashboards in import preview (AC: #4)
  - [x] Subtask 4.1: In `capsule/core/importer.py`, modify the `get_preview` method to include the dashboard files in the list of new or modified files.
- [x] Task 5: Implement and test failure rollback (AC: #5)
  - [x] Subtask 5.1: Add a test case that simulates a failure during dashboard generation.
  - [x] Subtask 5.2: Verify that the import transaction is rolled back correctly and no partial files are left in the vault.

### Review Follow-ups (AI)
- [x] [AI-Review][High] Update `capsule/core/merger.py` to include `dashboard_metadata`, `capsule_id`, `version`, `created`, `updated` in `section_level_merge` (or add specific dashboard merge logic) (AC #3)
- [x] [AI-Review][Med] Add a test case in `tests/test_core/test_dashboard_generation.py` that specifically verifies `dashboard_metadata` is updated when merging an existing dashboard (AC #3)

## Dev Agent Record


### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

- Implemented `generate_dashboards` in `capsule/core/importer.py` with support for merging existing capsule dashboards using `capsule.core.merger`.
- Integrated dashboard generation into `execute_import` workflow.
- Updated `analyze_impact` to include dashboard files in the import preview.
- Implemented rollback logic in `generate_dashboards` to clean up files if generation fails.
- Added tests for dashboard generation, rollback, and preview analysis in `tests/test_core/test_dashboard_generation.py` and `tests/test_core/test_importer.py`.
- Updated `capsule/core/merger.py` to support dashboard metadata merging.
- Updated `capsule/models/capsule.py` to include `dashboard_metadata`.
- Fixed `capsule/templates/capsule-dashboard.md.j2` to use correct `capsule_id` field.

### File List
- capsule/core/importer.py
- capsule/core/merger.py
- capsule/models/capsule.py
- capsule/templates/capsule-dashboard.md.j2
- tests/test_core/test_dashboard_generation.py
- tests/test_core/test_importer.py


---
# Change Log
- 2025-11-22: Initial draft created by BMad.
- 2025-11-22: Implemented dashboard generation, merging, preview, and rollback logic.
- 2025-11-22: Senior Developer Review notes appended.
- 2025-11-22: Senior Developer Review (Re-review) notes appended.

## Senior Developer Review (AI)

### Reviewer
BMad (Senior Developer Agent)

### Date
2025-11-22

### Outcome
**APPROVE**

### Justification
All acceptance criteria are met. The previous blocker regarding dashboard merge logic has been resolved by updating `capsule/core/merger.py` and adding a verification test case.

### Summary
The implementation is complete and robust. Dashboard generation is integrated into the import workflow, supports merging of metadata, and includes rollback protection. The developer has successfully addressed the findings from the previous review.

### Key Findings
None.

### Acceptance Criteria Coverage

| AC# | Description | Status | Evidence |
|-----|-------------|--------|----------|
| 1 | Implement `generate_dashboards()` method | **IMPLEMENTED** | `capsule/core/importer.py`:674 |
| 2 | Integrate into import workflow | **IMPLEMENTED** | `capsule/core/importer.py`:662 |
| 3 | Implement dashboard merge logic | **IMPLEMENTED** | `capsule/core/merger.py`:180 (universal_fields updated) |
| 4 | Include dashboards in import preview | **IMPLEMENTED** | `capsule/core/importer.py`:345 |
| 5 | Test dashboard generation failure rollback | **IMPLEMENTED** | `tests/test_core/test_dashboard_generation.py`:130 |

**Summary:** 5 of 5 acceptance criteria fully implemented.

### Task Completion Validation

| Task | Marked As | Verified As | Evidence |
|------|-----------|-------------|----------|
| Task 1: Implement `generate_dashboards()` | [x] | **VERIFIED** | `importer.py` |
| Task 2: Integrate into import workflow | [x] | **VERIFIED** | `importer.py` |
| Task 3: Implement dashboard merge logic | [x] | **VERIFIED** | `merger.py` updated |
| Task 4: Include dashboards in preview | [x] | **VERIFIED** | `importer.py` |
| Task 5: Implement failure rollback | [x] | **VERIFIED** | `test_dashboard_generation.py` |

**Summary:** 5 of 5 completed tasks verified.

### Test Coverage and Gaps
- **Coverage**: Excellent. Includes unit tests for generation, rollback, and the new merge logic test case (`test_generate_dashboards_merge_metadata`).
- **Gaps**: None identified.

### Architectural Alignment
- **Alignment**: Follows the template-driven generation pattern and uses the established merger utility.
- **Violations**: None.

### Security Notes
- Path traversal checks are present in extraction.
- Dashboard generation writes to vault path (assumed safe).

### Best-Practices and References
- **Jinja2**: Good use of `env.globals` for timestamps.
- **Type Hinting**: Consistently used.
- **Testing**: Comprehensive test suite.

### Action Items

**Code Changes Required:**
None.

**Advisory Notes:**
- Note: Consider refactoring `load_domain_sections` to avoid hardcoded domain mapping in the future (Low priority).
