"""Objects that represent FIT file message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import time
import datetime

import Fit.conversions as conversions
import Fit.field_enums as fe
from Fit.field_value import FieldValue
from Fit.field_definition import FieldDefinition


class Field(object):
    """The base object for all FIT file message fields."""

    _units = [None, None]
    # for measurment system independant conversion
    _scale = 1.0
    _offset = 0.0
    # for measurement system dependant conversion
    _conversion_factor = [1, 1]
    _conversion_constant = [0, 0]

    def __init__(self, **kwargs):
        """Return a new instance of the Field class."""
        for key, value in kwargs.items():
            self.__dict__['_' + key] = value
        if not hasattr(self, '_name'):
            raise ValueError(f'Unamed instance of {self.__class__.__name__}')
        self._subfield = {}

    @property
    def name(self):
        """Return the name of the field."""
        return self._name

    def units(self, value):
        """Return the units of the field."""
        if self._units[self.measurement_system.value]:
            return self._convert_many_units(value, None)

    def _invalid_single(self, value, invalid):
        return (value == invalid)

    def _invalid_many(self, values, invalid):
        for value in values:
            if self._invalid_single(value, invalid):
                return True
        return False

    def is_invalid(self, value, invalid):
        """Return if the field's value is valid."""
        if isinstance(value, list):
            return self._invalid_many(value, invalid)
        return self._invalid_single(value, invalid)

    def _convert_single(self, value, invalid):
        if value != invalid:
            return (value / self._conversion_factor[self.measurement_system.value]) + self._conversion_constant[self.measurement_system.value]

    def __convert_many(self, _convert_single, value, invalid):
        if isinstance(value, list):
            return [_convert_single(sub_value, invalid) for sub_value in value]
        return _convert_single(value, invalid)

    def _convert_many(self, value, invalid):
        return self.__convert_many(self._convert_single, value, invalid)

    def _convert_single_units(self, value, invalid):
        return self._units[self.measurement_system.value]

    def _convert_many_units(self, value, invalid):
        return self.__convert_many(self._convert_single_units, value, invalid)

    def convert(self, value, invalid, measurement_system=fe.DisplayMeasure.metric):
        """Return a FieldValue as intepretted by the field's rules."""
        self.measurement_system = measurement_system
        return FieldValue(self, invalid=invalid, value=self._convert_many(value, invalid), orig=value)

    def reconvert(self, value, invalid, measurement_system=fe.DisplayMeasure.metric):
        """Return the field's value as intepretted by the field's rules."""
        self.measurement_system = measurement_system
        return (self._convert_many(value, invalid), value)

    def __repr__(self):
        """Return a string representation of a Field instance."""
        return f'{self.__class__.__name__} ({self.name})'


class NamedField(Field):

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            super().__init__(name=args[0], **kwargs)
        else:
            super().__init__(**kwargs)


#
# Special fields
#
class UnknownField(Field):
    """Class that handles fields that are not documented."""

    def __init__(self, index):
        """Return a new instance of the UnknownField class."""
        super().__init__(name=f"unknown_{index}")


#
# Basic field types
#
class LeftRightBalanceField(NamedField):

    def _convert_single(self, value, invalid):
        if value != invalid:
            if value & 0x8000:
                left_or_right = 'Right'
            else:
                left_or_right = 'Left'
            percentage = (value & 0x3fff) / 100
            return f'{left_or_right} {percentage} %'


class PercentField(Field):

    _units = ['%', '%']

    def __init__(self, name, scale=1.0, **kwargs):
        super().__init__(name=name, conversion_factor=[100.0 * scale, 100.0 * scale], **kwargs)


class BytePercentField(NamedField):

    _units = ['%', '%']
    _conversion_factor = [2.0, 2.0]


class FitBaseTypeField(NamedField):

    def _convert_single(self, value, invalid):
        if value != invalid:
            try:
                return FieldDefinition._type_name(value)
            except Exception:
                return value


class MessageIndexField(NamedField):

    def _convert_single(self, value, invalid):
        converted_value = {}
        converted_value['selected'] = ((value & 0x8000) == 0x8000)
        converted_value['value'] = (value & 0x0FFF)
        return converted_value


class CaloriesField(NamedField):

    _name = 'calories'
    _units = ['kcal', 'kcal']


