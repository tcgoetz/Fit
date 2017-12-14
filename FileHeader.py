#!/usr/bin/env python

#
# copyright Tom Goetz
#

import logging, collections

from Data import Data

class FileHeader(Data):

    primary_schema = collections.OrderedDict(
        [ ('header_size', ['UINT8', 1, '%d']), ('protocol_version', ['UINT8', 1, '%x']),
          ('profile_version', ['UINT16', 1, '%d']), ('data_size', ['UINT32', 1, '%d']),
          ('data_type', ['CHAR', 4, '%c']) ]
    )
    optional_schema = collections.OrderedDict(
        [ ('crc', ['UINT16', 1, '%x']) ]
    )
    profile_version_str = { 100: 'activity', 1602 : 'device'}

    min_file_header_size = 12
    opt_file_header_size = 14
    protocol_version = 0x10
    file_data_type = [46, 70, 73, 84]
#    file_data_type = ['.', 'F', 'I', 'T']

    def __init__(self, file):
        Data.__init__(self, file, FileHeader.primary_schema, FileHeader.optional_schema)

    def decode_optional(self):
        return (self['header_size'] >= FileHeader.opt_file_header_size)

    def get_header_size(self):
        return self['header_size']

    def get_data_size(self):
        return self['data_size']

    def get_protocol_version(self):
        return self['protocol_version']

    def get_profile_version(self):
        return self['profile_version']

    def check(self):
        return ((self['header_size'] >= FileHeader.min_file_header_size) and
                (self['protocol_version'] == FileHeader.protocol_version) and
                (self['data_type'] == FileHeader.file_data_type))

    def __str__(self):
        return ("%s: header size %d prot ver %x prof ver %d" %
                (self.__class__.__name__, self['header_size'], self['protocol_version'], self['profile_version']))
