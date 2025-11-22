import semver


def compare_versions(v1: str, v2: str) -> int:
    """
    Compare two semantic version strings.

    Args:
        v1: First version string
        v2: Second version string

    Returns:
        -1 if v1 < v2
         0 if v1 == v2
         1 if v1 > v2

    Raises:
        ValueError: If either version string is invalid
    """
    try:
        ver1 = semver.VersionInfo.parse(v1)
        ver2 = semver.VersionInfo.parse(v2)
        return ver1.compare(ver2)
    except ValueError as e:
        raise ValueError(f"Invalid semantic version: {e}")


def is_valid_semver(version: str) -> bool:
    """
    Checks if a version string is a valid semantic version.
    Wrapper around semver.VersionInfo.parse for convenience.
    """
    try:
        semver.VersionInfo.parse(version)
        return True
    except ValueError:
        return False
