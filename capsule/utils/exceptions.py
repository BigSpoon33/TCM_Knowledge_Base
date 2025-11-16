# capsule/utils/exceptions.py

class CapsuleError(Exception):
    """Base exception for all Capsule-related errors."""
    pass

class YAMLFileError(CapsuleError):
    """Custom exception for errors during YAML file processing."""
    pass
