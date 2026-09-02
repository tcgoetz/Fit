"""Structured data for decoding a FIT file totals message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import FileTypeField, ManufacturerField, ProductField, IntegerField, TimestampField, LatiitudeField, LongitudeField, DistanceCentimetersToMetersField, \
    SpeedMpsField, TimeSField, AutoLapModeField, AutoPauseSettingField, PowerAveragingField, AutoScrollModeField, SwitchField, SatellitesField, VolumeUnitsField, \
    SelfEvaluationStatusField, TouchStatusField, RunningPowerModeField, ClimbProModeModeField, ClimbDetectionField, ClimbProTerrainField


training_settings_message = {
    2 : SpeedMpsField('virtual_partner_pace'),
    3 : AutoLapModeField(),
    4 : DistanceCentimetersToMetersField('auto_lap_distance'),
    5 : LatiitudeField('lat_5'),
    6 : LongitudeField('long_6'),
    7 : AutoPauseSettingField(),
    8 : IntegerField('auto_pause_threshold'),
    #
    12 : PowerAveragingField(),
    #
    15 : AutoScrollModeField(),
    #
    18 : SwitchField('timer_start_prompt'),
    #
    22 : DistanceCentimetersToMetersField('pool_length'),
    #
    25 : SwitchField('auto_sleep'),
    #
    27 : SatellitesField(),
    #
    31 : DistanceCentimetersToMetersField('target_distance'),
    32 : SpeedMpsField('target_speed'),
    33 : TimeSField('target_time'),
    #
    35 : SwitchField('speed_3d'),
    36 : SwitchField('distance_3d'),
    37 : SwitchField('auto_climb'),
    #
    40 : SwitchField('auto_climb_invert_colors'),
    41 : SpeedMpsField('auto_climb_vertical_speed'),
    42 : TimeSField('auto_climb_mode_switch'),
    #
    46 : SwitchField('lap_key'),
    #
    50 : SwitchField('workout_target_alerts'),
    51 : SwitchField('timer_start_auto'),
    52 : SpeedMpsField('timer_start_speed'),
    53 : SwitchField('segment_alerts'),
    #
    57 : SwitchField('countdown_start'),
    #
    63 : SwitchField('climb_pro'),
    #
    67 : SwitchField('track_consumption'),
    #
    69 : IntegerField('bottle_size'),
    70 : VolumeUnitsField(),
    #
    80 : TimeSField('minimum_ride_duration'),
    #
    86 : IntegerField('lane_number'),
    87 : SwitchField('broadcast_heart_rate'),
    #
    93 : SelfEvaluationStatusField(),
    #
    102 : SwitchField('speed_pro'),
    103 : TouchStatusField(),
    #
    106 : SwitchField('record_temperature'),
    #
    109 : RunningPowerModeField(),
    110 : SwitchField('account_for_wind'),
    111 : ClimbProModeModeField(),
    #
    117 : ClimbDetectionField(),
    #
    119 : ClimbProTerrainField(),
    #
    153 : SpeedMpsField('precise_target_speed'),
    #
    1001 : SwitchField('gps'),
    1002 : SwitchField('glonass'),
    1003 : SwitchField('galileo'),
    1004 : SwitchField('beidou'),
}


training_file_message = {
    0 : FileTypeField('type'),
    1 : ManufacturerField(),
    2 : ProductField(),
    3 : IntegerField('serial_number'),
    4 : TimestampField('time_created', utc=True),
}
