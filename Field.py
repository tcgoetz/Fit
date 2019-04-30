#!/usr/bin/env python

#
# copyright Tom Goetz
#

import time, datetime

from FieldEnums import *
from FieldValue import FieldValue
from FieldDefinition import FieldDefinition
from Conversions import *


class Field(object):
    attr_units_type_metric = 0
    attr_units_type_english = 1
    attr_units_type_default = attr_units_type_metric

    known_field = True
    _units = [ None, None ]
    _conversion_factor = [ 1, 1 ]
    _conversion_constant = [ 0, 0 ]

    def __init__(self, name=''):
        self.name = name
        if self.__class__.__name__ == 'Field':
            self.type = 'number'
        else:
            self.type = (self.__class__.__name__)[:-len('Field')]
        if not name:
            self.name = self.type
        self._subfield = {}
        self.units_type = self.attr_units_type_default

    def name(self):
        return self._name

    def units(self, value):
        if self._units[self.units_type]:
            return self.convert_many_units(value, None)

    def sub_field(self, name):
        return _sub_field[name]

    def convert_single(self, value, invalid):
        if value != invalid:
            return (value / self._conversion_factor[self.units_type]) + self._conversion_constant[self.units_type]

    def _convert_many(self, _convert_single, value, invalid):
        if isinstance(value, list):
            converted_value = []
            for index, sub_value in enumerate(value):
                converted_value.append(_convert_single(value[index], invalid))
        else:
            converted_value = _convert_single(value, invalid)
        return converted_value

    def convert_many(self, value, invalid):
        return self._convert_many(self.convert_single, value, invalid)

    def convert_single_units(self, value, invalid):
        return self._units[self.units_type]

    def convert_many_units(self, value, invalid):
        return self._convert_many(self.convert_single_units, value, invalid)

    def convert(self, value, invalid, english_units=False):
        if english_units:
            self.units_type = Field.attr_units_type_english
        else:
            self.units_type = Field.attr_units_type_metric
        return FieldValue(self, invalid=invalid, value=self.convert_many(value, invalid), orig=value)

    def __repr__(self):
        return self.__class__.__name__ + '(' + self.name + ')'


#
# Special fields
#
class UnknownField(Field):
    known_field = False
    def __init__(self, index):
        super(UnknownField, self).__init__("unknown_" + str(index))


class DevField(Field):
    def __init__(self, name, units, scale, offset, *args, **kwargs):
        self._units = [units, units]
        if scale is not None:
            self._conversion_factor = [scale, scale]
        if offset is not None:
            self._conversion_constant = [offset, offset]
        super(DevField, self).__init__(name=name, *args, **kwargs)


class ObjectField(Field):
    def __init__(self, name, obj_func, output_func):
        super(ObjectField, self).__init__(name)
        self.obj_func = obj_func
        self.output_func = output_func

    def convert_single(self, value, invalid):
        if value != invalid:
            return self.output_func(value, self.units_type == Field.attr_units_type_metric)

    def convert(self, value, invalid, english_units=False):
        if english_units:
            self.units_type = Field.attr_units_type_english
        else:
            self.units_type = Field.attr_units_type_metric
        value_obj = self.obj_func(value)
        return FieldValue(self, invalid=invalid, value=self.convert_many(value_obj, invalid), orig=value_obj)


#
# Basic field types
#
class BoolField(Field):
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

    def convert_single(self, value, invalid):
        if value != invalid:
            try:
                return bool(value)
            except:
                return value


class EnumField(Field):
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

    def convert_single(self, value, invalid):
        if value != invalid:
            try:
                return self.enum(value)
            except:
                return value


class SwitchField(EnumField):
    enum = Switch


class BitField(Field):
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

    def convert_single(self, value, invalid):
        if value != invalid:
            return self.bits.get(value, [self.bits[bit] for bit in self.bits if ((bit & value) == bit)])


class LeftRightBalanceField(Field):
    def convert_single(self, value, invalid):
        if value != invalid:
            if value & 0x8000:
                left_or_right = 'Right'
            else:
                left_or_right = 'Left'
            percentage = (value & 0x3fff) / 100
            return left_or_right + ' ' + str(percentage) + '%'


