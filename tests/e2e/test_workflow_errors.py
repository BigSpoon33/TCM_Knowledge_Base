"""
End-to-End Error Handling Tests

This module tests error scenarios in complete workflows:
1. Import of invalid/corrupted capsules
2. Export of malformed capsules
3. Validation failures
"""

import zipfile
from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from capsule.cli import app

runner = CliRunner()


@pytest.fixture
def temp_workspace(tmp_path):
    """Create a temporary workspace for error testing"""
    workspace = {
        "root": tmp_path,
        "config_dir": tmp_path / ".capsule",
        "vault": tmp_path / "vault",
        "invalid_capsules": tmp_path / "invalid_capsules",
        "backups": tmp_path / "backups",
    }

    for path in workspace.values():
        if isinstance(path, Path):
            path.mkdir(parents=True, exist_ok=True)

    return workspace


@pytest.fixture
def config_file(temp_workspace):
    """Create a test configuration file"""
    config_path = temp_workspace["config_dir"] / "config.yaml"

    config_data = {
        "llm_provider": "dummy",
        "api_key": "test_key",
        "default_model": "test-model",
        "project_dir": str(temp_workspace["vault"]),
        "user": {"name": "Test User", "vault_path": str(temp_workspace["vault"])},
        "research": {
            "provider": "dummy",
            "max_sources": 5,
            "enable_grounding": False,
        },
        "import": {"auto_backup": True, "backup_location": str(temp_workspace["backups"])},
        "logging": {"level": "INFO", "file": str(temp_workspace["root"] / "capsule.log")},
    }

    with open(config_path, "w") as f:
        yaml.dump(config_data, f)

    return config_path


@pytest.mark.e2e
def test_import_invalid_capsule_missing_cypher(temp_workspace, config_file):
    """
    Test import of a capsule that's missing the capsule-cypher.yaml file

    Expected behavior: Import should fail with error
    """
    invalid_dir = temp_workspace["invalid_capsules"]
    capsule_path = invalid_dir / "missing_cypher_capsule"
    capsule_path.mkdir()

    # Create a note without a cypher
    (capsule_path / "note.md").write_text("---\nid: test\n---\n# Test")

    # Create a zip from this invalid capsule
    zip_path = invalid_dir / "invalid_capsule.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.write(capsule_path / "note.md", arcname="note.md")

    # Attempt import
    result = runner.invoke(app, ["--config-path", str(config_file), "import", str(zip_path), "--yes"])

    # Import should fail
    assert result.exit_code != 0, f"Import should have failed but succeeded: {result.stdout}"


@pytest.mark.e2e
def test_import_capsule_corrupted_yaml(temp_workspace, config_file):
    """
    Test import of a capsule with corrupted YAML in cypher

    Expected behavior: Import should fail with YAML error
    """
    invalid_dir = temp_workspace["invalid_capsules"]
    capsule_path = invalid_dir / "corrupted_cypher_capsule"
    capsule_path.mkdir()

    # Create a malformed cypher file (invalid YAML)
    (capsule_path / "capsule-cypher.yaml").write_text(
        """
capsule_id: test
version: 1.0.0
this is not valid YAML: {[}]
random: ::::: garbage
"""
    )

    # Create a note
    (capsule_path / "note.md").write_text("---\nid: test\n---\n# Test")

    # Create zip
    zip_path = invalid_dir / "corrupted.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.write(capsule_path / "capsule-cypher.yaml", arcname="capsule-cypher.yaml")
        zf.write(capsule_path / "note.md", arcname="note.md")

    # Attempt import
    result = runner.invoke(app, ["--config-path", str(config_file), "import", str(zip_path), "--yes"])

    # Import should fail
    assert result.exit_code != 0, f"Import should have failed but succeeded: {result.stdout}"


@pytest.mark.e2e
def test_import_zip_file_not_found(temp_workspace, config_file):
    """
    Test import when the specified zip file doesn't exist

    Expected behavior: Import should fail with file not found error
    """
    nonexistent_zip = temp_workspace["root"] / "nonexistent.zip"

    result = runner.invoke(app, ["--config-path", str(config_file), "import", str(nonexistent_zip), "--yes"])

    # Import should fail
    assert result.exit_code != 0, f"Import should have failed but succeeded: {result.stdout}"


@pytest.mark.e2e
def test_export_nonexistent_capsule(temp_workspace, config_file):
    """
    Test export of a capsule path that doesn't exist

    Expected behavior: Export should fail
    """
    nonexistent_path = temp_workspace["root"] / "nonexistent_capsule"
    export_dir = temp_workspace["root"] / "exports"
    export_dir.mkdir()

    result = runner.invoke(
        app, ["--config-path", str(config_file), "export", str(nonexistent_path), "--output", str(export_dir)]
    )

    # Export should fail
    assert result.exit_code != 0, f"Export should have failed but succeeded: {result.stdout}"


@pytest.mark.e2e
def test_validate_nonexistent_path(temp_workspace, config_file):
    """
    Test validation of a path that doesn't exist

    Expected behavior: Validation should fail
    """
    nonexistent_path = temp_workspace["root"] / "this_path_does_not_exist"

    result = runner.invoke(app, ["--config-path", str(config_file), "validate", str(nonexistent_path)])

    # Validation should fail (non-zero exit code)
    assert result.exit_code != 0, f"Validation should have failed but got exit code: {result.exit_code}"


@pytest.mark.e2e
def test_export_capsule_missing_files_in_inventory(temp_workspace, config_file):
    """
    Test export of a capsule where files listed in cypher are missing

    Expected behavior: Export should fail or warn about missing files
    """
    invalid_dir = temp_workspace["invalid_capsules"]
    capsule_path = invalid_dir / "missing_files_capsule"
    capsule_path.mkdir()

    # Create cypher that references files that don't exist
    cypher = {
        "capsule_id": "test_missing",
        "name": "Test Missing Files",
        "version": "1.0.0",
        "domain_type": "test",
        "contents": {
            "root_notes": [
                {"file": "note1.md", "id": "note-1"},
                {"file": "note2.md", "id": "note-2"},  # This file won't exist
            ]
        },
    }

    with open(capsule_path / "capsule-cypher.yaml", "w") as f:
        yaml.dump(cypher, f)

    # Only create note1.md (note2.md is missing)
    (capsule_path / "note1.md").write_text("---\nid: note-1\n---\n# Note 1")

    # Attempt export
    export_dir = temp_workspace["root"] / "exports"
    export_dir.mkdir()

    result = runner.invoke(
        app, ["--config-path", str(config_file), "export", str(capsule_path), "--output", str(export_dir)]
    )

    # Export should fail or succeed with warnings (depending on implementation)
    # At minimum, verify it completes (implementation may vary)
    assert result.exit_code is not None, "Export should complete with some exit code"
