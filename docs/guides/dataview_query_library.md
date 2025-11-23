# Dataview Query Pattern Library

This guide documents the standard Dataview and DataviewJS query patterns provided by the `capsule.utils.dataview_queries` module.

## File List Query

Generates a standard table of files belonging to a capsule, filtered by type.

**Function:** `build_file_list_query(source_capsule, file_type)`

**Usage:**
```python
from capsule.utils.dataview_queries import build_file_list_query
query = build_file_list_query("TCM_Herbs_v1", "root_note")
```

**Output:**
```dataview
TABLE type, tags, updated
FROM ""
WHERE contains(source_capsules, "TCM_Herbs_v1")
  AND type = "root_note"
SORT name ASC
```

## Metadata Filter Query

Generates a query to filter capsule dashboards based on metadata fields.

**Function:** `build_metadata_filter_query(filters)`

**Usage:**
```python
from capsule.utils.dataview_queries import build_metadata_filter_query
filters = {"class": "TCM101", "active": True}
query = build_metadata_filter_query(filters)
```

**Output:**
```dataview
TABLE capsule_id, version, dashboard_metadata.topic
FROM ""
WHERE type = "capsule_dashboard"
  AND dashboard_metadata.class = "TCM101"
  AND dashboard_metadata.active = true
SORT file.name ASC
```

## Heading Extraction Query

Generates a DataviewJS query to extract content under a specific heading from notes with a given tag.

**Function:** `build_heading_extraction_query(tag, heading)`

**Usage:**
```python
from capsule.utils.dataview_queries import build_heading_extraction_query
query = build_heading_extraction_query("#formula", "Ingredients")
```

**Output:**
```dataviewjs
// ... JS code to extract headings ...
```

## Performance Notes

- **File List Query:** Fast (<1s). Uses indexed metadata.
- **Metadata Filter Query:** Fast (<1s). Uses indexed metadata.
- **Heading Extraction Query:** Slower. Requires reading file contents.
    - **< 50 notes:** Fast (< 1s)
    - **50-100 notes:** Moderate (1-3s)
    - **> 100 notes:** Slow (may exceed 5s). A warning is displayed.
    - **Recommendation:** Use specific tags to limit the scope of extraction.
