# Testing and Coverage Guide

## Overview

This project uses **pytest** with **pytest-cov** for comprehensive test coverage tracking. Coverage analysis helps ensure code quality by identifying untested code paths and measuring the effectiveness of the test suite.

## Current Coverage Status

- **Overall Coverage**: 63.41% (with branch coverage)
- **Minimum Threshold**: 60% (CI fails below this)
- **Target Goal**: 80% overall coverage
- **Test Count**: 346 tests (11 E2E, ~335 unit/integration)

### Coverage by Module Type

| Module Type | Current Coverage | Target | Status |
|-------------|------------------|--------|--------|
| **Models** (`capsule/models/`) | 95%+ | 90% | ✅ Excellent |
| **Core Logic** (`capsule/core/`) | Mixed (16-100%) | 90% | ⚠️ Needs improvement |
| **Commands** (`capsule/commands/`) | Mixed (0-100%) | 85% | ⚠️ Needs improvement |
| **Utilities** (`capsule/utils/`) | Mixed (0-100%) | 80% | ⚠️ Needs improvement |

## Running Coverage Locally

### Quick Start

Run all tests with coverage report:

```bash
pytest
```

This automatically runs with coverage enabled (configured in `pyproject.toml`).

### View Detailed HTML Report

After running tests, open the interactive HTML report:

```bash
# Generate coverage (done automatically by pytest)
pytest

# Open HTML report in browser
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

The HTML report shows:
- Line-by-line coverage highlighting
- Missed lines in red
- Covered lines in green
- Branch coverage details

### Coverage Report Formats

The test suite generates three coverage report formats:

1. **Terminal Report** - Shows in console after test run
   ```bash
   pytest  # View summary at end of output
   ```

2. **HTML Report** - Interactive browsable report
   ```bash
   # Generated in htmlcov/ directory
   open htmlcov/index.html
   ```

3. **XML Report** - Machine-readable format for CI/CD
   ```bash
   # Generated as coverage.xml
   # Used by coverage services and CI tooling
   ```

### Run Coverage for Specific Tests

Run coverage for a specific test file:

```bash
pytest tests/test_models/test_capsule.py
```

Run coverage for specific test markers:

```bash
pytest -m unit  # Only unit tests
pytest -m integration  # Only integration tests
pytest -m e2e  # Only end-to-end tests
```

### Generate Coverage Report Without Running Tests

If tests were already run:

```bash
coverage report  # Terminal summary
coverage html    # Generate HTML report
```

## Understanding Coverage Reports

### Coverage Metrics

**Statement Coverage**: Percentage of code statements executed during tests.

**Branch Coverage**: Percentage of decision branches (if/else) tested.
- More stringent than statement coverage
- Requires testing both True and False paths of conditionals

Example:
```python
def example(value):
    if value > 0:  # Branch point
        return "positive"
    else:
        return "negative"
