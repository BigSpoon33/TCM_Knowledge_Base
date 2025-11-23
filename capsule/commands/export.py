import logging
from pathlib import Path

import typer
import yaml
from rich.console import Console

from capsule.core.exporter import Exporter
from capsule.exceptions import CapsuleError, FileError, ValidationError

app = typer.Typer(rich_markup_mode="rich")
console = Console()
logger = logging.getLogger(__name__)


@app.command(
    epilog="""
[bold]Examples:[/bold]

  [green]# Export capsule to a zip file (default)[/green]
  capsule export ./my_capsule

  [green]# Export to a specific output directory[/green]
  capsule export ./my_capsule --output ./dist

  [green]# Export as a folder instead of zip[/green]
  capsule export ./my_capsule --no-zip

  [green]# Dry run: Preview export process[/green]
  capsule export ./my_capsule --dry-run
"""
)
def export(
    path: Path = typer.Argument(..., help="Path to the capsule directory to export."),
    output_dir: Path = typer.Option(
        Path("."), "--output", "-o", help="Output directory for the exported file.", rich_help_panel="Export Options"
    ),
    as_zip: bool = typer.Option(
        True, "--zip/--no-zip", help="Export as a .zip archive or a folder.", rich_help_panel="Export Options"
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Preview without creating files", rich_help_panel="Export Options"
    ),
):
    """
    Packages a capsule into a distributable format.

    This command prepares a capsule for distribution by validating it and packaging it
    into a ZIP archive or a standalone folder.
    """
    try:
        logger.info(f"Starting export for capsule at: {path}")
        if not path.exists():
            raise FileNotFoundError(f"Capsule path does not exist: {path}")

        if dry_run:
            typer.echo(f"[DRY RUN] Would export capsule from: {path}")
            typer.echo(f"Output directory: {output_dir}")

        exporter = Exporter(path, dry_run=dry_run)

        capsule_id = exporter.cypher.get("capsule_id", "capsule")
        version = exporter.cypher.get("version", "1.0.0")
        filename = f"{capsule_id}_v{version}"

        if not dry_run:
            output_dir.mkdir(parents=True, exist_ok=True)
        elif dry_run:
            typer.echo(f"[DRY RUN] Would create output directory: {output_dir}")

        if as_zip:
            output_path = output_dir / f"{filename}.zip"
            with console.status(f"[bold green]Exporting capsule to {output_path}..."):
                exporter.export_to_zip(output_path)
            if dry_run:
                typer.secho("✅ Dry run complete! No files were created.", fg=typer.colors.YELLOW)
            else:
                logger.info(f"[bold green]✅ Successfully exported capsule to:[/bold green] {output_path}")
        else:
            output_path = output_dir / filename
            with console.status(f"[bold green]Exporting capsule to {output_path}..."):
                exporter.export_to_folder(output_path)
            if dry_run:
                typer.secho("✅ Dry run complete! No files were created.", fg=typer.colors.YELLOW)
            else:
                logger.info(f"[bold green]✅ Successfully exported capsule to:[/bold green] {output_path}")

    except FileNotFoundError as e:
        logger.error(f"[bold red]❌ Error:[/bold red] {e}")
        raise typer.Exit(code=1)
    except ValidationError as e:
        logger.error(f"[bold red]❌ Validation Error:[/bold red] {e}")
        raise typer.Exit(code=1)
    except FileError as e:
        logger.error(f"[bold red]❌ File Error:[/bold red] {e}")
        raise typer.Exit(code=1)
    except CapsuleError as e:
        logger.error(f"[bold red]❌ Error:[/bold red] {e}")
        raise typer.Exit(code=1)
    except yaml.YAMLError as e:
        logger.error(f"[bold red]❌ YAML Error:[/bold red] {e}")
        raise typer.Exit(code=1)
    except Exception as e:
        logger.critical(f"[bold red]❌ An unexpected error occurred:[/bold red] {e}", exc_info=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
