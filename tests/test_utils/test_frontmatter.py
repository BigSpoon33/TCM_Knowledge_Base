import pytest
from pathlib import Path
from capsule.utils.frontmatter import FrontmatterHandler


class TestFrontmatterHandler:
    def test_init_empty(self):
        handler = FrontmatterHandler()
        assert handler.get_body() == ""
        # ruamel.yaml load("{}") returns an empty CommentedMap which equals {}
        assert handler.get_frontmatter() == {}

    def test_init_with_content(self):
        content = "---\nkey: value\n---\nBody"
        handler = FrontmatterHandler(content)
        assert handler.get_body() == "Body"
        assert handler.get_frontmatter()["key"] == "value"

    def test_round_trip_complex(self, tmp_path):
        # Read fixture
        fixture_path = Path("tests/fixtures/sample_notes/complex_note.md")
        if not fixture_path.exists():
            pytest.skip("Fixture not found")

        original_content = fixture_path.read_text(encoding="utf-8")

        # Load
        handler = FrontmatterHandler(original_content)

        # Verify some data
        fm = handler.get_frontmatter()
        assert fm["id"] == "complex-note-001"
        assert fm["herb_data"]["temperature"] == "warm"

        # Save to new file
        output_path = tmp_path / "output.md"
        handler.save(output_path)

        # Read back
        saved_content = output_path.read_text(encoding="utf-8")

        # Assert identical
        # Note: There might be slight differences in whitespace if original file
        # didn't match exactly what ruamel outputs (e.g. indentation of lists).
        # But since we want to preserve, we hope ruamel keeps it.
        # If the fixture was written BY HAND, it might differ from ruamel's default style.
        # However, ruamel.yaml is designed to preserve existing style.
        assert saved_content == original_content

    def test_get_set_interface(self):
        handler = FrontmatterHandler("---\nkey: old\n---\nBody")

        # Get
        fm = handler.get_frontmatter()
        assert fm["key"] == "old"
        assert handler.get_body() == "Body"

        # Set
        fm["key"] = "new"
        fm["added"] = "value"
        handler.set_frontmatter(fm)
        handler.set_body("New Body")

        # Verify string output
        output = handler.to_string()
        assert "key: new" in output
        assert "added: value" in output
        assert "New Body" in output
        # Old body should be gone
        assert output.endswith("New Body")

    def test_no_frontmatter(self):
        content = "Just body content"
        handler = FrontmatterHandler(content)
        assert handler.get_body() == "Just body content"
        assert handler.get_frontmatter() == {}  # Empty dict

        # Save should not add frontmatter if empty
        assert handler.to_string() == "Just body content"

        # Add frontmatter
        fm = handler.get_frontmatter()
        fm["title"] = "Added"
        handler.set_frontmatter(fm)

        output = handler.to_string()
        assert "---\n" in output
        assert "title: Added" in output
