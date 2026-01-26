import pytest
import tempfile
import os
import json
import yaml
from jsonschema import ValidationError

from tools.python.validate import load_schema, validate_yaml_file


@pytest.fixture
def sample_service_schema():
    """Fixture providing a minimal service schema for testing."""
    return {
        "$schema": "https://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "service": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "provider": {"type": "string"},
                    "category": {
                        "type": "string",
                        "enum": ["compute", "database", "storage", "cdn-edge", "serverless"]
                    },
                    "url": {"type": "string", "format": "uri"},
                    "free_tier": {
                        "type": "object",
                        "properties": {
                            "type": {"type": "string", "enum": ["always-free", "time-limited-trial", "credits"]}
                        },
                        "required": ["type"]
                    },
                    "regions": {"type": "object"},
                    "gotchas": {"type": "array", "items": {"type": "string"}},
                    "best_for": {"type": "array", "items": {"type": "string"}},
                    "not_for": {"type": "array", "items": {"type": "string"}},
                    "complementary_services": {"type": "array"},
                    "cost": {"type": "object"},
                    "requirements": {"type": "object"},
                    "resources": {"type": "object"},
                    "metadata": {
                        "type": "object",
                        "properties": {
                            "last_verified": {"type": "string", "pattern": r"^\d{4}-\d{2}-\d{2}$"}
                        },
                        "required": ["last_verified"]
                    },
                    "flags": {"type": "object"}
                },
                "required": ["id", "name", "provider", "category", "url", "free_tier", "regions",
                           "gotchas", "best_for", "not_for", "complementary_services", "cost",
                           "requirements", "resources", "metadata", "flags"]
            }
        },
        "required": ["service"]
    }


@pytest.fixture
def valid_service_data():
    """Fixture providing valid service data."""
    return {
        "service": {
            "id": "test-service",
            "name": "Test Service",
            "provider": "Test Provider",
            "category": "compute",
            "url": "https://example.com",
            "free_tier": {
                "type": "always-free"
            },
            "regions": {"always_free": ["Global"]},
            "gotchas": ["Test gotcha"],
            "best_for": ["Testing"],
            "not_for": ["Production"],
            "complementary_services": [],
            "cost": {"under_free_tier": "$0"},
            "requirements": {"credit_card": False},
            "resources": {"official_docs": "https://example.com/docs"},
            "metadata": {"last_verified": "2024-01-01"},
            "flags": {
                "time_sensitive": False,
                "cost_risk": "low",
                "vendor_lock_in": "low",
                "learning_curve": "low",
                "setup_time": 5
            }
        }
    }


@pytest.fixture
def invalid_service_data():
    """Fixture providing invalid service data (missing required fields)."""
    return {
        "service": {
            "id": "test-service",
            "name": "Test Service"
            # Missing many required fields
        }
    }


@pytest.fixture
def invalid_yaml_content():
    """Fixture providing invalid YAML content."""
    return """
service:
  id: test
  - invalid: yaml: structure
  name: test
"""


class TestLoadSchema:
    """Test cases for load_schema function."""

    def test_load_valid_schema(self, sample_service_schema, tmp_path):
        """Test loading a valid JSON schema file."""
        schema_file = tmp_path / "test_schema.json"
        with open(schema_file, 'w') as f:
            json.dump(sample_service_schema, f)

        schema = load_schema(str(schema_file))
        assert schema == sample_service_schema
        assert "$schema" in schema

    def test_load_nonexistent_schema(self):
        """Test loading a nonexistent schema file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            load_schema("nonexistent.json")

    def test_load_invalid_json_schema(self, tmp_path):
        """Test loading invalid JSON raises JSONDecodeError."""
        schema_file = tmp_path / "invalid.json"
        with open(schema_file, 'w') as f:
            f.write("invalid json content {")

        with pytest.raises(json.JSONDecodeError):
            load_schema(str(schema_file))


class TestValidateYamlFile:
    """Test cases for validate_yaml_file function."""

    def test_validate_valid_yaml_file(self, valid_service_data, sample_service_schema, tmp_path):
        """Test validating a valid YAML file against schema."""
        yaml_file = tmp_path / "valid.yaml"
        with open(yaml_file, 'w') as f:
            yaml.dump(valid_service_data, f)

        is_valid, error = validate_yaml_file(str(yaml_file), sample_service_schema)
        assert is_valid is True
        assert error is None

    def test_validate_invalid_yaml_file(self, invalid_service_data, sample_service_schema, tmp_path):
        """Test validating an invalid YAML file against schema."""
        yaml_file = tmp_path / "invalid.yaml"
        with open(yaml_file, 'w') as f:
            yaml.dump(invalid_service_data, f)

        is_valid, error = validate_yaml_file(str(yaml_file), sample_service_schema)
        assert is_valid is False
        assert "Validation Error" in error

    def test_validate_malformed_yaml_file(self, invalid_yaml_content, sample_service_schema, tmp_path):
        """Test validating a malformed YAML file."""
        yaml_file = tmp_path / "malformed.yaml"
        with open(yaml_file, 'w') as f:
            f.write(invalid_yaml_content)

        is_valid, error = validate_yaml_file(str(yaml_file), sample_service_schema)
        assert is_valid is False
        assert "YAML Error" in error

    def test_validate_nonexistent_yaml_file(self, sample_service_schema):
        """Test validating a nonexistent YAML file."""
        is_valid, error = validate_yaml_file("nonexistent.yaml", sample_service_schema)
        assert is_valid is False
        assert "No such file or directory" in error

    def test_validate_with_invalid_schema(self, valid_service_data, tmp_path):
        """Test validating with an invalid schema."""
        yaml_file = tmp_path / "valid.yaml"
        with open(yaml_file, 'w') as f:
            yaml.dump(valid_service_data, f)

        invalid_schema = {"type": "invalid"}
        is_valid, error = validate_yaml_file(str(yaml_file), invalid_schema)
        assert is_valid is False
        assert "Schema Error" in error


# Note: Testing the main() function is complex as it depends on the file system structure
# and prints output. For unit testing, we focus on the core functions above.
# Integration tests could be added separately to test the main function.