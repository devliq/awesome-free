# Code Style Rules for Awesome-Free Project

This document outlines comprehensive code style guidelines for the awesome-free project. These rules ensure consistency, readability, and maintainability across all code contributions. The guidelines are tailored to the project's specific needs while following industry best practices.

## Python Code Style

### PEP 8 Compliance with Project Adaptations

The project follows PEP 8 with the following adaptations for the awesome-free context:

#### Naming Conventions
- **Modules and packages**: Use lowercase with underscores (e.g., `link_checker.py`, `data_processor.py`)
- **Classes**: PascalCase for service and stack classes (e.g., `ServiceValidator`, `StackGenerator`)
- **Functions and methods**: snake_case (e.g., `validate_service()`, `export_to_json()`)
- **Constants**: UPPERCASE with underscores (e.g., `MAX_RETRIES = 3`)
- **Variables**: snake_case, descriptive names (e.g., `service_data`, `validation_errors`)

#### Line Length and Formatting
- Maximum line length: 88 characters (Black default)
- Use 4 spaces for indentation
- Break long lines logically, preferring parentheses over backslashes

#### Imports
- Standard library imports first, then third-party, then local imports
- One import per line
- Use absolute imports for clarity
- Group imports with blank lines between groups

```python
import os
import sys
from typing import Dict, List, Optional

import requests
import yaml

from .validators import ServiceValidator
from .exporters import JSONExporter
```

#### Docstrings and Comments
- Use triple-quoted docstrings for all public functions, classes, and modules
- Follow Google-style docstring format
- Comments should explain why, not what

```python
def validate_service(service_data: Dict) -> List[str]:
    """Validate a service definition against schema requirements.

    Args:
        service_data: Dictionary containing service metadata

    Returns:
        List of validation error messages, empty if valid

    Raises:
        ValueError: If service_data is not a dictionary
    """
    if not isinstance(service_data, dict):
        raise ValueError("service_data must be a dictionary")
    # Implementation...
```

#### Error Handling
- Use specific exception types
- Provide meaningful error messages
- Avoid bare except clauses

#### Type Hints
- Use type hints for all function parameters and return values
- Import from `typing` module as needed
- Use `Optional` for nullable types

### Tools for Enforcement
- **Black**: Automatic code formatting (`black .`)
- **isort**: Import sorting (`isort .`)
- **flake8**: Linting with PEP 8 checks (`flake8 .`)
- **mypy**: Static type checking (`mypy .`)

## Bash Scripting Standards

### Script Structure
- Use `#!/bin/bash` shebang
- Include script description and usage in comments at the top
- Use functions for reusable code blocks
- Exit with appropriate status codes

### Naming and Variables
- Use lowercase with underscores for variable names (e.g., `output_file`, `error_count`)
- Use `readonly` for constants
- Quote all variable expansions to prevent word splitting

### Error Handling
- Use `set -e` to exit on first error
- Use `set -u` to treat unset variables as errors
- Implement proper error checking for commands

### Best Practices
- Use `$(command)` instead of backticks for command substitution
- Use `[[ ]]` for conditional expressions (Bash 4+ features)
- Avoid using `eval` unless absolutely necessary
- Keep scripts modular and focused on single responsibilities

```bash
#!/bin/bash
# Script to validate YAML files in the services directory
# Usage: ./validate.sh [directory]

set -euo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly DEFAULT_DIR="${SCRIPT_DIR}/../../services"

validate_yaml() {
    local file="$1"
    if ! yamllint "$file" > /dev/null 2>&1; then
        echo "ERROR: Invalid YAML in $file" >&2
        return 1
    fi
}

main() {
    local target_dir="${1:-$DEFAULT_DIR}"
    local yaml_files

    if [[ ! -d "$target_dir" ]]; then
        echo "ERROR: Directory $target_dir does not exist" >&2
        exit 1
    fi

    mapfile -t yaml_files < <(find "$target_dir" -name "*.yaml" -type f)

    for file in "${yaml_files[@]}"; do
        if ! validate_yaml "$file"; then
            exit 1
        fi
    done

    echo "All YAML files are valid"
}

main "$@"
```

### Tools for Enforcement
- **shellcheck**: Static analysis for shell scripts (`shellcheck script.sh`)
- **shfmt**: Bash script formatter (`shfmt -w script.sh`)
- **yamllint**: YAML validation (integrated into validation scripts)

## YAML Formatting for Service/Stack Definitions

### Structure and Organization
- Use 2 spaces for indentation (consistent with YAML best practices)
- Use kebab-case for keys (e.g., `service-name`, `pricing-model`)
- Group related properties logically
- Use comments to explain complex structures

