# Testing and Quality Assurance Rules

This document outlines comprehensive testing requirements and automation guidelines for the awesome-free project. These rules ensure high-quality, reliable code across Python tools, Bash scripts, and data validation processes. The guidelines are tailored to the project's focus on curating legitimate free services while maintaining robust validation and documentation generation capabilities.

## Testing Requirements

### Unit Testing
- Write unit tests for all new functions and classes in Python scripts
- Maintain minimum 80% test coverage for critical business logic (validation, link checking, data processing)
- Test edge cases and error conditions thoroughly
- Use descriptive test names that explain what is being tested
- Follow arrange-act-assert pattern in test structure

**Example Python unit test (using pytest):**
```python
import pytest
from tools.python.validate import validate_service_data

def test_validate_service_data_valid_input():
    """Test validation of valid service data."""
    valid_data = {
        "name": "Test Service",
        "category": "compute",
        "pricing": {"model": "free"}
    }
    errors = validate_service_data(valid_data)
    assert len(errors) == 0

def test_validate_service_data_missing_required_field():
    """Test validation fails for missing required fields."""
    invalid_data = {"name": "Test Service"}  # Missing category and pricing
    errors = validate_service_data(invalid_data)
    assert len(errors) > 0
    assert "category" in str(errors)
```

### Integration Testing
- Include integration tests for data processing pipelines (YAML/JSON loading, validation, export)
- Test external API interactions (link checking, freshness validation)
- Validate end-to-end data flow from input files to generated documentation
- Test file I/O operations and schema validation

**Example integration test:**
```python
import pytest
import tempfile
import os
from tools.python.validate import validate_services_directory
from tools.python.export_json import export_services_to_json

def test_validate_and_export_pipeline():
    """Test the complete validation and export pipeline."""
    # Create temporary directory with test data
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test service file
        service_file = os.path.join(temp_dir, "test_service.yaml")
        with open(service_file, 'w') as f:
            f.write("""
name: "Test Service"
category: "compute"
pricing:
  model: "free"
""")

        # Validate directory
        is_valid = validate_services_directory(temp_dir)
        assert is_valid

        # Export to JSON
        output_file = os.path.join(temp_dir, "output.json")
        export_services_to_json(temp_dir, output_file)
        assert os.path.exists(output_file)
```

### End-to-End Testing
- Test complete workflows from data ingestion to documentation generation
- Validate generated markdown files for correctness and completeness
- Test CLI tool execution with various input scenarios
- Ensure data integrity across format conversions (YAML → JSON → Markdown)

**Example E2E test:**
```python
import pytest
import subprocess
import tempfile
import os

def test_full_documentation_generation():
    """Test end-to-end documentation generation process."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Setup test data
        services_dir = os.path.join(temp_dir, "services")
        os.makedirs(services_dir)
        with open(os.path.join(services_dir, "test.yaml"), 'w') as f:
            f.write("""
name: "Test Service"
category: "compute"
description: "A test service"
pricing:
  model: "free"
""")

        # Run generation script
        result = subprocess.run([
            "python", "tools/python/generate_markdown.py",
            "--input", services_dir,
            "--output", os.path.join(temp_dir, "README.md")
        ], capture_output=True, text=True)

        assert result.returncode == 0
        assert "Test Service" in result.stdout
```

### Bash Script Testing
- Test Bash scripts for correct execution and error handling
- Validate script inputs and outputs
- Test file operations and external command calls

**Example using bats (Bash Automated Testing System):**
```bash
#!/usr/bin/env bats

@test "validate.sh succeeds with valid YAML" {
    # Create test file
    echo "name: test" > test.yaml

    run ./tools/bash/validate.sh test.yaml
    [ "$status" -eq 0 ]
    [ "$output" = "All YAML files are valid" ]

    rm test.yaml
}

@test "validate.sh fails with invalid YAML" {
    # Create invalid test file
    echo "invalid: yaml: content: [" > test.yaml

    run ./tools/bash/validate.sh test.yaml
    [ "$status" -eq 1 ]

    rm test.yaml
}
```

## Testing Tools and Automation

### Python Testing Tools
- Use pytest for unit and integration testing of Python scripts
- Implement pytest-cov for test coverage reporting
- Use pytest-mock for mocking external dependencies
- Leverage hypothesis for property-based testing of data validation functions

**pytest configuration (pytest.ini):**
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = --cov=tools/python --cov-report=html --cov-report=term-missing
```

### Bash Testing Tools
- Use bats-core for testing Bash scripts
- Implement shellcheck for static analysis of shell scripts
- Use shfmt for consistent Bash script formatting

**Example bats installation and usage:**
```bash
# Install bats
git clone https://github.com/bats-core/bats-core.git
cd bats-core
sudo ./install.sh /usr/local

# Run tests
bats tools/bash/test/
```

### Test Data Management
- Use fixtures for reusable test data
- Implement factories for generating test service/stack definitions
- Maintain separate test data directories that mirror production structure

**Example pytest fixture:**
```python
import pytest
import yaml

