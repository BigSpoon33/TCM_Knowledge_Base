# tests/test_models/test_template.py

import unittest
from pathlib import Path
import tempfile
from capsule.models.template import TemplateSchema

class TestTemplateSchema(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)
        self.schema_data = {
            "domain_type": "TCM",
            "version": "1.0",
            "required_fields": ["name", "category"],
            "optional_fields": ["sub_category", "meridian"],
            "domain_sections": {
                "herbs": {
                    "type": "list",
                    "schema": "herb_schema"
                },
                "formulas": {
                    "type": "list",
                    "schema": "formula_schema"
                }
            }
        }
        self.schema = TemplateSchema(**self.schema_data)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_initialization(self):
        self.assertEqual(self.schema.domain_type, "TCM")
        self.assertEqual(self.schema.version, "1.0")
        self.assertListEqual(self.schema.required_fields, ["name", "category"])

    def test_to_dict(self):
        self.assertDictEqual(self.schema.to_dict(), self.schema_data)

    def test_to_from_yaml_file(self):
        file_path = self.temp_path / "schema.yaml"
        self.schema.to_yaml_file(file_path)
        self.assertTrue(file_path.exists())

        loaded_schema = TemplateSchema.from_yaml_file(file_path)
        self.assertEqual(self.schema, loaded_schema)

    def test_validate_structure_success(self):
        valid_data = {
            "name": "Some Name",
            "category": "Some Category",
            "meridian": "Some Meridian"
        }
        self.assertTrue(self.schema.validate_structure(valid_data))

    def test_validate_structure_failure(self):
        invalid_data = {
            "name": "Some Name",
            "meridian": "Some Meridian"
        }
        self.assertFalse(self.schema.validate_structure(invalid_data))

    def test_empty_and_default_fields(self):
        schema = TemplateSchema(domain_type="Minimal", version="0.1")
        self.assertEqual(schema.domain_type, "Minimal")
        self.assertEqual(schema.version, "0.1")
        self.assertListEqual(schema.required_fields, [])
        self.assertListEqual(schema.optional_fields, [])
        self.assertDictEqual(schema.domain_sections, {})

if __name__ == "__main__":
    unittest.main()
