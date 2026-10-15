"""FIT file definition message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import collections
import struct

from .data import Schema, Data, Architecture
from .fields import UnknownField
from .developer_field_definition import DeveloperFieldDefinition
from .definition_message_data import DefinitionMessageData
from .field_definition import FieldDefinition
from .message_type import MessageType


class DefinitionMessage(Data):
    """FIT file definition message."""

    dm_primary_schema = Schema(
        'dm_primary',
        collections.OrderedDict(
            [
                ('reserved', ['UINT8', 1]),
                ('architecture', ['UINT8', 1])
            ]
        )
    )
    dm_secondary_schema = Schema(
        'dm_secondary',
        collections.OrderedDict(
            [
                ('global_message_number', ['UINT16', 1]),
                ('fields', ['UINT8', 1])
            ]
        )
    )
    dm_dev_schema = Schema(
        'dm_dev',
        collections.OrderedDict(
            [
                ('dev_fields', ['UINT8', 1])
            ]
        )
    )

    def __init__(self, record_header, dev_field_dict, file):
        """
        Return a DefinitionMessage instance created by reading data from a FIT file.

        Paramters:
            record_header (RecordHeader): the record header associated with this definition message.
            dev_field_dict (dict): a dictionary of developer defoined fields in the FIT file.
            file (File): the FIT file instance to read the definition message data from.
        """
        self.reserved = None
        self.architecture = None
        self.global_message_number = None
        self.fields = None
        self.dev_fields = None
        super().__init__(file, DefinitionMessage.dm_primary_schema, [(DefinitionMessage.dm_secondary_schema, self.__decode_secondary)])

        self.__decode_plan = False
        self.message_type = MessageType.get_type(self.global_message_number)
        self.__message_data = DefinitionMessageData.get_message_definition(self.message_type)

        self.field_definitions = []
        for _ in range(self.fields):
            field_definition = FieldDefinition(file)
            self.file_size += field_definition.file_size
            self.field_definitions.append(field_definition)

        self.has_dev_fields = record_header.developer_data()
        self.dev_field_definitions = []
        if self.has_dev_fields:
            self._decode(DefinitionMessage.dm_dev_schema)
            for _ in range(self.dev_fields):
                dev_field_definition = DeveloperFieldDefinition(dev_field_dict, file)
                self.file_size += dev_field_definition.file_size
                self.dev_field_definitions.append(dev_field_definition)

    def __decode_secondary(self):
        try:
            self.endian = Architecture(self.architecture)
        except Exception:
            # treat all broken endians as little endian
            self.endian = Architecture.Little_Endian
        return True

    def field(self, field_number):
        """Return an instance of the proper Field subclass for the given field definition."""
        field = DefinitionMessageData.reserved_field_indexes.get(field_number)
        if field is None:
            field = self.__message_data.get(field_number)
        if field is None:
            field = UnknownField(field_number)
        return field

    def decode_plan(self):
        """
        Return what is needed to decode all of the fields of a data message with a single read.

        The plan is (struct, [(field, invalid value, index of the first value, value count)]) or None if the fields have
        to be decoded one at a time.
        """
        if self.__decode_plan is False:
            self.__decode_plan = self.__build_decode_plan()
        return self.__decode_plan

    def __build_decode_plan(self):
        unpack_format = '>' if self.endian is Architecture.Big_Endian else '<'
        entries = []
        index = 0
        for field_definition in self.field_definitions:
            type_string = field_definition.type_string()
            type_size = Schema.type_to_size[type_string]
            count = field_definition.type_count()
            if count < 1 or count * type_size != field_definition.size:
                return None
            unpack_format += Schema.type_to_unpack_format[type_string] * count
            entries.append((self.field(field_definition.field_definition_number), field_definition.invalid(), index, count))
            index += count
        return (struct.Struct(unpack_format), entries)

    def __str__(self):
        """Return a string representation of a DefinitionMessage instance."""
        return (f"DefinitionMessage: {repr(self.message_type)} {self.fields} {self.endian.name} fields")
