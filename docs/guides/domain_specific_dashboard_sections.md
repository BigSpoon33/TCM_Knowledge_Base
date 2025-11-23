# Adding Domain-Specific Dashboard Sections

This guide explains how to add custom dashboard sections for specific domains (e.g., TCM, Coding, Cooking) in the Obsidian Capsule Delivery System.

## Overview

When a capsule is imported, the system generates a `capsule-dashboard.md` file. This dashboard can include domain-specific sections that are dynamically loaded based on the capsule's `domain_type`.

## How It Works

1.  The `Importer` checks the capsule's `domain_type`.
2.  It looks for a matching template in `capsule/templates/domains/`.
3.  If found, it renders the template and injects it into the `{{ domain_sections }}` placeholder in the main dashboard.

## Steps to Add a New Domain Section

### 1. Create a Domain Template

Create a new Jinja2 template file in `capsule/templates/domains/`. The filename should match your domain type (lowercase) with `.md.j2` extension.

**Example:** For `domain_type: "coding"`, create `capsule/templates/domains/coding.md.j2`.

### 2. Add Content and Queries

Add Markdown content and Dataview queries to your template. You can use the `dv` object (which exposes `capsule.utils.dataview_queries`) and `capsule_id` variable.

**Example `coding.md.j2`:**

```jinja2
## Coding Resources

### Snippets
{{ dv.build_file_list_query(capsule_id, 'snippet') }}

### Algorithms
{{ dv.build_file_list_query(capsule_id, 'algorithm') }}
```

### 3. Verify Domain Type

Ensure your capsule's `capsule-cypher.yaml` uses the correct `domain_type`.

```yaml
capsule_id: "Python_Basics_v1"
domain_type: "coding"
...
```

## Available Utilities

The `dv` object provides helper functions to generate standard Dataview queries:

-   `dv.build_file_list_query(source_capsule, file_type)`: Lists files of a specific type.
-   `dv.build_metadata_filter_query(filters)`: Filters dashboards (mostly for master dashboard).
-   `dv.build_heading_extraction_query(tag, heading)`: Extracts content under headings (DataviewJS).

## Testing

1.  Create a test capsule with your new domain type.
2.  Run `capsule import <path-to-capsule>`.
3.  Check the generated `capsule-dashboard.md` to verify your sections appear.
