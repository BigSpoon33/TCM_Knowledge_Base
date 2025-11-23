import pytest
import frontmatter
from pathlib import Path
from capsule.core.importer import Importer
from capsule.models.capsule import Capsule
from capsule.models.config import Config


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
def sample_capsule():
    return Capsule(
        capsule_id="TCM_Herbs_v1",
        name="TCM Herbs",
        version="1.0.0",
        domain_type="traditional_chinese_medicine",
        dashboard_metadata={"active": True, "class": "NewClass"},
    )


class TestDashboardGeneration:
    def test_load_domain_sections_tcm(self, mock_config):
        """Test loading TCM domain sections"""
        importer = Importer(mock_config)
        content = importer.load_domain_sections("traditional_chinese_medicine", "TCM_Herbs_v1")

        assert "### Formulas" in content
        assert "### Herbs" in content
        assert "### Patterns" in content
        assert "TCM_Herbs_v1" in content  # Check if capsule_id is used in queries

    def test_load_domain_sections_unknown(self, mock_config):
        """Test loading unknown domain sections"""
        importer = Importer(mock_config)
        content = importer.load_domain_sections("unknown_domain", "test_id")
        assert content == ""

    def test_generate_dashboards(self, mock_config, sample_capsule):
        """Test generating dashboards"""
        importer = Importer(mock_config)
        vault_path = Path(mock_config.get("user.vault_path"))

        generated_files = importer.generate_dashboards(sample_capsule, vault_path)

        assert len(generated_files) == 2

        capsule_dashboard = vault_path / "TCM_Herbs_v1" / "capsule-dashboard.md"
        assert capsule_dashboard.exists()
        content = capsule_dashboard.read_text()
        assert "Capsule Dashboard: TCM Herbs" in content
        assert "### Formulas" in content  # Domain section

        master_dashboard = vault_path / "Master Dashboard.md"
        assert master_dashboard.exists()
        master_content = master_dashboard.read_text()
        assert "Master Dashboard" in master_content

    def test_generate_dashboards_master_exists(self, mock_config, sample_capsule):
        """Test generating dashboards when master dashboard already exists"""
        importer = Importer(mock_config)
        vault_path = Path(mock_config.get("user.vault_path"))

        # Create master dashboard
        master_dashboard = vault_path / "Master Dashboard.md"
        master_dashboard.write_text("Existing Content")

        generated_files = importer.generate_dashboards(sample_capsule, vault_path)

        # Should only generate capsule dashboard
        assert len(generated_files) == 1
        assert generated_files[0].name == "capsule-dashboard.md"

        # Master dashboard should not be overwritten
        assert master_dashboard.read_text() == "Existing Content"

    def test_generate_dashboards_merge_metadata(self, mock_config, sample_capsule):
        """Test that dashboard metadata is updated during merge"""
        importer = Importer(mock_config)
        vault_path = Path(mock_config.get("user.vault_path"))

        # Create existing dashboard with old metadata
        capsule_dir = vault_path / "TCM_Herbs_v1"
        capsule_dir.mkdir(parents=True, exist_ok=True)

        existing_content = """---
type: capsule_dashboard
capsule_id: TCM_Herbs_v1
version: 0.9.0
dashboard_metadata:
  active: false
  class: OldClass
source_capsules: ["TCM_Herbs_v1"]
---
# Old Content
"""
        (capsule_dir / "capsule-dashboard.md").write_text(existing_content)

        # Run generation
        importer.generate_dashboards(sample_capsule, vault_path)

        # Verify merge
        capsule_dashboard = capsule_dir / "capsule-dashboard.md"
        content = capsule_dashboard.read_text()
        post = frontmatter.loads(content)

        # Check updated fields
        assert post.metadata["version"] == "1.0.0"
        assert post.metadata["dashboard_metadata"]["active"] is True
        assert post.metadata["dashboard_metadata"]["class"] == "NewClass"

        # Check preserved content
        assert "# Old Content" in post.content

    def test_generate_dashboards_rollback(self, mock_config, sample_capsule, monkeypatch):
        """Test rollback when dashboard generation fails"""
        importer = Importer(mock_config)
        vault_path = Path(mock_config.get("user.vault_path"))

        # Mock load_domain_sections to succeed
        monkeypatch.setattr(importer, "load_domain_sections", lambda *args: "Domain Content")

        # Mock Environment.get_template to fail for Master Dashboard
        # We need to let it succeed for capsule-dashboard but fail for master-dashboard
        # This is tricky to mock at Environment level easily without a custom mock class

        # Instead, let's mock the write operation for Master Dashboard to fail
        # But generate_dashboards calls write_text on Path object.
        # We can mock Path.write_text? No, that affects all writes.

        # Let's mock the template render for Master Dashboard to raise exception
        from jinja2 import Environment

        original_get_template = Environment.get_template

        def mock_get_template(self, name, *args, **kwargs):
            if name == "master-dashboard.md.j2":
                raise Exception("Simulated generation failure")
            return original_get_template(self, name, *args, **kwargs)

        monkeypatch.setattr(Environment, "get_template", mock_get_template)

        # Run generation
        with pytest.raises(Exception, match="Simulated generation failure"):
            importer.generate_dashboards(sample_capsule, vault_path)

        # Verify rollback
        # Capsule dashboard should have been created then deleted
        capsule_dashboard = vault_path / "TCM_Herbs_v1" / "capsule-dashboard.md"
        assert not capsule_dashboard.exists()
