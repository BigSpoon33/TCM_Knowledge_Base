"""Console script for obsidian_capsule_cli."""

import typer
from rich.console import Console

from obsidian_capsule_cli import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for obsidian_capsule_cli."""
    console.print("Replace this message by putting your code into obsidian_capsule_cli.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
