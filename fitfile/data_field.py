"""FIT file data field."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import collections

from .data import Data, Schema
from .exceptions import FitDataFieldConvertError


class DataField(Data):
    """FIT file data field."""

    field_value = None
    __schema_cache = {}

    def __init__(self, file, definition_message, field_definition, measurement_system):
        """Return an instance of the DataField class."""
        self.field_definition = field_definition
        self.measurement_system = measurement_system
        self.field = definition_message.field(field_definition.field_definition_number)
        schema = self.__get_schema(field_definition.type_string(), field_definition.type_count())
        super().__init__(file, schema, None, definition_message.endian)

    def __populate_schema_cache(self, schema_sig, type, count):
        """Cache schema on the assumption that the set of schemas is much smaller than the number of times they are used."""
        schema = Schema(schema_sig, collections.OrderedDict([('field_value', [type, count])]))
        self.__schema_cache[schema_sig] = schema
        return schema

    def __get_schema(self, type, count):
        schema_sig = f'{type}_{count}'
        if schema_sig in self.__schema_cache:
            return self.__schema_cache[schema_sig]
        return self.__populate_schema_cache(schema_sig, type, count)

    def _convert(self):
        try:
            self.values = self.field.convert(self.field_value, self.field_definition.invalid(), self.measurement_system)
        except Exception as e:
            raise FitDataFieldConvertError(self.field_value, self.field, e)

    def __str__(self):
        """Return a string representation of the DataField instance."""
        return f'{self.field_definition.type_string()} {self.values[0] if len(self.values) == 1 else self.values}'

    def __repr__(self):
        return self.__str__()


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
