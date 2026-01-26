# Contributing to awesome-free

Thanks for your interest in improving awesome-free! This document explains how to contribute.

## Adding a New Service

1. **Check if it exists** - Search `services/` to avoid duplicates
2. **Create YAML entry** - Use `.yaml` (not `.yml`) following the schema
3. **File naming** - `services/[category]/[provider-service].yaml` (lowercase)
4. **Use the template** - Copy from an existing entry in same category
5. **Cite sources** - Link to official docs or < 6-month-old sources
6. **Test validation** - Run `python tools/validate.py` to check schema
7. **Open a PR** - Include which fields you verified (not just copy-paste)

## Updating an Existing Service

1. **Verify the change** - Check official docs; don't rely on rumors
2. **Update relevant fields** - Only change what actually changed
3. **Update last_verified** - Set to today's date
4. **Add metadata note** - Explain what changed
5. **Test validation** - Run `python tools/validate.py`
6. **Open a PR** - Cite the source of the change

## Questions / Issues

- **Broken link** - Open an issue with link and when you discovered it
- **Service removed free tier** - Mark in YAML and add to `archive/discontinued.yaml`
- **Wrong information** - Open an issue with correct info + source

## Code of Conduct

Be respectful. We value accuracy over speed. We prioritize users over companies.