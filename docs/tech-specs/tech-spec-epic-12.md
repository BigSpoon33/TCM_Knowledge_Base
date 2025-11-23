# Technical Specification: Epic 12 - Dashboard Polish & Interactivity

**Epic ID:** 12  
**Author:** Lead Architect  
**Date:** 2025-11-22  
**Status:** DRAFT  
**Version:** 1.0  

---

## 1. Executive Summary

Epic 12 aims to transform the functional dashboards delivered in Epic 11 into polished, production-ready navigation hubs. The primary objective is to elevate the user experience from "utilitarian" (Bronze Tier) to "delightful" (Silver/Gold Tier) through advanced visual design, interactive widgets, and responsive layouts.

This specification defines the technical architecture for:
1.  A robust **CSS Theming System** that supports multiple visual themes (Neon, Minimal, Academic) and ensures compatibility across Obsidian's ecosystem.
2.  **Interactive Components** powered by the Meta-Bind plugin, enabling users to filter content, track progress, and navigate capsules dynamically.
3.  **Responsive Design** standards to ensure dashboards function seamlessly across desktop, tablet, and mobile devices.

The successful execution of this epic will result in dashboards that are not only functional but also serve as a competitive differentiator for the Obsidian Capsule Delivery System (OCDS).

---

## 2. Architecture & Design

### 2.1 CSS Architecture

We will adopt a modular CSS architecture to ensure maintainability, scalability, and theme compatibility. The system will leverage Obsidian's CSS snippet capability.

**File Structure:**
We will organize CSS files within `capsule/templates/css/` which will be distributed to the user's `.obsidian/snippets/` folder.

```
capsule/templates/css/
├── base/
│   ├── variables.css           # Global CSS variables (colors, spacing, typography)
│   ├── reset.css               # Dashboard-specific resets to normalize behavior
│   └── typography.css          # Font definitions and text styles
├── themes/
│   ├── neon.css                # "Neon" theme variant (High contrast, vibrant)
│   ├── minimal.css             # "Minimal" theme variant (Clean, professional)
│   └── academic.css            # "Academic" theme variant (Traditional, serif)
├── components/
│   ├── headers.css             # Dashboard header styles
│   ├── sections.css            # Section containers, dividers, and cards
│   ├── widgets.css             # Meta-Bind widget styling (buttons, inputs)
│   ├── progress.css            # Progress bar and stat styling
│   └── tables.css              # Dataview table enhancements
└── layouts/
    ├── master-dashboard.css    # Grid layouts for the Master Dashboard
    ├── capsule-dashboard.css   # Layouts for Capsule Dashboards
    └── responsive.css          # Media queries for mobile/tablet adaptation
```

**Class Naming Convention:**
We will use a simplified BEM (Block Element Modifier) approach to avoid conflicts with other plugins or themes.
*   Prefix: `.ocds-`
*   Example: `.ocds-card`, `.ocds-card__header`, `.ocds-card--featured`

**Theme Compatibility Strategy:**
*   **Variable Abstraction:** All colors and dimensions will be defined as CSS variables (`--ocds-color-primary`, `--ocds-spacing-md`).
*   **Fallback Support:** Variables will fallback to standard Obsidian theme variables (e.g., `--background-primary`) to ensure decent rendering if a specific theme is missing.
*   **Scoped Styling:** Styles will be scoped to specific dashboard types using data attributes where possible (e.g., `[data-note-type="capsule_dashboard"]`).

### 2.2 Component Architecture

Standardized components will be developed to ensure consistency across all dashboards.

**1. Status Cards (`.ocds-stat-card`)**
*   **Purpose:** Display key metrics (e.g., "Total Capsules", "Cards Due").
*   **Structure:** Icon + Large Value + Label.
*   **Interactivity:** Optional click-through to detailed views.

**2. Progress Trackers (`.ocds-progress`)**
*   **Purpose:** Visualize completion status.
*   **Implementation:**
    *   **Linear Bar:** CSS-styled `div` width controlled by inline styles or Meta-Bind.
    *   **Circular:** Conic-gradient CSS for circular progress.
    *   **Meta-Bind Integration:** `INPUT[progressBar(...)]` wrapped in a custom container for styling.

**3. Navigation Grids (`.ocds-nav-grid`)**
*   **Purpose:** Quick access to capsule sections.
*   **Structure:** Grid layout of buttons or cards.
*   **Responsive:** 4 columns (Desktop) -> 2 columns (Tablet) -> 1 column (Mobile).

**4. Enhanced Tables (`.ocds-table`)**
*   **Purpose:** Display Dataview results cleanly.
*   **Features:** Striped rows, hover effects, status badges (Active/Inactive), and compact mode for mobile.

### 2.3 Plugin Integration

**Meta-Bind Integration:**
Meta-Bind is the core engine for interactivity. We will use it for:

*   **Navigation Buttons:**
    ```markdown
    ```meta-bind-button
    label: Start Learning
    style: primary
    class: ocds-btn-primary
    action:
      type: open
      link: "[[First_Root_Note]]"
    ```
    ```
*   **Filtering Controls:**
    *   Use `INPUT[select(...)]` bound to frontmatter fields (e.g., `filter_category`).
    *   DataviewJS queries will read these frontmatter fields to dynamically filter results.
    *   *Note:* Since DataviewJS doesn't auto-react to frontmatter changes instantly in all cases, we will implement a "Refresh" button pattern or rely on Obsidian's cache update cycle.

