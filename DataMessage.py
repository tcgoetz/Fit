#!/usr/bin/env python

#
# copyright Tom Goetz
#

import collections, logging

from Field import Field
from DataField import DataField
from DevDataField import DevDataField


logger = logging.getLogger(__name__)


class DataMessage():
    def __init__(self, definition_message, file, english_units=False):
        self.definition_message = definition_message

        self._fields = {}
        self.file_size = 0
        self.timestamp = None

        message_fields = {}
        for index in xrange(definition_message.fields):
            data_field = DataField(file, definition_message, definition_message.field_definitions[index], english_units)
            self.file_size += data_field.file_size

            # expand subfields?
            field_value = data_field._field_value()
            subfield_names = field_value.subfield_names()
            if subfield_names:
                for subfield_name in subfield_names:
                    subfield_value = field_value[subfield_name]
                    subfield_formal_name = subfield_value.field.name
                    if subfield_formal_name in message_fields:
                        message_fields[subfield_formal_name]._value.value += subfield_value._value.value
                    else:
                        message_fields[subfield_formal_name] = subfield_value
            else:
                message_fields[data_field._field_name()] = data_field._field_value()

        for field_value in message_fields.values():
            field = field_value.field
            self._fields[field_value.field.name] = field_value
            dependant_field_func = getattr(field, 'dependant_field', None)
            if dependant_field_func:
                control_values = [message_fields[control_field].value for control_field in field.dependant_field_control_fields]
                field_value.field = dependant_field_func(control_values)
                field_value.reconvert()
                self._fields[field_value.field.name] = field_value

        if definition_message.has_dev_fields:
            for index in xrange(definition_message.dev_fields):
                data_field = DevDataField(file, definition_message, definition_message.dev_field_definitions[index], english_units)
                self.file_size += data_field.file_size
                field_value = data_field._field_value()
                self._fields[field_value.field.name] = field_value

    def type(self):
        return self.definition_message.message_number()

    def name(self):
        return self.definition_message.name()

    def to_dict(self):
        fields = {}
        for field_name, field_value in self._fields.iteritems():
            if field_name == 'timestamp_16':
                fields['timestamp'] = self.timestamp
            else:
                fields[field_name] = field_value.value
        return fields

    def __getitem__(self, name):
        return self._fields.get(name, None)

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
        fields_str = "".join(["%s, " % value for value in self._fields.values()])
        return ("%s: %s (%d): %s" % (self.__class__.__name__,  self.name(), self.type(), fields_str))
