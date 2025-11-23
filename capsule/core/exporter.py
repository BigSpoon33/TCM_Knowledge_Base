import logging
from pathlib import Path

import yaml

from capsule.core.packager import Packager
from capsule.core.validator import Validator

logger = logging.getLogger(__name__)


class Exporter:
    """Handles the high-level logic for exporting a capsule."""

    def __init__(self, capsule_path: Path):
        logger.debug(f"Exporter initialized for capsule path: {capsule_path}")
        self.capsule_path = capsule_path
        self.validator = Validator(self.capsule_path)
        self.cypher_path = self.capsule_path / "capsule-cypher.yaml"

        with open(self.cypher_path) as f:
            self.cypher = yaml.safe_load(f)

        self.packager = Packager(self.capsule_path, self.cypher)

    def validate_capsule(self):
        logger.info(f"Starting validation for capsule: {self.capsule_path}")
        self.validator.validate_capsule()
        logger.info("Capsule validation successful.")

    def export_to_zip(self, output_path: Path):
        logger.info(f"Exporting capsule to zip: {output_path}")
        self.validate_capsule()
        self.packager.package_to_zip(output_path)

    def export_to_folder(self, output_path: Path):
        logger.info(f"Exporting capsule to folder: {output_path}")
        self.validate_capsule()
        self.packager.package_to_folder(output_path)
