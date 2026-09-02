"""Structured data for decoding a FIT file monitoring message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import NamedField, CaloriesField, TimeMsField, TimeSField, TimeMinField, DistanceCentimetersToMetersField, DistanceMillimetersToMetersField, TemperatureField, \
    IntegerField, HeartRateField, ActivityBasedCyclesField, ActivityTypeField, ActivityTypeIntensityField


monitoring_message = {
    0 : IntegerField('device_index'),
    1 : CaloriesField(),
    2 : DistanceCentimetersToMetersField('distance'),
    3 : ActivityBasedCyclesField(),
    4 : TimeMsField('cum_active_time'),
    5 : ActivityTypeField(),
    6 : NamedField('activity_subtype'),
    7 : NamedField('activity_level'),
    14 : TemperatureField('temperature_min'),
    15 : TemperatureField('temperature_max'),
    19 : CaloriesField('active_calories'),
    24 : ActivityTypeIntensityField('current_activity_type_intensity'),
    26 : TimeSField('timestamp_16'),
    27 : HeartRateField('heart_rate'),
    29 : TimeMinField('duration'),
    31 : DistanceMillimetersToMetersField('ascent'),
    32 : DistanceMillimetersToMetersField('descent'),
    33 : TimeMinField('moderate_activity_time'),
    34 : TimeMinField('vigorous_activity_time'),
    35 : DistanceMillimetersToMetersField('cum_ascent'),
    36 : DistanceMillimetersToMetersField('cum_descent')
}
