"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import Enum


class HeartRateZoneCalc(Enum):
    custom                      = 0
    percent_max_hr              = 1
    percent_hr_reserve          = 2
    percent_lactate_threshhold  = 3
    invalid                     = 255


class HeartRateZonesTimerType(Enum):
    """Gives the type of the Heart Rate Zone Timer."""

    session = 18
    lap = 19


class HeartRateVarianceStatus(Enum):
    """Gives the type of the Heart Rate Zone Timer."""

    none        = 0
    poor        = 1
    low         = 2
    unbalanced  = 3
    balanced    = 4
