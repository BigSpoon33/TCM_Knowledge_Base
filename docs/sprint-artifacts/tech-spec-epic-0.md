# Epic Technical Specification: Foundation & Project Setup

Date: 2025-11-15  
Author: BMad  
Epic ID: epic-0  
Status: Draft

---

## Overview

Epic 0 establishes the foundational infrastructure for the Obsidian Capsule Delivery System by implementing a modern Python CLI project using industry-standard tools and best practices. This epic creates the project skeleton using Cookiecutter PyPackage, installs all core dependencies identified in the architecture (Typer, python-frontmatter, ruamel.yaml, Jinja2, pytest), configures the CI/CD pipeline for automated testing and releases, and sets up development tools (black, flake8, mypy) to ensure code quality and maintainability.

This foundational work directly supports the PRD's vision of building a production-ready CLI tool (PRD Section: CLI Tool Specifications) and aligns with NFR31-35 (Maintainability Requirements) which mandate PEP 8 compliance, comprehensive docstrings, and semantic versioning. Without this epic, no subsequent development can proceed as it provides the essential project structure, dependency management, and quality assurance infrastructure.

## Objectives and Scope

### In Scope

**Primary Objectives:**
- ✅ Initialize modern Python package structure using Cookiecutter PyPackage template
- ✅ Install and configure all core dependencies (Typer, python-frontmatter, ruamel.yaml, Jinja2, PyYAML, requests, google-generativeai)
- ✅ Install and configure all development dependencies (pytest, pytest-cov, black, flake8, mypy)
- ✅ Set up GitHub Actions CI/CD pipeline for automated testing on multiple Python versions (3.8, 3.9, 3.10, 3.11, 3.12)
- ✅ Configure development tools with appropriate settings (pyproject.toml, setup.cfg, .flake8)
- ✅ Create initial project documentation structure (README.md, CHANGELOG.md, LICENSE)
- ✅ Verify project structure matches architecture specification (Architecture lines 72-186)
- ✅ Test that `capsule --version` command works as basic smoke test

**Secondary Objectives:**
- ✅ Set up pre-commit hooks for automatic code formatting
- ✅ Configure mypy for strict type checking
- ✅ Create .gitignore for Python projects
- ✅ Initialize semantic versioning at 0.1.0

### Out of Scope

**Explicitly Excluded:**
- ❌ Any business logic implementation (handled in later epics)
- ❌ CLI command implementations beyond basic version display
- ❌ Template creation (Epic 4)
- ❌ Research provider integration (Epic 3)
- ❌ Data model implementations (Epic 1)
- ❌ Deployment to PyPI (post-MVP)
- ❌ Docker containerization (future enhancement)
- ❌ Windows/macOS/Linux specific installers (future enhancement)

**Boundaries:**
- This epic focuses solely on project infrastructure - no domain logic
- CI/CD runs tests but no tests exist yet (test infrastructure created in Epic 13)
- Documentation structure created but content minimal (expanded during implementation)

## System Architecture Alignment

### Architecture References

**Primary Architecture Sections:**
- **Project Initialization** (Architecture lines 19-46)
  - Cookiecutter setup process
  - Core dependency installation
  - Development dependency installation
  - Project structure establishment

- **Decision Summary Table** (Architecture lines 49-67)
  - CLI Framework: Typer 0.9.0+ (type-safe, includes rich formatting)
  - Project Structure: Cookiecutter PyPackage (professional structure, testing, docs)
  - Testing Framework: pytest 7.0+ (de facto standard)
  - Code Formatting: black 23.0+ (uncompromising formatter)
  - Linting: flake8 + mypy (style + type checking)
  - Template Engine: Jinja2 3.1.0+ (for future epics)
  - YAML Libraries: python-frontmatter 1.0.0+, ruamel.yaml 0.17.0+

- **Complete Project Structure** (Architecture lines 70-186)
  - Folder layout: capsule/, tests/, docs/, scripts/
  - Configuration files: pyproject.toml, setup.py, setup.cfg
  - CI/CD: .github/workflows/ci.yml, release.yml

### Architectural Constraints

**Technology Constraints:**
- Python 3.8+ required (NFR29 - Architecture line 1878)
- Cross-platform compatibility: Windows, macOS, Linux (NFR28 - Architecture line 1871)
- PEP 8 compliance mandatory (NFR31 - Architecture line 1889)
- Semantic versioning required (NFR35 - Architecture line 1927)

