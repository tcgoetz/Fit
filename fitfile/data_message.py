"""FIT file data message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import logging
import datetime

from .data_field import DataField
from .dev_data_field import DevDataField
from .exceptions import FitMessageParse


logger = logging.getLogger(__name__)


class MessageFields(dict):
    """Class holds field names and values."""

    def __getattr__(self, name):
        return self.get(name)


class DataMessageDecodeContext():
    """Class that holds data used across decoding of all DataMessages."""

    def __init__(self):
        """Return a DataMessageDecodeContext instance."""
        self.matched_timestamp_16 = None
        self.last_timestamp = None
        self.last_absolute_timestamp = None

    def absolute_timestamp(self, absolute_timestamp):
        """Update the context given an absolute timestamp."""
        self.last_timestamp = absolute_timestamp
        self.last_absolute_timestamp = absolute_timestamp
        self.matched_timestamp_16 = None

    def timestamp16_to_timestamp(self, timestamp_16):
        """Calculate an absolute timestamp given a relative timestamp16."""
        if self.matched_timestamp_16:
            if timestamp_16 >= self.matched_timestamp_16:
                delta = timestamp_16 - self.matched_timestamp_16
            else:
                delta = (self.matched_timestamp_16 - 65535) + timestamp_16
        else:
            self.matched_timestamp_16 = timestamp_16
            delta = 0
        self.last_timestamp = self.last_absolute_timestamp + datetime.timedelta(seconds=delta)
        return self.last_timestamp


class DataMessage():
    """Class decodes and holds a FIT file data message."""

    def __init__(self, definition_message, fit_file, measurement_system, context):
        """Return a DataMessage instance decoded from the supplied FIT file using the supplied definition message."""
        self.__definition_message = definition_message
        self.__context = context
        self.fields = MessageFields()
        self.field_values = MessageFields()
        self.file_size = 0
        message_fields = {}
        for index in range(definition_message.fields):
            try:
                data_field = DataField(fit_file, definition_message, definition_message.field_definitions[index], measurement_system)
            except Exception as e:
                raise FitMessageParse(self, e)
            self.file_size += data_field.file_size
            for field_value in data_field.values:
                message_fields[field_value.field.name] = field_value
        self.__convert_fields(message_fields, measurement_system)
        self.__convert_dev_fields(fit_file, measurement_system)
        self.__track_time()

    def __add_field(self, field_value):
        field_name = field_value.field.name.lower()
        self.fields.update(field_value)
        self.field_values[field_name] = field_value

    def __control_field_value(self, field, message_fields, control_field_name):
        if control_field_name in message_fields:
            return message_fields[control_field_name].first()

    def __convert_fields(self, message_fields, measurement_system):
        for field_value in message_fields.values():
            field = field_value.field
            if field._dependant_field_control_fields:
                control_values = [self.__control_field_value(field, message_fields, control_field) for control_field in field._dependant_field_control_fields]
                field_value.field = field.dependant_field(control_values)
                field_value.reconvert(measurement_system)
            self.__add_field(field_value)

    def __convert_dev_fields(self, fit_file, measurement_system):
        if self.__definition_message.has_dev_fields:
            for index in range(self.__definition_message.dev_fields):
                dev_data_field = DevDataField(fit_file, self.__definition_message, self.__definition_message.dev_field_definitions[index], measurement_system)
                self.file_size += dev_data_field.file_size
                self.__add_field(dev_data_field.value)

    def __track_time(self):
        if 'timestamp' in self.fields:
            self.__context.absolute_timestamp(self.fields.timestamp)
        elif 'timestamp_16' in self.fields:
            timestamp_16 = self.fields.timestamp_16
            if timestamp_16 is not None:
                self.fields['timestamp'] = self.__context.timestamp16_to_timestamp(timestamp_16)
            else:
                # This should not happen, if the timestamp16 field exists, it should not be None
                # Issue #21: seen on Ubuntu on Windows
                logger.error('timestamp16 with value None: %r', self.fields)
                self.fields.add('timestamp', self.__context.last_timestamp)

    @property
    def type(self):
        """Return the message type."""
        return self.__definition_message.message_type

    def __str__(self):
        """Return a string representation of a DataMessage instance."""
        return f'{self.__class__.__name__}: {repr(self.type)}: {str(self.fields)}'

    def __repr__(self):
        """Return a string representation of a DataMessage instance."""
        # we reformat the values with a list comprehension to avoid the .values() showing up as a generator in the repr output
        return f'{self.__class__.__name__}({repr(self.type)}: {repr(list(self.field_values.values()))})'
