"""Logging configuration and setup for the Capsule CLI.

This module provides structured logging with dual-handler pattern:
- File handler: Captures everything at DEBUG level with rotation
- Console handler: Shows INFO+ by default, DEBUG with --verbose flag
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional

from rich.logging import RichHandler

from capsule.exceptions import FileError


def setup_logging(verbose: bool = False, config: Optional[dict] = None) -> logging.Logger:
    """Configure logging with file and console handlers.

    Args:
        verbose: If True, console handler shows DEBUG level. Otherwise INFO+
        config: Optional logging configuration dict with keys:
                - file_path: Path to log file (default: ~/.capsule/logs/capsule.log)
                - rotate_bytes: Max file size before rotation (default: 5MB)
                - backup_count: Number of backup files to keep (default: 3)
                - level: Base log level (default: INFO)

    Returns:
        Configured logger instance for 'capsule' namespace

    Raises:
        FileError: If log directory cannot be created
    """
    # Merge config with defaults
    if config is None:
        config = {}

    file_path_str = config.get("file_path", "~/.capsule/logs/capsule.log")
    rotate_bytes = config.get("rotate_bytes", 5 * 1024 * 1024)  # 5MB
    backup_count = config.get("backup_count", 3)

    # Expand user path
    log_file = Path(file_path_str).expanduser()

    # Create log directory with proper permissions
    try:
        log_file.parent.mkdir(parents=True, exist_ok=True, mode=0o755)
    except (OSError, PermissionError) as e:
        raise FileError(
            f"Failed to create log directory: {log_file.parent}", hint=f"Check directory permissions. Error: {e}"
        ) from e

    # Configure file handler with rotation (always DEBUG level)
    file_handler = RotatingFileHandler(log_file, maxBytes=rotate_bytes, backupCount=backup_count, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

    # Configure console handler with RichHandler (respects verbose flag)
    console_level = logging.DEBUG if verbose else logging.INFO
    console_handler = RichHandler(
        rich_tracebacks=True,
        markup=True,
        show_time=False,  # Time already in file logs
        show_path=verbose,  # Show file path only in verbose mode
    )
    console_handler.setLevel(console_level)

    # Get or create the capsule logger
    logger = logging.getLogger("capsule")
    logger.setLevel(logging.DEBUG)  # Capture everything, handlers will filter

    # Clear existing handlers to avoid duplicates on reconfiguration
    logger.handlers.clear()

    # Add both handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Prevent propagation to root logger
    logger.propagate = False

    return logger


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance for a specific module.

    Args:
        name: Module name (e.g., 'capsule.commands.generate')

    Returns:
        Logger instance that inherits from 'capsule' root logger

    Example:
        logger = get_logger(__name__)
        logger.info("Starting generation...")
    """
    return logging.getLogger(name)
