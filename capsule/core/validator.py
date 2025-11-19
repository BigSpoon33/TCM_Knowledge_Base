import yaml
from capsule.utils.validators import check_required_fields, is_valid_semver

class Validator:
    """
    The Validator class is responsible for ensuring the integrity of capsules and their contents.
    """

    def validate_capsule(self, capsule):
        """
        Orchestrates the validation of a capsule.
        """
        cypher_path = capsule.path / 'capsule-cypher.yaml'
        if not cypher_path.exists():
            raise FileNotFoundError(f"capsule-cypher.yaml not found in {capsule.path}")

        with open(cypher_path, 'r') as f:
            cypher = yaml.safe_load(f)

        self.validate_capsule_structure(cypher)
        self.validate_frontmatter_schema(capsule, cypher)
        self.validate_file_inventory(capsule, cypher)
        self.validate_data_types(capsule, cypher)

    def validate_capsule_structure(self, cypher):
        """
        Validates the structure of a capsule.
        """
        required_fields = ['capsule_id', 'name', 'version', 'domain_type', 'folder_structure', 'contents']
        missing_fields = check_required_fields(cypher, required_fields)
        if missing_fields:
            raise ValueError(f"Missing required fields in capsule-cypher.yaml: {', '.join(missing_fields)}")

        if not is_valid_semver(cypher['version']):
            raise ValueError(f"Invalid semantic version in capsule-cypher.yaml: {cypher['version']}")

    def validate_frontmatter_schema(self, capsule, cypher):
        """
        Validates the frontmatter schema of a capsule.
        """
        for content_type, files in cypher['contents'].items():
            if isinstance(files, list):
                for file_info in files:
                    file_path = capsule.path / file_info['file']
                    if not file_path.exists():
                        raise FileNotFoundError(f"File not found: {file_path}")
            elif isinstance(files, dict):
                for sub_type, sub_files in files.items():
                    for file_info in sub_files:
                        file_path = capsule.path / file_info['file']
                        if not file_path.exists():
                            raise FileNotFoundError(f"File not found: {file_path}")

    def validate_file_inventory(self, capsule, cypher):
        """
        Validates the file inventory of a capsule.
        """
        cypher_files = set()
        for content_type, files in cypher['contents'].items():
            if isinstance(files, list):
                for file_info in files:
                    cypher_files.add(capsule.path / file_info['file'])
            elif isinstance(files, dict):
                for sub_type, sub_files in files.items():
                    for file_info in sub_files:
                        cypher_files.add(capsule.path / file_info['file'])

        for file_path in cypher_files:
            if not file_path.exists():
                raise FileNotFoundError(f"File from cypher not found in capsule: {file_path}")

    def validate_data_types(self, capsule, cypher):
        """
        Validates the data types of a capsule.
        """
        # This is a placeholder implementation.
        # The actual implementation will be added in a future story.
        pass
