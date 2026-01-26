#!/bin/bash

# Bash wrapper for validation

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"

cd "$PROJECT_ROOT"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed or not in PATH."
    exit 1
fi

# Check if required packages are installed
python3 -c "import yaml, jsonschema" 2>/dev/null || {
    echo "Required Python packages not installed. Run: pip install -r tools/python/requirements.txt"
    exit 1
}

# Run validation
python3 tools/python/validate.py