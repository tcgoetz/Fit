"""Objects defining FIT file developer fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import collections

from Fit.data import Data, Schema
from Fit.base_type import BaseType
import Fit.fields as fields
from Fit.exceptions import FitUndefDevMessageType


class DeveloperFieldDefinition(Data, BaseType):
    """Developer filed definitions decoded from a FIT file."""

    dfd_schema = Schema(
        'dfd_schema',
        collections.OrderedDict(
            [
                ('field_number', ['UINT8', 1, '%x']),
                ('size', ['UINT8', 1, '%x']),
                ('developer_data_index', ['UINT8', 1, '%x'])
            ]
        )
    )

    def __init__(self, dev_field_dict, file):
        """
        Return a DeveloperFieldDefinition instance created by reading data from a FIT file.

        Paramters:
            dev_field_dict (dict): a dictionary of developer defined fields.
            file (File):  a FIT File instance.
        """
        super().__init__(file, DeveloperFieldDefinition.dfd_schema)
        self.dev_field = dev_field_dict.get(self.field_number)
        if self.dev_field is None:
            raise FitUndefDevMessageType('Dev field %d undefined in %r' % (self.field_number, dev_field_dict))
        self.field_name = self.dev_field['field_name'].value
        self.native_message_num = self.dev_field['native_message_num'].value
        self.native_field_num = self.dev_field['native_field_num'].value
        self.units = self.dev_field['units'].value
        self.offset = self.dev_field['offset'].value
        self.scale = self.dev_field['scale'].value

    def __base_type_value(self):
        return self.dev_field['fit_base_type_id'].orig

    def field(self):
        """Return a DevField instance representing the field for this DeveloperFieldDefinition instance."""
        # if self.native_message_num is not None and self.native_field_num is not None:
        #     message_data = DefinitionMessageData.get_message(self.native_message_num)
        #     field_dict = message_data[1]
        #     return field_dict[self.native_field_num]
        return fields.DevField('dev_' + self.field_name, self.units, self.scale, self.offset)

    def base_type(self):
        """Return the base type for the field."""
        return self._base_type(self.__base_type_value())

    def type_endian(self):
        """Return the endian value for the field."""
        return self._type_endian(self.__base_type_value())

    def type_name(self):
        """Return the type name for the field."""
        return self._type_name(self.__base_type_value())

    def invalid(self):
        """Return the invalid value for the field."""
        return self._invalid(self.__base_type_value())

    def type_string(self):
        """Return the type string for the field."""
        return self._type_string(self.__base_type_value())

    def type_count(self):
        """Return the number of values for the field."""
        type_size = Schema.type_to_size(self.type_string())
        return int(self.size / type_size)

    def __str__(self):
        """Return a string representation for the DeveloperFieldDefinition instance."""
        return f'{self.__class__.__name__}: type {self.field_number}: {self.developer_data_index} {self.type_count()} of {self.type_string()}'
