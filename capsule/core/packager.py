import os
from pathlib import Path
from capsule.models.cypher import CapsuleCypher
import frontmatter


class CapsulePackager:
    """Core logic for packaging capsules."""

    def __init__(self, capsule_path: str, output_dir: str) -> None:
        """
        Initialize the CapsulePackager.

        Args:
            capsule_path: The path to the capsule to be packaged.
            output_dir: The directory to output the packaged capsule to.
        """
        self.capsule_path = Path(capsule_path)
        self.output_dir = Path(output_dir)

    def generate_cypher(self) -> CapsuleCypher:
        """
        Generate the capsule-cypher.yaml file.

        Returns:
            The CapsuleCypher object.
        """
        contents = self._scan_contents()
        cypher = CapsuleCypher(
            capsule_id="TCM_Test_v1",
            name="Test Capsule",
            version="1.0.0",
            domain_type="tcm",
            folder_structure={"root_notes": "root_notes/"},
            contents=contents,
            data_schemas={},
            sequence_mode="freeform",
        )
        return cypher

    def _scan_contents(self) -> dict:
        """Scan the capsule directory for markdown files."""
        contents = {"root_notes": []}
        root_notes_path = self.capsule_path / "root_notes"
        if root_notes_path.is_dir():
            for file_path in sorted(root_notes_path.glob("*.md")):
                with open(file_path, "r") as f:
                    post = frontmatter.load(f)
                    contents["root_notes"].append(
                        {
                            "file": str(file_path.relative_to(self.capsule_path)),
                            "id": post.get("id", ""),
                        }
                    )
        return contents

    def create_folder_bundle(self) -> None:
        """
        Create a folder bundle for the capsule.
        """
        cypher = self.generate_cypher()
        bundle_path = self.output_dir / cypher.capsule_id
        os.makedirs(bundle_path, exist_ok=True)
        cypher_path = bundle_path / "capsule-cypher.yaml"
        with open(cypher_path, "w") as f:
            f.write(cypher.to_yaml())

    def package(self) -> None:
        """
        Package the capsule.
        """
        self.create_folder_bundle()
