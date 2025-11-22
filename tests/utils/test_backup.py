import zipfile
from pathlib import Path
from capsule.utils.backup import create_backup


def test_create_backup_successful(tmp_path):
    """
    Tests that a backup is created successfully with the correct structure.
    """
    # 1. Arrange: Create a fake vault structure
    vault_path = tmp_path / "vault"
    vault_path.mkdir()
    (vault_path / "note1.md").write_text("This is note 1.")
    (vault_path / "folder1").mkdir()
    (vault_path / "folder1" / "note2.md").write_text("This is note 2.")

    backup_dir = tmp_path / "backups"

    # 2. Act: Create the backup
    backup_path = create_backup(vault_path, backup_dir)

    # 3. Assert: Check the backup file
    assert backup_path.exists()
    assert backup_path.parent == backup_dir
    assert backup_path.name.startswith("vault_")
    assert backup_path.name.endswith(".zip")

    # Verify contents of the zip file
    with zipfile.ZipFile(backup_path, "r") as zipf:
        filenames = zipf.namelist()
        assert "note1.md" in filenames
        assert str(Path("folder1") / "note2.md") in filenames
        assert len(filenames) == 2

        with zipf.open("note1.md") as f:
            assert f.read().decode() == "This is note 1."
        with zipf.open(str(Path("folder1") / "note2.md")) as f:
            assert f.read().decode() == "This is note 2."


def test_backup_handles_empty_directory(tmp_path):
    """
    Tests that the backup function correctly handles an empty vault directory.
    """
    # 1. Arrange: Create an empty fake vault
    vault_path = tmp_path / "vault"
    vault_path.mkdir()

    backup_dir = tmp_path / "backups"

    # 2. Act: Create the backup
    backup_path = create_backup(vault_path, backup_dir)

    # 3. Assert: Check the backup file
    assert backup_path.exists()

    # Verify contents of the zip file
    with zipfile.ZipFile(backup_path, "r") as zipf:
        assert len(zipf.namelist()) == 0
