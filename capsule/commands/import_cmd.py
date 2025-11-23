import logging
from pathlib import Path

import questionary
import typer
from rich.console import Console

from capsule.core.importer import Importer
from capsule.exceptions import CapsuleError
from capsule.models.config import Config
from capsule.utils.backup import create_backup
from capsule.utils.progress import create_progress_bar

app = typer.Typer(rich_markup_mode="rich")
logger = logging.getLogger(__name__)


@app.command(
    name="import",
    epilog="""
[bold]Examples:[/bold]

  [green]# Interactive import with preview[/green]
  capsule import /path/to/capsule.zip

  [green]# Import without confirmation (useful for scripts)[/green]
  capsule import /path/to/capsule.zip --yes

  [green]# Preview changes without modifying the vault[/green]
  capsule import /path/to/capsule.zip --dry-run

  [green]# Import without creating a backup[/green]
  capsule import /path/to/capsule.zip --no-backup
""",
)
def import_capsule(
    ctx: typer.Context,
    path: Path = typer.Argument(..., help="Path to the capsule file (.zip) or directory to import.", exists=True),
    auto_approve: bool = typer.Option(
        False,
        "--yes",
        "-y",
        help="Automatically approve the import without a preview.",
        rich_help_panel="Import Options",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Show the import preview without performing the import.",
        rich_help_panel="Import Options",
    ),
    no_backup: bool = typer.Option(
        False, "--no-backup", help="Skip creating a backup before import.", rich_help_panel="Import Options"
    ),
):
    """
    Imports a capsule into the vault, with an interactive preview.

    This command analyzes the capsule content and compares it with your current vault.
    It generates a preview of changes (new files, updates, conflicts) before applying them.
    """
    console = Console()
    backup_path = None
    importer = None
    try:
        # Load configuration
        config_path = ctx.obj.get("config_path") if ctx.obj else None

        if config_path:
            config = Config.from_yaml_file(config_path)
        else:
            config = Config.load_config()

        importer = Importer(config, dry_run=dry_run)

        # Extract and Load
        with console.status("[bold green]Loading capsule..."):
            importer.extract_capsule(path)
            importer.load_cypher()
            importer.validate_capsule()

        # Generate Preview
        with console.status("[bold green]Analyzing impact..."):
            vault_path = Path(config.get("user.vault_path"))
            preview = importer.generate_preview(vault_path)

        # Display Preview
        importer.display_preview(preview)

        # Handle Dry Run
        if dry_run:
            typer.secho("\n[Dry Run] Previewing import execution...", fg=typer.colors.YELLOW)
            # Skip confirmation for dry run
        else:
            # Handle Approval
            if not auto_approve:
                if preview.conflicts:
                    confirm = questionary.confirm(
                        "Conflicts detected. Do you want to proceed with the import?", default=False
                    ).ask()
                else:
                    confirm = questionary.confirm("Do you want to proceed with the import?", default=True).ask()

                if not confirm:
                    typer.secho("Import cancelled by user.", fg=typer.colors.YELLOW)
                    raise typer.Exit(code=0)

        # Execute Import
        # Create backup first (unless disabled)
        if not no_backup:
            if dry_run:
                typer.echo("[DRY RUN] Would create vault backup")
            else:
                vault_path_str = config.get("user.vault_path")
                vault_path = Path(vault_path_str)
                backup_dir_str = config.get("import.backup_location", str(Path.home() / ".capsule" / "backups"))
                backup_dir = Path(backup_dir_str)

                # Progress bar for backup creation
                with create_progress_bar("Creating backup...", total=None) as progress:
                    backup_task = progress.add_task("Creating backup...", total=None)
                    backup_path = create_backup(vault_path, backup_dir)
                    progress.update(backup_task, completed=True, description="Backup created!")
                typer.echo(f"Backup created at: {backup_path}")

        # Progress bar for file extraction
        total_files = len(preview.new_files) + len(preview.updates)
        with create_progress_bar("Extracting files...", total=total_files) as progress:
            extract_task = progress.add_task("Extracting files...", total=total_files)
            # Wrap importer.execute_import with progress updates
            # We'll need to modify the importer to support progress callback
            # For now, just show a simple progress indicator
            importer.execute_import(preview)
            progress.update(extract_task, completed=total_files, description=f"Extracted {total_files} files!")

    except typer.Exit:
        raise
    except CapsuleError as e:
        logger.error(f"Capsule Error: {e}")
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    except Exception as e:
        logger.exception("Unexpected error during import")
        typer.secho(f"❌ Unexpected error: {e}", fg=typer.colors.RED)
        if backup_path:
            typer.echo(f"Your vault has been backed up at: {backup_path}")
        raise typer.Exit(code=1)
    finally:
        if importer:
            importer.cleanup()
