# Generated Data Files

The files in this `data/` directory are automatically generated from the service definitions in the `services/` directory.

## Files

- `services.csv` - CSV export of all services with key metadata
- `services.json` - JSON export of all services following the service schema
- `comparison.md` - Markdown table comparing all services

## Generation

These files are generated using scripts in the `tools/` directory:

- `tools/python/export_csv.py` - Generates services.csv
- `tools/python/export_json.py` - Generates services.json
- `tools/python/generate_markdown.py` - Generates comparison.md

## Important Notes

- **Do not edit these files manually** - they will be overwritten on next generation
- If you need to modify service data, edit the YAML files in `services/` directory
- Run the generation scripts after making changes to service definitions

## Last Generated

*This file was last updated: [Date will be updated by generation script]*