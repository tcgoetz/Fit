"""Objects that represent FIT file time fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import datetime

from ..conversions import ms_to_dt_time, hours_to_dt_time, min_to_dt_time, secs_to_dt_time
from . import Field, NamedField


class TimestampField(NamedField):

    _utc = None

    def _convert_single(self, value, invalid):
        if self._utc:
            return datetime.datetime(1989, 12, 31, 0, 0, 0, tzinfo=datetime.timezone.utc) + datetime.timedelta(seconds=value)
        return datetime.datetime(1989, 12, 31, 0, 0, 0) + datetime.timedelta(seconds=value)


class TimeMsField(NamedField):
    """A field holsing milliseconds returned as a datetime."""

    def _convert_single(self, value, invalid):
        if value != invalid:
            return ms_to_dt_time(value / self._scale)


class TimeSField(NamedField):
    """A field holding an integer number of seconds."""

    _units = 's'

    # invalid is not allowed, 65535 is a valid value
    def _convert_single(self, value, invalid):
        return value


class TimeOffsetField(Field):

    _name = 'time_offset'
    _units = 's'

    def _convert_single(self, value, invalid):
        # if the offset is greater than 24 hours, than it's negative
        if value <= 86400:
            return value
        if value >= 4294880895:
            return -(0xFFFFFFFF - value + 1)
        return datetime.datetime.now(datetime.timezone.utc).astimezone().utcoffset().total_seconds()


class TimeHourField(TimeMsField):
    """A field that holds a time value measured in milliseconds."""

    def _convert_single(self, milliseconds, invalid):
        if milliseconds != invalid:
            return hours_to_dt_time(milliseconds / self._scale)


class TimeMinField(TimeMsField):
    """A field that holds a time value measured in minutes."""

    def _convert_single(self, minutes, invalid):
        if minutes != invalid:
            return min_to_dt_time(minutes / self._scale)


class TimeOfDayField(NamedField):
    """A field that holds a time value measured in seconds."""

    def _convert_single(self, seconds, invalid):
        if seconds != invalid:
            return secs_to_dt_time(seconds)
