import logging
import os
import uuid
import shutil
from pathlib import Path
from capsule.models.capsule import Capsule
from capsule.models.cypher import CapsuleCypher
import frontmatter

logger = logging.getLogger(__name__)


from capsule.core.validator import Validator
from ruamel.yaml import YAML


class CapsulePackager:
    """Core logic for packaging capsules."""

    def __init__(self, capsule: Capsule, capsule_path: str, output_dir: str) -> None:
        """
        Initialize the CapsulePackager.

        Args:
            capsule: The capsule to be packaged.
            capsule_path: The path to the capsule to be packaged.
            output_dir: The directory to output the packaged capsule to.
        """
        print("Initializing CapsulePackager")
        self.capsule = capsule
        self.capsule_path = Path(capsule_path)
        self.output_dir = Path(output_dir)

        if not self.capsule_path.is_dir():
            logger.error(f"Capsule path {self.capsule_path} not found or not a directory.")
            raise FileNotFoundError(f"Capsule path {self.capsule_path} not found or not a directory.")

        logger.info(f"CapsulePackager initialized for capsule {self.capsule.capsule_id}")

    def _scan_schemas(self) -> dict:
        """Load the data schemas from the domain schema file."""
        logger.info(f"Loading data schemas for domain {self.capsule.domain_type}")
        # Assume the command is run from the project root.
        # A more robust solution might involve finding the project root dynamically.
        project_root = Path.cwd()
        domain_schema_path = project_root / f"capsule/templates/domains/{self.capsule.domain_type}.yaml"
        data_schemas = {}
        if domain_schema_path.is_file():
            with open(domain_schema_path, "r") as f:
                yaml = YAML()
                domain_schema = yaml.load(f)
                data_schemas = domain_schema.get("data_schemas", {})
        else:
            logger.warning(f"Domain schema file not found at {domain_schema_path}")
        logger.info(f"Loaded {len(data_schemas)} data schemas for domain {self.capsule.domain_type}")
        return data_schemas

    def generate_cypher(self) -> CapsuleCypher:
        """
        Generate the capsule-cypher.yaml file.

        Returns:
            The CapsuleCypher object.
        """
        logger.info(f"Generating cypher for capsule {self.capsule.capsule_id}")
        contents, folder_structure = self._scan_contents()
        data_schemas = self._scan_schemas()
        cypher = CapsuleCypher(
            capsule_id=self.capsule.capsule_id,
            name=self.capsule.name,
            version=self.capsule.version,
            domain_type=self.capsule.domain_type,
            folder_structure=folder_structure,
            contents=contents,
            data_schemas=data_schemas,
        )
        logger.info(f"Cypher generated for capsule {self.capsule.capsule_id}")
        return cypher

    def _generate_unique_id(self, file_path: Path) -> str:
        """Generate a unique ID for a file."""
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, str(file_path)))

    def _scan_contents(self) -> tuple[dict, dict]:
        """Scan the capsule directory for markdown files and folder structure."""
        logger.info(f"Scanning contents of {self.capsule_path}")
        contents = {}
        folder_structure = {}
        for root, dirs, files in os.walk(self.capsule_path):
            root_path = Path(root)
            relative_root = root_path.relative_to(self.capsule_path)

            # Skip the root directory itself for folder_structure
            if str(relative_root) != ".":
                folder_key = str(relative_root).replace(os.sep, "_")
                folder_structure[folder_key] = str(relative_root.as_posix())

            for d in sorted(dirs):
                dir_path = root_path / d
                relative_dir = dir_path.relative_to(self.capsule_path)
                folder_key = str(relative_dir).replace(os.sep, "_")
                contents[folder_key] = []
                folder_structure[folder_key] = str(relative_dir.as_posix())

            for file in sorted(files):
                if file.endswith(".md"):
                    file_path = root_path / file
                    relative_file_path = file_path.relative_to(self.capsule_path)
                    folder_key = str(relative_file_path.parent).replace(os.sep, "_")
                    if folder_key == ".":
                        folder_key = "root"

                    if folder_key not in contents:
                        contents[folder_key] = []

                    contents[folder_key].append(
                        {
                            "file": str(relative_file_path.as_posix()),
                            "id": self._generate_unique_id(relative_file_path),
                        }
                    )
        logger.info(f"Found {len(contents)} content sections in {self.capsule_path}")
        return contents, folder_structure

    def create_folder_bundle(self, cypher: CapsuleCypher) -> None:
        """
        Create a folder bundle for the capsule.
        """
        logger.info(f"Creating folder bundle for capsule {self.capsule.capsule_id}")
        bundle_path = self.output_dir / cypher.capsule_id
        try:
            os.makedirs(bundle_path, exist_ok=True)
            cypher_path = bundle_path / "capsule-cypher.yaml"
            with open(cypher_path, "w") as f:
                f.write(cypher.to_yaml())

            for content_type, files in cypher.contents.items():
                if isinstance(files, list):
                    for file_info in files:
                        source_path = self.capsule_path / file_info["file"]
                        destination_path = bundle_path / file_info["file"]
                        os.makedirs(destination_path.parent, exist_ok=True)
                        shutil.copy2(source_path, destination_path)
                elif isinstance(files, dict):
                    for sub_type, sub_files in files.items():
                        for file_info in sub_files:
                            source_path = self.capsule_path / file_info["file"]
                            destination_path = bundle_path / file_info["file"]
                            os.makedirs(destination_path.parent, exist_ok=True)
                            shutil.copy2(source_path, destination_path)
            logger.info(f"Folder bundle created at {bundle_path}")
        except PermissionError:
            logger.error(f"Permission denied to write to {self.output_dir}")
            raise PermissionError(f"Permission denied to write to {self.output_dir}")

    def package(self) -> None:
        """
        Package the capsule.
        """
        logger.info(f"Packaging capsule {self.capsule.capsule_id}")
        cypher = self.generate_cypher()
        self.create_folder_bundle(cypher)
        logger.info(f"Capsule {self.capsule.capsule_id} packaged successfully")

    def export_to_folder(self) -> None:
        """
        Export the capsule to a folder.
        """
        logger.info(f"Exporting capsule {self.capsule.capsule_id} to {self.output_dir}")
        self.validate()
        destination = Path(self.output_dir)
        destination.mkdir(parents=True, exist_ok=True)
        for item in self.capsule_path.iterdir():
            if item.is_dir():
                shutil.copytree(item, destination / item.name)
            else:
                shutil.copy2(item, destination / item.name)
        logger.info(f"Capsule {self.capsule.capsule_id} exported successfully to {self.output_dir}")

    def export_to_zip(self) -> None:
        """
        Export the capsule to a zip archive.
        """
        logger.info(f"Exporting capsule {self.capsule.capsule_id} to {self.output_dir}")
        self.validate()
        destination_zip = Path(self.output_dir)
        shutil.make_archive(str(destination_zip), "zip", self.capsule_path)
        logger.info(f"Capsule {self.capsule.capsule_id} exported successfully to {self.output_dir}.zip")

    def validate(self) -> None:
        """
        Validate the capsule.
        """
        logger.info(f"Validating capsule {self.capsule.capsule_id}")
        validator = Validator(self.capsule_path)
        validator.validate_capsule()
        logger.info(f"Capsule {self.capsule.capsule_id} validated successfully")