class PercentField(Field):
    _units = [ '%', '%' ]

    def __init__(self, name, scale=1.0, *args, **kwargs):
        self. _conversion_factor = [ 100.0 * scale, 100.0 * scale ]
        Field.__init__(self, name, *args, **kwargs)


class BytePercentField(Field):
    _units = [ '%', '%' ]
    _conversion_factor = [ 2.0, 2.0 ]


class StringField(Field):
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

    def convert_many(self, value, invalid):
        if isinstance(value, list):
            converted_value = ""
            for character in value:
                if character != 0:
                    converted_value += chr(character)
                else:
                    break
        else:
            converted_value = str(value)
        return converted_value.strip()


class BytesField(Field):
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

    def convert_many(self, value, invalid):
        if isinstance(value, list):
            converted_value = bytearray()
            for character in value:
                converted_value.append(character)
        else:
            converted_value = bytearray(value)
        return converted_value


class DistanceMetersField(ObjectField):
    def __init__(self, name, obj_func=Distance.from_meters, output_func=Distance.meters_or_feet, scale=1.0):
        super(DistanceMetersField, self).__init__(name, obj_func, output_func)
        self._conversion_factor = scale

    def convert(self, value, invalid, english_units=False):
        if english_units:
            self.units_type = Field.attr_units_type_english
        else:
            self.units_type = Field.attr_units_type_metric
        value_obj = self.obj_func(value / self._conversion_factor)
        return FieldValue(self, invalid=invalid, value=self.convert_many(value_obj, invalid), orig=value_obj)


class EnhancedDistanceMetersField(DistanceMetersField):
    def __init__(self, name):
        super(EnhancedDistanceMetersField, self).__init__(name, Distance.from_mm, Distance.meters_or_feet)


class DistanceCentimetersToKmsField(DistanceMetersField):
    def __init__(self, name='distance'):
        super(DistanceCentimetersToKmsField, self).__init__(name, Distance.from_cm, Distance.kms_or_miles)


class DistanceCentimetersToMetersField(DistanceMetersField):
    def __init__(self, name='distance'):
        super(DistanceCentimetersToMetersField, self).__init__(name, Distance.from_cm, Distance.meters_or_feet)


class DistanceMillimetersField(DistanceMetersField):
    def __init__(self, name='distance'):
        super(DistanceMillimetersField, self).__init__(name, Distance.from_mm, Distance.mm_or_inches, 10.0)


#
#
#
class FitBaseUnitField(EnumField):
    enum = FitBaseUnit


class DisplayMeasureField(EnumField):
    enum = DisplayMeasure


class DisplayHeartField(EnumField):
    enum = DisplayHeart


class DisplayPositionField(EnumField):
    enum = DisplayPosition


class FitBaseTypeField(Field):
    def convert_single(self, value, invalid):
        if value != invalid:
            try:
                return FieldDefinition._type_name(value)
            except:
                return value


class MessageNumberField(Field):
    def convert_single(self, value, invalid):
        if value != invalid:
            return value



#
# Hardware related fields
#
class ManufacturerField(EnumField):
    enum = Manufacturer

    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='manufacturer', *args, **kwargs)


class GarminProductField(EnumField):
    enum = GarminProduct


class WahooFitnessProductField(EnumField):
    enum = WahooFitnessProduct


class UnknownProductField(EnumField):
    enum = UnknownProduct


class ProductField(Field):
    dependant_field_control_fields = ['manufacturer']

    _manufacturer_to_product_fields = {
        Manufacturer.Garmin                 : GarminProductField,
        Manufacturer.Garmin_local_0         : GarminProductField,
        Manufacturer.Garmin_local_31533     : GarminProductField,
        Manufacturer.Garmin_local_42664     : GarminProductField,
        Manufacturer.Garmin_local_42768     : GarminProductField,
        Manufacturer.Garmin_local_43064     : GarminProductField,
        Manufacturer.Garmin_local_43168     : GarminProductField,
        Manufacturer.Garmin_local_43304     : GarminProductField,
        Manufacturer.Garmin_local_45192     : GarminProductField,
        Manufacturer.Garmin_local_45528     : GarminProductField,
        Manufacturer.Garmin_local_45712     : GarminProductField,
        Manufacturer.Garmin_local_47656     : GarminProductField,
        Manufacturer.Garmin_local_45784     : GarminProductField,
        Manufacturer.Garmin_local_52416     : GarminProductField,
        Manufacturer.Garmin_local_61440     : GarminProductField,
        Manufacturer.Garmin_local_65533     : GarminProductField,
        Manufacturer.Wahoo_Fitness          : WahooFitnessProductField,
    }

    def dependant_field(self, control_value_list):
        manufacturer = control_value_list[0]
        try:
            dependant_field_name = self._manufacturer_to_product_fields[manufacturer]
        except:
            dependant_field_name = UnknownProductField
        return dependant_field_name(name='product')