```

- **100% statement coverage**: Test with `value=1` only
- **100% branch coverage**: Test with both `value=1` AND `value=-1`

### Reading the Terminal Report

```
Name                                     Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------------------------
capsule/models/capsule.py                   26      2      4      2  86.67%   51, 75, 99
capsule/core/merger.py                      76      2     48      3  94.35%   112-115
```

- **Stmts**: Total statements in file
- **Miss**: Statements not covered by tests
- **Branch**: Total branch points (if/else)
- **BrPart**: Partially covered branches (one path tested, not both)
- **Cover**: Percentage coverage
- **Missing**: Line numbers not covered

### Interpreting HTML Report

The HTML report color codes:

- 🟢 **Green**: Fully covered lines
- 🔴 **Red**: Not covered by any test
- 🟡 **Yellow**: Partially covered (branch not fully tested)

Click on any file to see line-by-line coverage with annotations.

## Coverage Thresholds and Rationale

### Current Threshold: 60%

The CI pipeline enforces a **minimum 60% coverage** threshold. Builds fail if coverage drops below this level.

**Rationale**: 
- Baseline established from current test suite (63.41%)
- Prevents coverage regression
- Conservative starting point for brownfield project

### Target Thresholds by Module

Following the architecture document's testing strategy:

| Module Category | Threshold | Rationale |
|-----------------|-----------|-----------|
| **Critical Paths** (core logic, models) | 90%+ | High-risk code, core business logic |
| **Commands** (CLI entry points) | 85%+ | User-facing, integration points |
| **Utilities** (helpers, tools) | 80%+ | Supporting code, lower risk |
| **Overall Project** | 80%+ | Industry standard for production code |

### Excluded from Coverage

The following are intentionally excluded from coverage metrics:

- **Test files** (`tests/**`) - Don't measure test coverage
- **`__init__.py`** files - Usually just imports
- **`__main__.py`** - Entry point, tested via E2E
- **Type stubs and protocols** - No runtime behavior
- **Abstract methods** - Tested via implementations
- **Defensive assertions** - `raise NotImplementedError`

See `pyproject.toml` `[tool.coverage.report]` section for complete exclusion patterns.

## Coverage in CI/CD

### GitHub Actions Integration

Coverage runs automatically on every push and pull request:

```yaml
# .github/workflows/test.yml
- name: Run tests with coverage
  run: pytest --cov=capsule --cov-fail-under=60

- name: Upload coverage reports
  uses: actions/upload-artifact@v4
  with:
    name: coverage-reports-${{ matrix.python-version }}
    path: htmlcov/
```

### Viewing CI Coverage Reports

1. Navigate to GitHub Actions run
2. Scroll to "Artifacts" section
3. Download `coverage-reports-3.12` (or other Python version)
4. Extract and open `htmlcov/index.html`

### Coverage Badges

The README displays a coverage badge:

[![Coverage](https://img.shields.io/badge/coverage-63%25-yellow.svg)](htmlcov/index.html)

**Badge Colors**:
- 🟢 Green: ≥80% coverage (excellent)
- 🟡 Yellow: 60-79% coverage (good, needs improvement)
- 🔴 Red: <60% coverage (insufficient, CI fails)

**Updating the Badge**:

After improving coverage, update the badge in `README.md`:

```markdown
[![Coverage](https://img.shields.io/badge/coverage-XX%25-COLOR.svg)](htmlcov/index.html)
```

Replace `XX` with new percentage and `COLOR` with:
- `green` for ≥80%
- `yellow` for 60-79%
- `red` for <60%

## Improving Coverage

### Identify Coverage Gaps

1. **Run coverage with missing lines**:
   ```bash
   pytest
   # Look for "Missing" column in terminal output
   ```

2. **View HTML report**:
   ```bash
   open htmlcov/index.html
   # Click on files with low coverage
   # Red lines show untested code
   ```

3. **Sort by coverage**:
   ```bash
   coverage report --sort=cover
   # Shows lowest coverage files first
   ```

### Priority Modules for Improvement

Based on current coverage analysis:

**Critical (0% coverage, needs urgent attention):**
- `capsule/commands/config.py` (0%)
- `capsule/commands/conversation.py` (0%)
- `capsule/commands/research.py` (0%)
- `capsule/utils/config.py` (0%)
- `capsule/utils/output.py` (0%)

**Important (Low coverage, high risk):**
- `capsule/core/template_engine.py` (16%)
- `capsule/utils/validation.py` (16%)

**Good candidates for quick wins:**
- `capsule/utils/versioning.py` (67% → target 80%)
- `capsule/core/slides_generator.py` (62% → target 90%)

### Writing Coverage-Focused Tests

When writing tests to improve coverage:

1. **Test both success and error paths**:
   ```python
   def test_function_success():
       result = function(valid_input)
       assert result == expected
   
   def test_function_with_invalid_input():
       with pytest.raises(ValueError):
           function(invalid_input)
   ```

2. **Test all branches**:
   ```python
   def test_condition_true():
       result = function(condition=True)
       assert result == "true path"
   
   def test_condition_false():
       result = function(condition=False)
       assert result == "false path"
   ```

3. **Use parametrize for multiple scenarios**:
   ```python
   @pytest.mark.parametrize("input,expected", [
       (1, "positive"),
       (0, "zero"),
       (-1, "negative"),
   ])
   def test_classify_number(input, expected):
       assert classify(input) == expected
   ```

## Coverage Configuration

### pyproject.toml Configuration

Coverage is configured in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
# Automatically run coverage with pytest
addopts = "--cov=capsule --cov-report=term-missing --cov-report=html --cov-report=xml"

[tool.coverage.run]
# Enable branch coverage (more stringent)
branch = true

# Source code to measure
source = ["capsule"]

# Files to exclude from coverage
omit = [
    "tests/*",
    "*/__pycache__/*",
    "*/conftest.py",
    "*/__init__.py",
    "capsule/__main__.py",
]

