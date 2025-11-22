# Story 8.4: Conflict Detection Logic

Status: done

## Story

As a System Architect,
I want to implement the ConflictDetector class,
so that I can identify when multiple capsules or the user are trying to modify the same data, preventing data loss and ensuring integrity.

## Acceptance Criteria

1. **Provenance Check**: The system must check if a field being updated is already managed by another capsule using the `source_capsules` list.
2. **Capsule Conflict Detection**: If a field is managed by another capsule and the new value differs, flag as `CAPSULE_CONFLICT`.
3. **User Conflict Detection**: If a field exists but is NOT in `source_capsules` (user-created), flag as `USER_CONFLICT`.
4. **No Conflict on Identical Values**: If values are identical, no conflict should be raised regardless of ownership.
5. **Conflict Reporting**: The system must return a list of `Conflict` objects containing key, existing value, new value, source, and severity.

## Tasks / Subtasks

- [x] Implement `Conflict` data class
  - [x] Define fields: key, existing_value, new_value, source_capsule, severity
  - [x] Add to `capsule/core/merger.py` or `capsule/models/note.py`
- [x] Implement `ConflictDetector` class in `capsule/core/merger.py`
  - [x] Create `detect_conflicts(existing_fm, new_fm)` method
  - [x] Implement logic to iterate top-level keys
  - [x] Implement provenance checking against `source_capsules`
- [x] Implement User Conflict Logic
  - [x] Check if key exists in `existing_fm` but not in `source_capsules`
  - [x] Flag as `USER_CONFLICT` (Warning/Error)
- [x] Implement Capsule Conflict Logic
  - [x] Check if key is in `source_capsules` but from a different capsule ID
  - [x] Compare values for equality
  - [x] Flag as `CAPSULE_CONFLICT` if different
- [x] Create Unit Tests
  - [x] Test no conflict (identical values)
  - [x] Test capsule conflict (different values, different owner)
  - [x] Test user conflict (existing unmanaged key)
  - [x] Test no conflict (new key)

## Dev Notes

- **Architecture**: The `ConflictDetector` should be part of the `merger` module or a standalone utility used by the merger.
- **Data Structures**:
  ```python
  @dataclass
  class Conflict:
      key: str
      existing_value: Any
      new_value: Any
      source_capsule: str
      severity: str  # "WARNING", "ERROR"
  ```
- **Provenance**: `source_capsules` is a list of dicts or strings? Tech spec says:
  ```yaml
  source_capsules:
    - capsule_id: "tcm-herbs-basic"
      version: "1.0.0"
      sections_managed: ["herb_data", "aliases"]
  ```
  *Note: Architecture.md showed simple list of strings in some examples, but Tech Spec 8 is more detailed. Follow Tech Spec 8 for this implementation.*

### Project Structure Notes

- `capsule/core/merger.py`: Core logic location.
- `capsule/models/note.py`: May need updates to support the detailed `source_capsules` structure if not already present.

### References

- [Source: docs/tech-specs/epic-8-merge-strategies.md#63-conflict-detection]
- [Source: docs/architecture.md#epic-group-5-merge-strategies-fr32-fr38]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/stories/8-4-conflict-detection-logic.context.xml

### Agent Model Used

Claude 3.5 Sonnet (claude-3-5-sonnet-20241022)

### Debug Log References

**Implementation Plan:**
1. Created `Conflict` dataclass in `capsule/core/merger.py` with fields: key, existing_value, new_value, source_capsule, severity
2. Implemented `ConflictDetector` class with `detect_conflicts()` static method
3. Added support for both detailed source_capsules format (dict with sections_managed) and simple string format
4. Implemented provenance checking logic to determine section ownership
5. Distinguished between CAPSULE_CONFLICT (ERROR) and USER_CONFLICT (WARNING)
6. Created 11 comprehensive unit tests covering all acceptance criteria scenarios
7. Verified all 182 existing tests still pass (no regressions)

**Key Design Decisions:**
- Used static method for `detect_conflicts()` since it doesn't require instance state
- Supported both source_capsules formats per Tech Spec 8 (detailed dict and simple string)
- Universal fields (id, name, type, tags, created, updated, source_capsules) are explicitly ignored for conflict detection
- Values are compared using Python's equality operator, which handles deep nested structure comparison
- Same capsule updating its own sections does NOT generate conflicts (per section-level merge strategy)
- Missing or empty source_capsules treats all data as user-created content

### Completion Notes List

✅ **Story 8-4 Implementation Complete**

Implemented full conflict detection system for merge operations:
- `Conflict` dataclass provides structured representation of merge conflicts
- `ConflictDetector.detect_conflicts()` identifies three scenarios:
  1. No conflict when values are identical
  2. CAPSULE_CONFLICT (ERROR) when different capsules try to manage same section
  3. USER_CONFLICT (WARNING) when capsule tries to overwrite user content

**Test Coverage:**
- 11 new tests for ConflictDetector (100% coverage of acceptance criteria)
- All 182 tests in test suite pass
- Tests cover: identical values, new keys, capsule conflicts, user conflicts, multiple conflicts, complex nested structures, edge cases

**Alignment with Tech Spec:**
- Follows Tech Spec 8 section 6.3 (Conflict Detection algorithm)
- Supports detailed source_capsules format from Tech Spec
- Integrates with existing merger.py functions (section_level_merge, additive_merge)
- Ready for integration with Epic 7 Preview system

### File List

**Modified:**
- capsule/core/merger.py (added Conflict dataclass and ConflictDetector class)
- tests/test_core/test_merger.py (added TestConflictDetector with 11 test methods)
- docs/sprint-artifacts/8-4-conflict-detection-logic.md (updated task checkboxes, added completion notes)

## Change Log

- Created story based on Epic 8 and Tech Spec 8.
- Implemented Conflict dataclass and ConflictDetector class with full test coverage (Date: 2025-11-21)

# Senior Developer Review (AI)

- **Reviewer**: BMad
- **Date**: 2025-11-21
- **Outcome**: Approve

## Summary
The implementation of the conflict detection logic is excellent. The code is well-structured, thoroughly tested, and meets all acceptance criteria. The developer has shown a clear understanding of the requirements and has produced a high-quality module.

## Key Findings
No significant findings. The code is clean, robust, and well-documented.

## Acceptance Criteria Coverage
| AC# | Description | Status | Evidence |
|---|---|---|---|
| 1 | Provenance Check | IMPLEMENTED | `merger.py:100-114` |
| 2 | Capsule Conflict Detection | IMPLEMENTED | `merger.py:137-147` |
| 3 | User Conflict Detection | IMPLEMENTED | `merger.py:149-159` |
| 4 | No Conflict on Identical Values | IMPLEMENTED | `merger.py:129` |
| 5 | Conflict Reporting | IMPLEMENTED | `merger.py:50-162` |

**Summary**: 5 of 5 acceptance criteria fully implemented.

## Task Completion Validation
All tasks marked as complete have been verified. The implementation is present in `capsule/core/merger.py` and the tests in `tests/test_core/test_merger.py`.

**Summary**: All completed tasks verified.

## Test Coverage and Gaps
The `TestConflictDetector` class in `tests/test_core/test_merger.py` provides excellent test coverage for the new logic, including edge cases and different conflict scenarios. No gaps were identified.

## Architectural Alignment
The implementation aligns perfectly with the architecture defined in `docs/architecture.md` and the tech spec in `docs/tech-specs/epic-8-merge-strategies.md`.

## Action Items
- **Advisory Notes**:
  - Note: Consider adding logging to the `ConflictDetector` for easier debugging in the future.

