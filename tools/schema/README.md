# Schema Documentation

This directory contains JSON Schema files used to validate the YAML files in the awesome-free repository.

## Files

### service.schema.json

Validates service YAML files located in `services/[category]/[service-name].yaml`.

The schema ensures that each service entry follows the standardized structure with all required fields for accurate and complete service information.

**Key validations:**
- Required fields: id, name, provider, category, url, free_tier, regions, gotchas, best_for, not_for, complementary_services, cost, requirements, resources, metadata, flags
- Category must be one of: compute, database, storage, cdn-edge, serverless, devtools, communication, ai-ml, creative, web3
- Free tier type must be one of: always-free, time-limited-trial, credits, mixed
- Dates must be in YYYY-MM-DD format
- URLs must be valid URIs
- Flags use enumerated values (low/medium/high)

### stack.schema.json

Validates stack YAML files located in `stacks/[category]/[stack-name].yaml`.

The schema ensures that stack entries provide complete reference architectures combining multiple services.

**Key validations:**
- Required fields: name, category, description, services, total_monthly_cost, estimated_capacity, pros, cons, alternatives, getting_started, resources
- Services array contains objects with service_id, role, config, free_estimate
- Alternatives array contains comparison objects with name, cost, pros, cons
- Resources are valid URIs

## Usage

These schemas are used by the validation tools in `tools/python/validate.py` to ensure data quality and consistency across the repository.

Run validation with:
```bash
python tools/python/validate.py
```

## Schema Standards

- Based on JSON Schema Draft 07
- Strict validation to prevent incomplete entries
- Enumerated values for consistency
- URI format validation for links
- Date format validation for freshness tracking