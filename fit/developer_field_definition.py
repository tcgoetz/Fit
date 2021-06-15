"""Objects defining FIT file developer fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import collections
import logging

from .data import Schema
from .field_definition import FieldDefinitionBase
from .message_type import MessageType
from .definition_message_data import DefinitionMessageData
from .object_fields import DistanceMetersField, SpeedMpsField
from .dev_field import DevField, DevDistanceField, DerivedDevDistanceField, DevSpeedField, DerivedDevSpeedField
from .exceptions import FitUndefDevMessageType


logger = logging.getLogger(__name__)


class DeveloperFieldDefinition(FieldDefinitionBase):
    """Developer filed definitions decoded from a FIT file."""

    dfd_schema = Schema(
        'DeveloperFieldDefinition',
        collections.OrderedDict(
            [
                ('field_number', ['UINT8', 1]),
                ('size', ['UINT8', 1]),
                ('developer_data_index', ['UINT8', 1])
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
        self.field_number = None
        self.size = None
        self.developer_data_index = None
        super().__init__(file, DeveloperFieldDefinition.dfd_schema)
        self.dev_field_message = dev_field_dict.get(self.field_number)
        if self.dev_field_message is None:
            raise FitUndefDevMessageType(f'Dev field {self.field_number} undefined in {dev_field_dict}')
        # Parse values from dev_field_message
        self.field_name = self.dev_field_message.fields.field_name
        self.native_message_type = MessageType(self.dev_field_message.fields.native_message_num)
        self.native_field_num = self.dev_field_message.fields.native_field_num
        self.units = self.dev_field_message.fields.units
        self.offset = self.dev_field_message.fields.offset
        self.scale = self.dev_field_message.fields.scale
        self.base_type = self.dev_field_message.field_values.fit_base_type_id.orig
        # If the dev field shadows a native field, then take the field name from the native field.
        if self.native_message_type and self.native_field_num:
            field_dict = DefinitionMessageData.get_message_definition(self.native_message_type)
            field = field_dict[self.native_field_num]
            self.display_field_name = 'dev_' + field.name
            self._field = self.__derive_field(self.display_field_name, self.units, self.scale, self.offset, field)
        else:
            self.display_field_name = 'dev_' + self.field_name
            self._field = self.__map_field(self.display_field_name, self.units, self.scale, self.offset)
        logger.info('%s for %r field %s', self, self.native_message_type, self.native_field_num)

    @classmethod
    def __derive_field(cls, field_name, units, scale, offset, field_obj):
        if isinstance(field_obj, DistanceMetersField):
            return DerivedDevDistanceField(field_name, units, scale, offset, field_obj)
        if isinstance(field_obj, SpeedMpsField):
            return DerivedDevSpeedField(field_name, units, scale, offset, field_obj)
        return DevField(field_name, units, scale, offset)

    @classmethod
    def __map_field(cls, field_name, units, scale, offset):
        field_map = {
            'dev_distance'  : DevDistanceField,
            'dev_speed'     : DevSpeedField
        }
        if field_name in field_map:
            return field_map[field_name](field_name, units, scale, offset)
        return DevField(field_name, units, scale, offset)

    def field(self):
        """Return a field instance representing the field for this DeveloperFieldDefinition instance."""
        return self._field

    def __str__(self):
        """Return a string representation for the DeveloperFieldDefinition instance."""
        return (f'{self.__class__.__name__}({self.display_field_name}[{self.field_name}]: '
                + f'scale {self.scale} offset {self.offset} units {self.units}, {self.type_count()} of {self.type_string()})')
