from typer.testing import CliRunner
from unittest.mock import MagicMock, patch
import pytest

from capsule.cli import app
from capsule.core.generator import ContentGenerator
from capsule.models.config import Config
from capsule.core.researcher import GeminiResearchProvider

runner = CliRunner()


@pytest.fixture
def mock_config(monkeypatch):
    mock = MagicMock(spec=Config)
    mock.get.return_value = "DUMMY_API_KEY"
    monkeypatch.setattr("capsule.commands.generate.Config", lambda: mock)
    return mock


@pytest.fixture
def mock_researcher(monkeypatch):
    mock = MagicMock(spec=GeminiResearchProvider)
    monkeypatch.setattr("capsule.commands.generate.GeminiResearchProvider", lambda: mock)
    return mock


@pytest.fixture
def mock_generator(monkeypatch):
    with patch("capsule.commands.generate.ContentGenerator") as mock:
        mock_instance = mock.return_value
        mock_instance.generate.return_value = {"root_note": "This is a test"}
        yield mock_instance


def test_generate_command_success(mock_config, mock_researcher, mock_generator):
    result = runner.invoke(app, ["generate", "test topic"])
    assert result.exit_code == 0
    assert "Capsule generated successfully!" in result.stdout
    mock_generator.generate.assert_called_once()


def test_generate_command_dry_run(mock_generator):
    result = runner.invoke(app, ["generate", "test topic", "--dry-run"])
    assert result.exit_code == 0
    assert "Would generate capsule about: test topic" in result.stdout
    mock_generator.generate.assert_not_called()
