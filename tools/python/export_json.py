#!/usr/bin/env python3
"""
Export services to JSON.
"""

import os
import glob
import yaml
import json
import sys

def load_services():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    services_dir = os.path.join(project_root, 'services')

    services = []
    for yaml_file in glob.glob(os.path.join(services_dir, '**', '*.yml'), recursive=True):
        try:
            with open(yaml_file, 'r') as f:
                data = yaml.safe_load(f)
            services.append(data['service'])
        except Exception as e:
            print(f"Error loading {yaml_file}: {e}")

    for yaml_file in glob.glob(os.path.join(services_dir, '**', '*.yaml'), recursive=True):
        try:
            with open(yaml_file, 'r') as f:
                data = yaml.safe_load(f)
            services.append(data['service'])
        except Exception as e:
            print(f"Error loading {yaml_file}: {e}")

    return services

def export_to_json(services, output_file):
    with open(output_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(services, jsonfile, indent=2, ensure_ascii=False)

    print(f"Exported {len(services)} services to {output_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python export_json.py <output.json>")
        sys.exit(1)

    output_file = sys.argv[1]
    services = load_services()
    export_to_json(services, output_file)

if __name__ == "__main__":
    main()