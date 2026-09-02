"""Test FIT file parsing."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import unittest
import logging

from fitfile import UnknownEnumValue, MeasurementSystem
from fitfile.fields import Switch, SwitchField


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
        self.assertEqual(Switch.from_string('on'), Switch.on)

    def test_field_enum_unknown_conversion(self):
        self.assertIsInstance(Switch.from_string('junk'), UnknownEnumValue)

    def test_field_enum_fuzzy_metric(self):
        self.assertEqual(MeasurementSystem.from_string('metric_system'), MeasurementSystem.metric)

    def test_field_enum_fuzzy_statute(self):
        self.assertEqual(MeasurementSystem.from_string('statute_us'), MeasurementSystem.statute)

    def test_enum_field_valid_conversion(self):
        switch = SwitchField('test')
        field_value_list = switch.convert(1, 255)
        self.assertEqual(field_value_list[0]['test'], Switch.on)

    def test_enum_field_unknown_conversion(self):
        switch = SwitchField('test')
        field_value_list = switch.convert(10, 255)
        self.assertIsInstance(field_value_list[0]['test'], UnknownEnumValue)


if __name__ == '__main__':
    unittest.main(verbosity=2)
