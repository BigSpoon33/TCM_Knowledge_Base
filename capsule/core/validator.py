import yaml
from capsule.utils.validators import check_required_fields, is_valid_semver


class Validator:
    """
    The Validator class is responsible for ensuring the integrity of capsules and their contents.
    """

    def __init__(self, capsule_path):
        self.capsule_path = capsule_path
        self.cypher_path = self.capsule_path / "capsule-cypher.yaml"
        if not self.cypher_path.exists():
            raise FileNotFoundError(f"capsule-cypher.yaml not found in {self.capsule_path}")

        with open(self.cypher_path, "r") as f:
            self.cypher = yaml.safe_load(f)

    def validate_capsule(self):
        """
        Orchestrates the validation of a capsule.
        """
        self.validate_capsule_structure()
        self.validate_frontmatter_schema()
        self.validate_file_inventory()
        self.validate_data_types()

    def validate_capsule_structure(self):
        """
        Validates the structure of a capsule.
        """
        required_fields = ["capsule_id", "name", "version", "domain_type", "folder_structure", "contents"]
        missing_fields = check_required_fields(self.cypher, required_fields)
        if missing_fields:
            raise ValueError(f"Missing required fields in capsule-cypher.yaml: {', '.join(missing_fields)}")

        if not is_valid_semver(self.cypher["version"]):
            raise ValueError(f"Invalid semantic version in capsule-cypher.yaml: {self.cypher['version']}")

    def validate_frontmatter_schema(self):
        """
        Validates the frontmatter schema of a capsule.
        """
        if "schema" not in self.cypher:
            return

        schema = self.cypher["schema"]
        for content_type, files in self.cypher["contents"].items():
            if content_type not in schema:
                continue

            content_schema = schema[content_type]
            if isinstance(files, list):
                for file_info in files:
                    self._validate_file_frontmatter(file_info, content_schema)
            elif isinstance(files, dict):
                for sub_type, sub_files in files.items():
                    if sub_type not in content_schema:
                        continue
                    sub_type_schema = content_schema[sub_type]
                    for file_info in sub_files:
                        self._validate_file_frontmatter(file_info, sub_type_schema)

    def _validate_file_frontmatter(self, file_info, schema):
        file_path = self.capsule_path / file_info["file"]
        if not file_path.exists():
            return

        with open(file_path, "r") as f:
            content = f.read()
            # This is a simplified frontmatter parsing logic.
            # A more robust implementation would use a dedicated library.
            frontmatter_str = content.split("---")[1]
            frontmatter = yaml.safe_load(frontmatter_str)

        for field, properties in schema.items():
            if properties.get("required") and field not in frontmatter:
                raise ValueError(f"Missing required field '{field}' in {file_path}")

    def validate_file_inventory(self):
        """
        Validates the file inventory of a capsule.
        """
        cypher_files = set()
        for content_type, files in self.cypher["contents"].items():
            if isinstance(files, list):
                for file_info in files:
                    cypher_files.add(self.capsule_path / file_info["file"])
            elif isinstance(files, dict):
                for sub_type, sub_files in files.items():
                    for file_info in sub_files:
                        cypher_files.add(self.capsule_path / file_info["file"])

        for file_path in cypher_files:
            if not file_path.exists():
                raise FileNotFoundError(f"File from cypher not found in capsule: {file_path}")

        actual_files = {f for f in self.capsule_path.glob("**/*") if f.is_file()}
        extra_files = actual_files - cypher_files - {self.cypher_path}
        if extra_files:
            raise FileExistsError(f"Extra files found in capsule: {', '.join(str(f) for f in extra_files)}")

    def validate_data_types(self):
        """
        Validates the data types of a capsule.
        """
        if "schema" not in self.cypher:
            return

        schema = self.cypher["schema"]
        for content_type, files in self.cypher["contents"].items():
            if content_type not in schema:
                continue

            content_schema = schema[content_type]
            if isinstance(files, list):
                for file_info in files:
                    self._validate_file_data_types(file_info, content_schema)
            elif isinstance(files, dict):
                for sub_type, sub_files in files.items():
                    if sub_type not in content_schema:
                        continue
                    sub_type_schema = content_schema[sub_type]
                    for file_info in sub_files:
                        self._validate_file_data_types(file_info, sub_type_schema)

    def _validate_file_data_types(self, file_info, schema):
        file_path = self.capsule_path / file_info["file"]
        if not file_path.exists():
            return

        with open(file_path, "r") as f:
            content = f.read()
            # This is a simplified frontmatter parsing logic.
            # A more robust implementation would use a dedicated library.
            frontmatter_str = content.split("---")[1]
            frontmatter = yaml.safe_load(frontmatter_str)

        for field, field_type in schema.items():
            if field in frontmatter:
                if not isinstance(frontmatter[field], eval(field_type)):
                    raise TypeError(
                        f"Invalid data type for field '{field}' in {file_path}. Expected {field_type}, got {type(frontmatter[field]).__name__}"
                    )
