import zipfile
from pathlib import Path
from datetime import datetime
import os


def create_backup(vault_path: Path, backup_dir: Path) -> Path:
    """
    Creates a timestamped zip backup of the entire vault.

    Args:
        vault_path: The path to the Obsidian vault directory.
        backup_dir: The directory where the backup will be stored.

    Returns:
        The path to the created backup zip file.
    """
    backup_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"vault_{timestamp}.zip"
    backup_filepath = backup_dir / backup_filename

    with zipfile.ZipFile(backup_filepath, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(vault_path):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(vault_path)
                zipf.write(file_path, arcname)

    return backup_filepath
