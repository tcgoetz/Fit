#!/usr/bin/env python

#
# copyright Tom Goetz
#

import collections

from Field import Field
from DataField import DataField


class DataMessage():
    def __init__(self, definition_message, file, english_units=False):
        self.definition_message = definition_message

        self._fields = {}
        self.file_size = 0
        self._timestamp = None

        field_values = {}
        for index in xrange(definition_message.field_count()):
            data_field = DataField(file, definition_message, definition_message.field_definitions[index], english_units)
            self.file_size += data_field.file_size

            # expand subfields?
            field_value = data_field.value()
            subfield_names = field_value.subfield_names()
            if subfield_names:
                for subfield_name in subfield_names:
                    subfield_value = field_value[subfield_name]
                    subfield_formal_name = subfield_value.field.name
                    if subfield_formal_name in field_values:
                        field_values[subfield_formal_name]._value['value'] += subfield_value._value['value']
                    else:
                        field_values[subfield_formal_name] = subfield_value
            else:
                field_values[data_field.name()] = data_field.value()

        for field_value in field_values.values():
            field = field_value.field
            if field_value.field.is_dependant_field:
                control_value = field_values[field.dependant_field_control_field]['orig']
                field_value.field = field.dependant_field(control_value)
                field_value.reconvert()
                self._fields[field_value.field.name] = field_value
            else:
                self._fields[field_value.name()] = field_value

    def type(self):
        return self.definition_message.message_number()

    def name(self):
        return self.definition_message.name()

    def timestamp(self):
        return self._timestamp

    def __getitem__(self, name):
        if name in self._fields:
            return self._fields[name]
        return None

    def __iter__(self):
        return iter(self._fields)

    def keys(self):
        return self._fields.keys()

    def items(self):
        return self._fields.items()

    def iteritems(self):
        return self._fields.iteritems()

    def values(self):
        return self._fields.values()

    def __str__(self):
        fields_str = "".join(["%s," % value for value in self._fields.values()])
        return ("%s: %s (%d): %s" % (self.__class__.__name__,  self.name(), self.type(), fields_str))
