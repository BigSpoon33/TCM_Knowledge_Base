# End-to-End (E2E) Tests

This directory contains end-to-end tests that verify complete capsule workflows by combining multiple CLI commands.

## Test Coverage

### Happy Path Tests (`test_workflow_happy_path.py`)
- **test_complete_workflow_validate_export_import**: Full lifecycle test (Validate → Export → Import)
- **test_workflow_export_folder_format**: Export to folder bundle instead of zip
- **test_workflow_import_dry_run**: Import dry-run mode verification
- **test_workflow_validate_before_export**: Typical workflow validation before export
- **test_workflow_import_with_backup**: Backup creation during import

### Error Handling Tests (`test_workflow_errors.py`)
- **test_import_invalid_capsule_missing_cypher**: Import capsule without cypher file
- **test_import_capsule_corrupted_yaml**: Import capsule with corrupted YAML
- **test_import_zip_file_not_found**: Import non-existent zip file
- **test_export_nonexistent_capsule**: Export non-existent capsule
- **test_validate_nonexistent_path**: Validate non-existent path
- **test_export_capsule_missing_files_in_inventory**: Export capsule with missing files

## Running E2E Tests

### Run all E2E tests
```bash
pytest tests/e2e/ -v
```

### Run only E2E marked tests (includes tests in other directories)
```bash
pytest -m e2e -v
```

### Run a specific E2E test
```bash
pytest tests/e2e/test_workflow_happy_path.py::test_complete_workflow_validate_export_import -v
```

### Run with detailed output
```bash
pytest tests/e2e/ -vvs
```

## Test Design

### Fixtures
- **temp_workspace**: Creates isolated temp directories for vault1, vault2, exports, config
- **config_file**: Creates test configuration with all required settings
- **sample_capsule**: Creates a realistic capsule with root note, flashcards, and proper structure

### Key Characteristics
- **Isolated**: Each test runs in its own temporary directory
- **Deterministic**: Uses fixtures instead of `generate` command to avoid LLM API calls
- **Fast**: Tests complete in < 1 second each
- **Cleanup**: Automatic cleanup of temporary files
- **Marked**: All tests decorated with `@pytest.mark.e2e`

## Test Patterns

### Happy Path Pattern
1. Create sample capsule (via fixture)
2. Validate capsule structure
3. Export capsule (zip or folder)
4. Import capsule into second vault
5. Verify content integrity

### Error Handling Pattern
1. Create invalid/corrupted capsule
2. Attempt operation
3. Verify command fails with non-zero exit code
4. (Optionally) Verify error message content

## Adding New E2E Tests

When adding new E2E tests:

1. **Mark the test**: Add `@pytest.mark.e2e` decorator
2. **Use fixtures**: Reuse `temp_workspace`, `config_file`, `sample_capsule`
3. **Test full workflows**: Combine multiple commands
4. **Verify integrity**: Check both file existence and content
5. **Cleanup**: Tests automatically cleanup via fixtures

Example:
```python
@pytest.mark.e2e
def test_new_workflow(temp_workspace, config_file, sample_capsule):
    """Test description"""
    # Setup
    vault = temp_workspace["vault1"]
    
    # Execute commands
    result = runner.invoke(app, ["command", "args"])
    
    # Verify
    assert result.exit_code == 0
    assert expected_file.exists()
```

## Performance Notes

- E2E tests are slower than unit tests but still fast (< 1s each)
- Tests can be run in parallel with `pytest -n auto` (requires pytest-xdist)
- Total E2E suite runs in < 1 second on modern hardware

## CI/CD Integration

E2E tests are included in the main test suite but can be selectively run:

```bash
# Run all tests (including E2E)
pytest

# Run only E2E tests
pytest -m e2e

# Exclude E2E tests (for fast feedback loop)
pytest -m "not e2e"
```
