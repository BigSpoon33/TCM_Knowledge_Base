"""
End-to-End Tests for Complete Capsule Workflows

This module tests realistic capsule workflows by combining multiple operations:
1. Create a capsule (via fixtures, since generate requires LLM)
2. Validate the capsule
3. Export capsule (zip and folder formats)
4. Import capsule into a new vault
5. Verify content integrity throughout

Note: We use fixture-created capsules instead of the `generate` command
to avoid dependency on external LLM APIs during testing.
"""

import shutil
import zipfile
from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from capsule.cli import app

runner = CliRunner()


@pytest.fixture
def temp_workspace(tmp_path):
    """Create a temporary workspace with separate directories for each workflow step"""
    workspace = {
        "root": tmp_path,
        "config_dir": tmp_path / ".capsule",
        "vault1": tmp_path / "vault1",  # First vault for capsule creation
        "vault2": tmp_path / "vault2",  # Second vault for import testing
        "export_dir": tmp_path / "exports",
        "backups": tmp_path / "backups",
    }

    # Create all directories
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
        "project_dir": str(temp_workspace["vault1"]),
        "user": {"name": "Test User", "vault_path": str(temp_workspace["vault1"])},
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


@pytest.fixture
def sample_capsule(temp_workspace):
    """Create a sample capsule with realistic structure for testing"""
    capsule_path = temp_workspace["vault1"] / "Test_Capsule_v1"
    capsule_path.mkdir()

    # Create capsule-cypher.yaml
    cypher = {
        "capsule_id": "test_capsule_e2e",
        "name": "Test E2E Capsule",
        "version": "1.0.0",
        "domain_type": "education",
        "folder_structure": {"root": ".", "study_material": "study_material"},
        "contents": {
            "root_notes": [
                {"file": "Root_Note_Test_Capsule_v1.md", "id": "root-note-1"},
            ],
            "study_materials": [
                {"file": "study_material/Test_Flashcards.md", "id": "flashcard-1"},
            ],
        },
        "data_schemas": {
            "education_data": {
                "topic": "string",
                "difficulty": "string",
            }
        },
    }

    with open(capsule_path / "capsule-cypher.yaml", "w") as f:
        yaml.dump(cypher, f)

    # Create root note
    root_note_content = """---
id: root-note-1
name: Test Topic
type: root_note
tags: [education, test]
created: 2025-11-23
updated: 2025-11-23
source_capsules: [test_capsule_e2e]

education_data:
  topic: "Testing E2E Workflows"
  difficulty: "beginner"
---

# Test Topic

This is a test root note for E2E workflow testing.

## Overview

Testing capsule operations.
"""
    (capsule_path / "Root_Note_Test_Capsule_v1.md").write_text(root_note_content)

    # Create study material directory and flashcard
    (capsule_path / "study_material").mkdir()
    flashcard_content = """---
id: flashcard-1
name: Test Flashcards
type: flashcard
tags: [flashcard, test]
created: 2025-11-23
updated: 2025-11-23
source_capsules: [test_capsule_e2e]
---

# Test Flashcards

## Question 1

Q: What is being tested?

A: E2E workflows for capsule operations.
"""
    (capsule_path / "study_material" / "Test_Flashcards.md").write_text(flashcard_content)

    return capsule_path


