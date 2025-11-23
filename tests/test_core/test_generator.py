import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from capsule.core.generator import ContentGenerator
from capsule.models.research import ResearchResult


@pytest.fixture
def mock_researcher():
    return MagicMock()


@pytest.fixture
def mock_validator():
    return MagicMock()


@pytest.fixture
def content_generator(mock_researcher, mock_validator):
    with (
        patch("capsule.core.generator.FileOps") as MockFileOps,
        patch("capsule.core.generator.jinja2.Environment") as MockEnv,
        patch("capsule.core.generator.TemplateEngine") as MockTemplateEngine,
        patch("capsule.core.generator.SlidesGenerator") as MockSlidesGenerator,
        patch("capsule.core.generator.ConversationGenerator") as MockConversationGenerator,
    ):
        generator = ContentGenerator(mock_researcher, mock_validator)
        return generator


def test_initialization(content_generator, mock_researcher, mock_validator):
    assert content_generator.researcher == mock_researcher
    assert content_generator.validator == mock_validator
    assert content_generator.file_ops is not None
    assert content_generator.template_env is not None
    assert content_generator.template_engine is not None
    assert content_generator.slides_generator is not None
    assert content_generator.conversation_generator is not None


def test_generate_root_note(content_generator, mock_researcher):
    # Setup
    topic = "Test Topic"
    template_name = "test_template"
    materials = ["root_note"]

    mock_research_result = ResearchResult(content="Research content", citations=[], metadata={})
    mock_researcher.research.return_value = mock_research_result

    # Mock template loading and rendering
    mock_template = MagicMock()
    mock_template.render.return_value = "# Root Note Content"
    content_generator.template_env.get_template.return_value = mock_template

    # Execute
    result = content_generator.generate(topic, template_name, materials)

    # Verify
    mock_researcher.research.assert_called_once_with(topic)
    content_generator.template_env.get_template.assert_called_with(template_name)
    mock_template.render.assert_called()
    assert result["root_note"] == "# Root Note Content"


def test_generate_with_materials(content_generator, mock_researcher):
    # Setup
    topic = "Test Topic"
    template_name = "test_template"
    materials = ["flashcards", "quiz"]

    mock_research_result = ResearchResult(content="Research content", citations=[], metadata={})
    mock_researcher.research.return_value = mock_research_result

    # Mock internal generation methods to isolate logic
    content_generator._generate_flashcards = MagicMock(return_value="Flashcards Content")
    content_generator._generate_quiz = MagicMock(return_value="Quiz Content")

    # Execute
    result = content_generator.generate(topic, template_name, materials)

    # Verify
    assert result["flashcards"] == "Flashcards Content"
    assert result["quiz"] == "Quiz Content"
    content_generator._generate_flashcards.assert_called_once()
    content_generator._generate_quiz.assert_called_once()


def test_generate_from_source_path(content_generator, mock_researcher):
    # Setup
    topic = "Test Topic"
    template_name = "test_template"
    materials = ["root_note"]
    source_path = Path("test.md")

    content_generator.file_ops.read_text.return_value = "Existing content"

    mock_template = MagicMock()
    mock_template.render.return_value = "# Root Note Content"
    content_generator.template_env.get_template.return_value = mock_template

    # Execute
    with patch.object(Path, "exists", return_value=True):
        result = content_generator.generate(topic, template_name, materials, source_path=source_path)

    # Verify
    mock_researcher.research.assert_not_called()
    content_generator.file_ops.read_text.assert_called_with(source_path)
    assert result["root_note"] == "# Root Note Content"
