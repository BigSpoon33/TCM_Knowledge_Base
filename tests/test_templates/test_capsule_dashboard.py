import os
import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Constants
TEMPLATE_DIR = "capsule/templates"
TEMPLATE_NAME = "capsule-dashboard.md.j2"


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


@pytest.fixture
def sample_capsule():
    """Sample capsule data for testing."""
    return {
        "capsule_id": "TCM_Herbs_v1",
        "id": "TCM_Herbs_v1",
        "name": "TCM Materia Medica - Herbs",
        "version": "1.0.0",
        "domain_type": "traditional_chinese_medicine",
        "sequence_mode": "freeform",
        "created": "2025-11-22T10:00:00Z",
        "updated": "2025-11-22T10:00:00Z",
        "dashboard_metadata": {"class": "TCM101", "topic": "Herbal Medicine", "category": "CALE", "active": True},
    }


def test_capsule_dashboard_template_exists():
    """Verify the template file exists."""
    assert os.path.exists(os.path.join(TEMPLATE_DIR, TEMPLATE_NAME))


def test_capsule_dashboard_renders_successfully(env, mock_now, sample_capsule):
    """Verify the template renders without errors."""
    template = env.get_template(TEMPLATE_NAME)
    output = template.render(capsule=sample_capsule, now=mock_now, domain_sections="")
    assert output is not None
    assert len(output) > 0


def test_capsule_dashboard_frontmatter(env, mock_now, sample_capsule):
    """Verify frontmatter contains required fields."""
    template = env.get_template(TEMPLATE_NAME)
    output = template.render(capsule=sample_capsule, now=mock_now, domain_sections="")

    assert "type: capsule_dashboard" in output
    assert 'capsule_id: "TCM_Herbs_v1"' in output
    assert 'version: "1.0.0"' in output
    assert 'class: "TCM101"' in output
    assert 'topic: "Herbal Medicine"' in output
    assert 'category: "CALE"' in output
    assert "active: true" in output
    assert 'source_capsules: ["TCM_Herbs_v1"]' in output


def test_capsule_dashboard_sections_present(env, mock_now, sample_capsule):
    """Verify all required dashboard sections are present."""
    template = env.get_template(TEMPLATE_NAME)
    output = template.render(capsule=sample_capsule, now=mock_now, domain_sections="")

    expected_sections = [
        f'<h1 class="ocds-header__title">{sample_capsule["name"]}</h1>',
        '<h3 class="ocds-card__title">Overview</h3>',
        "<h2>📚 Root Notes</h2>",
        "<h2>📝 Study Materials</h2>",
        '<h3 class="ocds-card__title">Flashcards</h3>',
        '<h3 class="ocds-card__title">Quizzes</h3>',
        "<h2>Recent Activity</h2>",
    ]

    for section in expected_sections:
        assert section in output, f"Missing section: {section}"


def test_capsule_dashboard_queries_present(env, mock_now, sample_capsule):
    """Verify Dataview queries are present."""
    template = env.get_template(TEMPLATE_NAME)
    output = template.render(capsule=sample_capsule, now=mock_now, domain_sections="")

    # Check for Dataview blocks
    assert output.count("```dataview") >= 3

    # Check specific query logic parts
    assert 'WHERE contains(source_capsules, "TCM_Herbs_v1")' in output
    assert 'type != "dashboard"' in output
    assert 'type = "flashcard"' in output
    assert 'type = "quiz"' in output


def test_sequence_mode_conditional_rendering(env, mock_now, sample_capsule):
    """Verify Progress Tracking section renders only for sequenced capsules."""
    template = env.get_template(TEMPLATE_NAME)

    # Test freeform (default sample)
    output_freeform = template.render(capsule=sample_capsule, now=mock_now, domain_sections="")
    assert "<h2>📊 Progress Tracking</h2>" not in output_freeform

    # Test sequenced
    sample_capsule["sequence_mode"] = "sequenced"
    output_sequenced = template.render(capsule=sample_capsule, now=mock_now, domain_sections="")
    assert "<h2>📊 Progress Tracking</h2>" in output_sequenced
    assert "<h3>Active Timeline</h3>" in output_sequenced
    assert "```dataviewjs" in output_sequenced
    assert "const percentage = Math.round((completedTasks / totalTasks) * 100);" in output_sequenced


def test_domain_sections_rendering(env, mock_now, sample_capsule):
    """Verify domain sections are rendered."""
    template = env.get_template(TEMPLATE_NAME)
    domain_content = "### Formulas\nSome content"
    output = template.render(capsule=sample_capsule, now=mock_now, domain_sections=domain_content)

    assert domain_content in output
