"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.fields import NamedField
import Fit.field_enums as fe
import Fit.file_type as ft


class EnumField(NamedField):
    """Base class for a field that can be represented by an enum value."""

    _enum = None

    def _convert_single(self, value, invalid):
        return self._enum.from_string(value)


class SwitchField(EnumField):
    """A field whose value can be represented by a Switch enum."""

    _enum = fe.Switch


class FitBaseUnitField(EnumField):

    _enum = fe.FitBaseUnit


class DisplayMeasureField(EnumField):

    _enum = fe.DisplayMeasure


class DisplayHeartField(EnumField):

    _enum = fe.DisplayHeart


class DisplayPositionField(EnumField):

    _name = 'position_setting'
    _enum = fe.DisplayPosition


#
# Hardware related fields
#
class HeartRateZoneCalcField(EnumField):

    _name = 'hr_calc_type'
    _enum = fe.HeartRateZoneCalc


class PowerCalcField(EnumField):

    _name = 'pwr_calc_type'
    _enum = fe.PowerCalc


class DateModeField(EnumField):

    _name = 'date_mode'
    _enum = fe.DateMode


class TimeModeField(EnumField):

    _name = 'time_mode'
    _enum = fe.TimeMode


class FileTypeField(EnumField):
    """A field that indicates the FIT file type."""

    _name = 'file_type'
    _enum = ft.FileType


class EventField(EnumField):
    """A field that contains an event."""

    _name = 'event'
    _enum = fe.Event


class EventTypeField(EnumField):
    """A field that contains the type of an event."""

    _name = 'event_type'
    _enum = fe.EventType


class LapTriggerField(EnumField):
    """A field that indicates why a lap was started."""

    _name = 'lap_trigger'
    _enum = fe.LapTrigger


class SessionTriggerField(EnumField):
    """A field that indicates why a session was started."""

    _name = 'session_trigger'
    _enum = fe.SessionTrigger


class ClimbProEventField(EnumField):
    """A field that contains an event from a climbing program."""

    _name = 'climb_pro_event'
    _enum = fe.ClimbProEvent
