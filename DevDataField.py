#!/usr/bin/env python

#
# copyright Tom Goetz
#

import collections

from Data import *


class DevDataField(Data):

    def __init__(self, file, definition_message, dev_field_definition, english_units=False):
        self.dev_field_definition = dev_field_definition
        self.english_units = english_units

        self.field = dev_field_definition.field()
        type = dev_field_definition.type_string()
        count = dev_field_definition.type_count()
        schema = Schema(self.field.name, collections.OrderedDict( [ (self.field.name, [type, count, '%d']) ] ))

        Data.__init__(self, file, schema, None, definition_message.endian)

    def convert(self, english_units=False):
        self.value_obj = self.field.convert(self.__dict__[self.field.name], self.dev_field_definition.invalid(), self.english_units)

    def name(self):
        return self.value_obj.name()

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

