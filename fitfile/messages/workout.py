"""Structured data for decoding a FIT file workout message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import TimeSField, IntegerField, StringField, SportField, SubSportField, DistanceCentimetersToMetersField, DisplayMeasureField, WorkoutCapabilitiesField


workout_message = {
    4 : SportField(),
    5 : WorkoutCapabilitiesField(),
    6 : IntegerField('num_valid_steps'),
    8 : StringField('wkt_name'),
    9 : IntegerField('duration_type'),
    10 : IntegerField('duration_value'),
    11 : SubSportField(),
    14 : DistanceCentimetersToMetersField('pool_length'),
    15 : DisplayMeasureField('pool_length_unit'),
    #
    17 : StringField('wkt_description'),
    #
    20 : IntegerField('workout_index'),
    21 : TimeSField('time'),
    22 : IntegerField('distance'),
}


# duration_time	uint32			1000		s
# duration_distance	uint32			100		m
# duration_hr	workout_hr					% or bpm
# duration_calories	uint32					calories
# duration_step	uint32
# duration_power	workout_power					% or watts
# duration_reps	uint32
