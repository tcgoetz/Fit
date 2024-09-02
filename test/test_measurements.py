#!/usr/bin/env python3

"""Test measurement parsing."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import unittest
import logging

from fitfile import Distance, Weight, Temperature, Speed


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

    def test_distance_from_func(self):
        self.assertEqual(Distance.from_func('km'), Distance.from_kilometers)
        self.assertEqual(Distance.from_func('Kilometers'), Distance.from_kilometers)
        self.assertEqual(Distance.from_func('Feet'), Distance.from_feet)
        self.assertEqual(Distance.from_func('MeterS'), Distance.from_meters)

    def test_speed_from_func(self):
        self.assertEqual(Speed.from_func('KPH'), Speed.from_kph)
        self.assertEqual(Speed.from_func('Mph'), Speed.from_mph)

    def test_weight(self):
        weight = Weight.from_grams(100000)
        self.assertEqual(weight.value, 100.0)
        self.assertAlmostEqual(weight.to_lbs(), 220.46, 2)

    def test_temperature(self):
        temp = Temperature.from_celsius(100.0)
        self.assertEqual(temp.value, 100.0)
        self.assertEqual(temp.to_f(), 212.0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
