# tests/test_utils/test_file_ops.py
from pathlib import Path
from unittest.mock import patch

import pytest

from capsule.utils.exceptions import FileError
from capsule.utils.file_ops import read_file, safe_write


def test_safe_write_success(tmp_path):
    """Test that safe_write successfully writes content to a file."""
    file_path = tmp_path / "test.txt"
    content = "Hello, world!"
    safe_write(file_path, content)
    assert file_path.read_text(encoding="utf-8") == content


def test_read_file_success(tmp_path):
    """Test that read_file successfully reads content from a file."""
    file_path = tmp_path / "test.txt"
    content = "Hello, world!"
    file_path.write_text(content, encoding="utf-8")
    assert read_file(file_path) == content


def test_read_file_not_found():
    """Test that read_file raises FileError when the file does not exist."""
    with pytest.raises(FileError, match="File not found"):
        read_file(Path("non_existent_file.txt"))


@patch("pathlib.Path.write_text", side_effect=OSError("Permission denied"))
def test_safe_write_permission_error(mock_write, tmp_path):
    """Test that safe_write raises FileError on IOError."""
    file_path = tmp_path / "test.txt"
    with pytest.raises(FileError, match="Permission denied"):
        safe_write(file_path, "content")


@patch("pathlib.Path.read_text", side_effect=OSError("Read error"))
def test_read_file_read_error(mock_read):
    """Test that read_file raises FileError on IOError."""
    with pytest.raises(FileError, match="Read error"):
        read_file(Path("anyfile.txt"))


@patch("pathlib.Path.replace")
@patch("pathlib.Path.write_text")
def test_safe_write_atomicity(mock_write, mock_replace, tmp_path):
    """Test the atomic nature of safe_write."""
    file_path = tmp_path / "test.txt"
    temp_path = file_path.with_suffix(".txt.tmp")
    content = "atomic content"

    safe_write(file_path, content)

    mock_write.assert_called_once_with(content, encoding="utf-8")
    # This is a bit tricky as the Path object is created inside the function.
    # A better way would be to patch Path() to control the object returned.
    # For now, we'll just check that replace was called on *some* Path object.
    mock_replace.assert_called_once()
