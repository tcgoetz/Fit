#!/usr/bin/env python3

"""Test measurement parsing."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import unittest
import logging

from Fit import Distance


root_logger = logging.getLogger()
handler = logging.FileHandler('measurment.log', 'w')
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)


class TestMeasurement(unittest.TestCase):
    """Class for testing measurment parsing."""

    @classmethod
    def setUpClass(cls):
        pass

    def test_distance(self):
        distance = Distance.from_mm(1000000)
        self.assertEqual(distance.value, 1000.0)
        self.assertEqual(distance.to_mm(), 1000000.0)
        self.assertEqual(distance.to_meters(), 1000.0)
        self.assertEqual(distance.to_kms(), 1.0)
        self.assertEqual(distance.to_mm(), 1000000)
        self.assertEqual(distance.to_miles(), 0.6213712)


if __name__ == '__main__':
    unittest.main(verbosity=2)
