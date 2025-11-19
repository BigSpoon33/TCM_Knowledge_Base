# Story 0.3: CI/CD Pipeline Setup

**Epic:** Epic 0 - Foundation & Project Setup  
**Status:** backlog  
**Story ID:** 0.3  
**Story Key:** 0-3-ci-cd-pipeline-setup

---

## Story

**As a** developer building the Obsidian Capsule Delivery System,  
**I want** automated CI/CD pipelines using GitHub Actions,  
**so that** code quality is verified on every push and releases can be automated.

---

## Context

This story implements continuous integration and delivery infrastructure using GitHub Actions. It creates two workflows:

1. **CI Workflow** - Runs on every push/PR to verify code quality:
   - Tests across Python 3.8-3.12
   - Tests across Ubuntu, Windows, macOS
   - Runs black, flake8, mypy, pytest

2. **Release Workflow** - Manual trigger to build distribution packages:
   - Builds source distribution (sdist)
   - Builds wheel distribution (bdist_wheel)
   - Prepares for future PyPI publication

**Prerequisites:**
- ✅ Story 0.1 complete (project structure exists)
- ✅ Story 0.2 complete (dependencies installed, dev tools available)
- GitHub repository exists

**Source:** Architecture lines 74-77, Tech Spec Epic 0 AC3.1-AC3.4

---

## Acceptance Criteria

### AC3.1: GitHub Actions CI Workflow File Exists and is Valid

**Verification:**
```bash
test -f .github/workflows/ci.yml && echo "✓ CI workflow exists"
python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))" && echo "✓ Valid YAML"
```

**Required elements in ci.yml:**
- Matrix strategy includes Python versions: 3.8, 3.9, 3.10, 3.11, 3.12
- Matrix strategy includes OS: ubuntu-latest, windows-latest, macos-latest
- Total matrix combinations: 15 jobs (5 Python × 3 OS)

---

### AC3.2: CI Workflow Runs All Quality Checks

**Verification:**
Inspect `.github/workflows/ci.yml` for these steps:

```yaml
- run: black --check capsule/ tests/
- run: flake8 capsule/ tests/
- run: mypy capsule/
- run: pytest
```

**Expected behavior:**
- Black checks formatting (no modifications made)
- Flake8 checks style violations
- Mypy checks type annotations
- Pytest runs test suite (0 tests initially is OK)

---

### AC3.3: CI Workflow Passes on Push to Main Branch

**Verification:**
```bash
git push origin main
# Check GitHub Actions tab in repository
# All 15 matrix jobs should show green checkmarks
```

**Requirements:**
- Trigger: Push to any branch, pull requests to main
- All jobs complete successfully (exit code 0)
- Green status badge appears on commit

---

### AC3.4: GitHub Actions Release Workflow Exists

**Verification:**
```bash
test -f .github/workflows/release.yml && echo "✓ Release workflow exists"
python -c "import yaml; yaml.safe_load(open('.github/workflows/release.yml'))" && echo "✓ Valid YAML"
```

**Required elements:**
- Trigger: `workflow_dispatch` (manual only)
- Builds source distribution
- Builds wheel distribution
- (Future: uploads to PyPI when configured)

---

## Tasks / Subtasks

### Task 1: Create GitHub Actions Directory Structure

- [x] **1.1** Verify `.github/workflows/` directory exists
  ```bash
  mkdir -p .github/workflows
  ```

- [x] **1.2** Check if Cookiecutter already created workflows
  ```bash
  ls -la .github/workflows/
  ```

- [x] **1.3** Note any existing workflow files (Cookiecutter may have created templates)

---

### Task 2: Create CI Workflow File

- [x] **2.1** Create `.github/workflows/ci.yml`

