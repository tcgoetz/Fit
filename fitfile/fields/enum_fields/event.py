"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.event import Event, EventType


class EventField(EnumField):
    """A field that contains an event."""

    _name = 'event'
    _enum = Event


class EventTypeField(EnumField):
    """A field that contains the type of an event."""

    _name = 'event_type'
    _enum = EventType
