"""Structured data for decoding a FIT file split message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import TimeMsField, TimestampField, DistanceMetersField, HeartRateField, FloatField, CaloriesField, SportBasedGradeField, ClimbingRouteComletedField, IntegerField, \
    SpeedMpsField, DistanceCentimetersToMetersField, LatiitudeField, LongitudeField, AltitudeField, TimeSField, SportField, SubSportField, EnhancedCadenceField, \
    TemperatureField, DistanceMillimetersField, PercentField, PowerField, HeartRateVarianceField, SplitTypeField, EventField, EventTypeField, SwimStrokesField, SwimStrokeField, \
    SwimStrokesCadenceField, LengthTypeField, EnhancedRespirationRateField, RespirationRateField


split_message = {
    1  : TimeMsField('total_elapsed_time'),
    2  : TimeMsField('total_timer_time'),
    3  : DistanceCentimetersToMetersField('total_distance'),
    4  : SpeedMpsField('avg_speed'),
    5  : TimestampField('end_time', utc=True),
    #
    7  : DistanceCentimetersToMetersField('start_distance'),
    #
    9  : TimestampField('start_time', utc=True),
    #
    11 : SportField(),
    12 : SubSportField(),
    13 : DistanceMetersField('ascent'),
    14 : DistanceMetersField('descent'),
    15 : HeartRateField('avg_heart_rate'),
    16 : HeartRateField('max_heart_rate'),
    #
    21 : LatiitudeField('start_position_lat'),
    22 : LongitudeField('start_position_long'),
    23 : LatiitudeField('end_position_lat'),
    24 : LongitudeField('end_position_long'),
    25 : SpeedMpsField('max_speed'),
    26 : FloatField('avg_vertical_speed'),
    27 : TimestampField('end_time', utc=True),
    28 : CaloriesField('total_calories'),
    29 : EnhancedCadenceField('avg_cadence'),
    30 : EnhancedCadenceField('max_cadence'),
    #
    32 : TemperatureField('avg_temperature'),
    33 : TemperatureField('max_temperature'),
    34 : TemperatureField('min_temperature'),
    35 : DistanceMillimetersField('avg_vertical_oscillation'),
    36 : PercentField('avg_vertical_ratio', 100.0),
    37 : TimeMsField('avg_stance_time', scale=10.0),
    38 : PercentField('avg_stance_time_balance'),
    39 : DistanceMillimetersField('avg_step_length'),
    40 : PowerField('avg_power'),
    41 : PowerField('max_power'),
    42 : PowerField('normalized_power'),
    #
    67 : IntegerField('lap_index'),
    #
    70 : SportBasedGradeField('grade'),
    71 : ClimbingRouteComletedField('completed'),
    72 : IntegerField('falls'),
    #
    74 : AltitudeField('start_elevation'),
    #
    78 : TimeSField('active_time'),
    79 : CaloriesField('resting_calories'),
    #
    93 : SpeedMpsField('grade_adjusted_speed'),
    94 : HeartRateVarianceField('avg_hrv'),
    95 : HeartRateVarianceField('max_hrv'),
    #
    105 : TimeMsField('pedaling_time'),
    106 : TimeMsField('cruising_time'),
    107 : IntegerField('beginning_potential'),
    108 : IntegerField('ending_potential'),
    109 : IntegerField('min_stamina'),
    110 : TimeMsField('total_moving_time'),
    #
    130 : SpeedMpsField('step_speed_loss_distance'),
    131 : PercentField('step_speed_loss_percent'),
}

split_summary_message = {
    0 : SplitTypeField(),
    #
    3 : IntegerField('num_splits'),
    4 : TimeMsField('total_timer_time'),
    5 : DistanceCentimetersToMetersField('total_distance'),
    6 : SpeedMpsField('avg_speed'),
    7 : SpeedMpsField('max_speed'),
    8 : DistanceMetersField('total_ascent'),
    9 : DistanceMetersField('total_descent'),
    10 : HeartRateField('avg_heart_rate'),
    11 : HeartRateField('max_heart_rate'),
    12 : FloatField('avg_vertical_speed'),
    13 : CaloriesField('total_calories'),
    14 : EnhancedCadenceField('avg_cadence'),
    15 : EnhancedCadenceField('max_cadence'),
    #
    17 : TemperatureField('avg_temperature'),
    #
    19 : TemperatureField('min_temperature'),
    20 : DistanceMillimetersField('avg_vertical_oscillation'),
    21 : PercentField('avg_vertical_ratio', 100.0),
    22 : TimeMsField('avg_stance_time', scale=10.0),
    #
    24 : DistanceMillimetersField('avg_step_length'),
    25 : PowerField('avg_power'),
    26 : PowerField('max_power'),
    27 : PowerField('normalized_power'),
    #
    52 : DistanceMetersField('avg_split_ascent'),
    53 : DistanceMetersField('max_split_ascent'),
    #
    60 : DistanceMillimetersField('max_split_distance'),
    #
    64 : CaloriesField('resting_calories'),
    #
    72 : HeartRateVarianceField('avg_hrv'),
    73 : HeartRateVarianceField('max_hrv'),
    #
    79  : TimestampField('first_start_time', utc=True),
    #
    83 : SpeedMpsField('step_speed_loss_distance'),
    84 : PercentField('step_speed_loss_percent'),
    #
    65 : TimeMsField('active_time'),
    #
    77 : TimeMsField('total_moving_time'),
}

length_message = {
    0 : EventField(),
    1 : EventTypeField(),
    2 : TimestampField('start_time', utc=True),
    3 : TimeMsField('total_elapsed_time'),
    4 : TimeMsField('total_timer_time'),
    5 : SwimStrokesField(),
    6 : SpeedMpsField('avg_speed'),
    7 : SwimStrokeField(),
    #
    9 : SwimStrokesCadenceField('avg_swimming_cadence'),
    10 : IntegerField('event_group'),
    11 : CaloriesField('total_calories'),
    12 : LengthTypeField(),
    #
    18 : IntegerField('player_score'),
    19 : IntegerField('opponent_score'),
    20 : IntegerField('stroke_count'),
    21 : IntegerField('zone_count'),
    22 : EnhancedRespirationRateField('enhanced_avg_respiration_rate'),
    23 : EnhancedRespirationRateField('enhanced_max_respiration_rate'),
    24 : RespirationRateField('avg_respiration_rate'),
    25 : RespirationRateField('max_respiration_rate'),
}
