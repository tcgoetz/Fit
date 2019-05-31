#!/usr/bin/env python

#
# copyright Tom Goetz
#

from Metric import *
from FieldEnums import *


class Speed(Metric):
    def __init__(self, meters_per_sec, raw_value, invalid_value):
        super(Speed, self).__init__(raw_value, invalid_value, self.to_mph, 'mph')
        self.meters_per_sec = meters_per_sec

    @classmethod
    def from_mps(cls, meters_per_sec, invalid_value=None):
        return cls(meters_per_sec, meters_per_sec, invalid_value)

    @classmethod
    def from_cps(cls, centimeters_per_sec, invalid_value=None):
        return cls(centimeters_per_sec / 100.0, centimeters_per_sec, invalid_value)

    @classmethod
    def from_mmps(cls, mm_per_sec, invalid_value=None):
        return cls(mm_per_sec / 1000.0, mm_per_sec, invalid_value)

    def to_kph(self):
        return ((self.meters_per_sec * (60 * 60)) / 1000.0)

    def to_mph(self):
        return (self.meters_per_sec * 2.236936)

    @classmethod
    def kph_or_mph(cls, speed, measurement_system=DisplayMeasure.metric):
        return speed.kph_or_mph(measurement_system)

    def kph_or_mph(self, measurement_system=DisplayMeasure.metric):
        if self.meters_per_sec is not None:
            return self.to_kph() if measurement_system is DisplayMeasure.metric else self.to_mph()
