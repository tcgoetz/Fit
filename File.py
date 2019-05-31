#!/usr/bin/env python

#
# copyright Tom Goetz
#

import sys, logging, collections, traceback

from FitExceptions import *
from FileHeader import FileHeader
from RecordHeader import *
from DefinitionMessage import DefinitionMessage
from DataMessage import DataMessage
from MessageType import MessageType


logger = logging.getLogger(__name__)


class File(object):

    name_regex = r'\w+\.(fit|FIT)'

    def __init__(self, filename, measurement_system=False):
        self.filename = filename
        self.measurement_system = measurement_system

        self.last_date = None
        self.last_day = None

        self.matched_timestamp_16 = None

        self.file = open(filename, 'rb')
        self.parse()

    def parse(self):
        logger.debug("Parsing File %s", self.filename)
        self.file_header = FileHeader(self.file)

        self.data_size = self.file_header.data_size

        self._definition_messages = {}
        self._dev_fields = {}
        self._data_message_types = []
        data_consumed = 0
        self.record_count = 0
        self.first_message_timestamp = None
        self.last_message_timestamp = None

        while self.data_size > data_consumed:
            record_header = RecordHeader(self.file)
            local_message_num = record_header.local_message()
            data_consumed += record_header.file_size
            self.record_count += 1
            logger.debug("Parsed record %s", repr(record_header))

            if record_header.message_class is MessageClass.definition:
                definition_message = DefinitionMessage(record_header, self._dev_fields, self.file)
                logger.debug("  Definition [%d]: %s", local_message_num, str(definition_message))
                data_consumed += definition_message.file_size
                self._definition_messages[local_message_num] = definition_message
            else:
                definition_message = self._definition_messages[local_message_num]
                data_message = DataMessage(definition_message, self.file, self.measurement_system)
                logger.debug("  Data [%d]: %s", local_message_num, str(data_message))

                data_consumed += data_message.file_size

                data_message_type = data_message.type()

                if data_message.time_created_timestamp:
                     self.time_created_timestamp = data_message.time_created_timestamp
                # if self.last_message_timestamp is not None and data_message.timestamp < self.last_message_timestamp:
                #     raise FitOutOfOrderMessage('Message time stamp %s before previous %s' % (data_message.timestamp, self.last_message_timestamp))
                self.last_message_timestamp = data_message.timestamp

                if data_message_type == MessageType.field_description:
                    self._dev_fields[data_message['field_definition_number'].value] = data_message

                logger.debug("Parsed %s", repr(data_message_type))

                try:
                    self.__dict__[data_message_type].append(data_message)
                except:
                    self.__dict__[data_message_type] = [ data_message ]
                    self._data_message_types.append(data_message_type)

            logger.debug("Record %d: consumed %d of %s %r", self.record_count, data_consumed, self.data_size, self.measurement_system)
        logger.debug("File %s: %s -> %s", self.filename, self.time_created_timestamp, self.last_message_timestamp)

    def file_id(self):
        return self[MessageType.file_id][0]

    def type(self):
        return self.file_id()['type'].value

    def product(self):
        return self.file_id()['product'].value

    def serial_number(self):
        return self.file_id()[0]['serial_number'].value

    def device(self):
        return self.product() + "_" + str(self.serial_number())

    def time_created(self):
        return self.file_id()['time_created'].value

    def date_span(self):
        return (self.time_created(), self.last_message_timestamp)

    def message_types(self):
        return self._data_message_types

    def __getitem__(self, name):
        return self.__dict__.get(name)

    def __str__(self):
        return "Type: " + repr(self.type())
