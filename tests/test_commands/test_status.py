from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from capsule.cli import app
from capsule.models.cypher import CapsuleCypher

runner = CliRunner()


@pytest.fixture
def mock_status_service():
    with patch("capsule.commands.status.Status") as MockStatus:
        yield MockStatus


@pytest.fixture
def mock_config():
    with patch("capsule.commands.status.Config") as MockConfig:
        yield MockConfig


def test_status_command_no_vault_path(mock_config):
    """Test status command when vault path is not configured"""
    mock_config.load_config.return_value.user = {}

    result = runner.invoke(app, ["status"])

    assert result.exit_code == 1
    assert "Vault path not configured" in result.stdout


def test_status_command_success(mock_config, mock_status_service):
    """Test status command with valid configuration and capsules"""
    # Mock config
    mock_config.load_config.return_value.user = {"vault_path": "/tmp/vault"}

    # Mock status service
    mock_instance = mock_status_service.return_value
    mock_instance.get_vault_summary.return_value = {
        "capsule_count": 1,
        "capsules": [
            CapsuleCypher(
                capsule_id="test-capsule",
                name="Test Capsule",
                version="1.0.0",
                domain_type="test",
                folder_structure={},
                contents={},
                data_schemas={},
            )
        ],
    }

    result = runner.invoke(app, ["status"])

    assert result.exit_code == 0
    assert "Vault Status" in result.stdout
    assert "Installed Capsules: 1" in result.stdout
    assert "test-capsule" in result.stdout
    assert "Test Capsule" in result.stdout


def test_status_command_no_capsules(mock_config, mock_status_service):
    """Test status command when no capsules are installed"""
    # Mock config
    mock_config.load_config.return_value.user = {"vault_path": "/tmp/vault"}

    # Mock status service
    mock_instance = mock_status_service.return_value
    mock_instance.get_vault_summary.return_value = {"capsule_count": 0, "capsules": []}

    result = runner.invoke(app, ["status"])

    assert result.exit_code == 0
    assert "Installed Capsules: 0" in result.stdout
    assert "No capsules found" in result.stdout


def test_status_e2e(temp_dir):
    """E2E test for status command with real file system"""
    # Create a fake vault
    vault_path = temp_dir / "vault"
    vault_path.mkdir()

    # Create a fake capsule
    capsule_path = vault_path / "test_capsule"
    capsule_path.mkdir()

    cypher_content = """
capsule_id: test-capsule-e2e
name: E2E Test Capsule
version: 1.0.0
domain_type: test
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
    result = runner.invoke(app, ["--config-path", str(config_path), "status"])

    assert result.exit_code == 0
    assert "Vault Status" in result.stdout
    assert "Installed Capsules: 1" in result.stdout
    assert "test-capsule-e2e" in result.stdout
