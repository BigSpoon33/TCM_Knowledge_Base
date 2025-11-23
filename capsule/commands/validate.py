from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel

from capsule.core.validator import Validator
from capsule.exceptions import CapsuleError

console = Console()


def validate(
    path: Path = typer.Argument(
        ...,
        help="Path to the capsule directory to validate.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output.", rich_help_panel="Validation Options"
    ),
):
    """
    Validates a capsule's structure, cypher, and contents against its schema.

    This command performs a comprehensive check of the capsule to ensure it meets
    all requirements for distribution and import.
    """

    console.print(f"[bold blue]Validating capsule at:[/bold blue] {path}")

    try:
        validator = Validator(path)

        with console.status("[bold green]Running validation checks...[/bold green]"):
            validator.validate_capsule()

        # If we get here, validation passed
        console.print(
            Panel.fit(
                f"[bold green]✓ Validation Successful![/bold green]\nCapsule at [cyan]{path}[/cyan] is valid.",
                title="Validation Result",
                border_style="green",
            )
        )
        raise typer.Exit(code=0)

    except typer.Exit:
        raise
    except CapsuleError as e:
        # The Validator raises CapsuleError, we should catch them and print nicely
        console.print(
            Panel.fit(
                f"[bold red]✗ Validation Failed[/bold red]\n\n[red]{str(e)}[/red]",
                title="Validation Result",
                border_style="red",
            )
        )
        if e.hint:
            console.print(f"[yellow]Hint:[/yellow] {e.hint}")

        if verbose:
            console.print_exception()

        raise typer.Exit(code=1)

    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/bold red] {e}")
        if verbose:
            console.print_exception()
        raise typer.Exit(code=1)
