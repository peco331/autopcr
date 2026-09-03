import importlib
import os
import sys
import unittest


repo_root = os.environ.get("AUTOPCR_ROOT")
if repo_root:
    sys.path.insert(0, repo_root)
else:
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


class PydanticRuntimeCompatibilityTest(unittest.TestCase):
    def test_runtime_uses_the_expected_pydantic_v1_api(self):
        import pydantic

        modelbase = importlib.import_module("autopcr.model.modelbase")
        major_version = int(pydantic.VERSION.split(".", 1)[0])

        if major_version >= 2:
            self.assertTrue(modelbase.BaseModel.__module__.startswith("pydantic.v1"))
        else:
            self.assertEqual(modelbase.BaseModel.__module__, "pydantic.main")

    def test_nested_source_ini_response_preserves_json_field_semantics(self):
        modelbase = importlib.import_module("autopcr.model.modelbase")
        sdkrequests = importlib.import_module("autopcr.model.sdkrequests")
        response_type = modelbase.Response[
            sdkrequests.SourceIniGetMaintenanceStatusResponse
        ]

        for data in (
            {"json": 0, "encrypt": 0, "manifest_ver": "202609021434"},
            {"encrypt": 0, "manifest_ver": "202609021434"},
        ):
            with self.subTest(data=data):
                response = response_type.parse_obj(
                    {
                        "data_headers": {"servertime": 1756944000},
                        "data": data,
                    }
                )
                self.assertEqual(response.data.encrypt, 0)
                self.assertEqual(response.data.manifest_ver, "202609021434")


if __name__ == "__main__":
    unittest.main()
