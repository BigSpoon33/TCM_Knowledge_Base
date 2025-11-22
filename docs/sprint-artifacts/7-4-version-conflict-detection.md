# Story 7.4: version-conflict-detection

Status: review

## Story

As a user,
I want the system to detect version conflicts during import,
so that I don't accidentally overwrite a newer capsule version with an older one.

## Acceptance Criteria

1. The system compares the version of the incoming capsule with the installed version (if any).
2. If the incoming version is older than the installed version, a warning is displayed in the preview (Downgrade).
3. If the incoming version is the same as the installed version, a notice is displayed (Reinstall).
4. If the incoming version is newer, it is marked as an update.
5. The system uses semantic versioning (semver) for comparisons.
6. The import preview data structure includes version comparison results.

## Tasks / Subtasks

- [x] **Task 1: Implement Version Comparison Logic** (AC: #1, #5)
  - [x] Subtask 1.1: Update `capsule/utils/validators.py` or create `capsule/utils/versioning.py` to handle version comparison using `semver`.
  - [x] Subtask 1.2: Implement `compare_versions(v1, v2)` returning comparison result (-1, 0, 1).

- [x] **Task 2: Update `CapsuleImporter.analyze_impact`** (AC: #1, #2, #3, #4)
  - [x] Subtask 2.1: Retrieve installed capsule version from vault (check for existing `capsule-cypher.yaml` in target path).
  - [x] Subtask 2.2: Compare incoming version vs installed version.
  - [x] Subtask 2.3: Determine import type: `NEW`, `UPDATE`, `DOWNGRADE`, `SAME`.

- [x] **Task 3: Update `ImportPreview` Data Structure** (AC: #6)
  - [x] Subtask 3.1: Add `import_type` (str) and `version_diff` (str) fields to `ImportPreview` class in `capsule/core/importer.py`.

- [x] **Task 4: Update CLI Display** (AC: #2, #3, #4)
  - [x] Subtask 4.1: Update `capsule/core/importer.py` display logic to show import type in preview header.
  - [x] Subtask 4.2: Add warning styling (red/yellow) for Downgrades in the `rich` output.

- [x] **Task 5: Add Tests** (AC: #1-#6)
  - [x] Subtask 5.1: Add unit tests for version comparison logic.
  - [x] Subtask 5.2: Add unit tests for `analyze_impact` with different version scenarios (new, update, downgrade, same).

## Dev Notes

- **Semver Library:** The project already uses the `semver` library (seen in `capsule/utils/validators.py`). Use `semver.VersionInfo.parse()` for robust parsing and comparison.
- **Installed Version Detection:** The system needs to know if a capsule is already installed.
  - Check if the capsule directory exists in the vault.
  - If it exists, try to read `capsule-cypher.yaml` inside it to get the installed version.
  - If `capsule-cypher.yaml` is missing or invalid, assume it's a "New Install" or "Corrupted Install" (treat as New/Overwrite).
- **Import Types:**
  - `NEW`: No existing capsule found.
  - `UPDATE`: Incoming > Installed.
  - `DOWNGRADE`: Incoming < Installed.
  - `SAME`: Incoming == Installed.
- **Preview Display:**
  - Use `rich` panels or colored text to highlight Downgrades.
  - Example: `[bold red]⚠️ DOWNGRADE DETECTED[/bold red]: 1.2.0 -> 1.1.0`

### Project Structure Notes

- **Alignment with unified project structure:**
  - Modify `capsule/core/importer.py` (logic and display).
  - Modify `capsule/utils/validators.py` (or add helper there).
  - Tests in `tests/test_core/test_importer.py`.

### Learnings from Previous Story

**From Story 7-3-capsule-importer-with-preview (Status: done)**

- **New Files Created**: `capsule/core/importer.py`, `capsule/commands/import_cmd.py`.
- **Security**: Path traversal protection was added. Ensure any new file reading (like reading installed cypher) is also safe.
- **Error Handling**: Specific exception handling was improved. Continue this pattern when reading installed versions (handle missing files, bad YAML).
- **Testing**: High test coverage (100%) was achieved. Maintain this standard.
- **Rich Output**: The preview uses `rich`. Integrate the version warning seamlessly into the existing layout.

[Source: stories/7-3-capsule-importer-with-preview.md#Dev-Agent-Record]

### References

- [Source: docs/epics.md#Epic-7-Import-Export-Operations]
- [Source: docs/architecture.md#Epic-Group-4-Import-Export-Operations-FR26-FR31]
- [Source: docs/PRD.md#FR30]

## Dev Agent Record

### Context Reference

- [Context File](stories/7-4-version-conflict-detection.context.xml)

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

- Implemented version comparison logic using `semver` in `capsule/utils/versioning.py`.
- Updated `CapsuleImporter.analyze_impact` to detect installed version by looking for `capsule-cypher.yaml` in the capsule-specific directory (`vault_path / capsule_id`).
- Verified that `ImportPreview` and CLI display correctly handle `NEW`, `UPDATE`, `DOWNGRADE`, and `SAME` scenarios.
- Updated tests in `tests/test_core/test_importer_versioning.py` to reflect the directory structure assumption.
- Added `is_valid_semver` to `capsule/utils/versioning.py` for completeness.

### File List

- capsule/utils/versioning.py
- capsule/core/importer.py
- tests/test_core/test_importer_versioning.py
- tests/test_utils/test_versioning.py

## Senior Developer Review (AI)

### Reviewer
BMad

### Date
Fri Nov 21 2025

### Outcome
**Approve**
The implementation fully satisfies all acceptance criteria and tasks. The version comparison logic is robust, and the integration into the import preview provides clear and valuable feedback to the user.

### Summary
The story successfully implements version conflict detection for capsule imports. The system now correctly identifies whether an import is a new install, an update, a downgrade, or a reinstall. The use of `semver` ensures standard compliance, and the `rich` library integration makes the status immediately apparent to the user.

### Key Findings

#### Low Severity
- **Security / Input Validation**: In `CapsuleImporter.analyze_impact`, the `installed_cypher_path` is constructed using `vault_path / self.cypher.capsule_id`. While `validate_capsule()` is called prior to this, ensure that `capsule_id` is strictly validated to contain only safe characters (alphanumeric, underscores, hyphens) and no path traversal sequences (`..`, `/`) to prevent accessing files outside the vault.

### Acceptance Criteria Coverage

| AC# | Description | Status | Evidence |
|-----|-------------|--------|----------|
| 1 | Compare incoming vs installed version | **IMPLEMENTED** | `capsule/core/importer.py:247` |
| 2 | Display warning for Downgrade | **IMPLEMENTED** | `capsule/core/importer.py:441-442` |
| 3 | Display notice for Reinstall (Same) | **IMPLEMENTED** | `capsule/core/importer.py:447-448` |
| 4 | Mark newer version as Update | **IMPLEMENTED** | `capsule/core/importer.py:444-445` |
| 5 | Use semantic versioning (semver) | **IMPLEMENTED** | `capsule/utils/versioning.py:21-23` |
| 6 | Include comparison in ImportPreview | **IMPLEMENTED** | `capsule/core/importer.py:300-301` |

**Summary:** 6 of 6 acceptance criteria fully implemented.

### Task Completion Validation

| Task | Marked As | Verified As | Evidence |
|------|-----------|-------------|----------|
| 1. Implement Version Comparison Logic | [x] | **VERIFIED** | `capsule/utils/versioning.py` |
| 2. Update `CapsuleImporter.analyze_impact` | [x] | **VERIFIED** | `capsule/core/importer.py:230-258` |
| 3. Update `ImportPreview` Data Structure | [x] | **VERIFIED** | `capsule/core/importer.py:38-39` |
| 4. Update CLI Display | [x] | **VERIFIED** | `capsule/core/importer.py:440-452` |
| 5. Add Tests | [x] | **VERIFIED** | `tests/test_core/test_importer_versioning.py` |

**Summary:** 5 of 5 completed tasks verified.

### Test Coverage and Gaps
- **Coverage:** Comprehensive unit tests added for version comparison logic and all import impact scenarios (New, Update, Downgrade, Same, Mismatch).
- **Gaps:** None identified.

### Architectural Alignment
- **Compliance:** Follows the architecture's requirement for `semver` (NFR35) and `rich` output.
- **Structure:** Logic is correctly placed in `capsule/core/importer.py` and `capsule/utils/versioning.py`.

### Security Notes
- See Key Findings regarding `capsule_id` path traversal check.

### Best-Practices and References
- **Semver:** Good use of the `semver` library for robust comparison.
- **Rich:** Excellent use of color-coded panels for user feedback.

### Action Items

**Advisory Notes:**
- Note: Ensure `capsule_id` validation in `Validator` class is strict enough to prevent path traversal.

## Change Log

- **2025-11-21**: Senior Developer Review notes appended. Status updated to **done**.
