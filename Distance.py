#!/usr/bin/env python

#
# copyright Tom Goetz
#

from Metric import *
from FieldEnums import *


class Distance(Metric):
    def __init__(self, meters, raw_value, invalid_value):
        super(Distance, self).__init__(raw_value, invalid_value, self.to_meters, 'meters')
        self.meters = meters

    @classmethod
    def from_meters(cls, meters, invalid_value=None):
        return cls(meters, meters, invalid_value)

    @classmethod
    def from_cm(cls, cm, invalid_value=None):
        return cls(cm / 100.0, cm, invalid_value)

    @classmethod
    def from_mm(cls, mm, invalid_value=None):
        return cls(mm / 1000.0, mm, invalid_value)

    @classmethod
    def from_feet(cls, feet, invalid_value=None):
        return cls(feet / 3.2808399, feet, invalid_value)

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
    def mm_or_inches(cls, distance, measurement_system=DisplayMeasure.metric):
        return distance.mm_or_inches(measurement_system)

    def mm_or_inches(self, measurement_system=DisplayMeasure.metric):
        if self.meters is not None:
            return self.to_mm() if measurement_system is DisplayMeasure.metric else self.to_inches()

    @classmethod
    def meters_or_feet(cls, distance, measurement_system=DisplayMeasure.metric):
        return distance.meters_or_feet(measurement_system)

    def meters_or_feet(self, measurement_system=DisplayMeasure.metric):
        if self.meters is not None:
            return self.to_meters() if measurement_system is DisplayMeasure.metric else self.to_feet()

    @classmethod
    def kms_or_miles(cls, distance, measurement_system=DisplayMeasure.metric):
        return distance.kms_or_miles(measurement_system)

    def kms_or_miles(self, measurement_system=DisplayMeasure.metric):
        if self.meters is not None:
            return self.to_kms() if measurement_system is DisplayMeasure.metric else self.to_miles()
