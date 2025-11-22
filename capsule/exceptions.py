"""Custom exceptions for capsule operations"""


class CapsuleError(Exception):
    """Base exception for all capsule errors"""

    exit_code = 1


class ValidationError(CapsuleError):
    """Schema validation failed"""

    exit_code = 1


class FileError(CapsuleError):
    """File operation failed"""

    exit_code = 2


class NetworkError(CapsuleError):
    """Network/API error"""

    exit_code = 3


class UserCancelledError(CapsuleError):
    """User cancelled operation"""

    exit_code = 4


class ConfigError(CapsuleError):
    """Configuration error"""

    exit_code = 5


class MergeConflict(CapsuleError):
    """Merge conflict detected"""

    exit_code = 6

    def __init__(self, file: str, section: str, existing_source: list, incoming_source: str):
        self.file = file
        self.section = section
        self.existing_source = existing_source
        self.incoming_source = incoming_source
        super().__init__(f"Merge conflict in {file}: Section '{section}' already exists (Sources: {existing_source})")
