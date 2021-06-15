"""Enums that represent FIT file message file type field values."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

from .field_enums import FieldEnum


class FileType(FieldEnum):
    """Garmin defined values."""

    unknown0                    = 0
    device                      = 1
    settings                    = 2
    sport_settings              = 3
    activity                    = 4
    workout                     = 5
    course                      = 6
    schedules                   = 7
    weight                      = 9
    totals                      = 10
    goals                       = 11
    blood_pressure              = 14
    monitoring_a                = 15
    activity_summary            = 20
    monitoring_daily            = 28
    records                     = 29
    monitoring_b                = 32
    segment                     = 34
    segment_list                = 35
    exd_configuration           = 40
    metrics                     = 44
    sleep                       = 49
    unknown_file_type_64        = 64
    manufacturer_range_start    = 0xfe
    invalid                     = 255
