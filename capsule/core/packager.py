import json
import logging
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from capsule.exceptions import FileError
from capsule.models.cypher import CapsuleCypher

logger = logging.getLogger(__name__)


class Packager:
    """Handles the low-level logic for packaging a capsule."""

    def __init__(self, capsule_path: Path, cypher: dict | None = None):
        self.capsule_path = capsule_path
        self.cypher = cypher or {}
        logger.debug(f"Packager initialized for capsule path: {self.capsule_path}")

    def generate_cypher(
        self,
        capsule_id: str,
        name: str,
        version: str,
        domain_type: str,
        sequence_mode: str = "freeform",
        data_schemas: dict[str, Any] | None = None,
    ) -> CapsuleCypher:
        """
        Generates a CapsuleCypher object by scanning the capsule directory.

        Args:
            capsule_id: Unique identifier for the capsule
            name: Human-readable name
            version: Semantic version string
            domain_type: Content domain type
            sequence_mode: Learning sequence type (default: "freeform")
            data_schemas: Optional dictionary of data schemas

        Returns:
            CapsuleCypher object representing the capsule content
        """
        logger.debug(f"Generating cypher for capsule: {name} ({capsule_id})")

        folder_structure = {}
        contents = {}

        # Scan top-level directories
        for item in self.capsule_path.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                folder_name = item.name
                # Map logical name to folder path (using folder name as logical name)
                folder_structure[folder_name] = f"{folder_name}/"

                # Scan files within this directory (recursive)
                files = []
                for file_path in item.rglob("*"):
                    if file_path.is_file() and not file_path.name.startswith("."):
                        # Store relative path
                        rel_path = str(file_path.relative_to(self.capsule_path))
                        files.append(rel_path)
                contents[folder_name] = sorted(files)

        # Handle root files (optional, putting them in a 'root' category if they exist)
        root_files = []
        for item in self.capsule_path.iterdir():
            if item.is_file() and not item.name.startswith("."):
                root_files.append(item.name)

        if root_files:
            contents["root"] = sorted(root_files)

        return CapsuleCypher(
            capsule_id=capsule_id,
            name=name,
            version=version,
            domain_type=domain_type,
            folder_structure=folder_structure,
            contents=contents,
            data_schemas=data_schemas or {},
            sequence_mode=sequence_mode,
        )

    def generate_manifest(self) -> dict:
        logger.debug("Generating export manifest.")
        manifest = {
            "capsule_id": self.cypher.get("capsule_id"),
            "version": self.cypher.get("version"),
            "export_date": datetime.now(timezone.utc).isoformat(),
            "files": [str(p.relative_to(self.capsule_path)) for p in self.capsule_path.rglob("*") if p.is_file()],
        }
        logger.debug(f"Manifest generated with {len(manifest['files'])} files.")
        return manifest

    def package_to_zip(self, output_path: Path):
        logger.info(f"Packaging capsule to zip archive at: {output_path}")
        try:
            manifest = self.generate_manifest()
            with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
                zf.writestr("export-manifest.json", json.dumps(manifest, indent=2))
                for file_path in self.capsule_path.rglob("*"):
                    if file_path.is_file():
                        arcname = file_path.relative_to(self.capsule_path)
                        zf.write(file_path, arcname)
            logger.info(f"Successfully created zip archive at: {output_path}")
        except OSError as e:
            logger.error(f"Failed to create zip archive at {output_path}: {e}", exc_info=True)
            raise FileError(f"Failed to create zip archive at {output_path}: {e}") from e

    def package_to_folder(self, output_path: Path):
        logger.info(f"Packaging capsule to folder at: {output_path}")
        try:
            manifest = self.generate_manifest()
            if output_path.exists():
                logger.warning(f"Output path {output_path} exists. Removing it.")
                shutil.rmtree(output_path)
            shutil.copytree(self.capsule_path, output_path)
            with open(output_path / "export-manifest.json", "w") as f:
                json.dump(manifest, f, indent=2)
            logger.info(f"Successfully created folder bundle at: {output_path}")
        except OSError as e:
            logger.error(f"Failed to create folder bundle at {output_path}: {e}", exc_info=True)
            raise FileError(f"Failed to create folder bundle at {output_path}: {e}") from e
