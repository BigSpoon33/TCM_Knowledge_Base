"""List available patterns command."""

from pathlib import Path

import typer

from ..utils.config import get_config
from ..utils.output import print_error, print_pattern_list, print_warning
from ..utils.validation import get_all_patterns

list_app = typer.Typer()


@list_app.command("patterns")
def list_patterns(category: str = typer.Option(None, "--category", "-c", help="Filter by category")):
    """List all available TCM patterns."""
    try:
        config = get_config()
        kb_path = Path(config.get("paths.knowledge_base", Path.cwd()))

        # Try to find patterns directory
        patterns_dir = kb_path / "TCM_Patterns"

        if not patterns_dir.exists():
            # Try alternative location
            patterns_dir = kb_path / "Materials" / "TCM_Patterns"

        if not patterns_dir.exists():
            print_error("Patterns directory not found", f"Expected: {patterns_dir}")
            raise typer.Abort()

        # Get patterns from main dir and subdirectories
        patterns = []

        # Check main directory
        patterns.extend(get_all_patterns(patterns_dir))

        # Check subdirectories (like "Zang Fu Patterns")
        for subdir in patterns_dir.iterdir():
            if subdir.is_dir() and not subdir.name.startswith("."):
                patterns.extend(get_all_patterns(subdir))

        if not patterns:
            print_warning("No patterns found")
            return

        # Filter by category if specified
        if category:
            category_lower = category.lower()
            patterns = [p for p in patterns if category_lower in p.lower()]

            if not patterns:
                print_warning(f"No patterns found in category: {category}")
                return

        print_pattern_list(patterns)

    except Exception as e:
        print_error(f"Failed to list patterns: {e}")
        raise typer.Abort()
