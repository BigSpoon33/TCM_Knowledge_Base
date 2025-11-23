"""Import capsule with preview and analysis capabilities."""

import shutil
import tempfile
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import frontmatter
import typer
import yaml
from jinja2 import Environment, FileSystemLoader
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from capsule.core.merger import merge_notes
from capsule.core.validator import Validator
from capsule.exceptions import CapsuleError, ConfigError, FileError, ValidationError
from capsule.models.capsule import Capsule
from capsule.models.config import Config
from capsule.models.cypher import CapsuleCypher
from capsule.models.note import Note
from capsule.utils import dataview_queries
from capsule.utils.backup import create_backup
from capsule.utils.versioning import compare_versions
from capsule.utils.file_ops import FileOps
from capsule.utils.yaml_handler import YAMLHandler


@dataclass
class CapsuleInfo:
    """Metadata about the capsule."""

    id: str
    version: str
    file_count: int
    name: str
    domain_type: str


@dataclass
class Impact:
    """Summary of import impact."""

    new_files: int
    updated_files: int
    conflicts: int


@dataclass
class UpdateDetail:
    """Details about a file update."""

    file: str
    strategy: str
    changes: str


@dataclass
class ConflictDetail:
    """Details about a file conflict."""

    file: str
    reason: str
    sources: list[str]


@dataclass
class ImportPreview:
    """
    Data structure representing the import preview.

    Contains all information needed to display what will happen during import.
    """

    capsule_info: CapsuleInfo
    impact: Impact
    new_files: list[str]
    updates: list[UpdateDetail]
    conflicts: list[ConflictDetail]
    import_type: str = "NEW"
    version_diff: str | None = None


