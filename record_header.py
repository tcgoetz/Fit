"""Objects that represent a FIT file record header."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import collections
import enum

import data


class MessageClass(enum.Enum):
    """Enum reprersenting the class of a message."""

    data        = 0
    definition  = 1


class RecordHeader(data.Data):
    """Object that represents a FIT file record header."""

    rh_schema = data.Schema('rh', collections.OrderedDict([('record_header', ['UINT8', 1, '%x'])]))
    message_type_string = ['data', 'definition']

    def __init__(self, file):
        """Return a RecordHeader instance created by reading the record geader data from a FIT file."""
        super(RecordHeader, self).__init__(file, self.rh_schema)
        self.message_class = MessageClass(self.message_type())

    def __compressed_timestamp(self):
        return (self.record_header & 0x80) == 0x80

    def message_type(self):
        return (self.record_header & 0x40) == 0x40

    def developer_data(self):
        return (self.record_header & 0x60) == 0x60

    def local_message(self):
        return (self.record_header & 0x0f)

    def __str__(self):
        """Return a string representation of a RecordHeader instance."""
        return ("RecordHeader: Local %s message %d (Compressed %d)" %
                (self.message_class.name, self.local_message(), self.__compressed_timestamp()))

    def __repr__(self):
        """Return a string representation of a RecordHeader instance."""
        return self.__str__()
