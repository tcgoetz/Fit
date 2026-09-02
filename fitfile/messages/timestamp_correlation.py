"""Structured data for decoding a FIT file timestamp_correlation message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import TimeSField, TimestampField, TimeMsField


timestamp_correlation_message = {
    0 : TimeSField('fractional_timestamp'),
    1 : TimestampField('system_timestamp', utc=True),
    2 : TimeSField('fractional_system_timestamp'),
    3 : TimestampField('local_timestamp', utc=False),
    4 : TimeMsField('timestamp_ms'),
    5 : TimeMsField('timestamp_ms'),
}
