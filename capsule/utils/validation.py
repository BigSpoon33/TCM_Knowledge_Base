import difflib
import os
from datetime import datetime
from pathlib import Path

import chardet
import jsonschema
from jinja2 import Environment, FileSystemLoader


def get_all_patterns(directory: Path) -> list[str]:
    """Returns a list of all markdown files in a directory."""
    patterns = []
    for p in directory.rglob("*.md"):
        patterns.append(p.stem)
    return patterns


def validate_pattern_exists(pattern_name: str, patterns_dir: Path) -> tuple[bool, str | None, list[str]]:
    """
    Validates if a pattern exists, offering suggestions for typos.
    Returns (exists, matched_pattern, suggestions).
    """
    all_patterns = get_all_patterns(patterns_dir)
    if not all_patterns:
        return False, None, []

    # Case-insensitive check
    pattern_lower = pattern_name.lower()
    all_patterns_lower = [p.lower() for p in all_patterns]

    if pattern_lower in all_patterns_lower:
        # Find the original cased version
        idx = all_patterns_lower.index(pattern_lower)
        return True, all_patterns[idx], []

    # Suggest similar patterns
    suggestions = difflib.get_close_matches(pattern_lower, all_patterns_lower, n=5, cutoff=0.6)
    # Get original cased versions of suggestions
    suggestions_cased = [all_patterns[all_patterns_lower.index(s)] for s in suggestions]
    return False, None, suggestions_cased


def validate_api_key(api_key: str | None) -> tuple[bool, str]:
    """Validates the Gemini API key."""
    if not api_key:
        return False, "GEMINI_API_KEY not set in config or environment."
    return True, ""


def find_script_path(script_name: str, scripts_dir: Path) -> Path | None:
    """Finds the path to a script in the scripts directory."""
    script_path = scripts_dir / f"{script_name}.py"
    return script_path if script_path.exists() else None


class Validator:
    def validate(self, content: str) -> bool:
        return True


# New code for validation report generation
EXPECTED_FILES = [
    "capsule/commands/__init__.py",
    "capsule/commands/config.py",
    "capsule/commands/conversation.py",
    "capsule/commands/generate.py",
    "capsule/commands/init.py",
    "capsule/commands/list.py",
    "capsule/commands/research.py",
    "capsule/commands/validate.py",
    "capsule/core/__init__.py",
    "capsule/core/generator.py",
    "capsule/core/packager.py",
    "capsule/core/researcher.py",
    "capsule/core/validator.py",
    "capsule/models/__init__.py",
    "capsule/models/capsule.py",
    "capsule/models/citation.py",
    "capsule/models/config.py",
    "capsule/models/cypher.py",
    "capsule/models/note.py",
    "capsule/models/research.py",
    "capsule/models/template.py",
    "capsule/templates/__init__.py",
    "capsule/templates/flashcard.md.j2",
    "capsule/templates/flashcards.md.j2",
    "capsule/templates/quiz.md.j2",
    "capsule/templates/test_template.md.j2",
    "capsule/templates/universal-note.md.j2",
    "capsule/templates/validation_report.md.j2",
    "capsule/utils/__init__.py",
    "capsule/utils/config.py",
    "capsule/utils/exceptions.py",
    "capsule/utils/file_ops.py",
    "capsule/utils/output.py",
    "capsule/utils/templates.py",
    "capsule/utils/validation.py",
    "capsule/utils/validators.py",
    "capsule/utils/yaml_handler.py",
    "capsule/__init__.py",
    "capsule/__main__.py",
    "capsule/cli.py",
    "capsule/exceptions.py",
]


def check_file_inventory():
    """Checks for missing and unexpected files."""
    errors = []
    # Check for missing files
    for file_path in EXPECTED_FILES:
        if not os.path.exists(file_path):
            errors.append({"file_path": file_path, "details": "File is missing."})

    # Check for unexpected files
    for root, _, files in os.walk("capsule"):
        for name in files:
            file_path = os.path.join(root, name)
            if file_path not in EXPECTED_FILES and not file_path.endswith(".pyc"):
                errors.append({"file_path": file_path, "details": "Unexpected file."})
    return {"errors": errors}


def check_schema_validation():
    """Validates YAML/JSON files against their schemas."""
    errors = []
    # In a real application, you'd load the config and schema more dynamically
    try:
        with open("capsule-cypher.yaml") as f:
            config = yaml.safe_load(f)

        # This is a placeholder schema. In a real app, you'd have a proper schema file.
        capsule_schema = {
            "type": "object",
            "properties": {
                "project_name": {"type": "string"},
                "vault_path": {"type": "string"},
                "templates_path": {"type": "string"},
            },
            "required": ["project_name", "vault_path"],
        }
        jsonschema.validate(instance=config, schema=capsule_schema)
    except FileNotFoundError:
        errors.append({"file_path": "capsule-cypher.yaml", "details": "File not found."})
    except jsonschema.exceptions.ValidationError as e:
        errors.append({"file_path": "capsule-cypher.yaml", "details": str(e)})
    except Exception as e:
        errors.append({"file_path": "capsule-cypher.yaml", "details": f"An unexpected error occurred: {e}"})

    return {"errors": errors}


def check_encoding(directory_to_scan="."):
    """Checks the encoding of all .md, .yaml, and .json files."""
    errors = []
    for root, _, files in os.walk(directory_to_scan):
        for name in files:
            if name.endswith((".md", ".yaml", ".json")):
                file_path = os.path.join(root, name)
                try:
                    with open(file_path, "rb") as f:
                        result = chardet.detect(f.read())
                        if result["encoding"] not in ["utf-8", "ascii"]:
                            errors.append(
                                {"file_path": file_path, "details": f"Incorrect encoding: {result['encoding']}"}
                            )
                except Exception as e:
                    errors.append({"file_path": file_path, "details": str(e)})
    return {"errors": errors}


def run_validation():
    """Runs all validation checks and returns the results."""
    results = {
        "inventory_check": check_file_inventory(),
        "schema_validation": check_schema_validation(),
        "encoding_check": check_encoding(),
    }
    return results


def generate_report(results):
    """Generates a markdown validation report."""
    # Correctly locate the templates directory relative to this script
    # Assuming this script is in capsule/utils and templates are in capsule/templates
    template_dir = Path(__file__).parent.parent / "templates"
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("validation_report.md.j2")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_errors = sum(len(result.get("errors", [])) for result in results.values())
    summary = {
        "status": "FAILED" if total_errors > 0 else "PASSED",
        "total_checks": len(results),
        "total_errors": total_errors,
    }

    report_content = template.render(
        timestamp=timestamp,
        summary=summary,
        inventory_check=results["inventory_check"],
        schema_validation=results["schema_validation"],
        encoding_check=results["encoding_check"],
    )

    report_filename = f"validation-report-{datetime.now().strftime('%Y%m%d%H%M%S')}.md"
    # Ensure the target directory exists
    sprint_artifacts_dir = Path("docs/sprint-artifacts")
    sprint_artifacts_dir.mkdir(exist_ok=True)
    report_path = sprint_artifacts_dir / report_filename

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)

    return str(report_path)
