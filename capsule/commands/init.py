# capsule/commands/init.py
from pathlib import Path

import questionary
import typer
from rich.console import Console

from ..models.config import Config

console = Console()


def init():
    """
    Initializes the Capsule CLI configuration.

    Walks you through the setup process to configure your user details,
    vault location, and API keys.
    """
    console.print("[bold cyan]Welcome to Capsule! Let's set up your configuration.[/bold cyan]")

    try:
        # Get defaults from a temporary config object without creating the file
        temp_config = Config.load_config()

        questions = [
            {
                "type": "text",
                "name": "user.name",
                "message": "What is your name?",
                "default": temp_config.get("user.name", "User"),
            },
            {
                "type": "text",
                "name": "user.vault_path",
                "message": "What is the path to your Obsidian vault?",
                "default": temp_config.get("user.vault_path", str(Path.home() / "Documents" / "Obsidian")),
            },
            {
                "type": "password",
                "name": "research.api_key",
                "message": "What is your Google AI API key for research?",
            },
        ]

        answers = questionary.prompt(questions)

        if not answers:
            console.print("[yellow]Initialization cancelled.[/yellow]")
            raise typer.Abort()

        # Now, create the real config and save it
        config = Config(
            user={
                "name": answers.get("user.name"),
                "vault_path": answers.get("user.vault_path"),
            },
            research={
                "api_key": answers.get("research.api_key"),
            },
        )

        # Use XDG standard path
        config_path = Path.home() / ".config" / "capsule" / "config.yaml"
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config.to_yaml_file(config_path)

        console.print(f"[green]✓ Configuration saved to {config_path}[/green]")

    except Exception as e:
        console.print(f"[bold red]Error during initialization: {e}[/bold red]")
        raise typer.Abort()
