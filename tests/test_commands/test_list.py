from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from capsule.cli import app
from capsule.models.cypher import CapsuleCypher

runner = CliRunner()


@pytest.fixture
def mock_list_service():
    """Mock the List service for unit tests."""
    with patch("capsule.commands.status.List") as MockList:
        yield MockList


@pytest.fixture
def mock_config():
    """Mock the Config for unit tests."""
    with patch("capsule.commands.status.Config") as MockConfig:
        yield MockConfig


def test_list_command_no_vault_path(mock_config):
    """Test list command when vault path is not configured."""
    mock_config.load_config.return_value.user = {}

    result = runner.invoke(app, ["list"])

    assert result.exit_code == 1
    assert "Vault path not configured" in result.stdout


def test_list_command_success(mock_config, mock_list_service):
    """Test list command with valid configuration and capsules."""
    # Mock config
    mock_config.load_config.return_value.user = {"vault_path": "/tmp/vault"}

    # Mock list service
    mock_instance = mock_list_service.return_value
    mock_instance.get_installed_capsules.return_value = [
        CapsuleCypher(
            capsule_id="test-capsule-1",
            name="Test Capsule 1",
            version="1.0.0",
            domain_type="test",
            folder_structure={},
            contents={},
            data_schemas={},
        ),
        CapsuleCypher(
            capsule_id="test-capsule-2",
            name="Test Capsule 2",
            version="2.0.0",
            domain_type="education",
            folder_structure={},
            contents={},
            data_schemas={},
        ),
    ]

    result = runner.invoke(app, ["list"])

    assert result.exit_code == 0
    assert "Installed Capsules" in result.stdout
    assert "(2 found)" in result.stdout
    assert "test-capsule-1" in result.stdout
    assert "1.0.0" in result.stdout
    assert "test-capsule-2" in result.stdout
    assert "2.0.0" in result.stdout


def test_list_command_no_capsules(mock_config, mock_list_service):
    """Test list command when no capsules are installed."""
    # Mock config
    mock_config.load_config.return_value.user = {"vault_path": "/tmp/vault"}

    # Mock list service
    mock_instance = mock_list_service.return_value
    mock_instance.get_installed_capsules.return_value = []

    result = runner.invoke(app, ["list"])

    assert result.exit_code == 0
    assert "No capsules found" in result.stdout


def test_list_e2e(temp_dir):
    """E2E test for list command with real file system."""
    # Create a fake vault
    vault_path = temp_dir / "vault"
    vault_path.mkdir()

    # Create fake capsules
    capsule1_path = vault_path / "test_capsule_1"
    capsule1_path.mkdir()
    cypher1_content = """
capsule_id: test-capsule-e2e-1
name: E2E Test Capsule 1
version: 1.0.0
domain_type: test
folder_structure: {}
contents: {}
data_schemas: {}
"""
    (capsule1_path / "capsule-cypher.yaml").write_text(cypher1_content, encoding="utf-8")

    capsule2_path = vault_path / "test_capsule_2"
    capsule2_path.mkdir()
    cypher2_content = """
capsule_id: test-capsule-e2e-2
name: E2E Test Capsule 2
version: 3.2.1
domain_type: education
folder_structure: {}
contents: {}
data_schemas: {}
"""
    (capsule2_path / "capsule-cypher.yaml").write_text(cypher2_content, encoding="utf-8")

    # Create a config file pointing to this vault
    config_path = temp_dir / "config.yaml"
    config_content = f"""
user:
  vault_path: {str(vault_path)}
"""
    config_path.write_text(config_content, encoding="utf-8")

    # Run command with config path
    result = runner.invoke(app, ["--config-path", str(config_path), "list"])

    assert result.exit_code == 0
    assert "Installed Capsules" in result.stdout
    assert "(2 found)" in result.stdout
    assert "test-capsule-e2e-1" in result.stdout
    assert "1.0.0" in result.stdout
    assert "test-capsule-e2e-2" in result.stdout
    assert "3.2.1" in result.stdout


def test_list_e2e_single_capsule(temp_dir):
    """E2E test for list command with a single capsule."""
    # Create a fake vault
    vault_path = temp_dir / "vault"
    vault_path.mkdir()

    # Create one fake capsule
    capsule_path = vault_path / "single_capsule"
    capsule_path.mkdir()
    cypher_content = """
capsule_id: single-test-capsule
name: Single Test Capsule
version: 0.1.0
domain_type: reference
folder_structure: {}
contents: {}
data_schemas: {}
"""
    (capsule_path / "capsule-cypher.yaml").write_text(cypher_content, encoding="utf-8")

    # Create a config file pointing to this vault
    config_path = temp_dir / "config.yaml"
    config_content = f"""
user:
  vault_path: {str(vault_path)}
"""
    config_path.write_text(config_content, encoding="utf-8")

    # Run command with config path
    result = runner.invoke(app, ["--config-path", str(config_path), "list"])

    assert result.exit_code == 0
    assert "Installed Capsules" in result.stdout
    assert "(1 found)" in result.stdout
    assert "single-test-capsule" in result.stdout
    assert "0.1.0" in result.stdout
