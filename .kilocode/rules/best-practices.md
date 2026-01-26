# Best Practices for Awesome-Free Project

This document outlines comprehensive best practices for the awesome-free project. These guidelines ensure high-quality code, reliable data curation, and ethical maintenance of the free services collection. The practices are tailored to the project's focus on curating legitimate free-tier cloud services while maintaining technical excellence and community trust.

## Project Philosophy and Values

### Core Mission
Provide a single source of truth for developers, creators, and builders to discover and strategically combine free offerings into production-grade systems without vendor lock-in or unexpected costs.

### Core Values
1. **Accuracy** - Only cite official docs or credible sources < 6 months old
2. **Completeness** - Include gotchas, regional constraints, and cost traps (not just benefits)
3. **Usability** - Services organized by category, easy to search and compare
4. **Currency** - Flag outdated entries; automated weekly freshness checks
5. **Community** - Welcoming contributions; clear guidelines for additions/updates
6. **No Ads/Affiliates** - Pure curation, no sponsor preference or affiliate links

### What We Cover
- **Infrastructure**: Compute, databases, storage, networking (AWS, GCP, Azure, Oracle, Cloudflare, Fly.io, Railway, etc.)
- **Application Platforms**: Web hosting, serverless, FaaS (Vercel, Netlify, Render, Fly.io, Heroku alternatives)
- **Developer Tools**: CI/CD, monitoring, testing, security scanning (GitHub Actions, Sentry, Datadog, etc.)
- **Communication**: Email, SMS, chat APIs (SendGrid, Mailgun, Twilio, Discord)
- **AI/ML**: Model hosting, inference, fine-tuning (Hugging Face Spaces, Replicate, Together AI)
- **Creative Tools**: Open-source software with free tiers (Blender, GIMP, Krita, etc.)
- **Web3/Blockchain**: If applicable (IPFS, Arweave, etc.)

### What We DON'T Cover
- Services with no free tier whatsoever
- Illegal or pirated software
- Services requiring Darkweb access
- Spam/scam services
- Abandoned projects (no updates > 2 years)

## Code Quality Standards

### DRY (Don't Repeat Yourself)
- Eliminate code duplication by creating reusable functions for common operations
- Extract shared validation logic into utility modules
- Use configuration files instead of hardcoding repeated values

**Example**: Instead of duplicating URL validation regex across multiple scripts, create a `validators.py` module with a `validate_url()` function used by link_checker.py and validate.py.

### YAGNI (You Ain't Gonna Need It)
- Implement only features that are immediately needed
- Avoid speculative features like advanced analytics unless requested
- Focus on core functionality: service validation, data export, and documentation generation

**Example**: Don't add complex filtering options to export tools until users specifically request them. Start with basic JSON/CSV export functionality.

### Single Responsibility Principle
- Keep functions small and focused on one task
- Create separate modules for distinct concerns (validation, export, generation)
- Avoid monolithic scripts that handle multiple unrelated operations

**Example**: Split `validate.py` into focused functions: `validate_service_schema()`, `validate_service_links()`, `validate_service_freshness()` instead of one large validation function.

### Code Readability and Maintainability
- Use descriptive variable and function names that explain purpose
- Add docstrings to all public functions with parameters, return values, and examples
- Write self-documenting code with clear logic flow

**Example**:
```python
def validate_service_freshness(service_data: Dict[str, Any], max_age_days: int = 90) -> bool:
    """Validate that service documentation was checked within the specified timeframe.

    Args:
        service_data: Service definition dictionary
        max_age_days: Maximum allowed age in days for freshness checks

    Returns:
        True if service is fresh, False if it needs re-checking
    """
    last_checked = service_data.get('metadata', {}).get('last_verified')
    if not last_checked:
        return False
    # Implementation...
```

## Code Structure and Organization

### Modular Architecture
- Organize code into logical packages: `validators/`, `exporters/`, `generators/`
- Keep the root tools/python/ directory flat with clear entry points
- Use relative imports for internal modules

**Example Structure**:
```
tools/python/
├── validators/
│   ├── __init__.py
│   ├── service_validator.py
│   └── link_validator.py
├── exporters/
│   ├── __init__.py
│   ├── json_exporter.py
│   └── csv_exporter.py
├── generators/
│   ├── __init__.py
│   └── markdown_generator.py
├── main scripts like validate.py, export_json.py, etc.
```

### Consistent Naming Conventions
- Use snake_case for modules, functions, and variables
- Use PascalCase for classes (e.g., `ServiceValidator`)
- Prefix private functions with underscore (e.g., `_validate_url_format()`)
- Use descriptive names: `check_service_links()` instead of `validate()`

### Configuration Management
- Store configuration in dedicated files (config.yaml, settings.py)
- Use environment variables for sensitive or environment-specific settings
- Avoid hardcoding paths, URLs, or thresholds in code

**Example**: Create `config/settings.py` with:
```python
DEFAULT_MAX_LINK_AGE_DAYS = 90
SUPPORTED_CATEGORIES = ['compute', 'storage', 'database', 'cdn-edge']
OFFICIAL_DOCS_TIMEOUT = 30  # seconds
```

## Error Handling and Logging

### Structured Error Handling
- Use specific exception types instead of generic Exception
- Implement proper error propagation in async operations
- Provide meaningful error messages for debugging

**Example**:
```python
class ValidationError(Exception):
    """Raised when service validation fails."""
    pass

def validate_service(service_data):
    try:
        # validation logic
        if not service_data.get('name'):
            raise ValidationError("Service name is required")
    except KeyError as e:
        raise ValidationError(f"Missing required field: {e}") from e
```

