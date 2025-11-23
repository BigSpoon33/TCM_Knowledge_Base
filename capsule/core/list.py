import logging
from pathlib import Path
from typing import List

from capsule.models.cypher import CapsuleCypher
from capsule.utils.file_ops import read_file

logger = logging.getLogger(__name__)


class List:
    """
    Service for listing installed capsules in the vault.

    This service scans the vault for capsule-cypher.yaml files and returns
    a simple list of installed capsules with their basic metadata.
    """

    def __init__(self, vault_path: Path):
        """
        Initialize the List service.

        Args:
            vault_path: Path to the Obsidian vault directory.
        """
        self.vault_path = vault_path

    def get_installed_capsules(self) -> list[CapsuleCypher]:
        """
        Scans the vault for installed capsules by looking for capsule-cypher.yaml files.

        Returns:
            List of CapsuleCypher objects representing installed capsules.

        Example:
            >>> list_service = List(Path("/path/to/vault"))
            >>> capsules = list_service.get_installed_capsules()
            >>> for capsule in capsules:
            ...     print(f"{capsule.capsule_id}: v{capsule.version}")
        """
        capsules = []
        if not self.vault_path.exists():
            logger.warning(f"Vault path does not exist: {self.vault_path}")
            return capsules

        # Look for capsule-cypher.yaml files recursively
        # We catch errors to prevent one bad file from breaking the whole list
        for cypher_path in self.vault_path.rglob("capsule-cypher.yaml"):
            try:
                content = read_file(cypher_path)
                cypher = CapsuleCypher.from_yaml(content)
                capsules.append(cypher)
                logger.debug(f"Found capsule: {cypher.capsule_id} v{cypher.version}")
            except Exception as e:
                logger.warning(f"Failed to parse cypher at {cypher_path}: {e}")
                continue

        logger.info(f"Found {len(capsules)} installed capsule(s)")
        return capsules
