# capsule/commands/init.py
import typer
from rich.console import Console
import questionary
from pathlib import Path

from ..models.config import Config
from ..utils.exceptions import ConfigError

console = Console()

def init():
    """
    Initializes the Capsule CLI configuration.
    """
    console.print("[bold cyan]Welcome to Capsule! Let's set up your configuration.[/bold cyan]")

    try:
        # Get defaults from a temporary config object without creating the file
        temp_config = Config()
        
        questions = [
            {
                'type': 'text',
                'name': 'user.name',
                'message': 'What is your name?',
                'default': temp_config.get('user.name', 'User'),
            },
            {
                'type': 'text',
                'name': 'user.vault_path',
                'message': 'What is the path to your Obsidian vault?',
                'default': temp_config.get('user.vault_path', str(Path.home() / 'Documents' / 'Obsidian')),
            },
            {
                'type': 'password',
                'name': 'research.api_key',
                'message': 'What is your Google AI API key for research?',
            },
        ]

        answers = questionary.prompt(questions)

        if not answers:
            console.print("[yellow]Initialization cancelled.[/yellow]")
            raise typer.Abort()

        # Now, create the real config and save it
        config = Config()
        config.data['user']['name'] = answers.get('user.name')
        config.data['user']['vault_path'] = answers.get('user.vault_path')
        config.data['research']['api_key'] = answers.get('research.api_key')
        
        config.save()

        console.print(f"[green]✓ Configuration saved to {config.path}[/green]")

    except Exception as e:
        console.print(f"[bold red]Error during initialization: {e}[/bold red]")
        raise typer.Abort()
