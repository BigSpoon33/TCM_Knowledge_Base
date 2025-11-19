from pathlib import Path
from typing import List, Tuple, Optional
import difflib
import os

def get_all_patterns(directory: Path) -> List[str]:
    """Returns a list of all markdown files in a directory."""
    patterns = []
    for p in directory.rglob("*.md"):
        patterns.append(p.stem)
    return patterns

def validate_pattern_exists(pattern_name: str, patterns_dir: Path) -> Tuple[bool, Optional[str], List[str]]:
    """
    Validates if a pattern exists, offering suggestions for typos.
    Returns (exists, matched_pattern, suggestions).
    """
    all_patterns = get_all_patterns(patterns_dir)
    if not all_patterns:
        return False, None, []

    # Case-insensitive check
    pattern_lower = pattern_name.lower()
    all_patterns_lower = [p.lower() for p in all_patterns]

    if pattern_lower in all_patterns_lower:
        # Find the original cased version
        idx = all_patterns_lower.index(pattern_lower)
        return True, all_patterns[idx], []

    # Suggest similar patterns
    suggestions = difflib.get_close_matches(pattern_lower, all_patterns_lower, n=5, cutoff=0.6)
    # Get original cased versions of suggestions
    suggestions_cased = [all_patterns[all_patterns_lower.index(s)] for s in suggestions]
    return False, None, suggestions_cased

def validate_api_key(api_key: Optional[str]) -> Tuple[bool, str]:
    """Validates the Gemini API key."""
    if not api_key:
        return False, "GEMINI_API_KEY not set in config or environment."
    return True, ""

def find_script_path(script_name: str, scripts_dir: Path) -> Optional[Path]:
    """Finds the path to a script in the scripts directory."""
    script_path = scripts_dir / f"{script_name}.py"
    return script_path if script_path.exists() else None

class Validator:
    def validate(self, content: str) -> bool:
        return True
