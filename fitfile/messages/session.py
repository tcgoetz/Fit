"""Structured data for decoding a FIT file session message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import IntegerField, FloatField, HeartRateField, StringField, EnhancedRespirationRateField, Volume, TimestampField, NamedField, TimeMsField, CaloriesField, \
    TrainingEffectField, LeftRightBalanceField, WorkField, PercentField, FractionalCadenceField, FractionalCyclesField, BytePercentField, EventField, SessionTriggerField, \
    DisplayMeasureField, LatiitudeField, LongitudeField, DistanceCentimetersToKmsField, SpeedMpsField, DistanceMetersField, DistanceCentimetersToMetersField, AltitudeField, \
    TemperatureField, DistanceMillimetersField, WeightField, SportField, SubSportField, SportBasedCyclesField, SportBasedCadenceField, CadenceField, BenefitField, TimeSField, \
    RespirationRateField, HeartRateVarianceField, SwitchField, PowerField, SwimStrokesCadenceField


session_message = {
    0 : EventField(),
    1 : EventField(),
    2 : TimestampField('start_time', utc=True),
    3 : LatiitudeField('start_position_lat'),
    4 : LongitudeField('start_position_long'),
    5 : SportField(),
    6 : SubSportField(),
    7 : TimeMsField('total_elapsed_time'),
    8 : TimeMsField('total_timer_time'),
    9 : DistanceCentimetersToKmsField('total_distance'),
    10 : SportBasedCyclesField('total_cycles'),
    11 : CaloriesField('total_calories'),
    13 : CaloriesField('total_fat_calories'),
    14 : SpeedMpsField('avg_speed'),  # 16 bit version
    15 : SpeedMpsField('max_speed'),  # 16 bit version
    16 : HeartRateField('avg_heart_rate'),
    17 : HeartRateField('max_heart_rate'),
    18 : SportBasedCadenceField('avg_cadence'),
    19 : SportBasedCadenceField('max_cadence'),
    20 : PowerField('avg_power'),
    21 : PowerField('max_power'),
    22 : DistanceMetersField('total_ascent'),
    23 : DistanceMetersField('total_descent'),
    24 : TrainingEffectField('total_training_effect'),
    25 : IntegerField('first_lap_index'),
    26 : IntegerField('num_laps'),
    27 : NamedField('event_group'),
    28 : SessionTriggerField(),
    29 : LatiitudeField('nec_lat'),
    30 : LongitudeField('nec_long'),
    31 : LatiitudeField('swc_lat'),
    32 : LongitudeField('swc_long'),
    33 : IntegerField('length_count'),
    34 : PowerField('normalized_power'),
    35 : TrainingEffectField('training_stress_score'),
    36 : NamedField('intensity_factor'),
    37 : LeftRightBalanceField('left_right_balance'),
    38 : LatiitudeField('end_position_lat'),
    39 : LongitudeField('end_position_long'),
    #
    41 : IntegerField('avg_stroke_count'),
    42 : DistanceCentimetersToMetersField('avg_stroke_distance'),
    43 : NamedField('swim_stroke'),
    44 : DistanceCentimetersToMetersField('pool_length'),
    45 : PowerField('threshold_power'),
    46 : DisplayMeasureField('pool_length_unit'),
    47 : IntegerField('num_active_lengths'),
    48 : WorkField(),
    49 : AltitudeField('avg_altitude'),  # 16 bit version
    50 : AltitudeField('max_altitude'),  # 16 bit version
    51 : DistanceMetersField('gps_accuracy'),
    52 : PercentField('avg_grade'),
    53 : PercentField('avg_pos_grade'),
    54 : PercentField('avg_neg_grade'),
    55 : PercentField('max_pos_grade'),
    56 : PercentField('max_neg_grade'),
    57 : TemperatureField('avg_temperature'),
    58 : TemperatureField('max_temperature'),
    59 : TimeMsField('total_moving_time'),
    60 : SpeedMpsField('avg_pos_vertical_speed'),
    61 : SpeedMpsField('avg_neg_vertical_speed'),
    62 : SpeedMpsField('max_pos_vertical_speed'),
    63 : SpeedMpsField('max_neg_vertical_speed'),
    64 : HeartRateField('min_heart_rate'),
    65 : TimeMsField('time_in_hr_zone'),
    66 : TimeMsField('time_in_speed_zone'),
    67 : TimeMsField('time_in_cadence_zone'),
    68 : TimeMsField('time_in_power_zone'),
    69 : TimeMsField('avg_lap_time'),
    70 : IntegerField('best_lap_index'),
    71 : AltitudeField('min_altitude'),  # 16 bit version
    78 : TimeMsField('active_time'),
    79 : SwimStrokesCadenceField('avg_swimming_cadence'),    # strokes/length
    80 : NamedField('swolf'),
    82 : NamedField('player_score'),
    83 : NamedField('opponent_score'),
    84 : StringField('opponent_name'),
    85 : IntegerField('stroke_count'),
    86 : IntegerField('zone_count'),
    87 : SpeedMpsField('max_ball_speed'),
    88 : SpeedMpsField('avg_ball_speed'),
    89 : DistanceMillimetersField('avg_vertical_oscillation'),
    90 : PercentField('avg_stance_time_percent'),
    91 : TimeMsField('avg_stance_time', scale=10.0),
    92 : FractionalCadenceField('avg_fractional_cadence'),
    93 : FractionalCadenceField('max_fractional_cadence'),
    94 : FractionalCyclesField(),
    95 : FloatField('avg_total_hemoglobin_conc'),
    96 : FloatField('min_total_hemoglobin_conc'),
    97 : FloatField('max_total_hemoglobin_conc'),
    98 : PercentField('avg_saturated_hemoglobin_percent'),
    99 : PercentField('min_saturated_hemoglobin_percent'),
    100 : PercentField('max_saturated_hemoglobin_percent'),
    101 : BytePercentField('avg_left_torque_effectiveness'),
    102 : BytePercentField('avg_right_torque_effectiveness'),
    103 : BytePercentField('avg_left_pedal_smoothness'),
    104 : BytePercentField('avg_right_pedal_smoothness'),
    105 : BytePercentField('avg_combined_pedal_smoothness'),
    #
    107 : IntegerField('front_shifts'),
    108 : IntegerField('rear_shifts'),
    #
    110 : StringField('sport_name'),
    111 : IntegerField('sport_index'),
    112 : TimeMsField('time_standing'),
    113 : NamedField('stand_count'),
    114 : NamedField('avg_left_pco'),
    115 : NamedField('avg_right_pco'),
    116 : NamedField('avg_left_power_phase'),
    117 : NamedField('avg_left_power_phase_peak'),
    118 : NamedField('avg_right_power_phase'),
    119 : NamedField('avg_right_power_phase_peak'),
    120 : PowerField('avg_power_position'),
    121 : PowerField('max_power_position'),
    122 : CadenceField('avg_cadence_position'),
    123 : CadenceField('max_cadence_position'),
    124 : SpeedMpsField('avg_speed'),  # 32 bit version
    125 : SpeedMpsField('max_speed'),  # 32 bit version
    126 : AltitudeField('avg_altitude'),  # 32 bit version
    127 : AltitudeField('min_altitude'),  # 32 bit version
    128 : AltitudeField('max_altitude'),  # 32 bit version
    129 : PowerField('avg_lev_motor_power'),
    130 : PowerField('max_lev_motor_power'),
    131 : BytePercentField('lev_battery_consumption'),
    132 : PercentField('avg_vertical_ratio'),
    133 : PercentField('avg_stance_time_balance'),
    134 : DistanceMillimetersField('avg_step_length'),
    #
    137 : TrainingEffectField('total_anaerobic_training_effect'),
    #
    139 : SpeedMpsField('avg_vam'),
    140 : AltitudeField('avg_depth'),
    141 : AltitudeField('max_depth'),
    142 : TimeSField('surface_interval'),
    143 : PercentField('start_cns'),
    144 : PercentField('end_cns'),
    145 : PercentField('start_n2'),
    146 : PercentField('end_n2'),
    147 : RespirationRateField('avg_respiration_rate'),
    148 : RespirationRateField('max_respiration_rate'),
    149 : RespirationRateField('min_respiration_rates'),
    150 : TemperatureField('min_temperature'),
    151 : IntegerField('total_sets'),
    152 : Volume('unknonw_volume'),  # uint32			100		kg
    #
    155 : IntegerField('o2_toxicity', units='OTUs'),
    156 : IntegerField('DiveNumberFieldNum'),
    #
    168 : IntegerField('training_load_peak'),
    169 : EnhancedRespirationRateField('enhanced_avg_respiration_rate'),
    170 : EnhancedRespirationRateField('enhanced_max_respiration_rate'),
    #
    177 : CaloriesField('calories_consumed'),
    178 : Volume('est_sweat_loss'),
    179 : Volume('fluid_consumed'),
    180 : EnhancedRespirationRateField('enhanced_min_respiration_rate'),
    181 : FloatField('total_grit', units='kGrit'),
    182 : FloatField('total_flow', units='Flow'),
    183 : IntegerField('jump_count'),
    #
    185 : PercentField('execution_score'),
    186 : FloatField('avg_grit', units='kGrit'),
    187 : FloatField('avg_flow', units='Flow'),
    #
    188 : BenefitField('primary_benefit'),
    #
    192 : IntegerField('workout_feel'),
    193 : IntegerField('workout_rpe'),
    194 : PercentField('avg_spo2'),
    195 : PercentField('avg_stress'),
    196 : CaloriesField('metabolic_calories'),
    197 : HeartRateVarianceField('sdrr_hrv'),
    198 : HeartRateVarianceField('rmssd_hrv'),
    199 : DistanceCentimetersToMetersField('total_fractional_ascent'),
    200 : DistanceCentimetersToMetersField('total_fractional_descent'),
    #
    202 : IntegerField('recovery_heart_rate'),
    #
    205 : IntegerField('beginning_potential'),
    206 : IntegerField('ending_potential'),
    207 : IntegerField('min_stamina'),
    208 : TemperatureField('avg_core_temperature'),
    209 : TemperatureField('min_core_temperature'),
    210 : TemperatureField('max_core_temperature'),
    #
    211 : SpeedMpsField('grade_adjusted_speed'),
    212 : SwitchField('wind_data'),
    215 : IntegerField('beginning_body_battery'),
    216 : IntegerField('ending_body_battery'),
    #
    220 : WeightField('pack_weight'),  # 10		kg
    #
    222 : SpeedMpsField('step_speed_loss_distance'),
    223 : SpeedMpsField('step_speed_loss_percent'),
    224 : IntegerField('avg_force', scale=1000.0),
    225 : IntegerField('max_force', scale=1000.0),
    226 : IntegerField('normalized_force', scale=1000.0),
}
