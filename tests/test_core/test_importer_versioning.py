import pytest
from pathlib import Path
import shutil
from capsule.core.importer import Importer, ImportPreview
from capsule.models.config import Config
from capsule.models.cypher import CapsuleCypher


@pytest.fixture
def mock_config(temp_dir):
    """Create a mock config with temp vault path"""
    vault_path = temp_dir / "test_vault"
    vault_path.mkdir(parents=True, exist_ok=True)

    config = Config(
        llm_provider="openai",
        api_key="test-key",
        default_model="gpt-4-turbo",
        project_dir=temp_dir,
        user={"name": "Test User", "vault_path": str(vault_path)},
        research={},
    )
    return config


@pytest.fixture
def sample_capsule_folder(temp_dir):
    """Create a sample capsule folder for testing"""
    capsule_path = temp_dir / "test_capsule_v2"
    capsule_path.mkdir()

    # Create capsule-cypher.yaml (v2.0.0)
    cypher_content = """capsule_id: "test_capsule"
name: "Test Capsule"
version: "2.0.0"
domain_type: "education"
folder_structure: {}
contents: {}
data_schemas: {}
"""
    (capsule_path / "capsule-cypher.yaml").write_text(cypher_content)
    return capsule_path


class TestImporterVersioning:
    """Test Importer version detection logic"""

    def test_analyze_new_install(self, mock_config, sample_capsule_folder):
        """Test analysis when no version is installed"""
        importer = Importer(mock_config)
        importer.extracted_path = sample_capsule_folder
        importer.load_cypher()

        vault_path = Path(mock_config.get("user.vault_path"))
        preview = importer.analyze_impact(vault_path)

        assert preview.import_type == "NEW"
        assert preview.version_diff is None

    def test_analyze_update(self, mock_config, sample_capsule_folder):
        """Test analysis when updating (v1.0.0 -> v2.0.0)"""
        vault_path = Path(mock_config.get("user.vault_path"))
        capsule_dir = vault_path / "test_capsule"
        capsule_dir.mkdir(parents=True, exist_ok=True)

        # Install v1.0.0 cypher in vault
        installed_cypher = """capsule_id: "test_capsule"
name: "Test Capsule"
version: "1.0.0"
domain_type: "education"
folder_structure: {}
contents: {}
data_schemas: {}
"""
        (capsule_dir / "capsule-cypher.yaml").write_text(installed_cypher)

        importer = Importer(mock_config)
        importer.extracted_path = sample_capsule_folder
        importer.load_cypher()

        preview = importer.analyze_impact(vault_path)

        assert preview.import_type == "UPDATE"
        assert preview.version_diff == "1.0.0 -> 2.0.0"

    def test_analyze_downgrade(self, mock_config, sample_capsule_folder):
        """Test analysis when downgrading (v3.0.0 -> v2.0.0)"""
        vault_path = Path(mock_config.get("user.vault_path"))
        capsule_dir = vault_path / "test_capsule"
        capsule_dir.mkdir(parents=True, exist_ok=True)

        # Install v3.0.0 cypher in vault
        installed_cypher = """capsule_id: "test_capsule"
name: "Test Capsule"
version: "3.0.0"
domain_type: "education"
folder_structure: {}
contents: {}
data_schemas: {}
"""
        (capsule_dir / "capsule-cypher.yaml").write_text(installed_cypher)

        importer = Importer(mock_config)
        importer.extracted_path = sample_capsule_folder
        importer.load_cypher()

        preview = importer.analyze_impact(vault_path)

        assert preview.import_type == "DOWNGRADE"
        assert preview.version_diff == "3.0.0 -> 2.0.0"

    def test_analyze_same_version(self, mock_config, sample_capsule_folder):
        """Test analysis when reinstalling same version (v2.0.0 -> v2.0.0)"""
        vault_path = Path(mock_config.get("user.vault_path"))
        capsule_dir = vault_path / "test_capsule"
        capsule_dir.mkdir(parents=True, exist_ok=True)

        # Install v2.0.0 cypher in vault
        installed_cypher = """capsule_id: "test_capsule"
name: "Test Capsule"
version: "2.0.0"
domain_type: "education"
folder_structure: {}
contents: {}
data_schemas: {}
"""
        (capsule_dir / "capsule-cypher.yaml").write_text(installed_cypher)

        importer = Importer(mock_config)
        importer.extracted_path = sample_capsule_folder
        importer.load_cypher()

        preview = importer.analyze_impact(vault_path)

        assert preview.import_type == "SAME"
        assert "2.0.0 (Reinstall)" in preview.version_diff

    def test_analyze_different_capsule_id(self, mock_config, sample_capsule_folder):
        """Test analysis when installed cypher has different ID"""
        vault_path = Path(mock_config.get("user.vault_path"))
        capsule_dir = vault_path / "test_capsule"
        capsule_dir.mkdir(parents=True, exist_ok=True)

        # Install different capsule cypher in the expected folder (simulating corruption/mismatch)
        installed_cypher = """capsule_id: "other_capsule"
name: "Other Capsule"
version: "1.0.0"
domain_type: "education"
folder_structure: {}
contents: {}
data_schemas: {}
"""
        (capsule_dir / "capsule-cypher.yaml").write_text(installed_cypher)

        importer = Importer(mock_config)
        importer.extracted_path = sample_capsule_folder
        importer.load_cypher()

        preview = importer.analyze_impact(vault_path)

        # Should be treated as NEW because IDs don't match
        assert preview.import_type == "NEW"
        assert preview.version_diff is None
