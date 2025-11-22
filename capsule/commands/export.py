import typer
from pathlib import Path
from capsule.core.exporter import Exporter

app = typer.Typer()


@app.command()
def export(
    capsule_path: Path = typer.Argument(..., help="The path to the capsule directory to export."),
    output_path: Path = typer.Argument(..., help="The destination path for the exported file or folder."),
    format: str = typer.Option("zip", "--format", "-f", help="Export format: 'zip' or 'folder'"),
):
    """
    Exports a capsule to a distributable format (zip or folder).
    """
    exporter = Exporter(capsule_path)

    if format == "zip":
        # Ensure the output path has the correct extension
        if output_path.suffix != ".capsule":
            output_path = output_path.with_suffix(".capsule")
        exporter.export_to_zip(output_path)
    elif format == "folder":
        exporter.export_to_folder(output_path)
    else:
        typer.echo(f"Error: Invalid format '{format}'. Please choose 'zip' or 'folder'.")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
