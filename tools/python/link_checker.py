#!/usr/bin/env python3
"""
Check for broken links in services.
"""

import os
import glob
import yaml
import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

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

def extract_urls(service):
    urls = []
    if 'url' in service:
        urls.append(service['url'])
    resources = service.get('resources', {})
    for key in ['official_docs', 'free_tier_page', 'tutorial', 'community']:
        if key in resources and resources[key]:
            urls.append(resources[key])
    return urls

def check_url(url):
    try:
        response = requests.head(url, timeout=10, allow_redirects=True)
        return url, response.status_code < 400
    except requests.RequestException:
        return url, False

def main():
    services = load_services()
    all_urls = []
    for yaml_file, service in services:
        urls = extract_urls(service)
        for url in urls:
            all_urls.append((yaml_file, url))

    broken = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_url, url): (file, url) for file, url in all_urls}
        for future in as_completed(futures):
            file, url = futures[future]
            try:
                checked_url, is_ok = future.result()
                if not is_ok:
                    broken.append((file, checked_url))
            except Exception as e:
                broken.append((file, url))

    if broken:
        print("Broken links found:")
        for file, url in broken:
            print(f"  {file}: {url}")
        sys.exit(1)
    else:
        print("All links are accessible.")

if __name__ == "__main__":
    main()