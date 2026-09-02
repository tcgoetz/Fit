"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import Enum


class SleepActivityLevel(Enum):
    """Enum of values used to encode activity levels during sleep."""

    unmeasurable = 0
    awake = 1
    light_sleep = 2
    deep_sleep = 3
    rem_sleep = 4


class SleepDisruptionsSeverity(Enum):
    """Enum of values used to encode activity levels during sleep."""

    none    = 0
    low     = 1
    medium  = 2
    high    = 3
    invalid = 255
