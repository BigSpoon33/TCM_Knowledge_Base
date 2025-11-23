"""Rich terminal output helpers for Capsule."""

from typing import Any

from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TaskProgressColumn, TextColumn
from rich.table import Table

console = Console()


def print_header(title: str, subtitle: str | None = None) -> None:
    """Print a formatted header panel.

    Args:
        title: Main title
        subtitle: Optional subtitle
    """
    content = f"[bold]{title}[/bold]"
    if subtitle:
        content += f"\n\n{subtitle}"

    console.print(Panel(content, border_style="cyan"))


def print_success(message: str) -> None:
    """Print a success message.

    Args:
        message: Success message
    """
    console.print(f"[bold green]✅ {message}[/bold green]")


def print_error(message: str, hint: str | None = None) -> None:
    """Print an error message with optional hint.

    Args:
        message: Error message
        hint: Optional hint or suggestion
    """
    console.print(f"[bold red]❌ Error:[/bold red] {message}")
    if hint:
        console.print(f"[yellow]💡 Hint:[/yellow] {hint}")


def print_warning(message: str) -> None:
    """Print a warning message.

    Args:
        message: Warning message
    """
    console.print(f"[bold yellow]⚠️  Warning:[/bold yellow] {message}")


def print_info(message: str) -> None:
    """Print an info message.

    Args:
        message: Info message
    """
    console.print(f"[bold cyan]ℹ️  Info:[/bold cyan] {message}")


def print_suggestions(suggestions: list[str], title: str = "Did you mean:") -> None:
    """Print a list of suggestions.

    Args:
        suggestions: List of suggestions
        title: Title for suggestions
    """
    console.print(f"\n[yellow]{title}[/yellow]")
    for suggestion in suggestions:
        console.print(f"  [cyan]•[/cyan] {suggestion}")


def print_table(title: str, headers: list[str], rows: list[list[Any]], show_header: bool = True) -> None:
    """Print a formatted table.

    Args:
        title: Table title
        headers: Column headers
        rows: Table rows
        show_header: Whether to show header row
    """
    table = Table(title=title, show_header=show_header)

    for header in headers:
        table.add_column(header, style="cyan")

    for row in rows:
        table.add_row(*[str(cell) for cell in row])

    console.print(table)


def print_config_table(config_dict: dict[str, Any], section: str | None = None) -> None:
    """Print configuration as a formatted table.

    Args:
        config_dict: Configuration dictionary
        section: Optional section name
    """
    title = f"{section} Settings" if section else "Configuration"
    table = Table(title=title)

    table.add_column("Key", style="cyan")
    table.add_column("Value", style="white")

    for key, value in config_dict.items():
        if isinstance(value, dict):
            # Flatten nested dicts
            for subkey, subvalue in value.items():
                full_key = f"{key}.{subkey}"
                table.add_row(full_key, _format_value(subvalue))
        else:
            table.add_row(key, _format_value(value))

    console.print(table)


def _format_value(value: Any) -> str:
    """Format value for display (hide API keys, etc.)."""
    if value is None:
        return "[dim]Not set[/dim]"

    value_str = str(value)

    # Hide most of API key
    if len(value_str) > 20 and ("key" in str(value).lower() or "token" in str(value).lower()):
        return f"{value_str[:10]}...{value_str[-4:]}"

    return value_str


def create_progress() -> Progress:
    """Create a progress bar with spinner.

    Returns:
        Progress instance
    """
    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    )


def print_generation_results(results: list[dict[str, Any]]) -> None:
    """Print material generation results as a table.

    Args:
        results: List of generation results with keys: material, status, output, count
    """
    table = Table(title="Generation Results")

    table.add_column("Material", style="cyan")
    table.add_column("Status", style="white")
    table.add_column("Output", style="white")
    table.add_column("Count", style="white")

    for result in results:
        status_icon = "✅" if result.get("status") == "success" else "❌"
        table.add_row(result.get("material", ""), status_icon, result.get("output", ""), str(result.get("count", 0)))

    console.print(table)


def print_pattern_list(patterns: list[str]) -> None:
    """Print available patterns as a formatted list.

    Args:
        patterns: List of pattern names
    """
    console.print("\n[bold cyan]Available TCM Patterns:[/bold cyan]\n")

    for pattern in sorted(patterns):
        console.print(f"  [green]•[/green] {pattern}")

    console.print(f"\n[dim]Total: {len(patterns)} patterns[/dim]")


def confirm(message: str, default: bool = True) -> bool:
    """Ask for user confirmation.

    Args:
        message: Confirmation message
        default: Default value

    Returns:
        User's choice
    """
    try:
        import questionary

        return questionary.confirm(message, default=default).ask()
    except ImportError:
        # Fallback to simple input
        choice = input(f"{message} [{'Y/n' if default else 'y/N'}]: ").lower()
        if not choice:
            return default
        return choice in ["y", "yes"]
