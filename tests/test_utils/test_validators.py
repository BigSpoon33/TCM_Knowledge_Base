from capsule.utils.validators import (
    check_required_fields,
    is_utf8_encoded,
    is_valid_semver,
    is_valid_yaml,
)


def test_is_valid_semver():
    assert is_valid_semver("1.2.3")
    assert not is_valid_semver("1.2")
    assert not is_valid_semver("invalid")


def test_is_valid_yaml(tmp_path):
    valid_yaml = tmp_path / "valid.yaml"
    valid_yaml.write_text("key: value")
    assert is_valid_yaml(valid_yaml)

    invalid_yaml = tmp_path / "invalid.yaml"
    invalid_yaml.write_text("key: value:")
    assert not is_valid_yaml(invalid_yaml)


def test_is_utf8_encoded(tmp_path):
    utf8_file = tmp_path / "utf8.txt"
    utf8_file.write_text("hello", encoding="utf-8")
    assert is_utf8_encoded(utf8_file)

    latin1_file = tmp_path / "latin1.txt"
    latin1_file.write_text("héllo", encoding="latin-1")
    assert not is_utf8_encoded(latin1_file)


def test_check_required_fields():
    data = {"a": 1, "b": 2}
    required_fields = ["a"]
    assert check_required_fields(data, required_fields) == []

    required_fields = ["a", "c"]
    assert check_required_fields(data, required_fields) == ["c"]
