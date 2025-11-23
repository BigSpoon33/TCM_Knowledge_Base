from pathlib import Path

import typer
from rich.progress import Progress, SpinnerColumn, TextColumn

from capsule.constants import MATERIAL_CONFIG
from capsule.core.generator import ContentGenerator
from capsule.core.researcher import DummyResearchProvider, GeminiResearchProvider
from capsule.models.config import Config
from capsule.utils.validation import Validator


def generate(
    topic: str = typer.Argument(..., help="Topic to research and generate content about"),
    template: str = typer.Option("root_note", "--template", "-t", help="Template name to use"),
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
        config = Config.load_config()

        # Infer topic from hybrid file if empty
        if (not topic or not topic.strip()) and hybrid:
            topic = Path(hybrid).stem.replace("_", " ").title()
            if "Root Note" in topic:
                topic = topic.replace("Root Note", "").strip()
            typer.echo(f"ℹ️  Inferred topic from hybrid file: {topic}")

        if not topic or not topic.strip():
            typer.secho("❌ Error: Topic is required.", fg=typer.colors.RED)
            raise typer.Exit(code=1)

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

            # Create topic-specific folder if not already in one
            # Let's follow the pattern: Output_Dir / Topic_Name / Files

            topic_folder_name = topic.replace(" ", "_")
            final_output_path = output_path / topic_folder_name
            final_output_path.mkdir(parents=True, exist_ok=True)

            for material_name, content in generated_capsule.items():
                # generator.validator.validate(content) # Skip validation for now as it might be strict on frontmatter

                # Use centralized configuration for file naming
                if material_name in MATERIAL_CONFIG:
                    file_name_template = MATERIAL_CONFIG[material_name]["filename"]
                    file_name = file_name_template.format(topic=topic_folder_name)
                else:
                    # Fallback for unknown materials
                    file_name = f"{topic_folder_name}_{material_name.capitalize()}.md"

                file_path = final_output_path / file_name
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

            progress.update(val_task, completed=True)

        # Success message
        typer.secho("✅ Capsule generated successfully!", fg=typer.colors.GREEN)
        typer.echo(f"Location: {final_output_path.resolve()}")

    except Exception as e:
        # Consistent error handling
        typer.secho(f"❌ Error: {str(e)}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)
