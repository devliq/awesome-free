# Documentation Standards for Awesome-Free Project

This document outlines comprehensive documentation standards for the awesome-free project. These rules ensure high-quality, consistent, and maintainable documentation across all project components, including the extensive docs/ directory, provider guides, category guides, and evaluation criteria. The guidelines are tailored to the project's focus on curating legitimate free services while maintaining clear, actionable documentation for contributors and users.

## README Requirements

### Core README Structure

- **Project Overview**: Include a clear, concise description of the awesome-free project within the first 3-5 lines
- **Key Features**: Highlight the main benefits (free tier curation, evaluation criteria, provider guides)
- **Quick Start**: Provide immediate steps for users to get started with the documentation or tools
- **Table of Contents**: Use a collapsible TOC for easy navigation to sections like Overview, Evaluation Criteria, Category Guides, etc.

### Content Standards

- **Accurate Setup Instructions**: Keep installation and usage instructions current with the latest project structure
- **Environment Variables**: Document all required environment variables, configuration files, and their purposes
- **Troubleshooting Section**: Include common issues and solutions, especially for validation scripts and data processing
- **Contribution Guidelines**: Link to CONTRIBUTING.md and explain how to add new services or update documentation

### Maintenance Rules

- Update README.md immediately when adding new major features or changing core functionality
- Ensure all links are functional and point to the correct files within the docs/ directory
- Keep the README under 500 lines to maintain readability; use links to detailed docs for depth

```markdown
# Awesome-Free

A curated collection of legitimate free-tier cloud services with comprehensive evaluation criteria and provider guides.

## Quick Start

1. Browse [Category Guides](./docs/CATEGORY_GUIDES/) to find services by type
2. Check [Evaluation Criteria](./docs/EVALUATION_CRITERIA.md) for inclusion standards
3. Use [tools/python/validate.py](./tools/python/validate.py) to verify service definitions

## Documentation

- [Overview](./docs/OVERVIEW.md) - Project goals and methodology
- [How to Use](./docs/HOW_TO_USE.md) - Getting started guide
- [Category Guides](./docs/CATEGORY_GUIDES/) - Service categories and recommendations
- [Provider Guides](./docs/PROVIDER_GUIDES/) - Cloud provider comparisons
```

## Documentation Tools and Automation

### Static Site Generators

- **MkDocs**: Use for generating documentation sites from the docs/ directory markdown files
- **Docusaurus**: Consider for more interactive documentation with versioning support
- **GitBook**: Alternative for collaborative documentation with built-in search

### Automation Tools

- **GitHub Actions**: Automate documentation deployment on pushes to main branch
- **Read the Docs**: Host public documentation with automatic builds from GitHub
- **Pre-commit Hooks**: Use markdownlint and link checkers in pre-commit for quality gates

### Integration Examples

```yaml
# .github/workflows/docs.yml
name: Deploy Documentation
on:
  push:
    branches: [ main ]
    paths: [ 'docs/**' ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - run: pip install mkdocs mkdocs-material
      - run: mkdocs gh-deploy --force
```

### Markdown Processing

- **markdownlint**: Enforce consistent markdown formatting across all docs/
- **remark**: Use for automated markdown processing and linting
- **Prettier**: Format markdown files with `--parser markdown`

## Code Documentation

### Python Documentation Standards

- **Docstring Format**: Use Google-style docstrings for all public functions, classes, and modules
- **Type Hints**: Include type annotations for all parameters and return values
- **Function Documentation**: Document purpose, parameters, return values, and exceptions

```python
def validate_service_data(service_data: Dict[str, Any]) -> List[str]:
    """Validate a service definition against schema requirements.

    Performs comprehensive validation of service data including required fields,
    data types, and business logic rules.

    Args:
        service_data: Dictionary containing service metadata and configuration

    Returns:
        List of validation error messages. Empty list indicates valid data.

    Raises:
        ValueError: If service_data is not a dictionary

    Example:
        >>> errors = validate_service_data({"name": "Test Service"})
        >>> print(errors)
        ['Missing required field: category']
    """
    if not isinstance(service_data, dict):
        raise ValueError("service_data must be a dictionary")

    errors = []
    # Validation logic...
    return errors
```

### Bash Script Documentation

- **Script Headers**: Include purpose, usage, and examples in comment blocks at the top
- **Function Comments**: Document all functions with purpose and parameters
- **Inline Comments**: Explain complex logic or non-obvious operations

```bash
#!/bin/bash
# validate.sh - Validate YAML service definitions
# Usage: ./validate.sh [directory]
# Example: ./validate.sh services/

validate_yaml_file() {
    # Validate a single YAML file for syntax and structure
    local file_path="$1"

    if ! yamllint "$file_path" > /dev/null 2>&1; then
        echo "ERROR: Invalid YAML in $file_path" >&2
        return 1
    fi
}

main() {
    local target_dir="${1:-services}"

    # Validate all YAML files in directory
    find "$target_dir" -name "*.yaml" -type f | while read -r file; do
        validate_yaml_file "$file" || exit 1
    done

    echo "All YAML files are valid"
}
```

