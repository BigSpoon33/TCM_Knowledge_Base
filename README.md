# Obsidian Capsule Delivery System

[![Test Status](https://github.com/BigSpoon33/obsidian_capsule_cli/workflows/Test%20Python%20application/badge.svg)](https://github.com/BigSpoon33/obsidian_capsule_cli/actions)
[![Coverage](https://img.shields.io/badge/coverage-63%25-yellow.svg)](htmlcov/index.html)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

CLI tool for AI-powered educational content generation in Obsidian.

* Free software: MIT License

## Features

* AI-powered content generation
* Template-driven content creation
* Capsule-based content packaging and distribution
* And much more!

## Testing

This project maintains comprehensive test coverage with pytest.

### Running Tests

```bash
# Run all tests with coverage
pytest

# Run specific test types
pytest -m unit           # Unit tests only
pytest -m integration    # Integration tests only
pytest -m e2e            # End-to-end tests only

# View detailed HTML coverage report
pytest
open htmlcov/index.html  # macOS
```

### Coverage

- **Current Coverage**: 63.41% (with branch coverage)
- **Minimum Threshold**: 60%
- **Target Goal**: 80%

For detailed coverage information, see [Testing and Coverage Guide](docs/testing-coverage.md)

## Credits

This package was created with [Cookiecutter](https://github.com/audreyfeldroy/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
