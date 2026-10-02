"""Structured data for decoding a FIT file split message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import TimeMsField, TimestampField, DistanceMetersField, HeartRateField, FloatField, CaloriesField, SportBasedGradeField, ClimbingRouteComletedField, IntegerField, \
    SpeedMpsField, DistanceCentimetersToMetersField, LatiitudeField, LongitudeField, AltitudeField, TimeSField, SportField, SubSportField, EnhancedCadenceField, \
    TemperatureField, DistanceMillimetersField, PercentField, PowerField, HeartRateVarianceField, SplitTypeField, EventField, EventTypeField, SwimStrokesField, SwimStrokeField, \
    SwimStrokesCadenceField, LengthTypeField, EnhancedRespirationRateField, RespirationRateField, CyclesField, LeftRightBalanceField, NamedField, BytePercentField, \
    DistanceMillimetersToMetersField, FractionalCyclesField, TrainingEffectField


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
    17 : LatiitudeField('nec_lat'),
    18 : LatiitudeField('nec_long'),
    19 : LatiitudeField('swc_lat'),
    20 : LatiitudeField('swc_long'),
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
    31 : CyclesField('total_cycles'),
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
    43 : LeftRightBalanceField(),
    44 : TimeMsField('time_standing'),
    45 : DistanceMillimetersField('avg_left_pco'),
    46 : DistanceMillimetersField('avg_right_pco'),
    47 : NamedField('avg_left_power_phase'),
    48 : NamedField('avg_left_power_phase_peak'),
    49 : NamedField('avg_right_power_phase'),
    50 : NamedField('avg_right_power_phase_peak'),
    51 : PowerField('avg_power_position'),
    52 : PowerField('max_power_position'),
    53 : BytePercentField('avg_left_torque_effectiveness'),
    54 : BytePercentField('avg_right_torque_effectiveness'),
    55 : BytePercentField('avg_left_pedal_smoothness'),
    56 : BytePercentField('avg_right_pedal_smoothness'),
    57 : BytePercentField('avg_combined_pedal_smoothness'),
    58 : FloatField('avg_flow', units='Flow'),
    59 : FloatField('total_grit', units='kGrit'),
    #
    62 : SwimStrokeField(),
    63 : IntegerField('num_active_lengths'),
    64 : IntegerField('avg_swolf'),
    65 : DistanceCentimetersToMetersField('avg_stroke_distance'),
    66 : SwimStrokesCadenceField('avg_strokes_per_length'),
    67 : IntegerField('lap_index'),
    68 : IntegerField('num_laps'),
    69 : IntegerField('climb_grading_scale'),
    70 : SportBasedGradeField('grade'),
    71 : ClimbingRouteComletedField('completed'),
    72 : IntegerField('num_falls'),
    73 : IntegerField('climb_send'),
    74 : AltitudeField('start_elevation'),
    #
    78 : TimeSField('active_time'),
    79 : CaloriesField('resting_calories'),
    80 : DistanceCentimetersToMetersField('total_fractional_ascent'),
    81 : DistanceCentimetersToMetersField('total_fractional_descent'),
    #
    88 : PercentField('avg_grade'),
    89 : PercentField('max_grade'),
    90 : EnhancedCadenceField('min_cadence'),
    #
    93 : SpeedMpsField('grade_adjusted_speed'),
    94 : HeartRateVarianceField('avg_hrv'),
    95 : HeartRateVarianceField('max_hrv'),
    #
    99 : SpeedMpsField('avg_vam'),
    #
    104 : IntegerField('jump_count'),
    105 : TimeMsField('pedaling_time'),
    106 : TimeMsField('cruising_time'),
    107 : IntegerField('beginning_potential'),
    108 : IntegerField('ending_potential'),
    109 : IntegerField('min_stamina'),
    110 : TimeMsField('total_moving_time'),
    #
    112 : IntegerField('dive_section_type'),
    113 : SpeedMpsField('avg_ascent_rate'),
    114 : SpeedMpsField('max_ascent_rate'),
    115 : SpeedMpsField('avg_descent_rate'),
    116 : SpeedMpsField('max_descent_rate'),
    117 : TimeMsField('total_ascent_time'),
    118 : TimeMsField('total_descent_time'),
    119 : TimeMsField('total_hang_time'),
    120 : IntegerField('apnea_discipline'),
    121 : DistanceMillimetersToMetersField('avg_depth'),
    122 : DistanceMillimetersToMetersField('max_depth'),
    #
    124 : HeartRateField('min_heart_rate'),
    #
    127 : TimeSField('surface_interval'),
    #
    130 : SpeedMpsField('step_speed_loss_distance'),
    131 : PercentField('step_speed_loss_percent'),
    #
    135 : IntegerField('avg_force', scale=1000.0),
    136 : IntegerField('max_force', scale=1000.0),
    #
    140 : IntegerField('normalized_force', scale=1000.0),
    #
    142 : FractionalCyclesField(),
    #
    144 : PercentField('avg_stance_time_percent'),
    #
    168 : TrainingEffectField('total_anaerobic_training_effect'),
    169 : IntegerField('front_gear_shift_count'),
    170 : IntegerField('rear_gear_shift_count'),
}

split_summary_message = {
    0 : SplitTypeField(),
    1 : SportField(),
    2 : SubSportField(),
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
    16 : CyclesField('total_cycles'),
    17 : TemperatureField('avg_temperature'),
    18 : TemperatureField('max_temperature'),
    19 : TemperatureField('min_temperature'),
    20 : DistanceMillimetersField('avg_vertical_oscillation'),
    21 : PercentField('avg_vertical_ratio', 100.0),
    22 : TimeMsField('avg_stance_time', scale=10.0),
    23 : PercentField('avg_stance_time_balance'),
    24 : DistanceMillimetersField('avg_step_length'),
    25 : PowerField('avg_power'),
    26 : PowerField('max_power'),
    27 : PowerField('normalized_power'),
    28 : LeftRightBalanceField(),
    29 : TimeMsField('time_standing'),
    30 : DistanceMillimetersField('avg_left_pco'),
    31 : DistanceMillimetersField('avg_right_pco'),
    32 : NamedField('avg_left_power_phase'),
    33 : NamedField('avg_left_power_phase_peak'),
    34 : NamedField('avg_right_power_phase'),
    35 : NamedField('avg_right_power_phase_peak'),
    36 : PowerField('avg_power_position'),
    37 : PowerField('max_power_position'),
    38 : BytePercentField('avg_left_torque_effectiveness'),
    39 : BytePercentField('avg_right_torque_effectiveness'),
    40 : BytePercentField('avg_left_pedal_smoothness'),
    41 : BytePercentField('avg_right_pedal_smoothness'),
    42 : BytePercentField('avg_combined_pedal_smoothness'),
    43 : FloatField('avg_flow', units='Flow'),
    44 : FloatField('total_grit', units='kGrit'),
    #
    47 : SwimStrokeField(),
    48 : IntegerField('num_active_lengths'),
    49 : IntegerField('avg_swolf'),
    50 : DistanceCentimetersToMetersField('avg_stroke_distance'),
    51 : SwimStrokesCadenceField('avg_strokes_per_length'),
    #
    52 : DistanceMetersField('avg_split_ascent'),
    53 : DistanceMetersField('max_split_ascent'),
    54 : IntegerField('climb_grading_scale'),
    55 : SportBasedGradeField('grade'),
    56 : IntegerField('num_falls'),
    #
    58 : IntegerField('num_climbs_attempted'),
    59 : IntegerField('num_climbs_completed'),
    60 : DistanceMillimetersField('max_split_distance'),
    #
    64 : CaloriesField('resting_calories'),
    65 : TimeMsField('active_time'),
    66 : DistanceCentimetersToMetersField('total_fractional_ascent'),
    67 : DistanceCentimetersToMetersField('total_fractional_descent'),
    68 : DistanceCentimetersToMetersField('avg_fractional_ascent'),
    69 : DistanceCentimetersToMetersField('avg_fractional_descent'),
    #
    71 : SpeedMpsField('avg_grade_adjusted_speed'),
    72 : HeartRateVarianceField('avg_hrv'),
    73 : HeartRateVarianceField('max_hrv'),
    #
    76 : IntegerField('split_score_card_index'),
    77 : TimeMsField('total_moving_time'),
    #
    79  : TimestampField('first_start_time', utc=True),
    #
    83 : SpeedMpsField('step_speed_loss_distance'),
    84 : PercentField('step_speed_loss_percent'),
    #
    87 : HeartRateField('min_heart_rate'),
    #
    91 : PercentField('avg_stance_time_percent'),
    #
    101 : TimeMsField('max_total_timer_time')
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
    26 : CaloriesField('metabolic_calories')
}
