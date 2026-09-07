"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.activity import Activity, ActivityType, LapTrigger, PowerCalc, PowerZoneCalc, SessionTrigger, Benefit, AutoLapMode, PowerAveraging, \
    Spo2MeasurementType, SwimStroke, LengthType, SplitType


class ActivityField(EnumField):
    """A field holding an activity as a integer enum value."""

    _name = 'activity'
    _enum = Activity


class ActivityTypeField(EnumField):
    """A field holding an activity type as a integer enum value."""

    _name = 'activity_type'
    _enum = ActivityType


class LapTriggerField(EnumField):
    """A field that indicates why a lap was started."""

    _name = 'lap_trigger'
    _enum = LapTrigger


class AutoLapModeField(EnumField):
    """A field that indicates why a lap was started."""

    _name = 'auto_lap_mode'
    _enum = AutoLapMode


class PowerCalcField(EnumField):

    _name = 'pwr_calc_type'
    _enum = PowerCalc


class SessionTriggerField(EnumField):
    """A field that indicates why a session was started."""

    _name = 'session_trigger'
    _enum = SessionTrigger


class PowerZoneCalcField(EnumField):

    _name = 'pwr_calc_type'
    _enum = PowerZoneCalc


class PowerAveragingField(EnumField):

    _name = 'power_averaging'
    _enum = PowerAveraging


class BenefitField(EnumField):

    _name = 'pwr_calc_type'
    _enum = Benefit


class Spo2MeasurementTypeField(EnumField):

    _name = 'spo2_measurement_type'
    _enum = Spo2MeasurementType


class SwimStrokeField(EnumField):

    _name = 'swim_stroke'
    _enum = SwimStroke


class LengthTypeField(EnumField):

    _name = 'length_type'
    _enum = LengthType


class SplitTypeField(EnumField):

    _name = 'split_type'
    _enum = SplitType
