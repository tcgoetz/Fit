"""Structured data for decoding a FIT file user profile message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import TimestampField, NamedField, PowerField, TimeOfDayField, GenderField, LanguageField, HeightField, WeightField, EnhancedDistanceMetersField, \
    DisplayMeasureField, DisplayHeartField, DisplayPositionField, IntegerField, HeartRateField, YearOffset, ActivityClassField, SpeedKphField, TimeMinField, \
    StringField


user_profile_message = {
    1 : GenderField(),
    2 : IntegerField('age'),
    3 : HeightField(),
    4 : WeightField(),
    5 : LanguageField(),
    6 : DisplayMeasureField('elev_setting'),
    7 : DisplayMeasureField('weight_setting'),
    8 : HeartRateField('resting_heart_rate'),
    9 : HeartRateField('default_max_running_heart_rate'),
    10 : HeartRateField('default_max_biking_heart_rate'),
    11 : HeartRateField('default_max_heart_rate'),
    12 : DisplayHeartField('hr_setting'),
    13 : DisplayMeasureField('speed_setting'),
    14 : DisplayMeasureField('dist_setting'),
    16 : PowerField('power_setting'),
    17 : ActivityClassField(),
    18 : DisplayPositionField(),
    #
    21 : DisplayMeasureField('temperature_setting'),
    22 : NamedField('local_id'),
    23 : NamedField('global_id'),
    24 : YearOffset('year_of_birth'),
    #
    26 : IntegerField('pressure_setting'),
    #
    28 : TimeOfDayField('wake_time'),
    29 : TimeOfDayField('sleep_time'),
    30 : DisplayMeasureField('height_setting'),
    31 : EnhancedDistanceMetersField('user_running_step_length'),
    32 : EnhancedDistanceMetersField('user_walking_step_length'),
    #
    34 : TimeMinField('recovery_time'),
    35 : TimestampField('recovery_time_start', utc=True),
    #
    37 : SpeedKphField('lactate_threshold_speed'),
    #
    41 : TimestampField('time_last_running_lthr_update', utc=True),
    42 : TimestampField('time_last_cycling_lthr_update', utc=True),
    #
    44 : IntegerField('birth_day'),
    45 : IntegerField('birth_month'),
    #
    47 : DisplayMeasureField('depth_setting'),
    #
    49 : IntegerField('dive_count'),
    #
    53 : TimeMinField('moderate_activity'),
    54 : TimeMinField('vigorous_activity'),
    #
    58 : IntegerField('golf_distance'),
    #
    62 : GenderField('gender_x'),
    #
    65 : IntegerField('running_coach'),
    66 : IntegerField('cycling_coach'),
    67 : StringField('user_name')
}
