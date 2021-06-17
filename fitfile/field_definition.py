"""Object that defines the structure of a FIT file message field."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import collections

from .data import Data, Schema
from .base_type import BaseType


class FieldDefinitionBase(Data, BaseType):
    """Base object that defines the structure of a FIT file message field."""

    base_type = None
    size = None

    def invalid(self):
        """Return the invalid value for the field."""
        return self._invalid(self.base_type)

    def type_string(self):
        """Return the type string for the field."""
        return self._type_string(self.base_type)

    def type_count(self):
        """Return the number of values for the field."""
        type_size = Schema.type_to_size[self.type_string()]
        return int(self.size / type_size)


class FieldDefinition(FieldDefinitionBase):
    """Object that defines the structure of a FIT file message field."""

    field_definition_number = None
    size = None
    base_type = None

    fd_schema = Schema(
        'FieldDefinition',
        collections.OrderedDict(
            [
                ('field_definition_number', ['UINT8', 1]),
                ('size', ['UINT8', 1]),
                ('base_type', ['UINT8', 1])
            ]
        )
    )

    def __init__(self, file):
        """
        Return a FieldDefinition instance created by reading data from a FIT file.

        Paramters:
        ---------
            file (File):  a FIT File instance.
        """
        super().__init__(file, FieldDefinition.fd_schema)

    def __str__(self):
        """Return a string representation for the FieldDefinition instance."""
        return f'FieldDefinition: type {self.field_definition_number}: {self.type_count()} of {self.type_string()}'
