# capsule/utils/exceptions.py


class CapsuleError(Exception):
    """Base exception for all Capsule-related errors."""

    pass


class YAMLFileError(CapsuleError):
    """Custom exception for errors during YAML file processing."""

    pass


class NetworkError(CapsuleError):
    """Custom exception for network-related errors."""

    pass


class ConfigError(CapsuleError):
    """Custom exception for configuration errors."""

    pass


class FileError(CapsuleError):
    """Custom exception for file operation errors."""

    pass
