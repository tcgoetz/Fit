"""Code that manages a FIT file."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import logging

from file_header import FileHeader
from record_header import RecordHeader, MessageClass
from definition_message import DefinitionMessage
from data_message import DataMessage
from message_type import MessageType


logger = logging.getLogger(__name__)

name_regex = r'\w+\.(fit|FIT)'


class File(object):
    """Object that represents a FIT file."""

    def __init__(self, filename, measurement_system=False):
        """
        Return a File instance by parsing a FIT file.

        Parameters:
            filename (string): The name of the FIT file including full path.
            measurement_system (DisplayMeasure): The measurement units (metric, statute, etc) to sue when parsing the FIT file.

        """
        self.filename = filename
        self.measurement_system = measurement_system

        self.last_date = None
        self.last_day = None

        self.matched_timestamp_16 = None

        self.file = open(filename, 'rb')
        self.__parse()

    def __parse(self):
        logger.debug("Parsing File %s", self.filename)
        self.file_header = FileHeader(self.file)

        self.data_size = self.file_header.data_size

        self._definition_messages = {}
        self.__dev_fields = {}
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
            logger.debug("Parsed record %r", record_header)

            if record_header.message_class is MessageClass.definition:
                definition_message = DefinitionMessage(record_header, self.__dev_fields, self.file)
                logger.debug("  Definition [%d]: %s", local_message_num, definition_message)
                data_consumed += definition_message.file_size
                self._definition_messages[local_message_num] = definition_message
            else:
                definition_message = self._definition_messages[local_message_num]
                data_message = DataMessage(definition_message, self.file, self.measurement_system)
                logger.debug("  Data [%d]: %s", local_message_num, data_message)

                data_consumed += data_message.file_size

                data_message_type = data_message.type()

                if data_message.time_created_timestamp:
                    self.time_created_timestamp = data_message.time_created_timestamp
                # if self.last_message_timestamp is not None and data_message.timestamp < self.last_message_timestamp:
                #     raise FitOutOfOrderMessage('Message time stamp %s before previous %s' % (data_message.timestamp, self.last_message_timestamp))
                self.last_message_timestamp = data_message.timestamp

                if data_message_type == MessageType.field_description:
                    self.__dev_fields[data_message['field_definition_number'].value] = data_message

                logger.debug("Parsed %r", data_message_type)

                try:
                    self.__dict__[data_message_type].append(data_message)
                except Exception:
                    self.__dict__[data_message_type] = [data_message]
                    self._data_message_types.append(data_message_type)

            logger.debug("Record %d: consumed %d of %s %r", self.record_count, data_consumed, self.data_size, self.measurement_system)
        logger.debug("File %s: %s -> %s", self.filename, self.time_created_timestamp, self.last_message_timestamp)

    def file_id(self):
        """Return the file_id message for the file."""
        return self[MessageType.file_id][0]

    def type(self):
        """Return the file type for the file."""
        return self.file_id()['type'].value

    def product(self):
        """Return the product type from the file."""
        return self.file_id()['product'].value

    def serial_number(self):
        """Return the device serial number from the file."""
        return self.file_id()[0]['serial_number'].value

    def device(self):
        """Return the device from the file."""
        return self.product() + "_" + str(self.serial_number())

    def time_created(self):
        """Return the the time the file was created."""
        return self.file_id()['time_created'].value

    def date_span(self):
        """Return a tuple of the start and end dates of the file."""
        return (self.time_created(), self.last_message_timestamp)

    def message_types(self):
        """Return a list of the message types present in the file."""
        return self._data_message_types

    def __getitem__(self, name):
        return self.__dict__.get(name, [])

    def __str__(self):
        return "File(%r)" % self.type()
