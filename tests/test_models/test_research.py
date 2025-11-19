# tests/test_models/test_research.py
import pytest
from capsule.models.research import ResearchResult
from capsule.models.citation import Citation

def test_research_result_instantiation():
    """Test that a ResearchResult object can be instantiated correctly."""
    citation = Citation(
        title="Test Title",
        url="http://example.com",
        source_name="Test Source"
    )
    result = ResearchResult(
        content="Test content",
        citations=[citation],
        metadata={"provider": "test"}
    )
    assert result.content == "Test content"
    assert len(result.citations) == 1
    assert result.citations[0].title == "Test Title"
    assert result.metadata["provider"] == "test"
