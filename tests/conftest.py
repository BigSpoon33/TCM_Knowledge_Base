"""Pytest configuration and fixtures for capsule tests"""

import tempfile
from pathlib import Path

import pytest

from capsule.core.researcher import DummyResearchProvider
from capsule.models.config import Config


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing"""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_config():
    """Return a default configuration for testing"""
    return Config(
        llm_provider="dummy",
        api_key="test_key",
        default_model="test-model",
        project_dir=Path("/tmp/test_project"),
    )


@pytest.fixture
def mock_researcher():
    """Return a dummy researcher for testing"""
    return DummyResearchProvider()


@pytest.fixture
def sample_capsule_path(temp_dir):
    """Create a sample capsule structure in a temporary directory"""
    capsule_dir = temp_dir / "Test_Capsule"
    capsule_dir.mkdir()

    # Create some content files
    (capsule_dir / "Root_Note_Test_Capsule.md").write_text("# Test Capsule\n\nContent")
    (capsule_dir / "Test_Capsule_Flashcards.md").write_text("# Flashcards\n\nQ: A?\nA: B")

    # Create cypher
    (capsule_dir / "capsule-cypher.yaml").write_text("""
capsule_id: test_capsule
version: 0.1.0
domain_type: general
contents:
  root:
    - Root_Note_Test_Capsule.md
    - Test_Capsule_Flashcards.md
""")

    return capsule_dir
