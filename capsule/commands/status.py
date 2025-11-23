from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from capsule.core.list import List
from capsule.core.status import Status
from capsule.models.config import Config

console = Console()


def status(
    ctx: typer.Context,
):
    """
    Show a summary of all installed capsules in the vault.

    Displays a list of installed capsules including their ID, version, and domain.
    """
    try:
        # Load config
        config_path = ctx.obj.get("config_path") if ctx.obj else None
        if config_path:
            config = Config.from_yaml_file(config_path)
        else:
            config = Config.load_config()

        # Get vault path from config
        vault_path_str = config.user.get("vault_path")
        if not vault_path_str:
            console.print("[red]Error: Vault path not configured. Run 'capsule init' first.[/red]")
            raise typer.Exit(code=1)

        vault_path = Path(vault_path_str)

        # Initialize Status service
        status_service = Status(vault_path)

        # Get summary
        summary = status_service.get_vault_summary()
        capsules = summary["capsules"]

        console.print("\n[bold]Vault Status[/bold]")
        console.print(f"Location: [blue]{vault_path}[/blue]")
        console.print(f"Installed Capsules: [green]{summary['capsule_count']}[/green]\n")

        if capsules:
            table = Table(title="Installed Capsules")
            table.add_column("Capsule ID", style="cyan")
            table.add_column("Name", style="magenta")
            table.add_column("Version", style="green")
            table.add_column("Domain", style="yellow")

            for capsule in capsules:
                table.add_row(capsule.capsule_id, capsule.name, capsule.version, capsule.domain_type)

            console.print(table)
        else:
            console.print("[yellow]No capsules found in this vault.[/yellow]")

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(code=1)


def list_capsules(
    ctx: typer.Context,
):
    """
    List all installed capsules in the vault.

    Displays a simple list of installed capsules with their ID and version,
    allowing you to quickly identify all capsules present in your vault.

    Examples:
        # List all installed capsules
        capsule list

        # List with verbose output for debugging
        capsule --verbose list
    """
    try:
        # Load config
        config_path = ctx.obj.get("config_path") if ctx.obj else None
        if config_path:
            config = Config.from_yaml_file(config_path)
        else:
            config = Config.load_config()

        # Get vault path from config
        vault_path_str = config.user.get("vault_path")
        if not vault_path_str:
            console.print("[red]Error: Vault path not configured. Run 'capsule init' first.[/red]")
            raise typer.Exit(code=1)

        vault_path = Path(vault_path_str)

        # Initialize List service
        list_service = List(vault_path)

        # Get installed capsules
        capsules = list_service.get_installed_capsules()

        if capsules:
            console.print(f"\n[bold]Installed Capsules[/bold] ({len(capsules)} found)\n")

            table = Table(show_header=True, header_style="bold")
            table.add_column("Capsule ID", style="cyan", no_wrap=True)
            table.add_column("Version", style="green")

            for capsule in capsules:
                table.add_row(capsule.capsule_id, capsule.version)

            console.print(table)
            console.print(f"\nVault: [blue]{vault_path}[/blue]")
        else:
            console.print("[yellow]No capsules found in this vault.[/yellow]")
            console.print(f"Vault: [blue]{vault_path}[/blue]")

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(code=1)
