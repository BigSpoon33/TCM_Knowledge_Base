"""Import command for capsule CLI."""

import typer
from pathlib import Path
from capsule.core.importer import Importer
from capsule.models.config import Config
from capsule.utils.backup import create_backup

app = typer.Typer()


@app.command(name="import")
def import_cmd(
    capsule_path: Path = typer.Argument(
        ..., help="Path to the capsule file (.capsule zip) or folder to import.", exists=True
    ),
    target_vault: Path = typer.Option(None, "--target", "-t", help="Target vault path (defaults to config value)."),
    no_backup: bool = typer.Option(False, "--no-backup", help="Skip the pre-import backup."),
    force: bool = typer.Option(False, "--force", "-f", help="Skip interactive approval and force import."),
):
    """
    Import a capsule into your Obsidian vault with preview.

    This command extracts the capsule, analyzes its contents, validates
    the structure, and shows a detailed preview of what will be imported.

    The preview includes:
    - Capsule metadata (ID, name, version, domain type, file count)
    - Impact analysis (new files, updated files, potential conflicts)
    - Detailed lists of files that will be created or updated
    - Merge strategy for each file (section-level or additive)
    - Any detected conflicts with reasons

    Examples:
        # Import a capsule zip file with preview
        capsule import TCM_Herbs_v1.capsule

        # Import from a folder
        capsule import ./my-capsule-folder

        # Import to a specific vault (override config)
        capsule import my-capsule.capsule --target ~/Documents/MyVault

        # Skip backup (not recommended)
        capsule import my-capsule.capsule --no-backup

        # Force import without interactive approval
        capsule import my-capsule.capsule --force
    """
    backup_path = None
    try:
        # Load configuration
        config = Config.load_config()

        # Override vault path if specified
        if target_vault:
            config.user["vault_path"] = str(target_vault)

        importer = Importer(config)

        # Create backup if requested
        if not no_backup:
            vault_path_str = config.get("user.vault_path")
            if not vault_path_str:
                raise ValueError("Vault path is not set in the configuration.")
            vault_path = Path(vault_path_str)

            backup_dir_str = config.get("import.backup_location", str(Path.home() / ".capsule" / "backups"))
            backup_dir = Path(backup_dir_str)

            typer.echo("Creating vault backup...")
            backup_path = create_backup(vault_path, backup_dir)
            typer.echo(f"Backup created at: {backup_path}")

        # Extract capsule (handles both zip and folder)
        importer.extract_capsule(capsule_path)

        # Load and parse cypher
        importer.load_cypher()

        # Validate capsule structure
        importer.validate_capsule()

        # Analyze impact on vault
        vault_path = Path(config.get("user.vault_path"))
        preview = importer.analyze_impact(vault_path)

        # Display preview
        importer.display_preview(preview)

        # Interactive Approval
        if not force:
            if not typer.confirm("Do you want to proceed with the import?"):
                typer.echo("Import cancelled by user.")
                raise typer.Exit()

        # Execute Import
        importer.execute_import(preview)

    except FileNotFoundError as e:
        typer.secho(f"❌ File Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)
    except ValueError as e:
        typer.secho(f"❌ Validation Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)
    except typer.Exit:
        raise
    except Exception as e:
        typer.secho(f"❌ Unexpected Error: {e}", fg=typer.colors.RED, err=True)
        if backup_path:
            typer.echo(f"Your vault has been backed up at: {backup_path}")
        typer.echo("\nPlease report this issue with the full error message.")
        raise typer.Exit(code=1)
    finally:
        # Clean up temporary extraction directory
        if "importer" in locals():
            importer.cleanup()


if __name__ == "__main__":
    app()
