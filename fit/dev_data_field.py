"""Object that represents a FIT file developer data field."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import collections

from .data import Data, Schema


class DevDataField(Data):
    """Object that represents a FIT file developer data field."""

    def __init__(self, file, definition_message, dev_field_definition, measurement_system):
        """Return a new DevDataField instance created by reading the FIT file and applying the supplied definitions."""
        self.dev_field_definition = dev_field_definition
        self.measurement_system = measurement_system
        self.field = dev_field_definition.field()
        type = dev_field_definition.type_string()
        count = dev_field_definition.type_count()
        self.field_value = None
        schema = Schema('DevDataField', collections.OrderedDict([('field_value', [type, count])]))
        super().__init__(file, schema, None, definition_message.endian)

    def _convert(self):
        self.value = self.field.convert(self.field_value, self.dev_field_definition.invalid(), self.measurement_system)[0]

    def __str__(self):
        """Return a string representation of the DevDataField instance."""
        return str(self.value)
