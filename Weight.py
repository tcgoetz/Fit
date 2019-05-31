#!/usr/bin/env python

#
# copyright Tom Goetz
#

from Metric import *
from FieldEnums import *


class Weight(Metric):
    def __init__(self, kgs, raw_value, invalid_value):
        super(Weight, self).__init__(raw_value, invalid_value, self.to_lbs, 'lbs')
        self.kgs = kgs

    @classmethod
    def from_grams(cls, grams, invalid_value=None):
        return cls(grams / 1000.0, grams, invalid_value)

    @classmethod
    def from_cgs(cls, centigrams, invalid_value=None):
        return cls(centigrams / 10.0, centigrams, invalid_value)

    @classmethod
    def from_lbs(cls, lbs, invalid_value=None):
        return cls(lbs / 2.204623, lbs, invalid_value)

    def to_kgs(self):
        return self.kgs

    def to_lbs(self):
        return (self.kgs * 2.204623)

    @classmethod
    def kgs_or_lbs(cls, weight, measurement_system=DisplayMeasure.metric):
        return weight.kgs_or_lbs(measurement_system)

    def kgs_or_lbs(self, measurement_system=DisplayMeasure.metric):
        if self.kgs is not None:
            return self.to_kgs() if measurement_system is DisplayMeasure.metric else self.to_lbs()
