import pytest
from capsule.utils.dataview_queries import (
    build_file_list_query,
    build_metadata_filter_query,
    build_heading_extraction_query,
)


def test_build_file_list_query():
    """Test building a file list query."""
    query = build_file_list_query("TCM_Herbs_v1", "root_note")

    assert "```dataview" in query
    assert 'WHERE contains(source_capsules, "TCM_Herbs_v1")' in query
    assert 'AND type = "root_note"' in query
    assert "SORT name ASC" in query


def test_build_metadata_filter_query():
    """Test building a metadata filter query."""
    filters = {"class": "TCM101", "active": True, "category": "CALE"}
    query = build_metadata_filter_query(filters)

    assert "```dataview" in query
    assert 'WHERE type = "capsule_dashboard"' in query
    assert 'AND dashboard_metadata.class = "TCM101"' in query
    assert "AND dashboard_metadata.active = true" in query
    assert 'AND dashboard_metadata.category = "CALE"' in query


def test_build_heading_extraction_query():
    """Test building a heading extraction query."""
    query = build_heading_extraction_query("#formula", "Ingredients")

    assert "```dataviewjs" in query
    assert "function extractHeading" in query
    assert "dv.pages('#formula')" in query
    assert 'extractHeading(content, "Ingredients")' in query
    assert 'dv.table(["Note", "Ingredients"]' in query

    # Check for new robustness and performance features
    assert "escapedHeading =" in query
    assert "Performance Warning" in query
    assert "notes.length > 50" in query


def test_build_heading_extraction_query_special_chars():
    """Test building a query with special characters in the heading."""
    query = build_heading_extraction_query("#formula", "Ingredients (Active)")
    assert 'extractHeading(content, "Ingredients (Active)")' in query
