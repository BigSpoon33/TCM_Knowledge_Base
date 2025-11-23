# capsule/models/citation.py
from dataclasses import dataclass


@dataclass
class Citation:
    """Represents a citation for a piece of research."""

    title: str
    url: str
    source_name: str