**Dataview Integration:**
*   **Performance:** All queries must use `LIMIT` clauses.
*   **Styling:** Wrap Dataview blocks in `div` containers with specific classes (e.g., `<div class="ocds-table-container">`) to apply custom CSS without affecting global Dataview styles.

---

## 3. Data Models & Schemas

### 3.1 Frontmatter Updates

Dashboards will require extended frontmatter to support theming and state management for widgets.

**Master Dashboard Frontmatter:**
```yaml
type: master_dashboard
theme: "neon"           # Default theme preference
filter_class: "All"     # State for class filter
filter_status: "Active" # State for status filter
last_updated: 2025-11-22
```

**Capsule Dashboard Frontmatter:**
```yaml
type: capsule_dashboard
capsule_id: "tcm-formulas-v1"
theme: "default"        # Inherits or overrides master
progress_root_notes: 45 # Cached metric
progress_flashcards: 150 # Cached metric
view_mode: "standard"   # standard | compact
```

### 3.2 Widget Configuration Schema

We will define standard widget configurations in `capsule/core/config.yaml` (or similar registry) to allow the CLI to generate them consistently.

```yaml
widgets:
  navigation_button:
    template: |
      ```meta-bind-button
      label: {{label}}
      style: {{style}}
      action:
        type: open
        link: "{{link}}"
      ```
  progress_bar:
    template: |
      ```meta-bind
      INPUT[progressBar(minValue(0), maxValue({{max}}), value({{current}}))]
      ```
```

---

## 4. Implementation Plan

### Phase 1: Foundation (CSS + Core)
*Focus: Visual structure and theming infrastructure.*

*   **Task 1.1 (Story 12-1):** Set up CSS file structure in `capsule/templates/css/`. Implement `variables.css` and `reset.css`.
*   **Task 1.2 (Story 12-2):** Implement `typography.css` and `sections.css`. Define standard headers and dividers.
*   **Task 1.3 (Story 12-3):** Create `neon.css`, `minimal.css`, and `academic.css` theme files.
*   **Task 1.4:** Update Jinja2 templates for Dashboards to include necessary HTML classes (`ocds-dashboard`, `ocds-header`, etc.).

### Phase 2: Interactivity (Meta-Bind)
*Focus: Functional widgets and dynamic data.*

*   **Task 2.1 (Story 12-4):** Create a "Widget Gallery" test note to validate Meta-Bind syntax for Buttons, Inputs, and Progress bars.
*   **Task 2.2 (Story 12-5):** Implement Navigation Buttons in Capsule Dashboard templates.
*   **Task 2.3 (Story 12-6):** Implement Filtering Controls in Master Dashboard. Connect Frontmatter inputs to DataviewJS queries.
*   **Task 2.4:** Implement Progress Bars using Meta-Bind `progressBar` input type, styled with `progress.css`.

### Phase 3: Polish & Docs
*Focus: Mobile, compatibility, and user guidance.*

*   **Task 3.1 (Story 12-9):** Implement `responsive.css`. Test grid collapsing on mobile widths.
*   **Task 3.2 (Story 12-10):** Test dashboards against standard Obsidian themes (Default, Minimal). Add compatibility overrides if needed.
*   **Task 3.3 (Story 12-11):** Generate screenshots and GIFs for the "Inspiration Gallery".
*   **Task 3.4 (Story 12-12):** Write "Customization Guide" for users.

---

## 5. Testing Strategy

### 5.1 Visual Regression Testing
*   **Method:** Manual verification using a "Gold Master" vault.
*   **Process:**
    1.  Generate dashboards using the CLI.
    2.  Compare rendering against approved design mockups/screenshots.
    3.  Verify spacing, alignment, and color contrast.

### 5.2 Mobile Compatibility Testing
*   **Device Targets:** Mobile (Phone) and Tablet views.
*   **Key Checks:**
    *   Do grids collapse to single columns?
    *   Are touch targets (buttons) at least 44x44px?
    *   Do tables scroll horizontally without breaking layout?

### 5.3 Performance Benchmarking
*   **Metric:** Dashboard render time.
*   **Target:** < 2 seconds for initial load.
*   **Test Data:** Vault with 50 capsules and 500 notes.
*   **Optimization:** Ensure Dataview queries use `LIMIT` and specific `FROM` clauses to avoid scanning the entire vault.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
| :--- | :--- | :--- |
| **Meta-Bind Syntax Changes** | High | Pin plugin version requirements. Use standard, documented syntax only. |
| **Theme Conflicts** | Medium | Use high-specificity CSS selectors (`.ocds-dashboard .ocds-card`) to prevent theme styles from bleeding in. |
| **Performance Degradation** | Medium | Limit the number of active widgets per page. Use lazy loading techniques for heavy queries if possible. |
| **Mobile Layout Issues** | Low | "Mobile First" CSS design approach. Test on mobile early in Phase 3. |

---

## 7. Summary of Architectural Decisions

1.  **CSS-First Approach:** We are prioritizing a robust CSS foundation over complex JavaScript to ensure stability and performance.
2.  **Meta-Bind as Standard:** We are standardizing on Meta-Bind for all interactive elements to reduce dependency sprawl.
3.  **Scoped Styling:** We are using namespaced CSS classes (`ocds-*`) to ensure our dashboards look good regardless of the user's base theme.
4.  **Data-Driven Layouts:** Dashboard layouts will be controlled by Frontmatter configuration, allowing for future extensibility without code changes.