@pytest.mark.e2e
def test_complete_workflow_validate_export_import(temp_workspace, config_file, sample_capsule):
    """
    Test complete workflow: Validate -> Export (zip) -> Import -> Verify

    This is the canonical happy path that simulates a real user workflow:
    1. User has a capsule (created via fixture instead of generate)
    2. User validates the capsule structure
    3. User exports the capsule as a zip file
    4. User imports the capsule into a different vault
    5. System verifies content integrity
    """
    vault2 = temp_workspace["vault2"]
    export_dir = temp_workspace["export_dir"]

    # ==========================================
    # STEP 1: Validate Capsule
    # ==========================================
    result_validate = runner.invoke(
        app,
        [
            "--config-path",
            str(config_file),
            "validate",
            str(sample_capsule),
        ],
    )

    # Verify validation succeeded (exit code 0 means valid)
    assert result_validate.exit_code == 0, f"Validation failed: {result_validate.stdout}\n{result_validate.exception}"

    # ==========================================
    # STEP 2: Export Capsule (Zip Format)
    # ==========================================
    result_export = runner.invoke(
        app,
        [
            "--config-path",
            str(config_file),
            "export",
            str(sample_capsule),
            "--output",
            str(export_dir),
        ],
    )

    # Verify export succeeded
    assert result_export.exit_code == 0, f"Export failed: {result_export.stdout}\n{result_export.exception}"

    # Verify zip file was created
    zip_files = list(export_dir.glob("*.zip"))
    assert len(zip_files) > 0, f"No zip file found in {export_dir}"
    zip_path = zip_files[0]

    # Verify zip contains expected files
    with zipfile.ZipFile(zip_path, "r") as zf:
        names = zf.namelist()
        assert "capsule-cypher.yaml" in names, f"capsule-cypher.yaml not in zip. Contents: {names}"
        assert "Root_Note_Test_Capsule_v1.md" in names, f"Root note not in zip. Contents: {names}"
        assert "study_material/Test_Flashcards.md" in names, f"Flashcards not in zip. Contents: {names}"
        assert "export-manifest.json" in names, f"Export manifest not in zip. Contents: {names}"

    # ==========================================
    # STEP 3: Import Capsule into Second Vault
    # ==========================================
    # Update config to point to vault2
    with open(config_file, "r") as f:
        config_data = yaml.safe_load(f)

    config_data["user"]["vault_path"] = str(vault2)

    with open(config_file, "w") as f:
        yaml.dump(config_data, f)

    result_import = runner.invoke(
        app,
        [
            "--config-path",
            str(config_file),
            "import",
            str(zip_path),
            "--yes",  # Auto-approve import
        ],
    )

    # Verify import succeeded
    assert result_import.exit_code == 0, f"Import failed: {result_import.stdout}\n{result_import.exception}"

    # ==========================================
    # STEP 4: Verify Content Integrity
    # ==========================================
    # Verify files exist in vault2
    # Note: Import may create files in vault root or maintain structure
    all_imported_files = list(vault2.rglob("*"))
    imported_md_files = [f for f in all_imported_files if f.suffix == ".md"]

    assert len(imported_md_files) > 0, f"No markdown files imported to {vault2}. Files found: {all_imported_files}"

    # Find the root note
    root_notes = [f for f in imported_md_files if "Root_Note_Test_Capsule_v1" in f.name]
    assert len(root_notes) > 0, f"Root note not imported. Files: {[f.name for f in imported_md_files]}"
    imported_root_note = root_notes[0]

    # Find the flashcard
    flashcards = [f for f in imported_md_files if "Test_Flashcards" in f.name]
    assert len(flashcards) > 0, f"Flashcards not imported. Files: {[f.name for f in imported_md_files]}"
    imported_flashcard = flashcards[0]

    # Read and verify content integrity of imported files
    original_root_content = (sample_capsule / "Root_Note_Test_Capsule_v1.md").read_text()
    imported_root_content = imported_root_note.read_text()
    assert imported_root_content == original_root_content, "Root note content mismatch after import"

    original_flashcard_content = (sample_capsule / "study_material" / "Test_Flashcards.md").read_text()
    imported_flashcard_content = imported_flashcard.read_text()
    assert imported_flashcard_content == original_flashcard_content, "Flashcard content mismatch after import"

    # Verify Master Dashboard was created (feature of import workflow)
    master_dashboards = list(vault2.glob("Master Dashboard.md"))
    assert len(master_dashboards) > 0, "Master Dashboard should be created during import"

    # Verify capsule dashboard was created
    capsule_dashboards = list(vault2.rglob("capsule-dashboard.md"))
    assert len(capsule_dashboards) > 0, (
        f"Capsule dashboard should be created during import. Files: {[f.name for f in all_imported_files]}"
    )


@pytest.mark.e2e
def test_workflow_export_folder_format(temp_workspace, config_file, sample_capsule):
    """
    Test export to folder format (not zip)

    This verifies the --no-zip flag works and capsules can be
    distributed as folder bundles.
    """
    export_dir = temp_workspace["export_dir"]

    # Export as folder (not zip)
    result_export = runner.invoke(
        app,
        [
            "--config-path",
            str(config_file),
            "export",
            str(sample_capsule),
            "--output",
            str(export_dir),
            "--no-zip",
        ],
    )

    # Verify export succeeded
    assert result_export.exit_code == 0, f"Folder export failed: {result_export.stdout}"

    # Verify folder bundle was created (not a zip file)
    exported_dirs = [d for d in export_dir.iterdir() if d.is_dir()]
    assert len(exported_dirs) > 0, f"No folder bundle found in {export_dir}"

    folder_bundle = exported_dirs[0]

    # Verify folder contains expected files
    assert (folder_bundle / "capsule-cypher.yaml").exists(), "capsule-cypher.yaml not in folder bundle"
    assert (folder_bundle / "Root_Note_Test_Capsule_v1.md").exists(), "Root note not in folder bundle"
    assert (folder_bundle / "study_material" / "Test_Flashcards.md").exists(), "Flashcards not in folder bundle"
    assert (folder_bundle / "export-manifest.json").exists(), "Export manifest not in folder bundle"


