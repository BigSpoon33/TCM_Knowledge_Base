import os

import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Constants
TEMPLATE_DIR = "capsule/templates"
TEMPLATE_NAME = "master-dashboard.md.j2"


@pytest.fixture
def env():
    """Create Jinja2 environment for testing."""
    return Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=select_autoescape(["html", "xml", "md"]))


@pytest.fixture
def mock_now():
    """Mock now() function for template context."""

    def _now():
        return "2025-11-22T12:00:00Z"

    return _now


def test_master_dashboard_template_exists():
    """Verify the template file exists."""
    assert os.path.exists(os.path.join(TEMPLATE_DIR, TEMPLATE_NAME))


def test_master_dashboard_renders_successfully(env, mock_now):
    """Verify the template renders without errors."""
    template = env.get_template(TEMPLATE_NAME)
    # The master dashboard template doesn't strictly require variables,
    # but it uses now() which we provide in the context or as a global
    # In the actual app, now() might be a global or passed in context.
    # Let's pass it in context for this test.
    output = template.render(now=mock_now)
    assert output is not None
    assert len(output) > 0


def test_master_dashboard_frontmatter(env, mock_now):
    """Verify frontmatter contains required fields."""
    template = env.get_template(TEMPLATE_NAME)
    output = template.render(now=mock_now)

    assert "type: master_dashboard" in output
    assert 'title: "My Knowledge System"' in output
    assert 'created: "2025-11-22T12:00:00Z"' in output
    assert 'updated: "2025-11-22T12:00:00Z"' in output


def test_master_dashboard_sections_present(env, mock_now):
    """Verify all required dashboard sections are present."""
    template = env.get_template(TEMPLATE_NAME)
    output = template.render(now=mock_now)

    expected_sections = [
        "# Master Dashboard - My Knowledge System",
        "## 📚 Installed Capsules",
        "## 📊 Progress Overview",
        "## 🔍 Advanced Capsule Filters",
        "## 🗓️ Active Timelines (Sequenced Capsules)",
        "## 🔗 Cross-Capsule Connections",
        "## 📈 This Week's Activity",
        "## 🎯 Capsule Links",
    ]

    for section in expected_sections:
        assert section in output, f"Missing section: {section}"


def test_master_dashboard_queries_present(env, mock_now):
    """Verify Dataview and DataviewJS queries are present."""
    template = env.get_template(TEMPLATE_NAME)
    output = template.render(now=mock_now)

    # Check for Dataview blocks
    assert output.count("```dataview") == 7

    # Check for DataviewJS blocks
    assert output.count("```dataviewjs") == 2

    # Check specific query logic parts
    assert 'WHERE type = "capsule_dashboard"' in output
    assert "const renderTable = () => {" in output
    assert "dv.table(" in output


def test_dataviewjs_filtering_logic(env, mock_now):
    """Verify the DataviewJS logic for filtering active capsules is correct."""
    template = env.get_template(TEMPLATE_NAME)
    output = template.render(now=mock_now)

    # Check for the core dv.pages() call and initial filtering
    assert 'let pages = dv.pages(\'""\').where(p => p.type === "capsule_dashboard");' in output

    # Check for the filtering logic
    assert "if (classFilter.value)" in output
    assert "if (topicFilter.value)" in output
    assert "if (categoryFilter.value)" in output
    assert "if (activeFilter.value)" in output

    # Check that the table is rendered with the correct data
    assert "dv.table(" in output
    assert '["Capsule", "ID", "Class", "Topic", "Category", "Active"],' in output
