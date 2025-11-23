# tests/test_models/test_citation.py
from capsule.models.citation import Citation


def test_citation_instantiation():
    """Test that a Citation object can be instantiated correctly."""
    citation = Citation(title="Test Title", url="http://example.com", source_name="Test Source")
    assert citation.title == "Test Title"
    assert citation.url == "http://example.com"
    assert citation.source_name == "Test Source"
