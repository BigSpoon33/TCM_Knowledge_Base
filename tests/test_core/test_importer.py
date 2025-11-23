"""Tests for capsule/core/importer.py"""

import shutil
import zipfile
from pathlib import Path

import pytest

from capsule.core.importer import (
    CapsuleInfo,
    Impact,
    Importer,
    ImportPreview,
    UpdateDetail,
)
from capsule.models.config import Config


@pytest.fixture
def mock_config(temp_dir):
    """Create a mock config with temp vault path"""
    # Create vault directory
    vault_path = temp_dir / "test_vault"
    vault_path.mkdir(parents=True, exist_ok=True)

    # Create backup directory
    backup_dir = temp_dir / "backups"
    backup_dir.mkdir(parents=True, exist_ok=True)

    # Create config with proper structure matching Config dataclass
    config = Config(
        llm_provider="openai",
        api_key="test-key",
        default_model="gpt-4-turbo",
        project_dir=temp_dir,
        user={"name": "Test User", "vault_path": str(vault_path)},
        research={},
    )

    # Add import settings to user dict for backward compatibility
    config.user["import"] = {
        "auto_backup": False,
        "backup_location": str(backup_dir),
        "default_merge_strategy": "section-level",
    }

    return config


@pytest.fixture
def sample_capsule_folder(temp_dir):
    """Create a sample capsule folder for testing"""
    capsule_path = temp_dir / "test_capsule_v1"
    capsule_path.mkdir()

    # Create capsule-cypher.yaml
    cypher_content = """capsule_id: "test_capsule_v1"
name: "Test Capsule"
version: "1.0.0"
domain_type: "education"
folder_structure:
  root_notes: "notes/"
contents:
  root_notes:
    - file: "notes/test_note_1.md"
      id: "test-note-1"
    - file: "notes/test_note_2.md"
      id: "test-note-2"
data_schemas: {}
sequence_mode: "freeform"
"""
    (capsule_path / "capsule-cypher.yaml").write_text(cypher_content)

    # Create notes directory and sample notes
    notes_dir = capsule_path / "notes"
    notes_dir.mkdir()

    note1_content = """---
id: test-note-1
name: Test Note 1
type: root_note
tags: [test]
created: 2025-11-15
updated: 2025-11-15
source_capsules: [test_capsule_v1]

test_data:
  field1: value1
---

# Test Note 1 Content
"""
    (notes_dir / "test_note_1.md").write_text(note1_content)

    note2_content = """---
id: test-note-2
name: Test Note 2
type: root_note
tags: [test]
created: 2025-11-15
updated: 2025-11-15
source_capsules: [test_capsule_v1]
---

# Test Note 2 Content
"""
    (notes_dir / "test_note_2.md").write_text(note2_content)

    return capsule_path


@pytest.fixture
def sample_capsule_zip(sample_capsule_folder, temp_dir):
    """Create a sample capsule zip file for testing"""
    zip_path = temp_dir / "test_capsule_v1.capsule"

    with zipfile.ZipFile(zip_path, "w") as zip_ref:
        for file_path in sample_capsule_folder.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(sample_capsule_folder.parent)
                zip_ref.write(file_path, arcname)

    return zip_path


class TestImporterInit:
    """Test Importer initialization"""

    def test_init_with_config(self, mock_config):
        """Test importer initializes with config"""
        importer = Importer(mock_config)
        assert importer.config == mock_config
        assert importer.extracted_path is None
        assert importer.temp_dir is None
        assert importer.cypher is None


class TestExtractCapsule:
    """Test capsule extraction"""

    def test_extract_from_folder(self, mock_config, sample_capsule_folder):
        """Test extracting from an already-extracted folder"""
        importer = Importer(mock_config)
        importer.extract_capsule(sample_capsule_folder)

        assert importer.extracted_path == sample_capsule_folder
        assert importer.temp_dir is None
        assert (importer.extracted_path / "capsule-cypher.yaml").exists()

    def test_extract_from_zip(self, mock_config, sample_capsule_zip):
        """Test extracting from a zip archive"""
        importer = Importer(mock_config)
        importer.extract_capsule(sample_capsule_zip)

        assert importer.extracted_path is not None
        assert importer.temp_dir is not None
        assert (importer.extracted_path / "capsule-cypher.yaml").exists()

        # Cleanup
        importer.cleanup()

    def test_extract_nonexistent_file(self, mock_config, temp_dir):
        """Test error when capsule file doesn't exist"""
        importer = Importer(mock_config)
        nonexistent = temp_dir / "nonexistent.capsule"

        with pytest.raises(FileNotFoundError, match="Capsule not found"):
            importer.extract_capsule(nonexistent)

    def test_extract_zip_without_cypher(self, mock_config, temp_dir):
        """Test error when zip doesn't contain cypher file"""
        # Create a zip without cypher
        zip_path = temp_dir / "invalid.capsule"
        with zipfile.ZipFile(zip_path, "w") as zip_ref:
            zip_ref.writestr("dummy.txt", "test")

        importer = Importer(mock_config)

        with pytest.raises(FileNotFoundError, match="No capsule-cypher.yaml found"):
            importer.extract_capsule(zip_path)

    def test_extract_zip_with_path_traversal(self, mock_config, temp_dir):
        """Test error when zip contains path traversal attempt"""
        zip_path = temp_dir / "traversal.capsule"
        with zipfile.ZipFile(zip_path, "w") as zip_ref:
            # Add a file with path traversal
            zip_ref.writestr("../evil.txt", "evil content")

        importer = Importer(mock_config)

        with pytest.raises(ValueError, match="Path traversal detected"):
            importer.extract_capsule(zip_path)