class DisplayOrientationField(EnumField):
    enum = DisplayOrientation


class SideField(EnumField):
    enum = Side
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='side', *args, **kwargs)


class BacklightModeField(EnumField):
    enum = BacklightMode
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='backlight_mode', *args, **kwargs)


class AntNetworkField(EnumField):
    enum = AntNetwork
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='ant_network', *args, **kwargs)


class SourceTypeField(EnumField):
    enum = SourceType
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='source_type', *args, **kwargs)


class AntplusDeviceTypeField(EnumField):
    enum = AntplusDeviceType


class LocalDeviceTypeField(EnumField):
    enum = LocalDeviceType


class UnknownDeviceTypeField(EnumField):
    enum = UnknownDeviceType


class DeviceType(Field):
    dependant_field_control_fields = ['source_type']

    _source_to_device_type_fields = {
        SourceType.ant          : Field('ant_device_type'),
        SourceType.antplus      : AntplusDeviceTypeField,
        SourceType.local        : LocalDeviceTypeField,
    }

    def __init__(self, *args, **kwargs):
        Field.__init__(self, name='device_type', *args, **kwargs)

    def dependant_field(self, control_value_list):
        source_type = control_value_list[0]
        if source_type is not None:
            try:
                dependant_field_name = self._source_to_device_type_fields[source_type]
            except:
                dependant_field_name = UnknownDeviceTypeField
        else:
            dependant_field_name = Field
        return dependant_field_name(name='device_type')


class BatteryVoltageField(Field):
    _units = [ 'v', 'v' ]
    _conversion_factor = [ 256.0, 256.0 ]


class BatteryStatusField(EnumField):
    enum = BatteryStatus
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='battery_status', *args, **kwargs)


class AutoSyncFrequencyField(EnumField):
    enum = AutoSyncFrequency
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='auto_sync_frequency', *args, **kwargs)


class BodyLocationField(EnumField):
    enum = BodyLocation


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
        BitField.__init__(self, name='auto_activity_detect', *args, **kwargs)


class MessageIndexField(Field):
    def convert_single(self, value, invalid):
        converted_value = {}
        converted_value['selected'] = ((value & 0x8000) == 0x8000)
        converted_value['value'] = (value & 0x0FFF)
        return converted_value

#
# User related fields
#
class GenderField(EnumField):
    enum = Gender


class HeightField(ObjectField):
    def __init__(self, name='height'):
        super(HeightField, self).__init__(name, Distance.from_cm, Distance.meters_or_feet)


class WeightField(ObjectField):
    def __init__(self, name='weight'):
        super(WeightField, self).__init__(name, Weight.from_cgs, Weight.kgs_or_lbs)


class CaloriesField(Field):
    _units = [ 'kcal', 'kcal' ]


class ActiveCaloriesField(CaloriesField):
    def __init__(self, *args, **kwargs):
        CaloriesField.__init__(self, name='active_calories', *args, **kwargs)


class CaloriesDayField(Field):
    _units = [ 'kcal/day', 'kcal/day' ]
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)


class CyclesCaloriesField(Field):
    _units = [ 'kcal/cycle', 'kcal/cycle' ]
    _conversion_factor = [ 5019.6, 5019.6 ]
    def __init__(self):
        Field.__init__(self, 'cycles_to_calories')


class CyclesDistanceField(Field):
    _units = [ 'm/cycle', 'm/cycle' ]
    _conversion_factor = [ 5000.0, 5000.0 ]
    def __init__(self):
        Field.__init__(self, 'cycles_to_distance')


class HeartRateField(Field):
    _units = [ 'bpm', 'bpm' ]
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

