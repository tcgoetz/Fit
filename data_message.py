"""FIT file data message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import logging
import datetime

from Fit.data_field import DataField
from Fit.dev_data_field import DevDataField


logger = logging.getLogger(__name__)


class MessageFields(dict):
    """Class holds field names and values."""

    def __getattr__(self, name):
        return self.get(name)


class DataMessageDecodeContext():
    """Class that holds data used across decoding of all DataMessages."""

    def __init__(self):
        self.matched_timestamp_16 = None
        self.last_timestamp = None
        self.last_absolute_timestamp = None


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
            data_field = DataField(fit_file, definition_message, definition_message.field_definitions[index], measurement_system)
            self.file_size += data_field.file_size
            # expand subfields?
            field_value = data_field.value
            if field_value.subfield_names is not None:
                for subfield_name in field_value.subfield_names:
                    subfield_value = field_value[subfield_name]
                    subfield_formal_name = subfield_value.field.name
                    if subfield_formal_name in message_fields:
                        message_fields[subfield_formal_name]._value.value += subfield_value._value.value
                    else:
                        message_fields[subfield_formal_name] = subfield_value
            else:
                message_fields[data_field.name] = field_value
        self.__convert_fields(message_fields, measurement_system)
        self.__convert_dev_fields(fit_file, measurement_system)
        self.__track_time()

    def __add_field(self, field_value):
        field_name = field_value.field.name.lower()
        self.fields[field_name] = field_value.value
        self.field_values[field_name] = field_value

    def __control_field_value(self, field, message_fields, control_field_name):
        control_field = message_fields.get(control_field_name)
        if control_field is not None:
            return control_field.value
        logger.debug('Missing control field %s for %r in message %r', control_field_name, field, message_fields)

    def __convert_fields(self, message_fields, measurement_system):
        for field_value in message_fields.values():
            field = field_value.field
            dependant_field_func = getattr(field, 'dependant_field', None)
            if dependant_field_func:
                control_values = [self.__control_field_value(field, message_fields, control_field) for control_field in field._dependant_field_control_fields]
                field_value.field = dependant_field_func(control_values)
                field_value.reconvert(measurement_system)
            self.__add_field(field_value)

    def __convert_dev_fields(self, fit_file, measurement_system):
        if self.__definition_message.has_dev_fields:
            for index in range(self.__definition_message.dev_fields):
                dev_data_field = DevDataField(fit_file, self.__definition_message, self.__definition_message.dev_field_definitions[index],
                                              measurement_system)
                self.file_size += dev_data_field.file_size
                self.__add_field(dev_data_field._field_value())

    def __track_time(self):
        if 'timestamp' in self.fields:
            self.__context.last_timestamp = self.fields.timestamp
            self.__context.last_absolute_timestamp = self.fields.timestamp
            self.__context.matched_timestamp_16 = None
        elif 'timestamp_16' in self.fields:
            timestamp_16 = self.fields.timestamp_16
            if timestamp_16 is not None:
                self.__context.last_timestamp = self.__timestamp16_to_timestamp(timestamp_16)
                self.fields['timestamp'] = self.__context.last_timestamp
            else:
                # This should not happen, if the timestamp16 field exists, it should not be None
                # Issue #21: seen on Ubuntu on Windows
                logger.error('timestamp16 with value None: %r', self.__fields)
                self.fields.add('timestamp', self.__context.last_timestamp)

    def __timestamp16_to_timestamp(self, timestamp_16):
        if self.__context.matched_timestamp_16:
            if timestamp_16 >= self.__context.matched_timestamp_16:
                delta = timestamp_16 - self.__context.matched_timestamp_16
            else:
                delta = (self.__context.matched_timestamp_16 - 65535) + timestamp_16
        else:
            self.__context.matched_timestamp_16 = timestamp_16
            delta = 0
        return self.__context.last_absolute_timestamp + datetime.timedelta(seconds=delta)

    @property
    def type(self):
        """Return the message type."""
        return self.__definition_message.message_type

    def __str__(self):
        """Return a string representation of a DataMessage instance."""
        fields_str = "".join(["%s, " % value for value in self.field_values.values()])
        return f'{self.__class__.__name__}: {repr(self.type)}: {fields_str}'

    def __repr__(self):
        """Return a string representation of a DataMessage instance."""
        return f'{self.__class__.__name__}({repr(self.type)}: {repr(self.field_values)})'
