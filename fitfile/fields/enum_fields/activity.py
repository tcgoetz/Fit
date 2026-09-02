"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.activity import Activity, ActivityType, Sport, SubSport, LapTrigger, PowerCalc, PowerZoneCalc, SessionTrigger, Benefit, AutoLapMode, AutoPauseSetting, \
    PowerAveraging, AutoScrollMode


class ActivityField(EnumField):
    """A field holding an activity as a integer enum value."""

    _name = 'activity'
    _enum = Activity


class ActivityTypeField(EnumField):
    """A field holding an activity type as a integer enum value."""

    _name = 'activity_type'
    _enum = ActivityType


class SportField(EnumField):
    """A field representing a sport via an ineger enum value."""

    _name = 'sport'
    _enum = Sport
    _units = {
        0 : 'cycles',
        1 : 'steps',
        2 : 'strokes',
        5 : 'strokes',
        11 : 'steps',
        15 : 'strokes',
        17 : 'steps',
        19 : 'strokes',
        37 : 'strokes',
    }

    @classmethod
    def units(cls, sport_index):
        """Return the proper units for an activity given the sport index."""
        try:
            return cls._units[sport_index]
        except Exception:
            return cls._units[0]


class SubSportField(EnumField):
    """A field representing a sub-sport via an ineger enum value."""

    _name = 'sub_sport'
    _enum = SubSport


class LapTriggerField(EnumField):
    """A field that indicates why a lap was started."""

    _name = 'lap_trigger'
    _enum = LapTrigger


class AutoLapModeField(EnumField):
    """A field that indicates why a lap was started."""

    _name = 'auto_lap_mode'
    _enum = AutoLapMode


class AutoPauseSettingField(EnumField):
    """A field that indicates when to pause."""

    _name = 'auto_pause'
    _enum = AutoPauseSetting


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


class AutoScrollModeField(EnumField):

    _name = 'auto_scroll'
    _enum = AutoScrollMode
