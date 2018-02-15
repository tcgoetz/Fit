#!/usr/bin/env python

#
# copyright Tom Goetz
#

import sys, logging, collections, traceback
from datetime import tzinfo, timedelta, datetime

from FitExceptions import *
from FileHeader import FileHeader
from RecordHeader import RecordHeader
from DefinitionMessage import DefinitionMessage
from DataMessage import DataMessage


logger = logging.getLogger(__name__)


class File():
    def __init__(self, filename, english_units=False):
        self.filename = filename
        self.english_units = english_units

        self.last_date = None
        self.last_day = None

        self.matched_timestamp_16 = None

        self.file = open(filename, 'rb')
        self.parse()

    def timestamp16_to_timestamp(self, timestamp_16):
        if self.matched_timestamp_16:
            if timestamp_16 >= self.matched_timestamp_16:
                delta = timestamp_16 - self.matched_timestamp_16
            else:
                delta = (self.matched_timestamp_16 - 65535) + timestamp_16
        else:
            self.matched_timestamp_16 = timestamp_16
            delta = 0
        return self.last_message_timestamp + timedelta(0, delta)

    def track_dates(self, timestamp):
        self.last_message_timestamp = timestamp
        self.matched_timestamp_16 = None

    def parse(self):
        self.file_header = FileHeader(self.file)

        self.data_size = self.file_header.data_size

        self._definition_messages = {}
        self._dev_fields = {}
        self._data_messages = {}
        data_consumed = 0
        self.record_count = 0
        self.first_message_timestamp = None
        self.last_message_timestamp = None

        while self.data_size > data_consumed:
            record_header = RecordHeader(self.file)
            local_message_num = record_header.local_message()
            data_consumed += record_header.file_size
            self.record_count += 1

            if record_header.definition_message():
                definition_message = DefinitionMessage(record_header, self._dev_fields, self.file)
                data_consumed += definition_message.file_size
                self._definition_messages[local_message_num] = definition_message
            else:
                definition_message = self._definition_messages[local_message_num]
                data_message = DataMessage(definition_message, self.file, self.english_units)
                logger.debug("  Message [%d]: %s" % (local_message_num, str(data_message)))

                data_consumed += data_message.file_size

                data_message_name = data_message.name()

                time_created_timestamp = data_message['time_created']
                if time_created_timestamp:
                    self.time_created_timestamp = time_created_timestamp['value']
                    self.track_dates(self.time_created_timestamp)

                message_timestamp = data_message['timestamp']
                if message_timestamp:
                    self.track_dates(message_timestamp['value'])
                else:
                    message_timestamp_16 = data_message['timestamp_16']
                    if message_timestamp_16:
                        data_message.timestamp = self.timestamp16_to_timestamp(message_timestamp_16['value'])
                    else:
                        data_message.timestamp = self.last_message_timestamp

                if data_message_name == 'field_description':
                    self._dev_fields[data_message['field_definition_number']] = data_message

                try:
                    self._data_messages[data_message_name].append(data_message)
                except:
                    self._data_messages[data_message_name] = [ data_message ]

            logger.debug("Record %d: consumed %d of %s %r" % (self.record_count, data_consumed, self.data_size, self.english_units))
        logger.debug("File %s: %s -> %s" % (self.filename, self.time_created_timestamp, self.last_message_timestamp))

    def type(self):
        return self['file_id'][0]['type'].value()

    def product(self):
        return self['file_id'][0]['product'].value()

    def serial_number(self):
        return self['file_id'][0]['serial_number'].value()

    def device(self):
        return self.product() + "_" + str(self.serial_number())

    def time_created(self):
        return self['file_id'][0]['time_created'].value()

    def date_span(self):
        return (self.time_created_timestamp, self.last_message_timestamp)

    def message_types(self):
        return self._data_messages.keys()

    def __getitem__(self, name):
        return self._data_messages.get(name, None)

    def __str__(self):
        return "Type: " + self.type()
