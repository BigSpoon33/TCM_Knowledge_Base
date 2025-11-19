"""Configuration management commands."""

import typer
from pathlib import Path

from ..utils.config import get_config
from ..utils.output import (
    console,
    print_success,
    print_error,
    print_config_table,
)

config_app = typer.Typer()

@config_app.command("set")
def config_set(key: str, value: str):
    """Set a configuration value."""
    try:
        config = get_config()
        config.set(key, value)
        config.save()
        print_success(f"Set {key} = {value}")
    except Exception as e:
        print_error(f"Failed to set configuration: {e}")
        raise typer.Abort()

@config_app.command("get")
def config_get(key: str):
    """Get a configuration value."""
    try:
        config = get_config()
        value = config.get(key)
        
        if value is None:
            print_error(f"Configuration key '{key}' not found")
        else:
            console.print(f"[cyan]{key}[/cyan] = [white]{value}[/white]")
    except Exception as e:
        print_error(f"Failed to get configuration: {e}")
        raise typer.Abort()

@config_app.command("list")
def config_list():
    """List all configuration values."""
    try:
        config = get_config()
        config_dict = config.get_all()
        
        console.print(f"\n[bold]Configuration File:[/bold] {config.config_path}\n")
        
        # Print each section separately
        for section, values in config_dict.items():
            if isinstance(values, dict):
                print_config_table(values, section.title())
                console.print()
            else:
                print_config_table({section: values})
                console.print()
                
    except Exception as e:
        print_error(f"Failed to list configuration: {e}")
        raise typer.Abort()

@config_app.command("init")
def config_init():
    """Initialize configuration interactively."""
    try:
        config = get_config()
        
        console.print("\n[bold cyan]Capsule Configuration Setup[/bold cyan]\n")
        console.print("This will guide you through setting up Capsule.\n")
        
        config.init_interactive()
        print_success("Configuration initialized!")
        
        console.print(f"\n[dim]Config saved to: {config.config_path}[/dim]")
        
    except Exception as e:
        print_error(f"Failed to initialize configuration: {e}")
        raise typer.Abort()

@config_app.command("path")
def config_path():
    """Show the configuration file path."""
    config = get_config()
    console.print(f"\n[bold]Configuration file:[/bold] {config.config_path}")
    
    if config.config_path.exists():
        console.print(f"[green]File exists[/green]")
    else:
        console.print(f"[yellow]File does not exist (will be created on first save)[/yellow]")
