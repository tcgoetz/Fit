#!/usr/bin/env python

#
# copyright Tom Goetz
#

import struct


class Data():

    def __init__(self, file, primary_schema, optional_schema=None, endian=False):
        self.file = file
        self.primary_schema = primary_schema
        self.optional_schema = optional_schema
        self.endian = endian

        self.decoded_data = {}
        self.file_size = 0

        self.decode()
        self.convert()

    def type_to_size(self, type):
        type_size = { 'CHAR' : 1, 'INT8' : 1, 'UINT8' : 1, 'INT16' : 2, 'UINT16' : 2, 'INT32' : 4, 'UINT32' : 4,
                      'INT64' : 8, 'UINT64' : 8, 'FLOAT32' : 4, 'FLOAT64' : 4}
        return type_size[type]

    def type_to_unpack_format(self, type):
        type_size = { 'CHAR' : 'B', 'INT8' : 'b', 'UINT8' : 'B', 'INT16' : 'h', 'UINT16' : 'H', 'INT32' : 'i',
                      'UINT32' : 'I', 'INT64' : 'q', 'UINT64' : 'Q', 'FLOAT32' : 'f', 'FLOAT64' : 'd'}
        return type_size[type]

    def read(self, schema):
        if self.endian:
            unpack_format = '>'
        else:
            unpack_format = ''
        file_size = 0
        for key in schema:
            (type, count, format) = schema[key]
            for index in xrange(count):
                unpack_format += self.type_to_unpack_format(type)
            file_size += (count * self.type_to_size(type))
        self.file_size += file_size
        return struct.unpack(unpack_format, self.file.read(file_size))

    def __decode(self, schema):
        data = self.read(schema)
        decoded_data = {}
        index = 0
        for key in schema:
            (type, count, format) = schema[key]
            if count > 1:
                decoded_data[key] = []
                for repeat in xrange(count):
                    decoded_data[key].append(data[index])
                    index += 1
            else:
                    decoded_data[key] = data[index]
                    index += 1
        self.decoded_data.update(decoded_data)

    def decode(self):
        self.__decode(self.primary_schema)
        if self.decode_optional():
            self.__decode(self.optional_schema)

    def decode_optional(self):
        return (self.optional_schema != None)

    def convert(self):
        return

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

