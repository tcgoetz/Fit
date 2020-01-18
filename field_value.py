"""Object that represents a FIT field message field value."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


class FieldValue(object):
    """Object that represents a FIT field message field value."""

    def __init__(self, field, subfield_names=None, **kwargs):
        """Return a FieldValue instance given the field."""
        self.field = field
        self.subfield_names = subfield_names
        vars(self).update(kwargs)

    def is_invalid(self):
        """Return if the field value is valid."""
        return self.field.is_invalid(self.orig, self.invalid)

    def reconvert(self, measurement_system):
        """Redo field conversion based on new information."""
        (self.value, self.orig) = self.field.reconvert(self.orig, self.invalid, measurement_system)

    def __getitem__(self, key):
        return vars(self)[key]

    def __str__(self):
        """Return a string representation of a FieldValue instance."""
        field_string = self.field.name + "("
        if self.is_invalid():
            field_string += "[invalid]"
        else:
            field_string += repr(self.value)
        if self.field.units:
            field_string += " %s" % self.field.units
        if self.value != self.orig:
            field_string += " (%r)" % self.orig
        field_string += ")"
        return field_string

    def __repr__(self):
        """Return a string representation of a FieldValue instance."""
        return str(self)
