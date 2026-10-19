"""Test FIT file parsing."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import unittest
import io
import logging
import datetime
from unittest import mock

from fitfile import fields, MeasurementSystem
from fitfile.record_header import RecordHeader
from fitfile.definition_message import DefinitionMessage
from fitfile.data_message import DataMessage, DataMessageDecodeContext


root_logger = logging.getLogger()
handler = logging.FileHandler('fit_fields.log', 'w')
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)


RECORD = 20
SINT8 = 0x01
UINT8 = 0x02
UINT16 = 0x84
UINT32 = 0x86


def read_messages(field_definitions, data, byte_order):
    """Return the definition message and the data message read from a record message definition followed by its data."""
    definition = bytes([0x40, 0, byte_order == 'big']) + RECORD.to_bytes(2, byte_order) + bytes([len(field_definitions)])
    for field_definition in field_definitions:
        definition += bytes(field_definition)
    file = io.BytesIO(definition + bytes([0x00]) + data)
    definition_message = DefinitionMessage(RecordHeader(file), {}, file)
    RecordHeader(file)
    return definition_message, DataMessage(definition_message, file, MeasurementSystem.metric, DataMessageDecodeContext())


class TestFitFields(unittest.TestCase):
    """Class for testing FIT file parsing."""

    @classmethod
    def setUpClass(cls):
        pass

    def test_single_read_decoding_matches_field_by_field_decoding(self):
        # timestamp, heart rate, distance, speed, temperature and an unknown field holding four values
        field_definitions = [(253, 4, UINT32), (3, 1, UINT8), (5, 4, UINT32), (6, 2, UINT16), (13, 1, SINT8), (200, 4, UINT8)]
        for byte_order in ('little', 'big'):
            data = ((1000000000).to_bytes(4, byte_order) + bytes([142]) + (123456).to_bytes(4, byte_order) + (3210).to_bytes(2, byte_order)
                    + (-5).to_bytes(1, byte_order, signed=True) + bytes([1, 2, 255, 4]))
            definition_message, single_read = read_messages(field_definitions, data, byte_order)
            self.assertIsNotNone(definition_message.decode_plan())
            with mock.patch.object(DefinitionMessage, 'decode_plan', return_value=None):
                _, field_by_field = read_messages(field_definitions, data, byte_order)
            self.assertEqual(single_read.fields.heart_rate, 142)
            self.assertEqual(single_read.fields, field_by_field.fields)
            self.assertEqual(repr(single_read.field_values), repr(field_by_field.field_values))
            self.assertEqual(single_read.file_size, field_by_field.file_size)

    def test_fields_that_do_not_fill_their_size_are_decoded_one_at_a_time(self):
        definition_message, _ = read_messages([(3, 1, UINT8), (6, 3, UINT16)], bytes([142, 1, 2, 3]), 'little')
        self.assertIsNone(definition_message.decode_plan())

    def test_time_ms_field_valid_conversion(self):
        time = fields.TimeMsField('time')
        field_value_list = time.convert(508324, 4294967295)
        self.assertEqual(field_value_list[0]['time'], datetime.time(0, 8, 28, 324000))

    def __utc_timestamp_field_valid_conversion(self, value, expected_dt):
        time = fields.TimestampField('timestamp', utc=True)
        field_value_list = time.convert(value, 4294967295)
        self.assertEqual(field_value_list[0]['timestamp'], expected_dt)

    def test_utc_timestamp_field_valid_conversion(self):
        test_values = [
            (936189712, datetime.datetime(2019, 8, 31, 12, 41, 52, tzinfo=datetime.timezone.utc)),
            (936188666, datetime.datetime(2019, 8, 31, 12, 24, 26, tzinfo=datetime.timezone.utc)),
            (943190700, datetime.datetime(2019, 11, 20, 13, 25, 0, tzinfo=datetime.timezone.utc)),
            (857947331, datetime.datetime(2017, 3, 8, 22, 42, 11, tzinfo=datetime.timezone.utc))
        ]
        for value, expected_dt in test_values:
            self.__utc_timestamp_field_valid_conversion(value, expected_dt)

    def test_local_timestamp_field_valid_conversion(self):
        time = fields.TimestampField('timestamp', utc=False)
        field_value_list = time.convert(936189712, 4294967295)
        self.assertEqual(field_value_list[0]['timestamp'], datetime.datetime(2019, 8, 31, 12, 41, 52))

    def test_object_field_converts_every_value_of_an_array(self):
        speed = fields.SpeedMpsField('speed_1s')
        self.assertEqual(speed.convert([255, 255, 255], 255)[0]['speed_1s'], [None, None, None])
        values = speed.convert([1000, 255, 2000], 255)[0]['speed_1s']
        self.assertEqual(values[1], None)
        self.assertEqual(values[2], 2 * values[0])
        self.assertEqual(values[0], speed.convert(1000, 255)[0]['speed_1s'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
