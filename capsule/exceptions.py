from typing import Optional, List


class CapsuleError(Exception):
    """Base class for all OCDS exceptions."""

    def __init__(self, message: str, exit_code: int = 1, hint: Optional[str] = None):
        self.exit_code = exit_code
        self.hint = hint
        super().__init__(message)


class ValidationError(CapsuleError):
    """Raised when schema or data validation fails."""

    def __init__(self, message: str, hint: Optional[str] = None):
        super().__init__(message, exit_code=1, hint=hint)


class FileError(CapsuleError):
    """Raised when file operations fail (permissions, not found)."""

    def __init__(self, message: str, hint: Optional[str] = None):
        super().__init__(message, exit_code=2, hint=hint)


class NetworkError(CapsuleError):
    """Raised when network requests fail (research, API)."""

    def __init__(self, message: str, hint: Optional[str] = None):
        super().__init__(message, exit_code=3, hint=hint)


class UserCancelledError(CapsuleError):
    """Raised when user aborts an operation."""

    def __init__(self, message: str = "Operation cancelled by user.", hint: Optional[str] = None):
        super().__init__(message, exit_code=4, hint=hint)


class ConfigError(CapsuleError):
    """Configuration error"""

    def __init__(self, message: str, hint: Optional[str] = None):
        super().__init__(message, exit_code=5, hint=hint)


class MergeConflict(CapsuleError):
    """Merge conflict detected"""

    def __init__(self, file: str, section: str, existing_source: List[str], incoming_source: str):
        self.file = file
        self.section = section
        self.existing_source = existing_source
        self.incoming_source = incoming_source
        message = f"Merge conflict in {file}: Section '{section}' already exists (Sources: {existing_source})"
        super().__init__(message, exit_code=6, hint="Use --force to overwrite or manually resolve the conflict.")
