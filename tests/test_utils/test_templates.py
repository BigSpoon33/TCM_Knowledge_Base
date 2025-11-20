import pytest
from jinja2 import Environment, TemplateNotFound
from pathlib import Path
from capsule.utils.templates import create_jinja_environment, load_template


@pytest.fixture
def temp_template_dir(tmp_path):
    """Creates a temporary directory with a sample template."""
    temp_dir = tmp_path / "templates"
    temp_dir.mkdir()
    (temp_dir / "test.j2").write_text("Hello, {{ name }}!")
    return temp_dir


def test_create_jinja_environment(temp_template_dir):
    """Tests that the Jinja2 environment is created correctly."""
    env = create_jinja_environment(template_dir=temp_template_dir)
    assert isinstance(env, Environment)
    assert str(env.loader.searchpath[0]) == str(temp_template_dir)


def test_load_template_successfully(temp_template_dir):
    """Tests that a template can be loaded successfully."""
    template = load_template("test.j2", template_dir=temp_template_dir)
    assert template.render(name="World") == "Hello, World!"


def test_load_flashcard_template_successfully():
    """Tests that the flashcard.md.j2 template can be loaded."""
    template = load_template("flashcard.md.j2")
    assert template is not None


def test_render_flashcard_template():
    """Tests that the flashcard.md.j2 template renders correctly."""
    template = load_template("flashcard.md.j2")
    sample_data = {"question": "What is the capital of France?", "answer": "Paris"}
    rendered_output = template.render(sample_data)
    assert 'question: "What is the capital of France?"' in rendered_output
    assert 'answer: "Paris"' in rendered_output
    assert "# What is the capital of France?" in rendered_output
    assert "\nParis" in rendered_output


def test_load_quiz_template_successfully():
    """Tests that the quiz.md.j2 template can be loaded."""
    template = load_template("quiz.md.j2")
    assert template is not None


def test_render_quiz_template():
    """Tests that the quiz.md.j2 template renders correctly."""
    template = load_template("quiz.md.j2")
    sample_data = {
        "title": "French Capitals",
        "questions": [{"text": "What is the capital of France?", "options": ["London", "Paris", "Berlin"]}],
    }
    rendered_output = template.render(sample_data)
    assert 'title: "French Capitals"' in rendered_output
    assert 'text: "What is the capital of France?"' in rendered_output
    assert '- "London"' in rendered_output
    assert '- "Paris"' in rendered_output
    assert '- "Berlin"' in rendered_output
    assert "## What is the capital of France?" in rendered_output
    assert "- [ ] London" in rendered_output
    assert "- [ ] Paris" in rendered_output
    assert "- [ ] Berlin" in rendered_output