class HeartRateZoneCalcField(EnumField):
    enum = HeartRateZoneCalc
    def __init__(self):
        EnumField.__init__(self, 'hr_calc_type')


class PowerCalcField(EnumField):
    enum = PowerCalc
    def __init__(self):
        EnumField.__init__(self, 'pwr_calc_type')


class LanguageField(EnumField):
    enum = Language


#
# Time related fields
#
class DateModeField(EnumField):
    enum = DateMode
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='date_mode', *args, **kwargs)


class TimeModeField(EnumField):
    enum = TimeMode
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='time_mode', *args, **kwargs)


class TimestampField(Field):
    def __init__(self, name='timestamp', utc=True):
        self.utc = utc
        Field.__init__(self, name)

    def convert_single(self, value, invalid):
        if self.utc:
            timestamp = time.time()
            time_now = datetime.datetime.fromtimestamp(timestamp)
            time_utc = datetime.datetime.utcfromtimestamp(timestamp)
            utc_offset_secs = (time_now - time_utc).total_seconds()
            # hack - summary of the day messages appear at midnight and we want them to appear in the current day,
            # reimplement properly
            value += (utc_offset_secs - 1)
        return datetime.datetime(1989, 12, 31, 0, 0, 0) +  datetime.timedelta(0, value)


class TimeMsField(Field):
    def __init__(self, name='time_ms', scale=1.0):
        self._conversion_factor = scale
        Field.__init__(self, name)

    def convert_single(self, value, invalid):
        if value != invalid:
            return ms_to_dt_time(value / self._conversion_factor)


class TimeSField(Field):
    _units = [ 's', 's' ]

    # invalid is not allowed, 65535 is a valid value
    def convert_single(self, value, invalid):
        return value


class TimeMinField(TimeMsField):
    def __init__(self, name='time_min', scale=1.0):
        self._conversion_factor = scale
        Field.__init__(self, name)

    def convert_single(self, value, invalid):
        if value != invalid:
            return min_to_dt_time(value / self._conversion_factor)


class TimeOfDayField(Field):
    def convert_single(self, value, invalid):
        if value != invalid:
            return secs_to_dt_time(value)


class SpeedMpsField(ObjectField):
    def __init__(self, name):
        super(SpeedMpsField, self).__init__(name, Speed.from_mmps, Speed.kph_or_mph)


class CyclesField(Field):
    _units = ['cycles', 'cycles' ]
    def __init__(self, name, scale=2.0, *args, **kwargs):
        self. _conversion_factor = [ scale, scale ]
        Field.__init__(self, name)


class FractionalCyclesField(Field):
    _units = ['cycles', 'cycles' ]
    _conversion_factor = [ 128.0, 128.0 ]


class StepsField(Field):
    _units = ['steps', 'steps' ]
    def __init__(self, name, scale=1.0, *args, **kwargs):
        self. _conversion_factor = [ scale, scale ]
        Field.__init__(self, name)


class StrokesField(Field):
    _units = ['strokes', 'strokes' ]
    def __init__(self, name, scale=2.0, *args, **kwargs):
        self. _conversion_factor = [ scale, scale ]
        Field.__init__(self, name)


def cycles_units_to_field(name):
    field_mapping = {
        'cycles' : CyclesField,
        'steps' : StepsField,
        'strokes' : StrokesField,
    }
    try:
        return field_mapping[name]
    except:
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
    except:
        return _units['generic']


class ActivityBasedCyclesField(Field):
    _units = ['cycles', 'cycles' ]
    _conversion_factor = [ 2.0, 2.0 ]
    dependant_field_control_fields = ['activity_type']

    def __init__(self, name='cycles', *args, **kwargs):
        Field.__init__(self, name, *args, **kwargs)

    def dependant_field(self, control_value_list):
        activity_type = control_value_list[0]
        dependant_field_name_base = cycles_activity_to_units(activity_type)
        dependant_field_name = self.name.replace('cycles', dependant_field_name_base)
        return cycles_units_to_field(dependant_field_name_base)(name=dependant_field_name)


class ActivityField(EnumField):
    enum = Activity


class ActivityTypeField(Field):
    def __init__(self):
        Field.__init__(self, 'activity_type')

    def convert_single(self, value, invalid):
        return ActivityType(value)

    def convert_single_units(self, value, invalid):
        return cycles_activity_to_units(ActivityType(value).name)


