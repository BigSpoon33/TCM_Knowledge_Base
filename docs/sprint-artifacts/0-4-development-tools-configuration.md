# Story 0.4: Development Tools Configuration

**Epic:** Epic 0 - Foundation & Project Setup  
**Status:** backlog  
**Story ID:** 0.4  
**Story Key:** 0-4-development-tools-configuration

---

## Story

**As a** developer building the Obsidian Capsule Delivery System,  
**I want** properly configured development tools (black, flake8, mypy) in configuration files,  
**so that** code quality standards are enforced consistently and the CI passes reliably.

---

## Context

This story configures the development tools that were installed in Story 0.2 and tested in Story 0.3. It adds proper configuration sections to `pyproject.toml` and ensures all quality checks pass.

**Key Configuration:**
- **Black:** Code formatter (consistent style)
- **Flake8:** Style linter (PEP 8 compliance)  
- **Mypy:** Type checker (catch type errors)

**Prerequisites:**
- ✅ Story 0.1 complete (project structure exists)
- ✅ Story 0.2 complete (dev tools installed)
- ✅ Story 0.3 complete (CI workflow configured)

**Source:** Tech Spec Epic 0 AC4.1-AC4.5

---

## Acceptance Criteria

### AC4.1: Black Formatter is Configured and Passes

**Verification:**
```bash
# Check configuration exists
grep -A 5 "\[tool.black\]" pyproject.toml

# Run black check
black --check capsule/ tests/
echo $?  # Should be 0 (no changes needed)
```

**Required configuration in `pyproject.toml`:**
```toml
[tool.black]
line-length = 100
target-version = ['py310', 'py311', 'py312', 'py313']
include = '\.pyi?$'
```

**Note:** We already ran `black capsule/ tests/` in Story 0.3, so files are formatted.

---

### AC4.2: Flake8 Linter is Configured and Passes

**Verification:**
```bash
# Check configuration exists (already created in Story 0.3)
cat .flake8

# Run flake8 check
flake8 capsule/ tests/
echo $?  # Should be 0 (no violations)
```

**Required configuration in `.flake8`:**
```ini
[flake8]
max-line-length = 100
exclude = .git,__pycache__,build,dist,.eggs,.venv
```

**Status:** ✅ Already configured in Story 0.3

---

### AC4.3: Mypy Type Checker is Configured and Passes

**Verification:**
```bash
# Check configuration exists
grep -A 10 "\[tool.mypy\]" pyproject.toml

# Run mypy check
mypy capsule/
echo $?  # Should be 0 (no type errors)
```

**Required configuration in `pyproject.toml`:**
```toml
[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

---

### AC4.4: CLI Version Command Works

**Verification:**
```bash
python -m capsule --version
# Expected output: "Obsidian Capsule CLI v0.1.0"

# Check exit code
python -m capsule --version && echo "✓ Exit code 0"
```

**Status:** ✅ Already working from Story 0.1

---

### AC4.5: Help Command Works

**Verification:**
```bash
python -m capsule --help
# Expected: Shows usage information with "Obsidian Capsule Delivery System"

