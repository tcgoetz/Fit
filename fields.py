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
    _conversion_factor = [1, 1]
    _conversion_constant = [0, 0]

    def __init__(self, name=''):
        """Return a new instance of the Field class."""
        self.name = name
        if self.__class__.__name__ == 'Field':
            self.type = 'number'
        else:
            self.type = (self.__class__.__name__)[:-len('Field')]
        if not name:
            self.name = self.type
        self._subfield = {}
        self.measurement_system = fe.DisplayMeasure.metric

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


#
# Special fields
#
class UnknownField(Field):
    """Class that handles fields that are not documented."""

    def __init__(self, index):
        """Return a new instance of the UnknownField class."""
        super().__init__(f"unknown_{index}")


#
# Basic field types
#
class LeftRightBalanceField(Field):
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

    def __init__(self, name, scale=1.0, *args, **kwargs):
        self._conversion_factor = [100.0 * scale, 100.0 * scale]
        super().__init__(name, *args, **kwargs)


class BytePercentField(Field):
    _units = ['%', '%']
    _conversion_factor = [2.0, 2.0]


class FitBaseTypeField(Field):
    def _convert_single(self, value, invalid):
        if value != invalid:
            try:
                return FieldDefinition._type_name(value)
            except Exception:
                return value


class MessageNumberField(Field):
    def _convert_single(self, value, invalid):
        if value != invalid:
            return value


class MessageIndexField(Field):
    def _convert_single(self, value, invalid):
        converted_value = {}
        converted_value['selected'] = ((value & 0x8000) == 0x8000)
        converted_value['value'] = (value & 0x0FFF)
        return converted_value


class CaloriesField(Field):
    _units = ['kcal', 'kcal']


class ActiveCaloriesField(CaloriesField):
    def __init__(self, *args, **kwargs):
        super().__init__(name='active_calories', *args, **kwargs)


class CaloriesDayField(Field):
    _units = ['kcal/day', 'kcal/day']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CyclesCaloriesField(Field):
    _units = ['kcal/cycle', 'kcal/cycle']
    _conversion_factor = [5019.6, 5019.6]

    def __init__(self):
        super().__init__('cycles_to_calories')


class CyclesDistanceField(Field):
    _units = ['m/cycle', 'm/cycle']
    _conversion_factor = [5000.0, 5000.0]

    def __init__(self):
        super().__init__('cycles_to_distance')


class HeartRateField(Field):
    _units = ['bpm', 'bpm']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#
# Time related fields
#
class TimestampField(Field):
    def __init__(self, name='timestamp', utc=True):
        self.utc = utc
        super().__init__(name)

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


class TimeMsField(Field):
    def __init__(self, name='time', scale=1.0):
        self._conversion_factor = scale
        super().__init__(name)

    def _convert_single(self, value, invalid):
        if value != invalid:
            return conversions.ms_to_dt_time(value / self._conversion_factor)


class TimeSField(Field):
    _units = ['s', 's']

    # invalid is not allowed, 65535 is a valid value
    def _convert_single(self, value, invalid):
        return value


class TimeHourField(TimeMsField):
    def __init__(self, name='time', scale=1.0):
        super().__init__(name, scale)

    def _convert_single(self, value, invalid):
        if value != invalid:
            return conversions.hours_to_dt_time(value / self._conversion_factor)


class TimeMinField(TimeMsField):
    def __init__(self, name='time', scale=1.0):
        super().__init__(name, scale)

    def _convert_single(self, value, invalid):
        if value != invalid:
            return conversions.min_to_dt_time(value / self._conversion_factor)


class TimeOfDayField(Field):
    def _convert_single(self, value, invalid):
        if value != invalid:
            return conversions.secs_to_dt_time(value)


class CyclesField(Field):
    _units = ['cycles', 'cycles']

    def __init__(self, name, scale=2.0, *args, **kwargs):
        self. _conversion_factor = [scale, scale]
        super().__init__(name)


class FractionalCyclesField(Field):
    _units = ['cycles', 'cycles']
    _conversion_factor = [128.0, 128.0]


class StepsField(Field):
    _units = ['steps', 'steps']

    def __init__(self, name, scale=1.0, *args, **kwargs):
        self. _conversion_factor = [scale, scale]
        super().__init__(name)


class StrokesField(Field):
    _units = ['strokes', 'strokes']

    def __init__(self, name, scale=2.0, *args, **kwargs):
        self. _conversion_factor = [scale, scale]
        super().__init__(name)


class VersionField(Field):
    """A field that contains a software or hardware version."""

    _conversion_factor = 100.0

    def __init__(self, *args, **kwargs):
        """Return an instance of VersionField."""
        super().__init__(*args, **kwargs)

    def _convert_single(self, value, invalid):
        if value != invalid:
            return '{0:2.2f}'.format(value / self._conversion_factor)


class EventDataField(Field):
    _dependant_field = {
        'timer' : Field('timer_trigger'),
        245 : CyclesField
    }
    dependant_field_control_fields = ['event']

    def __init__(self, *args, **kwargs):
        super().__init__(name='event_data', *args, **kwargs)

    def dependant_field(self, control_value_list):
        event = control_value_list[0]
        return EventDataField._dependant_field[event]


class PosField(Field):
    _units = ['degrees', 'degrees']
    _conversion_factor = [11930326.891, 11930326.891]


class CadenceField(Field):
    _units = ['rpm', 'rpm']


class FractionalCadenceField(Field):
    _units = ['rpm', 'rpm']
    _conversion_factor = [128.0, 128.0]


class PowerField(Field):
    _units = ['watts', 'watts']

    def __init__(self, name='power'):
        super().__init__(name)


class WorkField(Field):
    _units = ['J', 'J']


class TrainingeffectField(Field):
    _conversion_factor = [10.0, 10.0]
