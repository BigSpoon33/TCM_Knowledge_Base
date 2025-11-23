"""Main CLI application using Typer framework"""

import logging
from pathlib import Path

import typer

from capsule import __version__
from capsule.commands import export, generate, import_cmd, init, status, template, validate

app = typer.Typer(
    name="capsule",
    help="Obsidian Capsule Delivery System - AI-powered educational content generation",
    add_completion=False,
)

app.command(name="generate")(generate.generate)
app.command(name="init")(init.init)
app.command(name="validate")(validate.validate)
app.command(name="status")(status.status)
app.command(name="list")(status.list_capsules)
app.add_typer(export.app)
app.add_typer(import_cmd.app)
app.add_typer(template.app, name="template")


def version_callback(value: bool):
    """Display version information"""
    if value:
        typer.echo(f"Obsidian Capsule CLI v{__version__}")
        raise typer.Exit()


@app.callback()
def cli_callback(
    ctx: typer.Context,
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        help="Enable verbose output with detailed logging",
    ),
    config_path: Path | None = typer.Option(
        None,
        "--config-path",
        help="Path to custom configuration file",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
    ),
):
    """
    Obsidian Capsule Delivery System

    AI-powered content generation and distribution for Obsidian knowledge bases.

    For detailed documentation, visit: https://github.com/BigSpoon33/TCM_Knowledge_Base
    """
    # Configure logging based on verbose flag
    log_level = logging.DEBUG if verbose else logging.INFO

    from rich.logging import RichHandler

    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True, markup=True)],
        force=True,
    )

    # Store config_path and verbose flag in context for use by subcommands

    ctx.obj = {"config_path": config_path, "verbose": verbose}


def main():
    """Entry point for the CLI"""
    app()


if __name__ == "__main__":
    app()
