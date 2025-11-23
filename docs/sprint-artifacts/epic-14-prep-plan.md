# Epic 14 Preparation Sprint Plan

## Overview
**Goal:** Clear critical path items before starting Epic 14 ("Testing Infrastructure").
**Duration:** 2 days
**Participants:** Charlie, Dana, Alice

## Critical Tasks

### 1. Verify CSS Deployment (Charlie - 2h)
- **Status:** Done
- **Description:** Ensure `capsule generate` command copies the `capsule/templates/css` directory to the user's `.obsidian/snippets` folder or a `css` folder within the capsule.
- **Action:** Check `capsule/core/generator.py` and `capsule/commands/generate.py`. Implement if missing.
- **Verification:** Run `capsule generate` and check for CSS files.

### 2. Mobile Responsiveness Check (Dana - 2h)
- **Status:** Done
- **Description:** Verify that the dashboard and generated content look good on mobile.
- **Action:** Review `capsule/templates/css/layouts/responsive.css`. Test with a sample capsule.
- **Verification:** Visual inspection (simulated).

### 3. Pytest Configuration & Fixture Strategy (Charlie - 4h)
- **Status:** Done
- **Description:** Set up `pytest` configuration and fixtures for efficient testing.
- **Action:** Create/Update `pytest.ini` or `pyproject.toml`. Create `tests/conftest.py`.
- **Verification:** Run `pytest` and ensure it picks up the configuration.

### 4. User Guide Update (Alice - 4h)
- **Status:** Done
- **Description:** Update the user guide to reflect recent changes (Dashboards, etc.).
- **Action:** Update `docs/guides/user-guide.md` (or similar).
- **Verification:** Review the updated guide.

## Execution Log

- [x] Task 1: Verify CSS Deployment
- [x] Task 2: Mobile Responsiveness Check
- [x] Task 3: Pytest Configuration
- [x] Task 4: User Guide Update
