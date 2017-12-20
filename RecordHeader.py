#!/usr/bin/env python

#
# copyright Tom Goetz
#

import logging, collections

from Data import *


class RecordHeader(Data):

    schema = Schema(collections.OrderedDict( [ ('record_header', ['UINT8', 1, '%x']) ] ))
    message_type_string = [ 'data', 'definition' ]

    def __init__(self, file):
        Data.__init__(self, file, RecordHeader.schema)

    def record_header(self):
        return self['record_header']

    def compressed_timestamp(self):
        return (self.record_header() & 0x80) >> 7

    def message_type(self):
        return (self.record_header() & 0x40) >> 6

    def message_type_str(self):
        return RecordHeader.message_type_string[self.message_type()]

    def definition_message(self):
        return self.message_type()

    def data_message(self):
        return not self.message_type()

    def local_message(self):
        return (self.record_header() & 0x0f)

    def __str__(self):
        return ("%s: Local %s message %d (Compressed %d)" %
                (self.__class__.__name__, self.message_type_str(), self.local_message(), self.compressed_timestamp()))
