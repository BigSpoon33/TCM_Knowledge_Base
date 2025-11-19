# capsule/models/research.py
from dataclasses import dataclass
from typing import Dict, List
from .citation import Citation

@dataclass
class ResearchResult:
    """Represents the result of a research task."""
    content: str
    citations: List[Citation]
    metadata: Dict
