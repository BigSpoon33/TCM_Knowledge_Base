from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from capsule.cli import app
from capsule.exceptions import FileError, ValidationError

runner = CliRunner()


@pytest.fixture
def mock_validator():
    with patch("capsule.commands.validate.Validator") as mock:
        yield mock


def test_validate_command_success(mock_validator, tmp_path):
    """Test that the validate command calls the validator and exits with 0 on success."""
    # Setup mock
    instance = mock_validator.return_value
    instance.validate_capsule.return_value = None  # Success

    # Create a dummy directory so Typer validation passes
    dummy_dir = tmp_path / "dummy"
    dummy_dir.mkdir()

    # Run command
    result = runner.invoke(app, ["validate", str(dummy_dir)])

    # Assertions
    assert result.exit_code == 0
    assert "Validation Successful" in result.stdout
    mock_validator.assert_called_once()
    instance.validate_capsule.assert_called_once()


def test_validate_command_failure(mock_validator, tmp_path):
    """Test that the validate command handles validation errors correctly."""
    # Setup mock
    instance = mock_validator.return_value
    instance.validate_capsule.side_effect = ValidationError("Missing required field")

    # Create a dummy directory so Typer validation passes
    dummy_dir = tmp_path / "dummy"
    dummy_dir.mkdir()

    # Run command
    result = runner.invoke(app, ["validate", str(dummy_dir)])

    # Assertions
    assert result.exit_code == 1
    assert "Validation Failed" in result.stdout
    assert "Missing required field" in result.stdout


def test_validate_command_file_not_found(mock_validator, tmp_path):
    """Test that the validate command handles FileNotFoundError correctly."""
    # Setup mock
    instance = mock_validator.return_value
    instance.validate_capsule.side_effect = FileError("File not found")

    # Create a dummy directory so Typer validation passes
    dummy_dir = tmp_path / "dummy"
    dummy_dir.mkdir()

    # Run command
    result = runner.invoke(app, ["validate", str(dummy_dir)])

    # Assertions
    assert result.exit_code == 1
    assert "Validation Failed" in result.stdout
    assert "File not found" in result.stdout


def test_validate_command_unexpected_error(mock_validator, tmp_path):
    """Test that the validate command handles unexpected errors."""
    # Setup mock
    instance = mock_validator.return_value
    instance.validate_capsule.side_effect = Exception("Unexpected boom")

    # Create a dummy directory so Typer validation passes
    dummy_dir = tmp_path / "dummy"
    dummy_dir.mkdir()

    # Run command
    result = runner.invoke(app, ["validate", str(dummy_dir)])

    # Assertions
    assert result.exit_code == 1
    assert "An unexpected error occurred" in result.stdout
    assert "Unexpected boom" in result.stdout


# E2E Tests


@pytest.fixture
def valid_capsule(tmp_path):
    """Create a valid capsule structure."""
    capsule_dir = tmp_path / "valid_capsule"
    capsule_dir.mkdir()

    # Create capsule-cypher.yaml
    cypher_content = """
capsule_id: "test-capsule"
name: "Test Capsule"
version: "1.0.0"
domain_type: "test"
folder_structure:
  root: "."
contents:
  root_note: []
"""
    (capsule_dir / "capsule-cypher.yaml").write_text(cypher_content)
    return capsule_dir


@pytest.fixture
def invalid_capsule(tmp_path):
    """Create an invalid capsule (missing cypher)."""
    capsule_dir = tmp_path / "invalid_capsule"
    capsule_dir.mkdir()
    return capsule_dir


def test_e2e_validate_valid_capsule(valid_capsule):
    """E2E test for validating a valid capsule."""
    # We need to mock Validator because the real Validator might fail
    # if it checks for actual files referenced in cypher (which are empty list here, so maybe ok).
    # But let's try to use the REAL Validator if possible for E2E.
    # The Validator checks: structure, frontmatter, inventory.
    # My valid_capsule fixture is minimal.
    # Let's see if it passes the real Validator.

    # Validator checks:
    # 1. capsule-cypher.yaml exists (Yes)
    # 2. required fields in cypher (Yes)
    # 3. valid semver (Yes)
    # 4. frontmatter schema (No schema defined, so skips)
    # 5. file inventory (contents is empty list, so no files to check)
    # 6. extra files check (no extra files)

    result = runner.invoke(app, ["validate", str(valid_capsule)])
    if result.exit_code != 0:
        print(result.stdout)
    assert result.exit_code == 0
    assert "Validation Successful" in result.stdout


def test_e2e_validate_invalid_capsule(invalid_capsule):
    """E2E test for validating an invalid capsule (missing cypher)."""
    result = runner.invoke(app, ["validate", str(invalid_capsule)])
    assert result.exit_code == 1
    assert "Validation Failed" in result.stdout
    assert "capsule-cypher.yaml not found" in result.stdout


def test_e2e_validate_invalid_structure(tmp_path):
    """E2E test for validating a capsule with invalid structure (missing version)."""
    capsule_dir = tmp_path / "bad_structure"
    capsule_dir.mkdir()

    cypher_content = """
capsule_id: "test-capsule"
name: "Test Capsule"
# version missing
domain_type: "test"
folder_structure:
  root: "."
contents:
  root_note: []
"""
    (capsule_dir / "capsule-cypher.yaml").write_text(cypher_content)

    result = runner.invoke(app, ["validate", str(capsule_dir)])
    assert result.exit_code == 1
    assert "Missing required fields" in result.stdout
