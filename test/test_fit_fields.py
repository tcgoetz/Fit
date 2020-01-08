#!/usr/bin/env python3

"""Test FIT file parsing."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import unittest
import logging
import datetime

from Fit import fields


root_logger = logging.getLogger()
handler = logging.FileHandler('fit_fields.log', 'w')
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)


class TestFitFields(unittest.TestCase):
    """Class for testing FIT file parsing."""

    @classmethod
    def setUpClass(cls):
        pass

    def test_time_ms_field_valid_conversion(self):
        time = fields.TimeMsField('time')
        field_value = time.convert(508324, 4294967295)
        self.assertEqual(field_value.value, datetime.time(0, 8, 28, 324000))

    def __utc_timestamp_field_valid_conversion(self, value, expected_dt):
        time = fields.TimestampField('timestamp', utc=True)
        field_value = time.convert(value, 4294967295)
        self.assertEqual(field_value.value, expected_dt)

    def test_utc_timestamp_field_valid_conversion(self):
        test_values = [
            (936189712, datetime.datetime(2019, 8, 31, 7, 41, 51)),
            (936188666, datetime.datetime(2019, 8, 31, 7, 24, 25)),
            (943190700, datetime.datetime(2019, 11, 20, 8, 24, 59)),
            (857947331, datetime.datetime(2017, 3, 8, 17, 42, 10))
        ]
        for value, expected_dt in test_values:
            self.__utc_timestamp_field_valid_conversion(value, expected_dt)

    def xtest_local_timestamp_field_valid_conversion(self):
        time = fields.TimestampField('timestamp', utc=False)
        field_value = time.convert(936189712, 4294967295)
        self.assertEqual(field_value.value, datetime.datetime(2019, 8, 31, 12, 41, 52))


if __name__ == '__main__':
    unittest.main(verbosity=2)
