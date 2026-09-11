"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.sleep import SleepActivityLevel, SleepDisruptionsSeverity, NapPeriodFeedback, NapSource


class SleepActivityLevelField(EnumField):
    """A field that contains Enum of values used to encode activity levels during sleep."""

    _name = 'sleep_activity_level'
    _enum = SleepActivityLevel


class SleepDisruptionsSeveritylField(EnumField):
    """A field that contains Enum of values used to encode disruptions during sleep."""

    _name = 'sleep_disruptions_severity'
    _enum = SleepDisruptionsSeverity


class NapPeriodFeedbackField(EnumField):
    """A field that contains Enum of values used to encode nap data."""

    _name = 'nap_period_feedback'
    _enum = NapPeriodFeedback


class NapSourceField(EnumField):
    """A field that contains Enum of values used to encode nap data."""

    _name = 'nap_source'
    _enum = NapSource
