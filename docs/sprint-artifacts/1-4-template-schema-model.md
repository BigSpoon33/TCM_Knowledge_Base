# Story 1.4: Template Schema Model

**Epic:** Epic 1 - Core Data Models  
**Status:** ready-for-dev  
**Story ID:** 1.4  
**Story Key:** 1-4-template-schema-model

---

## Story

**As a** developer building the Obsidian Capsule Delivery System,  
**I want** a TemplateSchema data model that defines and validates frontmatter structures,  
**so that** capsules can enforce schema compliance for domain-specific note templates.

---

## Context

This story implements the `TemplateSchema` data model - the specification for frontmatter schemas used in capsule templates. The TemplateSchema model defines required/optional fields, field types, and domain-specific sections, enabling schema validation for notes (Epic 5) and template management (Epic 4).

**The TemplateSchema model represents:**
- Domain type identifier (e.g., "tcm", "education", "reference")
- Required fields list (must be present in all notes)
- Optional fields list (may be present in notes)
- Domain sections with field definitions (typed schema for domain data)
- Validation rules for type checking

**Prerequisites:**
- ✅ Story 1.1 complete (Capsule model exists)
- ✅ Story 1.2 complete (CapsuleCypher model exists)
- ✅ Story 1.3 complete (Note model exists)
- ✅ Python 3.10+ installed
- ✅ Development tools configured (black, flake8, mypy, pytest)

**Source:** Architecture lines 114-118 (models/template.py), Architecture Template Schema Format section

---

## Acceptance Criteria

### AC4.1: TemplateSchema Class Exists with Required Fields

**Verification:**
```python
from capsule.models.template import TemplateSchema

schema = TemplateSchema(
    domain_type="tcm",
    version="1.0.0",
    required_fields=["id", "name", "type", "created", "updated"],
    optional_fields=["tags", "aliases"],
    domain_sections={
        "herb_data": {
            "required": {
                "hanzi": "string",
                "pinyin": "string",
                "temperature": "string"
            },
            "optional": {
                "dosage": "string",
                "contraindications": "array"
            }
        }
    }
)

assert schema.domain_type == "tcm"
assert "id" in schema.required_fields
assert "herb_data" in schema.domain_sections
print("✓ AC4.1 PASS")
```

**Required fields:**
- `domain_type`: str (domain identifier like "tcm", "education")
- `version`: str (schema version following semver)
- `required_fields`: list[str] (universal fields required in all notes)
- `optional_fields`: list[str] (universal fields that may be present)
- `domain_sections`: dict[str, Any] (domain-specific frontmatter sections with field definitions)

---

### AC4.2: TemplateSchema Can Load from YAML File

**Verification:**
```python
from capsule.models.template import TemplateSchema
from pathlib import Path

# Given a YAML template file at capsule/templates/domains/tcm.yaml
schema = TemplateSchema.from_yaml_file("capsule/templates/domains/tcm.yaml")

assert schema.domain_type == "traditional_chinese_medicine"
assert "id" in schema.required_fields
assert "herb_data" in schema.domain_sections
print("✓ AC4.2 PASS")
```

**Requirements:**
- `TemplateSchema.from_yaml_file(filepath)` class method
- Uses ruamel.yaml for loading (preserves comments)
- Handles missing files with FileNotFoundError
- Validates required keys present in YAML

---

### AC4.3: TemplateSchema Can Save to YAML File

**Verification:**
```python
from capsule.models.template import TemplateSchema

schema = TemplateSchema(
    domain_type="education",
    version="1.0.0",
    required_fields=["id", "name", "topic"],
    optional_fields=["difficulty", "prerequisites"],
    domain_sections={}
)

schema.to_yaml_file("output_schema.yaml")

# Verify file written correctly
loaded = TemplateSchema.from_yaml_file("output_schema.yaml")
assert loaded.domain_type == "education"
print("✓ AC4.3 PASS")
```

**Requirements:**
- `to_yaml_file(filepath)` method
- Uses ruamel.yaml for writing (preserves formatting)
- Creates parent directories if needed
- UTF-8 encoding

---

### AC4.4: TemplateSchema Has Type Hints and Passes Mypy

**Verification:**
```bash
mypy capsule/models/template.py --strict
# Expected output: Success: no issues found
```

**Requirements:**
- All fields have explicit type annotations
- Methods have return type annotations
- dict[str, Any] for flexible domain_sections
- list[str] for required_fields and optional_fields
- Passes mypy --strict with zero errors

---

### AC4.5: TemplateSchema Has Full Test Coverage

