import semver
import yaml

def is_valid_semver(version):
    """
    Checks if a version string is a valid semantic version.
    """
    try:
        semver.VersionInfo.parse(version)
        return True
    except ValueError:
        return False

def is_valid_yaml(file_path):
    """
    Checks if a file is a valid YAML file.
    """
    try:
        with open(file_path, 'r') as f:
            yaml.safe_load(f)
        return True
    except (yaml.YAMLError, FileNotFoundError):
        return False

def is_utf8_encoded(file_path):
    """
    Checks if a file is UTF-8 encoded.
    """
    try:
        with open(file_path, 'rb') as f:
            f.read().decode('utf-8')
        return True
    except (UnicodeDecodeError, FileNotFoundError):
        return False

def check_required_fields(data, required_fields):
    """
    Checks if a dictionary contains all required fields.
    """
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    return missing_fields