@pytest.mark.e2e
def test_workflow_import_dry_run(temp_workspace, config_file, sample_capsule):
    """
    Test import dry-run mode doesn't modify vault

    Verifies that --dry-run flag shows preview but doesn't import files.
    """
    vault2 = temp_workspace["vault2"]
    export_dir = temp_workspace["export_dir"]

    # First export the capsule
    result_export = runner.invoke(
        app, ["--config-path", str(config_file), "export", str(sample_capsule), "--output", str(export_dir)]
    )
    assert result_export.exit_code == 0

    zip_files = list(export_dir.glob("*.zip"))
    zip_path = zip_files[0]

    # Update config to vault2
    with open(config_file, "r") as f:
        config_data = yaml.safe_load(f)
    config_data["user"]["vault_path"] = str(vault2)
    with open(config_file, "w") as f:
        yaml.dump(config_data, f)

    # Dry run import
    result_dry_import = runner.invoke(app, ["--config-path", str(config_file), "import", str(zip_path), "--dry-run"])

    # Dry run should succeed
    assert result_dry_import.exit_code == 0, f"Dry run import failed: {result_dry_import.stdout}"

    # Should show dry run indicator
    assert "[Dry Run]" in result_dry_import.stdout or "dry run" in result_dry_import.stdout.lower()

    # Vault2 should still be empty (no files imported)
    vault2_files = list(vault2.glob("**/*"))
    # Filter out directories, only check for files
    vault2_files = [f for f in vault2_files if f.is_file()]
    assert len(vault2_files) == 0, f"Dry run import created files when it shouldn't: {vault2_files}"


@pytest.mark.e2e
def test_workflow_validate_before_export(temp_workspace, config_file, sample_capsule):
    """
    Test validation catches issues before export

    This test verifies the typical workflow where users validate
    before exporting to ensure capsule quality.
    """
    export_dir = temp_workspace["export_dir"]

    # Validate first
    result_validate = runner.invoke(app, ["--config-path", str(config_file), "validate", str(sample_capsule)])

    assert result_validate.exit_code == 0, "Validation should pass for well-formed capsule"

    # After successful validation, export should work
    result_export = runner.invoke(
        app, ["--config-path", str(config_file), "export", str(sample_capsule), "--output", str(export_dir)]
    )

    assert result_export.exit_code == 0, "Export should succeed after successful validation"

    # Verify zip was created
    zip_files = list(export_dir.glob("*.zip"))
    assert len(zip_files) > 0, "Export should create zip file after validation passes"


@pytest.mark.e2e
def test_workflow_import_with_backup(temp_workspace, config_file, sample_capsule):
    """
    Test that import creates backup of vault before modifying

    This is a critical safety feature - verify backup is created
    before any import operations.
    """
    vault2 = temp_workspace["vault2"]
    export_dir = temp_workspace["export_dir"]
    backup_dir = temp_workspace["backups"]

    # Create some existing content in vault2 to backup
    (vault2 / "existing_note.md").write_text("---\nid: existing\n---\n# Existing Content")

    # Export sample capsule
    result_export = runner.invoke(
        app, ["--config-path", str(config_file), "export", str(sample_capsule), "--output", str(export_dir)]
    )
    assert result_export.exit_code == 0

    zip_files = list(export_dir.glob("*.zip"))
    zip_path = zip_files[0]

    # Update config to vault2
    with open(config_file, "r") as f:
        config_data = yaml.safe_load(f)
    config_data["user"]["vault_path"] = str(vault2)
    with open(config_file, "w") as f:
        yaml.dump(config_data, f)

    # Import with backup enabled (default)
    result_import = runner.invoke(app, ["--config-path", str(config_file), "import", str(zip_path), "--yes"])

    assert result_import.exit_code == 0, "Import should succeed"

    # Verify backup was created
    assert backup_dir.exists(), "Backup directory should exist"
    backup_files = list(backup_dir.glob("*.zip"))
    assert len(backup_files) > 0, f"Backup zip should be created. Backup dir contents: {list(backup_dir.iterdir())}"

    # Verify backup contains the existing file
    backup_zip = backup_files[0]
    with zipfile.ZipFile(backup_zip, "r") as zf:
        backup_contents = zf.namelist()
        assert "existing_note.md" in backup_contents, (
            f"Backup should contain existing note. Contents: {backup_contents}"
        )
