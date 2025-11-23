import logging
from pathlib import Path

import questionary
import typer
from rich.console import Console

from capsule.core.importer import Importer
from capsule.exceptions import CapsuleError
from capsule.models.config import Config
from capsule.utils.backup import create_backup

app = typer.Typer()
console = Console()
logger = logging.getLogger(__name__)


@app.command(name="import")
def import_capsule(
    ctx: typer.Context,
    path: Path = typer.Argument(..., help="Path to the capsule file (.zip) or directory to import.", exists=True),
    auto_approve: bool = typer.Option(False, "--yes", "-y", help="Automatically approve the import without a preview."),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show the import preview without performing the import."),
    no_backup: bool = typer.Option(False, "--no-backup", help="Skip creating a backup before import."),
):
    """
    Imports a capsule into the vault, with an interactive preview.

    Examples:
        # Interactive import with preview
        capsule import /path/to/capsule.zip

        # Import without confirmation (useful for scripts)
        capsule import /path/to/capsule.zip --yes

        # Preview changes without modifying the vault
        capsule import /path/to/capsule.zip --dry-run

        # Import without creating a backup
        capsule import /path/to/capsule.zip --no-backup
    """
    backup_path = None
    importer = None
    try:
        # Load configuration
        config_path = ctx.obj.get("config_path") if ctx.obj else None

        if config_path:
            config = Config.from_yaml_file(config_path)
        else:
            config = Config.load_config()

        importer = Importer(config)

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
            typer.secho("\n[Dry Run] No changes were made to the vault.", fg=typer.colors.YELLOW)
            return

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
            vault_path_str = config.get("user.vault_path")
            vault_path = Path(vault_path_str)
            backup_dir_str = config.get("import.backup_location", str(Path.home() / ".capsule" / "backups"))
            backup_dir = Path(backup_dir_str)

            with console.status("[bold green]Creating backup..."):
                backup_path = create_backup(vault_path, backup_dir)
            typer.echo(f"Backup created at: {backup_path}")

        with console.status("[bold green]Executing import..."):
            importer.execute_import(preview)

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
