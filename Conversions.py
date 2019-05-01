#!/usr/bin/env python

#
# copyright Tom Goetz
#

import time, datetime, string


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

def date_to_dt(date):
    return datetime.datetime.combine(date, datetime.time.min)

def dt_to_epoch_ms(dt):
    return int((dt - datetime.datetime.fromtimestamp(0)).total_seconds() * 1000)

def epoch_ms_to_dt(epoch_ms):
    return datetime.datetime.fromtimestamp(epoch_ms / 1000.0)

def dt_to_utc_epoch_ms(dt):
    return int((dt - datetime.datetime.utcfromtimestamp(0)).total_seconds() * 1000)

def epoch_ms_to_utc_dt(epoch_ms):
    return datetime.datetime.utcfromtimestamp(epoch_ms / 1000.0).replace(tzinfo=from_zone)

def printable(string_in):
    return filter(lambda x: x in string.printable, string_in)

def speed_to_pace(speed):
    if speed:
        # secs_per_hour / speed_per_hour = speed_per
        return (datetime.datetime.min +  datetime.timedelta(0, 3600 / speed)).time()


class Temperature(object):
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_celsius(cls, celsius):
        return cls(celsius)

    def to_f(self):
        return (self.celsius * 1.8) + 32.0

    @classmethod
    def c_or_f(cls, temperature, metric):
        return temperature.c_or_f(metric)

    def c_or_f(self, metric):
        if self.celsius is not None:
            return self.celsius if metric else self.to_f()

    def __repr__(self):
        return self.__class__.__name__ + '(' + str(self.celsius) + ' celsius)'

    def __str__(self):
        return self.__repr__()


#####


class Weight(object):
    def __init__(self, kgs):
        self.kgs = kgs

    @classmethod
    def from_grams(cls, grams):
        return cls(grams / 1000.0)

    @classmethod
    def from_cgs(cls, centigrams):
        return cls(centigrams / 10.0)

    @classmethod
    def from_lbs(cls, lbs):
        return cls(lbs / 2.204623)

    def to_kgs(self):
        return self.kgs

    def to_lbs(self):
        return (self.kgs * 2.204623)

    @classmethod
    def kgs_or_lbs(cls, weight, metric):
        return weight.kgs_or_lbs(metric)

    def kgs_or_lbs(self, metric):
        if self.kgs is not None:
            return self.to_kgs() if metric else self.to_lbs()

    def __repr__(self):
        return self.__class__.__name__ + '(' + str(self.kgs) + ' kgs)'

    def __str__(self):
        return self.__repr__()


class Distance(object):
    def __init__(self, meters):
        self.meters = meters

    @classmethod
    def from_meters(cls, meters):
        return cls(meters)

    @classmethod
    def from_cm(cls, cm):
        return cls(cm / 100.0)

    @classmethod
    def from_mm(cls, mm):
        return cls(mm / 1000.0)

    @classmethod
    def from_feet(cls, feet):
        return cls(feet / 3.2808399)

    def to_mm(self):
        return self.meters * 1000.0

    def to_meters(self):
        return self.meters

    def to_kms(self):
        return (self.meters / 1000.0)

    def to_inches(self):
        return (self.meters * 39.37008)

    def to_feet(self):
        return (self.meters * 3.2808399)

    def to_miles(self):
        return (self.meters * 0.0006213712)

    @classmethod
    def mm_or_inches(cls, distance, metric):
        return distance.mm_or_inches(metric)

    def mm_or_inches(self, metric):
        if self.meters is not None:
            return self.to_mm() if metric else self.to_inches()

    @classmethod
    def meters_or_feet(cls, distance, metric):
        return distance.meters_or_feet(metric)

    def meters_or_feet(self, metric):
        if self.meters is not None:
            return self.to_meters() if metric else self.to_feet()

    @classmethod
    def kms_or_miles(cls, distance, metric):
        return distance.kms_or_miles(metric)

    def kms_or_miles(self, metric):
        if self.meters is not None:
            return self.to_kms() if metric else self.to_miles()

    def __repr__(self):
        return self.__class__.__name__ + '(' + str(self.meters) + ' meters)'

    def __str__(self):
        return self.__repr__()


class Speed(object):
    def __init__(self, meters_per_sec):
        self.meters_per_sec = meters_per_sec

    @classmethod
    def from_mps(cls, meters_per_sec):
        return cls(meters_per_sec)

    @classmethod
    def from_cps(cls, centimeters_per_sec):
        return cls(centimeters_per_sec / 100.0)

    @classmethod
    def from_mmps(cls, mm_per_sec):
        return cls(mm_per_sec / 1000.0)

    def to_kph(self):
        return ((self.meters_per_sec * (60 * 60)) / 1000.0)

    def to_mph(self):
        return (self.meters_per_sec * 2.236936)

    @classmethod
    def kph_or_mph(cls, speed, metric):
        return speed.kph_or_mph(metric)

    def kph_or_mph(self, metric):
        if self.meters_per_sec is not None:
            return self.to_kph() if metric else self.to_mph()

    def __repr__(self):
        return self.__class__.__name__ + '(' + str(self.meters_per_sec) + ' meters per sec)'

    def __str__(self):
        return self.__repr__()


class Position(object):
    def __init__(self, semicircles):
        self.semicircles = semicircles

    @classmethod
    def from_semicircles(cls, semicircles):
        return cls(semicircles)

    @classmethod
    def to_degrees(cls, position, metric):
        return position.to_degrees(metric)

    def to_degrees(self, metric):
        return (self.semicircles  / 11930326.891)


class Latitude(Position):
    pass


class Longitude(Position):
    pass