### Logging Standards
- Use structured logging with consistent formats
- Include contextual information (service name, operation type, timestamps)
- Log at appropriate levels: DEBUG for detailed info, INFO for normal operations, WARNING for issues, ERROR for failures

**Example**:
```python
import logging

logger = logging.getLogger(__name__)

def check_service_links(service_data):
    service_name = service_data['name']
    logger.info(f"Checking links for service: {service_name}")

    for url in service_data.get('documentation', []):
        try:
            # check logic
            logger.debug(f"Successfully validated URL: {url}")
        except requests.RequestException as e:
            logger.warning(f"Failed to validate URL {url} for {service_name}: {e}")
```

### Graceful Degradation
- Handle network failures by falling back to cached data
- Continue processing other services when one fails
- Provide partial results when complete validation isn't possible

**Example**: In link_checker.py, if a URL times out, log the error but continue checking other URLs and mark the service as needing manual review.

## Domain-Specific Best Practices

### Service Accuracy and Verification
- Cross-reference all service claims with official provider documentation
- Verify free tier limits, features, and restrictions against multiple sources
- Document verification sources and dates in service metadata

**Example**: For a storage service claiming "5GB free", check the official pricing page, terms of service, and user forums to confirm the exact limits and any hidden costs.

### When Uncertain Guidelines
- Mark with [NEEDS_VERIFICATION]
- Cite the source (even if you're unsure)
- Flag in metadata for community review
- Ask for official documentation link
- Don't guess on limits or pricing
- Check the service's official pricing page first

### Free Tier Integrity
- Flag any service requiring payment information for "free" access
- Verify that free tiers are truly unlimited in time (not time-limited trials)
- Document any usage limits, rate limits, or feature restrictions clearly

**Example**: Reject services that require credit card verification for free signup, as this violates the "truly free" principle. Instead, highlight services with genuine free tiers like AWS Free Tier or Google Cloud Free Tier.

### Community Curation
- Encourage community contributions through clear contribution guidelines
- Implement review processes for new service submissions
- Maintain transparency about curation decisions and criteria

**Example**: Use GitHub Issues for service suggestions with a template that requires submitters to provide official documentation links and verification evidence.

### Contribution Workflow

When you generate issues or PR templates for contributors:

#### New Service
- Link to schema
- Checklist of required fields
- Example YAML entry
- Link to provider's free tier page
- Request: "Create services/[category]/[service-id].yaml"

#### Update Service
- What changed (pricing, limits, regions)?
- Updated YAML fields
- New last_verified date
- Note in metadata about change
- Request: "Update services/[category]/[service-id].yaml"

#### Broken Link
- Which service/link is broken?
- When did you last verify it worked?
- Suggested fix

### Data Integrity and Freshness
- Implement automated freshness checks for service documentation
- Regularly review and update service definitions based on provider changes
- Archive discontinued services with clear discontinuation notices

**Example**: Run weekly automated checks using freshness_check.py to identify services whose documentation hasn't been verified in 90+ days, then manually review and update as needed.

### Ethical and Transparency Rules
- Clearly disclose any affiliations or sponsorships
- Maintain neutral, factual descriptions without marketing language
- Prioritize user benefit over provider relationships

**Example**: When describing services, use objective language like "Provides 5GB of free object storage" instead of promotional phrases like "The best free storage solution available".

### Stack Composition
- Ensure stack components are all legitimately free and compatible
- Document integration requirements and potential limitations
- Test stack combinations for real-world viability

**Example**: For a "static site hosting stack", verify that all components (CDN, storage, CI/CD) offer free tiers that work together without requiring paid upgrades for basic functionality.

### Automation and Monitoring
- Automate repetitive tasks like link checking and validation
- Monitor for service changes and provider policy updates
- Implement alerts for validation failures or data inconsistencies

**Example**: Set up GitHub Actions to run validation scripts on pull requests and weekly freshness checks, with notifications to maintainers for any failures.

### Automation & Scripts

When asked to generate tools:

#### Validation (validate.py)
- Load all YAML
- Validate against schema
- Check date freshness
- Verify links (optional, expensive)
- Report errors with line numbers

#### Comparison (compare.py)
- Side-by-side provider comparison
- Filter by category, cost, features
- Output formatted table (markdown, CSV, JSON)

#### Export (export_csv.py, export_json.py)
- Convert services to portable formats
- Include all fields, flatten nested objects
- Sort by category

#### GitHub Actions (.github/workflows/)
- Validate schema on every PR
- Run scheduled checks (weekly for freshness)
- Output nice formatting (comment on PR with results)
- Cache dependencies to speed up runs
- Use standard actions (actions/checkout, actions/setup-python)

### Documentation Maintenance
- Keep documentation synchronized with code changes
- Update examples and tutorials as tools evolve
- Maintain version consistency across README, docs, and code

**Example**: When adding a new validation rule to validate.py, simultaneously update docs/EVALUATION_CRITERIA.md and any relevant code comments to reflect the change.

## Success Criteria

A successful awesome-free repo will:

- Contain 200+ services within 6 months (all major cloud providers + common tools)
- Have < 5% broken links (validated weekly)
- Keep 95% of entries fresh (last_verified within 180 days)
- Support 10+ categories (compute, database, storage, cdn, serverless, devtools, comms, ai/ml, creative, web3)
- Enable users to build production systems on free tiers alone
- Provide clear cost comparison (always-free vs credits vs trials)
- Highlight gotchas more than benefits (balanced evaluation)
- Be automated (CI/CD validates, links check, exports generate)
- Be community-driven (clear contribution process, responsive reviews)
- Remain vendor-neutral (no affiliate links, no sponsor bias)

These best practices ensure the awesome-free project maintains high standards of quality, reliability, and ethical curation while supporting its mission of helping developers discover legitimate free cloud services.