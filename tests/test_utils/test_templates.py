import pytest
from jinja2 import Environment, TemplateNotFound
from pathlib import Path
from capsule.utils.templates import create_jinja_environment, load_template

@pytest.fixture
def mock_template_dir(monkeypatch, tmp_path):
    """Mocks the TEMPLATE_DIR constant to use a temporary directory."""
    temp_template_path = tmp_path / "templates"
    temp_template_path.mkdir()
    (temp_template_path / "test.j2").write_text("Hello, {{ name }}!")
    
    monkeypatch.setattr("capsule.utils.templates.TEMPLATE_DIR", temp_template_path)
    return temp_template_path

def test_create_jinja_environment(mock_template_dir):
    """Tests that the Jinja2 environment is created correctly."""
    env = create_jinja_environment()
    assert isinstance(env, Environment)
    assert str(env.loader.searchpath[0]) == str(mock_template_dir)

def test_load_template_successfully(mock_template_dir):
    """Tests that a template can be loaded successfully."""
    template = load_template("test.j2")
    assert template.render(name="World") == "Hello, World!"
def test_load_flashcard_template_successfully():
    """Tests that the flashcard.md.j2 template can be loaded."""
    template = load_template("flashcard.md.j2")
    assert template is not None

def test_render_flashcard_template():
    """Tests that the flashcard.md.j2 template renders correctly."""
    template = load_template("flashcard.md.j2")
    sample_data = {
        "question": "What is the capital of France?",
        "answer": "Paris"
    }
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
        "questions": [
            {
                "text": "What is the capital of France?",
                "options": ["London", "Paris", "Berlin"]
            }
        ]
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
