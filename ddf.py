"""Object that represents a FIT file developer data field."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import collections

import data


class DevDataField(data.Data):
    """Object that represents a FIT file developer data field."""

    def __init__(self, file, definition_message, dev_field_definition, measurement_system):
        self.dev_field_definition = dev_field_definition
        self.measurement_system = measurement_system
        self.field = dev_field_definition.field()
        type = dev_field_definition.type_string()
        count = dev_field_definition.type_count()
        schema = data.Schema(self.field.name, collections.OrderedDict([(self.field.name, [type, count, '%d'])]))
        super(DevDataField, self).__init__(file, schema, None, definition_message.endian)

    def _convert(self):
        self.value_obj = self.field.convert(self.__dict__[self.field.name], self.dev_field_definition.invalid(), self.measurement_system)

    def name(self):
        return self.value_obj.name()

    def _field_value(self):
        return self.value_obj

    def __iter__(self):
        return iter(self.value_obj)

    def keys(self):
        return self.value_obj.keys()

    def items(self):
        return self.value_obj.items()

    def values(self):
        return self.value_obj.values()

    def __str__(self):
        return str(self.value_obj)
