"""Test FIT file parsing."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import unittest
import logging

from fitfile import field_enums
from fitfile.product import GarminProduct
from fitfile import manufacturer_product_fields as mp_fields


root_logger = logging.getLogger()
handler = logging.FileHandler('fit_field_enum.log', 'w')
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)


class TestFitDependantField(unittest.TestCase):
    """Class for testing FIT file parsing."""

    @classmethod
    def setUpClass(cls):
        pass

    def test_product_field_reconvert(self):
        field_value = mp_fields.ProductField().convert(GarminProduct.Fenix_5_Sapphire.value, GarminProduct.invalid.value)[0]
        self.assertEqual(field_value['product'], GarminProduct.Fenix_5_Sapphire.value)
        field_value.field = mp_fields.GarminProductField()
        field_value.reconvert(field_enums.DisplayMeasure.metric)
        self.assertIsInstance(field_value['product'], mp_fields.GarminProduct)
        self.assertEqual(field_value['product'], GarminProduct.Fenix_5_Sapphire)


if __name__ == '__main__':
    unittest.main(verbosity=2)
