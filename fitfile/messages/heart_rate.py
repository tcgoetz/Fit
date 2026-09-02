"""Structured data for decoding a FIT file message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import BoolField, NamedField, HeartRateField, StringField, HeartRateZonesTimerTypeField, IntegerField, TimeMsField, HeartRateZoneCalcField, \
    PowerZoneCalcField, HeartRateVarianceField, HeartRateVarianceStatusField


hrm_profile_message = {
    0 : BoolField('enabled'),
    1 : NamedField('hrm_ant_id'),
    2 : BoolField('log_hrv'),
    3 : NamedField('hrm_ant_id_trans_type'),
}


hr_zone_message = {
    1 : HeartRateField('high_bpm'),
    2 : StringField('name'),
}


time_in_zone_message = {
    0 : HeartRateZonesTimerTypeField(),
    1 : IntegerField('reference_index'),
    2 : TimeMsField('time_in_hr_zone'),
    3 : TimeMsField('time_in_speed_zone'),
    4 : TimeMsField('time_in_cadence_zone'),
    5 : TimeMsField('time_in_power_zone'),
    6 : IntegerField('hr_zone_high_boundary'),
    7 : IntegerField('speed_zone_high_boundary'),
    8 : IntegerField('cadence_zone_high_bondary'),
    9 : IntegerField('power_zone_high_boundary'),
    10: HeartRateZoneCalcField(),
    11 : HeartRateField('max_heart_rate'),
    12 : HeartRateField('resting_heart_rate'),
    13 : HeartRateField('lactate_threshhold_heart_rate'),
    14 : PowerZoneCalcField(),
    15 : IntegerField('functional_threshold_power')
}


hrv_status_summary_message = {
    0 : HeartRateVarianceField('weekly_average'),           # RMSSD weekly average (scale 128)
    1 : HeartRateVarianceField('last_night'),               # Last night RMSSD (scale 128)
    2 : HeartRateVarianceField('last_night_average'),       # Last night average (scale 128)
    3 : HeartRateVarianceField('baseline_low'),             # Baseline low bound (scale 128)
    4 : HeartRateVarianceField('baseline_high'),            # Baseline high bound (scale 128)
    5 : HeartRateVarianceField('baseline_balanced_low'),    # Balanced range low (scale 128)
    6 : HeartRateVarianceStatusField(),                     # HRV status (0=unknown, 2=poor, 3=low, 4=balanced)
    7 : IntegerField('reading_count'),                      # Number of readings
    8 : HeartRateVarianceField('baseline_balanced_high')    # Balanced range high (scale 128)
}
