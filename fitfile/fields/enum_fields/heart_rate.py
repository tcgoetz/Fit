"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.heart_rate import HeartRateZoneCalc, HeartRateZonesTimerType, HeartRateVarianceStatus


class HeartRateZoneCalcField(EnumField):

    _name = 'hr_calc_type'
    _enum = HeartRateZoneCalc


class HeartRateZonesTimerTypeField(EnumField):
    """A field that contains the type of the Heart Rate Zone Timer."""

    _name = 'hr_zones_timer_type'
    _enum = HeartRateZonesTimerType


class HeartRateVarianceStatusField(EnumField):
    """A field that contains the status of hrv."""

    _name = 'hrv_status'
    _enum = HeartRateVarianceStatus
