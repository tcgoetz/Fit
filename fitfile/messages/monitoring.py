"""Structured data for decoding a FIT file monitoring message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import NamedField, CaloriesField, TimeMsField, TimeSField, TimeMinField, DistanceCentimetersToMetersField, DistanceMillimetersToMetersField, TemperatureField, \
    IntegerField, HeartRateField, ActivityBasedCyclesField, ActivityTypeField, ActivityTypeIntensityField, DistanceMetersField, TimestampField


monitoring_message = {
    0 : IntegerField('device_index'),
    1 : CaloriesField(),
    2 : DistanceCentimetersToMetersField('distance'),
    3 : ActivityBasedCyclesField(),
    4 : TimeMsField('cum_active_time'),
    5 : ActivityTypeField(),
    6 : NamedField('activity_subtype'),
    7 : NamedField('activity_level'),
    8 : DistanceMetersField('distance_16'),
    9 : IntegerField('cycles_16'),
    10 : TimeSField('active_time_16'),
    11 : TimestampField('local_timestamp', utc=False),
    12 : TemperatureField('temperature'),
    #
    14 : TemperatureField('temperature_min'),
    15 : TemperatureField('temperature_max'),
    16 : IntegerField('activity_time'),
    #
    19 : CaloriesField('active_calories'),
    #
    24 : ActivityTypeIntensityField('current_activity_type_intensity'),
    25 : IntegerField('timestamp_min_8'),
    26 : IntegerField('timestamp_16'),
    27 : HeartRateField('heart_rate'),
    28 : IntegerField('intensity'),
    29 : TimeMinField('duration_min'),
    30 : TimeSField('duration'),
    31 : DistanceMillimetersToMetersField('ascent'),
    32 : DistanceMillimetersToMetersField('descent'),
    33 : TimeMinField('moderate_activity_time'),
    34 : TimeMinField('vigorous_activity_time'),
    35 : DistanceMillimetersToMetersField('cum_ascent'),
    36 : DistanceMillimetersToMetersField('cum_descent'),
    41 : IntegerField('pushes'),
}
