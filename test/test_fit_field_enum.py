"""Test FIT file parsing."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import unittest
import logging

from fitfile import field_enums
from fitfile import enum_fields


root_logger = logging.getLogger()
handler = logging.FileHandler('fit_field_enum.log', 'w')
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)


class TestFitFieldEnum(unittest.TestCase):
    """Class for testing FIT file parsing."""

    @classmethod
    def setUpClass(cls):
        pass

    def test_field_enum_valid_conversion(self):
        self.assertEqual(field_enums.Switch.from_string('on'), field_enums.Switch.on)

    def test_field_enum_unknown_conversion(self):
        self.assertIsInstance(field_enums.Switch.from_string('junk'), field_enums.UnknownEnumValue)

    def test_field_enum_fuzzy_metric(self):
        self.assertEqual(field_enums.DisplayMeasure.from_string('metric_system'), field_enums.DisplayMeasure.metric)

    def test_field_enum_fuzzy_statute(self):
        self.assertEqual(field_enums.DisplayMeasure.from_string('statute_us'), field_enums.DisplayMeasure.statute)

    def test_enum_field_valid_conversion(self):
        switch = enum_fields.SwitchField('test')
        field_value_list = switch.convert(1, 255)
        self.assertEqual(field_value_list[0]['test'], field_enums.Switch.on)

    def test_enum_field_unknown_conversion(self):
        switch = enum_fields.SwitchField('test')
        field_value_list = switch.convert(10, 255)
        self.assertIsInstance(field_value_list[0]['test'], field_enums.UnknownEnumValue)


if __name__ == '__main__':
    unittest.main(verbosity=2)
