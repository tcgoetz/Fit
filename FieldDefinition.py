#!/usr/bin/env python

#
# copyright Tom Goetz
#

import logging, collections

from Data import *
from BaseType import BaseType


class FieldDefinition(Data, BaseType):

    fd_schema = Schema(
        'fd',
        collections.OrderedDict(
            [ ('field_definition_number', ['UINT8', 1, '%x']), ('size', ['UINT8', 1, '%x']), ('base_type', ['UINT8', 1, '%x']) ]
        )
    )

    def __init__(self, file):
        Data.__init__(self, file, FieldDefinition.fd_schema)

    def fdn_value(self):
        return self['field_definition_number']

    def size_value(self):
        return self['size']

    def base_type_value(self):
        return self['base_type']

    def base_type(self):
        return self._base_type(self.base_type_value())

    def type_endian(self):
        return self._type_endian(self.base_type_value())

    def type_name(self):
        return self._type_name(self.base_type_value())

    def invalid(self):
        return self._invalid(self.base_type_value())

    def type_string(self):
        return self._type_string(self.base_type_value())

    def type_count(self):
        type_size = Schema.type_to_size(self.type_string())
        return (self.size_value() / type_size)

    def __str__(self):
        return ("%s: type %d: %d of %s" %
            (self.__class__.__name__, self.fdn_value(), self.size_value(), self.type_string()));
