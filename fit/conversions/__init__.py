"""Library for parsing FIT files and returning them as lists of messages dictionaries."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

# flake8: noqa

from .conversions import ms_to_dt_time, secs_to_dt_time, min_to_dt_time, hours_to_dt_time, time_to_secs, time_to_timedelta, timedelta_to_time, add_time, subtract_time, day_of_the_year_to_datetime, meters_to_feet, meters_to_miles, mps_to_mph, celsius_to_fahrenheit, date_to_dt, dt_to_epoch_ms, dt_to_utc_epoch_ms, printable, perhour_speed_to_pace
