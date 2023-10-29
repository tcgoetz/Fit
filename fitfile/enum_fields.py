"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .fields import NamedField
from .field_enums import FitBaseUnit, Switch, DisplayMeasure, DisplayHeart, DisplayPosition, HeartRateZoneCalc, PowerCalc, DateMode, TimeMode, Event, EventType, LapTrigger, \
    SessionTrigger, ClimbProEvent, HeartRateZonesTimerType, HeartRateZonesMethod, SleepActivityLevel
from .file_type import FileType


class EnumField(NamedField):
    """Base class for a field that can be represented by an enum value."""

    _enum = None
    _default = None

    def _convert_single(self, value, invalid=None):
        return self._enum.from_string(value, self._default)


class SwitchField(EnumField):
    """A field whose value can be represented by a Switch enum."""

    _enum = Switch


class FitBaseUnitField(EnumField):

    _enum = FitBaseUnit


class DisplayMeasureField(EnumField):

    _enum = DisplayMeasure


class DisplayHeartField(EnumField):

    _enum = DisplayHeart


class DisplayPositionField(EnumField):

    _name = 'position_setting'
    _enum = DisplayPosition


#
# Hardware related fields
#
class HeartRateZoneCalcField(EnumField):

    _name = 'hr_calc_type'
    _enum = HeartRateZoneCalc


class PowerCalcField(EnumField):

    _name = 'pwr_calc_type'
    _enum = PowerCalc


class DateModeField(EnumField):

    _name = 'date_mode'
    _enum = DateMode


class TimeModeField(EnumField):

    _name = 'time_mode'
    _enum = TimeMode


class FileTypeField(EnumField):
    """A field that indicates the FIT file type."""

    _name = 'file_type'
    _enum = FileType


class EventField(EnumField):
    """A field that contains an event."""

    _name = 'event'
    _enum = Event


class EventTypeField(EnumField):
    """A field that contains the type of an event."""

    _name = 'event_type'
    _enum = EventType


class LapTriggerField(EnumField):
    """A field that indicates why a lap was started."""

    _name = 'lap_trigger'
    _enum = LapTrigger


class SessionTriggerField(EnumField):
    """A field that indicates why a session was started."""

    _name = 'session_trigger'
    _enum = SessionTrigger


class ClimbProEventField(EnumField):
    """A field that contains an event from a climbing program."""

    _name = 'climb_pro_event'
    _enum = ClimbProEvent


class HeartRateZonesTimerTypeField(EnumField):
    """A field that contains the type of the Heart Rate Zone Timer."""

    _name = 'hr_zones_timer_type'
    _enum = HeartRateZonesTimerType


class HeartRateZonesMethodField(EnumField):
    """A field that contains the method used to calculate the heart rate zones."""

    _name = 'hr_zones_method'
    _enum = HeartRateZonesMethod


class SleepActivityLevelField(EnumField):
    """A field that contains Enum of values used to encode activity levels during sleep."""

    _name = 'sleep_activity_level'
    _enum = SleepActivityLevel