class TestLoadCypher:
    """Test cypher loading"""

    def test_load_valid_cypher(self, mock_config, sample_capsule_folder):
        """Test loading valid cypher file"""
        importer = Importer(mock_config)
        importer.extracted_path = sample_capsule_folder
        importer.load_cypher()

        assert importer.cypher is not None
        assert importer.cypher.capsule_id == "test_capsule_v1"
        assert importer.cypher.name == "Test Capsule"
        assert importer.cypher.version == "1.0.0"
        assert importer.cypher.domain_type == "education"

    def test_load_without_extraction(self, mock_config):
        """Test error when loading before extraction"""
        importer = Importer(mock_config)

        with pytest.raises(ValueError, match="Capsule must be extracted"):
            importer.load_cypher()

    def test_load_missing_cypher(self, mock_config, temp_dir):
        """Test error when cypher file is missing"""
        capsule_path = temp_dir / "no_cypher_capsule"
        capsule_path.mkdir()

        importer = Importer(mock_config)
        importer.extracted_path = capsule_path

        with pytest.raises(FileNotFoundError, match="capsule-cypher.yaml not found"):
            importer.load_cypher()


class TestValidateCapsule:
    """Test capsule validation"""

    def test_validate_valid_capsule(self, mock_config, sample_capsule_folder):
        """Test validation of valid capsule"""
        importer = Importer(mock_config)
        importer.extracted_path = sample_capsule_folder
        importer.load_cypher()

        # Should not raise any exceptions
        importer.validate_capsule()

    def test_validate_without_extraction(self, mock_config):
        """Test error when validating before extraction"""
        importer = Importer(mock_config)

        with pytest.raises(ValueError, match="Capsule must be extracted"):
            importer.validate_capsule()


class TestCollectCapsuleFiles:
    """Test file collection from cypher"""

    def test_collect_simple_list(self, mock_config, sample_capsule_folder):
        """Test collecting files from simple list structure"""
        importer = Importer(mock_config)
        importer.extracted_path = sample_capsule_folder
        importer.load_cypher()

        files = importer._collect_capsule_files()

        assert len(files) == 2
        assert "notes/test_note_1.md" in files
        assert "notes/test_note_2.md" in files

    def test_collect_nested_structure(self, mock_config, temp_dir):
        """Test collecting files from nested structure"""
        capsule_path = temp_dir / "nested_capsule"
        capsule_path.mkdir()

        # Create cypher with nested structure
        cypher_content = """capsule_id: "nested_v1"
name: "Nested Capsule"
version: "1.0.0"
domain_type: "education"
folder_structure:
  study_material: "study/"
contents:
  study_material:
    flashcards:
      - file: "study/flashcards/set1.md"
        id: "flash-1"
    quizzes:
      - file: "study/quizzes/quiz1.md"
        id: "quiz-1"
data_schemas: {}
"""
        (capsule_path / "capsule-cypher.yaml").write_text(cypher_content)

        importer = Importer(mock_config)
        importer.extracted_path = capsule_path
        importer.load_cypher()

        files = importer._collect_capsule_files()

        assert len(files) == 2
        assert "study/flashcards/set1.md" in files
        assert "study/quizzes/quiz1.md" in files