@pytest.fixture
def sample_service_data():
    """Provide sample valid service data for testing."""
    return {
        "name": "Sample Cloud Service",
        "category": "compute",
        "description": "A sample service for testing",
        "pricing": {
            "model": "free",
            "free_tier": {
                "available": True,
                "limits": [
                    {"resource": "instances", "amount": 1, "unit": "instance"}
                ]
            }
        },
        "features": ["Auto-scaling", "Load balancing"],
        "tags": ["cloud", "compute"]
    }

@pytest.fixture
def temp_service_file(tmp_path, sample_service_data):
    """Create a temporary service YAML file."""
    file_path = tmp_path / "service.yaml"
    with open(file_path, 'w') as f:
        yaml.dump(sample_service_data, f)
    return file_path
```

## Pre-commit Checks

### Automated Quality Gates
- All tests must pass before committing (unit, integration, end-to-end)
- Code must pass linting and formatting checks (flake8, black, isort)
- No debug statements (print(), console.log()) in production code
- Check for trailing whitespace and proper line endings
- Validate that all imports are used and properly organized
- Run security scans for vulnerabilities

### Pre-commit Hook Configuration
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
      - id: flake8

  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true
```

### Custom Validation Hooks
- Validate YAML/JSON schema compliance before commit
- Check for broken links in documentation
- Ensure generated files are up-to-date with source data

## Code Review Standards

### Mandatory Review Criteria
- All code changes require review before merging to main branch
- Verify test coverage for new code meets minimum thresholds
- Check for security vulnerabilities and proper input validation
- Ensure new code follows established patterns and conventions
- Validate proper error handling and logging
- Confirm documentation updates for public APIs and complex logic

### Review Checklist
- [ ] Unit tests added/updated for new functionality
- [ ] Integration tests pass for data processing pipelines
- [ ] Code follows project style guidelines (PEP 8, Black formatting)
- [ ] No hardcoded secrets or sensitive data
- [ ] Error messages are user-friendly and informative
- [ ] Functions have appropriate type hints and docstrings
- [ ] Performance considerations addressed for data processing
- [ ] Backward compatibility maintained for existing functionality

### Automated Review Tools
- Use GitHub Actions for automated code review checks
- Integrate CodeQL for security vulnerability detection
- Implement automated dependency vulnerability scanning

## CI/CD Integration

### Pipeline Structure
- Automate build, test, and deployment processes using GitHub Actions
- Implement multi-stage pipelines: lint → test → build → deploy
- Use matrix builds for testing across Python versions (3.8, 3.9, 3.10, 3.11)
- Maintain separate environments (development, staging, production)

### GitHub Actions Workflow Example
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', 3.11]

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r tools/python/requirements.txt
        pip install pytest pytest-cov

    - name: Lint with flake8
      run: flake8 tools/python --count --select=E9,F63,F7,F82 --show-source --statistics

    - name: Test with pytest
      run: pytest --cov=tools/python --cov-report=xml

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  validate-data:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Validate service data
      run: python tools/python/validate.py --directory services

    - name: Check links
      run: python tools/python/link_checker.py --directory services

  bash-tests:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Install bats
      run: |
        git clone https://github.com/bats-core/bats-core.git
        cd bats-core
        sudo ./install.sh /usr/local

    - name: Run Bash tests
      run: bats tools/bash/test/
```

### Quality Gates and Deployment
- Require all tests to pass before merge (branch protection rules)
- Implement automated deployment to staging on successful CI
- Use manual approval for production deployments
- Monitor test execution time and fail builds exceeding thresholds

### Monitoring and Reporting
- Generate test reports and coverage badges
- Track test failure rates and flaky tests
- Implement automated regression testing for critical paths
- Set up alerts for test suite failures

## Quality Standards & Validation

### Required for Every Service Entry
- Unique ID in kebab-case (provider-service)
- Official URL (links to landing page, not docs)
- Free tier type clearly stated (always-free vs trial vs credits)
- All limits with units (KB, GB, requests, hours, etc.)
- At least 2-3 gotchas (cost traps, limitations, surprises)
- Best use cases (realistic, not marketing-speak)
- Complementary services listed
- Estimated cost breakdown
- Last verified date within 180 days
- Source cited (official docs preferred)

### Accuracy Standards
- Never invent numbers - If you don't have exact limits, mark as [NEEDS VERIFICATION]
- Cite sources - Every fact traceable to official docs or credible blog (< 6 months old)
- Note date of verification - Services change frequently; flag anything old
- Include caveats - "This is correct as of [date]" or "Check official docs for current pricing"

### Completeness Standards
- List ALL gotchas - Cost traps, regional limits, bandwidth charges, account freezes, etc.
- Don't hide negatives - Users expect balanced evaluation, not sales pitch
- Explain why - "Why is egress expensive?" not just "egress is expensive"
- Suggest alternatives - Include competing services in the gotchas/alternatives section

### Currency Standards
- Validate age - Any entry > 180 days old should be re-verified
- Automated checks - Python script checks last_verified and warns
- CI/CD validation - GitHub Actions runs on every PR to validate schema
- Community oversight - Ask contributors to flag stale entries they know about

These testing rules ensure the awesome-free project maintains high code quality and reliability across all components. Regular review and updates to this document are recommended as the project evolves.