"""
Dataview Query Pattern Library.

This module provides a library of standard Dataview and DataviewJS query patterns
for use in dashboard templates and generated content. It ensures consistency
and performance across all dashboards.
"""

from typing import Dict, Any, Optional


def build_file_list_query(source_capsule: str, file_type: str) -> str:
    """
    Build a Dataview query to list files of a specific type from a capsule.

    Args:
        source_capsule: The ID of the source capsule.
        file_type: The type of file to list (e.g., 'root_note', 'flashcard').

    Returns:
        A formatted Dataview query string.

    Example:
        >>> print(build_file_list_query("TCM_Herbs_v1", "root_note"))
        ```dataview
        TABLE type, tags, updated
        FROM ""
        WHERE contains(source_capsules, "TCM_Herbs_v1")
          AND type = "root_note"
        SORT name ASC
        ```
    """
    return f"""```dataview
TABLE type, tags, updated
FROM ""
WHERE contains(source_capsules, "{source_capsule}")
  AND type = "{file_type}"
SORT name ASC
```"""


def build_metadata_filter_query(filters: Dict[str, Any]) -> str:
    """
    Build a Dataview query to filter capsule dashboards by metadata.

    Args:
        filters: A dictionary of metadata filters (e.g., {'class': 'TCM101'}).

    Returns:
        A formatted Dataview query string.

    Example:
        >>> filters = {"class": "TCM101", "active": True}
        >>> print(build_metadata_filter_query(filters))
        ```dataview
        TABLE capsule_id, version, dashboard_metadata.topic
        FROM ""
        WHERE type = "capsule_dashboard"
          AND dashboard_metadata.class = "TCM101"
          AND dashboard_metadata.active = true
        SORT file.name ASC
        ```
    """
    query_lines = [
        "```dataview",
        "TABLE capsule_id, version, dashboard_metadata.topic",
        'FROM ""',
        'WHERE type = "capsule_dashboard"',
    ]

    for key, value in filters.items():
        if isinstance(value, bool):
            val_str = str(value).lower()
            query_lines.append(f"  AND dashboard_metadata.{key} = {val_str}")
        else:
            query_lines.append(f'  AND dashboard_metadata.{key} = "{value}"')

    query_lines.append("SORT file.name ASC")
    query_lines.append("```")

    return "\n".join(query_lines)


def build_heading_extraction_query(tag: str, heading: str) -> str:
    """
    Build a DataviewJS query to extract content under a specific heading from notes with a tag.

    Args:
        tag: The tag to filter notes by (e.g., '#formula').
        heading: The heading to extract content from (e.g., 'Ingredients').

    Returns:
        A formatted DataviewJS query string.

    Performance:
        This query involves reading file contents (I/O intensive).
        - < 50 notes: Fast (< 1s)
        - 50-100 notes: Moderate (1-3s)
        - > 100 notes: Slow (may exceed 5s)
        A warning is automatically added to the query if the note count exceeds 50.

    Example:
        >>> print(build_heading_extraction_query("#formula", "Ingredients"))
        ```dataviewjs
        // ... JS code ...
        ```
    """
    return f"""```dataviewjs
function extractHeading(content, heading) {{
    // Escape special regex characters in heading
    const escapedHeading = heading.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&');
    const regex = new RegExp(`^#+\\s+${{escapedHeading}}\\s*\\n([\\s\\S]*?)(?=\\n#+|$)`, 'm');
    const match = content.match(regex);
    return match ? match[1].trim() : null;
}}

const notes = dv.pages('{tag}');

// Performance warning for large datasets
if (notes.length > 50) {{
    dv.paragraph("⚠️ **Performance Warning**: Processing " + notes.length + " notes. This extraction requires reading file contents and may be slow.");
}}

const results = [];

for (let note of notes) {{
  const content = await dv.io.load(note.file.path);
  const headingContent = extractHeading(content, "{heading}");
  if (headingContent) {{
    results.push({{
      name: note.file.name,
      content: headingContent
    }});
  }}
}}

dv.table(["Note", "{heading}"], 
  results.map(r => [r.name, r.content]));
```"""
