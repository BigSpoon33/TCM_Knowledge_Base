from jinja2 import Environment, FileSystemLoader, Template
from pathlib import Path

# Define the base directory of the project to resolve paths correctly
# This assumes the script is in capsule/utils/templates.py
BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATE_DIR = BASE_DIR / "capsule" / "templates"

def create_jinja_environment() -> Environment:
    """Creates and configures a Jinja2 environment."""
    return Environment(loader=FileSystemLoader(TEMPLATE_DIR))

def load_template(template_name: str) -> Template:
    """Loads a Jinja2 template by name."""
    env = create_jinja_environment()
    return env.get_template(template_name)
