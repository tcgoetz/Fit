#!/usr/bin/env python

#
# copyright Tom Goetz
#

import collections

from Data import *
from FieldEnums import *


class DataField(Data):

    def __init__(self, file, definition_message, field_definition, measurement_system):
        self.field_definition = field_definition
        self.measurement_system = measurement_system
        self.field = definition_message.field(field_definition.field_definition_number)
        type = field_definition.type_string()
        count = field_definition.type_count()
        schema = Schema(self.field.name, collections.OrderedDict( [ (self.field.name, [type, count, '%d']) ] ))
        super(DataField, self).__init__(file, schema, None, definition_message.endian)

    def convert(self):
        self.value_obj = self.field.convert(self.__dict__[self.field.name], self.field_definition.invalid(), self.measurement_system)

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

