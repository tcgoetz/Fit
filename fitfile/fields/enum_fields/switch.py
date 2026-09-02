"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.switch import Switch


class SwitchField(EnumField):
    """A field whose value can be represented by a Switch enum."""

    _enum = Switch