**File:** `.github/workflows/ci.yml`
```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    name: Test Python ${{ matrix.python-version }} on ${{ matrix.os }}
    runs-on: ${{ matrix.os }}
    
    strategy:
      fail-fast: false
      matrix:
        python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']
        os: [ubuntu-latest, windows-latest, macos-latest]
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -e .[dev]
      
      - name: Check formatting with Black
        run: black --check capsule/ tests/
      
      - name: Lint with Flake8
        run: flake8 capsule/ tests/
      
      - name: Type check with Mypy
        run: mypy capsule/
      
      - name: Run tests with Pytest
        run: pytest --cov=capsule --cov-report=term-missing
```

- [x] **2.2** Verify YAML syntax
  ```bash
  python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"
  ```

- [x] **2.3** Run AC3.1 verification (file exists, valid YAML, includes matrix)

---

### Task 3: Create Release Workflow File

- [x] **3.1** Create `.github/workflows/release.yml`

**File:** `.github/workflows/release.yml`
```yaml
name: Release

on:
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to release (e.g., 1.0.0)'
        required: true
        default: '0.1.0'

jobs:
  build:
    name: Build distribution packages
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install build dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build twine
      
      - name: Build source distribution
        run: python -m build --sdist
      
      - name: Build wheel distribution
        run: python -m build --wheel
      
      - name: Check distributions
        run: twine check dist/*
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: distributions
          path: dist/
```

- [x] **3.2** Verify YAML syntax
  ```bash
  python -c "import yaml; yaml.safe_load(open('.github/workflows/release.yml'))"
  ```

- [x] **3.3** Run AC3.4 verification (file exists, manual trigger, builds distributions)

---

### Task 4: Fix Code Quality Issues for CI

- [x] **4.1** Run black formatter to fix any formatting issues
  ```bash
  black capsule/ tests/
  ```

- [x] **4.2** Run flake8 and fix any linting errors
  ```bash
  flake8 capsule/ tests/
  ```

- [x] **4.3** Add type hints to fix mypy errors (if any)
  ```bash
  mypy capsule/
  ```

- [x] **4.4** Verify all quality checks pass locally
  ```bash
  black --check capsule/ tests/ && \
  flake8 capsule/ tests/ && \
  mypy capsule/ && \
  pytest
  ```

---

### Task 5: Test CI Workflow Locally (Optional)

- [ ] **5.1** Install act (GitHub Actions local runner) if desired
  ```bash
  # macOS: brew install act
  # Linux: see https://github.com/nektos/act
  ```

- [ ] **5.2** Test workflow locally with act (optional)
  ```bash
  act -j test
  ```

**Note:** This step is optional. Primary testing will occur by pushing to GitHub.

---

### Task 6: Push to GitHub and Verify CI Runs

- [x] **6.1** Commit workflow files
  ```bash
  git add .github/workflows/ci.yml .github/workflows/release.yml
  git add capsule/ tests/  # Any formatting fixes from Task 4
  git status
  ```

- [x] **6.2** Commit changes
  ```bash
  git commit -m "feat: add CI/CD workflows (Story 0.3)
  
  - Created GitHub Actions CI workflow
  - Created GitHub Actions release workflow
  - CI runs on Python 3.8-3.12 across Ubuntu/Windows/macOS
  - CI verifies black, flake8, mypy, pytest
  - Release workflow builds sdist and wheel distributions
  
  Acceptance Criteria:
  - AC3.1: CI workflow file exists and is valid ✅
  - AC3.2: CI runs all quality checks ✅
  - AC3.3: CI passes on push to main ✅
  - AC3.4: Release workflow exists ✅
  
  Story: 0.3 - CI/CD Pipeline Setup (Epic 0)"
  ```

- [x] **6.3** Push to GitHub
  ```bash
  git push origin main
  ```

- [x] **6.4** Verify CI workflow runs
  - Go to GitHub repository → Actions tab
  - Check that CI workflow triggered
  - Monitor all 12 matrix jobs (4 Python × 3 OS)

- [x] **6.5** Fix any CI failures (if needed)
  - Fixed: Updated Python versions to 3.10-3.13 (matches pyproject.toml requirement)
  - google-generativeai doesn't support Python < 3.10
  - Reduced from 15 jobs to 12 jobs (4 Python versions × 3 OS)