### Data Types and Values
- Use appropriate data types (strings, booleans, numbers, arrays, objects)
- Quote strings when necessary (special characters, leading/trailing spaces)
- Use multi-line strings for descriptions and documentation
- Maintain consistent ordering of keys within objects
- 2-space indentation (not tabs)
- Consistent key ordering (id, name, provider, category, etc.)
- Comments explaining non-obvious fields
- ISO 8601 dates (YYYY-MM-DD)

### Validation and Schema
- All YAML files must conform to defined JSON schemas
- Use anchors and aliases for repeated structures where appropriate
- Keep files focused and avoid overly complex nesting

### File Organization Rules
- One service = one YAML file (don't combine multiple services)
- File naming = [provider]-[service].yaml in lowercase (aws-ec2.yaml, not AWS-EC2.yaml)
- Directory by category = services/compute/, services/database/, etc.
- Consistent indentation = 2 spaces, no tabs
- No trailing whitespace

```yaml
# Example service definition
service:
  name: "Example Cloud Service"
  category: "compute"
  description: |
    A comprehensive cloud computing platform offering
    virtual machines, containers, and serverless functions
    with global availability and enterprise-grade security.

  pricing:
    model: "pay-as-you-go"
    free-tier:
      available: true
      limits:
        - resource: "compute-hours"
          amount: 750
          unit: "hours/month"
        - resource: "storage"
          amount: 5
          unit: "GB"

  features:
    - "Auto-scaling"
    - "Load balancing"
    - "Monitoring and logging"
    - "Multi-region deployment"

  documentation:
    official: "https://example.com/docs"
    api-reference: "https://api.example.com"

  tags:
    - "cloud"
    - "compute"
    - "containers"
    - "serverless"
```

### Tools for Enforcement
- **yamllint**: YAML linting and formatting (`yamllint file.yaml`)
- **prettier**: YAML formatting with `--parser yaml` (`prettier --write file.yaml`)
- **Custom validation scripts**: Project-specific schema validation using Python tools

## Markdown Conventions for Documentation

### File Structure
- Use descriptive filenames with kebab-case (e.g., `evaluation-criteria.md`, `how-to-contribute.md`)
- Include front matter for metadata when applicable
- Use consistent heading hierarchy (H1 for title, H2 for sections, etc.)

### Formatting Standards
- Use ATX-style headers (`# Header`) instead of Setext-style
- Use code blocks with language specification for syntax highlighting
- Use inline code for commands, file names, and technical terms
- Use emphasis sparingly: *italics* for emphasis, **bold** for strong emphasis

### Lists and Tables
- Use hyphens for unordered lists, numbers for ordered lists
- Maintain consistent indentation for nested lists
- Use table format for structured data with proper alignment

### Links and References
- Use reference-style links for better readability
- Keep link text descriptive
- Use relative links for internal documentation

```markdown
# Evaluation Criteria

This document outlines the criteria used to evaluate services for inclusion in awesome-free.

## Core Requirements

All services must meet the following criteria:

- **Free tier availability**: Services must offer a genuine free tier without time limitations
- **Production readiness**: Free tier should be suitable for production workloads, not just development
- **API access**: Programmatic access through APIs or SDKs
- **Documentation quality**: Comprehensive documentation and examples

## Evaluation Process

1. Initial screening against core requirements
2. Technical validation of free tier claims
3. Community feedback and usage reports
4. Periodic re-evaluation (quarterly)

## Categories

| Category | Description | Key Metrics |
|----------|-------------|-------------|
| Compute | Virtual machines, containers | vCPU, RAM, storage |
| Storage | Object/file storage | GB stored, transfer limits |
| Database | Managed database services | Connections, storage, queries |
| CDN | Content delivery networks | Bandwidth, requests |

For more details, see the [category guides][category-guides].

[category-guides]: ./CATEGORY_GUIDES/
```

### Tools for Enforcement
- **markdownlint**: Markdown linting (`markdownlint file.md`)
- **prettier**: Markdown formatting (`prettier --write file.md`)
- **remark**: Markdown processor with plugins for consistency checks

## General Guidelines

### Commit Messages
- Use conventional commit format: `type(scope): description`
- Keep subject line under 50 characters
- Use imperative mood ("Add feature" not "Added feature")

### Code Reviews
- All changes require review before merging
- Focus on code quality, consistency, and adherence to these guidelines
- Use automated tools to catch style issues before review

### Tool Integration
- Integrate style checking into CI/CD pipelines
- Use pre-commit hooks for automatic formatting
- Maintain configuration files for all linting and formatting tools

These guidelines ensure that the awesome-free project maintains high code quality and consistency across all contributions. Regular updates to this document may be necessary as the project evolves.