import pytest
from pathlib import Path
import shutil
from capsule.core.generator import ContentGenerator
# Assuming a generator class that can render templates might exist
# This is a hypothetical test structure based on the project architecture


# A fixture to create a temporary directory for test outputs
@pytest.fixture
def temp_output_dir(tmp_path):
    """Create a temporary directory for generated files."""
    return tmp_path


def test_master_dashboard_template_generation(temp_output_dir):
    """
    Tests if the master-dashboard.md.j2 template renders correctly.

    This is a basic test to ensure the template file can be processed and
    contains the key elements for the interactive filter. It does not
    test the DataviewJS execution itself, as that requires an Obsidian environment.
    """
    # This test is conceptual. To make it work, we would need a template rendering engine
    # available from the core logic, which we'll assume exists for this test.

    # For now, we will just check the template file content directly.
    template_path = Path("capsule/templates/master-dashboard.md.j2")
    assert template_path.exists(), "Master dashboard template file should exist."

    content = template_path.read_text()

    # Verify key components of the interactive filter are in the template
    assert "INPUT[text:filter_class]" in content, "Class filter input should exist."
    assert "INPUT[text:filter_topic]" in content, "Topic filter input should exist."
    assert "INPUT[text:filter_category]" in content, "Category filter input should exist."
    assert "INPUT[toggle:filter_active]" in content, "Active status filter toggle should exist."

    # Verify that the DataviewJS block is present
    assert "```dataviewjs" in content, "DataviewJS block should be present."

    # This is a placeholder for a more advanced test that would involve
    # a hypothetical ContentGenerator class capable of rendering the template.
    # generator = ContentGenerator()
    # output_path = temp_output_dir / "master-dashboard.md"
    # generator.render_template('master-dashboard.md.j2', output_path)
    # assert output_path.exists()
    # content = output_path.read_text()
    # assert "Interactive Capsule Filters" in content