class ActiveCaloriesField(CaloriesField):

    _name = 'active_calories'


class CaloriesDayField(NamedField):

    _units = ['kcal/day', 'kcal/day']


class CyclesCaloriesField(Field):

    _name = 'cycles_to_calories'
    _units = ['kcal/cycle', 'kcal/cycle']
    _conversion_factor = [5019.6, 5019.6]


class CyclesDistanceField(Field):

    _name = 'cycles_to_distance'
    _units = ['m/cycle', 'm/cycle']
    _conversion_factor = [5000.0, 5000.0]


#
# Time related fields
#
class TimestampField(NamedField):

    def __init__(self, name, utc=True, **kwargs):
        self.utc = utc
        super().__init__(name, **kwargs)

    def _convert_single(self, value, invalid):
        if self.utc:
            timestamp = time.time()
            time_now = datetime.datetime.fromtimestamp(timestamp)
            time_utc = datetime.datetime.utcfromtimestamp(timestamp)
            utc_offset_secs = (time_now - time_utc).total_seconds()
            # hack - summary of the day messages appear at midnight and we want them to appear in the current day,
            # reimplement properly
            value += (utc_offset_secs - 1)
        return datetime.datetime(1989, 12, 31, 0, 0, 0) + datetime.timedelta(0, value)


class TimeMsField(NamedField):

    _name = 'time'

    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    def _convert_single(self, value, invalid):
        if value != invalid:
            return conversions.ms_to_dt_time(value / self._scale)


class TimeSField(NamedField):

    _name = 'time'
    _units = ['s', 's']

    # invalid is not allowed, 65535 is a valid value
    def _convert_single(self, value, invalid):
        return value


class TimeHourField(TimeMsField):

    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    def _convert_single(self, value, invalid):
        if value != invalid:
            return conversions.hours_to_dt_time(value / self._scale)


class TimeMinField(TimeMsField):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    def _convert_single(self, value, invalid):
        if value != invalid:
            return conversions.min_to_dt_time(value / self._scale)


class TimeOfDayField(NamedField):

    _name = 'time'

    def _convert_single(self, value, invalid):
        if value != invalid:
            return conversions.secs_to_dt_time(value)


class CyclesField(Field):

    _name = 'cycles'
    _units = ['cycles', 'cycles']

    def __init__(self, scale=2.0, *args, **kwargs):
        super().__init__(conversion_factor=[scale, scale], *args, **kwargs)


class FractionalCyclesField(Field):

    _name = 'total_fractional_cycles'
    _units = ['cycles', 'cycles']
    _conversion_factor = [128.0, 128.0]


class StepsField(Field):

    _name = 'steps'
    _units = ['steps', 'steps']

    def __init__(self, scale=1.0, **kwargs):
        self._conversion_factor = [scale, scale]
        super().__init__(**kwargs)


class StrokesField(Field):

    _name = 'strokes'
    _units = ['strokes', 'strokes']

    def __init__(self, scale=2.0, **kwargs):
        super().__init__(conversion_factor=[scale, scale], **kwargs)


class VersionField(NamedField):
    """A field that contains a software or hardware version."""

    _name = 'version'
    _scale = 100.0

    def _convert_single(self, value, invalid):
        if value != invalid:
            return '{0:2.2f}'.format(value / self._scale)


class EventDataField(Field):

    _name = 'event_data'
    _dependant_field = {
        'timer' : Field(name='timer_trigger'),
        245     : CyclesField
    }
    _dependant_field_control_fields = ['event']

    def dependant_field(self, control_value_list):
        event = control_value_list[0]
        return EventDataField._dependant_field[event]


class PosField(NamedField):

    _units = ['degrees', 'degrees']
    _conversion_factor = [11930326.891, 11930326.891]


class CadenceField(NamedField):

    _name = 'cadence'
    _units = ['rpm', 'rpm']


class FractionalCadenceField(NamedField):

    _name = 'fractional_cadence'
    _units = ['rpm', 'rpm']
    _conversion_factor = [128.0, 128.0]


class PowerField(NamedField):

    _name = 'power'
    _units = ['watts', 'watts']


class WorkField(Field):

    _name = 'total_work'
    _units = ['J', 'J']


class TrainingEffectField(NamedField):

    _conversion_factor = [10.0, 10.0]
