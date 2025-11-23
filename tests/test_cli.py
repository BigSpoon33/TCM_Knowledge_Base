import pytest
from unittest.mock import patch
from capsule.cli import main
from capsule.exceptions import ValidationError, FileError


def test_global_error_handler_validation_error(capsys):
    """Test that ValidationError is caught and formatted correctly."""
    with patch("capsule.cli.app") as mock_app:
        mock_app.side_effect = ValidationError("Invalid input", hint="Check your syntax")

        # We need to catch the sys.exit call
        with pytest.raises(SystemExit) as excinfo:
            main()

        assert excinfo.value.code == 1

        captured = capsys.readouterr()
        # Rich formatting might add ANSI codes, so we check for substring presence
        assert "Error" in captured.out
        assert "Invalid input" in captured.out
        assert "Hint" in captured.out
        assert "Check your syntax" in captured.out


def test_global_error_handler_file_error(capsys):
    """Test that FileError is caught and formatted correctly."""
    with patch("capsule.cli.app") as mock_app:
        mock_app.side_effect = FileError("File missing")

        with pytest.raises(SystemExit) as excinfo:
            main()

        assert excinfo.value.code == 2

        captured = capsys.readouterr()
        assert "Error" in captured.out
        assert "File missing" in captured.out


def test_global_error_handler_unexpected_error(capsys):
    """Test that unexpected exceptions are caught."""
    with patch("capsule.cli.app") as mock_app:
        mock_app.side_effect = RuntimeError("Boom")

        with pytest.raises(SystemExit) as excinfo:
            main()

        assert excinfo.value.code == 1

        captured = capsys.readouterr()
        assert "Unexpected Error" in captured.out
        assert "Boom" in captured.out
