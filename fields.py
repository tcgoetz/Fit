"""Objects that represent FIT file message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import datetime

import Fit.conversions as conversions
import Fit.field_enums as fe
from Fit.field_value import FieldValue
from Fit.field_definition import FieldDefinition


class Field(object):
    """The base object for all FIT file message fields."""

    _units = None
    _scale = 1.0
    _offset = 0.0
    _dependant_field_control_fields = None

    def __init__(self, **kwargs):
        """Return a new instance of the Field class."""
        for key, value in kwargs.items():
            vars(self)['_' + key] = value
        if not hasattr(self, '_name'):
            raise ValueError(f'Unamed instance of {self.__class__.__name__}')

    @property
    def name(self):
        """Return the name of the field."""
        return self._name

    @property
    def units(self):
        """Return the units of the field."""
        return self._units

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
            return (value / self._scale) + self._offset

    def __convert_many(self, _convert_single, value, invalid):
        if isinstance(value, list):
            return [_convert_single(sub_value, invalid) for sub_value in value]
        return _convert_single(value, invalid)

    def _convert_many(self, value, invalid):
        return self.__convert_many(self._convert_single, value, invalid)

    def convert(self, value, invalid, measurement_system=fe.DisplayMeasure.metric):
        """Return a FieldValue as intepretted by the field's rules."""
        return [FieldValue(self, value, invalid, **{self._name: self._convert_many(value, invalid)})]

    def reconvert(self, value, invalid, measurement_system=fe.DisplayMeasure.metric):
        """Return the field's value as intepretted by the field's rules."""
        return {self._name: self._convert_many(value, invalid)}

    def __repr__(self):
        """Return a string representation of a Field instance."""
        return f'{self.__class__.__name__} ({self._name})'


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

    _units = '%'

    def __init__(self, name, scale=1.0, **kwargs):
        super().__init__(name=name, scale=100.0 * scale, **kwargs)


class BytePercentField(NamedField):

    _units = '%'
    _scale = 2.0


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
    _units = 'kcal'


class ActiveCaloriesField(CaloriesField):

    _name = 'active_calories'


class CaloriesDayField(NamedField):

    _units = 'kcal/day'


class CyclesCaloriesField(Field):

    _name = 'cycles_to_calories'
    _units = 'kcal/cycle'
    _scale = 5019.6


class CyclesDistanceField(Field):

    _name = 'cycles_to_distance'
    _units = 'm/cycle'
    _scale = 5000.0


#
# Time related fields
#
class TimestampField(NamedField):

    def _convert_single(self, value, invalid):
        if self._utc:
            return datetime.datetime(1989, 12, 31, 0, 0, 0, tzinfo=datetime.timezone.utc) + datetime.timedelta(seconds=value)
        return datetime.datetime(1989, 12, 31, 0, 0, 0) + datetime.timedelta(seconds=value)


class TimeMsField(NamedField):

    def _convert_single(self, value, invalid):
        if value != invalid:
            return conversions.ms_to_dt_time(value / self._scale)


class TimeSField(NamedField):

    _units = 's'

    # invalid is not allowed, 65535 is a valid value
    def _convert_single(self, value, invalid):
        return value


class TimeOffsetField(Field):

    _name = 'time_offset'
    _units = 's'

    def _convert_single(self, value, invalid):
        # if the offset is greater than 24 hours, than it's negative
        if value > 86400:
            return -(0xFFFFFFFF - value + 1)
        return value


class TimeHourField(TimeMsField):

    def _convert_single(self, value, invalid):
        if value != invalid:
            return conversions.hours_to_dt_time(value / self._scale)


class TimeMinField(TimeMsField):

    def _convert_single(self, value, invalid):
        if value != invalid:
            return conversions.min_to_dt_time(value / self._scale)


class TimeOfDayField(NamedField):

    def _convert_single(self, value, invalid):
        if value != invalid:
            return conversions.secs_to_dt_time(value)


class CyclesField(Field):
    """Field that holds cycles measurement for sports activity."""

    _name = 'cycles'
    _units = 'cycles'

    def __init__(self, scale=2.0, *args, **kwargs):
        super().__init__(scale=scale, *args, **kwargs)


class StepsField(Field):
    """Field that holds steps measurement for sports activity."""

    _name = 'steps'
    _units = 'steps'


class StrokesField(Field):
    """Field that holds strokes measurement for sports activity."""

    _name = 'strokes'
    _units = 'strokes'

    def __init__(self, scale=2.0, **kwargs):
        super().__init__(scale=scale, **kwargs)


class FractionalCyclesField(Field):

    _name = 'total_fractional_cycles'
    _units = 'cycles'
    _scale = 128.0


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


class FractionalCadenceField(NamedField):

    _name = 'fractional_cadence'
    _units = 'rpm'
    _scale = 128.0


class PowerField(NamedField):

    _name = 'power'
    _units = 'watts'


class WorkField(Field):

    _name = 'total_work'
    _units = 'J'


class TrainingEffectField(NamedField):

    _scale = 10.0
