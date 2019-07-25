"""Object that defines the structure of a FIT file message field."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import collections

import data
import base_type


class FieldDefinition(data.Data, base_type.BaseType):
    """Object that defines the structure of a FIT file message field."""

    fd_schema = data.Schema(
        'fd',
        collections.OrderedDict(
            [
                ('field_definition_number', ['UINT8', 1, '%x']),
                ('size', ['UINT8', 1, '%x']),
                ('base_type', ['UINT8', 1, '%x'])
            ]
        )
    )

    def __init__(self, file):
        """
        Return a FieldDefinition instance created by reading data from a FIT file.

        Paramters:
            file (File):  a FIT File instance.
        """
        super(FieldDefinition, self).__init__(file, FieldDefinition.fd_schema)

    def base_type(self):
        """Return the base type for the field."""
        return self._base_type(self.base_type)

    def type_endian(self):
        """Return the endian value for the field."""
        return self._type_endian(self.base_type)

    def type_name(self):
        """Return the type name for the field."""
        return self._type_name(self.base_type)

    def invalid(self):
        """Return the invalid value for the field."""
        return self._invalid(self.base_type)

    def type_string(self):
        """Return the type string for the field."""
        return self._type_string(self.base_type)

    def type_count(self):
        """Return the number of values for the field."""
        type_size = data.Schema.type_to_size(self.type_string())
        return (self.size / type_size)

    def __str__(self):
        """Return a string representation for the FieldDefinition instance."""
        return ("FieldDefinition: type %d: %d of %s" % (self.field_definition_number, self.type_count(), self.type_string()))
