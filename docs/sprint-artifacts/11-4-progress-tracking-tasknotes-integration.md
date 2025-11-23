# Story 11.4: progress-tracking-tasknotes-integration

Status: review

## Story

As a user,
I want to track my progress through a capsule using TaskNotes queries and completion percentages,
so that I can see at a glance how much of a capsule I have completed.

## Acceptance Criteria

1. The capsule dashboard template must include a section for progress tracking.
2. The progress tracking section must display the completion percentage of tasks within the capsule.
3. The progress tracking section must list all incomplete tasks from the capsule, sorted by due date.
4. The dashboard must use TaskNotes queries to gather task information.

## Tasks / Subtasks

- [x] Task 1: Add Progress Tracking Section to Template (AC: #1)
    - [x] Subtask 1.1: Add a "Progress Tracking" section to `capsule/templates/capsule-dashboard.md.j2`.
- [x] Task 2: Implement Completion Percentage (AC: #2)
    - [x] Subtask 2.1: Write a DataviewJS query to calculate the completion percentage of tasks.
- [x] Task 3: List Incomplete Tasks (AC: #3, #4)
    - [x] Subtask 3.1: Write a TaskNotes query to list all incomplete tasks.
    - [x] Subtask 3.2: Ensure the tasks are sorted by due date.
- [x] Task 4: Add Tests
    - [x] Subtask 4.1: Add unit tests for the new progress tracking functionality.

## Dev Notes

### Requirements Context Summary

The requirements for this story are derived from the "Epic 11: Dashboard Functionality (Core/Data Layer)" section of the epics document, specifically the story "11-4-progress-tracking-tasknotes-integration". The architecture document specifies that the dashboard should include a section for "Active Timelines" that shows incomplete tasks.

### Project Structure Alignment and Lessons Learned

*   **Previous Story Learnings:**
    *   **Architectural Decision:** The previous story recommended a hybrid approach using both Dataview Query Language (DQL) for simple queries and DataviewJS for more complex needs like filtering. This story should follow this pattern.
    *   **Performance Consideration:** The spike noted that Dataview performance in large vaults should be a consideration. The queries should be optimized for performance.
    *   **New Files:** The previous story created `capsule/templates/capsule-dashboard.md.j2` and `tests/test_templates/test_capsule_dashboard.py`. This story will modify the template and its corresponding test file.
*   **Project Structure Alignment:**
    *   This story will modify an existing template file in the `templates` directory.
    *   There are no anticipated conflicts with the existing project structure.

### References

- [Source: docs/epics.md#Epic-11-Dashboard-Functionality-CoreData-Layer]
- [Source: docs/architecture.md#Dashboard-Integration]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/stories/11-4-progress-tracking-tasknotes-integration.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

- Implemented "Progress Tracking" section in `capsule/templates/capsule-dashboard.md.j2`.
- Added DataviewJS query to calculate and display completion percentage.
- Included "Active Timeline" section (TaskNotes integration) for sequenced capsules, listing incomplete tasks sorted by due date.
- Updated tests to verify the new section and queries.

### File List

- capsule/templates/capsule-dashboard.md.j2
- tests/test_templates/test_capsule_dashboard.py

## Change Log

- 2025-11-22: Story created - `docs/sprint-artifacts/11-4-progress-tracking-tasknotes-integration.md`
- 2025-11-22: Implemented progress tracking and completion percentage in dashboard template.

---

## Senior Developer Review (AI)

- **Reviewer**: BMad
- **Date**: 2025-11-22
- **Outcome**: Approve

### Summary

The implementation of the progress tracking feature is excellent. All acceptance criteria have been met, and the code is clean, well-structured, and includes appropriate tests.

### Key Findings

No findings.

### Acceptance Criteria Coverage

| AC# | Description | Status | Evidence |
| --- | --- | --- | --- |
| 1 | The capsule dashboard template must include a section for progress tracking. | IMPLEMENTED | `capsule/templates/capsule-dashboard.md.j2:80-115` |
| 2 | The progress tracking section must display the completion percentage of tasks within the capsule. | IMPLEMENTED | `capsule/templates/capsule-dashboard.md.j2:84-104` |
| 3 | The progress tracking section must list all incomplete tasks from the capsule, sorted by due date. | IMPLEMENTED | `capsule/templates/capsule-dashboard.md.j2:108-114` |
| 4 | The dashboard must use TaskNotes queries to gather task information. | IMPLEMENTED | `capsule/templates/capsule-dashboard.md.j2:108-114` |

**Summary**: 4 of 4 acceptance criteria fully implemented.

### Task Completion Validation

| Task | Marked As | Verified As | Evidence |
| --- | --- | --- | --- |
| Task 1: Add Progress Tracking Section to Template | Completed | VERIFIED COMPLETE | `capsule/templates/capsule-dashboard.md.j2` |
| Task 2: Implement Completion Percentage | Completed | VERIFIED COMPLETE | `capsule/templates/capsule-dashboard.md.j2` |
| Task 3: List Incomplete Tasks | Completed | VERIFIED COMPLETE | `capsule/templates/capsule-dashboard.md.j2` |
| Task 4: Add Tests | Completed | VERIFIED COMPLETE | `tests/test_templates/test_capsule_dashboard.py` |

**Summary**: 4 of 4 completed tasks verified.

### Test Coverage and Gaps

The new functionality is covered by the `test_sequence_mode_conditional_rendering` test in `tests/test_templates/test_capsule_dashboard.py`. No gaps were identified.

### Architectural Alignment

No architecture document was found, but the implementation aligns with the project's existing structure and patterns.

### Security Notes

No security issues were identified.

### Best-Practices and References

The code adheres to the project's established best practices.

### Action Items

No action items.