### Schema Documentation

- **JSON Schema Comments**: Document all schema files in tools/schema/ with inline comments
- **Field Descriptions**: Explain purpose and validation rules for each field
- **Example Objects**: Provide valid and invalid examples in comments

```json
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "title": "Service Definition Schema",
  "description": "Schema for validating service YAML definitions in awesome-free",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Human-readable service name",
      "minLength": 1,
      "maxLength": 100
    },
    "category": {
      "type": "string",
      "description": "Service category (compute, storage, database, etc.)",
      "enum": ["compute", "storage", "database", "cdn-edge", "serverless"]
    }
  },
  "required": ["name", "category"]
}
```

## Technical Documentation

### Architecture Documentation

- **System Overview**: Document the overall architecture in docs/OVERVIEW.md
- **Data Flow**: Explain how data flows from services/ YAML files through validation to generated documentation
- **Tool Relationships**: Describe how Python tools, Bash scripts, and schemas interact

### API Documentation

- **Tool Interfaces**: Document command-line interfaces for all tools in tools/python/ and tools/bash/
- **Function Signatures**: Detail public functions and their contracts
- **Error Codes**: Document exit codes and error messages from scripts

### Database Schema Documentation

- **Data Models**: Document the structure of service and stack definitions
- **Relationships**: Explain how services relate to categories and providers
- **Validation Rules**: Detail business logic constraints beyond basic schema validation

```markdown
## Service Data Model

### Core Fields
- `name`: Service display name (string, required)
- `category`: Service category classification (enum, required)
- `pricing`: Pricing model information (object, required)

### Relationships
- Services belong to one category
- Services may be offered by multiple providers
- Services can be components of stacks

### Validation Rules
- Name must be unique within category
- Pricing model must include free tier availability
- All URLs must be HTTPS and accessible
```

## Repository Initialization

### Quick Start for Repository Setup

```bash
# 1. Create the repo
git init awesome-free
cd awesome-free

# 2. Create directory structure
mkdir -p services/{compute,database,storage,cdn-edge,serverless,devtools,communication,ai-ml,creative}
mkdir -p stacks/{serverless-api,full-stack-app,static-site-cdn,monitoring-observability}
mkdir -p docs/{PROVIDER_GUIDES,CATEGORY_GUIDES}
mkdir -p tools/{schema,python,bash}
mkdir -p data
mkdir -p .github/{ISSUE_TEMPLATE,workflows}
mkdir -p archive

# 3. Create initial files
touch README.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
touch .gitignore .github/PULL_REQUEST_TEMPLATE.md
touch docs/OVERVIEW.md docs/HOW_TO_USE.md docs/EVALUATION_CRITERIA.md
touch tools/schema/service.schema.json tools/schema/stack.schema.json

# 4. Copy kilocode-instructions.md to root or .github/
cp .kilocode/prompts.md .kilocode-instructions.md

# 5. Initialize git
git add .
git commit -m "Initial commit: directory structure and documentation templates"
```

## Best Practices

### Documentation Maintenance

- **Version Control**: Keep documentation in sync with code changes
- **Review Process**: Require documentation review for all pull requests
- **Freshness Checks**: Regularly verify that examples and links remain current

### Content Organization

- **Logical Hierarchy**: Use clear heading structure (H1 → H2 → H3)
- **Consistent Terminology**: Use standard terms (service, stack, category, provider)
- **Cross-References**: Link related documents within the docs/ directory

### Markdown Generation Standards

When generating markdown files:

- **Clear Headings**: Use H1 for sections, H2 for subsections
- **Real Examples**: Show actual URLs, limits, and use cases
- **Extensive Linking**: Link every service to official documentation
- **Table of Contents**: Include TOC for long documents
- **Consistent Formatting**: Use code blocks for commands, bold for emphasis
- **Plain Language**: Explain cloud terms in simple English, avoid jargon

### Accessibility and Usability

- **Clear Language**: Use simple, direct language avoiding jargon
- **Progressive Disclosure**: Start with overview, link to details
- **Search Optimization**: Use descriptive headings and include keywords

### Automation Integration

- **CI/CD Checks**: Include documentation validation in GitHub Actions
- **Link Checking**: Automate verification of all internal and external links
- **Format Enforcement**: Use pre-commit hooks for consistent formatting

```yaml
# .pre-commit-config.yaml (excerpt)
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-yaml

  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.32.2
    hooks:
      - id: markdownlint
        files: \.(md|mdown|markdown)$
        exclude: ^(archive/|CHANGELOG.md)
```

### Metrics and Improvement

- **Documentation Coverage**: Track which parts of the codebase have documentation
- **User Feedback**: Monitor issues and PRs for documentation improvement opportunities
- **Regular Audits**: Quarterly review of documentation completeness and accuracy

These documentation standards ensure the awesome-free project maintains high-quality, accessible documentation that supports both contributors and users in understanding and utilizing the curated free services effectively.