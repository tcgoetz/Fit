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
class TypeField(Field):
    """A base class for fields based on python types."""

    def __init__(self, type_func, *args, **kwargs):
        """Return a field instance that holds an integer."""
        super().__init__(*args, **kwargs)
        self.type_func = type_func

    def _convert_single(self, value, invalid):
        if value != invalid:
            try:
                return self.type_func(value)
            except Exception:
                return value


class IntegerField(TypeField):
    """A FIT file message field with a boolean value."""

    def __init__(self, *args, **kwargs):
        """Return a field instance that holds an integer."""
        super().__init__(int, *args, **kwargs)


class FloatField(TypeField):
    def __init__(self, name, scale=1.0, *args, **kwargs):
        self._conversion_factor = [scale, scale]
        super().__init__(float, name, *args, **kwargs)


class BoolField(TypeField):
    """A FIT file message field with a boolean value."""

    def __init__(self, *args, **kwargs):
        super().__init__(bool, *args, **kwargs)


class EnumField(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _convert_single(self, value, invalid):
        return self.enum.from_string(value)


class SwitchField(EnumField):
    enum = fe.Switch


class BitField(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _convert_single(self, value, invalid):
        if value != invalid:
            return self.bits.get(value, [self.bits[bit] for bit in self.bits if ((bit & value) == bit)])


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


class StringField(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _invalid_single(self, value, invalid):
        return (value < 0) or (value > 127)

    def _convert_many(self, value, invalid):
        if isinstance(value, list):
            converted_value = ""
            for aschii_index in value:
                if aschii_index == 0:
                    break
                converted_value += chr(aschii_index)
        else:
            converted_value = str(value)
        return converted_value.strip()


class BytesField(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _convert_many(self, value, invalid):
        if isinstance(value, list):
            converted_value = bytearray()
            for character in value:
                converted_value.append(character)
        else:
            converted_value = bytearray(value)
        return converted_value


#
#
#
class FitBaseUnitField(EnumField):
    enum = fe.FitBaseUnit


class DisplayMeasureField(EnumField):
    enum = fe.DisplayMeasure


class DisplayHeartField(EnumField):
    enum = fe.DisplayHeart


class DisplayPositionField(EnumField):
    enum = fe.DisplayPosition


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


#
# Hardware related fields
#
class ManufacturerField(EnumField):
    enum = fe.Manufacturer

    def __init__(self, *args, **kwargs):
        super().__init__(name='manufacturer', *args, **kwargs)

    def _convert_single(self, value, invalid):
        try:
            return self.enum(value)
        except Exception:
            if value >= fe.Manufacturer.Garmin_local_start.value:
                return fe.Manufacturer.Garmin_local
            return value


class ProductField(EnumField):
    def __init__(self, *args, **kwargs):
        super().__init__(name='product', *args, **kwargs)


class GarminProductField(ProductField):
    enum = fe.GarminProduct


class GarminLocalProductField(ProductField):
    enum = fe.GarminLocalProduct


class ScoscheProductField(ProductField):
    enum = fe.ScoscheProduct


class WahooFitnessProductField(ProductField):
    enum = fe.WahooFitnessProduct


class UnknownProductField(ProductField):
    enum = fe.UnknownProduct


class ProductField(Field):
    dependant_field_control_fields = ['manufacturer']

    _manufacturer_to_product_fields = {
        fe.Manufacturer.Garmin                 : GarminProductField,
        fe.Manufacturer.Dynastream             : GarminProductField,
        fe.Manufacturer.Dynastream_OEM         : GarminProductField,
        fe.Manufacturer.Scosche                : ScoscheProductField,
        fe.Manufacturer.Wahoo_Fitness          : WahooFitnessProductField,
        fe.Manufacturer.Garmin_local           : GarminLocalProductField,
        fe.Manufacturer.invalid                : GarminProductField,
    }

    def dependant_field(self, control_value_list):
        manufacturer = control_value_list[0]
        try:
            dependant_field_name = self._manufacturer_to_product_fields[manufacturer]
        except Exception:
            dependant_field_name = UnknownProductField
        return dependant_field_name()


class DisplayOrientationField(EnumField):
    enum = fe.DisplayOrientation


class SideField(EnumField):
    enum = fe.Side

    def __init__(self, *args, **kwargs):
        super().__init__(name='side', *args, **kwargs)


class BacklightModeField(EnumField):
    enum = fe.BacklightMode

    def __init__(self, *args, **kwargs):
        super().__init__(name='backlight_mode', *args, **kwargs)


class AntNetworkField(EnumField):
    enum = fe.AntNetwork

    def __init__(self, *args, **kwargs):
        super().__init__(name='ant_network', *args, **kwargs)


class SourceTypeField(EnumField):
    enum = fe.SourceType

    def __init__(self, *args, **kwargs):
        super().__init__(name='source_type', *args, **kwargs)


class AntplusDeviceTypeField(EnumField):
    enum = fe.AntplusDeviceType


class LocalDeviceTypeField(EnumField):
    enum = fe.LocalDeviceType


class UnknownDeviceTypeField(EnumField):
    enum = fe.UnknownDeviceType


class DeviceType(Field):
    dependant_field_control_fields = ['source_type']

    _source_to_device_type_fields = {
        fe.SourceType.ant          : Field('ant_device_type'),
        fe.SourceType.antplus      : AntplusDeviceTypeField,
        fe.SourceType.local        : LocalDeviceTypeField,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(name='device_type', *args, **kwargs)

    def dependant_field(self, control_value_list):
        source_type = control_value_list[0]
        if source_type is not None:
            try:
                dependant_field_name = self._source_to_device_type_fields[source_type]
            except Exception:
                dependant_field_name = UnknownDeviceTypeField
        else:
            dependant_field_name = Field
        return dependant_field_name(name='device_type')


class BatteryVoltageField(Field):
    _units = ['v', 'v']
    _conversion_factor = [256.0, 256.0]


class BatteryStatusField(EnumField):
    enum = fe.BatteryStatus

    def __init__(self, *args, **kwargs):
        super().__init__(name='battery_status', *args, **kwargs)


class AutoSyncFrequencyField(EnumField):
    enum = fe.AutoSyncFrequency

    def __init__(self, *args, **kwargs):
        super().__init__(name='auto_sync_frequency', *args, **kwargs)


class BodyLocationField(EnumField):
    enum = fe.BodyLocation


class AutoActivityDetectField(BitField):
    bits = {
        0x00000000 : 'none',
        0x00000001 : 'running',
        0x00000002 : 'cycling',
        0x00000004 : 'swimming',
        0x00000008 : 'walking',
        0x00000020 : 'elliptical',
        0x00000400 : 'sedentary',
        0xffffffff : 'invalid'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(name='auto_activity_detect', *args, **kwargs)


class MessageIndexField(Field):
    def _convert_single(self, value, invalid):
        converted_value = {}
        converted_value['selected'] = ((value & 0x8000) == 0x8000)
        converted_value['value'] = (value & 0x0FFF)
        return converted_value

#
# User related fields
#


class GenderField(EnumField):
    enum = fe.Gender


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


class HeartRateZoneCalcField(EnumField):
    enum = fe.HeartRateZoneCalc

    def __init__(self):
        super().__init__('hr_calc_type')


class PowerCalcField(EnumField):
    enum = fe.PowerCalc

    def __init__(self):
        super().__init__('pwr_calc_type')


class LanguageField(EnumField):
    enum = fe.Language


#
# Time related fields
#
class DateModeField(EnumField):
    enum = fe.DateMode

    def __init__(self, *args, **kwargs):
        super().__init__(name='date_mode', *args, **kwargs)


class TimeModeField(EnumField):
    enum = fe.TimeMode

    def __init__(self, *args, **kwargs):
        super().__init__(name='time_mode', *args, **kwargs)


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


def cycles_units_to_field(name):
    field_mapping = {
        'cycles' : CyclesField,
        'steps' : StepsField,
        'strokes' : StrokesField,
    }
    try:
        return field_mapping[name]
    except Exception:
        return CyclesField


def cycles_activity_to_units(activity):
    _units = {
        'generic'                   : 'cycles',
        # steps activities
        'walking'                   : 'steps',
        'running'                   : 'steps',
        'hiking'                    : 'steps',
        'elliptical'                : 'steps',
        # strokes activities
        'cycling'                   : 'strokes',
        'swimming'                  : 'strokes',
        'rowing'                    : 'strokes',
        'paddling'                  : 'strokes',
        'stand_up_paddleboarding'   : 'strokes',
        'kayaking'                  : 'strokes',
    }
    try:
        return _units[activity.name]
    except Exception:
        return _units['generic']


class ActivityBasedCyclesField(Field):
    _units = ['cycles', 'cycles']
    _conversion_factor = [2.0, 2.0]
    dependant_field_control_fields = ['activity_type']

    def __init__(self, name='cycles', *args, **kwargs):
        super().__init__(name, *args, **kwargs)

    def dependant_field(self, control_value_list):
        activity_type = control_value_list[0]
        dependant_field_name_base = cycles_activity_to_units(activity_type)
        dependant_field_name = self.name.replace('cycles', dependant_field_name_base)
        return cycles_units_to_field(dependant_field_name_base)(name=dependant_field_name)


class ActivityField(EnumField):
    enum = fe.Activity


class ActivityTypeField(Field):
    def __init__(self):
        super().__init__('activity_type')

    def _convert_single(self, value, invalid):
        return fe.ActivityType(value)

    def _convert_single_units(self, value, invalid):
        return cycles_activity_to_units(fe.ActivityType(value).name)


class ActivityClassField(Field):
    def _convert_single(self, value, invalid):
        if value & 0x80:
            activity_class = "athlete "
        else:
            activity_class = ""
        activity_class += str(value & 0x7f)
        return activity_class


class IntensityField(Field):
    _max_intensity = 8

    def __init__(self, *args, **kwargs):
        super().__init__("intensity", *args, **kwargs)


class ActivityTypeIntensityField(Field):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._subfield['activity_type'] = ActivityTypeField()
        self._subfield['intensity'] = IntensityField()

    def convert(self, value, invalid, measurement_system):
        activity_type = value & 0x1f
        intensity = value >> 5
        return FieldValue(self, ['activity_type', 'intensity'],
                          invalid=invalid, value=self._convert_many(value, invalid), orig=value,
                          activity_type=self._subfield['activity_type'].convert(activity_type, 0xff, measurement_system),
                          intensity=self._subfield['intensity'].convert(intensity, 0xff, measurement_system))


class FileField(EnumField):
    enum = fe.FileType


class VersionField(Field):
    """A field that contains a software or hardware version."""

    _conversion_factor = 100.0

    def __init__(self, *args, **kwargs):
        """Return an instance of VersionField."""
        super().__init__(*args, **kwargs)

    def _convert_single(self, value, invalid):
        if value != invalid:
            return '{0:2.2f}'.format(value / self._conversion_factor)


class EventField(EnumField):
    enum = fe.Event


class EventTypeField(EnumField):
    enum = fe.EventType


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


class LapTriggerField(EnumField):
    enum = fe.LapTrigger


class SessionTriggerField(EnumField):
    enum = fe.SessionTrigger


class SportBasedCyclesField(Field):
    _units = ['cycles', 'cycles']
    _conversion_factor = [1.0, 1.0]
    dependant_field_control_fields = ['sport', 'sub_sport']
    _scale = {
        'cycles'    : 1.0,
        'steps'     : 0.5,
        'strokes'   : 1.0
    }

    def dependant_field(self, control_value_list):
        sport = control_value_list[0]
        dependant_field_name_base = cycles_activity_to_units(sport)
        if dependant_field_name_base == 'cycles':
            sub_sport = control_value_list[1]
            dependant_field_name_base = cycles_activity_to_units(sub_sport)
        dependant_field_name = self.name.replace('cycles', dependant_field_name_base)
        return cycles_units_to_field(dependant_field_name_base)(dependant_field_name, self._scale[dependant_field_name_base])


class SportField(EnumField):
    enum = fe.Sport
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

    def __init__(self, *args, **kwargs):
        super().__init__(name='sport', *args, **kwargs)

    @classmethod
    def units(cls, sport_index):
        try:
            return cls._units[sport_index]
        except Exception:
            return cls._units[0]


class SubSportField(EnumField):
    enum = fe.SubSport

    def __init__(self, *args, **kwargs):
        super().__init__(name='sub_sport', *args, **kwargs)


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


class WatchFaceModeField(EnumField):
    enum = fe.WatchFaceMode
