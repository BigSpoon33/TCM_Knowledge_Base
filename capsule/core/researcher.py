# capsule/core/researcher.py
from abc import ABC, abstractmethod
from typing import Dict, List
from ..utils.exceptions import NetworkError, ConfigError
import google.generativeai as genai
from ..models.config import Config
from ..models.citation import Citation
from ..models.research import ResearchResult


class ResearchProvider(ABC):
    """Abstract base for research providers"""

    @abstractmethod
    def research(self, topic: str, max_sources: int = 10) -> ResearchResult:
        """
        Performs research on a given topic.

        Args:
            topic: The topic to research.
            max_sources: The maximum number of sources to consult.

        Returns:
            A dictionary containing the research content, citations, and metadata.
            Example: {
                "content": "...",
                "citations": [...],
                "metadata": {...}
            }
        """
        pass


class GeminiResearchProvider(ResearchProvider):
    """A research provider that uses the Google Gemini API."""

    def __init__(self):
        self.config = Config()
        api_key = self.config.get("research.api_key")
        if not api_key:
            raise ConfigError("Gemini API key is not set in the configuration.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    def research(self, topic: str, max_sources: int = 10) -> Dict:
        """
        Performs research using the Gemini API.
        """
        prompt = f"Perform a comprehensive research on the topic: '{topic}'. Synthesize information from multiple sources and provide a detailed summary. Also, include a list of citations for the sources used."

        try:
            response = self.model.generate_content(prompt)

            content = response.text
            citations = self._parse_citations(response)
            metadata = {"provider": "gemini"}

            return ResearchResult(content=content, citations=citations, metadata=metadata)
        except Exception as e:
            raise NetworkError(f"An error occurred while calling the Gemini API: {e}") from e

    def _parse_citations(self, response) -> List[Citation]:
        """Parses citation metadata from the Gemini API response."""
        citations = []
        if hasattr(response, "citation_metadata") and response.citation_metadata:
            for source in response.citation_metadata.citation_sources:
                citations.append(
                    Citation(
                        title=getattr(source, "title", "N/A"),
                        url=getattr(source, "uri", "N/A"),
                        source_name=getattr(source, "publication", "N/A"),
                    )
                )
        return citations


class DummyResearchProvider(ResearchProvider):
    """A dummy research provider for testing or when research is skipped."""

    def research(self, topic: str, max_sources: int = 10) -> ResearchResult:
        return ResearchResult(
            content=f"Content for {topic} (Research Skipped)",
            citations=[],
            metadata={
                "provider": "dummy",
                "question": f"What is {topic}?",
                "answer": f"{topic} is a subject of study.",
                "title": f"{topic} Quiz",
                "questions": [
                    {"text": f"Is {topic} real?", "options": ["Yes", "No", "Maybe"]},
                    {"text": f"Is {topic} important?", "options": ["Very", "Somewhat", "Not at all"]},
                ],
            },
        )
