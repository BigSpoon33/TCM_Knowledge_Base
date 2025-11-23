import pytest
from typer.testing import CliRunner
from capsule.cli import app

runner = CliRunner()


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


def test_validate_command_success(valid_capsule):
    result = runner.invoke(app, ["validate", str(valid_capsule)])

    if result.exit_code != 0:
        print(f"Output: {result.stdout}")
        print(f"Exception: {result.exception}")

    assert result.exit_code == 0
    assert "Validation Successful" in result.stdout


def test_validate_command_failure(invalid_capsule):
    result = runner.invoke(app, ["validate", str(invalid_capsule)])

    assert result.exit_code == 1
    assert "Validation Failed" in result.stdout
    assert "capsule-cypher.yaml not found" in result.stdout


def test_validate_command_invalid_structure(tmp_path):
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
    assert "Validation Failed" in result.stdout
    assert "Missing required fields" in result.stdout


def test_validate_command_file_not_found(tmp_path):
    non_existent = tmp_path / "non_existent"
    result = runner.invoke(app, ["validate", str(non_existent)])

    assert result.exit_code == 2
    # assert "does not exist" in result.stdout
