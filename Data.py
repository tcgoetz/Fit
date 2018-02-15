#!/usr/bin/env python

#
# copyright Tom Goetz
#

import struct, logging


logger = logging.getLogger(__name__)


class Schema():

    def __init__(self, name, ordered_dict):
        self.name = name
        self.ordered_dict = ordered_dict
        self.file_size = 0
        self.unpack_format = None

    @classmethod
    def type_to_size(cls, type):
        type_size = { 'CHAR' : 1, 'INT8' : 1, 'UINT8' : 1, 'INT16' : 2, 'UINT16' : 2, 'INT32' : 4, 'UINT32' : 4,
                      'INT64' : 8, 'UINT64' : 8, 'FLOAT32' : 4, 'FLOAT64' : 4}
        return type_size[type]

    @classmethod
    def type_to_unpack_format(cls, type):
        type_format = { 'CHAR' : 'B', 'INT8' : 'b', 'UINT8' : 'B', 'INT16' : 'h', 'UINT16' : 'H', 'INT32' : 'i',
                      'UINT32' : 'I', 'INT64' : 'q', 'UINT64' : 'Q', 'FLOAT32' : 'f', 'FLOAT64' : 'd'}
        return type_format[type]

    def compile_unpack(self, endian):
        if endian:
            self.unpack_format = '>'
        else:
            self.unpack_format = ''
        for key in self.ordered_dict:
            (type, count, format) = self.ordered_dict[key]
            for index in xrange(count):
                self.unpack_format += self.type_to_unpack_format(type)
            self.file_size += (count * self.type_to_size(type))

    def get_unpack(self, endian):
        if self.unpack_format is None:
            self.compile_unpack(endian)
        return (self.unpack_format, self.file_size)

    def decode(self, data):
        decoded_data = {}
        index = 0
        for (key, (type, count, format)) in self.ordered_dict.iteritems():
            if count > 1:
                decoded_data[key] = [data[index + repeat] for repeat in xrange(count)]
                index += count
            else:
                decoded_data[key] = data[index]
                index += 1
        return decoded_data

    def printable_data(self, decoded_data):
        printable_data = {}
        for (key,(type, count, format)) in self.ordered_dict.iteritems():
            if count > 1:
                printable_data[key] = [(format % decoded_data[index + repeat]) for repeat in xrange(count)]
            else:
                printable_data[key] = (format % decoded_data[key])
        return printable_data


class Data():

    def __init__(self, file, primary_schema, secondary_schemas=None, endian=False):
        self.file = file
        self.primary_schema = primary_schema
        self.secondary_schemas = secondary_schemas
        self.endian = endian

        self.file_size = 0

        self.decode_all()
        self.convert()

    def read(self, schema):
        (unpack_format, file_size) = schema.get_unpack(self.endian)
        self.file_size += file_size
        return struct.unpack(unpack_format, self.file.read(file_size))

    def decode(self, schema):
        #logger.debug("Decoding: " + schema.name)
        self.__dict__.update(schema.decode(self.read(schema)))
        #logger.debug("Decoded: " + str(self.file_size) + " bytes")

    def decode_all(self):
        self.decode(self.primary_schema)
        if self.secondary_schemas is not None:
            for schema, control_func in self.secondary_schemas:
                if control_func():
                    self.decode(schema)

    def convert(self):
        pass

    def __str__(self):
        self.printable_data = self.primary_schema.printable_data(self.decoded_data)
        if self.secondary_schemas is not None:
            for schema, control_func in self.secondary_schemas:
                if control_func():
                    self.printable_data.update(schema.printable_data(self.decoded_data))
        return str(self.printable_data)

