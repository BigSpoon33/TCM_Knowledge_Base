"""Tests for capsule/commands/import_cmd.py"""

import pytest
from pathlib import Path
from typer.testing import CliRunner
from capsule.cli import app
import tempfile
import zipfile


runner = CliRunner()


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing"""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_config_file(temp_dir):
    """Create a mock config file"""
    # Use the correct path that Config.load_config() checks
    config_path = Path.home() / ".config" / "capsule" / "config.yaml"
    config_path.parent.mkdir(parents=True, exist_ok=True)

    # Create vault directory
    vault_path = temp_dir / "test_vault"
    vault_path.mkdir(parents=True, exist_ok=True)

    # Create backup directory
    backup_dir = temp_dir / "backups"
    backup_dir.mkdir(parents=True, exist_ok=True)

    config_content = f"""llm_provider: openai
api_key: test-key
default_model: gpt-4-turbo
project_dir: {temp_dir}
user:
  name: Test User
  vault_path: {vault_path}
  import:
    auto_backup: false
    backup_location: {backup_dir}
    default_merge_strategy: section-level
research: {{}}
"""
    config_path.write_text(config_content)

    yield config_path

    # Cleanup
    if config_path.exists():
        config_path.unlink()


@pytest.fixture
def sample_capsule(temp_dir):
    """Create a sample capsule folder"""
    capsule_path = temp_dir / "test_capsule_v1"
    capsule_path.mkdir()

    # Create cypher
    cypher_content = """capsule_id: "test_capsule_v1"
name: "Test Capsule"
version: "1.0.0"
domain_type: "education"
folder_structure:
  root_notes: "notes/"
contents:
  root_notes:
    - file: "notes/test.md"
      id: "test-1"
data_schemas: {}
sequence_mode: "freeform"
"""
    (capsule_path / "capsule-cypher.yaml").write_text(cypher_content)

    # Create note
    notes_dir = capsule_path / "notes"
    notes_dir.mkdir()

    note_content = """---
id: test-1
name: Test Note
type: root_note
tags: [test]
created: 2025-11-15
updated: 2025-11-15
source_capsules: [test_capsule_v1]
---

