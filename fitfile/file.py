"""Code that manages a FIT file."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import logging
import datetime

from .file_header import FileHeader
from .record_header import RecordHeader, MessageClass
from .definition_message import DefinitionMessage
from .data_message import DataMessageDecodeContext, DataMessage
from .message_type import MessageType
from .field_enums import DisplayMeasure


logger = logging.getLogger(__name__)

name_regex = r'\w+\.(fit|FIT)'


# dynamically generated class properties
# pylint: disable=no-member
class File():
    """Object that represents a FIT file."""

    def __init__(self, filename, measurement_system=DisplayMeasure.metric):
        """
        Return a File instance by parsing a FIT file.

        Parameters:
        ----------
            filename (string): The name of the FIT file including full path.
            measurement_system (DisplayMeasure): The measurement units (metric, statute, etc) to uwe when parsing the FIT file.

        """
        self.filename = filename
        self.measurement_system = measurement_system
        self.message_types = []
        self.messages = []
        for message_type in MessageType:
            vars(self)[message_type.name] = []
        with open(filename, 'rb') as file:
            self.__parse(file)
        self.__sumarize()

    def __parse(self, file):
        logger.debug("Parsing File %s", self.filename)
        self.file_header = FileHeader(file)
        self.data_size = self.file_header.data_size
        self._definition_messages = {}
        self.__dev_fields = {}
        data_consumed = 0
        self.record_count = 0
        data_message_context = DataMessageDecodeContext()
        while self.data_size > data_consumed:
            record_header = RecordHeader(file)
            local_message_num = record_header.local_message()
            data_consumed += record_header.file_size
            self.record_count += 1
            logger.debug("Parsed record %r", record_header)
            if record_header.message_class is MessageClass.definition:
                definition_message = DefinitionMessage(record_header, self.__dev_fields, file)
                logger.debug("  Definition [%d]: %s", local_message_num, definition_message)
                data_consumed += definition_message.file_size
                self._definition_messages[local_message_num] = definition_message
            else:
                definition_message = self._definition_messages[local_message_num]
                data_message = DataMessage(definition_message, file, self.measurement_system, data_message_context)
                logger.debug("  Data [%d]: %s", local_message_num, data_message)
                data_consumed += data_message.file_size
                data_message_type = data_message.type
                if data_message_type == MessageType.field_description:
                    self.__dev_fields[data_message.fields.field_definition_number] = data_message
                logger.debug("Parsed %r", data_message_type)
                self.__save_message(data_message_type, data_message)
            logger.debug("Record %d: consumed %d of %s %r", self.record_count, data_consumed, self.data_size, self.measurement_system)
        self.last_message_timestamp = data_message_context.last_timestamp

    def __save_message(self, data_message_type, data_message):
        if data_message_type.name in vars(self):
            vars(self)[data_message_type.name].append(data_message)
        else:
            vars(self)[data_message_type.name] = [data_message]
        self.messages.append(data_message)
        if data_message_type not in self.message_types:
            self.message_types.append(data_message_type)

    @classmethod
    def __calculate_utc_offset(cls, message):
        time_utc = message.fields.timestamp
        time_local = message.fields.local_timestamp
        return (time_local - time_utc.replace(tzinfo=None)).total_seconds()

    def __sumarize(self):
        first_file_id = self.file_id[0]
        self.time_created = first_file_id.fields.time_created
        self.type = first_file_id.fields.type
        self.product = first_file_id.fields.product
        self.serial_number = first_file_id.fields.serial_number
        self.device = f'{self.product}_{self.serial_number}'
        # File time zone and offset
        if MessageType.device_settings in self.message_types:
            self.utc_offset = self.device_settings[0].fields.time_offset
        elif MessageType.start in self.message_types:
            self.utc_offset = self.__calculate_utc_offset(self.start[0])
        elif MessageType.monitoring_info in self.message_types:
            self.utc_offset = self.__calculate_utc_offset(self.monitoring_info[0])
        else:
            self.utc_offset = 0
        self.local_tz = datetime.timezone(datetime.timedelta(seconds=self.utc_offset))
        self.time_created_local = self.utc_datetime_to_local(self.time_created)
        if self.last_message_timestamp is not None:
            self.time_ended_local = self.utc_datetime_to_local(self.last_message_timestamp)
        else:
            self.time_ended_local = self.time_created_local
        # File start and end times
        if MessageType.start in self.message_types:
            self.start_time = self.start[0].fields.timestamp
        else:
            self.start_time = self.time_created
        if MessageType.end in self.message_types:
            self.end_time = self.end[0].fields.timestamp
        else:
            self.end_time = self.last_message_timestamp
        if MessageType.sport in self.message_types:
            self.sport_type = self.sport[0].fields.sport
            self.sub_sport_type = self.sport[0].fields.sub_sport
        else:
            self.sport_type = None
            self.sub_sport_type = None
        if MessageType.dev_data_id in self.message_types:
            self.dev_application_ids = [dev_data_id.fields.application_id for dev_data_id in self.dev_data_id]
        else:
            self.dev_application_ids = []
        self.dev_fields = {msg.fields.field_name: {'native_message_num': msg.fields.native_message_num, 'units': msg.fields.units}for msg in self.field_description}

    def date_span(self):
        """Return a tuple of the start and end dates of the file."""
        return (self.start_time, self.end_time)

    def utc_datetime_to_local(self, dt):
        """Return a local datetime based on the passed in UTC datetime and the file's known UTC offset."""
        if self.local_tz is not None and dt.tzinfo is datetime.timezone.utc:
            return dt.astimezone(self.local_tz).replace(tzinfo=None)
        return dt.replace(tzinfo=None)

    def __getitem__(self, message_type):
        """Return the attribute named name."""
        return vars(self).get(message_type.name, [])

    def __str__(self):
        """Return a string representation of the class instance."""
        return f'File({repr(self.type)} {self.filename} {self.type} {repr(self.message_types)} dev fields {repr(self.dev_fields)})'
