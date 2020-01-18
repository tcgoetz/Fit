"""Test FIT file parsing."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import unittest
import logging

from Fit import field_enums
from Fit.manufacturer import Manufacturer
from Fit.product import GarminProduct
from Fit import manufacturer_product_fields as mp_fields


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
        manufacturer = mp_fields.ManufacturerField()
        field_value = manufacturer.convert(Manufacturer.Garmin.value, Manufacturer.invalid.value)
        product = mp_fields.ProductField()
        field_value = product.convert(GarminProduct.Fenix_5_Sapphire.value, GarminProduct.invalid.value)
        self.assertIsInstance(field_value.field, mp_fields.ProductField)
        field_value.field = mp_fields.GarminProductField()
        field_value.reconvert(field_enums.DisplayMeasure.metric)
        self.assertEqual(field_value.value, GarminProduct.Fenix_5_Sapphire)


if __name__ == '__main__':
    unittest.main(verbosity=2)
