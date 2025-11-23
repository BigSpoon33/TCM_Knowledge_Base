from unittest.mock import MagicMock, patch
import pytest
from pathlib import Path
from typer.testing import CliRunner
from capsule.cli import app
from capsule.core.researcher import GeminiResearchProvider
from capsule.models.config import Config
from capsule.models.research import ResearchResult

runner = CliRunner()


@pytest.fixture
def mock_config(monkeypatch):
    mock_class = MagicMock()
    mock_instance = MagicMock(spec=Config)
    mock_class.load_config.return_value = mock_instance
    mock_instance.get.return_value = "DUMMY_API_KEY"
    monkeypatch.setattr("capsule.commands.generate.Config", mock_class)
    return mock_instance


@pytest.fixture
def mock_researcher(monkeypatch):
    mock = MagicMock(spec=GeminiResearchProvider)

    # Mock research()
    mock.research.return_value = ResearchResult(
        content="This is a test content about the topic.", citations=[], metadata={"provider": "mock"}
    )

    # Mock generate_content() for flashcards/quiz
    mock.generate_content.return_value = "[]"  # Return empty JSON list for simplicity

    monkeypatch.setattr("capsule.commands.generate.GeminiResearchProvider", lambda: mock)
    return mock


def test_generate_command_success(mock_config, mock_researcher, tmp_path):
    # We need to run in a temp dir so files are created there
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["generate", "test topic"])

        if result.exit_code != 0:
            print(f"Output: {result.output}")
            print(f"Exception: {result.exception}")

        assert result.exit_code == 0
        assert "Capsule generated successfully!" in result.stdout
        mock_researcher.research.assert_called_once()

        # Verify files were created
        topic_dir = Path("test_topic")
        assert topic_dir.exists()
        assert (topic_dir / "Root_Note_test_topic.md").exists()


def test_generate_command_dry_run(mock_config, mock_researcher, tmp_path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["generate", "test topic", "--dry-run"])

        if result.exit_code != 0:
            print(f"Output: {result.stdout}")
            print(f"Exception: {result.exception}")

        assert result.exit_code == 0
        assert "[DRY RUN] Would generate capsule about: test topic" in result.stdout
        mock_researcher.research.assert_called_once()

        # Verify NO files were created
        topic_dir = Path("test_topic")
        assert not topic_dir.exists()


def test_generate_command_missing_args(mock_config, mock_researcher):
    result = runner.invoke(app, ["generate"])
    assert result.exit_code != 0
    # assert "Missing argument" in result.stdout