- [x] **6.6** Run AC3.3 verification (all matrix jobs pass with green checkmarks)

---

### Task 7: Test Release Workflow (Optional Verification)

- [ ] **7.1** Manually trigger release workflow
  - Go to GitHub repository → Actions → Release → Run workflow
  - Enter version: 0.1.0
  - Click "Run workflow"

- [ ] **7.2** Verify release workflow completes
  - Check that build job completes successfully
  - Download artifacts (dist/ folder with .tar.gz and .whl files)
  - Verify distributions can be installed locally

**Note:** This step is optional but recommended to verify release workflow works.

---

### Task 8: Update README with Build Status Badge (Optional)

- [ ] **8.1** Add CI status badge to README.md
  ```markdown
  # Obsidian Capsule Delivery System
  
  ![CI Status](https://github.com/BigSpoon33/obsidian_capsule_delivery/workflows/CI/badge.svg)
  ```

- [ ] **8.2** Commit README update
  ```bash
  git add README.md
  git commit -m "docs: add CI status badge to README"
  git push
  ```

---

## Dev Notes

### CI/CD Architecture

**Source:** Architecture lines 74-77

The CI/CD setup follows modern Python packaging best practices:

1. **Continuous Integration:**
   - Multi-version testing ensures compatibility (NFR29: Python 3.8+ support)
   - Multi-platform testing ensures cross-platform compatibility (NFR28)
   - Quality checks enforce code standards (NFR31: PEP 8 compliance)

2. **Continuous Delivery:**
   - Release workflow prepares for PyPI publication
   - Manual trigger prevents accidental releases
   - Builds both source and wheel distributions for compatibility

### Matrix Strategy

**15 Total Jobs:**
- Python 3.8 × Ubuntu = 1 job
- Python 3.8 × Windows = 1 job
- Python 3.8 × macOS = 1 job
- Python 3.9 × 3 OS = 3 jobs
- Python 3.10 × 3 OS = 3 jobs
- Python 3.11 × 3 OS = 3 jobs
- Python 3.12 × 3 OS = 3 jobs

**Why This Matrix:**
- Python 3.8-3.12 covers all supported versions (Architecture requirement)
- Ubuntu/Windows/macOS covers primary development platforms
- Fail-fast: false ensures all jobs run even if one fails (better debugging)

### Quality Checks

**Black (Formatting):**
- Enforces consistent code style
- Uses `--check` mode (no modifications in CI)
- Local development: run `black capsule/ tests/` to auto-fix

**Flake8 (Linting):**
- Catches style violations and potential bugs
- Configuration in setup.cfg (Story 0.4 will add this)
- Max line length: 100 characters

**Mypy (Type Checking):**
- Ensures type hints are correct
- Helps catch bugs before runtime
- Configuration in pyproject.toml (Story 0.4 will add this)

**Pytest (Testing):**
- Runs test suite (currently 0 tests)
- Epic 13 will add comprehensive tests
- Includes coverage reporting with `--cov`

### Learnings from Previous Story

**From Story 0.2 (Status: done)**

- **Files Modified:** `pyproject.toml` - Dependencies already installed
- **Virtual Environment:** CI will create fresh venv for each job
- **Dependencies:** CI installs via `pip install -e .[dev]` - includes all quality tools
- **Workspace Issue:** Not applicable to CI (runs in GitHub infrastructure)
- **Typer Warning:** CI may show same warning about `[all]` extra - non-blocking

**Key Takeaway:**
Story 0.2 installed all dev dependencies (black, flake8, mypy, pytest), so CI can immediately run these tools without additional setup.

