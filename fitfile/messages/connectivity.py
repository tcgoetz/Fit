"""Structured data for decoding a FIT file connectivity message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import BoolField, StringField


connectivity_message = {
    0 : BoolField('bluetooth_enabled'),
    1 : BoolField('bluetooth_le_enabled'),
    2 : BoolField('ant_enabled'),
    3 : StringField('name'),
    4 : BoolField('live_tracking_enabled'),
    5 : BoolField('weather_conditions_enabled'),
    6 : BoolField('weather_alerts_enabled'),
    7 : BoolField('auto_activity_upload_enabled'),
    8 : BoolField('course_download_enabled'),
    9 : BoolField('workout_download_enabled'),
    10 : BoolField('gps_ephemeris_download_enabled'),
    11 : BoolField('incident_detection_enabled'),
    12 : BoolField('grouptrack_enabled'),
}
