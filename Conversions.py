#!/usr/bin/env python

#
# copyright Tom Goetz
#

import time, datetime


def ms_to_dt_time(time_ms):
    if time_ms is not None:
        return (datetime.datetime.min + datetime.timedelta(0, 0, 0, time_ms)).time()
    return None

def secs_to_dt_time(time_secs):
    if time_secs is not None:
        return (datetime.datetime.min + datetime.timedelta(0, time_secs)).time()
    return None

def min_to_dt_time(time_mins):
    if time_mins is not None:
        return secs_to_dt_time(time_mins * 60)
    return None

def time_to_timedelta(time):
    if time is None:
        return None
    return datetime.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

def add_time(time1, time2, scale=1):
    return (datetime.datetime.min + time_to_timedelta(time1) + (time_to_timedelta(time2) * scale)).time()

def meters_to_feet(meters):
    if meters is not None:
        return (meters * 3.2808399)
    return None

def day_of_the_year_to_datetime(year, day):
    return datetime.datetime(year, 1, 1) + datetime.timedelta(day - 1)

def centimeters_to_meters(centimeters):
    if centimeters is None:
        return None
    return (centimeters * 100.0)

def meters_to_miles(meters):
    if meters is not None:
        return meters_to_feet(meters) / 5280.0
    return None
