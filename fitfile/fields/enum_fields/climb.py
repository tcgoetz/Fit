"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.climb import ClimbProEvent


class ClimbProEventField(EnumField):
    """A field that contains an event from a climbing program."""

    _name = 'climb_pro_event'
    _enum = ClimbProEvent