**Component Dependencies:**
- All future epics depend on this foundation
- Epic 1 (Core Data Models) requires project structure from this epic
- Epic 2 (Configuration Management) requires YAML libraries from this epic
- Epic 9 (CLI Commands) requires Typer framework from this epic
- Epic 13 (Testing Infrastructure) requires pytest configuration from this epic

### Integration Points

**Created by this Epic:**
- Project root directory structure
- Python package namespace (`capsule`)
- Dependency management system (pyproject.toml)
- CI/CD pipeline entry points
- Development toolchain configuration

**Used by Future Epics:**
- All epics will add modules to `capsule/` namespace
- All epics will add tests to `tests/` directory
- All epics will use configured development tools
- All epics will run through CI/CD pipeline

## Detailed Design

### Services and Modules

Epic 0 creates infrastructure, not services. However, it establishes the module structure that future epics will populate:

| Module Path | Purpose | Created By | Populated By |
|-------------|---------|-----------|--------------|
| `capsule/__init__.py` | Package initialization | Epic 0 | Epic 0 (version info) |
| `capsule/__main__.py` | CLI entry point skeleton | Epic 0 | Epic 9 (CLI implementation) |
| `capsule/cli.py` | Typer app definition skeleton | Epic 0 | Epic 9 (command registration) |
| `capsule/commands/` | CLI command implementations | Epic 0 (empty dir) | Epics 9-10 |
| `capsule/core/` | Business logic | Epic 0 (empty dir) | Epics 3-8 |
| `capsule/models/` | Data models | Epic 0 (empty dir) | Epic 1 |
| `capsule/templates/` | Jinja2 templates | Epic 0 (empty dir) | Epic 4, 11 |
| `capsule/utils/` | Utility modules | Epic 0 (empty dir) | Epic 2, 5, 8 |
| `capsule/exceptions.py` | Custom exceptions | Epic 0 (skeleton) | Epic 12 |
| `tests/` | Test suite | Epic 0 (empty structure) | Epic 13 |
| `tests/conftest.py` | Pytest fixtures | Epic 0 (skeleton) | Epic 13 |

### Data Models and Contracts

Epic 0 does not create data models, but establishes the pattern for future models:

**Version Information Model (Created in Epic 0):**

```python
# capsule/__init__.py
"""Obsidian Capsule Delivery System - Python CLI"""

__version__ = "0.1.0"
__author__ = "BMad"
__license__ = "MIT"
```

**Configuration File Contracts (Created in Epic 0):**

**pyproject.toml:**
```toml
[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "obsidian-capsule-cli"
version = "0.1.0"
description = "CLI tool for AI-powered educational content generation in Obsidian"
authors = [{name = "BMad", email = "bmad@example.com"}]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

dependencies = [
    "typer[all]>=0.9.0",
    "python-frontmatter>=1.0.0",
    "ruamel.yaml>=0.17.0",
    "jinja2>=3.1.0",
    "pyyaml>=6.0",
    "requests>=2.31.0",
    "google-generativeai>=0.3.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "black>=23.0",
    "flake8>=6.0",
    "mypy>=1.0",
    "pytest-mock>=3.10",
]

[project.scripts]
capsule = "capsule.cli:app"

[tool.black]
line-length = 100
target-version = ["py38", "py39", "py310", "py311", "py312"]
include = '\.pyi?$'

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

**setup.cfg:**
```ini
[flake8]
max-line-length = 100
exclude = .git,__pycache__,build,dist,.eggs
ignore = E203,W503

