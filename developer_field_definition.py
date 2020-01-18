"""Objects defining FIT file developer fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import collections
import logging

from Fit.data import Schema
from Fit.field_definition import FieldDefinitionBase
from Fit.message_type import MessageType
from Fit.definition_message_data import DefinitionMessageData
from Fit.object_fields import DistanceMetersField, SpeedMpsField
from Fit.dev_field import DevField, DevDistanceField, DerivedDevDistanceField, DevSpeedField, DerivedDevSpeedField
from Fit.exceptions import FitUndefDevMessageType


logger = logging.getLogger(__name__)


class DeveloperFieldDefinition(FieldDefinitionBase):
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
        self.dev_field_message = dev_field_dict.get(self.field_number)
        if self.dev_field_message is None:
            raise FitUndefDevMessageType('Dev field %d undefined in %r' % (self.field_number, dev_field_dict))
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
            self._field = self.derive_field(self.display_field_name, self.units, self.scale, self.offset, field)
        else:
            self.display_field_name = 'dev_' + self.field_name
            self._field = self.map_field(self.display_field_name, self.units, self.scale, self.offset)
        logger.info('%s for %r field %s', self, self.native_message_type, self.native_field_num)

    @classmethod
    def derive_field(cls, field_name, units, scale, offset, field_obj):
        if isinstance(field_obj, DistanceMetersField):
            return DerivedDevDistanceField(field_name, units, scale, offset, field_obj)
        if isinstance(field_obj, SpeedMpsField):
            return DerivedDevSpeedField(field_name, units, scale, offset, field_obj)
        return DevField(field_name, units, scale, offset)

    @classmethod
    def map_field(cls, field_name, units, scale, offset):
        field_map = {
            'dev_distance'  : DevDistanceField,
            'dev_speed'     : DevSpeedField
        }
        field = field_map.get(field_name)
        if field is not None:
            return field(field_name, units, scale, offset)
        return DevField(field_name, units, scale, offset)

    def field(self):
        """Return a field instance representing the field for this DeveloperFieldDefinition instance."""
        return self._field

    def __str__(self):
        """Return a string representation for the DeveloperFieldDefinition instance."""
        return (f'{self.__class__.__name__}({self.display_field_name}[{self.field_name}]: '
                + f'scale {self.scale} offset {self.offset}, {self.type_count()} of {self.type_string()})')
