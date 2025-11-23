# tests/test_commands/test_init.py
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from capsule.cli import app as cli_app


@pytest.fixture
def runner():
    return CliRunner()


@patch("questionary.prompt")
def test_init_success(mock_prompt, runner, tmp_path):
    """Test the init command successfully creates a config file."""

    # Simulate user input
    mock_prompt.return_value = {
        "user.name": "Test User",
        "user.vault_path": str(tmp_path / "ObsidianVault"),
        "research.api_key": "test_api_key",
    }

    # Mock Path.home() to use the temporary directory
    with patch("pathlib.Path.home", return_value=tmp_path):
        result = runner.invoke(cli_app, ["init"])

        assert result.exit_code == 0
        assert "Configuration saved" in result.output

        config_path = tmp_path / ".config" / "capsule" / "config.yaml"
        assert config_path.exists()

        # Verify content
        import yaml

        with open(config_path) as f:
            config_data = yaml.safe_load(f)

        assert config_data["user"]["name"] == "Test User"
        assert config_data["research"]["api_key"] == "test_api_key"


@patch("questionary.prompt")
def test_init_cancel(mock_prompt, runner, tmp_path):
    """Test the init command when the user cancels."""

    # Simulate user cancelling the prompt
    mock_prompt.return_value = {}

    with patch("pathlib.Path.home", return_value=tmp_path):
        result = runner.invoke(cli_app, ["init"])
        assert result.exit_code == 1

        config_path = tmp_path / ".config" / "capsule" / "config.yaml"
        assert not config_path.exists()
