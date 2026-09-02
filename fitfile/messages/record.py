"""Structured data for decoding a FIT file record message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import IntegerField, HeartRateField, EnhancedRespirationRateField, AbsolutePressureField, FloatField, NamedField, TimeMsField, CaloriesField, PowerField, \
    LeftRightBalanceField, PercentField, TimeSField, FractionalCadenceField, BytePercentField, LatiitudeField, LongitudeField, DistanceCentimetersToKmsField, SpeedMpsField, \
    DistanceMetersField, AltitudeField, TemperatureField, DistanceMillimetersField, CompressedSpeedDistanceField, CadenceField, ActivityBasedCyclesField, ActivityTypeField, \
    DistanceCentimetersToMetersField, RespirationRateField, DistanceKmsField, PressureField, FlowRateField


record_message = {
    0 : LatiitudeField('position_lat'),
    1 : LongitudeField('position_long'),
    2 : AltitudeField('altitude'),  # 16 bit version
    3 : HeartRateField('heart_rate'),
    4 : CadenceField(),
    5 : DistanceCentimetersToKmsField('distance'),
    6 : SpeedMpsField('speed'),  # 16 bit version
    7 : PowerField(),
    8 : CompressedSpeedDistanceField(),
    9 : PercentField('grade'),
    10 : NamedField('resistance'),
    11 : TimeMsField('time_from_course'),
    12 : DistanceMetersField('cycle_length', scale=100),
    13 : TemperatureField('temperature'),
    17 : SpeedMpsField('speed_1s'),
    18 : ActivityBasedCyclesField(),
    19 : ActivityBasedCyclesField('total_cycles'),
    #
    28 : NamedField('accumulated_power'),  # 16 bit version
    29 : NamedField('accumulated_power'),  # 32 bit version
    30 : LeftRightBalanceField('left_right_balance'),
    31 : DistanceMetersField('gps_accuracy'),
    32 : SpeedMpsField('vertical_speed'),
    33 : CaloriesField(),
    #
    39 : DistanceMillimetersField('avg_vertical_oscillation'),
    40 : PercentField('stance_time_percent'),
    41 : TimeMsField('stance_time', scale=10.0),
    42 : ActivityTypeField(),
    43 : BytePercentField('left_torque_effectiveness'),
    44 : BytePercentField('right_torque_effectiveness'),
    45 : BytePercentField('left_pedal_smoothness'),
    46 : BytePercentField('right_pedal_smoothness'),
    47 : BytePercentField('combined_pedal_smoothness'),
    48 : NamedField('time128'),
    49 : NamedField('stroke_type'),
    50 : NamedField('zone'),
    51 : NamedField('ball_speed'),
    52 : CadenceField('cadence256'),
    53 : FractionalCadenceField(),
    54 : NamedField('total_hemoglobin_conc'),
    55 : NamedField('total_hemoglobin_conc_min'),
    56 : NamedField('total_hemoglobin_conc_max'),
    57 : PercentField('saturated_hemoglobin_percent'),
    58 : PercentField('saturated_hemoglobin_percent_min'),
    59 : PercentField('saturated_hemoglobin_percent_max'),
    #
    62 : IntegerField('device_index'),
    #
    67 : NamedField('left_pco'),
    68 : NamedField('right_pco'),
    69 : NamedField('left_power_phase'),
    70 : NamedField('left_power_phase_peak'),
    71 : NamedField('right_power_phase'),
    72 : NamedField('right_power_phase_peak'),
    73 : SpeedMpsField('speed'),  # 32 bit version
    #
    78 : AltitudeField('altitude'),  # 32 bit version
    #
    81 : PercentField('battery_soc'),
    82 : PowerField('motor_power'),
    83 : PercentField('vertical_ratio', 100.0),
    84 : PercentField('stance_time_balance'),
    85 : DistanceMillimetersField('step_length'),
    #
    87 : DistanceCentimetersToMetersField('cycle_length16'),
    #
    90 : IntegerField('performance_condition'),
    91 : AbsolutePressureField(),
    92 : DistanceMillimetersField('depth'),
    93 : DistanceMillimetersField('next_stop_depth'),
    94 : TimeSField('next_stop_time'),
    95 : TimeSField('time_to_surface'),
    96 : TimeSField('ndl_time'),
    97 : PercentField('cns_load'),
    98 : PercentField('n2_load'),
    99 : RespirationRateField('respiration_rate'),
    #
    108 : EnhancedRespirationRateField('enhanced_respiration_rate'),
    #
    114 : FloatField('grit'),
    115 : FloatField('flow'),
    116 : NamedField('current_stress'),
    117 : DistanceKmsField('ebike_travel_range'),
    118 : PercentField('ebike_battery_level'),
    119 : NamedField('ebike_assist_mode'),
    120 : PercentField('ebike_assist_level_percent'),
    #
    121 : IntegerField('total_ascent'),
    #
    123 : TimeSField('air_time_remaining'),
    124 : PressureField('pressure_sac'),
    125 : FlowRateField('volume_sac'),
    126 : FlowRateField('rmv'),
    127 : SpeedMpsField('ascent_rate'),
    #
    129 : PercentField('po2'),
    #
    136 : HeartRateField('wrist_heart_rate'),
    137 : IntegerField('stamina_potential'),
    138 : IntegerField('stamina'),
    139 : TemperatureField('core_temperature'),
    140 : SpeedMpsField('grade_adjusted_speed'),
    143 : IntegerField('body_battery'),
    144 : HeartRateField('external_heart_rate'),
    146 : SpeedMpsField('step_speed_loss_distance'),
    147 : SpeedMpsField('step_speed_loss_percent'),
    148 : IntegerField('force'),
}
