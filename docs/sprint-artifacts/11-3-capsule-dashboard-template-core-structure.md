# Story 11.3: capsule-dashboard-template-core-structure

Status: review

## Story

As a user,
I want a capsule dashboard with metadata, navigation, and file counts,
so that I can get a clear overview of the contents and status of each capsule.

## Acceptance Criteria

1. Create a capsule dashboard template file.
2. The dashboard must display the capsule's metadata (`capsule_id`, `version`, `domain_type`, `sequence_mode`).
3. The dashboard must provide quick links for navigation (e.g., back to the master dashboard).
4. The dashboard must display the total number of root notes and study materials.
5. The dashboard must list all root notes with their type, tags, and last updated date.
6. The dashboard must list all study materials (flashcards, quizzes).

## Tasks / Subtasks

- [x] Task 1: Create Capsule Dashboard Template (AC: #1)
    - [x] Subtask 1.1: Create a new file `templates/capsule-dashboard-template.md`.
    - [x] Subtask 1.2: Add a header and basic structure to the template.
- [x] Task 2: Display Capsule Metadata (AC: #2)
    - [x] Subtask 2.1: Add placeholders for `capsule_id`, `version`, `domain_type`, and `sequence_mode`.
- [x] Task 3: Implement Navigation (AC: #3)
    - [x] Subtask 3.1: Add a link to the master dashboard.
- [x] Task 4: Display File Counts (AC: #4)
    - [x] Subtask 4.1: Write a Dataview query to count the number of root notes.
    - [x] Subtask 4.2: Write a Dataview query to count the number of study materials.
- [x] Task 5: List Root Notes and Study Materials (AC: #5, #6)
    - [x] Subtask 5.1: Write a Dataview query to list all root notes.
    - [x] Subtask 5.2: Write a Dataview query to list all study materials.
- [x] Task 6: Add Tests
    - [x] Subtask 6.1: Add unit tests for the new template.


## Dev Agent Record

- **Context Reference**: `docs/sprint-artifacts/stories/11-3-capsule-dashboard-template-core-structure.context.xml`

### Completion Notes

- Created `capsule/templates/capsule-dashboard.md.j2` with all required sections and queries.
- Implemented Dataview queries for root notes, study materials, and recent activity.
- Implemented DataviewJS inline queries for file counts.
- Added conditional rendering for "Active Timeline" section based on `sequence_mode`.
- Added unit tests in `tests/test_templates/test_capsule_dashboard.py` covering template existence, rendering, frontmatter, sections, and queries.
- Fixed regression in `tests/test_templates/test_master_dashboard.py` caused by template updates in previous story.

### File List

- capsule/templates/capsule-dashboard.md.j2
- tests/test_templates/test_capsule_dashboard.py
- tests/test_templates/test_master_dashboard.py

## Dev Notes

- The primary architectural driver for this story is the "Dashboard Integration" section of the architecture document, which provides templates for the dashboards. [Source: `docs/architecture.md#Dashboard-Integration`]
- The requirements for this story are derived from the "Epic 11: Dashboard Functionality (Core/Data Layer)" section of the epics document. [Source: `docs/epics.md`]
- The feasibility of querying the proposed schema fields has been validated in the technical spike. [Source: `docs/sprint-artifacts/11-0-dataview-spike-poc.md`]

### Learnings from Previous Story

*   **From Story 11.2 (Status: done)**
    *   **Architectural Decision:** A hybrid DQL/DataviewJS approach is recommended for dashboards. This story should use DataviewJS for filtering logic.
    *   **Performance:** Dataview performance should be considered. The queries should be as efficient as possible.
    *   **New Files:** The previous story created `tests/fixtures/sample_capsule_dashboard.md` and `tests/fixtures/dashboard_schema_test_plan.md`, which can be used for testing the master dashboard.
    *   **Modified Files:** The previous story modified `docs/architecture.md` to include the dashboard schema. This story should update the same document with information about the master dashboard.
    *   **Technical Debt:** No tests were added for the new master dashboard functionality.

### Project Structure Notes

**Structure Alignment Summary**

*   **Previous Story Learnings:**
    *   **Architectural Decision:** The previous story recommended a hybrid approach using both Dataview Query Language (DQL) for simple queries and DataviewJS for more complex needs like filtering. This story should follow this pattern.
    *   **Performance Consideration:** The spike noted that Dataview performance in large vaults should be a consideration. The capsule dashboard queries should be optimized for performance.
    *   **Technical Debt:** The previous story did not add tests for the master dashboard. This story should include tests for the capsule dashboard.
*   **Project Structure Alignment:**
    *   This story will create a new template file in the `templates` directory.
    *   There are no anticipated conflicts with the existing project structure.

### References

- Cite all technical details with source paths and sections, e.g. [Source: docs/<file>.md#Section]

## Change Log

- 2025-11-22: Story created - `docs/sprint-artifacts/11-3-capsule-dashboard-template-core-structure.md`
- 2025-11-22: Story completed - Template created and tested.
- 2025-11-22: Senior Developer Review notes appended.

---
## Senior Developer Review (AI)

- **Reviewer:** BMad
- **Date:** 2025-11-22
- **Outcome:** Approve

### Summary

The implementation of the capsule dashboard template is excellent. All acceptance criteria have been met, and all tasks marked as complete have been verified. The code is clean, well-tested, and aligns with the project's architecture and technical specifications.

### Key Findings

No findings.

### Acceptance Criteria Coverage

| AC# | Description | Status | Evidence |
|---|---|---|---|
| 1 | Create a capsule dashboard template file. | IMPLEMENTED | `capsule/templates/capsule-dashboard.md.j2` |
| 2 | The dashboard must display the capsule's metadata. | IMPLEMENTED | `capsule/templates/capsule-dashboard.md.j2:3-4, 28-31` |
| 3 | The dashboard must provide quick links for navigation. | IMPLEMENTED | `capsule/templates/capsule-dashboard.md.j2:34` |
| 4 | The dashboard must display the total number of root notes and study materials. | IMPLEMENTED | `capsule/templates/capsule-dashboard.md.j2:35-36` |
| 5 | The dashboard must list all root notes. | IMPLEMENTED | `capsule/templates/capsule-dashboard.md.j2:42-53` |
| 6 | The dashboard must list all study materials. | IMPLEMENTED | `capsule/templates/capsule-dashboard.md.j2:60-75` |

**Summary:** 6 of 6 acceptance criteria fully implemented.

### Task Completion Validation

| Task | Marked As | Verified As | Evidence |
|---|---|---|---|
| Task 1: Create Capsule Dashboard Template | Completed | VERIFIED COMPLETE | `capsule/templates/capsule-dashboard.md.j2` |
| Task 2: Display Capsule Metadata | Completed | VERIFIED COMPLETE | `capsule/templates/capsule-dashboard.md.j2` |
| Task 3: Implement Navigation | Completed | VERIFIED COMPLETE | `capsule/templates/capsule-dashboard.md.j2` |
| Task 4: Display File Counts | Completed | VERIFIED COMPLETE | `capsule/templates/capsule-dashboard.md.j2` |
| Task 5: List Root Notes and Study Materials | Completed | VERIFIED COMPLETE | `capsule/templates/capsule-dashboard.md.j2` |
| Task 6: Add Tests | Completed | VERIFIED COMPLETE | `tests/test_templates/test_capsule_dashboard.py` |

**Summary:** 6 of 6 completed tasks verified.

### Test Coverage and Gaps

- Unit tests in `tests/test_templates/test_capsule_dashboard.py` provide good coverage for the template's functionality.
- No gaps in testing were identified.

### Architectural Alignment

- The implementation aligns perfectly with the architecture and the tech spec for Epic 11.

### Security Notes

- No security issues were found.

### Best-Practices and References

- The code adheres to the project's established best practices.

### Action Items

**Advisory Notes:**
- Note: None.

