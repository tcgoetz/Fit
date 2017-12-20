#!/usr/bin/env python

#
# copyright Tom Goetz
#

import struct

class Schema():

    def __init__(self, ordered_dict):
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
        type_size = { 'CHAR' : 'B', 'INT8' : 'b', 'UINT8' : 'B', 'INT16' : 'h', 'UINT16' : 'H', 'INT32' : 'i',
                      'UINT32' : 'I', 'INT64' : 'q', 'UINT64' : 'Q', 'FLOAT32' : 'f', 'FLOAT64' : 'd'}
        return type_size[type]

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
        for key in self.ordered_dict:
            (type, count, format) = self.ordered_dict[key]
            if count > 1:
                decoded_data[key] = []
                for repeat in xrange(count):
                    decoded_data[key].append(data[index])
                    index += 1
            else:
                    decoded_data[key] = data[index]
                    index += 1
        return decoded_data


class Data():

    def __init__(self, file, primary_schema, optional_schema=None, endian=False):
        self.file = file
        self.primary_schema = Schema(primary_schema)
        if optional_schema:
            self.optional_schema = Schema(optional_schema)
        else:
            self.optional_schema = None
        self.endian = endian

        self.decoded_data = {}
        self.file_size = 0

        self.decode()
        self.convert()

    def read(self, schema):
        (unpack_format, file_size) = schema.get_unpack(self.endian)
        self.file_size += file_size
        return struct.unpack(unpack_format, self.file.read(file_size))

    def __decode(self, schema):
        self.decoded_data.update(schema.decode(self.read(schema)))

    def decode(self):
        self.__decode(self.primary_schema)
        if self.decode_optional():
            self.__decode(self.optional_schema)

    def decode_optional(self):
        return (self.optional_schema != None)

    def convert(self):
        pass

    def __string(self, schema):
        printable_data = {}
        for key in schema:
            (type, count, format) = schema[key]
            if count > 1:
                printable_data[key] = []
                for index in xrange(count):
                    values = self.decoded_data[key]
                    printable_data[key].append(format % values[index])
            else:
                printable_data[key] = (format % self.decoded_data[key])
        self.printable_data.update(printable_data)

    def __getitem__(self, key):
        return self.decoded_data[key]

    def __str__(self):
        self.printable_data = {}
        self.__string(self.primary_schema)
        if self.decode_optional():
            self.__string(self.optional_schema)
        return str(self.printable_data)

