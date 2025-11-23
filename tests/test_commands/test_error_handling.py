from typer.testing import CliRunner
from capsule.cli import app
from capsule.exceptions import FileError

runner = CliRunner()


def test_validate_non_existent_path():
    """Test that validate command handles missing path (Typer validation)."""
    result = runner.invoke(app, ["validate", "/non/existent/path"])
    assert result.exit_code == 2
    # Typer validation error should be present
    if result.stdout:
        assert "does not exist" in result.stdout


def test_import_non_existent_path():
    """Test that import command handles missing path (Typer validation)."""
    result = runner.invoke(app, ["import", "/non/existent/path"])
    assert result.exit_code == 2
    if result.stdout:
        assert "does not exist" in result.stdout
