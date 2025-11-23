from unittest.mock import MagicMock, patch

import pytest
from typer.testing import CliRunner

from capsule.cli import app
from capsule.core.researcher import GeminiResearchProvider
from capsule.models.config import Config

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
    if result.exit_code != 0:
        print(f"Output: {result.output}")
        print(f"Exception: {result.exception}")
    assert result.exit_code == 0
    assert "Capsule generated successfully!" in result.stdout
    mock_generator.generate.assert_called_once()


def test_generate_command_dry_run(mock_config, mock_researcher, mock_generator):
    result = runner.invoke(app, ["generate", "test topic", "--dry-run"])
    if result.exit_code != 0:
        print(f"Output: {result.stdout}")
        print(f"Exception: {result.exception}")
    assert result.exit_code == 0
    assert "[DRY RUN] Would generate capsule about: test topic" in result.stdout
    # In the new implementation, generate IS called (to prepare content), but file writing is skipped/mocked via FileOps
    mock_generator.generate.assert_called_once()
