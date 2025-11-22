import pytest
from capsule.utils.versioning import compare_versions


class TestVersioning:
    """Test version comparison logic"""

    def test_compare_versions_equal(self):
        """Test equal versions"""
        assert compare_versions("1.0.0", "1.0.0") == 0
        assert compare_versions("2.1.5", "2.1.5") == 0

    def test_compare_versions_greater(self):
        """Test v1 > v2"""
        assert compare_versions("1.0.1", "1.0.0") == 1
        assert compare_versions("2.0.0", "1.9.9") == 1
        assert compare_versions("1.1.0", "1.0.9") == 1

    def test_compare_versions_less(self):
        """Test v1 < v2"""
        assert compare_versions("1.0.0", "1.0.1") == -1
        assert compare_versions("1.9.9", "2.0.0") == -1
        assert compare_versions("1.0.9", "1.1.0") == -1

    def test_compare_versions_invalid(self):
        """Test invalid versions"""
        with pytest.raises(ValueError):
            compare_versions("invalid", "1.0.0")
        with pytest.raises(ValueError):
            compare_versions("1.0.0", "invalid")
