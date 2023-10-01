"""Methods for converting metrics from one representation to another."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import datetime
import string


def ms_to_dt_time(time_ms):
    """Convert time in milli seconds to a datetime object."""
    if time_ms is not None:
        return (datetime.datetime.min + datetime.timedelta(milliseconds=time_ms)).time()


def secs_to_dt_time(time_secs):
    """Convert time in seconds to a datetime object."""
    if time_secs is not None:
        return (datetime.datetime.min + datetime.timedelta(seconds=time_secs)).time()


def min_to_dt_time(time_mins):
    """Convert time in minutes to a datetime object."""
    if time_mins is not None:
        return (datetime.datetime.min + datetime.timedelta(minutes=time_mins)).time()


def hours_to_dt_time(time_hours):
    """Convert time in hours to a datetime object."""
    if time_hours is not None:
        return (datetime.datetime.min + datetime.timedelta(hours=time_hours)).time()


def time_to_secs(time):
    """Convert a datetime time object to seconds."""
    if time is not None:
        return (((time.hour * 60) + time.minute) * 60) + time.second


def time_to_timedelta(time):
    """Convert a datetime time object to timedelta object."""
    if time is not None:
        return datetime.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)


def timedelta_to_time(timedelta):
    """Convert a timedelta object to datetime time object."""
    return (datetime.datetime.min + timedelta).time()


def add_time(time1, time2, scale=1):
    """Add two datetime time values, treating both as elapsed time."""
    return (datetime.datetime.min + time_to_timedelta(time1) + (time_to_timedelta(time2) * scale)).time()


def subtract_time(time1, time2):
    """Subtract two datetime time values, treating both as elapsed time."""
    return (datetime.datetime.min + time_to_timedelta(time1) - time_to_timedelta(time2)).time()


def day_of_the_year_to_datetime(year, day):
    """Given the index of a day within the year, return a datetime object."""
    return datetime.datetime(year, 1, 1) + datetime.timedelta(day - 1)


def meters_to_feet(meters):
    """Convert meters to feet."""
    if meters is not None:
        return (meters * 3.2808399)


def meters_to_miles(meters):
    """Convert meters to miles."""
    if meters is not None:
        return meters_to_feet(meters) / 5280.0


def mps_to_mph(meters_per_sec):
    """Convert meters per second to miles per hour."""
    if meters_per_sec is not None:
        return meters_per_sec * 2.236936


def celsius_to_fahrenheit(celsius):
    """Convert celsius_to_fahrenheit to fahrenheit."""
    if celsius is not None:
        return (celsius * 1.8) + 32.0


def date_to_dt(date):
    """Given a datetime date object, return a date time datetime object for the given date at 00:00:00."""
    return datetime.datetime.combine(date, datetime.time.min)


def dt_to_epoch_ms(dt):
    """Convert a datetime object to milliseconds since the epoch."""
    return int((dt - datetime.datetime.fromtimestamp(0)).total_seconds() * 1000)


def dt_to_utc_epoch_ms(dt):
    """Convert a UTC datetime object to milliseconds since the epoch."""
    return int((dt - datetime.datetime.utcfromtimestamp(0)).total_seconds() * 1000)


def printable(string_in):
    """Return a string with only prinatable characters given a string with potentially unprintable characters."""
    if string_in is not None:
        return "".join(filter(lambda x: x in string.printable, string_in))


def persec_speed_to_pace(speed):
    """Convert a per second speed to a per distance pace."""
    if speed:
        # secs_per_hour / speed_per_hour = speed_per
        return (datetime.datetime.min + datetime.timedelta(seconds=(3600 / speed))).time()


def perhour_speed_to_pace(speed):
    """Convert a per second speed to a per distance pace."""
    if speed:
        # secs_per_hour / speed_per_hour = speed_per
        return (datetime.datetime.min + datetime.timedelta(seconds=(3600 / speed))).time()
