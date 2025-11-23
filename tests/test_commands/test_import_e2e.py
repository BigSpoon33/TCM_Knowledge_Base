import shutil

import pytest
import yaml
from typer.testing import CliRunner

from capsule.cli import app

runner = CliRunner()


@pytest.fixture
def test_vault(tmp_path):
    vault = tmp_path / "vault"
    vault.mkdir()
    return vault


@pytest.fixture
def test_capsule(tmp_path):
    capsule = tmp_path / "capsule"
    capsule.mkdir()

    # Create cypher
    cypher = {
        "capsule_id": "test_capsule",
        "name": "Test Capsule",
        "version": "1.0.0",
        "domain_type": "test",
        "folder_structure": {},
        "data_schemas": {},
        "contents": {"root_notes": [{"file": "note.md"}]},
    }
    with open(capsule / "capsule-cypher.yaml", "w") as f:
        yaml.dump(cypher, f)

    # Create note
    with open(capsule / "note.md", "w") as f:
        f.write("---\nid: note-1\n---\n# Test Note")

    return capsule


@pytest.fixture
def config_file(tmp_path, test_vault):
    config_dir = tmp_path / ".capsule"
    config_dir.mkdir()
    config_path = config_dir / "config.yaml"

    config_data = {"user": {"vault_path": str(test_vault)}, "import": {"backup_location": str(tmp_path / "backups")}}

    with open(config_path, "w") as f:
        yaml.dump(config_data, f)

    return config_path


def test_e2e_import(test_vault, test_capsule, config_file):
    result = runner.invoke(app, ["--config-path", str(config_file), "import", str(test_capsule), "--yes"])

    if result.exit_code != 0:
        print(result.output)
        print(result.exception)

    assert result.exit_code == 0
    assert (test_vault / "note.md").exists()
    assert "Executing import..." in result.stdout


def test_e2e_import_dry_run(test_vault, test_capsule, config_file):
    result = runner.invoke(app, ["--config-path", str(config_file), "import", str(test_capsule), "--dry-run"])

    if result.exit_code != 0:
        print(result.output)
        print(result.exception)

    assert result.exit_code == 0
    assert not (test_vault / "note.md").exists()
    assert "[Dry Run]" in result.stdout


def test_e2e_import_zip(test_capsule, test_vault, config_file, tmp_path):
    # Create zip from capsule folder
    zip_path = tmp_path / "test_capsule"  # make_archive adds .zip
    shutil.make_archive(str(zip_path), "zip", test_capsule)
    zip_file = tmp_path / "test_capsule.zip"

    # Run import command
    result = runner.invoke(app, ["--config-path", str(config_file), "import", str(zip_file), "--yes"])

    assert result.exit_code == 0
    assert (test_vault / "note.md").exists()


def test_e2e_import_no_backup(test_capsule, test_vault, config_file, tmp_path):
    backup_dir = tmp_path / "backups"

    result = runner.invoke(
        app, ["--config-path", str(config_file), "import", str(test_capsule), "--yes", "--no-backup"]
    )

    assert result.exit_code == 0
    assert (test_vault / "note.md").exists()
    # Check that backup dir is empty or doesn't exist (if it wasn't created before)
    if backup_dir.exists():
        assert not list(backup_dir.iterdir())


def test_e2e_import_creates_backup(test_capsule, test_vault, config_file, tmp_path):
    backup_dir = tmp_path / "backups"

    # Ensure vault has some content to backup
    (test_vault / "existing_file.md").write_text("content")

    result = runner.invoke(app, ["--config-path", str(config_file), "import", str(test_capsule), "--yes"])

    assert result.exit_code == 0
    assert backup_dir.exists()
    assert len(list(backup_dir.iterdir())) == 1
    # Verify backup content (it should be a zip file)
    backup_file = list(backup_dir.iterdir())[0]
    assert backup_file.suffix == ".zip"
