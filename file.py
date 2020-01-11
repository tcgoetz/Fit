"""Code that manages a FIT file."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import logging
import datetime

from Fit.file_header import FileHeader
from Fit.record_header import RecordHeader, MessageClass
from Fit.definition_message import DefinitionMessage
from Fit.data_message import DataMessage
from Fit.message_type import MessageType
from Fit.field_enums import DisplayMeasure


logger = logging.getLogger(__name__)

name_regex = r'\w+\.(fit|FIT)'


class File(object):
    """Object that represents a FIT file."""

    def __init__(self, filename, measurement_system=DisplayMeasure.metric):
        """
        Return a File instance by parsing a FIT file.

        Parameters:
            filename (string): The name of the FIT file including full path.
            measurement_system (DisplayMeasure): The measurement units (metric, statute, etc) to uwe when parsing the FIT file.

        """
        self.filename = filename
        self.measurement_system = measurement_system

        self.last_date = None
        self.last_day = None

        self.matched_timestamp_16 = None

        self.file = open(filename, 'rb')
        self.__parse()
        self.__sumarize()

    def __del__(self):
        """Delete the File instance."""
        self.file.close()

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

                # if data_message.time_created_timestamp:
                #     self.time_created_timestamp = data_message.time_created_timestamp
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

    def __sumarize(self):
        self.file_id = self[MessageType.file_id][0]
        self.time_created = self.file_id['time_created'].value
        self.type = self.file_id['type'].value
        self.product = self.file_id['product'].value
        self.serial_number = self.file_id['serial_number'].value
        self.device = f'{self.product}_{self.serial_number}'
        self.device_settings_list = self[MessageType.device_settings]
        self.monitoring_info_list = self[MessageType.monitoring_info]
        if len(self.device_settings_list) > 0:
            self.device_settings = self.device_settings_list[0]
            self.utc_offset = self.device_settings['time_offset'].value
        elif len(self.monitoring_info_list) > 0:
            self.monitoring_info = self.monitoring_info_list[0]
            monitoring_info_time_utc = self.monitoring_info['timestamp'].value
            monitoring_info_time_local = self.monitoring_info['local_timestamp'].value
            self.utc_offset = (monitoring_info_time_local - monitoring_info_time_utc.replace(tzinfo=None)).total_seconds()
        else:
            self.utc_offset = 0
        self.local_tz = datetime.timezone(datetime.timedelta(seconds=self.utc_offset))
        self.time_created_local = self.utc_datetime_to_local(self.time_created)
        logger.info("File %s: %s (%s) -> %s", self.filename, self.time_created, self.local_tz, self.last_message_timestamp)

    def date_span(self):
        """Return a tuple of the start and end dates of the file."""
        return (self.time_created(), self.last_message_timestamp)

    def utc_datetime_to_local(self, dt):
        if self.local_tz is not None and dt.tzinfo is datetime.timezone.utc:
            return dt.astimezone(self.local_tz).replace(tzinfo=None)
        return dt.replace(tzinfo=None)

    def message_types(self):
        """Return a list of the message types present in the file."""
        return self._data_message_types

    def __getitem__(self, name):
        """Return the attribute named name."""
        return self.__dict__.get(name, [])

    def __str__(self):
        """Return a string representation of the class instance."""
        return f'File({repr(self.type())})'
