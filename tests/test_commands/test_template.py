from pathlib import Path

from typer.testing import CliRunner

from capsule.cli import app

runner = CliRunner()


def test_template_create_success():
    with runner.isolated_filesystem():
        template_dir = Path("capsule/templates")
        template_dir.mkdir(parents=True)
        result = runner.invoke(app, ["template", "create", "my-template", "--fields", "title, author"])
        assert result.exit_code == 0
        assert "Template 'my-template' created successfully" in result.stdout
        template_file = template_dir / "my-template.md.j2"
        assert template_file.exists()
        content = template_file.read_text()
        assert "title: {{ title }}" in content
        assert "author: {{ author }}" in content


def test_template_create_already_exists():
    with runner.isolated_filesystem():
        template_dir = Path("capsule/templates")
        template_dir.mkdir(parents=True)
        template_file = template_dir / "my-template.md.j2"
        template_file.touch()
        result = runner.invoke(app, ["template", "create", "my-template"])
        assert result.exit_code == 1
        assert "Error: Template 'my-template' already exists" in result.stdout


def test_template_create_force():
    with runner.isolated_filesystem():
        template_dir = Path("capsule/templates")
        template_dir.mkdir(parents=True)
        template_file = template_dir / "my-template.md.j2"
        template_file.touch()
        result = runner.invoke(app, ["template", "create", "my-template", "--force"])
        assert result.exit_code == 0
        assert "Template 'my-template' created successfully" in result.stdout


def test_template_list_success():
    with runner.isolated_filesystem():
        template_dir = Path("capsule/templates")
        template_dir.mkdir(parents=True)
        (template_dir / "test1.md.j2").write_text("---\ndomain: education\n---\nContent")
        (template_dir / "test2.md.j2").write_text("Content")

        result = runner.invoke(app, ["template", "list"])
        assert result.exit_code == 0
        assert "test1" in result.stdout
        assert "education" in result.stdout
        assert "test2" in result.stdout
        assert "Universal" in result.stdout


def test_template_list_empty():
    with runner.isolated_filesystem():
        template_dir = Path("capsule/templates")
        template_dir.mkdir(parents=True)

        result = runner.invoke(app, ["template", "list"])
        assert result.exit_code == 0
        assert "No templates found" in result.stdout


def test_template_validate_success():
    with runner.isolated_filesystem():
        schema_file = Path("valid_schema.yaml")
        schema_content = """
domain_type: test_domain
version: 1.0.0
required_fields:
  - id
  - name
optional_fields:
  - tags
domain_sections:
  test_data:
    required:
      - field1
"""
        schema_file.write_text(schema_content, encoding="utf-8")

        result = runner.invoke(app, ["template", "validate", str(schema_file)])
        assert result.exit_code == 0
        assert "Template schema 'valid_schema.yaml' is valid" in result.stdout
        assert "Domain: test_domain" in result.stdout
        assert "Version: 1.0.0" in result.stdout


def test_template_validate_missing_fields():
    with runner.isolated_filesystem():
        schema_file = Path("invalid_schema.yaml")
        schema_content = """
domain_type: test_domain
# version is missing
"""
        schema_file.write_text(schema_content, encoding="utf-8")

        result = runner.invoke(app, ["template", "validate", str(schema_file)])
        assert result.exit_code == 1
        assert "Error: Missing required fields: version" in result.stdout


def test_template_validate_invalid_yaml():
    with runner.isolated_filesystem():
        schema_file = Path("invalid.yaml")
        schema_file.write_text("not a dict", encoding="utf-8")

        result = runner.invoke(app, ["template", "validate", str(schema_file)])
        assert result.exit_code == 1
        assert "Error: Invalid YAML structure" in result.stdout


def test_template_validate_file_not_found():
    with runner.isolated_filesystem():
        result = runner.invoke(app, ["template", "validate", "nonexistent.yaml"])
        assert result.exit_code != 0
