"""Test decoding of FIT data messages."""

__author__ = "Philippe Auriach"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import io
import unittest

from fitfile import MeasurementSystem
from fitfile.record_header import RecordHeader
from fitfile.definition_message import DefinitionMessage
from fitfile.data_message import DataMessage, DataMessageDecodeContext


MONITORING = 55
UINT16 = 0x84
UINT32 = 0x86


def decode_message(global_message_number, field_definitions, data, context):
    """Decode a data message from its definition, given as (field number, size, base type) tuples, and its little endian data."""
    definition = bytes([0x40, 0, 0]) + global_message_number.to_bytes(2, 'little') + bytes([len(field_definitions)])
    for field_definition in field_definitions:
        definition += bytes(field_definition)
    file = io.BytesIO(definition + bytes([0x00]) + data)
    definition_message = DefinitionMessage(RecordHeader(file), {}, file)
    RecordHeader(file)
    return DataMessage(definition_message, file, MeasurementSystem.metric, context)


class TestDataMessage(unittest.TestCase):
    """Class for testing FIT data message decoding."""

    def test_timestamp_16_is_relative_to_the_first_one_after_a_timestamp(self):
        context = DataMessageDecodeContext()
        absolute = decode_message(MONITORING, [(253, 4, UINT32)], (1000000000).to_bytes(4, 'little'), context)
        first = decode_message(MONITORING, [(26, 2, UINT16)], (100).to_bytes(2, 'little'), context)
        second = decode_message(MONITORING, [(26, 2, UINT16)], (160).to_bytes(2, 'little'), context)
        self.assertEqual(first.fields.timestamp, absolute.fields.timestamp)
        self.assertEqual((second.fields.timestamp - absolute.fields.timestamp).total_seconds(), 60)

    def test_invalid_timestamp_16_falls_back_to_the_last_timestamp(self):
        context = DataMessageDecodeContext()
        first = decode_message(MONITORING, [(253, 4, UINT32)], (1000000000).to_bytes(4, 'little'), context)
        second = decode_message(MONITORING, [(26, 2, UINT16)], (0xFFFF).to_bytes(2, 'little'), context)
        self.assertEqual(second.fields.timestamp, first.fields.timestamp)


if __name__ == '__main__':
    unittest.main(verbosity=2)
