import zipfile
from pathlib import Path
from typing import Dict, List
import yaml
import json
from datetime import datetime, timezone

from capsule.core.validator import Validator


class Exporter:
    """Handles the logic for exporting a capsule."""

    def __init__(self, capsule_path: Path):
        """
        Initializes the Exporter.

        Args:
            capsule_path: The path to the capsule directory.
        """
        self.capsule_path = capsule_path
        self.validator = Validator(self.capsule_path)
        self.cypher_path = self.capsule_path / "capsule-cypher.yaml"
        with open(self.cypher_path, "r") as f:
            self.cypher = yaml.safe_load(f)

    def validate_capsule(self) -> bool:
        """
        Runs validation on the capsule before exporting.

        Returns:
            True if the capsule is valid, False otherwise.
        """
        try:
            self.validator.validate_capsule()
            print("Capsule validation successful.")
            return True
        except (ValueError, FileNotFoundError, FileExistsError, TypeError) as e:
            print(f"Capsule validation failed: {e}")
            return False

    def generate_manifest(self) -> Dict:
        """
        Generates an export manifest.

        Returns:
            A dictionary representing the export manifest.
        """
        manifest = {
            "capsule_id": self.cypher.get("capsule_id"),
            "version": self.cypher.get("version"),
            "export_date": datetime.now(timezone.utc).isoformat(),
            "files": [str(p.relative_to(self.capsule_path)) for p in self.capsule_path.rglob("*") if p.is_file()],
        }
        return manifest

    def export_to_zip(self, output_path: Path):
        """
        Packages the capsule into a .capsule zip archive.

        Args:
            output_path: The path to save the exported .capsule file.
        """
        if not self.validate_capsule():
            return

        manifest = self.generate_manifest()

        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
            # Add manifest
            zf.writestr("export-manifest.json", json.dumps(manifest, indent=2))

            for file_path in self.capsule_path.rglob("*"):
                if file_path.is_file():
                    arcname = file_path.relative_to(self.capsule_path)
                    zf.write(file_path, arcname)
        print(f"Successfully exported capsule to {output_path}")

    def export_to_folder(self, output_path: Path):
        """
        Packages the capsule into a folder bundle.

        Args:
            output_path: The path to save the exported folder.
        """
        import shutil

        if not self.validate_capsule():
            return

        manifest = self.generate_manifest()

        if output_path.exists():
            shutil.rmtree(output_path)
        shutil.copytree(self.capsule_path, output_path)

        # Add manifest
        with open(output_path / "export-manifest.json", "w") as f:
            json.dump(manifest, f, indent=2)

        print(f"Successfully exported capsule to {output_path}")
