# Tests

This folder contains unit tests and integration tests for the project.

## Structure
Mirror the structure of your `src/` folder:
```
tests/
├── test_data_preprocessing.py
├── test_analysis.py
├── test_visualization.py
└── test_utils.py
```

## Running Tests
```bash
# Install pytest if not already installed
pip install pytest

# Run all tests
pytest

# Run tests with coverage
pytest --cov=src tests/
```

## Writing Tests
- Use pytest framework
- Name test files with `test_` prefix
- Name test functions with `test_` prefix
- Keep tests independent and isolated
- Use fixtures for common setup
