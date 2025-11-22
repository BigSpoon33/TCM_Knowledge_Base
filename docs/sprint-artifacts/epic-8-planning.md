# Epic 8 Planning: Merge Strategies

**Date:** 2025-11-21
**Status:** PLANNED

## Overview
Epic 8 focuses on the core logic for merging capsule content into existing user notes. This is a high-risk, high-value epic that directly impacts data integrity. The goal is to allow capsules to update their specific data sections without ever touching user content or other capsules' data.

## Technical Context
- **Tech Spec:** `docs/tech-specs/epic-8-merge-strategies.md`
- **Key Components:** `Merger`, `FrontmatterHandler`, `ConflictDetector`
- **Critical Constraint:** Markdown body content is immutable.

## Stories & Estimates

| ID | Story | Priority | Est. Effort | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| **8.1** | **Frontmatter Parser Utilities** | High | 3 pts | None |
| **8.2** | **Section-Level Merge Algorithm** | High | 5 pts | 8.1 |
| **8.3** | **Additive Merge Algorithm** | High | 3 pts | 8.1 |
| **8.4** | **Conflict Detection Logic** | Medium | 3 pts | 8.2, 8.3 |
| **8.5** | **User Content Preservation (Safety Wrapper)** | Critical | 5 pts | 8.1 |
| **8.6** | **Provenance Tracking** | Medium | 2 pts | 8.1 |

## Sprint Strategy
We will likely break this into 2 sprints:
1.  **Sprint 1:** Core Infrastructure (8.1, 8.5) and Basic Merging (8.2). Focus on safety first.
2.  **Sprint 2:** Advanced Merging (8.3), Conflict Detection (8.4), and Provenance (8.6).

## Risks
- **Data Loss:** If the parser fails to preserve comments or structure, users will be unhappy.
    - *Mitigation:* Extensive round-trip testing in Story 8.1.
- **Complexity:** Merging nested dictionaries can get messy.
    - *Mitigation:* Strict schema validation and unit tests for edge cases.

## Next Steps
1.  Start Sprint 1.
2.  Assign Story 8.1 (Frontmatter Utilities) as the first task.
