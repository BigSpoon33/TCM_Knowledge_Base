import logging
import os
from pathlib import Path
from capsule.models.capsule import Capsule
from capsule.models.cypher import CapsuleCypher
import frontmatter

logger = logging.getLogger(__name__)


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
        self.capsule = capsule
        self.capsule_path = Path(capsule_path)
        self.output_dir = Path(output_dir)

        if not self.capsule_path.is_dir():
            logger.error(f"Capsule path {self.capsule_path} not found or not a directory.")
            raise FileNotFoundError(f"Capsule path {self.capsule_path} not found or not a directory.")
        if not os.access(self.output_dir, os.W_OK):
            logger.error(f"Output directory {self.output_dir} is not writable.")
            raise IOError(f"Output directory {self.output_dir} is not writable.")

        logger.info(f"CapsulePackager initialized for capsule {self.capsule.capsule_id}")

    def _scan_schemas(self) -> dict:
        """Scan the capsule directory for data schemas."""
        logger.info(f"Scanning for data schemas in {self.capsule_path}")
        schemas_path = self.capsule_path / "schemas"
        data_schemas = {}
        if schemas_path.is_dir():
            for file_path in schemas_path.iterdir():
                if file_path.suffix in (".yaml", ".yml", ".json"):
                    schema_name = file_path.stem
                    with open(file_path, "r") as f:
                        yaml = YAML()
                        data_schemas[schema_name] = yaml.load(f)
        logger.info(f"Found {len(data_schemas)} data schemas in {self.capsule_path}")
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
            sequence_mode="freeform",
        )
        logger.info(f"Cypher generated for capsule {self.capsule.capsule_id}")
        return cypher

    def _scan_contents(self) -> tuple[dict, dict]:
        """Scan the capsule directory for markdown files and folder structure."""
        logger.info(f"Scanning contents of {self.capsule_path}")
        contents = {}
        folder_structure = {}
        for root, dirs, files in os.walk(self.capsule_path):
            root_path = Path(root)
            relative_root = root_path.relative_to(self.capsule_path)
            if str(relative_root) == ".":
                folder_key = "root"
            else:
                folder_key = str(relative_root).replace(os.sep, "_")

            # Ensure a key exists for the directory even if it's empty
            if folder_key not in contents:
                contents[folder_key] = []

            if dirs:
                folder_structure[folder_key] = [str(Path(d).as_posix()) for d in dirs]

            if files:
                for file in sorted(files):
                    if file.endswith(".md"):
                        file_path = root_path / file
                        with open(file_path, "r") as f:
                            post = frontmatter.load(f)
                            contents[folder_key].append(
                                {
                                    "file": str(file_path.relative_to(self.capsule_path).as_posix()),
                                    "id": post.get("id", ""),
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
        os.makedirs(bundle_path, exist_ok=True)
        cypher_path = bundle_path / "capsule-cypher.yaml"
        with open(cypher_path, "w") as f:
            f.write(cypher.to_yaml())
        logger.info(f"Folder bundle created at {bundle_path}")

    def package(self) -> None:
        """
        Package the capsule.
        """
        logger.info(f"Packaging capsule {self.capsule.capsule_id}")
        cypher = self.generate_cypher()
        self.create_folder_bundle(cypher)
        logger.info(f"Capsule {self.capsule.capsule_id} packaged successfully")
