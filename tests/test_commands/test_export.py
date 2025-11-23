from unittest.mock import patch
import pytest
import yaml
from pathlib import Path
from typer.testing import CliRunner
from capsule.cli import app
from capsule.core.packager import Packager

runner = CliRunner()


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
        "contents": {"root": [{"file": "test.md"}]},
        "data_schemas": {},
    }
    with open(capsule_path / "capsule-cypher.yaml", "w") as f:
        yaml.dump(cypher_content, f)

    # Add a dummy file
    (capsule_path / "test.md").write_text("Test content")

    return capsule_path


def test_export_zip_default(valid_capsule, tmp_path):
    # We need to run in a temp dir so output defaults to it
    with runner.isolated_filesystem(temp_dir=tmp_path):
        # The command defaults output to current dir if not specified
        # But valid_capsule is in tmp_path (which is now current dir)

        result = runner.invoke(app, ["export", str(valid_capsule)])

        if result.exit_code != 0:
            print(f"Output: {result.output}")
            print(f"Exception: {result.exception}")

        assert result.exit_code == 0
        assert "Exporting capsule to zip" in result.stdout

        # Check if zip file exists
        # Default name is {capsule_id}_v{version}.zip
        expected_zip = Path("test_capsule_v1.0.0.zip")
        assert expected_zip.exists()


def test_export_folder(valid_capsule, tmp_path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["export", str(valid_capsule), "--no-zip"])

        assert result.exit_code == 0
        assert "Exporting capsule to folder" in result.stdout

        # Check if folder exists
        expected_folder = Path("test_capsule_v1.0.0")
        assert expected_folder.exists()
        assert expected_folder.is_dir()
        assert (expected_folder / "test.md").exists()
        assert (expected_folder / "export-manifest.json").exists()


def test_export_custom_output(valid_capsule, tmp_path):
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    result = runner.invoke(app, ["export", str(valid_capsule), "--output", str(output_dir)])

    assert result.exit_code == 0

    # Check if zip file exists in output dir
    expected_zip = output_dir / "test_capsule_v1.0.0.zip"
    assert expected_zip.exists()


def test_export_path_not_found(tmp_path):
    non_existent_path = tmp_path / "non_existent"
    result = runner.invoke(app, ["export", str(non_existent_path)])

    assert result.exit_code != 0
    assert "Capsule path does not exist" in result.stdout


def test_export_yaml_error(tmp_path):
    capsule_path = tmp_path / "bad_yaml_capsule"
    capsule_path.mkdir()
    with open(capsule_path / "capsule-cypher.yaml", "w") as f:
        f.write("invalid: yaml: content: [")  # Invalid YAML

    result = runner.invoke(app, ["export", str(capsule_path)])

    assert result.exit_code != 0
    assert "YAML Error" in result.stdout
