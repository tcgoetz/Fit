"""Structured data for decoding a FIT file messages."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

# flake8: noqa

from .activity import activity_message, activity_metrics_message, best_effort_message, workout_schedule_message, user_metrics_message
from .alert import alert_message
from .bike_profile import bike_profile_message
from .climb_pro import climb_pro_message
from .connectivity import connectivity_message
from .data_screen import data_screen_message
from .dev import field_description_message, dev_data_id_message
from .device import device_info_message, device_status_message, device_settings_message, device_used_message, epo_status_message, gps_metadata_message
from .event import event_message
from .file_id import file_id_message
from .file_creator import file_creator_message
from .goal import goal_message
from .heart_rate import hrm_profile_message, hr_zone_message, time_in_zone_message, hrv_status_summary_message
from .jump import jump_message
from .lap import lap_message
from .location import location_message
from .monitoring import monitoring_message
from .monitoring_info import monitoring_info_message
from .personal_record import personal_record_message
from .power_zone import power_zone_message
from .range_alert import range_alert_message
from .record import record_message
from .sensor import sensor_message
from .session import session_message
from .sleep import sleep_assessment_message, sleep_assessment_message
from .split import split_message
from .sport import sport_message
from .stress import stress_level_message
from .timestamp_correlation import timestamp_correlation_message
from .totals import totals_message
from .training import training_settings_message, training_file_message
from .user_profile import user_profile_message
from .weight_scale import weight_scale_message
from .workout import workout_message
from .zones_target import zones_target_message