**Verification:**
```bash
pytest tests/test_models/test_template.py -v --cov=capsule/models/template
# Expected: All tests pass, coverage >95%
```

**Required tests (minimum 10):**
1. Create TemplateSchema with all fields
2. Create TemplateSchema with minimal fields (empty domain_sections)
3. Load TemplateSchema from YAML file
4. Handle FileNotFoundError for missing YAML files
5. Save TemplateSchema to YAML file
6. Roundtrip test (file → TemplateSchema → file → TemplateSchema)
7. Modify required_fields and verify changes
8. Modify domain_sections and verify changes
9. to_dict() serialization
10. Validate domain_sections structure (nested dict)

---

## Tasks / Subtasks

### Task 1: Create TemplateSchema Dataclass Structure (AC: 4.1, 4.4)
- [ ] Create `capsule/models/template.py`
- [ ] Import necessary types: dataclass, Optional, Any, dict, list
- [ ] Define TemplateSchema dataclass with fields:
  - [ ] domain_type: str
  - [ ] version: str
  - [ ] required_fields: list[str]
  - [ ] optional_fields: list[str]
  - [ ] domain_sections: dict[str, Any]
- [ ] Add docstring with usage examples
- [ ] Run mypy to verify type hints

### Task 2: Implement YAML File Loading (AC: 4.2, 4.4)
- [ ] Import ruamel.yaml library (YAML with comment preservation)
- [ ] Add `from_yaml_file(filepath: str)` class method
  - [ ] Use ruamel.yaml.YAML() for loading
  - [ ] Read file with UTF-8 encoding
  - [ ] Extract domain_type, version, required_fields, optional_fields, domain_sections
  - [ ] Handle FileNotFoundError gracefully
  - [ ] Validate required keys present
- [ ] Add type hints to method signature
- [ ] Test with sample YAML file

### Task 3: Implement YAML File Writing (AC: 4.3, 4.4)
- [ ] Add `to_yaml_file(filepath: str)` method
  - [ ] Use ruamel.yaml.YAML() for dumping
  - [ ] Create parent directories if needed (pathlib.Path.mkdir)
  - [ ] Write to file with UTF-8 encoding
  - [ ] Preserve YAML formatting and structure
- [ ] Add type hints to method signature
- [ ] Test roundtrip (read → write → read)

### Task 4: Add Helper Methods (AC: 4.1, 4.4)
- [ ] Add `to_dict()` method for serialization
- [ ] Add `__repr__()` for debugging
- [ ] Add `validate_structure()` method (basic validation of domain_sections format)
- [ ] Add type hints to all methods

### Task 5: Write Comprehensive Tests (AC: 4.5)
- [ ] Create `tests/test_models/test_template.py`
- [ ] Import pytest, TemplateSchema class, and fixtures
- [ ] Write 10 required unit tests (see AC4.5)
- [ ] Create test fixtures (sample YAML template files)
- [ ] Run tests with coverage: `pytest --cov=capsule/models/template`
- [ ] Ensure >95% coverage

### Task 6: Update Package Exports (AC: 4.1)
- [ ] Add TemplateSchema to `capsule/models/__init__.py`
- [ ] Export: `from capsule.models.template import TemplateSchema`
- [ ] Verify import works: `from capsule.models import TemplateSchema`

### Task 7: Run Quality Checks and Commit (AC: 4.4, 4.5)
- [ ] Run black formatter: `black capsule/models/template.py tests/test_models/test_template.py`
- [ ] Run mypy: `mypy capsule/models/template.py --strict`
- [ ] Run all tests: `pytest tests/test_models/test_template.py -v`
- [ ] Git add and commit changes
- [ ] Update story status in sprint-status.yaml

---

## Dev Notes

### Architecture Patterns

**ruamel.yaml Library Usage:**
- Use `ruamel.yaml.YAML()` instance for loading/dumping
- Preserves comments and formatting (unlike PyYAML)
- Handles complex nested structures safely
- Source: [Architecture lines 56, Decision Table - ruamel.yaml for cypher handling]

**Data Model Pattern (from Stories 1.1, 1.2, 1.3):**
- Use `@dataclass` decorator
- Explicit type hints on all fields
- list[str] for field lists, dict[str, Any] for flexible structures
- Follow established patterns for consistency

**File Operations:**
- Use pathlib.Path for cross-platform paths
- Always use UTF-8 encoding for file operations
- Create parent directories with `Path.mkdir(parents=True, exist_ok=True)`
- Source: [Architecture lines 63, stdlib patterns]

