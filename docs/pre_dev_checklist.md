# Pre-Development Architectural Review Checklist

Before beginning implementation of a new story, please review the following checklist to ensure alignment with the project's architecture and standards.

## 1. Framework and Library Alignment

- [ ] **CLI Framework:** Is the implementation using `Typer` for all CLI commands? (Or is there a documented exception?)
- [ ] **Configuration:** Is the implementation using the project's established configuration system? (e.g., `config.py`)
- [ ] **Dependencies:** Are all new dependencies approved and added to `pyproject.toml`?

## 2. Code Style and Structure

- [ ] **Naming Conventions:** Do all new files, classes, functions, and variables follow the project's naming conventions (e.g., `snake_case` for files and functions, `PascalCase` for classes)?
- [ ] **Directory Structure:** Are new files being placed in the correct directories according to the established project structure? (e.g., `capsule/core` for business logic, `capsule/models` for data models)
- [ ] **Testing:** Is there a corresponding test file created in the `tests/` directory that mirrors the source file's location?

## 3. Data Models and Schemas

- [ ] **Data Models:** Are all new data structures implemented as Pydantic models in the `capsule/models` directory?
- [ ] **Schema Changes:** If the story involves changes to data schemas, has the impact on other parts of the system been considered?
