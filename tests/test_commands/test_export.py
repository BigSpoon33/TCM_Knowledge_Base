from unittest.mock import patch

import pytest
import yaml
from typer.testing import CliRunner

from capsule.cli import app

runner = CliRunner()


@pytest.fixture
def mock_packager():
    with patch("capsule.core.exporter.Packager") as MockPackager:
        yield MockPackager


@pytest.fixture
def valid_capsule(tmp_path):
    capsule_path = tmp_path / "test_capsule"
    capsule_path.mkdir()
    cypher_content = {
        "capsule_id": "test_capsule",
        "name": "Test Capsule",
        "version": "1.0.0",
        "domain_type": "test",
        "folder_structure": {},
        "contents": {},
    }
    with open(capsule_path / "capsule-cypher.yaml", "w") as f:
        yaml.dump(cypher_content, f)
    return capsule_path


def test_export_zip_default(mock_packager, valid_capsule):
    result = runner.invoke(app, ["export", str(valid_capsule)])

    assert result.exit_code == 0
    mock_packager.return_value.package_to_zip.assert_called_once()


def test_export_folder(mock_packager, valid_capsule):
    result = runner.invoke(app, ["export", str(valid_capsule), "--no-zip"])

    assert result.exit_code == 0
    mock_packager.return_value.package_to_folder.assert_called_once()


def test_export_custom_output(mock_packager, valid_capsule, tmp_path):
    output_dir = tmp_path / "output"
    result = runner.invoke(app, ["export", str(valid_capsule), "--output", str(output_dir)])

    assert result.exit_code == 0
    # Check that package_to_zip was called with a path inside output_dir
    args, _ = mock_packager.return_value.package_to_zip.call_args
    output_path_arg = args[0]
    assert output_dir in output_path_arg.parents


def test_export_path_not_found(tmp_path):
    non_existent_path = tmp_path / "non_existent"
    result = runner.invoke(app, ["export", str(non_existent_path)])

    assert result.exit_code != 0
    assert "Capsule path does not exist" in result.stdout


def test_export_yaml_error(mock_packager, tmp_path):
    capsule_path = tmp_path / "bad_yaml_capsule"
    capsule_path.mkdir()
    with open(capsule_path / "capsule-cypher.yaml", "w") as f:
        f.write("invalid: yaml: content: [")  # Invalid YAML

    result = runner.invoke(app, ["export", str(capsule_path)])

    assert result.exit_code != 0
    assert "YAML Error" in result.stdout
