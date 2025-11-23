# capsule/utils/file_ops.py
from pathlib import Path

from .exceptions import FileError


def safe_write(path: Path, content: str) -> None:
    """
    Atomically writes content to a file by using a temporary file.

    Args:
        path: The destination file path.
        content: The string content to write.

    Raises:
        FileError: If any file operation fails.
    """
    try:
        temp_path = path.with_suffix(f"{path.suffix}.tmp")
        temp_path.write_text(content, encoding="utf-8")
        temp_path.replace(path)
    except OSError as e:
        raise FileError(f"Failed to write to {path}: {e}") from e


def read_file(path: Path) -> str:
    """
    Reads content from a file.

    Args:
        path: The file path to read from.

    Returns:
        The content of the file as a string.

    Raises:
        FileError: If the file cannot be read.
    """
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        raise FileError(f"File not found: {path}") from e
    except OSError as e:
        raise FileError(f"Failed to read from {path}: {e}") from e
