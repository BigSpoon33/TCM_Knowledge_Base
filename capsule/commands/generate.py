import typer
from rich.progress import Progress, SpinnerColumn, TextColumn
from capsule.models.config import Config
from capsule.core.researcher import GeminiResearchProvider, DummyResearchProvider
from capsule.utils.validation import Validator
from capsule.core.generator import ContentGenerator
from pathlib import Path


def generate(
    topic: str = typer.Argument(..., help="Topic to research and generate content about"),
    template: str = typer.Option("education", "--template", "-t", help="Template name to use"),
    output: str = typer.Option(".", "--output", "-o", help="Output directory"),
    materials: str = typer.Option(
        "all", "--materials", "-m", help="Materials to generate: flashcards,quizzes,slides,conversations"
    ),
    hybrid: str = typer.Option(None, "--hybrid", help="Path to existing note for AI enhancement"),
    no_research: bool = typer.Option(False, "--no-research", help="Skip deep research, use template only"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview without creating files"),
):
    """
    Generate a new capsule from research and templates.

    Example:
        capsule generate "Introduction to TCM Herbs" --template tcm
    """

    try:
        # Load config
        config = Config()

        # Show what will happen
        if dry_run:
            typer.echo(f"[DRY RUN] Would generate capsule about: {topic}")
            typer.echo(f"Template: {template}")
            typer.echo(f"Output: {output}")
            return

        # Create generator
        if no_research:
            researcher = DummyResearchProvider()
        else:
            researcher = GeminiResearchProvider()

        validator = Validator()
        generator = ContentGenerator(researcher, validator)

        # Research and Generation phase
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=False,
        ) as progress:
            gen_task = progress.add_task("Generating content...", total=None)
            materials_list = [m.strip() for m in materials.split(",")]

            # Determine template name
            if template.endswith(".md") or template.endswith(".j2"):
                template_name = template
            else:
                template_name = f"{template}.md.j2"

            generated_capsule = generator.generate(
                topic=topic,
                template_name=template_name,
                materials=materials_list,
                source_path=Path(hybrid) if hybrid else None,
            )
            progress.update(gen_task, completed=True)

            # Validation and Saving phase
            val_task = progress.add_task("Validating and saving...", total=None)
            output_path = Path(output)
            output_path.mkdir(parents=True, exist_ok=True)

            for material_name, content in generated_capsule.items():
                generator.validator.validate(content)
                file_name = f"{material_name.capitalize()}_{topic.replace(' ', '_')}.md"
                file_path = output_path / file_name
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

            progress.update(val_task, completed=True)

        # Success message
        typer.secho(f"✅ Capsule generated successfully!", fg=typer.colors.GREEN)
        typer.echo(f"Location: {output_path.resolve()}")

    except Exception as e:
        # Consistent error handling
        typer.secho(f"❌ Error: {str(e)}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)
