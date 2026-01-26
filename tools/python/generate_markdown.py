#!/usr/bin/env python3
"""
Generate markdown from YAML services.
"""

import os
import glob
import yaml
from jinja2 import Template
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

def group_services_by_category(services):
    from collections import defaultdict
    grouped = defaultdict(list)
    for service in services:
        grouped[service['category']].append(service)
    return grouped

def generate_markdown(services, output_file):
    grouped = group_services_by_category(services)

    template_str = """
# Awesome Free Services

This is a curated list of free tier services from various cloud providers.

{% for category, services in grouped.items() %}
## {{ category|title }}

{% for service in services %}
### {{ service.name }}

- **Provider**: {{ service.provider }}
- **URL**: [{{ service.url }}]({{ service.url }})
- **Free Tier Type**: {{ service.free_tier.type }}
- **Description**: Best for {{ service.best_for|join(', ') }}
- **Gotchas**: {{ service.gotchas|join(', ') if service.gotchas else 'None' }}
- **Last Verified**: {{ service.metadata.last_verified }}

{% endfor %}
{% endfor %}
"""

    template = Template(template_str)
    markdown = template.render(grouped=grouped)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown)

    print(f"Generated markdown to {output_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_markdown.py <output.md>")
        sys.exit(1)

    output_file = sys.argv[1]
    services = load_services()
    generate_markdown(services, output_file)

if __name__ == "__main__":
    main()