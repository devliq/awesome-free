#!/usr/bin/env python3
"""
Validate all YAML files against their schemas.
"""

import os
import glob
import yaml
import json
from jsonschema import validate, ValidationError, SchemaError
import sys

def load_schema(schema_path):
    with open(schema_path, 'r') as f:
        return json.load(f)

def validate_yaml_file(yaml_file, schema):
    try:
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
        validate(instance=data, schema=schema)
        return True, None
    except FileNotFoundError as e:
        return False, f"File not found: {e}"
    except yaml.YAMLError as e:
        return False, f"YAML Error: {e}"
    except ValidationError as e:
        return False, f"Validation Error: {e.message}"
    except SchemaError as e:
        return False, f"Schema Error: {e.message}"

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    schema_dir = os.path.join(project_root, 'tools', 'schema')

    service_schema = load_schema(os.path.join(schema_dir, 'service.schema.json'))
    stack_schema = load_schema(os.path.join(schema_dir, 'stack.schema.json'))

    services_dir = os.path.join(project_root, 'services')
    stacks_dir = os.path.join(project_root, 'stacks')

    errors = []

    # Validate services
    for yaml_file in glob.glob(os.path.join(services_dir, '**', '*.yml'), recursive=True):
        valid, error = validate_yaml_file(yaml_file, service_schema)
        if not valid:
            errors.append(f"{yaml_file}: {error}")

    for yaml_file in glob.glob(os.path.join(services_dir, '**', '*.yaml'), recursive=True):
        valid, error = validate_yaml_file(yaml_file, service_schema)
        if not valid:
            errors.append(f"{yaml_file}: {error}")

    # Validate stacks
    for yaml_file in glob.glob(os.path.join(stacks_dir, '**', '*.yml'), recursive=True):
        valid, error = validate_yaml_file(yaml_file, stack_schema)
        if not valid:
            errors.append(f"{yaml_file}: {error}")

    for yaml_file in glob.glob(os.path.join(stacks_dir, '**', '*.yaml'), recursive=True):
        valid, error = validate_yaml_file(yaml_file, stack_schema)
        if not valid:
            errors.append(f"{yaml_file}: {error}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  {error}")
        sys.exit(1)
    else:
        print("All YAML files are valid.")

if __name__ == "__main__":
    main()