class Importer:
    """
    Handles the capsule import process, including extraction, validation,
    and preview generation.

    Security:
        - Validates zip file paths to prevent path traversal attacks.
        - Creates backups before modifying the vault.
    """

    def __init__(self, config: Config, dry_run: bool = False):
        """
        Initialize importer with user configuration.

        Args:
            config: User configuration containing vault path and settings
            dry_run: If True, simulate operations without modifying vault
        """
        self.config = config
        self.dry_run = dry_run
        self.file_ops = FileOps(dry_run=dry_run)
        self.console = Console()
        self.extracted_path: Path | None = None
        self.temp_dir: str | None = None
        self.cypher: CapsuleCypher | None = None

    def run(self, capsule_path: Path, no_backup: bool = False) -> None:
        """
        Run the import process with preview.

        Args:
            capsule_path: Path to capsule file (.capsule zip) or folder
            no_backup: If True, skips the backup process

        Raises:
            ConfigError: If vault path is not configured
            FileError: If capsule path doesn't exist
        """
        # Create backup if requested
        backup_path = None
        if not no_backup and not self.dry_run:
            vault_path_str = self.config.get("user.vault_path")
            if not vault_path_str:
                raise ConfigError(
                    "Vault path is not set in the configuration.",
                    hint="Run 'capsule config --vault-path <path>' to set it.",
                )
            vault_path = Path(vault_path_str)

            backup_dir_str = self.config.get("import.backup_location", str(Path.home() / ".capsule" / "backups"))
            backup_dir = Path(backup_dir_str)

            typer.echo("Creating vault backup...")
            backup_path = create_backup(vault_path, backup_dir)
            typer.echo(f"Backup created at: {backup_path}")
        elif self.dry_run and not no_backup:
            typer.echo("[DRY RUN] Would create vault backup")

        try:
            # Extract capsule (handles both zip and folder)
            self.extract_capsule(capsule_path)

            # Load and parse cypher
            self.load_cypher()

            # Validate capsule structure
            self.validate_capsule()

            # Analyze impact on vault
            vault_path = Path(self.config.get("user.vault_path"))
            preview = self.analyze_impact(vault_path)

            # Display preview
            self.display_preview(preview)

            # TODO: In future stories (7-6), add interactive approval here
            typer.echo("\n" + "=" * 50)
            typer.secho(
                "ℹ️  Preview complete. Actual import execution will be implemented in story 7-6.", fg=typer.colors.BLUE
            )
            typer.echo("=" * 50)

        except Exception as e:
            if backup_path:
                typer.echo(f"Your vault has been backed up at: {backup_path}")

            if isinstance(e, CapsuleError):
                raise e
            raise CapsuleError(f"Error during import: {e}") from e
        finally:
            # Clean up temporary extraction directory
            self.cleanup()

    def extract_capsule(self, capsule_path: Path) -> None:
        """
        Extract capsule from zip archive or use folder directly.

        Security:
            - Checks for path traversal attempts in zip archives.
            - Raises ValueError if a file path attempts to escape the extraction directory.

        Args:
            capsule_path: Path to .capsule zip file or capsule folder

        Raises:
            FileError: If capsule path doesn't exist
            zipfile.BadZipFile: If zip file is corrupted
            ValidationError: If path traversal is detected
        """
        if not capsule_path.exists():
            raise FileError(f"Capsule not found: {capsule_path}")

        if capsule_path.is_dir():
            # Already a directory, use it directly
            self.extracted_path = capsule_path
            typer.echo(f"Using capsule folder: {capsule_path}")
        else:
            # Extract zip archive to temporary directory
            self.temp_dir = tempfile.mkdtemp(prefix="capsule_import_")
            extract_to = Path(self.temp_dir)

            typer.echo(f"Extracting capsule archive: {capsule_path}")
            with zipfile.ZipFile(capsule_path, "r") as zip_ref:
                # Validate paths to prevent path traversal attacks (Python < 3.11.4)
                for member in zip_ref.namelist():
                    member_path = (extract_to / member).resolve()
                    try:
                        member_path.relative_to(extract_to.resolve())
                    except ValueError:
                        raise ValidationError(
                            f"Path traversal detected in archive: {member}",
                            hint="The capsule archive contains malicious paths.",
                        )

                zip_ref.extractall(extract_to)

            # Find the root capsule directory (handle nested structure)
            # Look for capsule-cypher.yaml in extracted contents
            cypher_candidates = list(extract_to.rglob("capsule-cypher.yaml"))
            if not cypher_candidates:
                raise ValidationError(
                    f"No capsule-cypher.yaml found in archive: {capsule_path}",
                    hint="Ensure the archive is a valid capsule.",
                )

            self.extracted_path = cypher_candidates[0].parent
            typer.echo(f"Capsule extracted to: {self.extracted_path}")

    def load_cypher(self) -> None:
        """
        Load and parse the capsule-cypher.yaml file.

        Raises:
            FileError: If cypher file doesn't exist
            ValidationError: If cypher structure is invalid
        """
        if not self.extracted_path:
            raise ValidationError("Capsule must be extracted before loading cypher")

        cypher_path = self.extracted_path / "capsule-cypher.yaml"
        if not cypher_path.exists():
            raise FileError(f"capsule-cypher.yaml not found in {self.extracted_path}")

        typer.echo("Loading capsule cypher...")
        cypher_data = YAMLHandler.read(cypher_path)
        self.cypher = CapsuleCypher.from_dict(cypher_data)
        typer.echo(f"Loaded cypher for: {self.cypher.name} v{self.cypher.version}")

    def validate_capsule(self) -> None:
        """
        Validate capsule structure using existing Validator.

        Raises:
            ValidationError: If validation fails
        """
        if not self.extracted_path:
            raise ValidationError("Capsule must be extracted before validation")

        typer.echo("Validating capsule structure...")
        validator = Validator(self.extracted_path)
        validator.validate_capsule()
        typer.secho("✓ Capsule validation passed", fg=typer.colors.GREEN)

    def analyze_impact(self, vault_path: Path) -> ImportPreview:
        """
        Analyze the impact of importing this capsule on the vault.

        Compares capsule files with existing vault files to determine:
        - New files (not in vault)
        - Updated files (in both capsule and vault)
        - Potential conflicts (different capsule sources)
        - Version conflicts (downgrades)

        Args:
            vault_path: Path to Obsidian vault

        Returns:
            ImportPreview object with analysis results
        """
        if not self.cypher or not self.extracted_path:
            raise ValidationError("Cypher must be loaded before impact analysis")

        typer.echo("Analyzing impact on vault...")

        # Check for installed version
        import_type = "NEW"
        version_diff = None

        # Check for installed version in the capsule-specific directory
        # We assume the capsule metadata is stored in vault_path / capsule_id / capsule-cypher.yaml
        installed_cypher_path = vault_path / self.cypher.capsule_id / "capsule-cypher.yaml"

        if installed_cypher_path.exists():
            try:
                installed_data = YAMLHandler.read(installed_cypher_path)
                installed_cypher = CapsuleCypher.from_dict(installed_data)

                if installed_cypher.capsule_id == self.cypher.capsule_id:
                    installed_version = installed_cypher.version

                    # Compare versions
                    try:
                        comparison = compare_versions(self.cypher.version, installed_version)

                        if comparison > 0:
                            import_type = "UPDATE"
                            version_diff = f"{installed_version} -> {self.cypher.version}"
                        elif comparison < 0:
                            import_type = "DOWNGRADE"
                            version_diff = f"{installed_version} -> {self.cypher.version}"
                        else:
                            import_type = "SAME"
                            version_diff = f"{installed_version} (Reinstall)"
                    except ValueError as e:
                        typer.echo(f"Warning: Version comparison failed: {e}")

            except Exception as e:
                # If we can't read the installed cypher, assume NEW or ignore
                typer.echo(f"Warning: Could not read installed capsule-cypher.yaml: {e}")

        # Collect all capsule files
        capsule_files = self._collect_capsule_files()

        new_files = []
        updates = []
        conflicts = []

        for rel_path in capsule_files:
            vault_file = vault_path / rel_path
            capsule_file = self.extracted_path / rel_path

            if not vault_file.exists():
                # File doesn't exist in vault - will be created
                new_files.append(str(rel_path))
            else:
                # File exists - analyze for updates/conflicts
                update_info = self._analyze_file_update(vault_file, capsule_file, rel_path)

                if update_info.get("conflict"):
                    conflicts.append(
                        ConflictDetail(
                            file=update_info["file"],
                            reason=update_info["reason"],
                            sources=update_info["sources"],
                        )
                    )
                else:
                    updates.append(
                        UpdateDetail(
                            file=update_info["file"],
                            strategy=update_info["strategy"],
                            changes=update_info["changes"],
                        )
                    )

        # Analyze Dashboards
        capsule_dashboard_rel = Path(self.cypher.capsule_id) / "capsule-dashboard.md"
        capsule_dashboard_path = vault_path / capsule_dashboard_rel
        master_dashboard_path = vault_path / "Master Dashboard.md"

        # Capsule Dashboard
        if not capsule_dashboard_path.exists():
            new_files.append(str(capsule_dashboard_rel))
        else:
            updates.append(
                UpdateDetail(
                    file=str(capsule_dashboard_rel),
                    strategy="section-level",
                    changes="Will merge dashboard sections",
                )
            )

        # Master Dashboard
        if not master_dashboard_path.exists():
            new_files.append("Master Dashboard.md")

        # Count file statistics
        impact = Impact(new_files=len(new_files), updated_files=len(updates), conflicts=len(conflicts))

        # Capsule metadata
        capsule_info = CapsuleInfo(
            id=self.cypher.capsule_id,
            name=self.cypher.name,
            version=self.cypher.version,
            domain_type=self.cypher.domain_type,
            file_count=len(capsule_files),
        )

        return ImportPreview(
            capsule_info,
            impact,
            new_files,
            updates,
            conflicts,
            import_type=import_type,
            version_diff=version_diff,
        )

    def _collect_capsule_files(self) -> list[str]:
        """
        Collect all file paths from cypher contents.

        Returns:
            List of relative file paths
        """
        files = []
        contents = self.cypher.contents

        for content_type, items in contents.items():
            if isinstance(items, list):
                # Direct list of files
                for item in items:
                    if isinstance(item, dict) and "file" in item:
                        files.append(item["file"])
            elif isinstance(items, dict):
                # Nested structure (e.g., study_material -> flashcards -> files)
                for sub_type, sub_items in items.items():
                    if isinstance(sub_items, list):
                        for item in sub_items:
                            if isinstance(item, dict) and "file" in item:
                                files.append(item["file"])

        return files

    def _analyze_file_update(self, vault_file: Path, capsule_file: Path, rel_path: str) -> dict[str, Any]:
        """
        Analyze how a specific file will be updated.

        Determines merge strategy and detects conflicts.

        Args:
            vault_file: Existing file in vault
            capsule_file: Incoming file from capsule
            rel_path: Relative path for display

        Returns:
            Dictionary with update details
        """
        try:
            # Parse frontmatter from both files
            vault_note = frontmatter.load(vault_file)
            capsule_note = frontmatter.load(capsule_file)

            vault_sources = vault_note.metadata.get("source_capsules", [])
            incoming_capsule = self.cypher.capsule_id

            # Determine merge strategy
            if incoming_capsule in vault_sources:
                # Same capsule update - section-level merge
                strategy = "section-level"
                changes = "Will update matching sections with new data"
                conflict = False
            else:
                # Different capsule - additive merge
                strategy = "additive"

                # Check for domain section conflicts
                conflict_sections = self._detect_section_conflicts(vault_note.metadata, capsule_note.metadata)

                if conflict_sections:
                    conflict = True
                    changes = f"Conflict in sections: {', '.join(conflict_sections)}"
                    return {
                        "file": str(rel_path),
                        "conflict": True,
                        "reason": changes,
                        "sources": vault_sources + [incoming_capsule],
                    }
                else:
                    conflict = False
                    changes = "Will add new domain sections"

            return {"file": str(rel_path), "strategy": strategy, "changes": changes, "conflict": False}

        except yaml.YAMLError as e:
            # YAML parsing error in frontmatter
            return {
                "file": str(rel_path),
                "strategy": "replace",
                "changes": f"Will replace file (invalid YAML in frontmatter: {e})",
                "conflict": False,
            }
        except UnicodeDecodeError as e:
            # File encoding error
            return {
                "file": str(rel_path),
                "strategy": "replace",
                "changes": f"Will replace file (encoding error: {e})",
                "conflict": False,
            }
        except Exception as e:
            # Generic fallback for other parsing errors
            return {
                "file": str(rel_path),
                "strategy": "replace",
                "changes": f"Will replace file (frontmatter parse error: {e})",
                "conflict": False,
            }

    def _detect_section_conflicts(self, existing_fm: dict[str, Any], incoming_fm: dict[str, Any]) -> list[str]:
        """
        Detect conflicting domain sections between two frontmatters.

        Args:
            existing_fm: Existing note's frontmatter
            incoming_fm: Incoming note's frontmatter

        Returns:
            List of conflicting section names
        """
        conflicts = []

        # Check for domain sections (keys ending with '_data')
        for key in incoming_fm.keys():
            if key.endswith("_data") and key in existing_fm:
                # Both have the same domain section - potential conflict
                conflicts.append(key)

        return conflicts

    def display_preview(self, preview: ImportPreview) -> None:
        """
        Display formatted import preview using rich library.

        Args:
            preview: ImportPreview object with analysis results
        """
        console = Console()

        # Header
        console.print()
        console.print(Panel.fit("[bold cyan]Capsule Import Preview[/bold cyan]", border_style="cyan"))
        console.print()

        # Import Type & Version Warning
        if preview.import_type == "DOWNGRADE":
            console.print(f"[bold red]⚠️  DOWNGRADE DETECTED: {preview.version_diff}[/bold red]")
            console.print()
        elif preview.import_type == "UPDATE":
            console.print(f"[bold green]Update Available: {preview.version_diff}[/bold green]")
            console.print()
        elif preview.import_type == "SAME":
            console.print(f"[bold yellow]Reinstalling same version: {preview.version_diff}[/bold yellow]")
            console.print()
        else:
            console.print("[bold green]New Installation[/bold green]")
            console.print()

        # Capsule metadata
        console.print("[bold]Capsule Information:[/bold]")
        info = preview.capsule_info
        console.print(f"  ID:           {info.id}")
        console.print(f"  Name:         {info.name}")
        console.print(f"  Version:      {info.version}")
        console.print(f"  Domain:       {info.domain_type}")
        console.print(f"  Total Files:  {info.file_count}")
        console.print()

        # Impact summary
        console.print("[bold]Impact Analysis:[/bold]")
        impact = preview.impact
        console.print(f"  [green]New files:      {impact.new_files}[/green]")
        console.print(f"  [yellow]Updated files:  {impact.updated_files}[/yellow]")

        if impact.conflicts > 0:
            console.print(f"  [red]Conflicts:      {impact.conflicts}[/red]")
        else:
            console.print(f"  [green]Conflicts:      {impact.conflicts}[/green]")
        console.print()

        # New files list (limited to first 10)
        if preview.new_files:
            console.print("[bold green]New Files to be Created:[/bold green]")
            display_count = min(10, len(preview.new_files))
            for file_path in preview.new_files[:display_count]:
                console.print(f"  + {file_path}")

            if len(preview.new_files) > 10:
                remaining = len(preview.new_files) - 10
                console.print(f"  ... and {remaining} more files")
            console.print()

        # Updated files
        if preview.updates:
            console.print("[bold yellow]Files to be Updated:[/bold yellow]")

            table = Table(show_header=True, header_style="bold yellow")
            table.add_column("File", style="dim")
            table.add_column("Strategy")
            table.add_column("Changes")

            display_count = min(10, len(preview.updates))
            for update in preview.updates[:display_count]:
                table.add_row(update.file, update.strategy, update.changes)

            console.print(table)

            if len(preview.updates) > 10:
                remaining = len(preview.updates) - 10
                console.print(f"\n  ... and {remaining} more files")
            console.print()

        # Conflicts
        if preview.conflicts:
            console.print("[bold red]⚠️  Conflicts Detected:[/bold red]")

            table = Table(show_header=True, header_style="bold red")
            table.add_column("File", style="dim")
            table.add_column("Reason", style="red")
            table.add_column("Sources")

            for conflict in preview.conflicts:
                sources = ", ".join(conflict.sources)
                table.add_row(conflict.file, conflict.reason, sources)

            console.print(table)
            console.print()
            console.print("[red]⚠️  These conflicts must be resolved before import can proceed.[/red]")

    def generate_preview(self, vault_path: Path) -> ImportPreview:
        """
        Public method to generate preview.

        This is an alias for analyze_impact() to match the architecture
        specification in architecture.md.

        Args:
            vault_path: Path to Obsidian vault

        Returns:
            ImportPreview object
        """
        return self.analyze_impact(vault_path)

    def execute_import(self, preview: ImportPreview) -> None:
        """
        Execute the import based on the preview.

        Args:
            preview: The import preview containing files to process
        """
        typer.echo("\nExecuting import...")

        vault_path = Path(self.config.get("user.vault_path"))

        # Handle New Files
        for rel_path in preview.new_files:
            # Skip dashboard files as they are generated later
            if str(rel_path).endswith("capsule-dashboard.md") or str(rel_path) == "Master Dashboard.md":
                continue

            src = self.extracted_path / rel_path
            dst = vault_path / rel_path

            # Ensure parent dir exists
            self.file_ops.mkdir(dst.parent, parents=True, exist_ok=True)

            self.file_ops.copy(src, dst)
            if not self.dry_run:
                typer.echo(f"Created: {rel_path}")

        # Handle Updates
        for update in preview.updates:
            if update.strategy in ["section-level", "additive"]:
                typer.echo(
                    f"Skipping update for {update.file}: Merge strategy '{update.strategy}' not implemented yet (Epic 8)"
                )
            elif update.strategy == "replace":
                src = self.extracted_path / update.file
                dst = vault_path / update.file
                self.file_ops.copy(src, dst)
                if not self.dry_run:
                    typer.echo(f"Updated (Replaced): {update.file}")

        # Generate Dashboards
        typer.echo("\nGenerating dashboards...")
        capsule = Capsule(
            capsule_id=preview.capsule_info.id,
            name=preview.capsule_info.name,
            version=preview.capsule_info.version,
            domain_type=preview.capsule_info.domain_type,
            dashboard_metadata=self.cypher.dashboard_metadata if self.cypher else None,
        )
        self.generate_dashboards(capsule, vault_path)

        if self.dry_run:
            typer.secho("\n✅ Dry run complete! No files were modified.", fg=typer.colors.YELLOW)
        else:
            typer.secho("\n✅ Import execution completed.", fg=typer.colors.GREEN)

    def generate_dashboards(self, capsule: Capsule, vault_path: Path) -> list[Path]:
        """
        Generate master and capsule dashboards during import.

        Args:
            capsule: The capsule model
            vault_path: Path to the vault

        Returns:
            List of generated dashboard file paths
        """
        generated_files = []

        try:
            # Load templates
            # Assuming templates are relative to the package or current working directory
            template_dir = Path("capsule/templates")
            if not template_dir.exists():
                # Fallback or error handling
                pass

            env = Environment(loader=FileSystemLoader(str(template_dir)))
            env.globals["now"] = lambda: datetime.now(timezone.utc).isoformat()

            # 1. Capsule Dashboard
            capsule_template = env.get_template("capsule-dashboard.md.j2")

            # Render capsule dashboard
            domain_sections = self.load_domain_sections(capsule.domain_type, capsule.capsule_id)

            capsule_dashboard_content = capsule_template.render(
                capsule=capsule, domain_sections=domain_sections, dv=dataview_queries
            )

            # Write capsule dashboard
            capsule_dir = vault_path / capsule.capsule_id
            self.file_ops.mkdir(capsule_dir, parents=True, exist_ok=True)
            capsule_dashboard_path = capsule_dir / "capsule-dashboard.md"

            if capsule_dashboard_path.exists() and not self.dry_run:
                # Merge with existing dashboard
                # Parse generated content to create Note object
                post = frontmatter.loads(capsule_dashboard_content)
                new_note = Note(
                    file_path=str(capsule_dashboard_path),
                    frontmatter=post.metadata,
                    body=post.content,
                )

                existing_note = Note.from_file(str(capsule_dashboard_path))
                merged_note = merge_notes(existing_note, new_note, capsule.capsule_id)
                merged_note.to_file(str(capsule_dashboard_path))
                typer.echo(f"Updated capsule dashboard (merged): {capsule_dashboard_path}")
            elif capsule_dashboard_path.exists() and self.dry_run:
                typer.echo(f"[DRY RUN] Would update capsule dashboard (merged): {capsule_dashboard_path}")
            else:
                # Write new dashboard
                self.file_ops.write_text(capsule_dashboard_path, capsule_dashboard_content, encoding="utf-8")
                if not self.dry_run:
                    typer.echo(f"Generated capsule dashboard: {capsule_dashboard_path}")

            generated_files.append(capsule_dashboard_path)

            # 2. Master Dashboard
            master_dashboard_path = vault_path / "Master Dashboard.md"
            if not master_dashboard_path.exists():
                master_template = env.get_template("master-dashboard.md.j2")
                master_content = master_template.render(dv=dataview_queries)
                self.file_ops.write_text(master_dashboard_path, master_content, encoding="utf-8")
                generated_files.append(master_dashboard_path)
                if not self.dry_run:
                    typer.echo(f"Generated master dashboard: {master_dashboard_path}")
            else:
                typer.echo(f"Master dashboard already exists: {master_dashboard_path}")

        except Exception as e:
            typer.echo(f"Error generating dashboards: {e}")
            # Cleanup any dashboards generated before failure
            for f in generated_files:
                if f.exists() and not self.dry_run:
                    try:
                        f.unlink()
                        typer.echo(f"Rolled back: {f}")
                    except Exception as cleanup_error:
                        typer.echo(f"Failed to cleanup {f}: {cleanup_error}")
            raise e

        return generated_files

    def load_domain_sections(self, domain_type: str, capsule_id: str) -> str:
        """
        Load and render domain-specific dashboard sections.

        Args:
            domain_type: The domain type of the capsule (e.g., "traditional_chinese_medicine")
            capsule_id: The ID of the capsule

        Returns:
            Rendered markdown content for the domain sections
        """
        # Map domain type to template name
        domain_map = {
            "traditional_chinese_medicine": "tcm.md.j2",
            "tcm": "tcm.md.j2",
        }

        template_name = domain_map.get(domain_type.lower(), f"{domain_type.lower()}.md.j2")

        try:
            # Assuming templates are relative to the package or current working directory
            # Adjust path as necessary based on deployment
            template_dir = Path("capsule/templates/domains")
            if not template_dir.exists():
                # Fallback for installed package scenario if needed, but for now assuming dev structure
                pass

            env = Environment(loader=FileSystemLoader(str(template_dir)))
            template = env.get_template(template_name)
            return template.render(capsule_id=capsule_id, dv=dataview_queries)
        except Exception as e:
            # Only warn if it was a mapped domain or if we really expected it to exist?
            # If dynamic lookup fails, it might just mean no domain section is defined, which is fine.
            # But get_template raises TemplateNotFound.
            if "TemplateNotFound" not in str(e):
                typer.echo(f"Warning: Could not load domain template for {domain_type}: {e}")
            return ""

    def cleanup(self) -> None:
        """Clean up temporary extraction directory if it exists."""
        if self.temp_dir and Path(self.temp_dir).exists():
            shutil.rmtree(self.temp_dir)
            self.temp_dir = None
