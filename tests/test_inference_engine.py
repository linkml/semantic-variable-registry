"""Demo version test."""
import logging
import unittest

import gsvr.transformers.inference_engine as inference_engine
from gsvr.transformers.inference_engine import InferenceEngine
from tests import EXAMPLE_DIR, OUTPUT_DIR

logger = logging.getLogger(inference_engine.__name__)
logger.setLevel(logging.INFO)


class TestInferenceEngine(unittest.TestCase):

    def setUp(self):
        OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

    def test_inference(self):
        base = "VariableCollection-soil"
        ie = InferenceEngine()
        vc = ie.load(EXAMPLE_DIR / f"{base}.yaml")
        vc2 = ie.materialize(vc)
        ie.dump(vc2, OUTPUT_DIR / f"{base}-expanded.yaml")
        vnames = list(vc2.variables.keys())
        cases = [
            ("soil_concentration_nh4_unit_grams_per_kilogram", "g/kg"),
            ("soil_depth_unit_m", "m"),
            ("soil_depth_unit_Inch", "[in_i]"),
        ]
        for vn, ucum_code in cases:
            self.assertIn(vn, vnames)
            v = vc2.variables[vn]
            self.assertEqual(ucum_code, v.unit.ucum_code)