[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = --cov=capsule --cov-report=term-missing --cov-report=html
```

### APIs and Interfaces

Epic 0 creates the basic CLI interface contract:

**CLI Entry Point Interface:**

```python
# capsule/__main__.py
"""CLI entry point for python -m capsule"""
from capsule.cli import app

if __name__ == "__main__":
    app()
```

**Typer App Skeleton:**

```python
# capsule/cli.py
"""Main CLI application using Typer framework"""
import typer
from capsule import __version__

app = typer.Typer(
    name="capsule",
    help="Obsidian Capsule Delivery System - AI-powered educational content generation",
    add_completion=False,
)

def version_callback(value: bool):
    """Display version information"""
    if value:
        typer.echo(f"Obsidian Capsule CLI v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    ),
):
    """
    Obsidian Capsule Delivery System
    
    AI-powered content generation and distribution for Obsidian knowledge bases.
    """
    pass

if __name__ == "__main__":
    app()
```

**Exception Base Classes (Skeleton):**

```python
# capsule/exceptions.py
"""Custom exceptions for capsule operations"""

class CapsuleError(Exception):
    """Base exception for all capsule errors"""
    exit_code = 1

class ValidationError(CapsuleError):
    """Schema validation failed"""
    exit_code = 1

class FileError(CapsuleError):
    """File operation failed"""
    exit_code = 2

class NetworkError(CapsuleError):
    """Network/API error"""
    exit_code = 3

class UserCancelledError(CapsuleError):
    """User cancelled operation"""
    exit_code = 4

class ConfigError(CapsuleError):
    """Configuration error"""
    exit_code = 5
```

### Workflows and Sequencing

**Epic 0 Implementation Sequence:**

```
Story 0.1: Project Scaffolding
├─ Step 1: Install Cookiecutter
├─ Step 2: Run cookiecutter gh:audreyfeldroy/cookiecutter-pypackage
│  ├─ Project name: obsidian-capsule-cli
│  ├─ Package name: capsule
│  ├─ Author: BMad
│  ├─ Python version: 3.8+
│  └─ License: MIT
├─ Step 3: Create additional directories (commands, core, models, templates, utils)
├─ Step 4: Create __main__.py and cli.py skeletons
└─ Step 5: Verify directory structure matches architecture

Story 0.2: Core Dependencies Installation
├─ Step 1: Create pyproject.toml with dependencies section
├─ Step 2: Install core dependencies via pip install -e .[dev]
├─ Step 3: Verify imports work (import typer, import frontmatter, etc.)
└─ Step 4: Update __init__.py with version info

Story 0.3: CI/CD Pipeline Setup
├─ Step 1: Create .github/workflows/ci.yml
│  ├─ Test matrix: Python 3.8, 3.9, 3.10, 3.11, 3.12
│  ├─ Platforms: ubuntu-latest, windows-latest, macos-latest
│  ├─ Steps: checkout, setup-python, install deps, run black, run flake8, run mypy, run pytest
│  └─ Coverage upload to Codecov
├─ Step 2: Create .github/workflows/release.yml (manual trigger only)
│  └─ Build wheel, create GitHub release
├─ Step 3: Push to GitHub and verify CI runs
└─ Step 4: Fix any CI failures

Story 0.4: Development Tools Configuration
├─ Step 1: Configure black in pyproject.toml
├─ Step 2: Configure flake8 in setup.cfg
├─ Step 3: Configure mypy in pyproject.toml
├─ Step 4: Create .pre-commit-config.yaml (optional but recommended)
├─ Step 5: Run black on all Python files
├─ Step 6: Run flake8 and fix any issues
├─ Step 7: Run mypy and add type annotations where needed
└─ Step 8: Test that capsule --version works
```

**CI/CD Pipeline Flow:**

```
Git Push (any branch)
    ↓
GitHub Actions Triggered (.github/workflows/ci.yml)
    ↓
Matrix Build (5 Python versions × 3 platforms = 15 jobs)
    ├─ Job 1: Python 3.8 on ubuntu-latest
    │   ├─ Checkout code
    │   ├─ Setup Python 3.8
    │   ├─ Install dependencies (pip install -e .[dev])
    │   ├─ Run black --check .
    │   ├─ Run flake8 capsule/ tests/
    │   ├─ Run mypy capsule/
    │   ├─ Run pytest (will pass with 0 tests initially)
    │   └─ Upload coverage to Codecov
    ├─ Job 2-14: (similar for other Python versions/platforms)
    └─ Job 15: Python 3.12 on macos-latest
    ↓
All jobs must pass (green checkmark)
    ↓
Pull Request can be merged (if PR workflow)
```

**Manual Release Flow:**

```
Developer: Ready to release
    ↓
Manually trigger .github/workflows/release.yml
    ↓
Workflow Actions:
    ├─ Run full CI suite
    ├─ Build source distribution (sdist)
    ├─ Build wheel (bdist_wheel)
    ├─ Create GitHub release with tag (v0.1.0)
    └─ Attach dist files to release
    ↓
Future: Publish to PyPI (post-MVP)
```

## Non-Functional Requirements

### Performance

**Build and CI Performance Targets:**

| Metric | Target | Measurement | Rationale |
|--------|--------|-------------|-----------|
| Local `pip install -e .` time | <60 seconds | Time command | Fast iteration for developers |
| CI pipeline total time | <10 minutes | GitHub Actions duration | Quick feedback loop (NFR general principle) |
| Black formatting time | <5 seconds | Black output | Real-time formatting |
| Flake8 linting time | <10 seconds | Flake8 output | Fast linting feedback |
| Mypy type checking time | <30 seconds | Mypy output | Type safety without slowdown |

**Rationale:** While Epic 0 doesn't have runtime performance requirements, build/CI performance is critical for developer productivity. These targets align with industry standards for Python projects.

### Security

**Dependency Security:**

- **Requirement:** All dependencies must be from trusted PyPI sources
- **Verification:** Use `pip-audit` to scan for known vulnerabilities (optional in Epic 0, recommended for Epic 13)
- **Pinning Strategy:** Use `>=` constraints for flexibility, specific versions in requirements.txt for reproducibility
- **Secrets Management:** No API keys or secrets in Epic 0 (handled in Epic 2 configuration management)

**Code Security:**

- **Requirement:** No hardcoded credentials, API keys, or sensitive data
- **Verification:** flake8 with security plugins (optional enhancement)
- **Git Security:** .gitignore prevents committing __pycache__, .env, config files with secrets

**Source:** NFR10 (Input sanitization), NFR12 (Secure credential storage) - Architecture lines 1733-1743

### Reliability/Availability

**CI/CD Reliability:**

- **Requirement:** CI pipeline must be deterministic (same code = same result)
- **Implementation:** Pin Python versions explicitly (3.8, 3.9, 3.10, 3.11, 3.12)
- **Fallback:** If GitHub Actions unavailable, developers can run tests locally
- **Monitoring:** GitHub Actions provides build status badges

**Dependency Reliability:**

- **Requirement:** Dependencies must be from stable, maintained packages
- **Verification:** All chosen dependencies have 1M+ downloads/month on PyPI
- **Constraints:** Minimum versions specified, no upper bounds (allow patches/minor updates)

**Source:** NFR13-17 (Reliability requirements) - Architecture lines 1747-1802

### Observability

Epic 0 establishes the foundation for observability in future epics:

**Logging Setup (Skeleton):**

```python
# capsule/utils/logger.py (created in Epic 0, populated in Epic 12)
import logging
from pathlib import Path

def setup_logging(verbose: bool = False):
    """
    Configure logging based on verbosity.
    
    Args:
        verbose: Enable debug-level logging if True
        
    Returns:
        Configured logger instance
    """
    # Implementation in Epic 12
    pass
```

**Testing Observability:**

- **Requirement:** pytest generates coverage reports (HTML + terminal)
- **Implementation:** `pytest-cov` configured in setup.cfg
- **Output:** Coverage report shows % coverage per file
- **CI Integration:** Codecov uploads for trend tracking

**Source:** NFR17 (Detailed logs), Architecture lines 1799-1802

## Dependencies and Integrations

### Core Dependencies (Installed in Story 0.2)

| Dependency | Version | Purpose | Used By | Source |
|-----------|---------|---------|---------|--------|
| **typer[all]** | >=0.9.0 | CLI framework with rich output | Epic 9 (CLI commands) | Architecture line 53 |
| **python-frontmatter** | >=1.0.0 | YAML frontmatter parsing | Epic 8 (Merge strategies) | Architecture line 55 |
| **ruamel.yaml** | >=0.17.0 | YAML with comment preservation | Epic 2 (Config), Epic 6 (Cypher) | Architecture line 56 |
| **jinja2** | >=3.1.0 | Template rendering | Epic 4 (Content generation) | Architecture line 57 |
| **pyyaml** | >=6.0 | Config file parsing | Epic 2 (User config) | Architecture line 65 |
| **requests** | >=2.31.0 | HTTP requests | Epic 3 (Research API calls) | Architecture line 62 |
| **google-generativeai** | >=0.3.0 | Gemini API client | Epic 3 (Research provider) | Architecture line 204 |

### Development Dependencies (Installed in Story 0.2)

| Dependency | Version | Purpose | Used By | Source |
|-----------|---------|---------|---------|--------|
| **pytest** | >=7.0 | Testing framework | Epic 13 (All tests) | Architecture line 58 |
| **pytest-cov** | >=4.0 | Coverage reporting | Epic 13 (Coverage) | Architecture line 58 |
| **black** | >=23.0 | Code formatting | Epic 0 (CI/CD) | Architecture line 59 |
| **flake8** | >=6.0 | Style linting | Epic 0 (CI/CD) | Architecture line 60 |
| **mypy** | >=1.0 | Type checking | Epic 0 (CI/CD) | Architecture line 60 |
| **pytest-mock** | >=3.10 | Mocking for tests | Epic 13 (Unit tests) | Architecture line 214 |

### External Integrations

**GitHub Actions:**
- **Integration Point:** .github/workflows/*.yml
- **Authentication:** GitHub token (automatic)
- **Triggers:** Push, pull request, manual dispatch
- **Outputs:** Build status, test results, coverage reports

**Codecov (Optional):**
- **Integration Point:** Coverage upload in CI
- **Authentication:** CODECOV_TOKEN secret
- **Purpose:** Track coverage trends over time
- **Setup:** Add token to GitHub secrets (Story 0.3)

### Python Runtime Requirements

| Requirement | Version | Constraint | Rationale |
|-------------|---------|------------|-----------|
| **Python** | >=3.8 | Minimum version | NFR29 - Python 3.8+ support |
| **pip** | >=21.0 | Recommended | Modern pip features |
| **setuptools** | >=45 | Build requirement | pyproject.toml support |
| **wheel** | Latest | Build requirement | Wheel distribution |

### Operating System Support

| OS | Tested Versions | CI Platform | Notes |
|----|----------------|-------------|-------|
| **Ubuntu Linux** | 20.04, 22.04 | ubuntu-latest | Primary development platform |
| **macOS** | 11, 12, 13 | macos-latest | Apple Silicon + Intel |
| **Windows** | 10, 11 | windows-latest | PowerShell + CMD support |

**Source:** NFR28 (Cross-platform), Architecture line 1871

## Acceptance Criteria (Authoritative)

### Story 0.1: Project Scaffolding

**AC1.1:** Project directory structure matches architecture specification exactly (Architecture lines 72-186)
- `capsule/` package directory exists with `__init__.py`
- Subdirectories exist: `commands/`, `core/`, `models/`, `templates/`, `utils/`
- `tests/` directory exists with mirror structure
- `docs/` directory exists
- Root files exist: `README.md`, `pyproject.toml`, `setup.py`, `setup.cfg`, `.gitignore`, `LICENSE`

**AC1.2:** Package is importable in Python
- `python -c "import capsule"` succeeds without errors
- `capsule.__version__` returns "0.1.0"

**AC1.3:** Entry point is defined and callable
- `capsule/__main__.py` exists and imports `cli.app`
- `python -m capsule --help` displays help message

### Story 0.2: Core Dependencies Installation

**AC2.1:** All core dependencies install successfully
- `pip install -e .` completes without errors
- `pip list | grep typer` shows typer>=0.9.0
- `pip list | grep python-frontmatter` shows python-frontmatter>=1.0.0
- `pip list | grep ruamel.yaml` shows ruamel.yaml>=0.17.0
- `pip list | grep jinja2` shows jinja2>=3.1.0
- `pip list | grep pyyaml` shows pyyaml>=6.0
- `pip list | grep requests` shows requests>=2.31.0
- `pip list | grep google-generativeai` shows google-generativeai>=0.3.0

**AC2.2:** All dev dependencies install successfully
- `pip install -e .[dev]` completes without errors
- `black --version` shows black>=23.0
- `flake8 --version` shows flake8>=6.0
- `mypy --version` shows mypy>=1.0
- `pytest --version` shows pytest>=7.0

**AC2.3:** All dependencies can be imported
- `python -c "import typer; import frontmatter; import ruamel.yaml; import jinja2; import yaml; import requests; import google.generativeai"` succeeds

### Story 0.3: CI/CD Pipeline Setup

**AC3.1:** GitHub Actions CI workflow file exists and is valid
- `.github/workflows/ci.yml` exists
- YAML syntax is valid (no parsing errors)
- Workflow includes matrix for Python 3.8, 3.9, 3.10, 3.11, 3.12
- Workflow includes platforms: ubuntu-latest, windows-latest, macos-latest

**AC3.2:** CI workflow runs all quality checks
- Workflow runs `black --check .` (formatting check)
- Workflow runs `flake8 capsule/ tests/` (linting)
- Workflow runs `mypy capsule/` (type checking)
- Workflow runs `pytest` (tests - will show 0 tests initially)

**AC3.3:** CI workflow passes on push to main branch
- Push to main triggers CI
- All matrix jobs (15 total) complete successfully
- Green checkmark appears on commit in GitHub

**AC3.4:** GitHub Actions release workflow exists
- `.github/workflows/release.yml` exists
- Workflow is manual trigger only (workflow_dispatch)
- Workflow builds source distribution and wheel

### Story 0.4: Development Tools Configuration

**AC4.1:** Black formatter is configured and passes
- `pyproject.toml` contains `[tool.black]` section
- `black --check capsule/ tests/` exits with code 0 (no changes needed)
- Line length is set to 100 characters
- Target versions include py38 through py312

**AC4.2:** Flake8 linter is configured and passes
- `setup.cfg` contains `[flake8]` section
- `flake8 capsule/ tests/` exits with code 0 (no violations)
- Max line length is 100
- Excludes .git, __pycache__, build, dist, .eggs

**AC4.3:** Mypy type checker is configured and passes
- `pyproject.toml` contains `[tool.mypy]` section
- `mypy capsule/` exits with code 0 (no type errors)
- `python_version` is set to "3.8"
- `disallow_untyped_defs = true` is enabled

**AC4.4:** CLI version command works
- `capsule --version` displays "Obsidian Capsule CLI v0.1.0"
- `python -m capsule --version` displays the same
- Exit code is 0

**AC4.5:** Help command works
- `capsule --help` displays usage information
- Help message includes "Obsidian Capsule Delivery System"
- Help message includes "--version" option

## Traceability Mapping

| AC ID | Spec Section | Components | Test Strategy |
|-------|--------------|------------|---------------|
| AC1.1 | Detailed Design → Services and Modules | Directory structure | Manual verification + pytest test for directory existence |
| AC1.2 | APIs and Interfaces → CLI Entry Point | `capsule/__init__.py` | Unit test: `test_package_import()` |
| AC1.3 | APIs and Interfaces → CLI Entry Point | `capsule/__main__.py`, `capsule/cli.py` | Integration test: subprocess call |
| AC2.1 | Dependencies → Core Dependencies | pyproject.toml dependencies | Integration test: import checks |
| AC2.2 | Dependencies → Development Dependencies | pyproject.toml dev dependencies | Integration test: CLI version checks |
| AC2.3 | Dependencies → Core Dependencies | All imports | Unit test: `test_all_imports()` |
| AC3.1 | Workflows → CI/CD Pipeline Flow | .github/workflows/ci.yml | YAML validation + manual GitHub check |
| AC3.2 | Workflows → CI/CD Pipeline Flow | GitHub Actions steps | Manual verification in Actions UI |
| AC3.3 | Workflows → CI/CD Pipeline Flow | Full CI pipeline | End-to-end test: push to branch |
| AC3.4 | Workflows → Manual Release Flow | .github/workflows/release.yml | Manual verification in Actions UI |
| AC4.1 | Non-Functional → Performance (Build) | pyproject.toml [tool.black] | CI check + local run |
| AC4.2 | Non-Functional → Performance (Build) | setup.cfg [flake8] | CI check + local run |
| AC4.3 | Non-Functional → Performance (Build) | pyproject.toml [tool.mypy] | CI check + local run |
| AC4.4 | APIs and Interfaces → Typer App Skeleton | capsule/cli.py version_callback() | Integration test: subprocess call |
| AC4.5 | APIs and Interfaces → Typer App Skeleton | capsule/cli.py main() docstring | Integration test: subprocess call |

## Risks, Assumptions, Open Questions

### Risks

**R1: Cookiecutter template changes**
- **Description:** cookiecutter-pypackage template may have breaking changes
- **Likelihood:** Low (template is stable)
- **Impact:** Medium (would require manual adjustments)
- **Mitigation:** Pin to specific template version if needed, fork template if critical
- **Owner:** Dev implementing Story 0.1

**R2: CI matrix timeout on slower platforms**
- **Description:** macOS or Windows runners may be slower, causing timeouts
- **Likelihood:** Low (Epic 0 has no heavy operations)
- **Impact:** Low (can increase timeout or reduce matrix)
- **Mitigation:** Monitor CI times, adjust timeout to 15 minutes if needed
- **Owner:** Dev implementing Story 0.3

**R3: Dependency version conflicts**
- **Description:** Future dependency updates may introduce breaking changes
- **Likelihood:** Medium (dependencies evolve)
- **Impact:** Medium (could break builds)
- **Mitigation:** CI tests on multiple Python versions, dependabot alerts, version constraints
- **Owner:** Team (ongoing maintenance)

**R4: Type checking strictness may slow development**
- **Description:** `disallow_untyped_defs = true` requires all functions to have type hints
- **Likelihood:** High (this is strict)
- **Impact:** Low (improves code quality, slight developer overhead)
- **Mitigation:** Team agrees to maintain type hints, mypy cache speeds subsequent runs
- **Owner:** Team (ongoing practice)

### Assumptions

**A1: GitHub Actions is available and reliable**
- **Assumption:** GitHub Actions will be the CI/CD platform
- **Validation:** GitHub Actions has 99.9% uptime SLA
- **Impact if false:** Would need alternative CI (CircleCI, Travis, GitLab CI)

**A2: Python 3.8+ is sufficient for all platforms**
- **Assumption:** Target users have Python 3.8 or newer
- **Validation:** Python 3.8 released 2019, widely available
- **Impact if false:** Would need to support Python 3.7 (out of scope per NFR29)

**A3: Developers have git, Python, pip installed locally**
- **Assumption:** Standard development environment assumed
- **Validation:** Document requirements in README.md
- **Impact if false:** Provide installation instructions for these tools

**A4: MIT License is acceptable**
- **Assumption:** Open-source project with permissive license
- **Validation:** Aligns with PRD vision of ecosystem adoption
- **Impact if false:** License change requires legal review

### Open Questions

**Q1: Should we use Poetry or stick with pip + pyproject.toml?**
- **Context:** Poetry offers better dependency resolution but adds complexity
- **Recommendation:** Use pip + pyproject.toml for simplicity (per Architecture decision)
- **Decision Owner:** Architect (already decided in Architecture doc)
- **Resolution:** Closed - using pip + pyproject.toml per Architecture line 54

**Q2: Should we use pre-commit hooks for automatic formatting?**
- **Context:** Pre-commit hooks auto-format on git commit
- **Recommendation:** Yes, optional but recommended (enhances DX)
- **Decision Owner:** Dev implementing Story 0.4
- **Resolution:** Optional - include `.pre-commit-config.yaml` template

**Q3: What should be the initial version number?**
- **Context:** Semantic versioning starts at 0.1.0 or 1.0.0
- **Recommendation:** 0.1.0 (signals pre-release per semver)
- **Decision Owner:** Product Owner
- **Resolution:** Closed - using 0.1.0 per Architecture

**Q4: Should we publish to TestPyPI during CI?**
- **Context:** TestPyPI allows testing package installation
- **Recommendation:** No, defer to post-MVP (keeps Epic 0 simple)
- **Decision Owner:** Team
- **Resolution:** Closed - out of scope for Epic 0

## Test Strategy Summary

### Test Levels

Epic 0 creates infrastructure for future testing but does not implement comprehensive tests (Epic 13 handles that). However, basic smoke tests are recommended:

**Unit Tests (Minimal in Epic 0):**
- `test_package_import()` - Verify `import capsule` works
- `test_version_defined()` - Verify `capsule.__version__` exists
- `test_all_core_imports()` - Verify all dependencies can be imported

**Integration Tests (Recommended in Epic 0):**
- `test_cli_version_command()` - Verify `capsule --version` works
- `test_cli_help_command()` - Verify `capsule --help` works
- `test_entry_point_works()` - Verify `python -m capsule` works

**End-to-End Tests (Manual in Epic 0):**
- Manual verification: Push code → CI runs → All checks pass
- Manual verification: Run `capsule --version` on Windows, macOS, Linux

**Test Framework Setup:**

```python
# tests/test_basic.py (Created in Story 0.4 for smoke tests)
"""Basic smoke tests for Epic 0 infrastructure"""
import subprocess
import sys

def test_package_import():
    """Verify capsule package can be imported"""
    import capsule
    assert capsule.__version__ == "0.1.0"

def test_all_core_imports():
    """Verify all core dependencies can be imported"""
    import typer
    import frontmatter
    import ruamel.yaml
    import jinja2
    import yaml
    import requests
    import google.generativeai
    # If this function completes, all imports succeeded

def test_cli_version_command():
    """Verify capsule --version works"""
    result = subprocess.run(
        [sys.executable, "-m", "capsule", "--version"],
        capture_output=True,
        text=True,
        timeout=5,
    )
    assert result.returncode == 0
    assert "0.1.0" in result.stdout

def test_cli_help_command():
    """Verify capsule --help works"""
    result = subprocess.run(
        [sys.executable, "-m", "capsule", "--help"],
        capture_output=True,
        text=True,
        timeout=5,
    )
    assert result.returncode == 0
    assert "Obsidian Capsule Delivery System" in result.stdout
```

### Coverage Targets

**Epic 0 Coverage Target:** 80%+ (only a few files exist)
- `capsule/__init__.py` - 100% (simple module)
- `capsule/__main__.py` - 100% (one-liner)
- `capsule/cli.py` - 90%+ (version callback, main function)
- `capsule/exceptions.py` - 50%+ (classes defined but not used yet)

**CI Integration:**
- pytest-cov generates HTML and terminal reports
- Coverage report shows per-file coverage
- Codecov uploads track coverage trends (optional)

### Test Execution

**Local Development:**
```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=capsule --cov-report=html

# Run specific test
pytest tests/test_basic.py::test_package_import -v
```

**CI Pipeline:**
```yaml
# .github/workflows/ci.yml includes:
- name: Run tests with coverage
  run: pytest --cov=capsule --cov-report=xml

- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
```

### Definition of Done for Epic 0

Epic 0 is considered **DONE** when:

✅ All 4 stories (0.1, 0.2, 0.3, 0.4) are complete  
✅ All 17 acceptance criteria pass  
✅ CI pipeline passes on main branch (all 15 matrix jobs green)  
✅ `capsule --version` works on developer machine  
✅ All development tools (black, flake8, mypy) pass with zero issues  
✅ Code coverage ≥80% for Epic 0 files  
✅ README.md documents how to install and run basic commands  
✅ Epic 0 retrospective completed (optional)

---

## Appendix A: File Checklist

Files that MUST exist after Epic 0 completion:

**Root Directory:**
- [ ] `README.md` - Project overview and quick start
- [ ] `LICENSE` - MIT license file
- [ ] `CHANGELOG.md` - Version history (0.1.0 entry)
- [ ] `pyproject.toml` - Modern Python project configuration
- [ ] `setup.py` - Backward compatibility wrapper
- [ ] `setup.cfg` - Tool configuration (flake8, pytest)
- [ ] `.gitignore` - Python gitignore template
- [ ] `.python-version` - pyenv version file (3.8)

**Package Directory (capsule/):**
- [ ] `capsule/__init__.py` - Package initialization with version
- [ ] `capsule/__main__.py` - CLI entry point
- [ ] `capsule/cli.py` - Typer app definition
- [ ] `capsule/exceptions.py` - Custom exception classes
- [ ] `capsule/commands/__init__.py` - Empty (populated in Epic 9)
- [ ] `capsule/core/__init__.py` - Empty (populated in Epics 3-8)
- [ ] `capsule/models/__init__.py` - Empty (populated in Epic 1)
- [ ] `capsule/templates/` - Empty directory (populated in Epic 4, 11)
- [ ] `capsule/utils/__init__.py` - Empty (populated in Epic 2, 5, 8)

**Test Directory (tests/):**
- [ ] `tests/__init__.py` - Empty
- [ ] `tests/conftest.py` - Pytest configuration skeleton
- [ ] `tests/test_basic.py` - Basic smoke tests
- [ ] `tests/test_commands/__init__.py` - Empty (Epic 9-10)
- [ ] `tests/test_core/__init__.py` - Empty (Epics 3-8)
- [ ] `tests/test_models/__init__.py` - Empty (Epic 1)
- [ ] `tests/test_utils/__init__.py` - Empty (Epic 2, 5, 8)

**CI/CD (.github/workflows/):**
- [ ] `.github/workflows/ci.yml` - Continuous integration
- [ ] `.github/workflows/release.yml` - Release automation

**Documentation (docs/):**
- [ ] `docs/PRD.md` - Existing (from planning phase)
- [ ] `docs/architecture.md` - Existing (from solutioning phase)
- [ ] `docs/sprint-artifacts/sprint-status.yaml` - Existing (from sprint planning)
- [ ] `docs/sprint-artifacts/tech-spec-epic-0.md` - This document

---

## Appendix B: Command Reference

Essential commands for Epic 0 development:

**Installation:**
```bash
# Install in editable mode with dev dependencies
pip install -e .[dev]

# Verify installation
capsule --version
```

**Development Tools:**
```bash
# Format code with black
black capsule/ tests/

# Check formatting without changes
black --check capsule/ tests/

# Lint with flake8
flake8 capsule/ tests/

# Type check with mypy
mypy capsule/

# Run all quality checks
black --check . && flake8 capsule/ tests/ && mypy capsule/
```

**Testing:**
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=capsule --cov-report=html

# Run specific test file
pytest tests/test_basic.py -v

# Run specific test function
pytest tests/test_basic.py::test_package_import -v
```

**Build:**
```bash
# Build source distribution
python -m build --sdist

# Build wheel
python -m build --wheel

# Build both
python -m build
```

**Git Workflow:**
```bash
# Create feature branch for Story 0.1
git checkout -b story/0-1-project-scaffolding

# Make changes, commit
git add .
git commit -m "feat: initialize project structure with Cookiecutter"

# Push and create PR
git push -u origin story/0-1-project-scaffolding
```

---

**END OF EPIC 0 TECHNICAL SPECIFICATION**

This specification is the authoritative reference for implementing Epic 0: Foundation & Project Setup. All stories within this epic must align with the requirements, acceptance criteria, and architectural decisions documented here.

**Next Step:** Use `workflow create-story` to draft Story 0.1: Project Scaffolding
