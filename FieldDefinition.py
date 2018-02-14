#!/usr/bin/env python

#
# copyright Tom Goetz
#

import logging, collections

from Data import *



class FieldDefinition(Data):

    schema = Schema(collections.OrderedDict(
        [ ('field_definition_number', ['UINT8', 1, '%x']), ('size', ['UINT8', 1, '%x']), ('base_type', ['UINT8', 1, '%x']) ]
    ))
    base_type_data = {
        0x00 : [ False, 'enum',     0xFF,               'UINT8'],
        0x01 : [ False, 'sint8',    0x7F,               'INT8'],
        0x02 : [ False, 'uint8',    0xFF,               'UINT8'],
        0x07 : [ False, 'string',   0x00,               'CHAR'],
        0x83 : [ True,  'sint16',   0x7FFF,             'INT16'],
        0x84 : [ True,  'uint16',   0xFFFF,             'UINT16'],
        0x85 : [ True,  'sint32',   0x7FFFFFFF,         'INT32'],
        0x86 : [ True,  'uint32',   0xFFFFFFFF,         'UINT32'],
        0x88 : [ True,  'float32',  0xFFFFFFFF,         'FLOAT32'],
        0x89 : [ True,  'float64',  0xFFFFFFFFFFFFFFFF, 'FLOAT64'],
        0x0a : [ False, 'uint8z',   0x00,               'UINT8'],
        0x8b : [ True,  'uint16z',  0x00000000,         'UINT16'],
        0x8c : [ True,  'uint32z',  0x00000000,         'UINT32'],
        0x0d : [ False, 'byte',     0xFF,               'UINT8'],
        0x8e : [ True,  'sint64',   0x7FFFFFFFFFFFFFFF, 'INT64'],
        0x8f : [ True,  'uint64',   0xFFFFFFFFFFFFFFFF, 'UINT64'],
        0x90 : [ True,  'uint64z',  0x0000000000000000, 'UINT64'],
    }

    def __init__(self, file):
        Data.__init__(self, file, FieldDefinition.schema)

    def fdn_value(self):
        return self['field_definition_number']

    def size_value(self):
        return self['size']

    def base_type_value(self):
        return self['base_type']

    def base_type(self):
        if self.base_type_value() in FieldDefinition.base_type_data:
            return FieldDefinition.base_type_data[self.base_type_value()]
        raise IndexError("Unknown base type index %x" % self.base_type_value())

    def type_endian(self):
        return (self.base_type())[0]

    def type_name(self):
        return (self.base_type())[1]

    def invalid(self):
        return (self.base_type())[2]

    def type_string(self):
        return (self.base_type())[3]

    def type_count(self):
        type_size = Schema.type_to_size(self.type_string())
        return (self.size_value() / type_size)

    def __str__(self):
        return ("%s: type %d: %d of %s" %
            (self.__class__.__name__, self.fdn_value(), self.size_value(), self.type_string()));
