from jinja2 import Environment, FileSystemLoader, Template

from capsule.constants import TEMPLATES_DIR


def create_jinja_environment(template_dir=TEMPLATES_DIR) -> Environment:
    """Creates and configures a Jinja2 environment."""
    return Environment(loader=FileSystemLoader(template_dir))


def load_template(template_name: str, template_dir=TEMPLATES_DIR) -> Template:
    """Loads a Jinja2 template by name."""
    env = create_jinja_environment(template_dir)
    return env.get_template(template_name)
