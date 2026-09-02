"""Structured data for decoding a FIT file sport message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import NamedField, TimestampField, IntegerField


stress_level_message = {
    0 : NamedField('stress_level'),
    1 : TimestampField('local_timestamp', utc=False),
    3 : IntegerField('body_battery'),
}