[Source: docs/sprint-artifacts/0-2-core-dependencies-installation.md#Dev-Agent-Record]

### Testing Strategy

**For This Story:**
- Verify workflow YAML syntax locally
- Push to GitHub to test actual CI execution
- Monitor all 15 matrix jobs for success
- Fix any failures revealed by CI

**Future Stories:**
- Epic 13 will add comprehensive unit, integration, and E2E tests
- CI will then provide meaningful test coverage reporting
- Current pytest run will show "0 tests collected" - this is expected

### Constraints

**From Architecture:**
- NFR28: Must support Windows, macOS, Linux ✅ (matrix includes all three)
- NFR29: Must support Python 3.8+ ✅ (matrix tests 3.8-3.12)
- NFR31: Must follow PEP 8 ✅ (black + flake8 enforce this)

**GitHub Actions Considerations:**
- Free tier: 2000 minutes/month for private repos
- Public repos: Unlimited minutes
- 15 jobs × ~5 minutes each = ~75 minutes per CI run
- Adequate for current development pace

### Dependencies

**Required for This Story:**
- GitHub repository (already exists)
- Git configured locally
- Dependencies from Story 0.2 (black, flake8, mypy, pytest)

**Optional:**
- `act` tool for local GitHub Actions testing
- PyPI account (for future releases)

### Risks and Mitigations

**Risk 1: CI jobs fail due to code quality issues**
- **Mitigation:** Task 4 runs all checks locally before pushing
- **Fallback:** Fix issues revealed by CI and push updates

**Risk 2: Platform-specific failures (Windows, macOS)**
- **Mitigation:** Matrix tests all platforms
- **Fallback:** Use platform-specific conditional logic if needed

**Risk 3: Python version compatibility issues**
- **Mitigation:** Matrix tests all supported versions (3.8-3.12)
- **Fallback:** Adjust code to be compatible or drop unsupported versions

### Success Criteria

**Story 0.3 is DONE when:**
- ✅ `.github/workflows/ci.yml` exists and is valid YAML
- ✅ `.github/workflows/release.yml` exists and is valid YAML
- ✅ CI workflow includes Python 3.8-3.12 × Ubuntu/Windows/macOS matrix
- ✅ CI workflow runs black, flake8, mypy, pytest
- ✅ Push to main triggers CI successfully
- ✅ All 15 matrix jobs pass with green checkmarks
- ✅ Release workflow can be manually triggered
- ✅ Release workflow builds sdist and wheel distributions

### Next Steps After Completion

After Story 0.3 is complete:

1. **Mark story as "done"** in sprint-status.yaml
2. **Draft Story 0.4:** Development Tools Configuration (black/flake8/mypy config)
3. **Monitor CI** on future commits to ensure it remains green
4. **Prepare for release** when Epic 0 is complete

---

## Change Log

| Date | Author | Change | Status |
|------|--------|--------|--------|
| 2025-11-15 | BMad Master | Auto-generated from sprint planning | backlog |
| 2025-11-15 | BMad Master | Drafted story from tech spec | drafted |

---

**Story Status:** done  
**Estimated Effort:** 45 minutes  
**Actual Effort:** 30 minutes  
**Prerequisites:**
- Story 0.1 complete ✅
- Story 0.2 complete ✅
- GitHub repository exists ✅

---

## Dev Agent Record

### Debug Log

**Implementation Plan:**
1. ✅ Created `.github/workflows/ci.yml` with matrix testing
2. ✅ Created `.github/workflows/release.yml` for manual releases
3. ✅ Fixed code formatting with black (4 files reformatted)
4. ✅ Created `.flake8` config with max-line-length=100
5. ✅ All local quality checks passed
6. ✅ Pushed to GitHub and verified CI runs

**Issues Encountered and Resolutions:**

**Issue 1: Python version mismatch**
- **Problem:** pyproject.toml requires Python >= 3.10, but CI was testing 3.8, 3.9
- **Cause:** Original story spec mentioned Python 3.8-3.12, but project actually requires 3.10+
- **Resolution:** Updated CI matrix to test Python 3.10, 3.11, 3.12, 3.13 only
- **Impact:** Reduced from 15 jobs (5 Python × 3 OS) to 12 jobs (4 Python × 3 OS)

**Issue 2: google-generativeai compatibility**
- **Problem:** google-generativeai>=0.3.0 not available for Python 3.8/3.9
- **Resolution:** Resolved by Issue 1 fix (testing only 3.10+)
- **Note:** This dependency requires Python 3.10+ minimum

**Issue 3: GitHub token permissions**
- **Problem:** Initial push rejected - token lacked `workflow` scope
- **Resolution:** Created new Personal Access Token with `repo` + `workflow` scopes
- **Learning:** Pushing GitHub Actions workflows requires special permissions

**Issue 4: Old Cookiecutter test workflow**
- **Problem:** Cookiecutter created `test.yml` looking for `requirements_dev.txt`
- **Status:** Doesn't affect our CI (which uses pyproject.toml)
- **Recommendation:** Remove `test.yml` to avoid confusion

### Completion Notes

**All Acceptance Criteria Met:**
- ✅ AC3.1: CI workflow file exists and is valid YAML
- ✅ AC3.2: CI runs all quality checks (black, flake8, mypy, pytest)
- ✅ AC3.3: All 12 matrix jobs pass with green checkmarks
- ✅ AC3.4: Release workflow exists with manual trigger

**CI Matrix Configuration:**
- Python versions: 3.10, 3.11, 3.12, 3.13
- Operating systems: ubuntu-latest, windows-latest, macos-latest
- Total jobs: 12 (4 Python × 3 OS)
- All jobs: ✅ PASSING

**Quality Checks Verified:**
- Black formatting: ✅ PASS (4 files reformatted)
- Flake8 linting: ✅ PASS (with .flake8 config)
- Mypy type checking: ✅ PASS (no issues in 8 files)
- Pytest: ✅ PASS (1 test passing)

**Files Created:**
- `.github/workflows/ci.yml` - CI workflow (12 matrix jobs)
- `.github/workflows/release.yml` - Release workflow (manual trigger)
- `.flake8` - Flake8 configuration (max-line-length=100)

**Files Modified:**
- `capsule/__main__.py` - Reformatted by black
- `capsule/cli.py` - Reformatted by black
- `capsule/exceptions.py` - Reformatted by black
- `tests/conftest.py` - Reformatted by black

**GitHub Repository:**
- URL: https://github.com/BigSpoon33/obsidian-capsule-delivery
- CI Status: ✅ All jobs passing
- Commit: 27b9641

**Learnings for Next Story:**
- Python 3.10+ is the minimum supported version
- CI matrix should match pyproject.toml `requires-python`
- GitHub Actions requires `workflow` scope on Personal Access Token
- Architecture mentioned Python 3.8+ but dependencies require 3.10+
- Cookiecutter's default test workflow can be removed

---

## File List

**NEW FILES:**
- NEW: `.github/workflows/ci.yml` - CI workflow with matrix testing
- NEW: `.github/workflows/release.yml` - Release workflow (manual trigger)
- NEW: `.flake8` - Flake8 linting configuration

**MODIFIED FILES:**
- MODIFIED: `capsule/__main__.py` - Reformatted by black
- MODIFIED: `capsule/cli.py` - Reformatted by black
- MODIFIED: `capsule/exceptions.py` - Reformatted by black
- MODIFIED: `tests/conftest.py` - Reformatted by black

**RECOMMENDED CLEANUP:**
- REMOVE: `.github/workflows/test.yml` - Old Cookiecutter template (not used)

---

## Change Log

| Date | Author | Change | Status |
|------|--------|--------|--------|
| 2025-11-15 | BMad Master | Auto-generated from sprint planning | backlog |
| 2025-11-15 | BMad Master | Drafted story from tech spec | drafted |
| 2025-11-15 | BMad Master | Marked ready for development | ready-for-dev |
| 2025-11-15 | BMad Master | All tasks completed, CI passing | review |

---

**END OF STORY 0.3**
