#!/usr/bin/env python

#
# copyright Tom Goetz
#

import collections

from Data import *
from Field import *
from FieldDefinition import FieldDefinition
from DeveloperFieldDefinition import DeveloperFieldDefinition
from DefinitionMessageData import DefinitionMessageData
from MessageType import MessageType


class DefinitionMessage(Data):

    dm_primary_schema = Schema(
        'dm_primary',
        collections.OrderedDict(
            [ ('reserved', ['UINT8', 1, '%x']), ('architecture', ['UINT8', 1, '%x']) ]
        )
    )
    dm_secondary_schema = Schema(
        'dm_secondary',
        collections.OrderedDict(
            [ ('global_message_number', ['UINT16', 1, '%x']), ('fields', ['UINT8', 1, '%x']) ]
        )
    )
    dm_dev_schema = Schema(
        'dm_dev',
        collections.OrderedDict(
            [ ('dev_fields', ['UINT8', 1, '%x']) ]
        )
    )

    def __init__(self, record_header, dev_field_dict, file):
        Data.__init__(self, file, DefinitionMessage.dm_primary_schema, [(DefinitionMessage.dm_secondary_schema, self.decode_secondary)] )

        if (self.global_message_number < 0) or (self.global_message_number > MessageType.mfg_range_max.value):
            raise FitMessageType('Message number out of bounds: %d' % self.global_message_number)

        try:
            self.message_type = MessageType(self.global_message_number)
        except ValueError:
            raise FitMessageType("Unknown message type: %d" % self.global_message_number)

        self.message_data = DefinitionMessageData.get_message_definition(self.message_type)

        self.field_definitions = []
        for index in xrange(self.fields):
            field_definition = FieldDefinition(file)
            self.file_size += field_definition.file_size
            self.field_definitions.append(field_definition)

        self.has_dev_fields = record_header.developer_data()
        self.dev_field_definitions = []
        if self.has_dev_fields:
            self.decode(DefinitionMessage.dm_dev_schema)
            for index in xrange(self.dev_fields):
                dev_field_definition = DeveloperFieldDefinition(dev_field_dict, file)
                self.file_size += dev_field_definition.file_size
                self.dev_field_definitions.append(dev_field_definition)

    def decode_secondary(self):
        self.endian = Architecture(self.architecture)
        return True

    def field(self, field_number):
        return DefinitionMessageData.reserved_field_indexes.get(field_number, self.message_data.get(field_number, UnknownField(field_number)))

    def __str__(self):
        return ("%s: %s %d %s fields" % (self.__class__.__name__, self.message_type, self.field_count(), self.endian.name))
