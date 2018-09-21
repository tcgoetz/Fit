#!/usr/bin/env python

#
# copyright Tom Goetz
#

import collections, enum

from Data import *


class MessageClass(enum.Enum):
    data        = 0
    definition  = 1


class RecordHeader(Data):

    rh_schema = Schema('rh', collections.OrderedDict( [ ('record_header', ['UINT8', 1, '%x']) ] ))
    message_type_string = [ 'data', 'definition' ]

    def __init__(self, file):
        Data.__init__(self, file, RecordHeader.rh_schema)

        self.message_class = MessageClass(self.message_type())

    def compressed_timestamp(self):
        return (self.record_header & 0x80) == 0x80

    def message_type(self):
        return (self.record_header & 0x40) == 0x40

    def developer_data(self):
        return (self.record_header & 0x60) == 0x60

    def local_message(self):
        return (self.record_header & 0x0f)

    def __str__(self):
        return ("%s: Local %s message %d (Compressed %d)" %
                (self.__class__.__name__, self.message_class.name, self.local_message(), self.compressed_timestamp()))