class TestAnalyzeImpact:
    """Test impact analysis"""

    def test_analyze_all_new_files(self, mock_config, sample_capsule_folder):
        """Test analysis when all files are new"""
        importer = Importer(mock_config)
        importer.extracted_path = sample_capsule_folder
        importer.load_cypher()

        vault_path = Path(mock_config.get("user.vault_path"))
        preview = importer.analyze_impact(vault_path)

        # 2 original files + 2 dashboards (capsule + master)
        assert preview.impact.new_files == 4
        assert preview.impact.updated_files == 0
        assert preview.impact.conflicts == 0
        assert len(preview.new_files) == 4

    def test_analyze_with_existing_files(self, mock_config, sample_capsule_folder):
        """Test analysis when some files exist in vault"""
        # Setup: copy one file to vault
        vault_path = Path(mock_config.get("user.vault_path"))
        vault_notes = vault_path / "notes"
        vault_notes.mkdir(parents=True, exist_ok=True)

        # Copy first note to vault with same capsule source
        source_note = sample_capsule_folder / "notes" / "test_note_1.md"
        dest_note = vault_notes / "test_note_1.md"
        shutil.copy(source_note, dest_note)

        # Run analysis
        importer = Importer(mock_config)
        importer.extracted_path = sample_capsule_folder
        importer.load_cypher()

        preview = importer.analyze_impact(vault_path)

        # 1 new note + 2 dashboards = 3 new files
        assert preview.impact.new_files == 3
        assert preview.impact.updated_files == 1
        assert preview.impact.conflicts == 0

    def test_analyze_with_conflicts(self, mock_config, sample_capsule_folder):
        """Test analysis with conflicting files"""
        # Setup: create conflicting note in vault
        vault_path = Path(mock_config.get("user.vault_path"))
        vault_notes = vault_path / "notes"
        vault_notes.mkdir(parents=True, exist_ok=True)

        # Create note from different capsule with same domain section
        conflicting_note = """---
id: test-note-1
name: Test Note 1
type: root_note
tags: [test]
source_capsules: [other_capsule_v1]

test_data:
  field1: other_value
---

# Different content
"""
        (vault_notes / "test_note_1.md").write_text(conflicting_note)

        # Run analysis
        importer = Importer(mock_config)
        importer.extracted_path = sample_capsule_folder
        importer.load_cypher()

        preview = importer.analyze_impact(vault_path)

        assert preview.impact.conflicts == 1
        assert len(preview.conflicts) == 1
        assert "test_data" in preview.conflicts[0].reason


class TestDetectSectionConflicts:
    """Test section conflict detection"""

    def test_no_conflicts(self, mock_config):
        """Test when there are no conflicting sections"""
        importer = Importer(mock_config)

        existing_fm = {"id": "test", "herb_data": {}}
        incoming_fm = {"id": "test", "recipe_data": {}}

        conflicts = importer._detect_section_conflicts(existing_fm, incoming_fm)

        assert len(conflicts) == 0

    def test_with_conflicts(self, mock_config):
        """Test when there are conflicting domain sections"""
        importer = Importer(mock_config)

        existing_fm = {"id": "test", "herb_data": {"temp": "warm"}}
        incoming_fm = {"id": "test", "herb_data": {"temp": "cool"}}

        conflicts = importer._detect_section_conflicts(existing_fm, incoming_fm)

        assert len(conflicts) == 1
        assert "herb_data" in conflicts

    def test_multiple_conflicts(self, mock_config):
        """Test detecting multiple conflicting sections"""
        importer = Importer(mock_config)

        existing_fm = {"id": "test", "herb_data": {}, "recipe_data": {}}
        incoming_fm = {"id": "test", "herb_data": {}, "recipe_data": {}}

        conflicts = importer._detect_section_conflicts(existing_fm, incoming_fm)

        assert len(conflicts) == 2
        assert "herb_data" in conflicts
        assert "recipe_data" in conflicts


class TestImportPreview:
    """Test ImportPreview data structure"""

    def test_create_preview(self):
        """Test creating ImportPreview object"""
        capsule_info = CapsuleInfo(
            id="test_v1",
            name="Test",
            version="1.0.0",
            domain_type="education",
            file_count=5,
        )
        impact = Impact(new_files=3, updated_files=2, conflicts=0)
        new_files = ["file1.md", "file2.md", "file3.md"]
        updates = [UpdateDetail(file="existing.md", strategy="section-level", changes="update")]
        conflicts = []

        preview = ImportPreview(capsule_info, impact, new_files, updates, conflicts)

        assert preview.capsule_info == capsule_info
        assert preview.impact == impact
        assert len(preview.new_files) == 3
        assert len(preview.updates) == 1
        assert len(preview.conflicts) == 0


class TestDisplayPreview:
    """Test preview display (basic verification)"""

    def test_display_preview_runs(self, mock_config, sample_capsule_folder):
        """Test that display_preview executes without error"""
        importer = Importer(mock_config)
        importer.extracted_path = sample_capsule_folder
        importer.load_cypher()

        vault_path = Path(mock_config.get("user.vault_path"))
        preview = importer.analyze_impact(vault_path)

        # Should not raise any exceptions
        importer.display_preview(preview)


class TestCleanup:
    """Test temporary directory cleanup"""

    def test_cleanup_temp_dir(self, mock_config, sample_capsule_zip):
        """Test that temporary directory is cleaned up"""
        importer = Importer(mock_config)
        importer.extract_capsule(sample_capsule_zip)

        temp_dir = importer.temp_dir
        assert Path(temp_dir).exists()

        importer.cleanup()

        assert not Path(temp_dir).exists()
        assert importer.temp_dir is None

    def test_cleanup_when_no_temp_dir(self, mock_config):
        """Test cleanup when there's no temp directory"""
        importer = Importer(mock_config)

        # Should not raise any exceptions
        importer.cleanup()
