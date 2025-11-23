import logging
from pathlib import Path

import typer
import yaml
from rich.console import Console

from capsule.core.exporter import Exporter
from capsule.exceptions import CapsuleError, FileError, ValidationError

app = typer.Typer()
console = Console()
logger = logging.getLogger(__name__)


@app.command()
def export(
    path: Path = typer.Argument(..., help="Path to the capsule directory to export."),
    output_dir: Path = typer.Option(Path("."), "--output", "-o", help="Output directory for the exported file."),
    as_zip: bool = typer.Option(True, "--zip/--no-zip", help="Export as a .zip archive or a folder."),
):
    """
    Packages a capsule into a distributable format.
    """
    try:
        logger.info(f"Starting export for capsule at: {path}")
        if not path.exists():
            raise FileNotFoundError(f"Capsule path does not exist: {path}")

        exporter = Exporter(path)

        capsule_id = exporter.cypher.get("capsule_id", "capsule")
        version = exporter.cypher.get("version", "1.0.0")
        filename = f"{capsule_id}_v{version}"

        output_dir.mkdir(parents=True, exist_ok=True)

        if as_zip:
            output_path = output_dir / f"{filename}.zip"
            with console.status(f"[bold green]Exporting capsule to {output_path}..."):
                exporter.export_to_zip(output_path)
            logger.info(f"[bold green]✅ Successfully exported capsule to:[/bold green] {output_path}")
        else:
            output_path = output_dir / filename
            with console.status(f"[bold green]Exporting capsule to {output_path}..."):
                exporter.export_to_folder(output_path)
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