# Test Content
"""
    (notes_dir / "test.md").write_text(note_content)

    return capsule_path


@pytest.fixture
def sample_capsule_zip(sample_capsule, temp_dir):
    """Create a sample capsule zip file"""
    zip_path = temp_dir / "test_capsule_v1.capsule"

    with zipfile.ZipFile(zip_path, "w") as zip_ref:
        for file_path in sample_capsule.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(sample_capsule.parent)
                zip_ref.write(file_path, arcname)

    return zip_path


class TestImportCommand:
    """Test import command execution"""

    def test_import_from_folder(self, mock_config_file, sample_capsule):
        """Test importing from a capsule folder"""
        result = runner.invoke(app, ["import", "import", str(sample_capsule), "--no-backup"], input="y\n")

        # Print output for debugging
        if result.exit_code != 0:
            print(f"Exit code: {result.exit_code}")
            print(f"Output: {result.stdout}")
            if result.exception:
                print(f"Exception: {result.exception}")

        assert result.exit_code == 0, f"Command failed with output: {result.stdout}"
        assert "Test Capsule" in result.stdout
        assert "Import execution completed" in result.stdout

    def test_import_from_zip(self, mock_config_file, sample_capsule_zip):
        """Test importing from a capsule zip file"""
        result = runner.invoke(app, ["import", "import", str(sample_capsule_zip), "--no-backup"], input="y\n")

        assert result.exit_code == 0
        assert "Extracting capsule archive" in result.stdout
        assert "Test Capsule" in result.stdout
        assert "Import execution completed" in result.stdout

    def test_import_nonexistent_file(self, mock_config_file, temp_dir):
        """Test error when importing nonexistent file"""
        nonexistent = temp_dir / "nonexistent.capsule"
        result = runner.invoke(app, ["import", "import", str(nonexistent)])

        # Exit code 2 means typer caught the error (file doesn't exist check in argument validation)
        assert result.exit_code == 2

    def test_import_with_custom_target(self, mock_config_file, sample_capsule, temp_dir):
        """Test importing with custom target vault"""
        custom_vault = temp_dir / "custom_vault"
        custom_vault.mkdir()

        result = runner.invoke(
            app, ["import", "import", str(sample_capsule), "--target", str(custom_vault), "--no-backup"], input="y\n"
        )

        assert result.exit_code == 0
        assert "Import execution completed" in result.stdout

    def test_import_shows_preview(self, mock_config_file, sample_capsule):
        """Test that preview information is displayed"""
        result = runner.invoke(app, ["import", "import", str(sample_capsule), "--no-backup"], input="y\n")

        assert result.exit_code == 0
        # Check for preview elements
        assert "Capsule Information" in result.stdout
        assert "Impact Analysis" in result.stdout
        assert "test_capsule_v1" in result.stdout
        assert "1.0.0" in result.stdout

    def test_import_interactive_yes(self, mock_config_file, sample_capsule):
        """Test interactive approval with 'y'"""
        result = runner.invoke(app, ["import", "import", str(sample_capsule), "--no-backup"], input="y\n")
        assert result.exit_code == 0
        assert "Do you want to proceed with the import?" in result.stdout
        assert "Import execution completed" in result.stdout

    def test_import_interactive_no(self, mock_config_file, sample_capsule):
        """Test interactive approval with 'n'"""
        result = runner.invoke(app, ["import", "import", str(sample_capsule), "--no-backup"], input="n\n")
        assert result.exit_code == 0
        assert "Do you want to proceed with the import?" in result.stdout
        assert "Import cancelled by user" in result.stdout
        assert "Import execution completed" not in result.stdout

    def test_import_force(self, mock_config_file, sample_capsule):
        """Test force flag bypasses prompt"""
        result = runner.invoke(app, ["import", "import", str(sample_capsule), "--no-backup", "--force"])
        assert result.exit_code == 0
        assert "Do you want to proceed with the import?" not in result.stdout
        assert "Import execution completed" in result.stdout


class TestImportCommandHelp:
    """Test import command help"""

    def test_help_shows_usage(self):
        """Test that help shows usage information"""
        result = runner.invoke(app, ["import", "import", "--help"])

        assert result.exit_code == 0
        assert "Import a capsule" in result.stdout
        assert "capsule_path" in result.stdout or "CAPSULE_PATH" in result.stdout

    def test_help_shows_options(self):
        """Test that help shows available options"""
        result = runner.invoke(app, ["import", "import", "--help"])

        assert result.exit_code == 0
        assert "--target" in result.stdout or "-t" in result.stdout
        assert "--no-backup" in result.stdout

    def test_help_shows_examples(self):
        """Test that help includes examples"""
        result = runner.invoke(app, ["import", "import", "--help"])

        assert result.exit_code == 0
        # Examples section exists
        assert "Example" in result.stdout or "capsule import" in result.stdout


class TestImportCommandValidation:
    """Test import command validation behavior"""

    def test_import_invalid_capsule(self, mock_config_file, temp_dir):
        """Test error when capsule is invalid"""
        # Create capsule without cypher
        invalid_capsule = temp_dir / "invalid_capsule"
        invalid_capsule.mkdir()
        (invalid_capsule / "dummy.txt").write_text("test")

        result = runner.invoke(app, ["import", "import", str(invalid_capsule), "--no-backup"])

        assert result.exit_code == 1
        # Check output (stdout + stderr)
        assert "Error" in result.stdout or "Error" in str(result.stderr)

    def test_import_shows_validation_success(self, mock_config_file, sample_capsule):
        """Test that validation success is reported"""
        result = runner.invoke(app, ["import", "import", str(sample_capsule), "--no-backup"], input="y\n")

        assert result.exit_code == 0
        # Check for validation elements
        assert "validation" in result.stdout.lower() or "Validating" in result.stdout
