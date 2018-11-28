#!/usr/bin/env python

#
# copyright Tom Goetz
#

import collections, logging

from Field import Field
from DataField import DataField
from DevDataField import DevDataField
from FitExceptions import *


logger = logging.getLogger(__name__)


class DataMessage():
    def __init__(self, definition_message, fit_file, english_units=False):
        self.definition_message = definition_message

        self._fields = {}
        self.file_size = 0
        self.timestamp = None

        message_fields = {}
        for index in xrange(definition_message.fields):
            data_field = DataField(fit_file, definition_message, definition_message.field_definitions[index], english_units)
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
        self.convert_fields(message_fields)
        self.convert_dev_fields(fit_file, definition_message, english_units)

    def control_field_value(self, field, message_fields, control_field_name):
        control_field = message_fields.get(control_field_name, None)
        if control_field is not None:
            return control_field.value
        logger.debug('Missing control field %s for %s in message %s' % (control_field_name, repr(field), repr(message_fields)))

    def convert_fields(self, message_fields):
        for field_value in message_fields.values():
            field = field_value.field
            dependant_field_func = getattr(field, 'dependant_field', None)
            if dependant_field_func:
                control_values = [self.control_field_value(field, message_fields, control_field) for control_field in field.dependant_field_control_fields]
                field_value.field = dependant_field_func(control_values)
                field_value.reconvert()
            self._fields[field_value.field.name] = field_value

    def convert_dev_fields(self, fit_file, definition_message, english_units):
        if definition_message.has_dev_fields:
            for index in xrange(definition_message.dev_fields):
                data_field = DevDataField(fit_file, definition_message, definition_message.dev_field_definitions[index], english_units)
                self.file_size += data_field.file_size
                field_value = data_field._field_value()
                self._fields[field_value.field.name] = field_value

    def type(self):
        return self.definition_message.message_type

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
        return "%s: %s: %s" % (self.__class__.__name__, repr(self.type()), fields_str)