**Schema Structure:**
- domain_sections uses nested dict structure
- Each section has "required" and "optional" sub-dicts
- Field types specified as strings ("string", "array", "number", "boolean")
- This structure enables validation in Epic 5

### Project Structure Notes

**File Locations:**
- Model: `capsule/models/template.py`
- Tests: `tests/test_models/test_template.py`
- Exports: `capsule/models/__init__.py`
- Sample templates: `capsule/templates/domains/*.yaml` (future stories)

**Expected Structure:**
```
capsule/models/template.py
└─ TemplateSchema dataclass
    ├─ domain_type: str
    ├─ version: str
    ├─ required_fields: list[str]
    ├─ optional_fields: list[str]
    ├─ domain_sections: dict[str, Any]
    ├─ from_yaml_file(filepath) → TemplateSchema
    ├─ to_yaml_file(filepath) → None
    ├─ to_dict() → dict[str, Any]
    └─ validate_structure() → bool
```

### Testing Strategy

**Test Coverage (10 tests minimum):**
1. `test_template_schema_creation` - Create with all fields
2. `test_template_schema_minimal` - Create with empty domain_sections
3. `test_from_yaml_file` - Load from YAML file
4. `test_from_yaml_file_not_found` - Handle missing file
5. `test_to_yaml_file` - Write to YAML file
6. `test_roundtrip` - Read → Write → Read (verify identical)
7. `test_modify_required_fields` - Change field list and verify
8. `test_modify_domain_sections` - Change sections and verify
9. `test_to_dict` - Serialize to dictionary
10. `test_nested_domain_sections` - Validate complex nested structure

**Why This Coverage:**
- Tests all public methods (from_yaml_file, to_yaml_file, to_dict)
- Tests critical path: YAML I/O roundtrip
- Tests edge cases: missing files, empty sections
- Validates nested structure handling (domain_sections)
- ~100% code coverage expected

### Learnings from Previous Story (1.3)

**From Story 1-3-note-model-with-frontmatter (Status: done)**

**Established Patterns to Follow:**
- Dataclass with explicit type hints (list[str], dict[str, Any])
- from_file/to_file class method and instance method pattern
- Comprehensive test suite with 10+ tests (15 tests in Story 1.3)
- 100% quality compliance (Black, Mypy strict, Pytest)

**Key Files Created:**
- `capsule/models/note.py` - Note dataclass (206 lines)
- `tests/test_models/test_note.py` - 15 unit tests (277 lines)

**Quality Standards:**
- ✅ Black formatting required
- ✅ Mypy strict mode with zero errors
- ✅ 100% test coverage (15/15 tests passing in Story 1.3)
- ✅ All ACs verified with evidence

**Implementation Approach:**
- Follow Story 1.1/1.2/1.3 dataclass pattern for consistency
- Use ruamel.yaml instead of python-frontmatter (different lib for template schemas)
- Test roundtrip thoroughly (critical for file operations)
- Ensure UTF-8 encoding throughout
- Use similar from_yaml_file/to_yaml_file naming to from_file/to_file from Story 1.3

[Source: docs/sprint-artifacts/1-3-note-model-with-frontmatter.md#Senior-Developer-Review]

### References

**Architecture Citations:**
- Lines 56: YAML Cypher Handling decision (ruamel.yaml for template schemas)
- Lines 114-118: Template schema model specification (models/template.py)
- Template Schema Format section: YAML structure and field definitions

**PRD Citations:**
- Lines 154-158: Template system requirements (schema definitions, validation)

**Epic 1 Context:**
- Story 1.1: Capsule model pattern ✅
- Story 1.2: CapsuleCypher model pattern ✅ (uses ruamel.yaml - same lib for templates)
- Story 1.3: Note model pattern ✅ (use as template for structure)

---

## Change Log

| Date | Author | Change | Status |
|------|--------|--------|--------|
| 2025-11-16 | BMad Master | Drafted from architecture/PRD | drafted |

---

**Story Status:** drafted  
**Estimated Effort:** 50 minutes  
**Prerequisites:**
- Story 1.1 complete ✅
- Story 1.2 complete ✅
- Story 1.3 complete ✅
- Python 3.10+ installed ✅
- Development tools configured ✅
- ruamel.yaml dependency available ✅ (already installed in Story 1.2)

---

## Dev Agent Record

### Context Reference

- `docs/sprint-artifacts/1-4-template-schema-model.context.xml` (Generated: 2025-11-16)

### Agent Model Used

Claude 3.7 Sonnet (BMad Master Agent) - 2025-11-16

### Debug Log References

### Completion Notes List

### File List
