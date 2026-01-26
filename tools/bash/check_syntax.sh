#!/bin/bash

# Quick syntax checker for YAML files

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"

cd "$PROJECT_ROOT"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed or not in PATH."
    exit 1
fi

# Check if PyYAML is installed
python3 -c "import yaml" 2>/dev/null || {
    echo "PyYAML not installed. Run: pip install PyYAML"
    exit 1
}

# Find all YAML files
find services stacks -name "*.yml" -o -name "*.yaml" | while read -r file; do
    if ! python3 -c "import yaml; yaml.safe_load(open('$file'))" 2>/dev/null; then
        echo "Syntax error in $file"
        exit 1
    fi
done

echo "All YAML files have valid syntax."