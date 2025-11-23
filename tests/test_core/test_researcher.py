# tests/test_core/test_researcher.py
from unittest.mock import MagicMock, patch

import pytest

from capsule.core.researcher import GeminiResearchProvider
from capsule.models.citation import Citation
from capsule.models.research import ResearchResult
from capsule.utils.exceptions import ConfigError, NetworkError


@patch("capsule.core.researcher.Config")
@patch("capsule.core.researcher.genai")
def test_gemini_provider_success_with_citations(mock_genai, mock_config):
    """Test the GeminiResearchProvider with a successful API call and citation parsing."""
    # Mock the Config
    config_instance = MagicMock()
    config_instance.get.return_value = "test_api_key"
    mock_config.load_config.return_value = config_instance

    # Mock the Gemini API response
    mock_model = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "Gemini research content"

    # Simulate citation_metadata
    mock_citation_source = MagicMock()
    mock_citation_source.title = "Source 1"
    mock_citation_source.uri = "http://example.com/1"
    mock_citation_source.publication = "TestSource1"

    mock_citation_metadata = MagicMock()
    mock_citation_metadata.citation_sources = [mock_citation_source]
    mock_response.citation_metadata = mock_citation_metadata

    mock_model.generate_content.return_value = mock_response
    mock_genai.GenerativeModel.return_value = mock_model

    provider = GeminiResearchProvider()
    result = provider.research("test topic")

    assert isinstance(result, ResearchResult)
    assert result.content == "Gemini research content"
    assert len(result.citations) == 1
    assert isinstance(result.citations[0], Citation)
    assert result.citations[0].title == "Source 1"
    assert result.citations[0].url == "http://example.com/1"
    assert result.citations[0].source_name == "TestSource1"
    mock_genai.configure.assert_called_with(api_key="test_api_key")
    mock_model.generate_content.assert_called_once()


@patch("capsule.core.researcher.Config")
@patch("capsule.core.researcher.genai")
def test_gemini_provider_api_error(mock_genai, mock_config):
    """Test the GeminiResearchProvider with a failed API call."""
    config_instance = MagicMock()
    config_instance.get.return_value = "test_api_key"
    mock_config.load_config.return_value = config_instance

    mock_model = MagicMock()
    mock_model.generate_content.side_effect = Exception("API Error")
    mock_genai.GenerativeModel.return_value = mock_model

    provider = GeminiResearchProvider()
    with pytest.raises(NetworkError, match="API Error"):
        provider.research("test topic")


@patch("capsule.core.researcher.Config")
def test_gemini_provider_no_api_key(mock_config):
    """Test that a ConfigError is raised if the API key is missing."""
    config_instance = MagicMock()
    config_instance.get.return_value = None
    mock_config.load_config.return_value = config_instance

    with pytest.raises(ConfigError, match="Gemini API key is not set"):
        GeminiResearchProvider()
