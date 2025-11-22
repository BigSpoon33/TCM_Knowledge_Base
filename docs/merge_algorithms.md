# Merge Algorithms: Section-Level vs. Additive

This document explains the two primary merge strategies used by the Obsidian Capsule Delivery System when importing content into an existing vault.

## Overview

When importing a capsule, the system must decide how to handle files that already exist in the user's vault. The decision depends on the relationship between the incoming capsule and the existing file's source.

## 1. Section-Level Merge (Update)

**Scenario:** The existing file in the vault was previously installed by the *same* capsule that is currently being imported (an update).

**Goal:** Update the content managed by this capsule without overwriting user customizations or content from other capsules.

**Mechanism:**
1.  **Identification:** The system checks the `source_capsules` list in the file's frontmatter. If the incoming capsule ID is present, it's an update.
2.  **Parsing:** Both the existing file and the incoming file are parsed to identify "sections".
    *   **Markdown Sections:** Defined by headers (e.g., `## Study Notes`).
    *   **Frontmatter Fields:** Specific keys in the YAML frontmatter.
3.  **Matching:** Sections are matched by their headers/keys.
4.  **Replacement:**
    *   If a section exists in both, the content from the *incoming* capsule replaces the content in the *existing* file.
    *   If a section exists only in the incoming capsule, it is added to the existing file.
    *   If a section exists only in the existing file (user content), it is *preserved* untouched.
5.  **Outcome:** The file is updated with the latest capsule content while preserving user notes.

**Example:**
*   **Existing:** Contains `## Study Notes` (User content) and `## Definition` (Capsule v1 content).
*   **Incoming:** Contains `## Definition` (Capsule v2 content) and `## Examples` (New Capsule v2 content).
*   **Result:** `## Study Notes` (Preserved), `## Definition` (Updated to v2), `## Examples` (Added).

## 2. Additive Merge (New Content)

**Scenario:** The existing file in the vault was created by the user or a *different* capsule.

**Goal:** Add the new capsule's content to the file without disrupting the existing context.

**Mechanism:**
1.  **Identification:** The incoming capsule ID is *not* in the `source_capsules` list.
2.  **Conflict Detection:** The system checks for "Domain Sections" (frontmatter keys ending in `_data`, e.g., `tcm_data`).
    *   If the existing file already has the same domain section, it is flagged as a **Conflict**.
3.  **Appending:**
    *   If no conflict, the new capsule's content is appended to the end of the file.
    *   New frontmatter fields are merged into the existing frontmatter.
    *   The incoming capsule ID is added to `source_capsules`.
4.  **Outcome:** The file now contains content from multiple sources.

**Example:**
*   **Existing:** A user note about "Headaches".
*   **Incoming:** A TCM capsule note about "Headaches" containing `## TCM Perspective`.
*   **Result:** The file retains the user's text and appends `## TCM Perspective` at the end.

## Summary Table

| Feature | Section-Level Merge | Additive Merge |
| :--- | :--- | :--- |
| **Trigger** | Same Capsule ID in `source_capsules` | Different or No Capsule ID |
| **Primary Action** | Replace specific sections | Append content to end of file |
| **User Content** | Preserved (if outside managed sections) | Preserved |
| **Conflict Risk** | Low (Managed by capsule structure) | Medium (Domain section collisions) |
| **Use Case** | Updating a capsule to a new version | Installing a new capsule that overlaps with existing notes |
