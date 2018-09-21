#!/usr/bin/env python

#
# copyright Tom Goetz
#

import collections

from Data import *


class DataField(Data):

    def __init__(self, file, definition_message, field_definition, english_units=False):
        self.field_definition = field_definition
        self.english_units = english_units

        self.field = definition_message.field(field_definition.field_definition_number)

        type = field_definition.type_string()
        count = field_definition.type_count()
        schema = Schema(self.field.name, collections.OrderedDict( [ (self.field.name, [type, count, '%d']) ] ))

        Data.__init__(self, file, schema, None, definition_message.endian)

    def convert(self, english_units=False):
        self.value_obj = self.field.convert(self.__dict__[self.field.name], self.field_definition.invalid(), self.english_units)

    def _field_name(self):
        return self.value_obj.field.name

    def _field_value(self):
        return self.value_obj

    def __iter__(self):
        return iter(self.value_obj)

    def keys(self):
        return self.value_obj.keys()

    def items(self):
        return self.value_obj.items()

    def values(self):
        return self.value_obj.values()

    def __str__(self):
        return str(self.value_obj)

