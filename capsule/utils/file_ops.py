# capsule/utils/file_ops.py
import json
import shutil
import zipfile
from pathlib import Path
from typing import Optional

from .exceptions import FileError
from .logger import get_logger

logger = get_logger(__name__)


class FileOps:
    """
    Centralized file operations with dry-run support.
    """

    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run

    def write_text(self, path: Path, content: str, encoding: str = "utf-8") -> None:
        """
        Writes text to a file, respecting dry-run mode.
        """
        if self.dry_run:
            logger.info(f"[yellow][DRY RUN][/yellow] Would write to {path}")
            return

        try:
            # Atomic write pattern
            temp_path = path.with_suffix(f"{path.suffix}.tmp")
            temp_path.write_text(content, encoding=encoding)
            temp_path.replace(path)
        except OSError as e:
            raise FileError(f"Failed to write to {path}: {e}") from e

    def read_text(self, path: Path, encoding: str = "utf-8") -> str:
        """
        Reads text from a file.
        """
        try:
            return path.read_text(encoding=encoding)
        except FileNotFoundError as e:
            raise FileError(f"File not found: {path}") from e
        except OSError as e:
            raise FileError(f"Failed to read from {path}: {e}") from e

    def mkdir(self, path: Path, parents: bool = False, exist_ok: bool = False) -> None:
        """
        Creates a directory, respecting dry-run mode.
        """
        if self.dry_run:
            logger.info(f"[yellow][DRY RUN][/yellow] Would create directory {path}")
            return

        try:
            path.mkdir(parents=parents, exist_ok=exist_ok)
        except OSError as e:
            raise FileError(f"Failed to create directory {path}: {e}") from e

    def copy(self, src: Path, dst: Path) -> None:
        """
        Copies a file, respecting dry-run mode.
        """
        if self.dry_run:
            logger.info(f"[yellow][DRY RUN][/yellow] Would copy {src} to {dst}")
            return

        try:
            shutil.copy2(src, dst)
        except OSError as e:
            raise FileError(f"Failed to copy {src} to {dst}: {e}") from e

    def remove(self, path: Path) -> None:
        """
        Removes a file, respecting dry-run mode.
        """
        if self.dry_run:
            logger.info(f"[yellow][DRY RUN][/yellow] Would remove {path}")
            return

        try:
            if path.exists():
                path.unlink()
        except OSError as e:
            raise FileError(f"Failed to remove {path}: {e}") from e

    def copytree(self, src: Path, dst: Path) -> None:
        """
        Recursively copies a directory, respecting dry-run mode.
        """
        if self.dry_run:
            logger.info(f"[yellow][DRY RUN][/yellow] Would copy directory {src} to {dst}")
            return

        try:
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        except OSError as e:
            raise FileError(f"Failed to copy directory {src} to {dst}: {e}") from e

    def create_zip(self, output_path: Path, source_dir: Path, manifest: dict | None = None) -> None:
        """
        Creates a zip archive from a directory, respecting dry-run mode.
        """
        if self.dry_run:
            logger.info(f"[yellow][DRY RUN][/yellow] Would create zip archive at {output_path}")
            return

        try:
            with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
                if manifest:
                    zf.writestr("export-manifest.json", json.dumps(manifest, indent=2))
                for file_path in source_dir.rglob("*"):
                    if file_path.is_file():
                        arcname = file_path.relative_to(source_dir)
                        zf.write(file_path, arcname)
        except OSError as e:
            raise FileError(f"Failed to create zip archive at {output_path}: {e}") from e


# Backward compatibility wrappers
_default_ops = FileOps(dry_run=False)


def safe_write(path: Path, content: str) -> None:
    """
    Atomically writes content to a file by using a temporary file.
    Deprecated: Use FileOps.write_text instead.
    """
    _default_ops.write_text(path, content)


def read_file(path: Path) -> str:
    """
    Reads content from a file.
    Deprecated: Use FileOps.read_text instead.
    """
    return _default_ops.read_text(path)