class ActivityClassField(Field):
    def convert_single(self, value, invalid):
        if value & 0x80:
            activity_class = "athlete "
        else:
            activity_class = ""
        activity_class += str(value & 0x7f)
        return activity_class


class IntensityField(Field):
    _max_intensity = 8
    def __init__(self, *args, **kwargs):
        super(IntensityField, self).__init__("intensity", *args, **kwargs)


class ActivityTypeIntensityField(Field):
    def __init__(self, *args, **kwargs):
        super(ActivityTypeIntensityField, self).__init__(*args, **kwargs)
        self._subfield['activity_type'] = ActivityTypeField()
        self._subfield['intensity'] = IntensityField()

    def convert(self, value, invalid, english_units=False):
        activity_type = value & 0x1f
        intensity = value >> 5
        return FieldValue(self, ['activity_type', 'intensity'],
                          invalid=invalid, value=self.convert_many(value, invalid), orig=value,
                          activity_type=self._subfield['activity_type'].convert(activity_type, 0xff, english_units),
                          intensity=self._subfield['intensity'].convert(intensity, 0xff, english_units))


class FileField(EnumField):
    enum = FileType


class VersionField(Field):
    _conversion_factor = [ 100.0, 100.0 ]
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

    def convert_single(self, value, invalid):
        if value != invalid:
            return '{0:2.2f}'.format(value / self._conversion_factor[self.units_type])


class EventField(EnumField):
    enum = Event


class EventTypeField(EnumField):
    enum = EventType


class EventDataField(Field):
    _dependant_field = {
        'timer' : Field('timer_trigger'),
        245 : CyclesField
    }
    dependant_field_control_fields = ['event']

    def __init__(self, *args, **kwargs):
        super(EventDataField, self).__init__(name='event_data', *args, **kwargs)

    def dependant_field(self, control_value_list):
        event = control_value_list[0]
        return EventDataField._dependant_field[event]


class LapTriggerField(EnumField):
    enum = LapTrigger


class SessionTriggerField(EnumField):
    enum = SessionTrigger


class SportBasedCyclesField(Field):
    _units = ['cycles', 'cycles' ]
    _conversion_factor = [ 1.0, 1.0 ]
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
    enum = Sport
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
        super(SportField, self).__init__(name='sport', *args, **kwargs)

    @classmethod
    def units(cls, sport_index):
        try:
            return cls._units[sport_index]
        except:
            return cls._units[0]


class SubSportField(EnumField):
    enum = SubSport
    def __init__(self, *args, **kwargs):
        super(SubSportField, self).__init__(name='sub_sport', *args, **kwargs)


class PosField(Field):
    _units = [ 'degrees', 'degrees' ]
    _conversion_factor = [ 11930326.891, 11930326.891 ]


class LongitudeField(ObjectField):
    def __init__(self, name):
        super(LongitudeField, self).__init__(name, Longitude.from_semicircles, Longitude.to_degrees)


class LatiitudeField(ObjectField):
    def __init__(self, name):
        super(LatiitudeField, self).__init__(name, Latitude.from_semicircles, Latitude.to_degrees)


class CadenceField(Field):
    _units = [ 'rpm', 'rpm' ]


class FractionalCadenceField(Field):
    _units = [ 'rpm', 'rpm' ]
    _conversion_factor = [ 128.0, 128.0 ]


class PowerField(Field):
    _units = [ 'watts', 'watts' ]


class WorkField(Field):
    _units = [ 'J', 'J' ]


class AltitudeField(DistanceMetersField):
    def __init__(self, name='altitude'):
        super(AltitudeField, self).__init__(name, Distance.from_cm, Distance.meters_or_feet, 5.0)


class EnhancedAltitudeField(DistanceMetersField):
    def __init__(self, name='altitude'):
        super(EnhancedAltitudeField, self).__init__(name, Distance.from_meters, Distance.meters_or_feet, 6993.0)


class TemperatureField(ObjectField):
    def __init__(self, name):
        super(TemperatureField, self).__init__(name, Temperature.from_celsius, Temperature.c_or_f)


class TrainingeffectField(Field):
    _conversion_factor = [ 10.0, 10.0 ]
