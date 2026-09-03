import importlib
import os
import sys
import unittest


repo_root = os.environ.get("AUTOPCR_ROOT")
if repo_root:
    sys.path.insert(0, repo_root)
else:
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


class PydanticV2RuntimeCompatibilityTest(unittest.TestCase):
    def test_models_use_pydantic_v1_compatibility_api(self):
        import pydantic

        self.assertGreaterEqual(int(pydantic.VERSION.split(".", 1)[0]), 2)

        modelbase = importlib.import_module("autopcr.model.modelbase")
        sdkrequests = importlib.import_module("autopcr.model.sdkrequests")

        self.assertTrue(modelbase.BaseModel.__module__.startswith("pydantic.v1"))

        response = sdkrequests.SourceIniGetMaintenanceStatusResponse(
            encrypt=0,
            manifest_ver="202609021434",
        )
        self.assertEqual(response.encrypt, 0)
        self.assertEqual(response.manifest_ver, "202609021434")


if __name__ == "__main__":
    unittest.main()
