"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import Enum


#
# Some undocumented values from https://medium.com/@harry_90407/beyond-the-fit-sdk-c9969430aeeb
#


class FileType(Enum):
    """Garmin defined values."""

    unknown0                    = 0
    device                      = 1
    settings                    = 2
    sport                       = 3
    activity                    = 4
    workout                     = 5
    course                      = 6
    schedules                   = 7
    locations                   = 8
    weight                      = 9
    totals                      = 10
    goals                       = 11
    blood_pressure              = 14
    monitoring_a                = 15
    activity_summary            = 20
    monitoring_daily            = 28
    records                     = 29
    monitoring_b                = 32
    multi_sport                 = 33
    segment                     = 34
    segment_list                = 35
    clubs                       = 37
    score_card                  = 38
    exd_configuration           = 40
    metrics                     = 44
    sleep                       = 49
    chrono_shot_session         = 54
    pace_band                   = 56
    ecg                         = 61
    unknown_file_type_64        = 64
    calendar                    = 65
    hrv_status                  = 68
    lha_backup                  = 72
    skin_temp                   = 73
    ptd_backup                  = 74
    schedule                    = 77
    sleep_disruptions           = 79
    manufacturer_range_start    = 0xfe
    invalid                     = 255
