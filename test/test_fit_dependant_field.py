"""Test FIT file parsing."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import unittest
import logging

from fitfile import MeasurementSystem
from fitfile.fields import ProductField, GarminProduct, GarminProductField, SportBasedGradeField, Sport, SubSport
from fitfile.fields.enum_fields.sport import BoulderingFontGradeField, IndoorFontGradeField
from fitfile.fields.sport import ClimbingGradeField



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
        field_value = ProductField().convert(GarminProduct.Fenix_5_Sapphire.value, GarminProduct.invalid.value)[0]
        self.assertEqual(field_value['product'], GarminProduct.Fenix_5_Sapphire.value)
        field_value.field = GarminProductField()
        field_value.reconvert(MeasurementSystem.metric)
        self.assertIsInstance(field_value['product'], GarminProduct)
        self.assertEqual(field_value['product'], GarminProduct.Fenix_5_Sapphire)

    def test_sport_based_grade_field_dependant_field(self):
        grade = SportBasedGradeField('grade')
        self.assertIsInstance(grade.dependant_field([Sport.rock_climbing, SubSport.bouldering]), BoulderingFontGradeField)
        self.assertIsInstance(grade.dependant_field([Sport.rock_climbing, SubSport.indoor_climbing]), IndoorFontGradeField)
        self.assertIsInstance(grade.dependant_field([Sport.rock_climbing, None]), ClimbingGradeField)
        self.assertIsInstance(grade.dependant_field([Sport.running, None]), ClimbingGradeField)


if __name__ == '__main__':
    unittest.main(verbosity=2)
