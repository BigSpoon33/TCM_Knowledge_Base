# capsule/models/research.py
from dataclasses import dataclass

from .citation import Citation


@dataclass
class ResearchResult:
    """Represents the result of a research task."""

    content: str
    citations: list[Citation]
    metadata: dict
