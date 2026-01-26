#!/usr/bin/env python3
"""
Compare providers side-by-side by displaying services grouped by provider and category.
"""

import os
import glob
import yaml
from collections import defaultdict
from tabulate import tabulate

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

def group_by_provider_category(services):
    grouped = defaultdict(lambda: defaultdict(list))
    for service in services:
        provider = service['provider']
        category = service['category']
        grouped[provider][category].append(service['name'])
    return grouped

def display_comparison(grouped):
    # Create a table with providers as rows, categories as columns
    providers = sorted(grouped.keys())
    categories = set()
    for provider in providers:
        categories.update(grouped[provider].keys())
    categories = sorted(categories)

    table = []
    for provider in providers:
        row = [provider]
        for category in categories:
            services = grouped[provider].get(category, [])
            row.append(', '.join(services) if services else '-')
        table.append(row)

    headers = ['Provider'] + categories
    print(tabulate(table, headers=headers, tablefmt='grid'))

def main():
    services = load_services()
    grouped = group_by_provider_category(services)
    display_comparison(grouped)

if __name__ == "__main__":
    main()