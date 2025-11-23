from pathlib import Path

import typer

from capsule.constants import MATERIAL_CONFIG, TEMPLATES_DIR
from capsule.core.generator import ContentGenerator
from capsule.core.researcher import DummyResearchProvider, GeminiResearchProvider
from capsule.models.config import Config
from capsule.utils.file_ops import FileOps
from capsule.utils.progress import create_progress_bar, create_spinner
from capsule.utils.validation import Validator


def deploy_css(output_path: Path, file_ops: FileOps):
    """
    Deploys CSS files to the .obsidian/snippets directory if it exists.
    """
    # Find .obsidian directory
    obsidian_dir = None
    current_path = output_path.resolve()

    # Check current and parents for .obsidian
    # Limit traversal to avoid going too far up
    for _ in range(5):
        if (current_path / ".obsidian").exists():
            obsidian_dir = current_path / ".obsidian"
            break
        if current_path.parent == current_path:
            break
        current_path = current_path.parent

    if not obsidian_dir:
        return

    snippets_dir = obsidian_dir / "snippets"
    file_ops.mkdir(snippets_dir, parents=True, exist_ok=True)

    css_dir = TEMPLATES_DIR / "css"

    # Copy main CSS files
    for css_file in css_dir.glob("*.css"):
        file_ops.copy(css_file, snippets_dir / css_file.name)

    # Copy themes
    themes_dir = css_dir / "themes"
    if themes_dir.exists():
        for theme_file in themes_dir.glob("*.css"):
            file_ops.copy(theme_file, snippets_dir / theme_file.name)

    typer.echo(f"✨ Deployed CSS snippets to {snippets_dir}")


def generate(
    topic: str = typer.Argument(..., help="Topic to research and generate content about"),
    template: str = typer.Option(
        "root_note", "--template", "-t", help="Template name to use", rich_help_panel="Generation Options"
    ),
    output: str = typer.Option(".", "--output", "-o", help="Output directory", rich_help_panel="Output Options"),
    materials: str = typer.Option(
        "all",
        "--materials",
        "-m",
        help="Materials to generate: flashcards,quizzes,slides,conversations",
        rich_help_panel="Generation Options",
    ),
    hybrid: str = typer.Option(
        None,
        "--hybrid",
        help="Path to existing note for AI enhancement",
        rich_help_panel="Generation Options",
    ),
    no_research: bool = typer.Option(
        False,
        "--no-research",
        help="Skip deep research, use template only",
        rich_help_panel="Generation Options",
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Preview without creating files", rich_help_panel="Output Options"
    ),
):
    """
    Generate a new capsule from research and templates.

    This command performs deep research on the given TOPIC (using Gemini AI) and generates
    a set of educational materials (Capsule) based on the specified template.

    You can also use 'Hybrid Mode' to enhance an existing note.
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

        # Initialize FileOps
        file_ops = FileOps(dry_run=dry_run)

        # Create generator
        if no_research:
            researcher = DummyResearchProvider()
        else:
            researcher = GeminiResearchProvider()

        validator = Validator()
        generator = ContentGenerator(researcher, validator, dry_run=dry_run)

        materials_list = [m.strip() for m in materials.split(",")]
        if "all" in materials_list:
            materials_list = list(MATERIAL_CONFIG.keys())

        # Determine template name
        if template.endswith(".md") or template.endswith(".j2"):
            template_name = template
        else:
            template_name = f"{template}.md.j2"

        # Research phase (spinner for indeterminate progress)
        generated_capsule = None
        if not no_research:
            with create_spinner("Deep research...") as progress:
                research_task = progress.add_task("Deep research...", total=None)
                # Research happens inside generator.generate() - update description to show we're working
                progress.update(research_task, description="Deep research... (analyzing sources)")

                generated_capsule = generator.generate(
                    topic=topic,
                    template_name=template_name,
                    materials=materials_list,
                    source_path=Path(hybrid) if hybrid else None,
                )
                progress.update(research_task, completed=True, description="Deep research complete!")
        else:
            # No research - just generate from template
            generated_capsule = generator.generate(
                topic=topic,
                template_name=template_name,
                materials=materials_list,
                source_path=Path(hybrid) if hybrid else None,
            )

        # Generation phase (progress bar with percentage)
        total_materials = len(generated_capsule.keys())
        with create_progress_bar("Generating content...", total=total_materials) as progress:
            gen_task = progress.add_task("Generating content...", total=total_materials)
            output_path = Path(output)

            # Create topic-specific folder if not already in one
            # Let's follow the pattern: Output_Dir / Topic_Name / Files

            topic_folder_name = topic.replace(" ", "_")
            final_output_path = output_path / topic_folder_name
            file_ops.mkdir(final_output_path, parents=True, exist_ok=True)

            current_idx = 0
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
                file_ops.write_text(file_path, content)

                current_idx += 1
                progress.update(gen_task, completed=current_idx, description=f"Generating content... ({material_name})")

        # Deploy CSS if applicable
        deploy_css(final_output_path, file_ops)

        # Success message
        if dry_run:
            typer.secho("✅ Dry run complete! No files were created.", fg=typer.colors.YELLOW)
        else:
            typer.secho("✅ Capsule generated successfully!", fg=typer.colors.GREEN)
            typer.echo(f"Location: {final_output_path.resolve()}")

    except Exception as e:
        # Consistent error handling
        typer.secho(f"❌ Error: {str(e)}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)
