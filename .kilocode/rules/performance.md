# Performance Rules for Awesome-Free Project

This document outlines comprehensive performance optimization guidelines for the awesome-free project. These rules ensure efficient data processing, validation scripts, and documentation generation while maintaining high performance standards. The guidelines are tailored to the project's Python-based tooling, YAML/JSON data handling, and potential web documentation components.

## Optimization Techniques

### Efficient Algorithms and Data Structures

- **Use appropriate data structures**: Prefer dictionaries for O(1) lookups over lists for frequent searches. For example, when validating services, load service data into a dictionary keyed by service ID for fast access.

```python
# Example: Efficient service lookup
service_dict = {service['id']: service for service in services}
if service_id in service_dict:
    validate_service(service_dict[service_id])
```

- **Implement streaming for large files**: Use generators or streaming parsers for processing large YAML/JSON files to avoid loading entire datasets into memory.

```python
import yaml

def stream_yaml_services(file_path):
    with open(file_path, 'r') as f:
        for service in yaml.safe_load_all(f):
            yield service
```

- **Optimize loops and iterations**: Use list comprehensions for simple transformations and avoid nested loops where possible. For link checking, batch requests using asyncio for concurrent processing.

```python
import asyncio
import aiohttp

async def check_links_batch(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [session.head(url) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)
```

### Caching Strategies

- **Implement in-memory caching**: Use functools.lru_cache for expensive computations like schema validation or repeated API calls.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def validate_service_schema(service_data):
    # Expensive validation logic
    return jsonschema.validate(service_data, schema)
```

- **Cache external data**: Store API responses or external validation results in Redis or local files with TTL to reduce redundant network calls.

```python
import redis
import json

cache = redis.Redis()

def get_cached_api_data(key, ttl=3600):
    cached = cache.get(key)
    if cached:
        return json.loads(cached)
    data = fetch_api_data(key)
    cache.setex(key, ttl, json.dumps(data))
    return data
```

- **Lazy loading for documentation**: Generate documentation pages on-demand rather than pre-building all content. Use pagination for large service lists.

### Lazy Loading and Resource Management

- **Defer heavy computations**: For documentation generation, load and process data only when needed. Use lazy properties in classes.

```python
class ServiceProcessor:
    @property
    def processed_data(self):
        if not hasattr(self, '_processed_data'):
            self._processed_data = self._process_data()
        return self._processed_data
```

- **Resource pooling**: Use connection pools for database operations or external API calls to reuse connections efficiently.

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=0.3)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
```

## Profiling and Monitoring

### Profiling Tools and Techniques

- **Use Python profilers**: Employ cProfile or line_profiler to identify bottlenecks in validation scripts and data processing.

```bash
python -m cProfile -s time tools/python/validate.py
```

- **Memory profiling**: Use memory_profiler to detect memory leaks in long-running processes.

```python
from memory_profiler import profile

@profile
def process_large_dataset():
    # Processing logic
    pass
```

- **Benchmark critical functions**: Use timeit for micro-benchmarks of core algorithms.

```python
import timeit

time = timeit.timeit('validate_service(data)', globals=globals(), number=1000)
print(f"Average validation time: {time/1000:.4f} seconds")
```

### Monitoring and APM

- **Implement logging for performance metrics**: Log execution times and resource usage in scripts.

```python
import logging
import time

start_time = time.time()
# Process data
end_time = time.time()
logging.info(f"Data processing completed in {end_time - start_time:.2f} seconds")
```

- **Application Performance Monitoring**: Integrate tools like New Relic or DataDog for monitoring script performance in production environments.

- **Core Web Vitals (for web documentation)**: If the project includes a web interface for documentation, monitor Largest Contentful Paint (LCP), First Input Delay (FID), and Cumulative Layout Shift (CLS).

