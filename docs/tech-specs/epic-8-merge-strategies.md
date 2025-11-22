# Technical Specification: Epic 8 - Merge Strategies

## 1. Overview
This specification details the implementation of intelligent merging logic for the Obsidian Capsule Delivery System. The goal is to safely update existing notes with new capsule content while strictly preserving user customizations. This system treats the user's notes as the source of truth for body content, while allowing capsules to manage and update specific frontmatter sections.

## 2. Goals
- **Section-Level Merge:** Update specific frontmatter sections (e.g., `herb_data`) while leaving others untouched.
- **Additive Merge:** Add new sections from different capsules (e.g., adding `recipe_data` to an existing `herb` note).
- **Conflict Detection:** Identify when two capsules try to write to the same section.
- **User Content Preservation:** CRITICAL. Never modify the markdown body of a note, only the frontmatter.
- **Provenance Tracking:** Track which capsules contributed to a note via `source_capsules`.

## 3. Non-Goals
- **Body Content Merging:** We will NOT attempt to merge markdown body content. If the body exists, it is immutable to the capsule system.
- **Real-time Synchronization:** This is a batch import process, not a real-time sync engine.
- **Git-style Conflict Resolution:** We will not ask users to resolve line-by-line diffs. Conflicts are handled at the section level.

## 4. Architecture

### 4.1 Components
- **`capsule/core/merger.py`**: The core logic engine responsible for taking an existing note and a new note, and producing a merged result.
- **`capsule/utils/frontmatter.py`**: Robust utilities for reading/writing frontmatter. Must use `ruamel.yaml` to preserve comments and ordering.
- **`capsule/models/note.py`**: Enhanced to support multi-source tracking and validation of merge operations.

### 4.2 Data Flow
1. **Read:** `frontmatter.py` reads the existing note from disk.
2. **Parse:** Separates Frontmatter (YAML) and Body (Markdown).
3. **Merge:** `merger.py` compares existing frontmatter with new capsule frontmatter.
   - Checks `source_capsules` for provenance.
   - Applies merge strategies (Overwrite, Append, Ignore).
   - Detects conflicts.
4. **Write:** If merge is successful, writes back to disk using `frontmatter.py`, ensuring the body is untouched.

## 5. Data Structures

### 5.1 Frontmatter Schema Extensions
To support provenance, every managed note will include:
```yaml
source_capsules:
  - capsule_id: "tcm-herbs-basic"
    version: "1.0.0"
    sections_managed: ["herb_data", "aliases"]
  - capsule_id: "tcm-recipes-addon"
    version: "1.2.0"
    sections_managed: ["recipe_data"]
```

### 5.2 MergeResult Class
```python
@dataclass
class MergeResult:
    success: bool
    merged_frontmatter: Dict
    conflicts: List[Conflict]
    changes: List[Change]
```

### 5.3 Conflict Class
```python
@dataclass
class Conflict:
    key: str
    existing_value: Any
    new_value: Any
    source_capsule: str
    severity: str  # "WARNING", "ERROR"
```

## 6. Algorithms

### 6.1 Section-Level Merge
Logic to update existing keys within a specific domain section.
1. Identify target section (e.g., `herb_data`).
2. If section exists:
   - For each key in new data:
     - If key missing in existing: Add it.
     - If key exists and value differs: Update it (if owned by same capsule) OR Raise Conflict (if owned by user/other capsule).
3. If section missing: Create it.

### 6.2 Additive Merge
Logic to append new domain sections to existing notes.
1. Check if the top-level key (e.g., `recipe_data`) exists.
2. If not, simply add the entire block.
3. Update `source_capsules` to include the new capsule ID.

### 6.3 Conflict Detection
1. Iterate through all top-level keys in the new capsule data.
2. Check if key is already managed by another capsule in `source_capsules`.
3. If managed by another capsule:
   - If values are identical: No conflict.
   - If values differ: Flag as CONFLICT.
4. If key exists but is NOT in `source_capsules` (User created):
   - Flag as USER_CONFLICT (requires user approval to overwrite).

## 7. Stories & Implementation Plan

### 8-1: Frontmatter Parser Utilities
**Goal:** Robust utilities for reading/writing frontmatter without destroying comments or ordering.
- **Task:** Implement `FrontmatterHandler` class using `ruamel.yaml`.
- **Requirement:** Must pass round-trip tests (Read -> Write -> Read) with zero loss of comments or formatting.

### 8-2: Section-Level Merge Algorithm
**Goal:** Logic to update existing keys within a specific domain section.
- **Task:** Implement `Merger.merge_section(existing_dict, new_dict, strategy)`.
- **Strategies:** `OVERWRITE`, `KEEP_EXISTING`, `MERGE_LISTS`.

### 8-3: Additive Merge Algorithm
**Goal:** Logic to append new domain sections to existing notes.
- **Task:** Implement `Merger.merge_note(existing_note, new_note)`.
- **Logic:** Handle top-level key additions and `source_capsules` updates.

### 8-4: Conflict Detection Logic
**Goal:** Logic to raise errors/warnings when `source_capsules` conflict.
- **Task:** Implement `ConflictDetector` class.
- **Output:** List of conflicts to be presented to the user (via the Preview system from Epic 7).

### 8-5: User Content Preservation
**Goal:** Tests and safeguards to ensure body content is immutable during merge.
- **Task:** Create a "Safety Wrapper" around the write operation.
- **Check:** Calculate hash of body content before and after merge. If different, ABORT.

### 8-6: Provenance Tracking
**Goal:** Managing the `source_capsules` list in frontmatter.
- **Task:** Logic to update the `source_capsules` list, handling version bumps and new capsule additions.

## 8. Security & Safety
- **Backup:** Always create a backup of the note before writing (leveraging Epic 7 Backup System).
- **Atomic Writes:** Use temporary files and rename to ensure atomic writes.
- **Validation:** Validate the merged YAML against the schema before writing.

## 9. Testing Strategy
- **Unit Tests:** Test each merge strategy with various dictionary permutations.
- **Integration Tests:** Simulate a full import process with conflicting and non-conflicting capsules.
- **Fuzz Testing:** Feed random YAML structures to ensure the parser doesn't crash.
- **Safety Tests:** specifically test that body content is preserved byte-for-byte.

## Post-Review Follow-ups
- Note: Consider adding logging to the `ConflictDetector` for easier debugging in the future (from review of story 8.4).

