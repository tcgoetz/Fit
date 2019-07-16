#
# copyright Tom Goetz
#

from Metric import Metric
from FieldEnums import DisplayMeasure


class Temperature(Metric):
    def __init__(self, celsius, raw_value, invalid_value):
        super(Temperature, self).__init__(raw_value, invalid_value, self.to_f, 'F')
        self.celsius = celsius

    @classmethod
    def from_celsius(cls, celsius, invalid_value=None):
        return cls(celsius, celsius, invalid_value)

    def to_f(self):
        return (self.celsius * 1.8) + 32.0

    @classmethod
    def c_or_f(cls, temperature, measurement_system=DisplayMeasure.metric):
        return temperature.c_or_f(measurement_system)

    def c_or_f(self, measurement_system=DisplayMeasure.metric):
        if self.celsius is not None:
            return self.celsius if measurement_system is DisplayMeasure.metric else self.to_f()
