#!/usr/bin/env python

#
# copyright Tom Goetz
#

import logging, collections

from Data import *
from BaseType import BaseType
from Field import DevField


class DeveloperFieldDescription(Data, BaseType):

    dfd_schema = Schema(
        'dfd_schema',
        collections.OrderedDict(
            [
                ('field_number', ['UINT8', 1, '%x']),
                ('size', ['UINT8', 1, '%x']),
                ('developer_data_index', ['UINT8', 1, '%x'])
            ]
        )
    )

    def __init__(self, dev_field_dict, file):
        Data.__init__(self, file, DeveloperFieldDescription.dfd_schema)
        self.dev_field = dev_field_dict[self.field_number]

    def type_string(self):
        return self.dev_field['fit_base_type_id']

    def field_name(self):
        return self.dev_field['field_name']

    def units(self):
        return self.dev_field['units']

    def offset(self):
        return self.dev_field['offset']

    def scale(self):
        return self.dev_field['scale']

    def field(self):
        return DevField(self.field_name(), self.units(), self.scale(), self.offset())

    def base_type_value(self):
        return self.dev_field['fit_base_type_id']

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
        return (self.size / type_size)

    def __str__(self):
        return ("%s: type %d: %d of %s" %
            (self.__class__.__name__, self.field_number, self.size, self.type_string()));
