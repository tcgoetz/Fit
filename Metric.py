#!/usr/bin/env python

#
# copyright Tom Goetz
#



class Metric(object):
    def __init__(self, raw_value, invalid_value, default_output_func=None, default_output_units=None):
        self.raw_value = raw_value
        self.invalid_value = invalid_value
        self.default_output_func = default_output_func
        self.default_output_units = default_output_units

    def is_invalid(self):
        return (self.raw_value == self.invalid_value)

    def __repr__(self):
        if self.is_invalid():
            value = 'invalid'
        else:
            value = '%s %s [%s]' % (self.default_output_func(), self.default_output_units, str(self.raw_value))
        return self.__class__.__name__ + '(' + value + ')'

    def __str__(self):
        return self.__repr__()
