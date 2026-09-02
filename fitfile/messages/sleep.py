"""Structured data for decoding a FIT file split message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import IntegerField


sleep_assessment_message = {
    0 : IntegerField('combined_awake_score'),
    1 : IntegerField('awake_time_score'),
    2 : IntegerField('awakenings_count_score'),
    3 : IntegerField('sleep_duration_score'),
    4 : IntegerField('light_sleep_score'),
    5 : IntegerField('overall_sleep_score'),
    6 : IntegerField('overall_sleep_score'),
    7 : IntegerField('sleep_quality_score'),
    8 : IntegerField('sleep_recovery_score'),
    9 : IntegerField('rem_sleep_score'),
    10 : IntegerField('sleep_restlessness_score'),
    11 : IntegerField('awakenings_count'),
    #
    14 : IntegerField('interruptions_score'),
    15 : IntegerField('average_stress_during_sleep', scale=100),
}
