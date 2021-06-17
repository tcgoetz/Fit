"""Manages FIT file format base types."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


class BaseType():
    """Manages FIT file format base types."""

    __base_type_data = {
        0x00 : [False, 'enum',     0xFF,               'UINT8'],
        0x01 : [False, 'sint8',    0x7F,               'INT8'],
        0x02 : [False, 'uint8',    0xFF,               'UINT8'],
        0x07 : [False, 'string',   0x00,               'CHAR'],
        0x83 : [True,  'sint16',   0x7FFF,             'INT16'],
        0x84 : [True,  'uint16',   0xFFFF,             'UINT16'],
        0x85 : [True,  'sint32',   0x7FFFFFFF,         'INT32'],
        0x86 : [True,  'uint32',   0xFFFFFFFF,         'UINT32'],
        0x88 : [True,  'float32',  0xFFFFFFFF,         'FLOAT32'],
        0x89 : [True,  'float64',  0xFFFFFFFFFFFFFFFF, 'FLOAT64'],
        0x0a : [False, 'uint8z',   0x00,               'UINT8'],
        0x8b : [True,  'uint16z',  0x00000000,         'UINT16'],
        0x8c : [True,  'uint32z',  0x00000000,         'UINT32'],
        0x0d : [False, 'byte',     0xFF,               'UINT8'],
        0x8e : [True,  'sint64',   0x7FFFFFFFFFFFFFFF, 'INT64'],
        0x8f : [True,  'uint64',   0xFFFFFFFFFFFFFFFF, 'UINT64'],
        0x90 : [True,  'uint64z',  0x0000000000000000, 'UINT64'],
    }
    index_endian = 0
    index_name = 1
    index_invalid = 2
    index_string = 3

    @classmethod
    def __base_type(cls, index):
        try:
            return cls.__base_type_data[index]
        except Exception:
            raise IndexError(f'Unknown base type index {index}')

    @classmethod
    def _type_endian(cls, index):
        return cls.__base_type(index)[cls.index_endian]

    @classmethod
    def type_name(cls, index):
        """Return the name for a type given it's index."""
        return cls.__base_type(index)[cls.index_name]

    @classmethod
    def _invalid(cls, index):
        """Return the invalid value for a type given it's index."""
        return cls.__base_type(index)[cls.index_invalid]

    @classmethod
    def _type_string(cls, index):
        """Return the name of a type given it's index."""
        return cls.__base_type(index)[cls.index_string]
