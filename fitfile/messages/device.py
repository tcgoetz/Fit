"""Structured data for decoding a FIT file device info message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import IntegerField, StringField, VersionField, NamedField, TimeMsField, DeviceTypeField, BatteryVoltageField, BatteryStatusField, BodyLocationField, \
    AntNetworkField, SourceTypeField, ManufacturerField, ProductField, FloatField, BoolField, TimestampField, TimeSField, TimeHourField, TimeOffsetField, TimeModeField, \
    SwitchField, DateModeField, TimeMinField, BacklightModeField, DisplayOrientationField, SideField, AutoSyncFrequencyField, AutoActivityDetectField, PercentField, \
    TemperatureField, EpoCpeStatusField, LatiitudeField, LongitudeField, AltitudeField, SpeedMpsField, HeadingField, TapSensitivityField


device_info_message = {
    0 : IntegerField('device_index'),
    1 : DeviceTypeField(),
    2 : ManufacturerField(),
    3 : IntegerField('serial_number'),
    4 : ProductField(),
    5 : VersionField('software_version'),
    6 : NamedField('hardware_version'),
    7 : TimeMsField('cum_operating_time', scale=1000.0),
    #
    10 : BatteryVoltageField(),
    11 : BatteryStatusField(),
    #
    15 : NamedField('ant_related'),    # only found on ant devices?
    #
    18 : BodyLocationField('sensor_position'),
    19 : StringField('descriptor'),
    20 : NamedField('ant_transmission_type'),
    21 : NamedField('ant_device_number'),
    22 : AntNetworkField(),
    #
    24 : NamedField('ant_channel_id'),
    25 : SourceTypeField(),
    #
    27 : StringField('product_name'),
    #
    32 : PercentField('battery_level'),
}


device_status_message = {
    0 : TimeMinField('remaining_mins'),
    2 : PercentField('battery_level'),
    3 : TemperatureField(),
}


device_settings_message = {
    0 : NamedField('active_time_zone'),
    1 : FloatField('utc_offset'),
    2 : TimeOffsetField(),
    4 : TimeModeField(),
    5 : TimeHourField('time_zone_offset'),
    #
    8 : TimeSField('alarms_time'),
    #
    12 : BacklightModeField(),
    #
    28 : SwitchField('alarms_enabled'),
    #
    35 : SwitchField('switch_35'),
    36 : BoolField('activity_tracker_enabled'),
    #
    38 : SwitchField('switch_38'),
    39 : TimestampField('clock_time', utc=True),
    40 : NamedField('pages_enabled'),
    41 : SwitchField('switch_41'),
    42 : SwitchField('switch_42'),
    43 : SwitchField('switch_43'),
    44 : SwitchField('switch_44'),
    45 : SwitchField('switch_45'),
    46 : BoolField('move_alert_enabled'),
    47 : DateModeField(),
    48 : SwitchField('switch_48'),
    49 : SwitchField('switch_49'),
    #
    52 : SwitchField('switch_52'),
    53 : SwitchField('switch_53'),
    #
    55 : DisplayOrientationField('display_orientation'),
    56 : SideField(),
    57 : NamedField('default_page'),
    58 : NamedField('autosync_min_steps'),
    59 : NamedField('autosync_min_time'),
    #
    64 : SwitchField('switch_64'),
    65 : SwitchField('switch_65'),
    #
    68 : SwitchField('switch_68'),
    #
    80 : BoolField('lactate_threshold_autodetect_enabled'),
    81 : SwitchField('switch_81'),
    82 : SwitchField('switch_82'),
    83 : SwitchField('switch_83'),
    84 : SwitchField('switch_84'),
    85 : SwitchField('switch_85'),
    86 : BoolField('ble_auto_upload_enabled'),
    87 : SwitchField('switch_87'),
    #
    89 : AutoSyncFrequencyField(),
    90 : AutoActivityDetectField(),
    #
    92 : IntegerField('alarms_repeat'),
    #
    94 : IntegerField('number_of_screens'),
    95 : DisplayOrientationField('smart_notification_display_orientation'),
    #
    107 : SwitchField('switch_107'),
    108 : SwitchField('switch_108'),
    109 : SwitchField('switch_109'),
    110 : SwitchField('switch_110'),
    111 : SwitchField('switch_111'),
    112 : SwitchField('switch_112'),
    #
    126 : SwitchField('switch_126'),
    127 : SwitchField('switch_127'),
    128 : SwitchField('switch_128'),
    #
    133 : SwitchField('switch_133'),
    134 : SwitchField('tap_interface'),
    #
    141 : SwitchField('switch_141'),
    #
    174 : TapSensitivityField(),
}


device_used_message = {
    0 : IntegerField('speed'),
    1 : IntegerField('distance'),
    2 : IntegerField('cadence'),
    3 : IntegerField('elevation'),
    4 : IntegerField('heart_rate'),
    6 : IntegerField('power'),
}


epo_status_message = {
    0 : EpoCpeStatusField(),
    1 : TimestampField('start_time', utc=False),
    2 : TimestampField('end_time', utc=False),
    4 : LatiitudeField('start_pos'),
    5 : LongitudeField('end_pos'),
}


gps_metadata_message = {
    0 : TimeMsField('duration'),  # uint16			1000		ms
    1 : LatiitudeField('position_lat'),
    2 : LongitudeField('position_long'),
    3 : AltitudeField('enhanced_altitude'),
    4 : SpeedMpsField('enhanced_speed'),
    5 : HeadingField(),
    6 : TimestampField('utc_timestamp', utc=True),
    7 : SpeedMpsField('velocity'),
}