[tool.coverage.report]
# Fail if coverage below 60%
fail_under = 60.0

# Show 2 decimal places
precision = 2

# Show missing lines
show_missing = true

# Patterns to exclude from coverage
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
    "class .*\\bProtocol\\):",
    "@(abc\\.)?abstractmethod",
]
```

### Exclude Code from Coverage

Use `# pragma: no cover` to exclude specific lines:

```python
def debug_only_function():  # pragma: no cover
    """Only used in development, not in production"""
    print(debugging_info)
```

## Best Practices

### DO:
✅ Run tests with coverage before committing
✅ Aim for 100% coverage on critical paths (core logic, models)
✅ Test both success and error cases
✅ Use branch coverage (enabled by default)
✅ Review HTML coverage report for gaps
✅ Add tests when coverage drops

### DON'T:
❌ Write tests just to hit 100% coverage (test behavior, not lines)
❌ Ignore low coverage warnings in CI
❌ Skip error handling tests (these catch bugs!)
❌ Exclude production code from coverage without good reason
❌ Test implementation details instead of contracts

## Troubleshooting

### Coverage Report Shows 0% for Everything

**Cause**: Coverage data not collected during test run.

**Solution**:
```bash
# Ensure pytest-cov is installed
pip install pytest-cov

# Run with explicit coverage
pytest --cov=capsule
```

### Coverage Lower Than Expected

**Cause**: Branch coverage is more stringent than statement coverage.

**Explanation**: 
- Statement coverage: 67%
- Branch coverage: 63%

This is normal. Branch coverage requires testing both paths of if/else.

### CI Fails with "Coverage Below Threshold"

**Cause**: Coverage dropped below 60%.

**Solution**:
1. Run `pytest` locally to see current coverage
2. Identify missing tests with `coverage report --sort=cover`
3. Add tests to improve coverage
4. Commit and push

### HTML Report Not Generated

**Cause**: Missing `[tool.coverage.html]` configuration or file write error.

**Solution**:
```bash
# Manually generate HTML report
coverage html

# Check for write permission errors
ls -la htmlcov/
```

## References

- **pytest-cov Documentation**: https://pytest-cov.readthedocs.io/
- **Coverage.py Documentation**: https://coverage.readthedocs.io/
- **Project Testing Strategy**: See `docs/architecture.md#testing-strategy`
- **CI Workflow**: See `.github/workflows/test.yml`
- **Test Organization**: See `tests/README.md` (if exists)

## Coverage Roadmap

### Current State (Story 14-5)
- ✅ Coverage tool configured
- ✅ CI integration complete
- ✅ Baseline established: 63.41%
- ✅ Minimum threshold: 60%
- ✅ Documentation complete

### Next Steps (Future Stories)
- [ ] Increase threshold to 70% (after gap-filling)
- [ ] Increase threshold to 80% (target goal)
- [ ] Achieve 90%+ coverage on critical paths
- [ ] Integrate with Codecov or Coveralls (optional)
- [ ] Add coverage trend tracking

## Questions?

If you have questions about coverage or testing:
1. Review this guide
2. Check the HTML coverage report for specific files
3. Consult the architecture document's testing strategy
4. Ask in team discussions or PRs

---

**Last Updated**: 2025-11-23 (Story 14-5)
**Maintained By**: Development Team
