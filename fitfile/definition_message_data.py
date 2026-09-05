"""Structured data for decoding a FIT file definition message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

from .message_type import MessageType
from .fields import BytesField, NamedField, VersionField, FloatField, IntegerField, TimestampField, TimeMsField, WatchFaceModeField, SleepActivityLevelField, \
    SleepDisruptionsSeveritylField, SwitchField, EnhancedRespirationRateField, MessageIndexField, HeartRateField, HeartRateVarianceField, TemperatureField, TimeSField, \
    TemperatureMilliField, Spo2MeasurementTypeField

from .messages import file_id_message, device_settings_message, user_profile_message, hrm_profile_message, bike_profile_message, zones_target_message, hr_zone_message, \
    power_zone_message, sport_message, data_screen_message, goal_message, alert_message, range_alert_message, session_message, lap_message, record_message, event_message, \
    device_used_message, device_info_message, workout_message, location_message, weight_scale_message, totals_message, activity_message, monitoring_message, \
    file_creator_message, training_file_message, monitoring_info_message, device_status_message, personal_record_message, connectivity_message, activity_metrics_message, \
    epo_status_message, sensor_message, field_description_message, dev_data_id_message, time_in_zone_message, jump_message, split_message, climb_pro_message, \
    hrv_status_summary_message, timestamp_correlation_message, best_effort_message, workout_schedule_message, gps_metadata_message, user_metrics_message, \
    training_settings_message, stress_level_message, sleep_assessment_message, sleep_data_info_message


class DefinitionMessageData():
    """Structured data for decoding a FIT file definition message."""

    known_messages = {
        MessageType.file_id : file_id_message,
        MessageType.capabilities : {},
        MessageType.device_settings : device_settings_message,
        MessageType.user_profile : user_profile_message,
        MessageType.hrm_profile : hrm_profile_message,
        MessageType.sdm_profile : {},
        MessageType.bike_profile : bike_profile_message,
        MessageType.zones_target : zones_target_message,
        MessageType.hr_zone : hr_zone_message,
        MessageType.power_zone : power_zone_message,
        MessageType.met_zone : {},
        MessageType.sport : sport_message,
        MessageType.training_settings : training_settings_message,
        MessageType.data_screen : data_screen_message,
        MessageType.goal : goal_message,
        MessageType.alert : alert_message,
        MessageType.range_alert : range_alert_message,
        MessageType.session : session_message,
        MessageType.lap : lap_message,
        MessageType.record : record_message,
        MessageType.event : event_message,
        MessageType.device_used : device_used_message,
        MessageType.device_info : device_info_message,
        MessageType.unknown_24 : {
            2 : BytesField('data'),
        },
        MessageType.workout : workout_message,
        MessageType.workout_step : {
            18 : NamedField('skip_last_recover'),
            31 : NamedField('workout_index'),
        },
        MessageType.schedule : {},
        MessageType.location : location_message,
        MessageType.weight_scale : weight_scale_message,
        MessageType.course : {},
        MessageType.course_point : {},
        MessageType.totals : totals_message,
        MessageType.activity : activity_message,
        MessageType.software : {
            3 : VersionField()
        },
        MessageType.file_capabilities : {},
        MessageType.mesg_capabilities : {},
        MessageType.field_capabilities : {},
        MessageType.file_creator : file_creator_message,
        MessageType.blood_pressure : {},
        MessageType.speed_zone : {},
        MessageType.monitoring : monitoring_message,
        MessageType.map_layer : {},
        MessageType.routing : {},
        MessageType.training_file : training_file_message,
        MessageType.hrv : {
            0 : TimeMsField('time'),
        },
        MessageType.user_metrics : user_metrics_message,
        MessageType.ant_rx : {},
        MessageType.ant_tx : {},
        MessageType.ant_channel_id : {},
        MessageType.open_water_event : {},
        MessageType.length : {},
        MessageType.monitoring_info : monitoring_info_message,
        MessageType.device_status : device_status_message,
        MessageType.pad : {},
        MessageType.slave_device : {},
        MessageType.best_effort : best_effort_message,
        MessageType.personal_record : personal_record_message,
        MessageType.connectivity : connectivity_message,
        MessageType.weather_conditions : {},
        MessageType.weather_alert : {},
        MessageType.cadence_zone : {},
        MessageType.hr : {},
        MessageType.activity_metrics : activity_metrics_message,
        MessageType.epo_status : epo_status_message,
        MessageType.segment_lap : {},
        MessageType.multisport_settings : {},
        MessageType.multisport_activity : {},
        MessageType.memo_glob : {},
        MessageType.sensor : sensor_message,
        MessageType.segment_id : {},
        MessageType.segment_leaderboard_entry : {},
        MessageType.segment_point : {},
        MessageType.segment_file : {},
        MessageType.metronome : {},
        MessageType.workout_session : {},
        MessageType.watchface_settings : {
            0 : WatchFaceModeField('mode'),
            1 : NamedField('layout'),
        },
        MessageType.gps_metadata : gps_metadata_message,
        MessageType.camera_event : {},
        MessageType.timestamp_correlation : timestamp_correlation_message,
        MessageType.gyroscope_data : {},
        MessageType.accelerometer_data : {},
        MessageType.three_d_sensor_calibration : {},
        MessageType.video_frame : {},
        MessageType.connect_iq_field : {},
        MessageType.clubs : {},
        MessageType.obdii_data : {},
        MessageType.nmea_sentence : {},
        MessageType.aviation_attitude : {},
        MessageType.video : {},
        MessageType.video_title : {},
        MessageType.video_description : {},
        MessageType.video_clip : {},
        MessageType.ohr_settings : {
            0 : SwitchField('enabled'),
        },
        MessageType.waypoint_handling : {},
        MessageType.golf_course : {},
        MessageType.golf_stats : {},
        MessageType.score : {},
        MessageType.hole : {},
        MessageType.shot : {},
        MessageType.exd_screen_configuration : {},
        MessageType.exd_data_field_configuration : {},
        MessageType.exd_data_concept_configuration : {},
        MessageType.field_description : field_description_message,
        MessageType.dev_data_id : dev_data_id_message,
        MessageType.magnetometer_data : {},
        MessageType.barometer_data : {},
        MessageType.one_d_sensor_calibration : {},
        MessageType.monitoring_hr_data : {
            0 : HeartRateField('resting_heart_rate'),
            1 : HeartRateField('current_day_resting_heart_rate'),
        },
        MessageType.time_in_zone : time_in_zone_message,
        MessageType.alarm_settings : {},
        MessageType.set : {},
        MessageType.stress_level : stress_level_message,
        MessageType.max_met_data : {},
        MessageType.metrics_232 : {},
        MessageType.unknown_233 : {
            2 : BytesField('unknown_2'),
        },
        MessageType.local_time : {
            0 : TimestampField('local_timestamp', utc=False)
        },
        MessageType.music_info : {},
        MessageType.dive_settings : {},
        MessageType.dive_gas : {},
        MessageType.dive_alarm : {},
        MessageType.exercise_title : {},
        MessageType.dive_summary : {},
        MessageType.spo2 : {
            0 : FloatField('reading_spo2'),
            1 : IntegerField('reading_confidence'),
            2 : Spo2MeasurementTypeField('mode'),
        },
        MessageType.sleep_data_info : sleep_data_info_message,
        MessageType.sleep_data : {
            0 : BytesField('data'),
        },
        MessageType.sleep_level : {
            0 : SleepActivityLevelField('sleep_level'),
        },
        MessageType.sleep_end : {},
        MessageType.metrics_281 : {
            1 : TimestampField('end', utc=True),
            2 : TimestampField('start', utc=True)
        },
        MessageType.metrics_282 : {},
        MessageType.unknown_284 : {
            1 : TimestampField('ts_1', utc=True),
        },
        MessageType.jump : jump_message,
        MessageType.respiration_rate : {
            0 : EnhancedRespirationRateField(),
        },
        MessageType.aad_accel_features : {},
        MessageType.beat_intervals : {},
        MessageType.metrics_294 : {},
        MessageType.hsa_accelerometer_data : {},
        MessageType.hsa_step_data : {},
        MessageType.hsa_spo2_data : {},
        MessageType.hsa_spo2_data2 : {},
        MessageType.hsa_respiration_data : {},
        MessageType.hsa_heart_rate_data : {},
        MessageType.mtb_cx : {},
        MessageType.race : {},
        MessageType.split_time : {},
        MessageType.split: split_message,
        MessageType.split_summary : {},
        MessageType.hsa_body_battery_data : {},
        MessageType.hsa_event : {},
        MessageType.climb_pro : climb_pro_message,
        MessageType.tank_update : {},
        MessageType.power_mode : {},
        MessageType.tank_summary : {},
        MessageType.gps_event : {},
        MessageType.ecg_summary : {},
        MessageType.ecg_raw_sample : {},
        MessageType.ecg_smooth_sample : {},
        MessageType.metrics_339 : {
            0 : TimestampField('local_time', utc=False),
        },
        MessageType.sleep_assessment : sleep_assessment_message,
        MessageType.functional_metrics : {},
        MessageType.race_event : {},
        MessageType.training_readiness : {},
        MessageType.hrv_status_summary : hrv_status_summary_message,
        MessageType.hrv_value : {
            0 : HeartRateVarianceField()
        },
        MessageType.raw_bbi : {},
        MessageType.device_aux_battery_info : {},
        MessageType.hsa_gyroscope_data : {},
        MessageType.training_load : {},
        MessageType.sleep_schedule : {
            0 : TimeSField('bed_time'),
            1 : TimeSField('wake_time'),
        },
        MessageType.sleep_restless_moments : {
            1 : IntegerField('restless_moments_count'),
            2 : TimeSField('durations'),
        },
        MessageType.chrono_shot_session : {},
        MessageType.chrono_shot_data : {},
        MessageType.hsa_configuration_data : {},
        MessageType.dive_apnea_alarm : {},
        MessageType.cpe_status : {},
        MessageType.skin_temp : {
            1 : TemperatureField(),
        },
        MessageType.skin_temp_overnight : {},
        MessageType.hill_score : {},
        MessageType.endurance_score : {},
        MessageType.unknown_407 : {
            7 : TimestampField('local_timestamp', utc=False),
        },
        MessageType.hsa_wrist_temperature_data : {
            0 : TimeSField('processing_interval'),
            1 : TemperatureMilliField('value')
        },
        MessageType.nap_event : {},
        MessageType.workout_schedule : workout_schedule_message,
        MessageType.sleep_disruption_severity_period : {
            0 : SleepDisruptionsSeveritylField()
        },
        MessageType.sleep_disruption_overnight_severity : {},
        #
        MessageType.metrics_493 : {
            0 : TimestampField('start', utc=True),
            1 : TimestampField('end', utc=True),
            11 : TimestampField('unknown_ts', utc=True),
        },
        #
        MessageType.mfg_range_min : {},
        MessageType.mfg_range_max : {},
    }
    reserved_field_indexes = {
        250 : IntegerField('part_index'),
        253 : TimestampField('timestamp', utc=True),
        254 : MessageIndexField('message_index')
    }

    @classmethod
    def get_message_definition(cls, message_type):
        """Given a message number, return a message definition."""
        return cls.known_messages.get(message_type, {})
