# Obsidian CSS Theming Guide for OCDS Dashboards

## Document Information
**Epic:** Epic 12 - Dashboard Polish & Interactivity  
**Created:** 2025-11-22  
**Purpose:** Comprehensive guide for implementing custom CSS theming in OCDS dashboards

---

## Table of Contents
1. [Overview](#overview)
2. [CSS Snippets Basics](#css-snippets-basics)
3. [Obsidian-Specific Selectors](#obsidian-specific-selectors)
4. [Dashboard Component Styling](#dashboard-component-styling)
5. [Dataview Table Styling](#dataview-table-styling)
6. [Callout Customization](#callout-customization)
7. [Theme Compatibility](#theme-compatibility)
8. [Best Practices](#best-practices)
9. [Code Examples](#code-examples)
10. [Resources](#resources)

---

## Overview

### What Are CSS Snippets?

CSS snippets in Obsidian are custom stylesheets that override or extend the base theme. They allow you to:

- Customize appearance without changing the core theme
- Create reusable style patterns
- Target specific elements (e.g., dashboards, tables, callouts)
- Maintain consistency across vaults

### How CSS Snippets Work

1. **Location:** `.obsidian/snippets/` directory
2. **File Format:** `.css` files
3. **Activation:** Settings → Appearance → CSS snippets → Enable individual snippets
4. **Hot Reload:** Changes are applied immediately when file is saved

### Current Vault Setup

```
.obsidian/
├── snippets/
│   └── noyaml.css          # Hides frontmatter in reading mode
├── themes/
│   └── Minimal/            # Active theme
│       └── theme.css
└── appearance.json         # Theme configuration
```

**Active Theme:** Minimal by @kepano  
**Enabled Snippets:** `noyaml`

---

## CSS Snippets Basics

### Creating a CSS Snippet

1. **Create file** in `.obsidian/snippets/` directory:
   ```bash
   touch .obsidian/snippets/dashboard-polish.css
   ```

2. **Add CSS rules** to the file

3. **Enable snippet** in Obsidian:
   - Settings → Appearance → CSS snippets
   - Toggle on `dashboard-polish`

### Basic CSS Snippet Structure

```css
/* ================================
   Dashboard Polish Snippet
   Purpose: Custom styling for OCDS dashboards
   ================================ */

/* Target specific dashboard type */
.markdown-preview-view[data-note-type="capsule_dashboard"] {
    /* Your styles here */
}

/* Target all dashboards */
.dashboard-container {
    padding: 1rem;
    background: var(--background-secondary);
}
```

---

## Obsidian-Specific Selectors

### Core Content Containers

```css
/* Main content area */
.markdown-preview-view {
    /* Reading/preview mode */
}

.markdown-source-view {
    /* Edit/source mode */
}

/* Live preview mode (CM6) */
.markdown-source-view.mod-cm6.is-live-preview {
    /* Live preview specific styles */
}
```

### Metadata & Frontmatter

```css
/* Frontmatter container */
.metadata-container {
    background: var(--background-secondary);
    border-radius: 4px;
    padding: 0.5rem;
}

/* Hide frontmatter (like noyaml.css) */
.markdown-preview-view.hide-frontmatter .metadata-container {
    display: none;
}

/* Individual property */
.metadata-property {
    margin-bottom: 0.5rem;
}
```

### Headings

```css
/* All headings */
.markdown-preview-view h1,
.markdown-preview-view h2,
.markdown-preview-view h3 {
    color: var(--text-accent);
    border-bottom: 1px solid var(--background-modifier-border);
    padding-bottom: 0.3rem;
}

/* Specific heading levels */
.markdown-preview-view h1 {
    font-size: var(--h1-size);
    font-weight: var(--h1-weight);
}

/* Heading with icon */
.markdown-preview-view h2::before {
    content: "📊 ";
    margin-right: 0.5rem;
}
```

### Links & Navigation

```css
/* Internal links (wikilinks) */
.internal-link {
    color: var(--text-accent);
    text-decoration: none;
}

.internal-link:hover {
    color: var(--text-accent-hover);
    text-decoration: underline;
}

/* Unresolved links */
.internal-link.is-unresolved {
    color: var(--text-muted);
    opacity: 0.6;
}
```

---

## Dashboard Component Styling

### Progress Trackers

```css
/* Progress bar container */
.progress-tracker {
    width: 100%;
    background: var(--background-modifier-border);
    border-radius: 8px;
    overflow: hidden;
    margin: 1rem 0;
}

/* Progress bar fill */
.progress-fill {
    height: 20px;
    background: linear-gradient(90deg, 
        var(--color-green) 0%, 
        var(--color-cyan) 100%);
    transition: width 0.3s ease;
}

/* Progress percentage text */
.progress-text {
    font-size: var(--font-adaptive-small);
    color: var(--text-muted);
    margin-top: 0.25rem;
}
```

### Statistics Displays

```css
/* Stat card grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

/* Individual stat card */
.stat-card {
    background: var(--background-secondary);
    border: 1px solid var(--background-modifier-border);
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stat-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px var(--shadow-color);
}

/* Stat value (large number) */
.stat-value {
    font-size: 2rem;
    font-weight: 600;
    color: var(--text-accent);
    line-height: 1;
}

/* Stat label */
.stat-label {
    font-size: var(--font-adaptive-small);
    color: var(--text-muted);
    margin-top: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
```

### Content Cards

```css
/* Card container */
.content-card {
    background: var(--background-primary);
    border: 1px solid var(--background-modifier-border);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 4px var(--shadow-color);
}

/* Card header */
.card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 2px solid var(--background-modifier-border);
}

.card-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--text-normal);
}

.card-icon {
    font-size: 1.5rem;
}

/* Card body */
.card-body {
    color: var(--text-normal);
    line-height: 1.6;
}

/* Card footer */
.card-footer {
    margin-top: 1rem;
    padding-top: 0.75rem;
    border-top: 1px solid var(--background-modifier-border);
    font-size: var(--font-adaptive-small);
    color: var(--text-muted);
}
```

### Navigation Elements

```css
/* Tab-style navigation */
.nav-tabs {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
    border-bottom: 2px solid var(--background-modifier-border);
}

.nav-tab {
    padding: 0.5rem 1rem;
    background: transparent;
    border: none;
    border-bottom: 2px solid transparent;
    color: var(--text-muted);
    cursor: pointer;
    transition: all 0.2s ease;
}

.nav-tab:hover {
    color: var(--text-normal);
}

.nav-tab.active {
    color: var(--text-accent);
    border-bottom-color: var(--text-accent);
}

/* Breadcrumb navigation */
.breadcrumb {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 1rem;
    font-size: var(--font-adaptive-small);
    color: var(--text-muted);
}

.breadcrumb-item::after {
    content: " / ";
    margin-left: 0.5rem;
    color: var(--text-faint);
}

.breadcrumb-item:last-child::after {
    content: "";
}
```

---

## Dataview Table Styling

### Basic Table Improvements

```css
/* Dataview table container */
.block-language-dataview {
    margin: 1.5rem 0;
}

/* Table styling */
.dataview.table-view-table {
    width: 100%;
    border-collapse: collapse;
    border-spacing: 0;
}

/* Table headers */
.dataview.table-view-table thead {
    background: var(--background-secondary);
    border-bottom: 2px solid var(--background-modifier-border);
}

.dataview.table-view-table th {
    padding: 0.75rem 1rem;
    text-align: left;
    font-weight: 600;
    font-size: var(--font-adaptive-small);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--text-muted);
}

/* Table rows */
.dataview.table-view-table tbody tr {
    border-bottom: 1px solid var(--background-modifier-border);
    transition: background-color 0.15s ease;
}

.dataview.table-view-table tbody tr:hover {
    background: var(--background-modifier-hover);
}

/* Table cells */
.dataview.table-view-table td {
    padding: 0.75rem 1rem;
    color: var(--text-normal);
}

/* Alternating row colors */
.dataview.table-view-table tbody tr:nth-child(even) {
    background: var(--background-secondary-alt);
}
```

### Advanced Table Features

```css
/* Sortable column headers */
.dataview.table-view-table th.sortable {
    cursor: pointer;
    user-select: none;
}

.dataview.table-view-table th.sortable::after {
    content: " ↕";
    opacity: 0.3;
}

.dataview.table-view-table th.sortable:hover::after {
    opacity: 1;
}

/* Compact table variant */
.dataview.table-view-table.compact td,
.dataview.table-view-table.compact th {
    padding: 0.4rem 0.75rem;
    font-size: var(--font-adaptive-smaller);
}

/* Striped table variant */
.dataview.table-view-table.striped tbody tr:nth-child(odd) {
    background: var(--background-primary);
}

.dataview.table-view-table.striped tbody tr:nth-child(even) {
    background: var(--background-secondary);
}

/* Bordered table variant */
.dataview.table-view-table.bordered {
    border: 1px solid var(--background-modifier-border);
}

.dataview.table-view-table.bordered td,
.dataview.table-view-table.bordered th {
    border: 1px solid var(--background-modifier-border);
}

/* Highlight first column */
.dataview.table-view-table td:first-child {
    font-weight: 500;
    color: var(--text-accent);
}
```

### Dataview List Styling

```css
/* Dataview list container */
.dataview.list-view-ul {
    list-style: none;
    padding-left: 0;
}

.dataview.list-view-ul li {
    padding: 0.5rem 0;
    border-bottom: 1px solid var(--background-modifier-border);
}

.dataview.list-view-ul li:last-child {
    border-bottom: none;
}

/* Dataview task list */
.dataview.task-list-basic {
    list-style: none;
    padding-left: 1rem;
}

.dataview.task-list-item {
    padding: 0.25rem 0;
}

.dataview.task-list-item input[type="checkbox"] {
    margin-right: 0.5rem;
}
```

---

## Callout Customization

### Default Callout Styling

```css
/* All callouts */
.callout {
    border-radius: 8px;
    margin: 1rem 0;
    padding: 1rem;
    border-left: 4px solid var(--callout-color);
    background: var(--callout-background);
}

/* Callout title */
.callout-title {
    font-weight: 600;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.callout-title-inner {
    color: var(--callout-color);
}

/* Callout icon */
.callout-icon {
    flex-shrink: 0;
}

/* Callout content */
.callout-content {
    color: var(--text-normal);
}
```

### Custom Callout Types

```css
/* Info callout */
.callout[data-callout="info"] {
    --callout-color: var(--color-blue);
    --callout-background: hsla(var(--color-blue), 0.1);
}

/* Success callout */
.callout[data-callout="success"] {
    --callout-color: var(--color-green);
    --callout-background: hsla(var(--color-green), 0.1);
}

/* Warning callout */
.callout[data-callout="warning"] {
    --callout-color: var(--color-orange);
    --callout-background: hsla(var(--color-orange), 0.1);
}

/* Error callout */
.callout[data-callout="error"] {
    --callout-color: var(--color-red);
    --callout-background: hsla(var(--color-red), 0.1);
}

/* Dashboard-specific callout */
.callout[data-callout="dashboard"] {
    --callout-color: var(--color-purple);
    --callout-background: var(--background-secondary);
    border: 2px solid var(--color-purple);
    border-left: 4px solid var(--color-purple);
}

/* Stats callout (for displaying metrics) */
.callout[data-callout="stats"] {
    --callout-color: var(--color-cyan);
    --callout-background: var(--background-primary);
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 1rem;
}
```

### Collapsible Callouts

```css
/* Collapsible callout header */
.callout.is-collapsible .callout-title {
    cursor: pointer;
    user-select: none;
}

.callout.is-collapsible .callout-title::after {
    content: " ▼";
    margin-left: auto;
    transition: transform 0.2s ease;
}

.callout.is-collapsible.is-collapsed .callout-title::after {
    transform: rotate(-90deg);
}

/* Collapsed content */
.callout.is-collapsed .callout-content {
    display: none;
}
```

---

## Theme Compatibility

### Using CSS Variables

Obsidian themes define CSS variables that adapt to light/dark mode. Always use these instead of hard-coded colors:

```css
/* ✅ GOOD: Uses theme variables */
.dashboard-header {
    background: var(--background-secondary);
    color: var(--text-normal);
    border: 1px solid var(--background-modifier-border);
}

/* ❌ BAD: Hard-coded colors break in dark mode */
.dashboard-header {
    background: #ffffff;
    color: #000000;
    border: 1px solid #cccccc;
}
```

### Common Obsidian CSS Variables

#### Background Colors
```css
--background-primary          /* Main background */
--background-primary-alt       /* Alternative primary */
--background-secondary         /* Sidebar background */
--background-secondary-alt     /* Alternative secondary */
--background-modifier-border   /* Border color */
--background-modifier-hover    /* Hover state */
```

#### Text Colors
```css
--text-normal                  /* Primary text */
--text-muted                   /* Secondary text */
--text-faint                   /* Tertiary text */
--text-accent                  /* Accent/link color */
--text-accent-hover           /* Hovered accent */
--text-error                  /* Error text */
```

#### Interactive Elements
```css
--interactive-normal          /* Button background */
--interactive-hover           /* Button hover */
--interactive-accent          /* Primary button */
--interactive-accent-hover    /* Primary button hover */
```

#### Extended Palette (Minimal Theme)
```css
--color-red                   /* #d04255 */
--color-orange               /* #d5763f */
--color-yellow               /* #e5b567 */
--color-green                /* #a8c373 */
--color-cyan                 /* #73bbb2 */
--color-blue                 /* #6c99bb */
--color-purple               /* #9e86c8 */
--color-pink                 /* #b05279 */
```

### Light/Dark Mode Targeting

```css
/* Light mode only */
.theme-light .dashboard-card {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* Dark mode only */
.theme-dark .dashboard-card {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
}

/* Both modes using variables */
.dashboard-card {
    box-shadow: 0 2px 8px var(--shadow-color);
}
```

### Mobile Responsiveness

```css
/* Desktop only */
@media (min-width: 768px) {
    .stats-grid {
        grid-template-columns: repeat(4, 1fr);
    }
}

/* Tablet */
@media (max-width: 767px) {
    .stats-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Mobile */
.is-mobile .dashboard-container {
    padding: 0.5rem;
}

.is-mobile .stat-card {
    font-size: 0.9rem;
}
```

---

## Best Practices

### 1. Performance Considerations

```css
/* ✅ GOOD: Efficient selectors */
.dataview.table-view-table td {
    padding: 0.75rem;
}

/* ❌ BAD: Overly complex selectors */
.workspace-leaf-content .view-content .markdown-preview-view .dataview table tbody tr td {
    padding: 0.75rem;
}

/* ✅ GOOD: Use CSS transforms for animations */
.card:hover {
    transform: translateY(-2px);
    transition: transform 0.2s ease;
}

/* ❌ BAD: Animating layout properties */
.card:hover {
    margin-top: -2px;
    transition: margin 0.2s ease;
}
```

### 2. Maintainability

```css
/* ✅ GOOD: Organized with comments and sections */
/* ================================
   Dashboard Tables
   ================================ */

/* Table container */
.dashboard-table {
    margin: 1rem 0;
}

/* Table headers */
.dashboard-table th {
    font-weight: 600;
}

/* ❌ BAD: Disorganized, no comments */
.dashboard-table { margin: 1rem 0; }
.dashboard-table th { font-weight: 600; }
.card { padding: 1rem; }
.stat-value { font-size: 2rem; }
```

### 3. Specificity & Cascading

```css
/* Use appropriate specificity */

/* Low specificity (easy to override) */
.card {
    padding: 1rem;
}

/* Medium specificity */
.dashboard-container .card {
    padding: 1.5rem;
}

/* High specificity (use sparingly) */
.markdown-preview-view .dashboard-container .card.featured {
    padding: 2rem;
}
```

### 4. Avoid !important

```css
/* ✅ GOOD: Increase specificity instead */
.markdown-preview-view .dashboard-table {
    border-collapse: collapse;
}

/* ❌ BAD: Using !important as a quick fix */
.dashboard-table {
    border-collapse: collapse !important;
}
```

### 5. Custom Properties for Reusability

```css
/* Define custom properties */
:root {
    --dashboard-spacing: 1.5rem;
    --dashboard-border-radius: 12px;
    --dashboard-shadow: 0 2px 8px var(--shadow-color);
}

/* Use custom properties */
.card {
    padding: var(--dashboard-spacing);
    border-radius: var(--dashboard-border-radius);
    box-shadow: var(--dashboard-shadow);
}

.stats-grid {
    gap: var(--dashboard-spacing);
}
```

---

## Code Examples

### Example 1: Complete Dashboard Card System

```css
/* ================================
   OCDS Dashboard Cards
   Purpose: Modular card system for dashboards
   ================================ */

/* Card container */
.ocds-card {
    background: var(--background-primary);
    border: 1px solid var(--background-modifier-border);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    transition: all 0.2s ease;
}

.ocds-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px var(--shadow-color);
    border-color: var(--text-accent);
}

/* Card variants */
.ocds-card.info {
    border-left: 4px solid var(--color-blue);
}

.ocds-card.success {
    border-left: 4px solid var(--color-green);
}

.ocds-card.warning {
    border-left: 4px solid var(--color-orange);
}

.ocds-card.accent {
    border-left: 4px solid var(--text-accent);
}

/* Card header */
.ocds-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 2px solid var(--background-modifier-border);
}

.ocds-card-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--text-normal);
    margin: 0;
}

.ocds-card-icon {
    font-size: 1.5rem;
    opacity: 0.8;
}

/* Card body */
.ocds-card-body {
    color: var(--text-normal);
    line-height: 1.6;
}

/* Card footer */
.ocds-card-footer {
    margin-top: 1rem;
    padding-top: 0.75rem;
    border-top: 1px solid var(--background-modifier-border);
    font-size: var(--font-adaptive-small);
    color: var(--text-muted);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

### Example 2: Enhanced Dataview Tables

```css
/* ================================
   OCDS Dataview Tables
   Purpose: Professional table styling for dashboards
   ================================ */

/* Table container */
.ocds-table {
    width: 100%;
    margin: 1.5rem 0;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 4px var(--shadow-color);
}

/* Table headers */
.ocds-table thead {
    background: var(--background-secondary);
}

.ocds-table th {
    padding: 1rem;
    text-align: left;
    font-weight: 600;
    font-size: var(--font-adaptive-small);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--text-muted);
    border-bottom: 2px solid var(--background-modifier-border);
}

/* Table rows */
.ocds-table tbody tr {
    border-bottom: 1px solid var(--background-modifier-border);
    transition: background-color 0.15s ease;
}

.ocds-table tbody tr:hover {
    background: var(--background-modifier-hover);
}

.ocds-table tbody tr:last-child {
    border-bottom: none;
}

/* Table cells */
.ocds-table td {
    padding: 0.75rem 1rem;
    color: var(--text-normal);
}

/* Striped rows */
.ocds-table.striped tbody tr:nth-child(even) {
    background: var(--background-secondary-alt);
}

/* Compact variant */
.ocds-table.compact td,
.ocds-table.compact th {
    padding: 0.5rem 0.75rem;
    font-size: var(--font-adaptive-smaller);
}

/* Centered columns */
.ocds-table td.center,
.ocds-table th.center {
    text-align: center;
}

/* Right-aligned columns (for numbers) */
.ocds-table td.right,
.ocds-table th.right {
    text-align: right;
}

/* Status badges in tables */
.ocds-table .status-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 12px;
    font-size: 0.85rem;
    font-weight: 500;
}

.ocds-table .status-badge.active {
    background: var(--color-green);
    color: white;
}

.ocds-table .status-badge.inactive {
    background: var(--color-red);
    color: white;
}

.ocds-table .status-badge.pending {
    background: var(--color-orange);
    color: white;
}
```

### Example 3: Progress Indicators

```css
/* ================================
   OCDS Progress Indicators
   Purpose: Visual progress tracking for dashboards
   ================================ */

/* Progress bar container */
.ocds-progress {
    width: 100%;
    background: var(--background-modifier-border);
    border-radius: 8px;
    overflow: hidden;
    margin: 1rem 0;
    position: relative;
}

/* Progress bar fill */
.ocds-progress-bar {
    height: 24px;
    background: linear-gradient(90deg, 
        var(--color-cyan) 0%, 
        var(--color-blue) 100%);
    transition: width 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: var(--font-adaptive-smaller);
    font-weight: 600;
}

/* Progress variants */
.ocds-progress-bar.low {
    background: linear-gradient(90deg, 
        var(--color-red) 0%, 
        var(--color-orange) 100%);
}

.ocds-progress-bar.medium {
    background: linear-gradient(90deg, 
        var(--color-orange) 0%, 
        var(--color-yellow) 100%);
}

.ocds-progress-bar.high {
    background: linear-gradient(90deg, 
        var(--color-green) 0%, 
        var(--color-cyan) 100%);
}

/* Progress text outside bar */
.ocds-progress-text {
    font-size: var(--font-adaptive-small);
    color: var(--text-muted);
    margin-top: 0.25rem;
    display: flex;
    justify-content: space-between;
}

/* Circular progress indicator */
.ocds-progress-circle {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: conic-gradient(
        var(--color-cyan) 0deg,
        var(--color-cyan) calc(var(--progress) * 3.6deg),
        var(--background-modifier-border) calc(var(--progress) * 3.6deg)
    );
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}

.ocds-progress-circle::before {
    content: "";
    width: 60px;
    height: 60px;
    background: var(--background-primary);
    border-radius: 50%;
    position: absolute;
}

.ocds-progress-circle-value {
    position: relative;
    z-index: 1;
    font-weight: 600;
    font-size: 1.2rem;
}
```

### Example 4: Dashboard Grid Layout

```css
/* ================================
   OCDS Dashboard Grid
   Purpose: Responsive grid system for dashboard layouts
   ================================ */

/* Main dashboard container */
.ocds-dashboard {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

/* Dashboard header */
.ocds-dashboard-header {
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid var(--background-modifier-border);
}

.ocds-dashboard-title {
    font-size: 2rem;
    font-weight: 600;
    color: var(--text-normal);
    margin-bottom: 0.5rem;
}

.ocds-dashboard-subtitle {
    font-size: var(--font-adaptive-normal);
    color: var(--text-muted);
}

/* Grid layouts */
.ocds-grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
}

.ocds-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
}

.ocds-grid-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
}

/* Responsive grids */
@media (max-width: 1024px) {
    .ocds-grid-4 {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .ocds-grid-2,
    .ocds-grid-3,
    .ocds-grid-4 {
        grid-template-columns: 1fr;
    }
}

/* Auto-fit grid (responsive) */
.ocds-grid-auto {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
}

/* Sidebar layout */
.ocds-layout-sidebar {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 2rem;
}

@media (max-width: 1024px) {
    .ocds-layout-sidebar {
        grid-template-columns: 1fr;
    }
}
```

---

## Resources

### Official Documentation
- [Obsidian Help - CSS Snippets](https://help.obsidian.md/Extending+Obsidian/CSS+snippets)
- [Obsidian Developer Docs](https://docs.obsidian.md/)
- [Minimal Theme Documentation](https://minimal.guide/)

### Community Themes & Snippets
- [Minimal Theme by @kepano](https://github.com/kepano/obsidian-minimal) - Clean, highly customizable theme
- [ITS Theme by SlRvb](https://github.com/SlRvb/Obsidian--ITS-Theme) - Feature-rich with extensive snippets
- [Obsidian CSS Snippets Collection](https://github.com/Dmytro-Shulha/obsidian-css-snippets)

### CSS Frameworks & Patterns
- Dashboard layout patterns from existing vault examples
- Dataview plugin CSS classes and structure
- Meta-Bind plugin form styling
- Advanced Slides plugin theming

### Obsidian Forums
- [CSS Hacks Meta Post](https://forum.obsidian.md/t/meta-post-common-css-hacks/1978)
- [Creating Fancy Horizontal Rules](https://forum.obsidian.md/t/creating-fancy-horizontal-rule-lines/63700/2)

### Inspiration Repositories
- [HOCA-1/neon-homepage-vault](https://github.com/HOCA-1/neon-homepage-vault) - Neon-themed dashboard
- [rafaelveiga/obsidian-widgets](https://github.com/rafaelveiga/obsidian-widgets) - Interactive widgets
- [TfTHacker/DashboardPlusPlus](https://github.com/TfTHacker/DashboardPlusPlus) - Advanced dashboard system

---

## Next Steps for Epic 12

### Recommended CSS Snippets to Create

1. **`ocds-dashboard-core.css`**
   - Core dashboard styling
   - Grid layouts
   - Card systems
   - Typography

2. **`ocds-dataview-tables.css`**
   - Enhanced table styling
   - Sortable columns
   - Striped/bordered variants
   - Responsive tables

3. **`ocds-progress-indicators.css`**
   - Progress bars
   - Circular indicators
   - Stats displays
   - Badges and labels

4. **`ocds-navigation.css`**
   - Breadcrumbs
   - Tab navigation
   - Sidebar menus
   - Quick actions

5. **`ocds-callouts.css`**
   - Custom callout types
   - Dashboard-specific callouts
   - Collapsible sections

6. **`ocds-mobile.css`**
   - Mobile-specific overrides
   - Touch-friendly interfaces
   - Responsive adjustments

### Testing Checklist

- [ ] Test in light mode
- [ ] Test in dark mode
- [ ] Test on desktop
- [ ] Test on mobile
- [ ] Test with different base themes
- [ ] Verify performance (no layout shifts)
- [ ] Check accessibility (contrast ratios)

---

## Conclusion

This guide provides the foundation for implementing polished, professional CSS theming in OCDS dashboards. By following these patterns and best practices, you can create:

- Consistent visual design across all dashboards
- Theme-compatible styles that work in light/dark mode
- Responsive layouts for desktop and mobile
- Performant CSS with minimal overhead
- Maintainable code that's easy to extend

For Epic 12 implementation, start with the core dashboard styles and progressively enhance with advanced features like animations, interactive widgets, and plugin integrations.
