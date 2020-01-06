"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.fields import Field
import Fit.field_enums as fe


class EnumField(Field):
    """Base class for a field that can be represented by an enum value."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _convert_single(self, value, invalid):
        return self.enum.from_string(value)


class SwitchField(EnumField):
    enum = fe.Switch


class FitBaseUnitField(EnumField):
    enum = fe.FitBaseUnit


class DisplayMeasureField(EnumField):
    enum = fe.DisplayMeasure


class DisplayHeartField(EnumField):
    enum = fe.DisplayHeart


class DisplayPositionField(EnumField):
    enum = fe.DisplayPosition


#
# Hardware related fields
#
class HeartRateZoneCalcField(EnumField):
    enum = fe.HeartRateZoneCalc

    def __init__(self):
        super().__init__('hr_calc_type')


class PowerCalcField(EnumField):
    enum = fe.PowerCalc

    def __init__(self):
        super().__init__('pwr_calc_type')


class DateModeField(EnumField):
    enum = fe.DateMode

    def __init__(self, *args, **kwargs):
        super().__init__(name='date_mode', *args, **kwargs)


class TimeModeField(EnumField):
    enum = fe.TimeMode

    def __init__(self, *args, **kwargs):
        super().__init__(name='time_mode', *args, **kwargs)


class FileTypeField(EnumField):
    """A field that indicates the FIT file type."""

    enum = fe.FileType


class EventField(EnumField):
    """A field that contains an event."""

    enum = fe.Event


class EventTypeField(EnumField):
    """A field that contains the type of an event."""

    enum = fe.EventType


class LapTriggerField(EnumField):
    """A field that indicates why a lap was started."""

    enum = fe.LapTrigger


class SessionTriggerField(EnumField):
    """A field that indicates why a session was started."""

    enum = fe.SessionTrigger
