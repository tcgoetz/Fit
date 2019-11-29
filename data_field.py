"""FIT file data field."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import collections

from Fit.data import Data, Schema


class DataField(Data):
    """FIT file data field."""

    __schema_cache = {}

    def __init__(self, file, definition_message, field_definition, measurement_system):
        """Return an instance of the DataField class."""
        self.field_definition = field_definition
        self.measurement_system = measurement_system
        self.field = definition_message.field(field_definition.field_definition_number)
        schema = self.__get_schema(self.field.name, field_definition.type_string(), field_definition.type_count())
        super().__init__(file, schema, None, definition_message.endian)

    def __populate_schema_cache(self, schema_sig, field_name, type, count):
        """Cache schema on the assumption that the set of schemas is much smaller than the number of times they are used."""
        schema = Schema(field_name, collections.OrderedDict([(field_name, [type, count, '%d'])]))
        self.__schema_cache[schema_sig] = schema
        return schema

    def __get_schema(self, field_name, type, count):
        schema_sig = f'{field_name}_{type}_{count}'
        schema = self.__schema_cache.get(schema_sig)
        if schema is not None:
            return schema
        return self.__populate_schema_cache(schema_sig, field_name, type, count)

    def _convert(self):
        self.value_obj = self.field.convert(self.__dict__[self.field.name], self.field_definition.invalid(), self.measurement_system)

    def _field_name(self):
        return self.value_obj.field.name

    def _field_value(self):
        return self.value_obj

    def __iter__(self):
        """Iterate over the data field's data."""
        return iter(self.value_obj)

    def keys(self):
        """Return the keys to the value object dictionary."""
        return self.value_obj.keys()

    def items(self):
        """Return the key-value pairs for the value object dictionary."""
        return self.value_obj.items()

    def values(self):
        """Return the values to the value object dictionary."""
        return self.value_obj.values()

    def __str__(self):
        """Return a string reprsentation of the DataField instance."""
        return f'<DataField: {self.value_obj}'