# Verify key elements present
python -m capsule --help | grep -i "obsidian"
python -m capsule --help | grep -i "version"
```

**Status:** ✅ Already working from Story 0.1

---

## Tasks / Subtasks

### Task 1: Configure Black Formatter in pyproject.toml

- [ ] **1.1** Add `[tool.black]` section to pyproject.toml

**Add this to `pyproject.toml`:**
```toml
[tool.black]
line-length = 100
target-version = ['py310', 'py311', 'py312', 'py313']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.venv
  | build
  | dist
  | \.eggs
)/
'''
```

- [ ] **1.2** Verify black configuration works
  ```bash
  black --check capsule/ tests/
  ```

- [ ] **1.3** Run AC4.1 verification (configuration exists and passes)

---

### Task 2: Verify Flake8 Configuration

- [ ] **2.1** Confirm `.flake8` file exists (created in Story 0.3)
  ```bash
  cat .flake8
  ```

- [ ] **2.2** Verify flake8 passes
  ```bash
  flake8 capsule/ tests/
  ```

- [ ] **2.3** Run AC4.2 verification (no violations)

**Status:** This task should be quick - configuration already exists!

---

### Task 3: Configure Mypy Type Checker in pyproject.toml

- [ ] **3.1** Add `[tool.mypy]` section to pyproject.toml

**Add this to `pyproject.toml`:**
```toml
[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
exclude = [
    "^build/",
    "^dist/",
]
```

- [ ] **3.2** Run mypy and check for errors
  ```bash
  mypy capsule/
  ```

- [ ] **3.3** Fix any type errors revealed by stricter settings

**Expected:** Should already pass (Story 0.3 verified mypy works)

- [ ] **3.4** Run AC4.3 verification (configuration exists and passes)

---

### Task 4: Verify CLI Commands Work

- [ ] **4.1** Test version command
  ```bash
  python -m capsule --version
  # Expected: "Obsidian Capsule CLI v0.1.0"
  ```

- [ ] **4.2** Test help command
  ```bash
  python -m capsule --help
  # Expected: Shows usage with description
  ```

- [ ] **4.3** Verify exit codes are correct
  ```bash
  python -m capsule --version && echo "✓ Version exit code 0"
  python -m capsule --help && echo "✓ Help exit code 0"
  ```

- [ ] **4.4** Run AC4.4 and AC4.5 verification

**Status:** Should already work from Story 0.1!

---

### Task 5: Run All Quality Checks Together

- [ ] **5.1** Run comprehensive quality check
  ```bash
  black --check capsule/ tests/ && \
  flake8 capsule/ tests/ && \
  mypy capsule/ && \
  pytest && \
  echo "✅ All quality checks PASSED"
  ```

- [ ] **5.2** Verify CI will pass with new configurations
  - All checks should pass locally
  - CI uses same commands, so should pass on GitHub too

---

### Task 6: Add Pre-commit Hooks (Optional but Recommended)

- [ ] **6.1** Create `.pre-commit-config.yaml` (optional)

**File:** `.pre-commit-config.yaml`
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.10.0
    hooks:
      - id: black
        language_version: python3.10

  - repo: https://github.com/pycqa/flake8
    rev: 7.1.1
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.13.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

- [ ] **6.2** Install pre-commit hooks (optional)
  ```bash
  pip install pre-commit
  pre-commit install
  ```

- [ ] **6.3** Test pre-commit hooks
  ```bash
  pre-commit run --all-files
  ```

**Note:** This task is optional. Pre-commit hooks run quality checks before each commit.

---

### Task 7: Update Documentation

- [ ] **7.1** Add development section to README.md (optional)

**Add to README.md:**
```markdown
## Development

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/BigSpoon33/obsidian-capsule-delivery.git
   cd obsidian-capsule-delivery
   ```

2. Create virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv/bin/activate.fish for fish shell
   ```

3. Install in editable mode with dev dependencies:
   ```bash
   pip install -e .[dev]
   ```

### Code Quality

Run all quality checks before committing:

```bash
black --check capsule/ tests/  # Code formatting
flake8 capsule/ tests/          # Linting
mypy capsule/                   # Type checking
pytest                          # Tests
```

Or use pre-commit hooks (optional):
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```
```

- [ ] **7.2** Commit README updates (optional)

---

### Task 8: Commit Configuration Changes

- [ ] **8.1** Check what will be committed
  ```bash
  git status
  git diff pyproject.toml
  ```

- [ ] **8.2** Add updated files
  ```bash
  git add pyproject.toml
  # If pre-commit was added:
  git add .pre-commit-config.yaml
  # If README was updated:
  git add README.md
  ```

- [ ] **8.3** Commit configuration
  ```bash
  git commit -m "feat: configure development tools (Story 0.4)

  - Added Black formatter configuration to pyproject.toml
  - Added Mypy type checker configuration to pyproject.toml
  - Flake8 already configured in .flake8 (Story 0.3)
  - All quality checks passing (black, flake8, mypy, pytest)
  - Optional: Added pre-commit hooks configuration
  - Optional: Updated README with development instructions
  
  Acceptance Criteria:
  - AC4.1: Black configured and passing ✅
  - AC4.2: Flake8 configured and passing ✅
  - AC4.3: Mypy configured and passing ✅
  - AC4.4: CLI version command works ✅
  - AC4.5: CLI help command works ✅
  
  Story: 0.4 - Development Tools Configuration (Epic 0)"
  ```

- [ ] **8.4** Push to GitHub
  ```bash
  git push origin main
  ```

- [ ] **8.5** Verify CI passes with new configurations
  - Check GitHub Actions tab
  - All jobs should remain green

---

## Dev Notes

### Tool Configuration Philosophy

**Black (Formatter):**
- Line length: 100 characters (matches architecture specification)
- Target versions: Python 3.10-3.13 (matches CI matrix)
- Opinionated formatter - no style debates needed
- "Any color you want, as long as it's black"

**Flake8 (Linter):**
- Max line length: 100 (consistent with Black)
- Excludes: virtual environments, build artifacts
- Catches style violations and potential bugs
- Complements Black (Black formats, Flake8 finds issues)

**Mypy (Type Checker):**
- Python version: 3.10 (minimum supported)
- Strict settings: `disallow_untyped_defs = true`
- Catches type errors before runtime
- Improves code documentation and IDE support

### Configuration File Locations

**pyproject.toml:**
- Black configuration: `[tool.black]`
- Mypy configuration: `[tool.mypy]`
- Modern Python standard (PEP 518)
- Single source of truth

**.flake8:**
- Flake8 configuration: `[flake8]`
- Already created in Story 0.3
- Separate file because flake8 doesn't support pyproject.toml yet

### Learnings from Previous Story

**From Story 0.3 (Status: done)**

- **Files Already Formatted:** Black ran in Story 0.3, reformatted 4 files
- **Flake8 Config Exists:** `.flake8` created with max-line-length=100
- **Mypy Already Passing:** No type errors in 8 files
- **CI Already Testing:** All quality checks run in GitHub Actions
- **Python Versions:** 3.10-3.13 (not 3.8-3.12 as originally planned)

**Key Takeaway:**
Most of the work is already done! Story 0.4 just adds proper configuration sections so settings are documented and consistent.

[Source: docs/sprint-artifacts/0-3-ci-cd-pipeline-setup.md#Dev-Agent-Record]

### Why This Story Matters

Even though tools are working, proper configuration:
1. **Documents standards** - New developers know the rules
2. **Ensures consistency** - Settings don't drift over time
3. **Enables customization** - Easy to adjust if needed
4. **Supports tooling** - IDEs can read configurations
5. **Makes CI reliable** - No surprises between local and CI

### Testing Strategy

**For This Story:**
- Verify configuration files have correct sections
- Run all quality checks locally
- Ensure CI continues to pass
- No new tests needed (tools already tested in Story 0.3)

**Future Stories:**
- Epic 13 will add comprehensive test suite
- Quality tools will catch issues in new code
- Pre-commit hooks (if added) run before each commit

### Optional Enhancements

**Pre-commit Hooks:**
- Run quality checks automatically before commits
- Prevent bad code from being committed
- Requires `pip install pre-commit`
- Recommended but not required for this story

**README Documentation:**
- Helps new contributors get started
- Documents development workflow
- Shows how to run quality checks
- Recommended but not required for this story

### Success Criteria

**Story 0.4 is DONE when:**
- ✅ `pyproject.toml` contains `[tool.black]` section
- ✅ `pyproject.toml` contains `[tool.mypy]` section
- ✅ `.flake8` exists with correct configuration
- ✅ `black --check capsule/ tests/` exits 0
- ✅ `flake8 capsule/ tests/` exits 0
- ✅ `mypy capsule/` exits 0
- ✅ `python -m capsule --version` works
- ✅ `python -m capsule --help` works
- ✅ CI passes on GitHub

### Next Steps After Completion

After Story 0.4 is complete:

1. **Mark story as "done"** in sprint-status.yaml
2. **Epic 0 is COMPLETE!** 🎉
3. **Run epic retrospective** (optional)
4. **Begin Epic 1:** Core Data Models
5. **Celebrate!** Foundation is solid!

---

## Change Log

| Date | Author | Change | Status |
|------|--------|--------|--------|
| 2025-11-15 | BMad Master | Auto-generated from sprint planning | backlog |
| 2025-11-15 | BMad Master | Drafted story from tech spec | drafted |

---

**Story Status:** done  
**Estimated Effort:** 20 minutes  
**Prerequisites:**
- Story 0.1 complete ✅
- Story 0.2 complete ✅
- Story 0.3 complete ✅

---

**END OF STORY 0.4**
