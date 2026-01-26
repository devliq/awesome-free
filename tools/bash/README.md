# Tools Documentation

This directory contains bash scripts and the `python/` subdirectory contains Python tools for managing the awesome-free project.

## Python Tools

All Python tools require Python 3 and the dependencies listed in `tools/python/requirements.txt`.

Install dependencies: `pip install -r tools/python/requirements.txt`

### validate.py
Validates all YAML files against their JSON schemas.
- Services in `services/` validated against `tools/schema/service.schema.json`
- Stacks in `stacks/` validated against `tools/schema/stack.schema.json`

Usage: `python tools/python/validate.py`

### compare.py
Displays services grouped by provider and category in a table.

Usage: `python tools/python/compare.py`

### export_csv.py
Exports all services to a CSV file.

Usage: `python tools/python/export_csv.py <output.csv>`

### export_json.py
Exports all services to a JSON file.

Usage: `python tools/python/export_json.py <output.json>`

### link_checker.py
Checks for broken links in service URLs and resources.

Usage: `python tools/python/link_checker.py`

### generate_markdown.py
Generates a markdown file from services, grouped by category.

Usage: `python tools/python/generate_markdown.py <output.md>`

### freshness_check.py
Flags services with `last_verified` older than 6 months.

Usage: `python tools/python/freshness_check.py`

## Bash Scripts

### validate.sh
Bash wrapper for running validation. Checks for Python and dependencies.

Usage: `./tools/bash/validate.sh`

### update_readme.sh
Auto-generates README.md from services using the markdown generator.

Usage: `./tools/bash/update_readme.sh`

### check_syntax.sh
Quick YAML syntax checker without full validation.

Usage: `./tools/bash/check_syntax.sh`

## CI/CD Integration

These tools are integrated into GitHub Actions workflows in `.github/workflows/`:
- `validate.yml`: Runs validation on PRs
- `link-checker.yml`: Checks links
- `freshness-check.yml`: Checks for stale entries