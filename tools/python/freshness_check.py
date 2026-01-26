#!/usr/bin/env python3
"""
Flag stale entries (> 6 months).
"""

import os
import glob
import yaml
from datetime import datetime, timedelta
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
            services.append((yaml_file, data['service']))
        except Exception as e:
            print(f"Error loading {yaml_file}: {e}")

    for yaml_file in glob.glob(os.path.join(services_dir, '**', '*.yaml'), recursive=True):
        try:
            with open(yaml_file, 'r') as f:
                data = yaml.safe_load(f)
            services.append((yaml_file, data['service']))
        except Exception as e:
            print(f"Error loading {yaml_file}: {e}")

    return services

def is_stale(last_verified_str):
    try:
        last_verified = datetime.strptime(last_verified_str, '%Y-%m-%d')
        six_months_ago = datetime.now() - timedelta(days=180)
        return last_verified < six_months_ago
    except ValueError:
        return True  # If date format wrong, consider stale

def main():
    services = load_services()
    stale = []
    for yaml_file, service in services:
        last_verified = service.get('metadata', {}).get('last_verified', '')
        if is_stale(last_verified):
            stale.append((yaml_file, last_verified))

    if stale:
        print("Stale entries (> 6 months):")
        for file, date in stale:
            print(f"  {file}: last verified {date}")
        sys.exit(1)
    else:
        print("All entries are fresh.")

if __name__ == "__main__":
    main()