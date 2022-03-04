"""Given a schema, unpack FIT file encoded data into a Python object."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import struct
import logging
import enum


logger = logging.getLogger(__name__)


class Architecture(enum.Enum):
    """The endian type that the FIT file was encoded with."""

    Little_Endian   = 0
    Big_Endian      = 1


class Schema():
    """Describes how the data of a FIT file object is encoded."""

    type_to_size = {
        'CHAR': 1,
        'INT8': 1,
        'UINT8': 1,
        'INT16': 2,
        'UINT16': 2,
        'INT32': 4,
        'UINT32': 4,
        'INT64': 8,
        'UINT64': 8,
        'FLOAT32': 4,
        'FLOAT64': 4
    }

    __type_to_unpack_format = {
        'CHAR': 'B',
        'INT8': 'b',
        'UINT8': 'B',
        'INT16': 'h',
        'UINT16': 'H',
        'INT32': 'i',
        'UINT32': 'I',
        'INT64': 'q',
        'UINT64': 'Q',
        'FLOAT32': 'f',
        'FLOAT64': 'd'
    }

    def __init__(self, name, ordered_dict):
        """Return a message schema given it's name and an ordered dict of its fields."""
        self.name = name
        self.ordered_dict = ordered_dict
        self.file_size = [0, 0]
        self.unpack_format = [None, None]

    def __compile_unpack(self, endian):
        if endian is Architecture.Big_Endian:
            unpack_format = '>'
        else:
            unpack_format = ''
        for key in self.ordered_dict:
            (type, count) = self.ordered_dict[key]
            for _ in range(count):
                unpack_format += self.__type_to_unpack_format[type]
                self.file_size[endian.value] += self.type_to_size[type]
        self.unpack_format[endian.value] = unpack_format

    def get_unpack(self, endian):
        """Get a compiled unpack format for this schema."""
        if self.unpack_format[endian.value] is None:
            self.__compile_unpack(endian)
        return (self.unpack_format[endian.value], self.file_size[endian.value])

    def _decode(self, data):
        """Create a dict of message fields given a bytesarray."""
        decoded_data = {}
        index = 0
        for (key, (_, count)) in self.ordered_dict.items():
            if count > 1:
                decoded_data[key] = [data[index + repeat] for repeat in range(count)]
                index += count
            elif count == 1:
                decoded_data[key] = data[index]
                index += 1
        return decoded_data


class Data():
    """The base object for decoding FIT file data."""

    def __init__(self, file, primary_schema, secondary_schemas=None, endian=Architecture.Little_Endian):
        """Return a Data instance created by parsing data from a FIT file."""
        self.file = file
        self.primary_schema = primary_schema
        self.secondary_schemas = secondary_schemas
        self.endian = endian
        self.file_size = 0
        self.decode_all()
        self._convert()

    def _decode(self, schema):
        """Given a schema decode file data into fields and add them as properties of the data object."""
        (unpack_format, file_size) = schema.get_unpack(self.endian)
        self.file_size += file_size
        bytes = struct.unpack(unpack_format, self.file.read(file_size))
        vars(self).update(schema._decode(bytes))

    def decode_all(self):
        """Decode file data using all of the data objects schemas."""
        self._decode(self.primary_schema)
        if self.secondary_schemas is not None:
            for schema, control_func in self.secondary_schemas:
                if control_func():
                    self._decode(schema)

    def _convert(self):
        pass
