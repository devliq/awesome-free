#!/usr/bin/env python3
"""
Export services to CSV.
"""

import os
import glob
import yaml
import csv
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

def flatten_service(service):
    # Flatten key fields
    row = {
        'id': service.get('id', ''),
        'name': service.get('name', ''),
        'provider': service.get('provider', ''),
        'category': service.get('category', ''),
        'url': service.get('url', ''),
        'free_tier_type': service.get('free_tier', {}).get('type', ''),
        'always_free_included': service.get('free_tier', {}).get('always_free', {}).get('included', False),
        'time_limited_duration_days': service.get('free_tier', {}).get('time_limited', {}).get('duration_days', ''),
        'credits_amount': service.get('free_tier', {}).get('credits', {}).get('amount', ''),
        'regions_always_free': ', '.join(service.get('regions', {}).get('always_free', [])),
        'gotchas': ', '.join(service.get('gotchas', [])),
        'best_for': ', '.join(service.get('best_for', [])),
        'not_for': ', '.join(service.get('not_for', [])),
        'cost_under_free_tier': service.get('cost', {}).get('under_free_tier', ''),
        'cost_typical_after': service.get('cost', {}).get('typical_after_free', ''),
        'requirements_credit_card': service.get('requirements', {}).get('credit_card', False),
        'requirements_phone_verification': service.get('requirements', {}).get('phone_verification', False),
        'official_docs': service.get('resources', {}).get('official_docs', ''),
        'last_verified': service.get('metadata', {}).get('last_verified', ''),
        'verified_by': service.get('metadata', {}).get('verified_by', ''),
        'cost_risk': service.get('flags', {}).get('cost_risk', ''),
        'vendor_lock_in': service.get('flags', {}).get('vendor_lock_in', ''),
        'learning_curve': service.get('flags', {}).get('learning_curve', ''),
        'setup_time': service.get('flags', {}).get('setup_time', ''),
    }
    return row

def export_to_csv(services, output_file):
    if not services:
        print("No services to export.")
        return

    fieldnames = list(flatten_service(services[0]).keys())

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for service in services:
            writer.writerow(flatten_service(service))

    print(f"Exported {len(services)} services to {output_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python export_csv.py <output.csv>")
        sys.exit(1)

    output_file = sys.argv[1]
    services = load_services()
    export_to_csv(services, output_file)

if __name__ == "__main__":
    main()