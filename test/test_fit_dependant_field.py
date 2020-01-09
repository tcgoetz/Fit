#!/usr/bin/env python3

"""Test FIT file parsing."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import unittest
import logging

from Fit import field_enums
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
        field_value = manufacturer.convert(field_enums.Manufacturer.Garmin.value, field_enums.Manufacturer.invalid.value)
        product = mp_fields.ProductField()
        field_value = product.convert(field_enums.GarminProduct.Fenix_5_Sapphire.value, field_enums.GarminProduct.invalid.value)
        self.assertIsInstance(field_value.field, mp_fields.ProductField)
        field_value.field = mp_fields.GarminProductField()
        field_value.reconvert(field_enums.DisplayMeasure.metric)
        self.assertEqual(field_value.value, field_enums.GarminProduct.Fenix_5_Sapphire)


if __name__ == '__main__':
    unittest.main(verbosity=2)
