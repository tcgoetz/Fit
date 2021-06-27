"""Test conversion functions."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import unittest
import logging
import datetime

from fitfile import conversions


root_logger = logging.getLogger()
handler = logging.FileHandler('conversions.log', 'w')
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)


class TestConversions(unittest.TestCase):
    """Class for testing conversion functions."""

    @classmethod
    def setUpClass(cls):
        pass

    def test_perhour_speed_to_pace(self):
        test_data = [
            (3.0, datetime.time(minute=20)),
            (5.0, datetime.time(minute=12)),
            (7.2, datetime.time(minute=8, second=20))
        ]
        for (speed, pace) in test_data:
            converted_pace = conversions.perhour_speed_to_pace(speed)
            self.assertEqual(converted_pace, pace, f'Bad conversion for speed {speed}')


if __name__ == '__main__':
    unittest.main(verbosity=2)
