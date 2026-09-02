"""Objects that represent FIT file enum fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..field import NamedField


class EnumField(NamedField):
    """Base class for a field that can be represented by an enum value."""

    _enum = None
    _default = None

    def _convert_single(self, value, invalid=None):
        return self._enum.from_string(value, self._default)
