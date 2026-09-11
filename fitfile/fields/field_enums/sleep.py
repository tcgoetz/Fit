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

class NapPeriodFeedback(Enum):
    none                                    = 0
    multiple_naps_during_day                = 1
    jetlag_ideal_timing_ideal_duration      = 2
    jetlag_ideal_timing_long_duration       = 3
    jetlag_late_timing_ideal_duration       = 4
    jetlag_late_timing_long_duration        = 5
    ideal_timing_ideal_duration_low_need    = 6
    ideal_timing_ideal_duration_high_need   = 7
    ideal_timing_long_duration_low_need     = 8
    ideal_timing_long_duration_high_need    = 9
    late_timing_ideal_duration_low_need     = 10
    late_timing_ideal_duration_high_need    = 11
    late_timing_long_duration_low_need      = 12
    late_timing_long_duration_high_need     = 13
    ideal_duration_low_need                 = 14
    ideal_duration_high_need                = 15
    long_duration_low_need                  = 16
    long_duration_high_need                 = 17

class NapSource(Enum):
    automatic       = 0
    manual_device   = 1
    manual_gc       = 2
