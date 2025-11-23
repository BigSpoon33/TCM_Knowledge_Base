from typer.testing import CliRunner
from capsule.cli import app

runner = CliRunner()


def test_global_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Examples:" in result.stdout
    assert "capsule generate" in result.stdout


def test_generate_help():
    result = runner.invoke(app, ["generate", "--help"])
    assert result.exit_code == 0
    assert "Examples:" in result.stdout
    assert "capsule generate" in result.stdout
    assert "Generation Options" in result.stdout
    assert "Output Options" in result.stdout


def test_import_help():
    result = runner.invoke(app, ["import", "--help"])
    assert result.exit_code == 0
    assert "Examples:" in result.stdout
    assert "capsule import" in result.stdout
    assert "Import Options" in result.stdout


def test_export_help():
    result = runner.invoke(app, ["export", "--help"])
    assert result.exit_code == 0
    assert "Examples:" in result.stdout
    assert "capsule export" in result.stdout
    assert "Export Options" in result.stdout


def test_template_help():
    result = runner.invoke(app, ["template", "--help"])
    assert result.exit_code == 0
    # Template group help might not have examples, but subcommands do


def test_template_create_help():
    result = runner.invoke(app, ["template", "create", "--help"])
    assert result.exit_code == 0
    assert "Examples:" in result.stdout
    assert "capsule template create" in result.stdout
    assert "Template Options" in result.stdout


def test_template_list_help():
    result = runner.invoke(app, ["template", "list", "--help"])
    assert result.exit_code == 0
    assert "Examples:" in result.stdout
    assert "capsule template list" in result.stdout


def test_template_validate_help():
    result = runner.invoke(app, ["template", "validate", "--help"])
    assert result.exit_code == 0
    assert "Examples:" in result.stdout
    assert "capsule template validate" in result.stdout


def test_validate_help():
    result = runner.invoke(app, ["validate", "--help"])
    assert result.exit_code == 0
    assert "Examples:" in result.stdout
    assert "capsule validate" in result.stdout
    assert "Validation Options" in result.stdout


def test_status_help():
    result = runner.invoke(app, ["status", "--help"])
    assert result.exit_code == 0
    assert "Examples:" in result.stdout
    assert "capsule status" in result.stdout


def test_list_help():
    result = runner.invoke(app, ["list", "--help"])
    assert result.exit_code == 0
    assert "Examples:" in result.stdout
    assert "capsule list" in result.stdout


def test_init_help():
    result = runner.invoke(app, ["init", "--help"])
    assert result.exit_code == 0
    assert "Examples:" in result.stdout
    assert "capsule init" in result.stdout
