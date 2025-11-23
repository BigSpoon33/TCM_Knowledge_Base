# tests/test_utils/test_file_ops.py
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from capsule.utils.exceptions import FileError
from capsule.utils.file_ops import FileOps, read_file, safe_write


class TestFileOps:
    @pytest.fixture
    def file_ops(self):
        return FileOps(dry_run=False)

    @pytest.fixture
    def dry_run_ops(self):
        return FileOps(dry_run=True)

    def test_write_text_success(self, file_ops, tmp_path):
        """Test that write_text successfully writes content to a file."""
        file_path = tmp_path / "test.txt"
        content = "Hello, world!"
        file_ops.write_text(file_path, content)
        assert file_path.read_text(encoding="utf-8") == content

    def test_write_text_dry_run(self, dry_run_ops, tmp_path):
        """Test that write_text does NOT write content in dry-run mode."""
        file_path = tmp_path / "test.txt"
        content = "Hello, world!"
        dry_run_ops.write_text(file_path, content)
        assert not file_path.exists()

    def test_read_text_success(self, file_ops, tmp_path):
        """Test that read_text successfully reads content from a file."""
        file_path = tmp_path / "test.txt"
        content = "Hello, world!"
        file_path.write_text(content, encoding="utf-8")
        assert file_ops.read_text(file_path) == content

    def test_read_text_not_found(self, file_ops):
        """Test that read_text raises FileError when the file does not exist."""
        with pytest.raises(FileError, match="File not found"):
            file_ops.read_text(Path("non_existent_file.txt"))

    def test_mkdir_success(self, file_ops, tmp_path):
        """Test that mkdir successfully creates a directory."""
        dir_path = tmp_path / "new_dir"
        file_ops.mkdir(dir_path)
        assert dir_path.exists()
        assert dir_path.is_dir()

    def test_mkdir_dry_run(self, dry_run_ops, tmp_path):
        """Test that mkdir does NOT create a directory in dry-run mode."""
        dir_path = tmp_path / "new_dir"
        dry_run_ops.mkdir(dir_path)
        assert not dir_path.exists()

    def test_copy_success(self, file_ops, tmp_path):
        """Test that copy successfully copies a file."""
        src = tmp_path / "src.txt"
        dst = tmp_path / "dst.txt"
        src.write_text("content", encoding="utf-8")
        file_ops.copy(src, dst)
        assert dst.exists()
        assert dst.read_text(encoding="utf-8") == "content"

    def test_copy_dry_run(self, dry_run_ops, tmp_path):
        """Test that copy does NOT copy a file in dry-run mode."""
        src = tmp_path / "src.txt"
        dst = tmp_path / "dst.txt"
        src.write_text("content", encoding="utf-8")
        dry_run_ops.copy(src, dst)
        assert not dst.exists()

    def test_remove_success(self, file_ops, tmp_path):
        """Test that remove successfully removes a file."""
        file_path = tmp_path / "test.txt"
        file_path.write_text("content", encoding="utf-8")
        file_ops.remove(file_path)
        assert not file_path.exists()

    def test_remove_dry_run(self, dry_run_ops, tmp_path):
        """Test that remove does NOT remove a file in dry-run mode."""
        file_path = tmp_path / "test.txt"
        file_path.write_text("content", encoding="utf-8")
        dry_run_ops.remove(file_path)
        assert file_path.exists()

    @patch("pathlib.Path.write_text", side_effect=OSError("Permission denied"))
    def test_write_text_permission_error(self, mock_write, file_ops, tmp_path):
        """Test that write_text raises FileError on IOError."""
        file_path = tmp_path / "test.txt"
        with pytest.raises(FileError, match="Permission denied"):
            file_ops.write_text(file_path, "content")

    @patch("pathlib.Path.read_text", side_effect=OSError("Read error"))
    def test_read_text_read_error(self, mock_read, file_ops):
        """Test that read_text raises FileError on IOError."""
        with pytest.raises(FileError, match="Read error"):
            file_ops.read_text(Path("anyfile.txt"))


# Backward compatibility tests
def test_safe_write_compat(tmp_path):
    """Test that safe_write wrapper works."""
    file_path = tmp_path / "test.txt"
    content = "Hello, world!"
    safe_write(file_path, content)
    assert file_path.read_text(encoding="utf-8") == content


def test_read_file_compat(tmp_path):
    """Test that read_file wrapper works."""
    file_path = tmp_path / "test.txt"
    content = "Hello, world!"
    file_path.write_text(content, encoding="utf-8")
    assert read_file(file_path) == content
