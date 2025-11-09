# OCDS Python Code Style Guide

**Purpose:** Coding standards and best practices for OCDS automation scripts

**Last Updated:** 2025-11-06  
**OCDS Version:** 1.0.0

---

## 📋 Overview

This guide defines the coding standards for all OCDS Python scripts. Following these standards ensures consistency, maintainability, and reliability across the codebase.

---

## 🎯 Core Principles

1. **Readability** - Code is read more than written
2. **Consistency** - Follow established patterns
3. **Simplicity** - Simple solutions over clever ones
4. **Documentation** - Document intent, not implementation
5. **Testing** - Write tests for critical functions

---

## 📝 Code Formatting

### PEP 8 Compliance

Follow [PEP 8](https://pep8.org/) with these specifics:

**Line Length:**
- Maximum 100 characters (not 79)
- Break long lines logically

**Indentation:**
- 4 spaces (no tabs)
- Continuation lines: align or indent 4 spaces

**Blank Lines:**
- 2 blank lines between top-level functions/classes
- 1 blank line between methods
- Use blank lines sparingly within functions

**Imports:**
```python
# Standard library
import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

# Third-party
import yaml
import click
from jinja2 import Template

# Local
from utils.frontmatter_parser import parse_frontmatter
from utils.yaml_loader import load_yaml
```

---

## 🏗️ Naming Conventions

### Functions and Variables

```python
# Functions: snake_case
def calculate_final_grade(scores: List[float]) -> float:
    pass

# Variables: snake_case
student_id = "john_doe"
quiz_score = 85.5
total_points = 100

# Constants: UPPER_CASE
MAX_ATTEMPTS = 3
DEFAULT_TIMEOUT = 30
PASSING_SCORE = 70
```

### Classes

```python
# Classes: PascalCase
class MaterialGenerator:
    pass

class QuizGrader:
    pass

class UnlockManager:
    pass
```

### Private Members

```python
# Private: _leading_underscore
def _parse_response(response: str) -> Dict[str, Any]:
    pass

class GradeCalculator:
    def __init__(self):
        self._cache = {}
    
    def _validate_input(self, data: Any) -> bool:
        pass
```

---

## 📖 Documentation

### Docstrings (Google Style)

```python
def grade_quiz(quiz_file: Path, answer_key: Dict[str, str]) -> float:
    """
    Grade a multiple choice quiz against an answer key.
    
    Args:
        quiz_file (Path): Path to quiz markdown file
        answer_key (Dict[str, str]): Mapping of question IDs to correct answers
    
    Returns:
        float: Score as percentage (0-100)
    
    Raises:
        FileNotFoundError: If quiz file doesn't exist
        ValueError: If answer key is invalid
    
    Example:
        >>> grade_quiz(Path('quiz.md'), {'q1': 'A', 'q2': 'B'})
        85.0
    """
    if not quiz_file.exists():
        raise FileNotFoundError(f"Quiz not found: {quiz_file}")
    
    # Implementation...
    return score
```

### Comments

```python
# Good: Explain WHY, not WHAT
# Calculate weighted average to account for different point values
weighted_avg = sum(score * weight for score, weight in zip(scores, weights))

# Bad: Obvious comment
# Loop through scores
for score in scores:
    pass
```

---

## 🔧 Type Hints

Use type hints for all function signatures:

```python
from typing import List, Dict, Any, Optional, Tuple

def process_materials(
    class_id: str,
    weeks: List[int],
    force: bool = False
) -> Dict[str, Any]:
    """Process materials for specified weeks."""
    pass

def get_student_progress(
    class_id: str,
    student_id: str
) -> Optional[Dict[str, Any]]:
    """Get student progress, or None if not found."""
    pass

def calculate_scores(
    quizzes: List[float],
    homework: List[float]
) -> Tuple[float, float]:
    """Calculate quiz and homework averages."""
    return (sum(quizzes) / len(quizzes), sum(homework) / len(homework))
```

---

## ⚠️ Error Handling

### Specific Exceptions

```python
# Good: Specific exceptions
try:
    data = load_yaml(config_file)
except FileNotFoundError:
    logger.error(f"Config file not found: {config_file}")
    raise
except yaml.YAMLError as e:
    logger.error(f"Invalid YAML syntax: {e}")
    raise ValueError(f"Cannot parse {config_file}")

# Bad: Bare except
try:
    data = load_yaml(config_file)
except:
    pass  # Silent failure!
```

### Validation

```python
def calculate_grade(scores: List[float], weights: List[float]) -> float:
    """Calculate weighted grade."""
    
    # Validate inputs
    if not scores:
        raise ValueError("Scores list cannot be empty")
    
    if len(scores) != len(weights):
        raise ValueError("Scores and weights must have same length")
    
    if not all(0 <= s <= 100 for s in scores):
        raise ValueError("Scores must be between 0 and 100")
    
    if abs(sum(weights) - 1.0) > 0.01:
        raise ValueError("Weights must sum to 1.0")
    
    # Calculate
    return sum(s * w for s, w in zip(scores, weights))
```

---

## 📊 Logging

Use Python's logging module:

```python
import logging

logger = logging.getLogger(__name__)

def import_class(package: str):
    """Import a class package."""
    
    logger.info(f"Importing class from {package}")
    
    try:
        extract_package(package)
        logger.debug("Package extracted successfully")
    except Exception as e:
        logger.error(f"Failed to extract package: {e}")
        raise
    
    logger.info("Class import complete")
```

**Log Levels:**
- `DEBUG`: Detailed diagnostic info
- `INFO`: General informational messages
- `WARNING`: Warning messages
- `ERROR`: Error messages
- `CRITICAL`: Critical errors

---

## 🧪 Testing

### Unit Tests

```python
import pytest
from pathlib import Path
from grading import calculate_final_grade

def test_calculate_final_grade_basic():
    """Test basic grade calculation."""
    scores = {'quizzes': 90, 'homework': 85, 'tasks': 95}
    weights = {'quizzes': 0.5, 'homework': 0.3, 'tasks': 0.2}
    
    result = calculate_final_grade(scores, weights)
    
    assert result == 89.5

def test_calculate_final_grade_empty_scores():
    """Test that empty scores raises ValueError."""
    with pytest.raises(ValueError):
        calculate_final_grade({}, {})

def test_calculate_final_grade_invalid_weights():
    """Test that invalid weights raises ValueError."""
    scores = {'quizzes': 90}
    weights = {'quizzes': 0.5}  # Doesn't sum to 1.0
    
    with pytest.raises(ValueError):
        calculate_final_grade(scores, weights)
```

---

## 🎯 Best Practices

### File Operations

```python
from pathlib import Path

# Good: Use Path objects
def read_file(file_path: Path) -> str:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return file_path.read_text(encoding='utf-8')

# Good: Context managers
def write_file(file_path: Path, content: str) -> None:
    with file_path.open('w', encoding='utf-8') as f:
        f.write(content)
```

### YAML Handling

```python
import yaml
from pathlib import Path

def load_yaml(file_path: Path) -> Dict[str, Any]:
    """Load YAML file safely."""
    with file_path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def save_yaml(file_path: Path, data: Dict[str, Any]) -> None:
    """Save data to YAML file."""
    with file_path.open('w', encoding='utf-8') as f:
        yaml.safe_dump(data, f, default_flow_style=False, allow_unicode=True)
```

### CLI with Click

```python
import click

@click.command()
@click.option('--class-id', required=True, help='Class identifier')
@click.option('--student-id', required=True, help='Student identifier')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
def grade_student(class_id: str, student_id: str, verbose: bool):
    """Grade all materials for a student."""
    
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    
    # Implementation...
```

---

## ✅ Checklist

### Before Committing Code

- [ ] Code follows PEP 8 (run `flake8`)
- [ ] All functions have docstrings
- [ ] Type hints on all function signatures
- [ ] Error handling in place
- [ ] Logging statements added
- [ ] Unit tests written
- [ ] Tests pass (`pytest`)
- [ ] No hardcoded paths
- [ ] No sensitive data in code

---

## 🔗 Tools

### Linting

```bash
# Install tools
pip install flake8 black mypy

# Check style
flake8 scripts/

# Auto-format
black scripts/

# Type checking
mypy scripts/
```

### Configuration

**.flake8:**
```ini
[flake8]
max-line-length = 100
exclude = .git,__pycache__,venv
ignore = E203,W503
```

**pyproject.toml:**
```toml
[tool.black]
line-length = 100
target-version = ['py39']

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
```

---

**Consistent code is maintainable code. Follow the guide!**

---

*Last updated: 2025-11-06*  
*OCDS Version: 1.0.0*
