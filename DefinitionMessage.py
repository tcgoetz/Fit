#!/usr/bin/env python

#
# copyright Tom Goetz
#

import collections, logging

from Data import *
from Field import *
from FieldDefinition import FieldDefinition


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class DefinitionMessage(Data):
    primary_schema = Schema(collections.OrderedDict(
        [ ('reserved', ['UINT8', 1, '%x']), ('architecture', ['UINT8', 1, '%x']) ]
    ))
    secondary_schema = Schema(collections.OrderedDict(
        [ ('global_message_number', ['UINT16', 1, '%x']), ('fields', ['UINT8', 1, '%x']) ]
    ))
    known_messages = {
        0   : [ 'file_id', {
                    0: FileField('type'),
                    1 : ManufacturerField(),
                    2 : ProductField('product'),
                    3 : Field('serial_number'),
                    4: TimestampField('time_created'),
                    5 : Field('number'),
                    7 : StringField('product_name')
                }
            ],
        1   : [ 'capabilities', {} ],
        2   : [ 'device_settings', {
                    0 : Field('active_time_zone'),
                    1 : Field('utc_offset'),
                    2 : Field('time_offset'),
                    4 : TimeModeField(),
                    5 : Field('time_zone_offset'),
                    12 : BacklightModeField(),
                    36 : BoolField('activity_tracker_enabled'),
                    39 : TimestampField('clock_time'),
                    40 : Field('pages_enabled'),
                    46 : BoolField('move_alert_enabled'),
                    47 : DateModeField(),
                    55 : DisplayOrientationField('display_orientation'),
                    56 : SideField(),
                    57 : Field('default_page'),
                    58 : Field('autosync_min_steps'),
                    59 : Field('autosync_min_time'),
                    80 : BoolField('lactate_threshold_autodetect_enabled'),
                    86 : BoolField('ble_auto_upload_enabled'),
                    89 : AutoSyncFrequencyField(),
                    90 : AutoActivityDetectField(),
                    94 : Field('number_of_screens'),
                    95 : DisplayOrientationField('smart_notification_display_orientation'),
                    134 : SwitchField('tap_interface'),
                }
            ],
        3   : [ 'user_profile', {
                    1 : GenderField(),
                    2 : Field('age'),
                    3 : HeightField(),
                    4 : WeightField(),
                    22 : Field('local_id')
                }
            ],
        4   : [ 'hrm_profile', {} ],
        5   : [ 'sdm_profile', {} ],
        6   : [ 'bike_profile', {} ],
        7   : [ 'zones_target', {
                    1 : Field('max_heart_rate'),
                    2 : Field('threshold_heart_rate'),
                    3 : Field('functional_threshold_power'),
                    5 : HeartRateZoneCalcField(),
                    7 : PowerCalcField()
                }
            ],
        8   : [ 'hr_zone', {} ],
        9   : [ 'power_zone', {} ],
        10  : [ 'met_zone', {} ],
        12  : [ 'sport', {
                    0 : SportField('sport'),
                    1 : SubSportField('sub_sport'),
                    3 : StringField('name')
                }
            ],
        15  : [ 'goal', {} ],
        18  : [ 'session', {
                    0 : EventField(),
                    1 : EventTypeField(),
                    2: TimestampField('start_time'),
                    3 : PosField('start_position_lat'),
                    4 : PosField('start_position_long'),
                    5 : SportField(),
                    6 : SubSportField(),
                    7 : TimeMsField('total_elapsed_time'),
                    8 : TimeMsField('total_timer_time'),
                    9 : DistanceField('total_distance'),
                    10 : CyclesField('total_cycles'),
                    11 : CaloriesField('total_calories'),
                    13 : CaloriesField('total_fat_calories'),
                    14 : SpeedField('avg_speed'),
                    15 : SpeedField('max_speed'),
                    16 : Field('avg_heart_rate'),
                    17 : Field('max_heart_rate'),
                    18 : Field('avg_cadence'),
                    19 : Field('max_cadence'),
                    20 : Field('avg_power'),
                    21 : Field('max_power'),
                    22 : DistanceField('total_ascent'),
                    23 : DistanceField('total_descent'),
                    24 : Field('total_training_effect'),
                    25 : Field('first_lap_index'),
                    26 : Field('num_laps'),
                    27 : Field('event_group'),
                    28 : SessionTriggerField(),
                    36 : Field('intensity_factor'),
                    37 : Field('left_right_balance'),
                    41 : Field('avg_stroke_count'),
                    44 : Field('pool_length'),
                    45 : Field('threshold_power'),
                    89 : Field('avg_vertical_oscillation'),
                    90 : Field('avg_stance_time_percent'),
                    91 : Field('avg_stance_time'),
                    92 : Field('avg_fractional_cadence'),
                    93 : Field('max_fractional_cadence'),
                    102 : Field('avg_right_torque_effectiveness'),
                    103 : Field('avg_left_pedal_smoothness'),
                    104 : Field('avg_right_pedal_smoothness'),
                    105 : Field('avg_combined_pedal_smoothness'),
                    116 : Field('avg_left_power_phase'),
                    120 : Field('avg_power_position'),
                    122 : Field('avg_cadence_position'),
                    137 : Field('total_anaerobic_training_effect'),
                }
            ],
        19  : [ 'lap', {
                    0 : EventField(),
                    1 : EventTypeField(),
                    2: TimestampField('start_time'),
                    3 : PosField('start_position_lat'),
                    4 : PosField('start_position_long'),
                    5 : PosField('end_position_lat'),
                    6 : PosField('end_position_long'),
                    7 : TimeMsField('total_elapsed_time'),
                    8 : TimeMsField('total_timer_time'),
                    9 : DistanceField('total_distance'),
                    10 : CyclesField('total_cycles'),
                    11 : CaloriesField('total_calories'),
                    12 : CaloriesField('total_fat_calories'),
                    13 : SpeedField('avg_speed'),
                    14 : SpeedField('max_speed'),
                    15 : Field('avg_heart_rate'),
                    16 : Field('max_heart_rate'),
                    17 : Field('avg_cadence'),
                    18 : Field('max_cadence'),
                    19 : Field('avg_power'),
                    20 : Field('max_power'),                    21 : DistanceField('total_ascent'),
                    22 : DistanceField('total_descent'),
                    24 : LapTriggerField(),
                    25 : SportField()
                }
            ],
        20  : [ 'record', {
                    0 : PosField('position_lat'),
                    1 : PosField('position_long'),
                    2 : AltField('altitude'),
                    3 : HeartRateField('heart_rate'),
                    4 : Field('cadence'),
                    5 : DistanceField('distance'),
                    6 : SpeedField('speed'),
                    13 : Field('temperature'),
                    53 : Field('fractional_cadence'),
                }
            ],
        21  : [ 'event', {
                    0 : EventField('event'),
                    1 : EventTypeField(),
                    2 : Field('data16'),
                    3 : Field('data'),
                    4 : Field('event_group'),
                    7 : Field('score'),
                    8 : Field('opponent_score'),
                    9 : Field('front_gear_num'),
                    10 : Field('front_gear'),
                    11 : Field('rear_gear_num'),
                    12 : Field('rear_gear'),
                    13 : Field('device_index')
                }
            ],
        22  : [ 'source', {} ],
        23  : [ 'device_info', {
                    0 : Field('device_index'),
                    1 : Field('device_type'),
                    2 : ManufacturerField(),
                    3 : Field('serial_number'),
                    4 : ProductField('garmin_product'),
                    5 : VersionField('software_version'),
                    6 : Field('hardware_version'),
                    7 : TimeSField('cum_operating_time'),
                    10 : BatteryVoltageField('battery_voltage'),
                    11 : BatteryStatusField(),
                    18 : BodyLocationField('sensor_position'),
                    19 : StringField('descriptor'),
                    20 : Field('ant_transmission_type'),
                    21 : Field('ant_device_number'),
                    22 : AntNetworkField(),
                    25 : SourceTypeField(),
                    27 : StringField('product_name'),
                }
            ],
        25  : [ 'workout', {} ],
        26  : [ 'workout', { 6 : Field('num_valid_steps'), 8 : StringField('wkt_name'), } ],
        25  : [ 'workout_step', {} ],
        28  : [ 'schedule', {} ],
        29  : [ 'location', {} ],
        30  : [ 'weight_scale', { 0 : WeightField(), 1 : PercentField('percent_fat'), 12 : Field('user_profile_index') } ],
        31  : [ 'course', {} ],
        32  : [ 'course_point', {} ],
        33  : [ 'totals', {} ],
        34  : [ 'activity', {
                    0 : TimeMsField('total_timer_time'),
                    1 : Field('num_sessions'),
                    2 : ActivityField(),
                    3 : EventField(),
                    4 : EventTypeField(),
                    5 : TimestampField('local_timestamp', False),
                    6 : Field('event_group'),
                }
            ],
        35  : [ 'software', { 3 : VersionField('version') } ],
        37  : [ 'file_capabilities', {} ],
        38  : [ 'mesg_capabilities', {} ],
        39  : [ 'field_capabilities', {} ],
        49  : [ 'file_creator', { 0 : VersionField('software_version'), 1 : VersionField('hardware_version')} ],
        51  : [ 'blood_pressure', {} ],
        53  : [ 'speed_zone', {} ],
        55  : [ 'monitoring', {
                    0 : Field('device_index'),
                    1 : CaloriesField('calories'),
                    2 : MonitoringDistanceField(),
                    3 : CyclesBaseField(),
                    4 : CumActiveTimeField(),
                    5 : ActivityTypeField(),
                    19 : ActiveCaloriesField(),
                    24 : ActivityTypeIntensityField('current_activity_type_intensity'),
                    26 : TimeSField('timestamp_16'),
                    27 : HeartRateField('heart_rate'),
                    29 : DurationField(),
                    31 : ClimbField('ascent'),
                    32 : ClimbField('descent'),
                    33 : TimeMinField('moderate_activity_mins'),
                    34 : TimeMinField('vigorous_activity_mins'),
                    35 : ClimbField('cum_ascent'),
                    36 : ClimbField('cum_descent')
                }
            ],
        72  : [ 'training_file', {} ], # timestamp, serial_number, creation_time, product_ID, session_style
        78  : [ 'hrv', {} ],
        80  : [ 'ant_rx', {} ],
        81  : [ 'ant_tx', {} ],
        82  : [ 'ant_channel_id', {} ],
        101 : [ 'length', {} ],
        103 : [ 'monitoring_info', {
                    0 : TimestampField('local_timestamp', False),
                    1 : ActivityTypeField(),
                    3 : CyclesDistanceField(),
                    4 : CyclesCaloriesField(),
                    5 : CaloriesDayField('resting_metabolic_rate')
                }
            ],
        104 : [ 'battery', {} ],
        105 : [ 'pad', {} ],
        106 : [ 'slave_device', {} ],
        127 : [ 'connectivity', {} ],
        128 : [ 'weather_conditions', {} ],
        129 : [ 'weather_alert', {} ],
        131 : [ 'cadence_zone', {} ],
        132 : [ 'hr', {} ],
        142 : [ 'segment_lap', {} ],
        145 : [ 'memo_glob', {} ],
        147 : [ 'sensor', {} ],
        148 : [ 'segment_id', {} ],
        149 : [ 'segment_leaderboard_entry', {} ],
        150 : [ 'segment_point', {} ],
        151 : [ 'segment_file', {} ],
        160 : [ 'gps_metadata', {} ],
        161 : [ 'camera_event', {} ],
        162 : [ 'timestamp_correlation', {} ],
        164 : [ 'gyroscope_data', {} ],
        165 : [ 'accelerometer_data', {} ],
        167 : [ 'three_d_sensor_calibration', {} ],
        169 : [ 'video_frame', {} ],
        174 : [ 'obdii_data', {} ],
        177 : [ 'nmea_sentence', {} ],
        178 : [ 'aviation_attitude', {} ],
        184 : [ 'video', {} ],
        185 : [ 'video_title', {} ],
        186 : [ 'video_description', {} ],
        187 : [ 'video_clip', {} ],
        200 : [ 'exd_screen_configuration', {} ],
        201 : [ 'exd_data_field_configuration', {} ],
        202 : [ 'exd_data_concept_configuration', {} ],
        206 : [ 'field_description', {
                    0 : Field('developer_data_index'),
                    1 : Field('field_definition_number'),
                    2 : FitBaseUnitField('fit_base_type_id'),
                    3 : StringField('field_name'),
                    4 : Field('array'),
                    5 : StringField('components'),
                    6 : Field('scale'),
                    7 : Field('offset'),
                    8 : StringField('units'),
                    9 : StringField('bits'),
                    10 : StringField('accumulate'),
                    13 : FitBaseUnitField('fit_base_unit_id'),
                    14 : Field('native_message_num'),
                    15 : Field('native_field_num')
                }
            ],
        207 : [ 'dev_data_id', {
                    0 : Field('developer_id'),
                    1 : Field('application_id'),
                    2 : ManufacturerField(),
                    3 : Field('developer_data_index'),
                    4 : Field('application_version')
                }
            ],
        208 : [ 'magnetometer_data', {} ],
        209 : [ 'barometer_data', {} ],
        210 : [ 'one_d_sensor_calibration', {} ],
        227 : [ 'stress_level', {
                    0 : Field('stress_level_value'),
                    1 : TimestampField('stress_level_time', False),
                }
            ],
        258 : [ 'dive_settings', {} ],
        259 : [ 'dive_gas', {} ],
        262 : [ 'dive_alarm', {} ],
        264 : [ 'exercise_title', {} ],
        268 : [ 'dive_summary', {} ],
        0xFF00  : 'mfg_range_min',
        0xFFFE  : 'mfg_range_max',
    }
    reserved_field_indexes = {
        250 : Field('part_index'),
        253 : TimestampField(),
        254 : MsssageIndexField()
    }
    architecture_table = { 0 : 'Little Endian', 1 : 'Big Endian'}

    def __init__(self, record_header, file):
        Data.__init__(self, file, DefinitionMessage.primary_schema, DefinitionMessage.secondary_schema)
        self.record_header = record_header

        msg_num = self.message_number()
        if msg_num in DefinitionMessage.known_messages:
            self.message_data = DefinitionMessage.known_messages[msg_num]
        else:
            logger.info("Unknown message number %d: %s" % (msg_num, str(self.decoded_data)))
            self.message_data = ['unknown_msg_' + str(msg_num), {}]

        self.field_definitions = []
        for index in xrange(self.field_count()):
            field_definition = FieldDefinition(file)
            self.file_size += field_definition.file_size
            self.field_definitions.append(field_definition)

    def decode_optional(self):
        self.endian = self.architecture()
        return True

    def architecture(self):
        return self['architecture']

    def architecture_str(self):
        return DefinitionMessage.architecture_table[self.architecture()]

    def field_count(self):
        return self['fields']

    def message_number(self):
        gmn = self['global_message_number']
        if (gmn < 0) or (gmn > 0xFFFE):
            raise ValueError('Definition Message message number out of bounds: %d' % gmn)
        return gmn

    def name(self):
        return self.message_data[0]

    def fields(self):
        return self.message_data[1]

    def field(self, field_number):
        # first check for reserved indexes
        if field_number in DefinitionMessage.reserved_field_indexes:
            field = DefinitionMessage.reserved_field_indexes[field_number]
        else:
            fields = self.fields()
            if field_number in fields:
                field = fields[field_number]
            else:
                field = UnknownField(field_number)
        return (field)

    def __str__(self):
        return ("%s: %s (%d) %d %s fields" %
                (self.__class__.__name__, self.name(), self.message_number(), self.field_count(), self.architecture_str()))