```javascript
// Example: Monitoring LCP in a web app
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry.entryType === 'largest-contentful-paint') {
      console.log('LCP:', entry.startTime);
    }
  }
}).observe({entryTypes: ['largest-contentful-paint']});
```

### Alerting and Thresholds

- Set performance budgets: Define maximum acceptable execution times for key operations and alert when exceeded.

```python
MAX_VALIDATION_TIME = 30  # seconds

if validation_time > MAX_VALIDATION_TIME:
    logging.warning(f"Validation exceeded budget: {validation_time}s")
```

## Best Practices

### Critical Rendering Path Optimization

- **Minimize blocking operations**: For web documentation, optimize CSS and JavaScript loading. Use async/defer for scripts.

```html
<script src="validation.js" defer></script>
<link rel="stylesheet" href="styles.css" media="print" onload="this.media='all'">
```

- **Optimize images and assets**: Compress images and use modern formats (WebP) for documentation pages.

- **Prioritize above-the-fold content**: Load critical documentation content first, defer non-essential elements.

### Graceful Degradation and Error Handling

- **Implement fallback mechanisms**: If a service validation fails due to network issues, provide cached results or skip non-critical validations.

```python
try:
    result = validate_external_service(service)
except requests.RequestException:
    logging.warning("External validation failed, using cached result")
    result = get_cached_validation(service)
```

- **Progressive enhancement**: Design scripts to work with minimal resources and enhance performance when more resources are available.

- **Handle large datasets gracefully**: Implement pagination or chunking for processing thousands of services.

```python
def process_services_in_chunks(services, chunk_size=100):
    for i in range(0, len(services), chunk_size):
        chunk = services[i:i + chunk_size]
        process_chunk(chunk)
```

### Resource Management

- **Limit concurrent operations**: Use semaphores to prevent overwhelming system resources during parallel processing.

```python
import asyncio

semaphore = asyncio.Semaphore(10)  # Limit to 10 concurrent requests

async def limited_request(url):
    async with semaphore:
        return await fetch_url(url)
```

- **Clean up resources**: Use context managers for file operations and database connections.

```python
with open('services.yaml', 'r') as f:
    data = yaml.safe_load(f)
# File automatically closed
```

## Tools and Automation

### Performance Testing Tools

- **Lighthouse**: For web documentation performance audits, focusing on performance, accessibility, and SEO.

```bash
npx lighthouse https://awesome-free-docs.example.com --output=json --output-path=./report.json
```

- **Webpack Bundle Analyzer**: If using JavaScript for web components, analyze bundle sizes.

```javascript
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  plugins: [new BundleAnalyzerPlugin()]
};
```

- **Locust or JMeter**: For load testing data processing pipelines.

### CI/CD Integration

- **Automate performance checks**: Integrate performance testing in GitHub Actions or CI pipelines.

```yaml
# .github/workflows/performance.yml
name: Performance Tests
on: [push, pull_request]
jobs:
  performance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run performance tests
        run: python -m pytest tests/ --durations=10
      - name: Profile critical functions
        run: python -m cProfile tools/python/validate.py > profile.txt
```

- **Performance regression detection**: Use tools like pytest-benchmark to detect performance regressions.

```python
import pytest_benchmark

def test_validation_performance(benchmark):
    data = load_test_data()
    benchmark(validate_service, data)
```

### Automation Scripts

- **Automated profiling**: Create scripts to run profilers on key operations and generate reports.

```bash
#!/bin/bash
# profile_validation.sh
python -m cProfile -o profile.prof tools/python/validate.py
python -m pstats profile.prof | head -20 > profile_report.txt
```

- **Continuous monitoring**: Set up cron jobs or scheduled tasks to monitor performance metrics.

```bash
# crontab entry
*/30 * * * * /path/to/performance_monitor.py
```

These performance rules ensure the awesome-free project maintains optimal performance across data processing, validation, and documentation generation tasks. Regular profiling and monitoring should be conducted to identify and address performance bottlenecks proactively.