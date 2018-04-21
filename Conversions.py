#!/usr/bin/env python

#
# copyright Tom Goetz
#

import time, datetime


def ms_to_dt_time(time_ms):
    if time_ms is not None:
        return (datetime.datetime.min + datetime.timedelta(0, 0, 0, time_ms)).time()

def secs_to_dt_time(time_secs):
    if time_secs is not None:
        return (datetime.datetime.min + datetime.timedelta(0, time_secs)).time()

def min_to_dt_time(time_mins):
    if time_mins is not None:
        return secs_to_dt_time(time_mins * 60)

def time_to_timedelta(time):
    if time is not None:
        return datetime.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

def timedelta_to_time(timedelta):
    return (datetime.datetime.min + timedelta).time()

def add_time(time1, time2, scale=1):
    return (datetime.datetime.min + time_to_timedelta(time1) + (time_to_timedelta(time2) * scale)).time()

def subtract_time(time1, time2):
    return (datetime.datetime.min + time_to_timedelta(time1) - time_to_timedelta(time2)).time()

def meters_to_feet(meters):
    if meters is not None:
        return (meters * 3.2808399)

def day_of_the_year_to_datetime(year, day):
    return datetime.datetime(year, 1, 1) + datetime.timedelta(day - 1)

def centimeters_to_meters(centimeters):
    if centimeters is not None:
        return (centimeters * 100.0)

def meters_to_miles(meters):
    if meters is not None:
        return meters_to_feet(meters) / 5280.0

def mps_to_mph(meters_per_sec):
    if meters_per_sec is not None:
        return meters_per_sec * 2.236936

def celsius_to_fahrenheit(celsius):
    if celsius is not None:
        return (celsius * 1.8) + 32.0
