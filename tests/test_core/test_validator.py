import pytest
from unittest.mock import Mock
from capsule.core.validator import Validator
import tempfile
from pathlib import Path
import yaml

@pytest.fixture
def validator():
    return Validator()

def test_validate_capsule_calls_all_validation_methods(validator):
    capsule = Mock()
    capsule.path = Path('.')
    (capsule.path / 'capsule-cypher.yaml').touch()
    validator.validate_capsule_structure = Mock()
    validator.validate_frontmatter_schema = Mock()
    validator.validate_file_inventory = Mock()
    validator.validate_data_types = Mock()

    validator.validate_capsule(capsule)

    validator.validate_capsule_structure.assert_called_once()
    validator.validate_frontmatter_schema.assert_called_once()
    validator.validate_file_inventory.assert_called_once()
    validator.validate_data_types.assert_called_once()

def test_validate_capsule_with_valid_capsule(validator):
    with tempfile.TemporaryDirectory() as temp_dir:
        capsule_path = Path(temp_dir)
        
        # Create a mock capsule object with a path attribute
        class MockCapsule:
            def __init__(self, path):
                self.path = path
        
        mock_capsule = MockCapsule(capsule_path)

        # Create capsule-cypher.yaml
        cypher_data = {
            'capsule_id': 'temp-capsule',
            'name': 'Test Capsule',
            'version': '1.0.0',
            'domain_type': 'education',
            'folder_structure': {'root_notes': 'root_notes'},
            'contents': {'root_notes': [{'file': 'root_notes/test.md', 'id': 'test-1'}]}
        }
        with open(capsule_path / 'capsule-cypher.yaml', 'w') as f:
            yaml.dump(cypher_data, f)

        # Create content file
        (capsule_path / 'root_notes').mkdir()
        with open(capsule_path / 'root_notes' / 'test.md', 'w') as f:
            f.write('test content')

        validator.validate_capsule(mock_capsule)

def test_validate_capsule_with_invalid_cypher(validator):
    with tempfile.TemporaryDirectory() as temp_dir:
        capsule_path = Path(temp_dir)
        
        class MockCapsule:
            def __init__(self, path):
                self.path = path
        
        mock_capsule = MockCapsule(capsule_path)

        cypher_data = {
            'capsule_id': 'temp-capsule',
            'name': 'Test Capsule',
            'version': '1.0',
            'domain_type': 'education',
            'folder_structure': {'root_notes': 'root_notes'},
            'contents': {'root_notes': [{'file': 'root_notes/test.md', 'id': 'test-1'}]}
        }
        with open(capsule_path / 'capsule-cypher.yaml', 'w') as f:
            yaml.dump(cypher_data, f)

        (capsule_path / 'root_notes').mkdir()
        with open(capsule_path / 'root_notes' / 'test.md', 'w') as f:
            f.write('test content')

        with pytest.raises(ValueError):
            validator.validate_capsule(mock_capsule)

def test_validate_capsule_with_extra_file(validator):
    with tempfile.TemporaryDirectory() as temp_dir:
        capsule_path = Path(temp_dir)
        
        class MockCapsule:
            def __init__(self, path):
                self.path = path
        
        mock_capsule = MockCapsule(capsule_path)

        cypher_data = {
            'capsule_id': 'temp-capsule',
            'name': 'Test Capsule',
            'version': '1.0.0',
            'domain_type': 'education',
            'folder_structure': {'root_notes': 'root_notes'},
            'contents': {'root_notes': []}
        }
        with open(capsule_path / 'capsule-cypher.yaml', 'w') as f:
            yaml.dump(cypher_data, f)

        (capsule_path / 'root_notes').mkdir()
        with open(capsule_path / 'root_notes' / 'test.md', 'w') as f:
            f.write('test content')

        # This should pass, as we are not validating for extra files yet.
        validator.validate_capsule(mock_capsule)
