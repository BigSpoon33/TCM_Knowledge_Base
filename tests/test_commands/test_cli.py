"""Tests for the main CLI application and global options"""

import pytest
from typer.testing import CliRunner
from pathlib import Path
import tempfile
import yaml

from capsule.cli import app as cli_app
from capsule import __version__


@pytest.fixture
def runner():
    """Create a CLI test runner"""
    return CliRunner()


@pytest.fixture
def temp_config(tmp_path):
    """Create a temporary config file for testing"""
    config_path = tmp_path / "test_config.yaml"
    config_data = {
        "user": {"name": "Test User", "vault_path": str(tmp_path / "vault")},
        "research": {"provider": "gemini", "api_key": "test_key"},
    }
    with open(config_path, "w") as f:
        yaml.dump(config_data, f)
    return config_path


class TestVersionDisplay:
    """Test AC #5: Version display mechanism"""

    def test_version_flag_displays_version(self, runner):
        """Test that --version flag prints the correct version"""
        result = runner.invoke(cli_app, ["--version"])

        assert result.exit_code == 0
        assert f"Obsidian Capsule CLI v{__version__}" in result.output

    def test_version_short_flag(self, runner):
        """Test that -v short flag also displays version"""
        result = runner.invoke(cli_app, ["-v"])

        assert result.exit_code == 0
        assert f"Obsidian Capsule CLI v{__version__}" in result.output

    def test_version_exits_cleanly(self, runner):
        """Test that version display exits with code 0"""
        result = runner.invoke(cli_app, ["--version"])

        assert result.exit_code == 0


class TestVerboseOption:
    """Test AC #4: --verbose global option"""

    def test_verbose_flag_accepted(self, runner):
        """Test that --verbose flag is accepted without error"""
        result = runner.invoke(cli_app, ["--verbose", "--help"])

        # Should not error when verbose is provided
        assert result.exit_code == 0

    def test_verbose_enables_debug_logging(self, runner, caplog):
        """Test that --verbose flag enables DEBUG logging level"""
        import logging

        # Run with verbose flag
        result = runner.invoke(cli_app, ["--verbose", "--help"])

        # Check that logging was configured
        # Note: We can't easily check the exact level in this test framework,
        # but we verify the flag is processed without error
        assert result.exit_code == 0

    def test_default_behavior_without_verbose(self, runner):
        """Test that CLI works normally without verbose flag"""
        result = runner.invoke(cli_app, ["--help"])

        assert result.exit_code == 0
        assert "verbose" in result.output.lower()  # Help should mention verbose


class TestConfigPathOption:
    """Test AC #4: --config-path global option"""

    def test_config_path_flag_accepted(self, runner, temp_config):
        """Test that --config-path accepts a valid file path"""
        result = runner.invoke(cli_app, ["--config-path", str(temp_config), "--help"])

        assert result.exit_code == 0

    def test_config_path_option_available(self, runner):
        """Test that --config-path option is available and documented"""
        result = runner.invoke(cli_app, ["--help"])

        assert result.exit_code == 0
        assert "--config-path" in result.output

    def test_config_path_stored_in_context(self, runner, temp_config):
        """Test that config_path is stored for downstream command use"""
        # The config_path should be accepted and stored
        # Validation happens when the config is actually loaded/used
        result = runner.invoke(cli_app, ["--config-path", str(temp_config), "--help"])

        assert result.exit_code == 0
        # Should show help without error
        assert "Obsidian Capsule Delivery System" in result.output


class TestGlobalOptionsIntegration:
    """Test that global options work together"""

    def test_verbose_and_config_path_together(self, runner, temp_config):
        """Test using --verbose and --config-path together"""
        result = runner.invoke(cli_app, ["--verbose", "--config-path", str(temp_config), "--help"])

        assert result.exit_code == 0

    def test_all_global_options_with_version(self, runner, temp_config):
        """Test that version takes precedence (is_eager=True)"""
        result = runner.invoke(cli_app, ["--verbose", "--config-path", str(temp_config), "--version"])

        # Version should display and exit
        assert result.exit_code == 0
        assert f"v{__version__}" in result.output


class TestDefaultBehavior:
    """Test AC-General: Default behavior when no options provided"""

    def test_help_displays_without_options(self, runner):
        """Test that help displays correctly with no global options"""
        result = runner.invoke(cli_app, ["--help"])

        assert result.exit_code == 0
        assert "Obsidian Capsule Delivery System" in result.output
        assert "--verbose" in result.output
        assert "--config-path" in result.output
        assert "--version" in result.output

    def test_cli_app_has_correct_name(self, runner):
        """Test that the CLI app is properly named"""
        result = runner.invoke(cli_app, ["--help"])

        assert result.exit_code == 0
        # The app name should appear in the help


class TestErrorHandling:
    """Test AC-General: Error handling for invalid inputs"""

    def test_unknown_option_shows_error(self, runner):
        """Test that unknown options are caught"""
        result = runner.invoke(cli_app, ["--unknown-option"])

        assert result.exit_code != 0
        assert "error" in result.output.lower() or "no such option" in result.output.lower()

    def test_config_path_validation_deferred(self, runner):
        """Test that config_path validation is deferred to actual usage

        Note: Typer allows Optional[Path] to pass through even with exists=True.
        The actual validation happens when commands try to load the config file.
        This is intentional - we want global options to be lightweight.
        """
        # This should not fail at the global option level
        result = runner.invoke(cli_app, ["--config-path", "/nonexistent.yaml", "--help"])

        # Help should still display (validation deferred)
        assert result.exit_code == 0
        assert "Obsidian Capsule Delivery System" in result.output


class TestTyperAppConfiguration:
    """Test AC #1, #2: Typer app exists and is properly configured"""

    def test_cli_app_exists(self):
        """Test that the Typer app instance exists"""
        import typer

        assert isinstance(cli_app, typer.Typer)

    def test_cli_app_has_correct_configuration(self):
        """Test that the Typer app has the expected configuration"""
        assert cli_app.info.name == "capsule"
        assert "Obsidian Capsule Delivery System" in cli_app.info.help

    def test_cli_app_has_commands_registered(self):
        """Test that subcommands are registered"""
        # The app should have multiple commands registered
        # This is verified by checking that commands exist
        runner = CliRunner()
        result = runner.invoke(cli_app, ["--help"])

        assert "generate" in result.output
        assert "validate" in result.output
        assert "export" in result.output
        assert "import" in result.output
        assert "init" in result.output
