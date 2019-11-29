"""Object that represents a FIT field message field value."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


class FieldValue(object):
    """Object that represents a FIT field message field value."""

    def __init__(self, field, subfield_names=None, **kwargs):
        """Return a FieldValue instance given the field."""
        self.field = field
        self._subfield_names = subfield_names
        self.__dict__.update(kwargs)

    def is_invalid(self):
        """Return if the field value is valid."""
        return self.field.is_invalid(self.orig, self.invalid)

    def subfield_names(self):
        """Return a list of the names of sub-fields."""
        return self._subfield_names

    def type(self):
        """Return the type of the field."""
        return self.field.type

    def reconvert(self, measurement_system):
        """Redo field conversion based on new information."""
        (self.value, self.orig) = self.field.reconvert(self.orig, self.invalid, measurement_system)

    def units(self):
        """Return the units of the field."""
        return self.field.units(self.orig)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __str__(self):
        """Return a string representation of a FieldValue instance."""
        field_string = self.field.name + "("
        if self.is_invalid():
            field_string += "[invalid]"
        else:
            field_string += repr(self.value)
        if self.units():
            field_string += " %s" % self.units()
        if self.value != self.orig:
            field_string += " (%r)" % self.orig
        field_string += ")"
        return field_string

    def __repr__(self):
        """Return a string representation of a FieldValue instance."""
        return str(self)
