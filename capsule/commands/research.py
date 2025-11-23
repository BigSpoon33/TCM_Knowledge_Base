"""Deep research commands."""

import os
import subprocess
import sys
from pathlib import Path

import typer

from ..utils.config import get_config
from ..utils.output import (
    console,
    create_progress,
    print_error,
    print_header,
    print_success,
)
from ..utils.validation import find_script_path, validate_api_key

research_app = typer.Typer()


@research_app.command("topic")
def research_topic(
    topic: str,
    project: str = typer.Option("Traditional Chinese Medicine", "--project", help="Project/domain context"),
    template: str = typer.Option(None, "--template", help="Custom template file"),
    output: str = typer.Option(None, "--output", help="Output directory (for --deep) or file path"),
    deep: bool = typer.Option(False, "--deep", help="Use deep research pipeline (creates root note + all materials)"),
    depth: str = typer.Option("comprehensive", "--depth", help="Research depth", case_sensitive=False),
    class_id: str = typer.Option(None, "--class-id", help="Class ID (default: creates project_topic folder)"),
):
    """Research a TCM topic and generate comprehensive notes."""
    config = get_config()

    # Get configuration values
    kb_path = Path(config.get("paths.knowledge_base", Path.cwd()))

    # Set class_id - use provided, or config default, or None (creates project_topic folder)
    if not class_id:
        class_id = config.get("defaults.class_id") if not deep else None

    if deep:
        # Deep research uses simple template by default (10 sections, faster)
        # Use Root_Note_Template.md for exhaustive detail (52 sections, slower)
        if not template:
            if depth == "exhaustive":
                template = "Root_Note_Template.md"  # Full template
            else:
                template = "TCM_Pattern_Template_Simple.md"  # Simple template (FAST!)
    else:
        # Standard research uses simpler template
        template = template or config.get("defaults.template", "TCM_Pattern_Template_Simple.md")

    # Validate API key
    api_key = config.get("api.gemini_key")
    is_valid, error_msg = validate_api_key(api_key)
    if not is_valid:
        print_error(error_msg)
        raise typer.Abort()

    # Check if output already exists (for deep research)
    if deep and not output:
        # Generate default output path
        materials_dir = kb_path / config.get("paths.output_dir", "Materials")

        if class_id:
            output_dir = materials_dir / class_id
        else:
            # Creates folder like: Traditional_Chinese_Medicine_Edema
            folder_name = f"{project.replace(' ', '_')}_{topic.replace(' ', '_')}"
            output_dir = materials_dir / folder_name

        # Check if folder already exists with materials
        if output_dir.exists():
            existing_files = list(output_dir.glob("*.md"))
            if existing_files:
                from ..utils.output import confirm, print_warning

                print_warning(f"Output folder already exists with {len(existing_files)} files: {output_dir}")

                if not confirm("Overwrite existing materials?", default=False):
                    print_error("Research cancelled")
                    raise typer.Abort()

    # Print header
    research_type = "Deep Research Pipeline" if deep else "Standard Research"
    header_info = f"Topic: {topic}\nProject: {project}\nDepth: {depth}"
    if deep:
        header_info += f"\nTemplate: {template}"
        if class_id:
            header_info += f"\nClass ID: {class_id}"
        else:
            folder_name = f"{project.replace(' ', '_')}_{topic.replace(' ', '_')}"
            header_info += f"\nOutput Folder: {folder_name}/"

    print_header(research_type, header_info)

    # Find research script
    scripts_dir = kb_path / "scripts"

    if deep:
        script_path = find_script_path("deep_research_pipeline", scripts_dir)
        script_name = "deep_research_pipeline.py"
    else:
        script_path = find_script_path("gemini_research", scripts_dir)
        script_name = "gemini_research.py"

    if not script_path:
        print_error("Research script not found", f"Expected: scripts/{script_name}")
        raise typer.Abort()

    # Build command arguments
    cmd_args = [
        sys.executable,
        str(script_path),
        "--topic",
        topic,
        "--project",
        project,
    ]

    # Add depth
    if depth:
        cmd_args.extend(["--depth", depth])

    # For deep research, add template and class_id
    if deep:
        # Find template file
        template_path = kb_path / "OCDS_Documentation" / "05_Material_Templates" / template
        if not template_path.exists():
            # Try in Materials
            template_path = kb_path / "Materials" / template
        if not template_path.exists():
            # Try in root
            template_path = kb_path / template

        if not template_path.exists():
            print_error(f"Template not found: {template}")
            raise typer.Abort()

        cmd_args.extend(["--template", str(template_path)])

        # Add class-id if provided
        if class_id:
            cmd_args.extend(["--class-id", class_id])

        # For deep research, output is the output directory
        if output:
            cmd_args.extend(["--output-dir", output])
    else:
        # For standard research, always save to a file
        if not output:
            # Generate default output path
            output_dir = kb_path / config.get("paths.output_dir", "Materials")
            class_id = config.get("defaults.class_id", "TCM_101")
            output_dir = output_dir / class_id
            output_dir.mkdir(parents=True, exist_ok=True)

            # Create filename
            safe_topic = topic.replace(" ", "_").replace("/", "_")
            output = str(output_dir / f"Research_{safe_topic}.md")

        cmd_args.extend(["--output", output])

    # Run research script
    try:
        if deep:
            # For deep research, show live output with progress tracking
            import re
            import threading
            import time
            from collections import deque

            from rich.live import Live
            from rich.panel import Panel
            from rich.progress import BarColumn, Progress, ProgressColumn, SpinnerColumn, TextColumn
            from rich.table import Table
            from rich.text import Text

            # --- Shared State ---
            lock = threading.Lock()
            recent_lines = deque(maxlen=5)
            progress_status = {
                "description": "Initializing...",
                "completed": 0,
                "total": None,  # Start as indeterminate
            }

            # --- Custom Rich Column ---
            class CountColumn(ProgressColumn):
                """Renders the completed/total tasks, but only when the total is known."""

                def render(self, task) -> Text:
                    if task.total is None:
                        return Text("")
                    else:
                        return Text(f"({task.completed}/{task.total})", style="dim")

            # --- Renderable Class (The Correct Rich Pattern) ---
            class ProgressDisplay:
                """A renderable for Rich Live that displays progress."""

                def __init__(self):
                    self.progress = Progress(
                        SpinnerColumn(spinner_name="dots", style="cyan"),
                        TextColumn("[cyan]{task.description}"),
                        BarColumn(bar_width=40, style="grey50", complete_style="cyan"),
                        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                        CountColumn(),
                    )
                    self.task_id = self.progress.add_task("Overall Progress", total=None)  # Start as indeterminate

                def __rich__(self) -> Panel:
                    """Called by Live on every refresh to get the renderable."""
                    with lock:
                        self.progress.update(
                            self.task_id,
                            total=progress_status["total"],
                            completed=progress_status["completed"],
                            description=progress_status["description"],
                        )

                        log_table = Table.grid(padding=(0, 2), expand=True)
                        log_table.add_column(style="dim")
                        for line in recent_lines:
                            clean_line = re.sub(r"\x1b\[[0-9;]*m", "", line)
                            log_table.add_row(clean_line[:100])

                    layout = Table.grid(expand=True)
                    layout.add_row(self.progress)
                    layout.add_row("")
                    layout.add_row(log_table)

                    return Panel(layout, title="[cyan]Deep Research Progress", border_style="cyan", padding=(1, 2))

            # --- Background Worker ---
            def read_output(process):
                """Reads subprocess output and updates shared state."""
                total_headings = 0
                total_materials = 0
                totals_calculated = False

                for line in process.stdout:
                    line = line.strip()
                    if not line:
                        continue

                    with lock:
                        recent_lines.append(line)

                        # --- Update Description ---
                        step_match = re.search(r"STEP \d+: ([\w\s]+)", line)
                        if step_match:
                            progress_status["description"] = step_match.group(1).strip()

                        # --- Calculate Total ---
                        if line.startswith("TOTAL_HEADINGS:"):
                            total_headings = int(line.split(":")[1].strip())
                        elif line.startswith("TOTAL_MATERIALS:"):
                            total_materials = int(line.split(":")[1].strip())

                        if not totals_calculated and total_headings > 0 and total_materials > 0:
                            progress_status["total"] = 2 + total_headings + total_materials
                            totals_calculated = True

                        # --- Update Progress ---
                        if line == "COMPLETED: prompt":
                            progress_status["completed"] = 1
                        elif line == "COMPLETED: research":
                            progress_status["completed"] = 2
                        elif line.startswith("HEADING_COMPLETED:"):
                            if totals_calculated and progress_status["completed"] < progress_status["total"]:
                                progress_status["completed"] += 1
                        elif line.startswith("MATERIAL_COMPLETED:"):
                            if totals_calculated and progress_status["completed"] < progress_status["total"]:
                                progress_status["completed"] += 1
                            # Update description for the last phase
                            progress_status["description"] = "Generating Materials"

            # --- Main Execution ---
            env = {"GEMINI_API_KEY": api_key, "PYTHONUNBUFFERED": "1", **os.environ}
            process = subprocess.Popen(
                cmd_args, cwd=kb_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, env=env
            )

            reader_thread = threading.Thread(target=read_output, args=(process,), daemon=True)
            reader_thread.start()

            with Live(ProgressDisplay(), refresh_per_second=10, console=console) as live:
                while reader_thread.is_alive():
                    time.sleep(0.1)

            # Final state update to show 100%
            with lock:
                progress_status["description"] = "Complete!"
                if progress_status["total"] != 100:  # If we have a real total
                    progress_status["completed"] = progress_status["total"]

            # Short live display to show the final "Complete!" status
            with Live(ProgressDisplay(), refresh_per_second=10, console=console, transient=True) as live:
                time.sleep(0.2)

            process.wait()
            result = type("Result", (), {"returncode": process.returncode})()
            print()
        else:
            # For standard research, use progress bar
            with create_progress() as progress:
                task = progress.add_task(f"[cyan]Researching {topic}...", total=None)

                result = subprocess.run(
                    cmd_args, cwd=kb_path, capture_output=True, text=True, env={"GEMINI_API_KEY": api_key, **os.environ}
                )

        if result.returncode == 0:
            print_success("Research complete!")

            # Print script output for standard research
            if not deep and result.stdout:
                print(result.stdout)

            # Show where file was saved
            if output:
                from ..utils.output import print_info

                print_info(f"Saved to: {output}")
        else:
            print_error("Research failed")
            if hasattr(result, "stderr") and result.stderr:
                print(result.stderr)
            raise typer.Abort()

    except Exception as e:
        print_error(f"Failed to run research: {e}")
        raise typer.Abort()
