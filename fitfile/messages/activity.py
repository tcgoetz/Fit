"""Structured data for decoding a FIT file activity messages."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import TimeMsField, IntegerField, ActivityField, EventField, EventTypeField, TimestampField, NamedField, HeartRateField, TrainingEffectField, \
    TimeMinField, SportField, PowerField, TimeSField, DistanceMetersField, BenefitField, BoolField, WeightField, HeightField, \
    GenderField, Vo2MaxField, DistanceCentimetersToMetersField, DistanceMillimetersToMetersField, SubSportField, CaloriesField, ActivityClassField, \
    BestEffortDistance, MetaMaxField, SpeedKphField, TemperatureField, RespirationRateField, PercentField, StringField


activity_message = {
    0 : TimeMsField('total_timer_time'),
    1 : IntegerField('num_sessions'),
    2 : ActivityField(),
    3 : EventField(),
    4 : EventTypeField(),
    5 : TimestampField('local_timestamp', utc=False),
    6 : NamedField('event_group'),
    #
    8 : StringField('name')
}


activity_metrics_message = {
    0 : HeartRateField('avg_heart_rate'),
    1 : HeartRateField('max_heart_rate'),
    #
    4 : TrainingEffectField('aerobic_training_effect'),
    5 : MetaMaxField('energy_expenditure'),
    6 : CaloriesField('total_energy_expenditure'),
    7 : MetaMaxField('met_max'),
    8 : IntegerField('met_max_minutes'),
    9 : TimeMinField('recovery_time'),
    #
    11 : SportField(),
    12 : SubSportField(),
    13 : HeartRateField('minimal_hr'),
    14 : HeartRateField('lactate_threshold_heart_rate'),
    15 : PowerField('lactate_threshold_power'),
    16 : SpeedKphField('lactate_threshold_speed'),
    17 : IntegerField('ending_performance_condition'),
    #
    20 : TrainingEffectField('anaerobic_training_effect'),
    21 : RespirationRateField('respiratory_rate'),
    #
    24 : DistanceCentimetersToMetersField('3d_distance'),
    25 : IntegerField('ending_body_battery'),
    #
    29 : Vo2MaxField('activity_vo2_max'),
    30 : TemperatureField('avg_temperature'),
    31 : IntegerField('avg_humidity'),
    32 : DistanceMillimetersToMetersField('ascent'),
    #
    35 : TimeMsField('elapsed_time'),  # uint32			1000		s
    36 : DistanceCentimetersToMetersField('distance'),  # uint32			100		m
    #
    41 : BenefitField('primary_benefit'),
    #
    44 : CaloriesField('active_calories'),
    #
    48 : TimestampField('local_timestamp', utc=False),
    49 : PercentField('ending_load_stamina'),
    50 : IntegerField('ending_potential'),
    #
    53 : HeartRateField('hr_max'),
    #
    57 : TimeMinField('ascent_slow_minutes'),
    58 : TimeMinField('ascent_fast_minutes'),
    #
    60 : DistanceMetersField('total_ascent'),
    61 : DistanceMetersField('total_descent'),
    62 : IntegerField('ending_body_battery'),
    63 : HeartRateField('avg_heart_rate'),
    64 : WeightField('user_weight'),
    #
    69 : TimeSField('time_5k'),
    70 : TimeSField('time_10k'),
    71 : TimeSField('time_half_marathon'),
    72 : TimeSField('time_full_marathon'),
}


best_effort_message = {
    1 : SportField(),
    2 : BestEffortDistance(),  # uint32			100		m
    3 : TimeMsField('time'),  # uint32			1000		s
    4 : TimestampField('start_time', utc=False),
    5 : BoolField('personal_record')
}


workout_schedule_message = {
    1 : IntegerField('workout_index'),
    3 : BenefitField('est_benefit'),
    5 : TrainingEffectField('est_aerobic_training_effect'),
    6 : TrainingEffectField('est_anaerobic_training_effect'),
    7 : SportField(),
    9 : TimeSField('duration'),  # uint32			1000		s
}


user_metrics_message = {
    0 : Vo2MaxField('vo2_max'),
    1 : IntegerField('age'),
    2 : HeightField(),  # uint8			100		m
    3 : WeightField(),  # uint16			10		kg
    4 : GenderField(),
    5 : ActivityClassField(),
    6 : HeartRateField('max_heart_rate'),
    8 : TimeMinField('remaining_recovery_time'),  # uint16					min
    #
    9 : NamedField('monthly_load'),
    10 : HeartRateField('resting_heart_rate'),
    11 : HeartRateField('lactate_threshold_heart_rate'),
    12 : PowerField('lactate_threshold_power'),  # uint16					watts
    13 : SpeedKphField('lactate_threshold_speed'),  # uint16			10		km/h
    #
    15 : IntegerField('beginning_body_battery'),
    16 : TimestampField('start_of_activity', utc=False),
    17 : Vo2MaxField('pre_activity_vo2_max'),
    18 : Vo2MaxField('activity_vo2_max'),
    19 : Vo2MaxField('first_vo2_max'),  # sint32			18724.57143		ml/kg/min
    #
    23 : IntegerField('time_zone_offset'),
    #
    25 : TimeSField('wake_time'),
    26 : TimeSField('sleep_time'),
    #
    29 : DistanceCentimetersToMetersField('running_max_distance'),
    30 : DistanceCentimetersToMetersField('cycling_max_distance'),
    31 : PercentField('stamina_potential_load'),
    32 : PercentField('stamina_potential_distance'),
    33 : TimeMinField('recovery_minutes'),
    #
    35 : TimestampField('end_of_previous_activity', utc=False),
    #
    38 : TimeMinField('sleep_need'),
    39 : TimestampField('wake_up_time', utc=False),
    40 : IntegerField('wheelchair'),
    #
    44 : SportField()
}
