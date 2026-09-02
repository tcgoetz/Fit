"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.sleep import SleepActivityLevel, SleepDisruptionsSeverity


class SleepActivityLevelField(EnumField):
    """A field that contains Enum of values used to encode activity levels during sleep."""

    _name = 'sleep_activity_level'
    _enum = SleepActivityLevel


class SleepDisruptionsSeveritylField(EnumField):
    """A field that contains Enum of values used to encode disruptions during sleep."""

    _name = 'sleep_disruptions_severity'
    _enum = SleepDisruptionsSeverity
