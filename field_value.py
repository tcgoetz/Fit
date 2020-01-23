"""Object that represents a FIT field message field value."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


class FieldValue(dict):
    """Object that represents a FIT field message field value."""

    def __init__(self, field, orig, invalid, **kwargs):
        """Return a FieldValue instance given the field."""
        self.field = field
        self.orig = orig
        self.invalid = invalid
        self.update(kwargs)

    def first(self):
        """Return the first value. Most of the time there is only one."""
        return next(iter(self.values()))

    def is_invalid(self):
        """Return if the field value is valid."""
        return self.field.is_invalid(self.orig, self.invalid)

    def reconvert(self, measurement_system):
        """Redo field conversion based on new information."""
        self.update(self.field.reconvert(self.orig, self.invalid, measurement_system))

    def __str__(self):
        """Return a string representation of a FieldValue instance."""
        field_string = ""
        for field_name, value in self.items():
            field_string = field_name + "("
            if self.is_invalid():
                field_string += "[invalid]"
            else:
                field_string += repr(value)
            if self.field.units:
                field_string += " %s" % self.field.units
            if value != self.orig:
                field_string += " (%r)" % self.orig
            field_string += ")"
        return field_string

    def __repr__(self):
        """Return a string representation of a FieldValue instance."""
        return str(self)
