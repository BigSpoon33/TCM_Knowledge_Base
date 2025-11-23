from pathlib import Path

import frontmatter
import ruamel.yaml
import typer
from rich.console import Console
from rich.table import Table

from capsule.models.template import TemplateSchema

app = typer.Typer(help="Manage Jinja2 templates for content generation.", rich_markup_mode="rich")


@app.command(
    "list",
    epilog="""
[bold]Examples:[/bold]

  [green]# List all available templates[/green]
  capsule template list
""",
)
def list_templates():
    """
    List all available templates.

    Displays a table of installed templates with their names and domains.
    """
    try:
        template_dir = Path("capsule/templates")
        if not template_dir.exists():
            typer.secho("❌ Error: Templates directory not found.", fg=typer.colors.RED)
            return

        templates = sorted(template_dir.glob("*.md.j2"))

        if not templates:
            typer.echo("No templates found.")
            return

        console = Console()
        table = Table(title="Available Templates")
        table.add_column("Template Name", style="cyan")
        table.add_column("Domain", style="magenta")

        for template_path in templates:
            name = template_path.name.replace(".md.j2", "")
            domain = "Universal"  # Default

            # Try to read domain from frontmatter
            try:
                post = frontmatter.load(template_path)
                if "domain" in post.metadata:
                    domain = post.metadata["domain"]
            except Exception:
                pass  # Keep default if parsing fails

            table.add_row(name, domain)

        console.print(table)

    except Exception as e:
        typer.secho(f"❌ Error: {str(e)}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)


@app.command(
    epilog="""
[bold]Examples:[/bold]

  [green]# Create a basic template[/green]
  capsule template create my_template

  [green]# Create a template with frontmatter fields[/green]
  capsule template create study_note --fields "tags,status,priority"

  [green]# Overwrite an existing template[/green]
  capsule template create my_template --force
"""
)
def create(
    name: str = typer.Argument(..., help="The name of the new template"),
    fields: str = typer.Option(
        None, "--fields", "-f", help="A comma-separated list of frontmatter fields", rich_help_panel="Template Options"
    ),
    domain: str = typer.Option(
        "custom", "--domain", "-d", help="The domain of the template", rich_help_panel="Template Options"
    ),
    force: bool = typer.Option(
        False, "--force", help="Overwrite the template if it already exists", rich_help_panel="Template Options"
    ),
):
    """
    Create a new template for content generation.

    Generates a new Jinja2 template file with optional frontmatter fields.
    """
    try:
        template_dir = Path("capsule/templates")
        template_dir.mkdir(exist_ok=True)
        template_file = template_dir / f"{name}.md.j2"

        if template_file.exists() and not force:
            typer.secho(f"❌ Error: Template '{name}' already exists. Use --force to overwrite.", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        # Create the template content
        content = "---\n"
        if fields:
            field_list = [field.strip() for field in fields.split(",")]
            for field in field_list:
                content += f"{field}: {{{{ {field} }}}}\n"
        content += "---\n\n"
        content += "{{ content }}\n"

        with open(template_file, "w", encoding="utf-8") as f:
            f.write(content)

        typer.secho(f"✅ Template '{name}' created successfully at {template_file}", fg=typer.colors.GREEN)

    except Exception as e:
        typer.secho(f"❌ Error: {str(e)}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)


@app.command(
    epilog="""
[bold]Examples:[/bold]

  [green]# Validate a template schema file[/green]
  capsule template validate ./schemas/my_schema.yaml
"""
)
def validate(
    filepath: Path = typer.Argument(
        ..., help="Path to the template schema YAML file", exists=True, readable=True, resolve_path=True
    ),
):
    """
    Validate a template schema file.

    Checks if the provided YAML file conforms to the TemplateSchema definition.
    """
    try:
        yaml = ruamel.yaml.YAML()

        # Load the file
        with open(filepath, encoding="utf-8") as f:
            data = yaml.load(f)

        if not isinstance(data, dict):
            typer.secho("❌ Error: Invalid YAML structure. Root must be a dictionary.", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        # Validate required fields for TemplateSchema
        required_fields = ["domain_type", "version"]
        missing = [f for f in required_fields if f not in data]

        if missing:
            typer.secho(f"❌ Error: Missing required fields: {', '.join(missing)}", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        # Try to instantiate TemplateSchema to check types and structure
        try:
            schema = TemplateSchema(**data)
        except TypeError as e:
            typer.secho(f"❌ Error: Schema validation failed. {str(e)}", fg=typer.colors.RED)
            raise typer.Exit(code=1)
        except Exception as e:
            typer.secho(f"❌ Error: {str(e)}", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        typer.secho(f"✅ Template schema '{filepath.name}' is valid.", fg=typer.colors.GREEN)
        typer.echo(f"Domain: {schema.domain_type}")
        typer.echo(f"Version: {schema.version}")

    except typer.Exit:
        raise
    except Exception as e:
        typer.secho(f"❌ Error: {str(e)}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)
