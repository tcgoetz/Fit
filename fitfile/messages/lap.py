"""Structured data for decoding a FIT file lap message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import IntegerField, HeartRateField, EnhancedRespirationRateField, Volume, TimestampField, NamedField, TimeMsField, CaloriesField, PowerField, \
    LeftRightBalanceField, WorkField, PercentField, FractionalCadenceField, FractionalCyclesField, BytePercentField, MessageIndexField, EventField, EventTypeField, \
    LapTriggerField, LatiitudeField, LongitudeField, DistanceCentimetersToMetersField, SpeedMpsField, DistanceMetersField, AltitudeField, \
    TemperatureField, DistanceMillimetersField, SportField, SubSportField, SportBasedCyclesField, SportBasedCadenceField, CadenceField, RespirationRateField, FloatField


lap_message = {
    0 : EventField(),
    1 : EventTypeField(),
    2 : TimestampField('start_time', utc=True),
    3 : LatiitudeField('start_position_lat'),
    4 : LongitudeField('start_position_long'),
    5 : LatiitudeField('end_position_lat'),
    6 : LongitudeField('end_position_long'),
    7 : TimeMsField('total_elapsed_time'),
    8 : TimeMsField('total_timer_time'),
    9 : DistanceCentimetersToMetersField('total_distance'),
    10 : SportBasedCyclesField('total_cycles'),
    11 : CaloriesField('total_calories'),
    12 : CaloriesField('total_fat_calories'),
    13 : SpeedMpsField('avg_speed'),  # 16 bit version
    14 : SpeedMpsField('max_speed'),  # 16 bit version
    15 : HeartRateField('avg_heart_rate'),
    16 : HeartRateField('max_heart_rate'),
    17 : SportBasedCadenceField('avg_cadence'),
    18 : SportBasedCadenceField('max_cadence'),
    19 : PowerField('avg_power'),
    20 : PowerField('max_power'),
    21 : DistanceMetersField('total_ascent'),
    22 : DistanceMetersField('total_descent'),
    23 : IntegerField('intensity'),
    24 : LapTriggerField(),
    25 : SportField(),
    26 : NamedField('event_group'),
    27 : LatiitudeField('nec_lat'),
    28 : LongitudeField('nec_long'),
    29 : LatiitudeField('swc_lat'),
    30 : LongitudeField('swc_long'),
    #
    32 : IntegerField('num_lengths'),
    33 : PowerField('normalized_power'),
    34 : LeftRightBalanceField('left_right_balance'),
    35 : IntegerField('first_length_index'),
    #
    37 : DistanceCentimetersToMetersField('avg_stroke_distance'),
    38 : NamedField('swim_stroke'),
    39 : SubSportField(),
    40 : IntegerField('num_active_lengths'),
    41 : WorkField(),
    42 : AltitudeField('avg_altitude'),  # 16 bit version
    43 : AltitudeField('max_altitude'),  # 16 bit version
    44 : DistanceMetersField('gps_accuracy'),
    45 : PercentField('avg_grade'),
    46 : PercentField('avg_pos_grade'),
    47 : PercentField('avg_neg_grade'),
    48 : PercentField('max_pos_grade'),
    49 : PercentField('max_neg_grade'),
    50 : TemperatureField('avg_temperature'),
    51 : TemperatureField('max_temperature'),
    52 : TimeMsField('total_moving_time'),
    53 : SpeedMpsField('avg_pos_vertical_speed'),
    54 : SpeedMpsField('avg_neg_vertical_speed'),
    55 : SpeedMpsField('max_pos_vertical_speed'),
    56 : SpeedMpsField('max_neg_vertical_speed'),
    57 : TimeMsField('time_in_hr_zone'),
    58 : TimeMsField('time_in_speed_zone'),
    59 : TimeMsField('time_in_cadence_zone'),
    60 : TimeMsField('time_in_power_zone'),
    61 : IntegerField('repetition_num'),
    62 : AltitudeField('min_altitude'),  # 16 bit version
    63 : HeartRateField('min_heart_rate'),
    #
    70 : NamedField('swim_time'),
    71 : MessageIndexField('wkt_step_index'),
    72 : IntegerField('average_stroke'),
    73 : IntegerField('avg_swolf'),
    74 : NamedField('opponent_score'),
    75 : IntegerField('stroke_count'),
    76 : IntegerField('zone_count'),
    77 : DistanceMillimetersField('avg_vertical_oscillation'),
    78 : PercentField('avg_stance_time_percent'),
    79 : TimeMsField('avg_stance_time', scale=10.0),
    80 : FractionalCadenceField('avg_fractional_cadence'),
    81 : FractionalCadenceField('max_fractional_cadence'),
    82 : FractionalCyclesField(),
    83 : NamedField('player_score'),
    84 : NamedField('avg_total_hemoglobin_conc'),
    85 : NamedField('min_total_hemoglobin_conc'),
    86 : NamedField('max_total_hemoglobin_conc'),
    87 : PercentField('avg_saturated_hemoglobin_percent'),
    88 : PercentField('min_saturated_hemoglobin_percent'),
    89 : PercentField('max_saturated_hemoglobin_percent'),
    91 : BytePercentField('avg_left_torque_effectiveness'),
    92 : BytePercentField('avg_right_torque_effectiveness'),
    93 : BytePercentField('avg_left_pedal_smoothness'),
    94 : BytePercentField('avg_right_pedal_smoothness'),
    95 : BytePercentField('avg_combined_pedal_smoothness'),
    #
    98 : TimeMsField('time_standing'),
    99 : IntegerField('stand_count'),
    100 : NamedField('avg_left_pco'),
    101 : NamedField('avg_right_pco'),
    102 : NamedField('avg_left_power_phase'),
    103 : NamedField('avg_left_power_phase_peak'),
    104 : NamedField('avg_right_power_phase'),
    105 : NamedField('avg_right_power_phase_peak'),
    106 : PowerField('avg_power_position'),
    107 : PowerField('max_power_position'),
    108 : CadenceField('avg_cadence_position'),
    109 : CadenceField('max_cadence_position'),
    110 : SpeedMpsField('avg_speed'),  # 32 bit version
    111 : SpeedMpsField('max_speed'),  # 32 bit version
    112 : AltitudeField('avg_altitude'),  # 32 bit version
    113 : AltitudeField('min_altitude'),  # 32 bit version
    114 : AltitudeField('max_altitude'),  # 32 bit version
    115 : PowerField('avg_lev_motor_power'),
    116 : PowerField('max_lev_motor_power'),
    117 : BytePercentField('lev_battery_consumption'),
    118 : PercentField('avg_vertical_ratio', 100.0),
    119 : PercentField('avg_stance_time_balance'),
    120 : DistanceMillimetersField('avg_step_length'),
    121 : SpeedMpsField('avg_vam'),
    122 : DistanceMetersField('avg_depth'),
    123 : DistanceMetersField('max_depth'),
    124 : TemperatureField('min_temperature'),
    #
    136 : EnhancedRespirationRateField('enhanced_avg_respiration_rate'),
    137 : EnhancedRespirationRateField('enhanced_max_respiration_rate'),
    #
    145 : Volume('est_sweat_loss'),
    #
    147 : RespirationRateField('avg_respiration_rate'),
    148 : RespirationRateField('max_respiration_rate'),
    149 : FloatField('total_grit', units='kGrit'),
    150 : FloatField('total_flow', units='Flow'),
    151 : IntegerField('jump_count'),
    152 : PercentField('execution_score'),
    153 : FloatField('avg_grit', units='kGrit'),
    154 : FloatField('avg_flow', units='Flow'),
    155 : CaloriesField('resting_calories'),
    156 : DistanceCentimetersToMetersField('total_fractional_ascent'),
    157 : DistanceCentimetersToMetersField('total_fractional_descent'),
    158 : TemperatureField('avg_core_temperature'),
    159 : TemperatureField('min_core_temperature'),
    160 : TemperatureField('max_core_temperature'),
    161 : SpeedMpsField('grade_adjusted_speed'),
    #
    163 : PercentField('unpaved'),
    164 : SpeedMpsField('step_speed_loss_distance'),
    165 : PercentField('step_speed_loss_percent'),
    166 : IntegerField('avg_force'),
    167 : IntegerField('max_force'),
    168 : IntegerField('normalized_force'),
}
