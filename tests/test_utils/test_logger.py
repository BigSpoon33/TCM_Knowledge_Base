"""Unit tests for capsule.utils.logger module."""

import logging
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

import pytest

from capsule.exceptions import FileError
from capsule.utils.logger import setup_logging, get_logger


class TestSetupLogging:
    """Test suite for setup_logging function."""

    def test_creates_log_directory_if_missing(self, tmp_path):
        """Test that setup_logging creates log directory if it doesn't exist."""
        log_file = tmp_path / "logs" / "test.log"
        config = {"file_path": str(log_file), "rotate_bytes": 1024, "backup_count": 2}

        # Ensure directory doesn't exist
        assert not log_file.parent.exists()

        # Setup logging
        logger = setup_logging(verbose=False, config=config)

        # Verify directory was created
        assert log_file.parent.exists()
        assert log_file.parent.stat().st_mode & 0o777 == 0o755
        assert isinstance(logger, logging.Logger)

    def test_file_handler_configured_with_rotation(self, tmp_path):
        """Test that file handler has correct rotation settings."""
        log_file = tmp_path / "logs" / "test.log"
        rotate_bytes = 2 * 1024 * 1024  # 2MB
        backup_count = 5

        config = {"file_path": str(log_file), "rotate_bytes": rotate_bytes, "backup_count": backup_count}

        logger = setup_logging(verbose=False, config=config)

        # Find the RotatingFileHandler
        file_handler = None
        for handler in logger.handlers:
            if isinstance(handler, logging.handlers.RotatingFileHandler):
                file_handler = handler
                break

        assert file_handler is not None
        assert file_handler.maxBytes == rotate_bytes
        assert file_handler.backupCount == backup_count
        assert file_handler.level == logging.DEBUG

    def test_file_handler_uses_structured_format(self, tmp_path):
        """Test that file handler uses the correct log format."""
        log_file = tmp_path / "logs" / "test.log"
        config = {"file_path": str(log_file)}

        logger = setup_logging(verbose=False, config=config)

        # Find the RotatingFileHandler
        file_handler = None
        for handler in logger.handlers:
            if isinstance(handler, logging.handlers.RotatingFileHandler):
                file_handler = handler
                break

        assert file_handler is not None
        formatter = file_handler.formatter
        assert formatter is not None

        # Check format string
        expected_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        assert formatter._fmt == expected_format

    def test_console_handler_respects_verbose_flag_info(self, tmp_path):
        """Test that console handler shows INFO level when verbose=False."""
        log_file = tmp_path / "logs" / "test.log"
        config = {"file_path": str(log_file)}

        logger = setup_logging(verbose=False, config=config)

        # Find the RichHandler
        from rich.logging import RichHandler

        console_handler = None
        for handler in logger.handlers:
            if isinstance(handler, RichHandler):
                console_handler = handler
                break

        assert console_handler is not None
        assert console_handler.level == logging.INFO

    def test_console_handler_respects_verbose_flag_debug(self, tmp_path):
        """Test that console handler shows DEBUG level when verbose=True."""
        log_file = tmp_path / "logs" / "test.log"
        config = {"file_path": str(log_file)}

        logger = setup_logging(verbose=True, config=config)

        # Find the RichHandler
        from rich.logging import RichHandler

        console_handler = None
        for handler in logger.handlers:
            if isinstance(handler, RichHandler):
                console_handler = handler
                break

        assert console_handler is not None
        assert console_handler.level == logging.DEBUG

    def test_uses_default_config_when_none_provided(self, tmp_path):
        """Test that default configuration is used when config=None."""

        # Mock Path.expanduser() to use tmp_path
        def mock_expanduser(self):
            # Convert ~/.capsule/logs/capsule.log to tmp_path/.capsule/logs/capsule.log
            return tmp_path / ".capsule" / "logs" / "capsule.log"

        with patch.object(Path, "expanduser", mock_expanduser):
            logger = setup_logging(verbose=False, config=None)

            # Should use default path ~/.capsule/logs/capsule.log
            expected_log_dir = tmp_path / ".capsule" / "logs"
            assert expected_log_dir.exists()

            # Check default rotation settings
            from logging.handlers import RotatingFileHandler

            file_handler = None
            for handler in logger.handlers:
                if isinstance(handler, RotatingFileHandler):
                    file_handler = handler
                    break

            assert file_handler is not None
            assert file_handler.maxBytes == 5 * 1024 * 1024  # 5MB
            assert file_handler.backupCount == 3

    def test_expands_user_path_in_config(self, tmp_path):
        """Test that ~ is expanded in file_path config."""

        def mock_expanduser(self):
            # Convert ~/.capsule/logs/custom.log to tmp_path/.capsule/logs/custom.log
            return tmp_path / ".capsule" / "logs" / "custom.log"

        with patch.object(Path, "expanduser", mock_expanduser):
            config = {"file_path": "~/.capsule/logs/custom.log", "rotate_bytes": 1024, "backup_count": 1}

            logger = setup_logging(verbose=False, config=config)

            # Verify path was expanded
            expected_dir = tmp_path / ".capsule" / "logs"
            assert expected_dir.exists()

    def test_raises_file_error_on_permission_denied(self, tmp_path):
        """Test that FileError is raised if log directory can't be created."""
        log_file = tmp_path / "restricted" / "logs" / "test.log"
        config = {"file_path": str(log_file)}

        # Mock mkdir to raise PermissionError
        with patch("pathlib.Path.mkdir", side_effect=PermissionError("Access denied")):
            with pytest.raises(FileError) as exc_info:
                setup_logging(verbose=False, config=config)

            assert "Failed to create log directory" in str(exc_info.value)
            assert exc_info.value.hint is not None

    def test_logger_name_is_capsule(self, tmp_path):
        """Test that returned logger has name 'capsule'."""
        log_file = tmp_path / "logs" / "test.log"
        config = {"file_path": str(log_file)}

        logger = setup_logging(verbose=False, config=config)

        assert logger.name == "capsule"

    def test_logger_does_not_propagate(self, tmp_path):
        """Test that logger doesn't propagate to root logger."""
        log_file = tmp_path / "logs" / "test.log"
        config = {"file_path": str(log_file)}

        logger = setup_logging(verbose=False, config=config)

        assert logger.propagate is False

    def test_clears_existing_handlers_on_reconfiguration(self, tmp_path):
        """Test that calling setup_logging multiple times clears old handlers."""
        log_file = tmp_path / "logs" / "test.log"
        config = {"file_path": str(log_file)}

        # First setup
        logger1 = setup_logging(verbose=False, config=config)
        handler_count_1 = len(logger1.handlers)

        # Second setup (should clear and re-add)
        logger2 = setup_logging(verbose=True, config=config)
        handler_count_2 = len(logger2.handlers)

        # Should have same number of handlers (not doubled)
        assert handler_count_1 == handler_count_2
        assert handler_count_2 == 2  # File + Console


class TestGetLogger:
    """Test suite for get_logger function."""

    def test_returns_logger_with_correct_name(self):
        """Test that get_logger returns a logger with the specified name."""
        name = "capsule.commands.generate"
        logger = get_logger(name)

        assert logger.name == name
        assert isinstance(logger, logging.Logger)

    def test_logger_inherits_from_capsule_namespace(self, tmp_path):
        """Test that child loggers inherit configuration from capsule root."""
        log_file = tmp_path / "logs" / "test.log"
        config = {"file_path": str(log_file)}

        # Setup root capsule logger
        root_logger = setup_logging(verbose=False, config=config)

        # Get child logger
        child_logger = get_logger("capsule.commands.test")

        # Child logger should have no direct handlers (inherits from parent)
        assert len(child_logger.handlers) == 0

        # But should still log through parent
        assert child_logger.name.startswith("capsule.")

    def test_can_be_called_with_dunder_name(self):
        """Test common pattern of get_logger(__name__)."""
        # Simulate calling from a module
        module_name = "capsule.core.generator"
        logger = get_logger(module_name)

        assert logger.name == module_name
