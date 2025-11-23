"""Main CLI application using Typer framework"""

import logging
from pathlib import Path

import typer

from capsule import __version__
from capsule.commands import export, generate, import_cmd, init, status, template, validate
from capsule.utils.logger import setup_logging

app = typer.Typer(
    name="capsule",
    help="Obsidian Capsule Delivery System - AI-powered educational content generation",
    add_completion=False,
    rich_markup_mode="rich",
    epilog="""
[bold]Examples:[/bold]

  [green]# Generate content for a topic[/green]
  capsule generate "Liver Qi Stagnation"

  [green]# Export capsule to a zip file[/green]
  capsule export --format zip

  [green]# Import a capsule from a zip file[/green]
  capsule import capsule_export.zip

  [green]# Create a new template[/green]
  capsule template create my_template

  [green]# Check system status[/green]
  capsule status
""",
)

app.command(
    name="generate",
    rich_help_panel="Core Commands",
    epilog="""
[bold]Examples:[/bold]

  [green]# Basic generation[/green]
  capsule generate "Liver Qi Stagnation"

  [green]# Specify template and output directory[/green]
  capsule generate "Insomnia" --template tcm --output ./my_vault

  [green]# Hybrid mode: Enhance an existing note[/green]
  capsule generate --hybrid ./notes/My_Draft.md

  [green]# Dry run: Preview what would be generated[/green]
  capsule generate "Headache" --dry-run
""",
)(generate.generate)
app.command(
    name="init",
    rich_help_panel="Core Commands",
    epilog="""
[bold]Examples:[/bold]

  [green]# Initialize configuration[/green]
  capsule init
""",
)(init.init)
app.command(
    name="validate",
    rich_help_panel="Core Commands",
    epilog="""
[bold]Examples:[/bold]

  [green]# Validate a capsule directory[/green]
  capsule validate ./my_capsule

  [green]# Validate with verbose output[/green]
  capsule validate ./my_capsule --verbose
""",
)(validate.validate)
app.command(
    name="status",
    rich_help_panel="Core Commands",
    epilog="""
[bold]Examples:[/bold]

  [green]# Check system status[/green]
  capsule status
""",
)(status.status)
app.command(
    name="list",
    rich_help_panel="Core Commands",
    epilog="""
[bold]Examples:[/bold]

  [green]# List all installed capsules[/green]
  capsule list
""",
)(status.list_capsules)
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
    [bold]Obsidian Capsule Delivery System[/bold]

    AI-powered content generation and distribution for Obsidian knowledge bases.
    This tool helps you generate, manage, and distribute educational content capsules.

    [bold]Key Features:[/bold]
    * [cyan]Generate[/cyan]: Create comprehensive study materials from topics
    * [cyan]Template[/cyan]: Manage Jinja2 templates for content generation
    * [cyan]Export[/cyan]: Package capsules for distribution (folder or zip)
    * [cyan]Import[/cyan]: Ingest capsules into your knowledge base
    * [cyan]Validate[/cyan]: Ensure content integrity and schema compliance

    For detailed documentation, visit: https://github.com/BigSpoon33/TCM_Knowledge_Base
    """
    # Load configuration for logging settings
    from capsule.models.config import Config

    try:
        config = Config.load_config() if config_path is None else Config.from_yaml_file(config_path)
        logging_config = config.logging
    except Exception:
        # If config fails to load, use defaults
        logging_config = None

    # Initialize structured logging with file rotation and console output
    setup_logging(verbose=verbose, config=logging_config)

    # Store config_path and verbose flag in context for use by subcommands
    ctx.obj = {"config_path": config_path, "verbose": verbose}


import sys
from rich.console import Console
from capsule.exceptions import CapsuleError


def main():
    """Entry point for the CLI"""
    console = Console()
    try:
        app()
    except CapsuleError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        if e.hint:
            console.print(f"[yellow]Hint:[/yellow] {e.hint}")
        sys.exit(e.exit_code)
    except Exception as e:
        console.print(f"[bold red]Unexpected Error:[/bold red] {e}")
        console.print_exception()
        sys.exit(1)


if __name__ == "__main__":
    app()
