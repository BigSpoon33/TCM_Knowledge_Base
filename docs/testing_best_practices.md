# Testing Best Practices

This guide outlines best practices for writing effective and maintainable tests for this project.

## Pre-Development Review

Before writing tests, ensure you have completed the [Pre-Development Architectural Review Checklist](./pre_dev_checklist.md). This will help prevent common issues that can complicate testing.

## 1. Avoid Code Duplication

Tests should be DRY (Don't Repeat Yourself). Avoid duplicating logic or data across multiple tests.

**Bad Practice:** Duplicating template content or large data structures inside test files.

```python
# tests/test_bad_example.py

def test_template_rendering():
    template_content = """
    # {{ title }}
    {{ content }}
    """
    # ... test logic ...
```

**Good Practice:** Load artifacts directly from their source files. This ensures tests are validating the actual production code and are easier to maintain.

```python
# tests/test_good_example.py
from pathlib import Path

def test_template_rendering():
    template_path = Path(__file__).parent.parent / "capsule/templates/my_template.md"
    template_content = template_path.read_text()
    # ... test logic ...
```

## 2. Load Artifacts, Don't Recreate Them

Whenever a test needs to interact with a file or artifact (like a template, configuration file, or test data), load it from the file system. Recreating it within the test leads to brittle tests that can become out-of-sync with the real artifact.

## 3. Use Mocks for External Dependencies

When testing a unit of code that has external dependencies (like a database, API, or complex object), use mocks to isolate the unit under test. This makes tests faster, more reliable, and easier to write.

Use libraries like `unittest.mock` to patch dependencies and control their behavior during tests.
